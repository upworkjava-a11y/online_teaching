import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
        ("exercises", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="exercise",
            name="lecture",
            field=models.ForeignKey(
                blank=True,
                help_text="Darsga biriktirilgan amaliy mashq",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="practice_exercises",
                to="courses.lecture",
            ),
        ),
    ]
