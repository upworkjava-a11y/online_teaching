from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exercises", "0003_exercise_kind_quiz"),
    ]

    operations = [
        migrations.AddField(
            model_name="exercise",
            name="difficulty",
            field=models.CharField(
                choices=[("easy", "Easy"), ("medium", "Medium"), ("hard", "Hard")],
                db_index=True,
                default="easy",
                max_length=10,
            ),
        ),
    ]
