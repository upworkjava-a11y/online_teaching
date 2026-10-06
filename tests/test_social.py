"""Tests for social features: chat, follow, block, presence, avatar, activity."""

from __future__ import annotations

import io
from datetime import date

from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings
from django.urls import reverse
from PIL import Image

from apps.social.models import Block, Conversation, Follow, Message, UserActivity, conversation_pair_key
from apps.social.services import activity as activity_svc
from apps.social.services import avatar as avatar_svc
from apps.social.services import chat as chat_svc
from apps.social.services import presence as presence_svc
from apps.social.services.relations import SocialRelationError, block, follow, unfollow

User = get_user_model()


def _user(username, **extra):
    return User.objects.create_user(
        email=f"{username}@example.com",
        password="Pass123!",
        username=username,
        first_name=username.title(),
        role=User.Role.STUDENT,
        **extra,
    )


def _png_bytes(color=(30, 144, 255), size=(64, 64)):
    buf = io.BytesIO()
    Image.new("RGB", size, color).save(buf, format="PNG")
    return buf.getvalue()


class ChatTests(TestCase):
    def setUp(self):
        cache.clear()
        self.a = _user("alice")
        self.b = _user("bob")
        self.c = _user("cara")

    def test_create_conversation_unique(self):
        c1 = chat_svc.get_or_create_conversation(self.a, self.b)
        c2 = chat_svc.get_or_create_conversation(self.b, self.a)
        self.assertEqual(c1.pk, c2.pk)
        self.assertEqual(Conversation.objects.count(), 1)
        self.assertEqual(c1.pair_key, conversation_pair_key(self.a.pk, self.b.pk))

    def test_cannot_access_others_conversation(self):
        conv = chat_svc.get_or_create_conversation(self.a, self.b)
        self.assertFalse(chat_svc.user_can_access(conv, self.c))
        client = Client()
        client.force_login(self.c)
        resp = client.get(reverse("social:chat_detail", args=[conv.pk]))
        self.assertEqual(resp.status_code, 404)

    def test_send_message_and_unread(self):
        conv = chat_svc.get_or_create_conversation(self.a, self.b)
        msg = chat_svc.send_message(self.a, conv, "Salom!")
        self.assertEqual(msg.text, "Salom!")
        self.assertIsNone(msg.read_at)
        self.assertEqual(chat_svc.unread_total(self.b), 1)
        chat_svc.mark_conversation_read(conv, self.b)
        self.assertEqual(chat_svc.unread_total(self.b), 0)
        msg.refresh_from_db()
        self.assertIsNotNone(msg.read_at)

    @override_settings(SOCIAL_MESSAGE_MIN_INTERVAL_SECONDS=0)
    def test_chat_updates_polling(self):
        conv = chat_svc.get_or_create_conversation(self.a, self.b)
        first = chat_svc.send_message(self.a, conv, "bir")
        client = Client()
        client.force_login(self.b)
        empty = client.get(reverse("social:chat_updates", args=[conv.pk]), {"after": first.pk})
        self.assertEqual(empty.status_code, 200)
        self.assertEqual(empty.content, b"")
        second = chat_svc.send_message(self.a, conv, "ikki")
        resp = client.get(reverse("social:chat_updates", args=[conv.pk]), {"after": first.pk})
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "ikki")
        self.assertContains(resp, f'data-msg-id="{second.pk}"')
        self.assertEqual(resp.get("X-Chat-Last-Id"), str(second.pk))
        # Advancing cursor must not redeliver the same message.
        again = client.get(reverse("social:chat_updates", args=[conv.pk]), {"after": second.pk})
        self.assertEqual(again.content, b"")

    @override_settings(SOCIAL_MESSAGE_MIN_INTERVAL_SECONDS=0)
    def test_unread_badge_poll(self):
        conv = chat_svc.get_or_create_conversation(self.a, self.b)
        chat_svc.send_message(self.a, conv, "badge me")
        client = Client()
        client.force_login(self.b)
        resp = client.get(reverse("social:unread_badge"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "social-badge")
        self.assertContains(resp, "1")
        chat_svc.mark_conversation_read(conv, self.b)
        empty = client.get(reverse("social:unread_badge"))
        self.assertEqual(empty.status_code, 200)
        self.assertNotContains(empty, "social-badge")
        # Navbar includes live poller
        home = client.get(reverse("dashboard:home"))
        self.assertContains(home, "nav-unread-poll")
        self.assertContains(home, 'id="nav-unread-badge"')

    def test_message_length_validation(self):
        conv = chat_svc.get_or_create_conversation(self.a, self.b)
        with self.assertRaises(chat_svc.ChatError):
            chat_svc.send_message(self.a, conv, "x" * 1001)

    @override_settings(SOCIAL_MESSAGE_RATE_PER_MINUTE=2, SOCIAL_MESSAGE_MIN_INTERVAL_SECONDS=0)
    def test_rate_limiting(self):
        cache.clear()
        conv = chat_svc.get_or_create_conversation(self.a, self.b)
        chat_svc.send_message(self.a, conv, "one")
        chat_svc.send_message(self.a, conv, "two")
        with self.assertRaises(chat_svc.ChatError):
            chat_svc.send_message(self.a, conv, "three")


class FollowBlockTests(TestCase):
    def setUp(self):
        self.a = _user("alice2")
        self.b = _user("bob2")

    def test_follow_unfollow(self):
        follow(self.a, self.b)
        self.assertEqual(Follow.objects.count(), 1)
        follow(self.a, self.b)  # idempotent get_or_create
        self.assertEqual(Follow.objects.count(), 1)
        unfollow(self.a, self.b)
        self.assertEqual(Follow.objects.count(), 0)

    def test_cannot_follow_self(self):
        with self.assertRaises(SocialRelationError):
            follow(self.a, self.a)

    def test_block_removes_follow_and_blocks_chat(self):
        follow(self.a, self.b)
        follow(self.b, self.a)
        block(self.a, self.b)
        self.assertEqual(Follow.objects.count(), 0)
        self.assertTrue(Block.objects.filter(blocker=self.a, blocked=self.b).exists())
        with self.assertRaises(chat_svc.ChatError):
            chat_svc.get_or_create_conversation(self.b, self.a)


class PresenceTests(TestCase):
    def setUp(self):
        cache.clear()
        self.user = _user("pres")

    def test_online_offline(self):
        self.assertFalse(presence_svc.is_online(self.user.pk))
        presence_svc.heartbeat(self.user.pk)
        self.assertTrue(presence_svc.is_online(self.user.pk))
        cache.clear()
        self.assertFalse(presence_svc.is_online(self.user.pk))

    def test_blocked_status(self):
        other = _user("pres2")
        status = presence_svc.presence_status(viewer=self.user, target=other, blocked=True)
        self.assertEqual(status, "blocked")


class AvatarTests(TestCase):
    def setUp(self):
        self.user = _user("avatar")

    def test_preset_and_upload(self):
        avatar_svc.set_preset_avatar(self.user, "avatar-03")
        url = avatar_svc.resolve_avatar_url(self.user)
        self.assertIn("avatar-03", url)
        uploaded = SimpleUploadedFile("pic.png", _png_bytes(), content_type="image/png")
        profile = avatar_svc.upload_avatar(self.user, uploaded)
        self.assertTrue(profile.avatar_image.name.endswith(".webp"))

    def test_reject_fake_image(self):
        uploaded = SimpleUploadedFile("evil.png", b"<svg xmlns='http://www.w3.org/2000/svg'></svg>", content_type="image/png")
        with self.assertRaises(ValidationError):
            avatar_svc.upload_avatar(self.user, uploaded)


class ActivityTests(TestCase):
    def setUp(self):
        self.user = _user("act")

    def test_record_and_calendar(self):
        activity_svc.record_lesson(self.user)
        activity_svc.record_exercise(self.user)
        activity_svc.record_exercise(self.user, is_quiz=True)
        day = date.today()
        data = activity_svc.day_breakdown(self.user, day)
        self.assertEqual(data["total"], 3)
        year = activity_svc.year_calendar(self.user, day.year)
        self.assertGreaterEqual(year["totals"].get(day, 0), 3)
        month = activity_svc.month_calendar(self.user, day.year, day.month)
        self.assertTrue(month["weeks"])

    def test_profile_page(self):
        client = Client()
        client.force_login(self.user)
        resp = client.get(reverse("social:profile", args=[self.user.username]))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.user.username)
        self.assertContains(resp, "O‘qish statistikasi")
        self.assertContains(resp, "Yutuqlar")
        self.assertContains(resp, "Faoliyat")
        self.assertContains(resp, "Profilni tahrirlash")
        self.assertEqual(reverse("social:profile", args=[self.user.username]), f"/profile/{self.user.username}/")
