from django.test import TestCase

from apps.core.python_content import build_python_modules
from apps.core.python_skill_tests import MODULE_SKILL_TESTS, skill_tests_for_module


class PythonContentTests(TestCase):
    def test_modules_have_practice_puzzles_and_exercises(self):
        modules = build_python_modules()
        self.assertGreaterEqual(len(modules), 9)
        for module in modules:
            with self.subTest(module=module["slug"]):
                self.assertTrue(module["lectures"])
                practice = module.get("practice") or {}
                self.assertTrue(practice, msg="har darsda mashq bo‘lishi kerak")
                for slug, items in practice.items():
                    self.assertIsInstance(items, list)
                    self.assertGreaterEqual(len(items), 1)
                    for quiz in items:
                        self.assertEqual(quiz["kind"], "quiz")
                        self.assertEqual(len(quiz["quiz_options"]), 4)
                self.assertGreaterEqual(len(module.get("exercises") or []), 2)

    def test_skill_tests_cover_every_module(self):
        modules = build_python_modules()
        for module in modules:
            quizzes = skill_tests_for_module(module["slug"])
            with self.subTest(module=module["slug"]):
                self.assertGreaterEqual(len(quizzes), 10)
                self.assertEqual(len(quizzes), 11)
                for q in quizzes:
                    self.assertTrue(q["is_skill_test"])
                    self.assertEqual(q["kind"], "quiz")
                    self.assertEqual(len(q["quiz_options"]), 4)
                    self.assertIn(q["rows"][0][0], "ABCD")
        self.assertEqual(len(MODULE_SKILL_TESTS), len(modules))

    def test_python_course_is_closed_for_release(self):
        from apps.access.services import OPEN_COURSE_SLUGS

        self.assertNotIn("python", OPEN_COURSE_SLUGS)
        self.assertIn("sql", OPEN_COURSE_SLUGS)
