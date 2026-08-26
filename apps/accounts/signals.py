from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import StudentProfile, TeacherProfile, User


@receiver(post_save, sender=User)
def ensure_role_profile(sender, instance, created, **kwargs):
    if instance.role == User.Role.STUDENT:
        StudentProfile.objects.get_or_create(user=instance)
        if created:
            from apps.courses.models import Course, CourseEnrollment

            for course in Course.objects.filter(is_published=True, is_visible=True):
                CourseEnrollment.objects.get_or_create(student=instance, course=course)
    elif instance.role == User.Role.TEACHER:
        TeacherProfile.objects.get_or_create(user=instance)
        if created:
            User.objects.filter(pk=instance.pk).update(is_staff=False)
    elif instance.role == User.Role.ADMIN:
        if not instance.is_staff:
            User.objects.filter(pk=instance.pk).update(is_staff=True, is_superuser=True)
