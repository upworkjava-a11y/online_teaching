from django.test import SimpleTestCase

from apps.core.sql_skill_tests import MODULE_SKILL_TESTS, skill_tests_for_module


class SqlSkillTestsContentTests(SimpleTestCase):
    def test_each_module_has_at_least_10_quizzes(self):
        self.assertGreaterEqual(len(MODULE_SKILL_TESTS), 11)
        for slug, items in MODULE_SKILL_TESTS.items():
            self.assertGreaterEqual(len(items), 10, msg=f"{slug} da kamida 10 ta savol bo‘lishi kerak")
            for item in items:
                self.assertEqual(len(item["quiz_options"]), 4)
                self.assertEqual(item["kind"], "quiz")
                self.assertTrue(item["is_skill_test"])
                self.assertIn(item["rows"][0][0], "ABCD")
                for opt in item["quiz_options"]:
                    self.assertRegex(opt, r"^[A-D]\) ")

    def test_skill_tests_for_module_slugs(self):
        quizzes = skill_tests_for_module("sql-asoslari")
        self.assertGreaterEqual(len(quizzes), 10)
        self.assertTrue(quizzes[0]["slug"].startswith("bt-sql-asoslari-"))
