from asgiref.sync import sync_to_async

from apps.accounts.models import TelegramAccount


@sync_to_async
def enabled_telegram_ids() -> list[int]:
    return list(TelegramAccount.objects.filter(notify_enabled=True).values_list("telegram_id", flat=True))
