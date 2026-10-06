"""Security regression tests: sandboxes, chat IDOR/XSS, avatar, follow, badges."""

from __future__ import annotations

import io

from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings
from django.urls import reverse
from PIL import Image

from apps.badges.models import Badge, UserBadge
from apps.sandbox.exceptions import ForbiddenSQLError, QueryTimeoutError
from apps.sandbox.python_executor import python_executor
from apps.sandbox.python_safe import run_user_code, validate_python_source, UnsafePythonError
from apps.sandbox.security import validate_student_sql
from apps.social.services import avatar as avatar_svc
from apps.social.services import chat as chat_svc
from apps.social.services.relations import SocialRelationError, follow

User = get_user_model()


def _user(username: str):
    return User.objects.create_user(
        email=f"{username}@example.com",
        password="Pass123!",
        username=username,
        first_name=username.title(),
        role=User.Role.STUDENT,
    )


def _png(size=(64, 64)):
    buf = io.BytesIO()
    Image.new("RGB", size, (10, 20, 30)).save(buf, format="PNG")
    return buf.getvalue()


class PythonSandboxSecurityTests(TestCase):
    def test_blocks_os_subprocess_open_import(self):
        for src in (
            "import os",
            "import subprocess",
            'open("x.txt")',
            '__import__("os")',
            "import socket",
        ):
            out, err, code = run_user_code(src)
            self.assertNotEqual(code, 0, msg=src)

    def test_blocks_popen_subclass_escape(self):
        evil = (
            "subs = ().__class__.__bases__[0].__subclasses__()\n"
            "Popen = [c for c in subs if getattr(c,'__name__','') == 'Popen'][0]\n"
            "r = Popen(['echo','PWNED'], stdout=-1)\n"
            "print(r.communicate()[0])\n"
        )
        with self.assertRaises(UnsafePythonError):
            validate_python_source(evil)
        out, err, code = run_user_code(evil)
        self.assertNotEqual(code, 0)
        self.assertNotIn(b"PWNED", (out or "").encode("utf-8", errors="ignore"))
        self.assertNotIn("PWNED", out or "")

    def test_blocks_getattr_class_escape(self):
        evil = 'print(getattr([], "__class__"))'
        out, err, code = run_user_code(evil)
        self.assertNotEqual(code, 0)

    def test_blocks_pandas_read_csv(self):
        out, err, code = run_user_code(
            "import pandas as pd\n"
            "print(pd.read_csv(r'C:\\\\Windows\\\\win.ini', header=None).head())\n"
        )
        self.assertNotEqual(code, 0)
        self.assertNotIn("16-bit", out or "")

    def test_allows_pandas_dataframe_in_memory(self):
        out, err, code = run_user_code(
            "import pandas as pd\n"
            "df = pd.DataFrame({'a':[1,2]})\n"
            "print(df['a'].sum())\n"
        )
        self.assertEqual(code, 0, msg=err)
        self.assertIn("3", out)

    def test_allows_type_check_not_metaclass(self):
        out2, err2, code2 = run_user_code("print(type(123))")
        self.assertEqual(code2, 0, msg=err2)
        out3, err3, code3 = run_user_code("type('Evil', (), {})")
        self.assertNotEqual(code3, 0)

    @override_settings(PYTHON_SANDBOX_TIMEOUT_SECONDS=1)
    def test_executor_timeout_on_infinite_loop(self):
        with self.assertRaises(QueryTimeoutError):
            python_executor.execute("while True:\n    pass")


class SQLSandboxSecurityTests(TestCase):
    def test_blocks_destructive_and_extension(self):
        blocked = [
            "DROP TABLE customers",
            "DELETE FROM customers",
            "UPDATE customers SET name='x'",
            "INSERT INTO customers(name) VALUES('x')",
            "CREATE TABLE x(a INT)",
            "ALTER TABLE customers ADD COLUMN x INT",
            "SELECT load_extension('x')",
            "SELECT writefile('a','b')",
            "ATTACH DATABASE 'evil.db' AS evil",
            "PRAGMA table_info(customers)",
        ]
        for sql in blocked:
            with self.assertRaises(ForbiddenSQLError, msg=sql):
                validate_student_sql(sql, 8000)

    def test_blocks_pragma_tables_and_spaced_funcs(self):
        for sql in (
            "SELECT * FROM pragma_database_list",
            "SELECT name FROM sqlite_master",
            "SELECT load_extension ('x')",
            "SELECT pg_read_file ('/etc/passwd')",
        ):
            with self.assertRaises(ForbiddenSQLError, msg=sql):
                validate_student_sql(sql, 8000)

    def test_sqlite_recursive_cte_times_out(self):
        from apps.sandbox.exceptions import QueryTimeoutError
        from apps.sandbox.executor import sql_executor

        with self.assertRaises(QueryTimeoutError):
            sql_executor.execute(
                "WITH RECURSIVE t(n) AS (SELECT 1 UNION ALL SELECT n+1 FROM t) "
                "SELECT n FROM t WHERE n < 0"
            )


