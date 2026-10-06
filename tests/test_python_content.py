from django.test import TestCase

from apps.core.python_content import build_python_modules
from apps.core.python_skill_tests import MODULE_SKILL_TESTS, skill_tests_for_module


class PythonContentTests(TestCase):
    def test_modules_have_practice_puzzles_and_exercises(self):
        modules = build_python_modules()
        self.assertGreaterEqual(len(modules), 10)
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

    def test_python_course_is_open_with_preview(self):
        from apps.access.services import FREE_PREVIEW_BY_COURSE, OPEN_COURSE_SLUGS

        self.assertIn("python", OPEN_COURSE_SLUGS)
        self.assertEqual(FREE_PREVIEW_BY_COURSE.get("python"), 1)

    def test_practice_puzzles_not_duplicated_by_topic(self):
        from apps.core.python_puzzles import _quiz_topic_fingerprint

        for module in build_python_modules():
            with self.subTest(module=module["slug"]):
                module_tags: set[str] = set()
                for lec_slug, items in (module.get("practice") or {}).items():
                    lec_tags: set[str] = set()
                    for quiz in items:
                        tags = set(_quiz_topic_fingerprint(quiz))
                        overlap = tags & lec_tags
                        self.assertFalse(
                            overlap,
                            msg=f"{module['slug']}/{lec_slug} {quiz['slug']} repeats {overlap}",
                        )
                        lec_tags |= tags
                        module_tags |= tags
                for ex in module.get("exercises") or []:
                    ex_tags = set(_quiz_topic_fingerprint(ex))
                    overlap = ex_tags & module_tags
                    self.assertFalse(
                        overlap,
                        msg=f"{module['slug']} module ex {ex['slug']} repeats lecture topic {overlap}",
                    )
                    module_tags |= ex_tags

    def test_localize_html_py_wrapper(self):
        from apps.core.i18n.languages import LANG_UZ
        from apps.core.i18n.service import localize_html, set_language

        set_language(LANG_UZ)
        html = "<h2>Dars maqsadi</h2><p>Python.</p>"
        out = localize_html(html, slug="py-noldan-start")
        self.assertIn("py-lesson", out)
        self.assertIn("py-banner", out)

    def test_lessons_have_structure_and_code_editor(self):
        from apps.core.python_lesson_format import format_python_lesson

        sample = format_python_lesson(
            '<p>Salom.</p><pre>print("OK")</pre><p>Yakun.</p>',
            goal_p="<p>Birinchi print.</p>",
        )
        self.assertIn("<h2>Dars maqsadi</h2>", sample)
        self.assertIn("<h2>Batafsil tushuntirish</h2>", sample)
        self.assertIn("py-editor", sample)
        self.assertIn("hello.py", sample)
        self.assertIn('print("OK")', sample)

        required_any = (
            "Dars maqsadi",
            "Oddiy tilda",
            "Qadam-baqadam",
            "Lesson goal",
        )
        for module in build_python_modules():
            for lecture in module["lectures"]:
                with self.subTest(slug=lecture["slug"]):
                    html = lecture["content"]
                    self.assertIn("<h2", html.lower())
                    self.assertTrue(
                        any(marker in html for marker in required_any),
                        msg=f"{lecture['slug']} missing beginner structure headings",
                    )
                    if "<pre" in html.lower() or "py-editor" in html:
                        self.assertIn("py-editor", html)
                        self.assertIn("py-editor__code", html)

    def test_skill_tests_shuffle_answers(self):
        from collections import Counter

        from apps.core.python_skill_tests import skill_tests_for_module

        letters = Counter()
        for q in skill_tests_for_module("py-noldan"):
            ans = q["rows"][0][0]
            letters[ans] += 1
            self.assertTrue(q["editorial"].startswith("To‘g‘ri javob:"))
            self.assertIn(f"To‘g‘ri javob: {ans}.", q["editorial"])
        # Not stuck on a single letter
        self.assertGreaterEqual(len(letters), 2)

    def test_hard_puzzles_exist(self):
        hard = 0
        for module in build_python_modules():
            for ex in module.get("exercises") or []:
                if ex.get("difficulty") == "hard":
                    hard += 1
            for items in (module.get("practice") or {}).values():
                for q in items if isinstance(items, list) else [items]:
                    if q.get("difficulty") == "hard":
                        hard += 1
        self.assertGreaterEqual(hard, 5)

    def test_lesson_goals_cover_all_slugs(self):
        from apps.core.i18n.python_lessons_meta import PYTHON_LESSONS

        for module in build_python_modules():
            for lecture in module["lectures"]:
                self.assertIn(lecture["slug"], PYTHON_LESSONS)
