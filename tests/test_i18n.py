from django.test import TestCase
from django.urls import reverse

from apps.core.i18n.cyrillic import latin_to_cyrillic
from apps.core.i18n.languages import LANG_CYRL, LANG_EN, LANG_RU
from apps.core.i18n.service import localize, localize_html, set_language, t
from tests.helpers import make_course, make_exercise, make_lecture, make_module


class I18nServiceTests(TestCase):
    def test_sql_keywords_stay_in_cyrillic(self):
        set_language(LANG_CYRL)
        text = "Quyidagi SELECT so‘rov WHERE shartini yozing."
        out = localize(text)
        self.assertIn("SELECT", out)
        self.assertIn("WHERE", out)
        self.assertIn("Қуйидаги", out)

    def test_sql_in_html_pre_untouched(self):
        set_language(LANG_CYRL)
        html = "<p>So‘rov:</p><pre><code>SELECT name FROM customers;</code></pre>"
        out = localize_html(html)
        self.assertIn("SELECT name FROM customers;", out)
        self.assertIn("<pre>", out)

    def test_column_headers_stay_latin(self):
        set_language(LANG_CYRL)
        html = (
            "<table><tr><th>id</th><th>name</th><th>city</th></tr>"
            "<tr><td>1</td><td>Ali Valiyev</td><td>Toshkent</td></tr></table>"
        )
        out = localize_html(html)
        self.assertIn("<th>id</th>", out)
        self.assertIn("<th>name</th>", out)
        self.assertIn("<th>city</th>", out)
        self.assertNotIn(">ид<", out)
        self.assertNotIn(">наме<", out)
        self.assertNotIn(">сити<", out)
        self.assertIn("Али", out)
        self.assertIn("Тошкент", out)

    def test_english_keeps_sql(self):
        set_language(LANG_EN)
        out = t("SQL mashqlari va testlarni yechish, natijani saqlash uchun tizimga kiring yoki ro‘yxatdan o‘ting.")
        self.assertIn("SQL", out)
        self.assertIn("Sign in", out)

    def test_russian_nav(self):
        set_language(LANG_RU)
        self.assertEqual(t("Amaliyot"), "Практика")
        self.assertEqual(t("Kirish"), "Войти")

    def test_weekly_contest_copy(self):
        title = "Haftalik SQL musobaqasi"
        description = (
            "Shu hafta ichida SQL masalalarini yeching. "
            "Ball: Oson +1, O‘rta +2, Qiyin +3. Musobaqa reytingi umumiy reytingdan alohida."
        )
        set_language(LANG_RU)
        self.assertEqual(localize(title), "Еженедельное соревнование по SQL")
        self.assertIn("SQL", localize(description))
        self.assertNotIn("yeching", localize(description))
        self.assertIn("Рейтинг соревнования", localize(description))
        set_language(LANG_EN)
        self.assertEqual(localize(title), "Weekly SQL contest")
        self.assertIn("Easy +1", localize(description))
        self.assertNotIn("yeching", localize(description))
        set_language(LANG_CYRL)
        self.assertIn("Ҳафталик", localize(title))
        self.assertIn("SQL", localize(title))

    def test_default_uzbek_unchanged(self):
        set_language("uz")
        self.assertEqual(t("Amaliyot"), "Amaliyot")
        self.assertEqual(latin_to_cyrillic("o‘rganing"), "ўрганинг")

    def test_english_tanlang_is_not_select_keyword(self):
        set_language(LANG_EN)
        out = localize("To‘g‘ri javobni tanlang")
        self.assertNotIn("SELECT", out.upper())
        self.assertIn("choose", out.lower())

    def test_lesson_titles_keep_sql(self):
        set_language(LANG_EN)
        self.assertEqual(t("SELECT nima?"), "What is SELECT?")
        self.assertEqual(t("Ustunlarni tanlash"), "Selecting columns")
        self.assertEqual(t("Toshkent mijozlari"), "Tashkent customers")
        set_language(LANG_RU)
        self.assertEqual(t("SELECT nima?"), "Что такое SELECT?")
        self.assertIn("SELECT", t("SELECT nima?"))

    def test_homework_instructions_keep_sql(self):
        from apps.core.sql_content import HOMEWORK

        set_language(LANG_EN)
        title = t("Filtrlash va saralash uy vazifasi")
        self.assertEqual(title, "Filtering and sorting homework")
        out = t(HOMEWORK["filtrlash-va-saralash"])
        self.assertIn("WHERE", out)
        self.assertIn("AND", out)
        self.assertIn("OR", out)
        self.assertIn("DESC", out)
        self.assertIn("LIKE", out)
        self.assertIn("Explain how text and numbers", out)
        self.assertNotIn("yozilishini", out)
        self.assertNotIn("tushuntiring", out)

    def test_cyrillic_keeps_join_group_by(self):
        set_language(LANG_CYRL)
        out = localize("JOIN va GROUP BY yordamida yozing.")
        self.assertIn("JOIN", out)
        self.assertIn("GROUP BY", out)

    def test_english_sql_lesson_is_full_english(self):
        from apps.core.sql_teacher_lessons import LECTURES

        set_language(LANG_EN)
        out = localize_html(LECTURES["select-nima"], slug="select-nima")
        self.assertIn("If you have never written SQL", out)
        self.assertNotIn("yozmagan", out)
        self.assertNotIn("bo‘lsangiz", out)
        self.assertIn("SELECT name FROM customers;", out)
        self.assertIn("<code>customers</code>", out)
        self.assertIn("<th>id</th>", out)
        self.assertIn("<th>name</th>", out)
        self.assertIn("<th>city</th>", out)

    def test_russian_sql_lesson_is_not_word_salad(self):
        from apps.core.sql_teacher_lessons import LECTURES

        set_language(LANG_RU)
        out = localize_html(LECTURES["select-nima"], slug="select-nima")
        self.assertIn("Если вы никогда не писали SQL", out)
        self.assertNotIn("таблицаda", out)
        self.assertNotIn("Ishda", out)
        self.assertNotIn("yotadi", out)
        self.assertIn("SELECT name FROM customers;", out)
        self.assertIn("<code>customers</code>", out)

    def test_sql_lesson_lookup_without_slug_matches_source(self):
        from apps.core.sql_teacher_lessons import LECTURES

        set_language(LANG_EN)
        out = localize_html(LECTURES["select-nima"])
        self.assertIn("If you have never written SQL", out)

    def test_every_sql_lesson_keeps_pre_blocks(self):
        import re

        from apps.core.i18n.sql_lessons_data import SQL_LESSON_HTML
        from apps.core.sql_teacher_lessons import ADVANCED_LECTURES, LECTURES

        for slug, uz in {**LECTURES, **ADVANCED_LECTURES}.items():
            self.assertIn(slug, SQL_LESSON_HTML)
            for lang in ("en", "ru"):
                html = SQL_LESSON_HTML[slug][lang]
                for pre in re.findall(r"<pre>(.*?)</pre>", uz, re.S):
                    self.assertIn(pre, html)

    def test_english_sql_puzzle_is_full_english(self):
        from apps.core.sql_content import LECTURE_PRACTICE

        puzzle = LECTURE_PRACTICE["select-nima"]
        set_language(LANG_EN)
        desc = localize(puzzle["description"])
        task = localize(puzzle["task"])
        self.assertIn("Get the product_id values", desc)
        self.assertNotIn("mahsulotlarning", desc)
        self.assertNotIn("ustun tanlash", desc)
        self.assertIn("product_id", desc)
        self.assertIn("low_fats", desc)
        self.assertIn("recyclable", desc)
        self.assertIn("Products", desc)
        self.assertEqual(task, "Only the product_id column. All rows.")
        hint = localize(puzzle["hints"][0])
        self.assertIn("SELECT", hint)
        self.assertNotIn("keyin", hint)

    def test_russian_sql_puzzle_is_not_word_salad(self):
        from apps.core.sql_content import LECTURE_PRACTICE

        puzzle = LECTURE_PRACTICE["select-nima"]
        set_language(LANG_RU)
        desc = localize(puzzle["description"])
        task = localize(puzzle["task"])
        self.assertIn("Получите значения product_id", desc)
        self.assertNotIn("столбец tanlash", desc)
        self.assertNotIn("mahsulotlarning", desc)
        self.assertIn("product_id", desc)
        self.assertIn("low_fats", desc)
        self.assertIn("recyclable", desc)
        self.assertIn("product_id", task)
        self.assertNotIn("ustuni", task)
        self.assertNotIn("qatorlar", task)

    def test_every_sql_puzzle_keeps_identifiers(self):
        import re

        from apps.core.i18n.sql_puzzles_data import PAIRS

        snake = re.compile(r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+)+\b")
        sql = re.compile(
            r"\b(?:SELECT|DISTINCT|FROM|WHERE|JOIN|INNER|LEFT|GROUP|ORDER|HAVING|"
            r"AND|OR|NOT|IN|LIKE|BETWEEN|EXISTS|CASE|WHEN|THEN|ELSE|END|"
            r"COUNT|SUM|AVG|MIN|MAX|COALESCE|WITH|OVER|PARTITION|"
            r"ROW_NUMBER|RANK|DENSE_RANK|ASC|DESC|LIMIT|AS|NULL)\b"
        )
        for uz, ru, en in PAIRS:
            for token in snake.findall(uz) + sql.findall(uz):
                self.assertIn(token, ru)
                self.assertIn(token, en)

    def test_sql_skill_test_russian_and_english(self):
        from apps.core.sql_skill_tests import MODULE_SKILL_TESTS

        quiz = MODULE_SKILL_TESTS["sql-asoslari"][1]
        self.assertEqual(quiz["title"], "FROM qismi")
        answer = quiz["rows"][0][0]
        self.assertIn(answer, "ABCD")
        correct_body = next(o for o in quiz["quiz_options"] if o.startswith(f"{answer}) "))
        self.assertIn("jadvaldan", correct_body)

        set_language(LANG_RU)
        self.assertEqual(localize(quiz["title"]), "Часть FROM")
        self.assertIn("FROM", localize(quiz["task"]))
        self.assertNotIn("kalit", localize(quiz["task"]))
        for opt in quiz["quiz_options"]:
            out = localize(opt)
            self.assertRegex(out, r"^[A-D]\) ")
            self.assertNotIn("jadvaldan", out)
            self.assertNotIn("столбец название", out)
            self.assertNotIn("cортировка", out)
        ed = localize(quiz["editorial"])
        self.assertIn(f"Правильный ответ: {answer}.", ed)
        self.assertIn("FROM", ed)

        set_language(LANG_EN)
        self.assertEqual(localize(quiz["title"]), "The FROM clause")
        self.assertIn("FROM", localize(quiz["task"]))
        self.assertNotIn("bildiradi", localize(quiz["task"]))
        for opt in quiz["quiz_options"]:
            out = localize(opt)
            self.assertRegex(out, r"^[A-D]\) ")
            self.assertNotIn("o‘qish", out)
        self.assertIn(f"Correct answer: {answer}.", localize(quiz["editorial"]))
        self.assertIn("FROM", localize(quiz["editorial"]))