class ChatSecurityTests(TestCase):
    def setUp(self):
        cache.clear()
        self.a = _user("seca")
        self.b = _user("secb")
        self.c = _user("secc")

    def test_idor_chat_history(self):
        conv = chat_svc.get_or_create_conversation(self.a, self.b)
        chat_svc.send_message(self.a, conv, "secret-for-ab")
        client = Client()
        client.force_login(self.c)
        resp = client.get(reverse("social:chat_history", args=[conv.pk]))
        self.assertEqual(resp.status_code, 404)
        self.assertNotContains(resp, "secret-for-ab", status_code=404)

    def test_xss_message_escaped_in_html(self):
        conv = chat_svc.get_or_create_conversation(self.a, self.b)
        payload = "<script>alert(1)</script>"
        chat_svc.send_message(self.a, conv, payload)
        client = Client()
        client.force_login(self.b)
        resp = client.get(reverse("social:chat_detail", args=[conv.pk]))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "&lt;script&gt;")
        self.assertNotContains(resp, "<script>alert(1)</script>")

    def test_cannot_edit_other_profile(self):
        client = Client()
        client.force_login(self.a)
        resp = client.post(
            reverse("social:settings"),
            {
                "action": "bio",
                "bio": "hacked by A",
            },
        )
        self.assertEqual(resp.status_code, 302)
        # B's bio unchanged / A only updates own social profile
        from apps.social.models import SocialProfile

        a_bio = SocialProfile.objects.get(user=self.a).bio
        self.assertEqual(a_bio, "hacked by A")
        b_profile, _ = SocialProfile.objects.get_or_create(user=self.b)
        self.assertNotEqual(b_profile.bio, "hacked by A")


class FollowAvatarBadgeSecurityTests(TestCase):
    def setUp(self):
        self.a = _user("fa")
        self.b = _user("fb")

    def test_self_follow_blocked(self):
        with self.assertRaises(SocialRelationError):
            follow(self.a, self.a)

    def test_avatar_rejects_exe_and_huge_dims(self):
        exe = SimpleUploadedFile("evil.exe", b"MZ\x00\x00notanimage", content_type="image/png")
        with self.assertRaises(ValidationError):
            avatar_svc.upload_avatar(self.a, exe)

        # Oversized dimensions
        big = SimpleUploadedFile(
            "huge.png",
            _png(size=(5000, 5000)),
            content_type="image/png",
        )
        with override_settings(SOCIAL_AVATAR_MAX_DIMENSION=1024, SOCIAL_AVATAR_MAX_PIXELS=1_000_000):
            with self.assertRaises(ValidationError):
                avatar_svc.upload_avatar(self.a, big)

        ok = SimpleUploadedFile("ok.png", _png(), content_type="image/png")
        profile = avatar_svc.upload_avatar(self.a, ok)
        self.assertTrue(profile.avatar_image.name.endswith(".webp"))

    def test_cannot_self_award_badge_via_api(self):
        badge, _ = Badge.objects.get_or_create(
            slug="first-step",
            defaults={
                "name": "First Step",
                "description": "x",
                "category": Badge.Category.PROBLEM,
                "requirement_type": Badge.RequirementType.PROBLEMS_SOLVED,
                "requirement_value": 1,
                "sort_order": 1,
            },
        )
        client = Client()
        client.force_login(self.a)
        # No public award endpoint — toast pop only returns existing
        resp = client.get(reverse("badges:toasts"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(UserBadge.objects.filter(user=self.a, badge=badge).count(), 0)
        # Direct POST to achievements must not create badges
        resp = client.post(reverse("badges:achievements", args=[self.a.username]), {"badge": badge.slug})
        self.assertIn(resp.status_code, (200, 405))
        self.assertEqual(UserBadge.objects.filter(user=self.a, badge=badge).count(), 0)


class BlockPrivacyTests(TestCase):
    def setUp(self):
        cache.clear()
        self.a = _user("blka")
        self.b = _user("blkb")
        from apps.social.services.relations import block

        block(self.a, self.b)

    def test_blocked_profile_hides_learning_data(self):
        client = Client()
        client.force_login(self.b)
        resp = client.get(reverse("social:profile", args=[self.a.username]))
        self.assertEqual(resp.status_code, 403)
        self.assertNotContains(resp, "O‘qish statistikasi", status_code=403)
        self.assertNotContains(resp, "Faoliyat", status_code=403)

    def test_blocked_activity_and_followers_hidden(self):
        client = Client()
        client.force_login(self.b)
        self.assertEqual(
            client.get(reverse("social:activity_month", args=[self.a.username])).status_code,
            404,
        )
        self.assertEqual(
            client.get(reverse("social:followers", args=[self.a.username])).status_code,
            404,
        )


class ProfileUnifiedSecurityTests(TestCase):
    def setUp(self):
        self.a = _user("pa")
        self.b = _user("pb")

    def test_other_profile_has_follow_not_edit(self):
        client = Client()
        client.force_login(self.a)
        resp = client.get(reverse("social:profile", args=[self.b.username]))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Xabar")
        self.assertNotContains(resp, "Profilni tahrirlash")

    def test_bio_xss_escaped(self):
        from apps.social.services.avatar import get_or_create_profile

        profile = get_or_create_profile(self.b)
        profile.bio = '<img src=x onerror=alert(1)>'
        profile.save(update_fields=["bio", "updated_at"])
        client = Client()
        client.force_login(self.a)
        resp = client.get(reverse("social:profile", args=[self.b.username]))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "&lt;img")
        self.assertNotContains(resp, "<img src=x onerror=alert(1)>")
