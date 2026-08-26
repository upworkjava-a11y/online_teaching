from __future__ import annotations

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from telegram_bot.config import BOT_TOKEN
from telegram_bot.handlers import auth, exercises, homework, learning, start, student, support, teacher

logging.basicConfig(level=logging.INFO, stream=sys.stdout)


async def main() -> None:
    if not BOT_TOKEN:
        raise SystemExit("TELEGRAM_BOT_TOKEN .env faylida yo‘q. BotFather dan token qo‘ying.")
    bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(start.router)
    dp.include_router(auth.router)
    dp.include_router(student.router)
    dp.include_router(learning.router)
    dp.include_router(exercises.router)
    dp.include_router(homework.router)
    dp.include_router(teacher.router)
    dp.include_router(support.router)
    # Local polling conflicts with an active webhook (e.g. old hosting).
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
