from django.conf import settings
from django.db import migrations, models
from django.db.models import Count


def dedupe_submissions(apps, schema_editor):
    HomeworkSubmission = apps.get_model("homework", "HomeworkSubmission")
    dup_keys = (
        HomeworkSubmission.objects.values("student_id", "assignment_id")
        .annotate(c=Count("id"))
        .filter(c__gt=1)
    )
    for row in dup_keys:
        qs = HomeworkSubmission.objects.filter(
            student_id=row["student_id"],
            assignment_id=row["assignment_id"],
        ).order_by("-created_at", "-id")
        keep_id = qs.first().pk
        qs.exclude(pk=keep_id).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("homework", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(dedupe_submissions, migrations.RunPython.noop),
        migrations.AddConstraint(
            model_name="homeworksubmission",
            constraint=models.UniqueConstraint(
                fields=("student", "assignment"),
                name="homework_one_submission_per_student_assignment",
            ),
        ),
    ]
