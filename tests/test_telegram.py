from django.test import TestCase

from apps.accounts.models import TelegramAccount, User
from tests.helpers import make_user


class TelegramAccountTests(TestCase):
    def test_one_telegram_one_django_user(self):
        user = make_user("web@test.com")
        TelegramAccount.objects.create(user=user, telegram_id=111, telegram_username="ali")
        self.assertEqual(TelegramAccount.objects.get(telegram_id=111).user.email, "web@test.com")
        self.assertEqual(user.telegram_account.telegram_id, 111)
