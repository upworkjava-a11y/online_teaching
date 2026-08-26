from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_telegram_messaging"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_premium",
            field=models.BooleanField(
                default=False,
                help_text="Belgilansa, foydalanuvchi har bir kursning barcha darslarini ochadi. Belgilanmasa — faqat dastlabki 3 dars.",
                verbose_name="Premium",
            ),
        ),
    ]
