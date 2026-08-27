from django.conf import settings
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from django.db import transaction

from apps.access.services import PREMIUM_GROUP_NAME, access_service
from apps.accounts.models import TeacherProfile, User
from apps.courses.models import Course, CourseEnrollment, Lecture, Module
from apps.exercises.models import Dataset, Exercise, ExerciseDataset, ExerciseExpectedResult
from apps.homework.models import HomeworkAssignment
from apps.core.excel_content import COURSE_DESCRIPTION as EXCEL_COURSE_DESCRIPTION
from apps.core.excel_content import build_excel_modules
from apps.core.powerbi_content import COURSE_DESCRIPTION as PBI_COURSE_DESCRIPTION
from apps.core.powerbi_content import build_powerbi_modules
from apps.core.projects_content import COURSE_DESCRIPTION as PROJECTS_COURSE_DESCRIPTION
from apps.core.projects_content import build_projects_modules
from apps.core.python_content import COURSE_DESCRIPTION as PYTHON_COURSE_DESCRIPTION
from apps.core.python_content import build_python_modules
from apps.core.statistics_content import COURSE_DESCRIPTION as STATS_COURSE_DESCRIPTION
from apps.core.statistics_content import build_statistics_modules
from apps.core.sql_content import COURSE_DESCRIPTION, EXERCISE_COPY, HOMEWORK, LECTURE_PRACTICE, LECTURES, SQL_EXAMPLES
from apps.core.sql_modules_advanced import (
    ADVANCED_HOMEWORK,
    ADVANCED_PRACTICE,
    build_advanced_modules,
)
from apps.core.sql_practice_extra import practices_for_lecture
from apps.sandbox.datasets import (
    CUSTOMERS_SCHEMA,
    ORDERS_SCHEMA,
    PRODUCTS_SCHEMA,
    SAMPLE_PREVIEW,
    SEED_SQL,
    TRANSACTIONS_SCHEMA,
    seed_sandbox_database,
)
from apps.sandbox.leetcode_sql import LEETCODE_PREVIEWS, LEETCODE_SCHEMA_SQL, LEETCODE_SEED_SQL


SQL_FUTURE_MODULES = []  # modules 4–11 now seeded with full content via build_advanced_modules()


