import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_googleaccount"),
    ]

    operations = [
        migrations.CreateModel(
            name="TelegramAccount",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("telegram_id", models.BigIntegerField(unique=True)),
                ("telegram_username", models.CharField(blank=True, max_length=255)),
                ("notify_enabled", models.BooleanField(default=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="telegram_account",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Telegram hisobi",
                "verbose_name_plural": "Telegram hisoblari",
            },
        ),
        migrations.AddIndex(
            model_name="telegramaccount",
            index=models.Index(fields=["telegram_id"], name="accounts_te_telegra_idx"),
        ),
        migrations.CreateModel(
            name="Announcement",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=200)),
                ("body", models.TextField()),
                ("is_published", models.BooleanField(default=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="announcements",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["-created_at"], "verbose_name": "E’lon", "verbose_name_plural": "E’lonlar"},
        ),
        migrations.CreateModel(
            name="DirectMessage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("body", models.TextField()),
                ("read_at", models.DateTimeField(blank=True, null=True)),
                (
                    "recipient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_messages",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_messages",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["-created_at"], "verbose_name": "Xabar", "verbose_name_plural": "Xabarlar"},
        ),
        migrations.CreateModel(
            name="SupportTicket",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("message", models.TextField()),
                ("reply", models.TextField(blank=True)),
                ("is_resolved", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="support_tickets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Yordam so‘rovi",
                "verbose_name_plural": "Yordam so‘rovlari",
            },
        ),
    ]
