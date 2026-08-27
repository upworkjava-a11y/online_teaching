from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.urls import reverse

from apps.access.models import UserContentAccess
from apps.access.services import access_service
from apps.accounts.models import User
from tests.helpers import make_course, make_lecture, make_module, make_user


class UserAccessControlTests(TestCase):
    def setUp(self):
        self.student = make_user("student@test.com", User.Role.STUDENT)
        self.admin = make_user("admin@test.com", User.Role.ADMIN, is_staff=True, is_superuser=True)
        self.course = make_course()
        self.module = make_module(self.course)
        self.hidden_module = make_module(self.course, slug="hidden", published=False, title="Yashirin")
        self.lecture = make_lecture(self.module)
        self.hidden_lecture = make_lecture(self.hidden_module, slug="hidden-lecture")

    def _block(self, obj):
        UserContentAccess.objects.create(
            user=self.student,
            content_type=ContentType.objects.get_for_model(obj),
            object_id=obj.pk,
            status=UserContentAccess.Status.BLOCKED,
            created_by=self.admin,
        )

    def _allow(self, obj):
        UserContentAccess.objects.create(
            user=self.student,
            content_type=ContentType.objects.get_for_model(obj),
            object_id=obj.pk,
            status=UserContentAccess.Status.ALLOWED,
            created_by=self.admin,
        )

    def test_admin_can_block_module(self):
        self._block(self.module)
        self.assertFalse(access_service.can_access(self.student, self.module))

    def test_student_cannot_access_blocked_module(self):
        self._block(self.module)
        self.client.force_login(self.student)
        response = self.client.get(reverse("learning:lecture", args=[self.lecture.pk]))
        self.assertEqual(response.status_code, 403)
        self.assertContains(response, "yopilgan", status_code=403)

    def test_direct_url_bypass_fails(self):
        self._block(self.course)
        self.client.force_login(self.student)
        response = self.client.get(reverse("learning:lecture", args=[self.lecture.pk]))
        self.assertEqual(response.status_code, 403)

    def test_admin_unblocks_module(self):
        rule = UserContentAccess.objects.create(
            user=self.student,
            content_type=ContentType.objects.get_for_model(self.module),
            object_id=self.module.pk,
            status=UserContentAccess.Status.BLOCKED,
            created_by=self.admin,
        )
        rule.status = UserContentAccess.Status.ALLOWED
        rule.save()
        self.assertTrue(access_service.can_access(self.student, self.module))

    def test_published_but_blocked(self):
        self.assertTrue(access_service.can_access(self.student, self.lecture))
        self._block(self.lecture)
        self.assertFalse(access_service.can_access(self.student, self.lecture))

    def test_unpublished_explicitly_allowed(self):
        self.assertFalse(access_service.can_access(self.student, self.hidden_module))
        self._allow(self.hidden_module)
        self.assertTrue(access_service.can_access(self.student, self.hidden_module))

    def _six_modules(self):
        """Base setUp already has module order=1; add modules 2–6."""
        extra_lectures = []
        for index in range(2, 7):
            module = make_module(self.course, slug=f"mod-{index}", title=f"Modul {index}")
            module.order = index
            module.save()
            lecture = make_lecture(module, slug=f"lec-{index}", title=f"Dars {index}")
            extra_lectures.append(lecture)
        return extra_lectures

    def test_free_user_gets_first_five_modules_only(self):
        lecture2, lecture3, lecture4, lecture5, lecture6 = self._six_modules()
        self.assertTrue(access_service.can_access(self.student, self.lecture))
        self.assertTrue(access_service.can_access(self.student, lecture2))
        self.assertTrue(access_service.can_access(self.student, lecture3))
        self.assertTrue(access_service.can_access(self.student, lecture4))
        self.assertTrue(access_service.can_access(self.student, lecture5))
        self.assertFalse(access_service.can_access(self.student, lecture6))
        self.client.force_login(self.student)
        locked = self.client.get(reverse("learning:lecture", args=[lecture6.pk]))
        self.assertEqual(locked.status_code, 302)
        self.assertIn("/courses/sql/premium/", locked.url)
        offer = self.client.get(locked.url)
        self.assertEqual(offer.status_code, 200)
        self.assertContains(offer, "Premium")
        self.assertContains(offer, "50 000")
        outline = self.client.get(reverse("courses:detail", args=["sql"]))
        self.assertContains(outline, "🔒")
        self.assertContains(outline, "Dars 6")
        self.assertContains(outline, "Dastlabki 5 modul ochiq")

    def test_premium_user_gets_full_course(self):
        *_rest, lecture6 = self._six_modules()
        self.assertFalse(access_service.can_access(self.student, lecture6))
        self.student.is_premium = True
        self.student.save(update_fields=["is_premium"])
        self.assertTrue(access_service.can_access(self.student, lecture6))
        self.client.force_login(self.student)
        response = self.client.get(reverse("learning:lecture", args=[lecture6.pk]))
        self.assertEqual(response.status_code, 200)

    def test_course_allow_rule_unlocks_all_lessons(self):
        *_rest, lecture6 = self._six_modules()
        self.assertFalse(access_service.can_access(self.student, lecture6))
        self._allow(self.course)
        self.assertTrue(access_service.has_full_course_access(self.student, self.course))
        self.assertTrue(access_service.can_access(self.student, lecture6))

    def test_grant_course_access_opens_only_that_course(self):
        *_rest, lecture6 = self._six_modules()
        other = make_course("python", published=True, visible=True, title="Python")
        py_lectures = []
        for i in range(1, 7):
            mod = make_module(other, slug=f"py-mod-{i}", order=i, title=f"Py modul {i}")
            py_lectures.append(make_lecture(mod, slug=f"py-dars-{i}", title=f"Py dars {i}", order=1))

        access_service.grant_course_access(self.student, self.course, reason="To‘lov SQL")
        self.assertTrue(access_service.has_full_course_access(self.student, self.course))
        self.assertTrue(access_service.can_access(self.student, lecture6))
        self.assertFalse(access_service.has_full_course_access(self.student, other))
        self.assertFalse(access_service.can_access(self.student, py_lectures[-1]))

    def test_premium_group_unlocks_full_course(self):
        from django.contrib.auth.models import Group

        from apps.access.services import PREMIUM_GROUP_NAME

        *_rest, lecture6 = self._six_modules()
        self.assertFalse(access_service.can_access(self.student, lecture6))
        group, _ = Group.objects.get_or_create(name=PREMIUM_GROUP_NAME)
        self.student.groups.add(group)
        self.assertTrue(access_service.is_premium_user(self.student))
        self.assertTrue(access_service.can_access(self.student, lecture6))
