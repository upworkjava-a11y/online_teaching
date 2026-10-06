from django.conf import settings
from django.contrib import messages
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from apps.access.services import access_service
from apps.core.i18n.service import t
from apps.core.views import GuestBrowseMixin, RoleRequiredMixin
from apps.courses.models import Lecture
from apps.exercises.models import ExerciseAttempt
from apps.homework.services import homework_service
from apps.learning.python_playground import extract_python_starter
from apps.progress.models import LectureProgress
from apps.progress.services import progress_service
from apps.sandbox.exceptions import SandboxError
from apps.sandbox.python_executor import python_executor


class LectureDetailView(GuestBrowseMixin, View):
    allowed_roles = ("student", "teacher", "admin")

    def get_lecture(self, request, pk):
        lecture = get_object_or_404(
            Lecture.objects.select_related("module", "module__course"),
            pk=pk,
        )
        decision = access_service.evaluate(request.user, lecture)
        return lecture, decision

    def get(self, request, pk):
        lecture, decision = self.get_lecture(request, pk)
        if not decision.allowed:
            if decision.code == "premium":
                return redirect("courses:premium", slug=lecture.module.course.slug)
            return render(request, "core/blocked.html", {"reason": decision.reason}, status=403)
        progress = None
        latest_hw = None
        solved_ids = set()
        if request.user.is_authenticated:
            progress_service.touch_lecture(request.user, lecture)
            progress = LectureProgress.objects.filter(student=request.user, lecture=lecture).first()
            homework = getattr(lecture, "homework_assignment", None)
            latest_hw = homework_service.latest_for_student(request.user, homework) if homework else None
        homework = getattr(lecture, "homework_assignment", None)
        practice = lecture.practice_exercises.filter(is_published=True).order_by("order").first()
        practices = list(lecture.practice_exercises.filter(is_published=True).order_by("order", "id"))
        if request.user.is_authenticated:
            solved_ids = set(
                ExerciseAttempt.objects.filter(
                    student=request.user,
                    exercise_id__in=[ex.pk for ex in practices],
                    is_correct=True,
                ).values_list("exercise_id", flat=True)
            )
        practice_left = bool(practices) and any(ex.pk not in solved_ids for ex in practices)
        previous = lecture.get_previous()
        next_item = lecture.get_next()
        next_allowed = bool(next_item) and access_service.can_access(request.user, next_item)
        is_python = lecture.module.course.slug == "python"
        python_starter = ""
        if is_python:
            python_starter = extract_python_starter(
                lecture.content or "",
                lecture.sql_examples or [],
            )
        return render(
            request,
            "learning/lecture.html",
            {
                "lecture": lecture,
                "progress": progress,
                "previous": previous,
                "next_item": next_item if next_allowed else None,
                "next_locked": bool(next_item) and not next_allowed,
                "homework": homework,
                "latest_hw": latest_hw,
                "practice": practice,
                "practices": practices,
                "solved_ids": solved_ids,
                "practice_left": practice_left,
                "is_python_course": is_python,
                "python_starter": python_starter,
            },
        )


class RunPythonLectureView(RoleRequiredMixin, View):
    """Run a short Python snippet for Python-course lessons (like SQL sandbox)."""

    allowed_roles = ("student", "teacher", "admin")
    auth_gate_title = "Python kodini ishga tushirish uchun hisob kerak"
    auth_gate_message = (
        "Darsdagi Python sandboxdan foydalanish uchun tizimga kiring yoki ro‘yxatdan o‘ting."
    )

    def post(self, request, pk):
        lecture = get_object_or_404(
            Lecture.objects.select_related("module", "module__course"),
            pk=pk,
        )
        if lecture.module.course.slug != "python":
            return JsonResponse(
                {"ok": False, "error": t("Bu sandbox faqat Python kursi uchun.")},
                status=400,
            )
        decision = access_service.evaluate(request.user, lecture)
        if not decision.allowed:
            return JsonResponse({"ok": False, "error": decision.reason}, status=403)

        cache_key = f"py-rate:{request.user.pk}"
        current = cache.get(cache_key, 0)
        limit = int(getattr(settings, "PYTHON_RATE_LIMIT_PER_MINUTE", 30))
        if current >= limit:
            return JsonResponse(
                {"ok": False, "error": t("Juda ko‘p so‘rov. Biroz kuting.")},
                status=429,
            )
        cache.set(cache_key, current + 1, 60)

        code = request.POST.get("code") or ""
        try:
            result = python_executor.execute(code)
        except SandboxError as exc:
            return JsonResponse(
                {"ok": False, "error": str(exc.message), "stdout": "", "stderr": ""}
            )

        return JsonResponse(
            {
                "ok": result.ok,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "execution_ms": result.execution_ms,
                "error": ""
                if result.ok
                else (result.stderr.strip().splitlines() or ["Xato"])[-1],
            }
        )


class CompleteLectureView(RoleRequiredMixin, View):
    allowed_roles = ("student",)
    auth_gate_title = "Darsni belgilash uchun hisob kerak"
    auth_gate_message = (
        "Darsni tugallangan deb belgilash, progress saqlash uchun tizimga kiring yoki ro‘yxatdan o‘ting."
    )

    def post(self, request, pk):
        lecture = get_object_or_404(Lecture.objects.select_related("module", "module__course"), pk=pk)
        decision = access_service.evaluate(request.user, lecture)
        if not decision.allowed:
            return render(request, "core/blocked.html", {"reason": decision.reason}, status=403)
        progress_service.complete_lecture(request.user, lecture)
        practices = list(lecture.practice_exercises.filter(is_published=True))
        if practices:
            solved = set(
                ExerciseAttempt.objects.filter(
                    student=request.user,
                    exercise_id__in=[ex.pk for ex in practices],
                    is_correct=True,
                ).values_list("exercise_id", flat=True)
            )
            if any(ex.pk not in solved for ex in practices):
                messages.info(
                    request,
                    t(
                        "Dars o‘qildi. Endi amaliyotni yeching — shunda dars to‘liq tugallangan hisoblanadi."
                    ),
                )
                return redirect("learning:lecture", pk=lecture.pk)
        messages.success(request, t("Ma’ruza tugallandi."))
        nxt = lecture.get_next()
        if nxt and access_service.can_access(request.user, nxt):
            return redirect("learning:lecture", pk=nxt.pk)
        if nxt:
            messages.info(
                request,
                t("Keyingi modullar Premium. To‘liq kurs uchun admin ruxsati kerak."),
            )
        return redirect("courses:detail", slug=lecture.course.slug)