class Command(BaseCommand):
    help = "Create initial courses, Uzbek SQL content, demo users, and sandbox datasets."

    @transaction.atomic
    def handle(self, *args, **options):
        self._create_users()
        courses = self._create_courses()
        self._create_sql_content(courses["sql"])
        self._seed_structured_course(courses["excel"], build_excel_modules())
        self._seed_structured_course(courses["statistics"], build_statistics_modules())
        self._seed_structured_course(courses["python"], build_python_modules())
        self._seed_python_skill_tests(courses["python"])
        self._seed_structured_course(courses["power-bi"], build_powerbi_modules())
        self._seed_structured_course(courses["real-projects"], build_projects_modules())
        for course in courses.values():
            self._assign_teacher(course)
        self._seed_weekly_contest(
            courses["sql"],
            slug="haftalik-sql",
            title="Haftalik SQL musobaqasi",
            description=(
                "Shu hafta ichida SQL masalalarini yeching. "
                "Ball: Oson +1, O‘rta +2, Qiyin +3. Musobaqa reytingi umumiy reytingdan alohida."
            ),
            seed_skill_tests=True,
        )
        # Production release: faqat SQL — Python musobaqasini yashirish
        self._hide_python_for_release(courses["python"])
        try:
            seed_sandbox_database()
            self.stdout.write(self.style.SUCCESS("Sandbox datasetlari yuklandi."))
        except Exception as exc:
            self.stdout.write(self.style.WARNING(f"Sandbox seed o‘tkazib yuborildi: {exc}"))
        self.stdout.write(self.style.SUCCESS("Platforma boshlang‘ich ma’lumotlari tayyor."))

    def _create_users(self):
        Group.objects.get_or_create(name=PREMIUM_GROUP_NAME)
        email = getattr(settings, "env", None)
        admin_email = settings.env("DJANGO_SUPERUSER_EMAIL", default="admin@example.com") if hasattr(settings, "env") else "admin@example.com"
        try:
            from config.settings.base import env

            admin_email = env("DJANGO_SUPERUSER_EMAIL", default="admin@example.com")
            admin_password = env("DJANGO_SUPERUSER_PASSWORD", default="ChangeMeNow123!")
            admin_first = env("DJANGO_SUPERUSER_FIRST_NAME", default="Admin")
            admin_last = env("DJANGO_SUPERUSER_LAST_NAME", default="User")
        except Exception:
            admin_email = "admin@example.com"
            admin_password = "ChangeMeNow123!"
            admin_first = "Admin"
            admin_last = "User"

        if not User.objects.filter(email=admin_email).exists():
            User.objects.create_superuser(
                email=admin_email,
                password=admin_password,
                first_name=admin_first,
                last_name=admin_last,
                username="admin",
            )
        teacher, created = User.objects.get_or_create(
            email="teacher@example.com",
            defaults={
                "username": "teacher",
                "first_name": "Nodira",
                "last_name": "Toshpulatova",
                "role": User.Role.TEACHER,
            },
        )
        if created:
            teacher.set_password("TeacherPass123!")
            teacher.save()
        student, created = User.objects.get_or_create(
            email="student@example.com",
            defaults={
                "username": "student",
                "first_name": "Ali",
                "last_name": "Valiyev",
                "role": User.Role.STUDENT,
            },
        )
        if created:
            student.set_password("StudentPass123!")
            student.save()

    def _create_courses(self):
        specs = [
            ("sql", "SQL", COURSE_DESCRIPTION, 1),
            ("excel", "Excel", EXCEL_COURSE_DESCRIPTION, 2),
            ("statistics", "Statistika", STATS_COURSE_DESCRIPTION, 3),
            ("python", "Python", PYTHON_COURSE_DESCRIPTION, 4),
            ("power-bi", "Power BI", PBI_COURSE_DESCRIPTION, 5),
            ("real-projects", "Amaliy loyihalar", PROJECTS_COURSE_DESCRIPTION, 6),
        ]
        courses = {}
        for slug, title, description, order in specs:
            # Release: Python yashirin; SQL ochiq; qolganlar “Hozir jarayonda” uchun ko‘rinadi
            is_visible = slug != "python"
            course, _ = Course.objects.get_or_create(
                slug=slug,
                defaults={
                    "title": title,
                    "description": description,
                    "order": order,
                    "is_published": True,
                    "is_visible": is_visible,
                },
            )
            course.title = title
            course.description = description
            course.order = order
            course.is_published = True
            course.is_visible = is_visible
            course.save(update_fields=["title", "description", "order", "is_published", "is_visible"])
            courses[slug] = course
        return courses

    def _seed_structured_course(self, course: Course, modules_data):
        for module_data in modules_data:
            module, _ = Module.objects.update_or_create(
                course=course,
                slug=module_data["slug"],
                defaults={
                    "title": module_data["title"],
                    "description": module_data["description"],
                    "order": module_data["order"],
                    "is_published": True,
                },
            )
            practice_map = module_data.get("practice") or {}
            for index, lecture_data in enumerate(module_data["lectures"], start=1):
                lecture, _ = Lecture.objects.update_or_create(
                    module=module,
                    slug=lecture_data["slug"],
                    defaults={
                        "title": lecture_data["title"],
                        "content": lecture_data["content"],
                        "sql_examples": lecture_data.get("sql_examples") or [],
                        "order": index,
                        "is_published": True,
                    },
                )
                practices = practice_map.get(lecture.slug)
                if practices:
                    if isinstance(practices, dict):
                        practices = [practices]
                    for p_i, practice in enumerate(practices):
                        self._upsert_exercise(
                            module,
                            practice,
                            [],
                            lecture=lecture,
                            order=100 + index * 10 + p_i,
                        )
                if module_data.get("homework") and index == len(module_data["lectures"]):
                    HomeworkAssignment.objects.update_or_create(
                        lecture=lecture,
                        defaults={
                            "title": f"{module.title} uy vazifasi",
                            "instructions": module_data["homework"],
                            "max_score": 100,
                            "is_published": True,
                        },
                    )
            for index, exercise_data in enumerate(module_data.get("exercises") or [], start=1):
                self._upsert_exercise(module, exercise_data, [], order=index)

    def _create_sql_content(self, course: Course):
        customers, _ = Dataset.objects.update_or_create(
            name="customers",
            defaults={
                "description": "Bank mijozlari",
                "schema_sql": CUSTOMERS_SCHEMA,
                "seed_sql": SEED_SQL,
                "preview": SAMPLE_PREVIEW["customers"],
            },
        )
        transactions, _ = Dataset.objects.update_or_create(
            name="transactions",
            defaults={
                "description": "Mijoz tranzaksiyalari",
                "schema_sql": TRANSACTIONS_SCHEMA,
                "seed_sql": SEED_SQL,
                "preview": SAMPLE_PREVIEW["transactions"],
            },
        )
        Dataset.objects.update_or_create(
            name="shop_products",
            defaults={"description": "Do‘kon mahsulotlari", "schema_sql": PRODUCTS_SCHEMA, "seed_sql": SEED_SQL, "preview": SAMPLE_PREVIEW["products"]},
        )
        Dataset.objects.update_or_create(
            name="orders",
            defaults={"description": "Buyurtmalar", "schema_sql": ORDERS_SCHEMA, "seed_sql": SEED_SQL, "preview": SAMPLE_PREVIEW["orders"]},
        )
        lc_datasets = {}
        for table_name, preview in LEETCODE_PREVIEWS.items():
            ds, _ = Dataset.objects.update_or_create(
                name=table_name,
                defaults={
                    "description": f"LeetCode jadvali: {table_name}",
                    "schema_sql": LEETCODE_SCHEMA_SQL,
                    "seed_sql": LEETCODE_SEED_SQL,
                    "preview": preview,
                },
            )
            lc_datasets[table_name] = ds

        old_practice_slugs = [
            "lc-customer-ids",
            "lc-name-city",
            "lc-unique-cities",
            "lc-samarqand-customers",
            "lc-newest-customers",
            "lc-ova-names",
            "lc-credit-count",
            "lc-credit-sum",
            "lc-customers-per-city",
        ]
        Exercise.objects.filter(slug__in=old_practice_slugs).delete()

        modules_data = [
            {
                "order": 1,
                "title": "SQL asoslari",
                "slug": "sql-asoslari",
                "description": "SELECT, ustunlar va oddiy so‘rovlar.",
                "lectures": [
                    {
                        "title": "SELECT nima?",
                        "slug": "select-nima",
                        "content": LECTURES["select-nima"],
                        "sql_examples": SQL_EXAMPLES["select-nima"],
                    },
                    {
                        "title": "Ustunlarni tanlash",
                        "slug": "ustunlarni-tanlash",
                        "content": LECTURES["ustunlarni-tanlash"],
                        "sql_examples": SQL_EXAMPLES["ustunlarni-tanlash"],
                    },
                    {
                        "title": "Natijani o‘qish",
                        "slug": "natijani-oqish",
                        "content": LECTURES["natijani-oqish"],
                        "sql_examples": SQL_EXAMPLES["natijani-oqish"],
                    },
                ],
                "exercises": [
                    {
                        "title": "Mijoz ismlari",
                        "slug": "mijoz-ismlari",
                        "description": EXERCISE_COPY["mijoz-ismlari"]["description"],
                        "task": EXERCISE_COPY["mijoz-ismlari"]["task"],
                        "hints": ["Faqat bitta ustun kerak — ism"],
                        "columns": ["name"],
                        "rows": [["Ali Valiyev"], ["Malika Karimova"], ["Javohir Saidov"], ["Dilnoza Yusupova"], ["Sardor Ergashev"]],
                    },
                    {
                        "title": "Toshkent mijozlari",
                        "slug": "toshkent-mijozlari",
                        "description": EXERCISE_COPY["toshkent-mijozlari"]["description"],
                        "task": EXERCISE_COPY["toshkent-mijozlari"]["task"],
                        "hints": ["Shaharni filtrlab oling"],
                        "columns": ["name", "city"],
                        "rows": [["Ali Valiyev", "Toshkent"], ["Dilnoza Yusupova", "Toshkent"]],
                    },
                    {
                        "title": "Katta tranzaksiyalar",
                        "slug": "katta-tranzaksiyalar",
                        "description": EXERCISE_COPY["katta-tranzaksiyalar"]["description"],
                        "task": EXERCISE_COPY["katta-tranzaksiyalar"]["task"],
                        "hints": ["To‘lovlar boshqa jadvalda"],
                        "columns": ["id", "amount"],
                        "rows": [[1, 120000], [9, 150000]],
                    },
                ],
                "homework": True,
            },
            {
                "order": 2,
                "title": "Filtrlash va saralash",
                "slug": "filtrlash-va-saralash",
                "description": "WHERE va ORDER BY.",
                "lectures": [
                    {
                        "title": "WHERE operatori",
                        "slug": "where-operatori",
                        "content": LECTURES["where-operatori"],
                        "sql_examples": SQL_EXAMPLES["where-operatori"],
                    },
                    {
                        "title": "ORDER BY",
                        "slug": "order-by",
                        "content": LECTURES["order-by"],
                        "sql_examples": SQL_EXAMPLES["order-by"],
                    },
                    {
                        "title": "Bir nechta shart",
                        "slug": "bir-nechta-shart",
                        "content": LECTURES["bir-nechta-shart"],
                        "sql_examples": SQL_EXAMPLES["bir-nechta-shart"],
                    },
                ],
                "exercises": [
                    {
                        "title": "Debit operatsiyalar",
                        "slug": "debit-operatsiyalar",
                        "description": EXERCISE_COPY["debit-operatsiyalar"]["description"],
                        "task": EXERCISE_COPY["debit-operatsiyalar"]["task"],
                        "hints": ["Operatsiya turini filtrlang"],
                        "columns": ["id", "transaction_type"],
                        "rows": [[1, "debit"], [2, "debit"], [4, "debit"], [5, "debit"], [6, "debit"], [7, "debit"], [9, "debit"], [10, "debit"], [11, "debit"]],
                    },
                    {
                        "title": "Summa bo‘yicha saralash",
                        "slug": "summa-boyicha-saralash",
                        "description": EXERCISE_COPY["summa-boyicha-saralash"]["description"],
                        "task": EXERCISE_COPY["summa-boyicha-saralash"]["task"],
                        "hints": ["Summa bo‘yicha tushing — eng katta tepada"],
                        "require_row_order": True,
                        "columns": ["id", "amount"],
                        "rows": [[9, 150000], [1, 120000], [11, 90000], [3, 80000], [8, 70000], [7, 50000], [2, 45000], [6, 31000], [5, 22000], [10, 20000], [4, 15000], [12, 10000]],
                    },
                    {
                        "title": "Faol mijozlar",
                        "slug": "faol-mijozlar",
                        "description": EXERCISE_COPY["faol-mijozlar"]["description"],
                        "task": EXERCISE_COPY["faol-mijozlar"]["task"],
                        "hints": ["Avval mijoz bo‘yicha sanang, keyin kichiklarini tashlang"],
                        "columns": ["customer_id"],
                        "rows": [[1]],
                    },
                ],
                "homework": True,
            },
            {
                "order": 3,
                "title": "Agregatsiyalar",
                "slug": "agregatsiyalar",
                "description": "COUNT, SUM, AVG.",
                "lectures": [
                    {
                        "title": "COUNT",
                        "slug": "count",
                        "content": LECTURES["count"],
                        "sql_examples": SQL_EXAMPLES["count"],
                    },
                    {
                        "title": "SUM va AVG",
                        "slug": "sum-va-avg",
                        "content": LECTURES["sum-va-avg"],
                        "sql_examples": SQL_EXAMPLES["sum-va-avg"],
                    },
                    {
                        "title": "GROUP BY asoslari",
                        "slug": "group-by-asoslari",
                        "content": LECTURES["group-by-asoslari"],
                        "sql_examples": SQL_EXAMPLES["group-by-asoslari"],
                    },
                ],
                "exercises": [
                    {
                        "title": "Jami summa",
                        "slug": "jami-summa",
                        "description": EXERCISE_COPY["jami-summa"]["description"],
                        "task": EXERCISE_COPY["jami-summa"]["task"],
                        "hints": ["Barcha qatorlardagi summani bir songa yig‘ing", "Ustun nomini total qiling"],
                        "columns": ["total"],
                        "rows": [[703000]],
                    },
                    {
                        "title": "Mijozlar bo‘yicha soni",
                        "slug": "mijozlar-boyicha-soni",
                        "description": EXERCISE_COPY["mijozlar-boyicha-soni"]["description"],
                        "task": EXERCISE_COPY["mijozlar-boyicha-soni"]["task"],
                        "hints": ["Har mijoz uchun qatorlar soni", "Ustun nomini cnt qiling"],
                        "columns": ["customer_id", "cnt"],
                        "rows": [[1, 6], [2, 2], [3, 2], [4, 1], [5, 1]],
                    },
                    {
                        "title": "Mijozlar yig‘indisi",
                        "slug": "mijozlar-yigindisi",
                        "description": EXERCISE_COPY["mijozlar-yigindisi"]["description"],
                        "task": EXERCISE_COPY["mijozlar-yigindisi"]["task"],
                        "hints": ["Har mijoz uchun summalarni yig‘ing", "Ustun nomini total qiling"],
                        "columns": ["customer_id", "total"],
                        "rows": [[1, 313000], [2, 120000], [3, 170000], [4, 90000], [5, 10000]],
                    },
                ],
                "homework": True,
            },
        ]
        HOMEWORK.update(ADVANCED_HOMEWORK)
        LECTURE_PRACTICE.update(ADVANCED_PRACTICE)
        modules_data.extend(build_advanced_modules())

        # Dars mashqlari modul/slug o‘zgarganda eski nusxalar qolmasin
        Exercise.objects.filter(
            module__course=course,
            lecture__isnull=False,
            slug__startswith="lc-",
        ).delete()

        for module_data in modules_data:
            module, _ = Module.objects.update_or_create(
                course=course,
                slug=module_data["slug"],
                defaults={
                    "title": module_data["title"],
                    "description": module_data["description"],
                    "order": module_data["order"],
                    "is_published": True,
                },
            )
            for index, lecture_data in enumerate(module_data["lectures"], start=1):
                lecture, _ = Lecture.objects.update_or_create(
                    module=module,
                    slug=lecture_data["slug"],
                    defaults={
                        "title": lecture_data["title"],
                        "content": lecture_data["content"],
                        "sql_examples": lecture_data["sql_examples"],
                        "order": index,
                        "is_published": True,
                    },
                )
                practice_list = practices_for_lecture(lecture.slug, LECTURE_PRACTICE)
                for p_index, practice in enumerate(practice_list):
                    ds_list = [lc_datasets[name] for name in practice["dataset_names"]]
                    self._upsert_exercise(
                        module,
                        practice,
                        ds_list,
                        lecture=lecture,
                        order=100 + index * 10 + p_index,
                    )
                if module_data.get("homework") and index == 3:
                    HomeworkAssignment.objects.update_or_create(
                        lecture=lecture,
                        defaults={
                            "title": f"{module.title} uy vazifasi",
                            "instructions": HOMEWORK[module.slug],
                            "max_score": 100,
                            "is_published": True,
                        },
                    )
            for index, exercise_data in enumerate(module_data["exercises"], start=1):
                self._upsert_exercise(module, exercise_data, [customers, transactions], order=index)

        # Ensure no leftover empty unpublished stubs for advanced slugs
        for module_data in build_advanced_modules():
            Module.objects.filter(course=course, slug=module_data["slug"]).update(is_published=True)

    def _upsert_exercise(self, module, exercise_data, datasets, lecture=None, order=1):
        kind = exercise_data.get("kind", "sql")
        difficulty = exercise_data.get("difficulty", "easy")
        editorial = exercise_data.get("editorial") or (
            "Yechim yo‘riqnomasi:\n"
            "1) Topshiriqda qaysi ustunlar kerakligini aniqlang.\n"
            "2) Kerakli jadval(lar)ni FROM qismida yozing.\n"
            "3) WHERE / GROUP BY / ORDER BY shartlarini bosqichma-bosqich qo‘shing.\n"
            "4) Natijani kutilgan ustunlar bilan solishtiring."
        )
        exercise, _ = Exercise.objects.update_or_create(
            module=module,
            slug=exercise_data["slug"],
            defaults={
                "title": exercise_data["title"],
                "description": exercise_data["description"],
                "task": exercise_data["task"],
                "hints": exercise_data.get("hints") or [],
                "editorial": editorial,
                "kind": kind,
                "difficulty": difficulty,
                "quiz_options": exercise_data.get("quiz_options") or [],
                "is_skill_test": bool(exercise_data.get("is_skill_test", False)),
                "order": order,
                "is_published": True,
                "require_row_order": exercise_data.get("require_row_order", False),
                "require_column_order": False,
                "max_score": 100,
                "lecture": lecture,
            },
        )
        for dataset in datasets or []:
            ExerciseDataset.objects.get_or_create(exercise=exercise, dataset=dataset)
        ExerciseExpectedResult.objects.update_or_create(
            exercise=exercise,
            defaults={"columns": exercise_data["columns"], "rows": exercise_data["rows"]},
        )
        return exercise

    def _seed_weekly_contest(
        self,
        course: Course,
        *,
        slug: str,
        title: str,
        description: str,
        seed_skill_tests: bool = False,
        limit: int = 8,
    ):
        from datetime import timedelta

        from django.utils import timezone

        from apps.contests.models import Contest, ContestExercise

        now = timezone.now()
        week_start = now - timedelta(days=now.weekday())
        starts = week_start.replace(hour=0, minute=0, second=0, microsecond=0)
        ends = starts + timedelta(days=7)
        contest, _ = Contest.objects.update_or_create(
            slug=slug,
            defaults={
                "title": title,
                "description": description,
                "starts_at": starts,
                "ends_at": ends,
                "is_published": True,
            },
        )
        # Preview (ochiq) modullardan masala tanlash — bepul talaba ham yecha olsin
        preview_ids = access_service.preview_module_ids(course)
        exercises = list(
            Exercise.objects.filter(
                module__course=course,
                module_id__in=preview_ids,
                is_published=True,
                is_skill_test=False,
            ).order_by("difficulty", "order", "id")[:limit]
        )
        if len(exercises) < limit:
            # preview yetmasa — kursdagi boshqa mashqlar
            extra = list(
                Exercise.objects.filter(
                    module__course=course,
                    is_published=True,
                    is_skill_test=False,
                )
                .exclude(pk__in=[e.pk for e in exercises])
                .order_by("module__order", "order", "id")[: limit - len(exercises)]
            )
            exercises.extend(extra)
        ContestExercise.objects.filter(contest=contest).exclude(exercise__in=exercises).delete()
        for index, exercise in enumerate(exercises, start=1):
            ContestExercise.objects.update_or_create(
                contest=contest,
                exercise=exercise,
                defaults={"order": index, "points": 0},
            )
        if seed_skill_tests:
            self._seed_skill_tests(course)
        self.stdout.write(self.style.SUCCESS(f"Musobaqa tayyor: {contest.title} ({len(exercises)} masala)."))

    def _seed_skill_tests(self, course: Course):
        """Har bir SQL moduliga kamida 10 ta 4 variantli bilim testi."""
        from apps.core.sql_skill_tests import MODULE_SKILL_TESTS, skill_tests_for_module

        total = 0
        for module in course.modules.filter(is_published=True).order_by("order"):
            # Eski bitta umumiy testni olib tashlash
            Exercise.objects.filter(module=module, slug=f"{module.slug}-bilim-testi").delete()
            quizzes = skill_tests_for_module(module.slug)
            if not quizzes:
                # Noma’lum modul — kamida SELECT asoslari to‘plamidan nusxa
                quizzes = skill_tests_for_module("sql-asoslari")
                for q in quizzes:
                    q["slug"] = f"bt-{module.slug}-{q['slug'].rsplit('-', 1)[-1]}"
            for index, quiz in enumerate(quizzes, start=1):
                self._upsert_exercise(module, quiz, [], order=900 + index)
                total += 1
        covered = sorted(MODULE_SKILL_TESTS.keys())
        self.stdout.write(
            self.style.SUCCESS(
                f"Bilim testlari yuklandi: {total} ta savol "
                f"({len(covered)} modul uchun maxsus to‘plam)."
            )
        )

    def _seed_python_skill_tests(self, course: Course):
        """Python moduli uchun bilim testlari (SQL bilan bir xil format)."""
        from apps.core.python_skill_tests import MODULE_SKILL_TESTS, skill_tests_for_module

        total = 0
        for module in course.modules.filter(is_published=True).order_by("order"):
            quizzes = skill_tests_for_module(module.slug)
            if not quizzes:
                continue
            for index, quiz in enumerate(quizzes, start=1):
                self._upsert_exercise(module, quiz, [], order=900 + index)
                total += 1
        self.stdout.write(
            self.style.SUCCESS(
                f"Python bilim testlari: {total} ta savol ({len(MODULE_SKILL_TESTS)} modul)."
            )
        )

    def _hide_python_for_release(self, course: Course):
        """Hozirgi release: faqat SQL ochiq — Python kurs va musobaqasini yashirish."""
        from apps.contests.models import Contest

        course.is_visible = False
        course.save(update_fields=["is_visible"])
        updated = Contest.objects.filter(slug="haftalik-python").update(is_published=False)
        self.stdout.write(
            self.style.WARNING(
                f"Release: Python kursi yashirildi (is_visible=False)"
                f"{', musobaqa yopildi' if updated else ''}."
            )
        )

    def _assign_teacher(self, course: Course):
        teacher = User.objects.filter(email="teacher@example.com").first()
        student = User.objects.filter(email="student@example.com").first()
        if teacher:
            profile, _ = TeacherProfile.objects.get_or_create(user=teacher)
            profile.assigned_courses.add(course)
        if student:
            CourseEnrollment.objects.get_or_create(student=student, course=course)
