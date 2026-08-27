from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_premium_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_premium",
            field=models.BooleanField(
                default=False,
                help_text=(
                    "Belgilansa, foydalanuvchi har bir kursning barcha modullarini ochadi. "
                    "Belgilanmasa — faqat dastlabki 5 modul."
                ),
                verbose_name="Premium",
            ),
        ),
    ]
