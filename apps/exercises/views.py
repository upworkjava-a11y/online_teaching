from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from apps.access.services import OPEN_COURSE_SLUGS, access_service
from apps.core.i18n.service import t
from apps.core.views import GuestBrowseMixin, RoleRequiredMixin
from apps.courses.models import Course, Module
from apps.progress.models import CourseProgress

from .models import Exercise, ExerciseAttempt, ExerciseComment
from .navigation import exercise_nav_context
from .services import RateLimited, exercise_service

DIFFICULTY_FILTERS = {
    "": "Barchasi",
    "easy": "Oson",
    "medium": "O‘rta",
    "hard": "Qiyin",
}


class PracticeCatalogView(GuestBrowseMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def get(self, request):
        difficulty = request.GET.get("difficulty", "")
        course_slug = (request.GET.get("course") or "").strip()
        q = (request.GET.get("q") or "").strip()
        status = request.GET.get("status", "")
        open_courses = list(
            Course.objects.filter(slug__in=OPEN_COURSE_SLUGS, is_published=True, is_visible=True).order_by("order")
        )
        qs = (
            Exercise.objects.filter(is_published=True, is_skill_test=False)
            .select_related("module", "module__course", "lecture")
            .order_by("module__course__order", "module__order", "order", "id")
        )
        # Faqat ochiq kurslar (SQL, Python, …)
        qs = qs.filter(module__course__slug__in=OPEN_COURSE_SLUGS)
        if course_slug in OPEN_COURSE_SLUGS:
            qs = qs.filter(module__course__slug=course_slug)
        if difficulty in DIFFICULTY_FILTERS and difficulty:
            qs = qs.filter(difficulty=difficulty)
        if q:
            qs = qs.filter(
                Q(title__icontains=q)
                | Q(task__icontains=q)
                | Q(module__title__icontains=q)
                | Q(module__course__title__icontains=q)
            )

        solved_ids = set()
        if request.user.is_authenticated and request.user.is_student:
            solved_ids = set(
                ExerciseAttempt.objects.filter(student=request.user, is_correct=True).values_list(
                    "exercise_id", flat=True
                )
            )
            if status == "solved":
                qs = qs.filter(pk__in=solved_ids)
            elif status == "unsolved":
                qs = qs.exclude(pk__in=solved_ids)

        visible = []
        user = request.user
        staff_bypass = user.is_authenticated and (user.is_teacher or user.is_admin)
        for exercise in qs:
            if staff_bypass:
                locked = False
            else:
                locked = not access_service.can_access(user, exercise)
            # Solved/unsolved filter only applies to tasks the user can open
            if status in ("solved", "unsolved") and locked:
                continue
            visible.append({"exercise": exercise, "locked": locked})

        paginator = Paginator(visible, 20)
        page = paginator.get_page(request.GET.get("page"))
        return render(
            request,
            "exercises/catalog.html",
            {
                "page": page,
                "difficulty": difficulty,
                "difficulty_filters": DIFFICULTY_FILTERS,
                "course_slug": course_slug,
                "open_courses": open_courses,
                "q": q,
                "status": status,
                "solved_ids": solved_ids,
            },
        )


class ExerciseDetailView(RoleRequiredMixin, View):
    allowed_roles = ("student", "teacher", "admin")
    template_name = "exercises/detail.html"
    auth_gate_title = "Masalani yechish uchun hisob kerak"
    auth_gate_message = (
        "SQL mashqlari va testlarni yechish, natijani saqlash uchun tizimga kiring yoki ro‘yxatdan o‘ting."
    )

    def get_exercise(self, request, pk):
        exercise = get_object_or_404(
            Exercise.objects.select_related("module", "module__course", "lecture", "expected_result"),
            pk=pk,
        )
        decision = access_service.evaluate(request.user, exercise)
        if not decision.allowed:
            return None, decision
        if not exercise.is_published and decision.code != "explicit_allow":
            return None, decision
        return exercise, decision

    def _context(self, request, exercise, attempts, last_sql, latest_attempt):
        solved = ExerciseAttempt.objects.filter(
            student=request.user,
            exercise=exercise,
            is_correct=True,
        ).exists()
        comments = (
            ExerciseComment.objects.filter(exercise=exercise, is_hidden=False)
            .select_related("author")
            .order_by("created_at")[:50]
        )
        context = {
            "exercise": exercise,
            "attempts": attempts,
            "last_sql": last_sql,
            "datasets": exercise.datasets.all(),
            "latest_attempt": latest_attempt,
            "exercise_solved": solved,
            "comments": comments,
        }
        if solved:
            context.update(exercise_nav_context(request.user, exercise))
        else:
            context["next_exercise"] = None
            context["next_lecture"] = None
        return context

    def get(self, request, pk):
        exercise, decision = self.get_exercise(request, pk)
        if exercise is None:
            if decision and decision.code == "premium":
                exercise_obj = get_object_or_404(
                    Exercise.objects.select_related("module", "module__course"),
                    pk=pk,
                )
                return redirect("courses:premium", slug=exercise_obj.module.course.slug)
            return render(request, "core/blocked.html", {"reason": decision.reason}, status=403)
        attempts = ExerciseAttempt.objects.filter(student=request.user, exercise=exercise)[:10]
        if exercise.kind == Exercise.Kind.QUIZ:
            last_sql = attempts[0].sql_query if attempts else ""
        else:
            last_sql = attempts[0].sql_query if attempts else "SELECT "
        CourseProgress.objects.update_or_create(
            student=request.user,
            course=exercise.course,
            defaults={},
        )
        return render(
            request,
            self.template_name,
            self._context(request, exercise, attempts, last_sql, attempts[0] if attempts else None),
        )

    def post(self, request, pk):
        exercise, decision = self.get_exercise(request, pk)
        if exercise is None:
            if decision and decision.code == "premium":
                exercise_obj = get_object_or_404(
                    Exercise.objects.select_related("module", "module__course"),
                    pk=pk,
                )
                return redirect("courses:premium", slug=exercise_obj.module.course.slug)
            return render(request, "core/blocked.html", {"reason": decision.reason}, status=403)

        action = request.POST.get("action", "run")
        if action == "comment":
            body = (request.POST.get("body") or "").strip()
            if len(body) < 3:
                messages.error(request, t("Izoh juda qisqa. Kamida 3 ta belgi yozing."))
            elif len(body) > 2000:
                messages.error(request, t("Izoh juda uzun (maksimum 2000 belgi)."))
            else:
                ExerciseComment.objects.create(exercise=exercise, author=request.user, body=body)
                messages.success(request, t("Izohingiz qo‘shildi."))
            return redirect("exercises:detail", pk=exercise.pk)

        if exercise.kind == Exercise.Kind.QUIZ:
            submission = request.POST.get("answer", "")
        else:
            submission = request.POST.get("sql", "")
        try:
            attempt = exercise_service.run(request.user, exercise, submission)
        except RateLimited as exc:
            messages.error(request, exc.message)
            return redirect("exercises:detail", pk=exercise.pk)

        attempts = ExerciseAttempt.objects.filter(student=request.user, exercise=exercise)[:10]
        context = self._context(request, exercise, attempts, submission, attempt)
        if request.htmx:
            return render(request, "exercises/partials/result.html", context)
        return render(request, self.template_name, context)


class SkillTestListView(RoleRequiredMixin, View):
    allowed_roles = ("student", "teacher", "admin")
    auth_gate_title = "Bilim testi uchun hisob kerak"
    auth_gate_message = (
        "Modul bilim testini boshlash va natijani ko‘rish uchun tizimga kiring yoki ro‘yxatdan o‘ting."
    )

    def get(self, request, module_id):
        module = get_object_or_404(Module.objects.select_related("course"), pk=module_id)
        if not access_service.can_take_skill_test(request.user, module):
            return render(
                request,
                "core/blocked.html",
                {"reason": t("Bu modul bilim testi Premium. To‘liq kurs ochilgach yoki dastlabki 5 modulda mavjud.")},
                status=403,
            )
        tests = list(
            Exercise.objects.filter(module=module, is_published=True, is_skill_test=True).order_by("order", "id")
        )
        solved_ids = set(
            ExerciseAttempt.objects.filter(
                student=request.user, exercise_id__in=[t.pk for t in tests], is_correct=True
            ).values_list("exercise_id", flat=True)
        )
        return render(
            request,
            "exercises/skill_tests.html",
            {
                "module": module,
                "tests": tests,
                "solved_ids": solved_ids,
                "done_count": len(solved_ids),
                "total_count": len(tests),
            },
        )