class LanguageSwitcherTests(TestCase):
    def setUp(self):
        self.course = make_course("sql", published=True, visible=True)

    def test_switcher_on_courses(self):
        response = self.client.get(reverse("courses:list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "O‘zbekcha")
        self.assertContains(response, "Ўзбекча")
        self.assertContains(response, "Русский")
        self.assertContains(response, "English")

    def test_register_footer_translates(self):
        self.client.post(reverse("set_language"), {"language": "ru", "next": "/"})
        response = self.client.get(reverse("accounts:register"))
        self.assertContains(response, "Уже есть аккаунт?")
        self.assertContains(response, "Войти")
        self.assertContains(response, "К курсам")
        self.assertNotContains(response, "Allaqachon hisobingiz bormi?")
        self.assertNotContains(response, "Kurslarni ko")

        self.client.post(reverse("set_language"), {"language": "en", "next": "/"})
        response = self.client.get(reverse("accounts:register"))
        self.assertContains(response, "Already have an account?")
        self.assertContains(response, "Sign in")
        self.assertContains(response, "Browse courses")
        self.assertNotContains(response, "Allaqachon hisobingiz bormi?")
        self.assertContains(response, "/i18n/setlang/")
        self.assertContains(response, 'id="lang-switch"')

    def test_set_english(self):
        response = self.client.post(
            reverse("set_language"),
            {"language": "en", "next": "/courses/"},
        )
        self.assertEqual(response.status_code, 302)
        page = self.client.get(reverse("courses:list"))
        self.assertContains(page, "Courses")
        self.assertContains(page, "Sign in")

    def test_set_cyrillic(self):
        self.client.post(reverse("set_language"), {"language": "uz-cyrl", "next": "/courses/"})
        page = self.client.get(reverse("courses:list"))
        self.assertContains(page, "Курслар")

    def test_lecture_sql_example_not_translated(self):
        module = make_module(self.course)
        lecture = make_lecture(module)
        lecture.content = "<p>SELECT nima?</p><pre>SELECT 1;</pre>"
        lecture.sql_examples = ["SELECT name FROM customers"]
        lecture.save()
        self.client.post(reverse("set_language"), {"language": "en", "next": "/"})
        page = self.client.get(reverse("learning:lecture", args=[lecture.pk]))
        self.assertEqual(page.status_code, 200)
        self.assertContains(page, "SELECT name FROM customers")
        self.assertContains(page, "SELECT 1;")

    def test_course_detail_translates_section_and_titles(self):
        module = make_module(self.course)
        make_lecture(module)
        make_exercise(module, title="Toshkent mijozlari")
        self.client.post(reverse("set_language"), {"language": "en", "next": "/"})
        page = self.client.get(reverse("courses:detail", args=[self.course.slug]))
        self.assertEqual(page.status_code, 200)
        self.assertContains(page, "Lessons")
        self.assertContains(page, "Extra exercises")
        self.assertContains(page, "What is SELECT?")
        self.assertContains(page, "Tashkent customers")
        self.assertNotContains(page, "Darslar")

    def test_lecture_page_english_and_russian_bodies(self):
        from apps.core.sql_teacher_lessons import LECTURES

        module = make_module(self.course)
        lecture = make_lecture(module, slug="select-nima")
        lecture.content = LECTURES["select-nima"]
        lecture.save()

        self.client.post(reverse("set_language"), {"language": "en", "next": "/"})
        page = self.client.get(reverse("learning:lecture", args=[lecture.pk]))
        self.assertEqual(page.status_code, 200)
        self.assertContains(page, "If you have never written SQL")
        self.assertNotContains(page, "yozmagan")
        self.assertNotContains(page, "with filtering hard")
        self.assertContains(page, "SELECT name FROM customers;")
        self.assertContains(page, "customers")

        self.client.post(reverse("set_language"), {"language": "ru", "next": "/"})
        page = self.client.get(reverse("learning:lecture", args=[lecture.pk]))
        self.assertContains(page, "Если вы никогда не писали SQL")
        self.assertNotContains(page, "таблицаda")
        self.assertNotContains(page, "Ishda")
        self.assertContains(page, "SELECT name FROM customers;")

    def test_exercise_page_english_and_russian_copy(self):
        from apps.accounts.models import User
        from apps.core.sql_content import LECTURE_PRACTICE

        from tests.helpers import make_user

        puzzle = LECTURE_PRACTICE["select-nima"]
        module = make_module(self.course)
        exercise = make_exercise(
            module,
            slug=puzzle["slug"],
            title=puzzle["title"],
        )
        exercise.description = puzzle["description"]
        exercise.task = puzzle["task"]
        exercise.hints = puzzle["hints"]
        exercise.save()
        student = make_user("puzzle@test.com", User.Role.STUDENT)
        self.client.force_login(student)

        self.client.post(reverse("set_language"), {"language": "en", "next": "/"})
        page = self.client.get(reverse("exercises:detail", args=[exercise.pk]))
        self.assertEqual(page.status_code, 200)
        self.assertContains(page, "Get the product_id values")
        self.assertNotContains(page, "mahsulotlarning")
        self.assertContains(page, "product_id")
        self.assertContains(page, "low_fats")
        self.assertContains(page, "recyclable")

        self.client.post(reverse("set_language"), {"language": "ru", "next": "/"})
        page = self.client.get(reverse("exercises:detail", args=[exercise.pk]))
        self.assertContains(page, "Получите значения product_id")
        self.assertNotContains(page, "столбец tanlash")
        self.assertContains(page, "product_id")
