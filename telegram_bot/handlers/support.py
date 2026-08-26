from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from telegram_bot.keyboards.menus import cancel_keyboard, main_keyboard_for
from telegram_bot.services.platform import create_support
from telegram_bot.services.users import get_user_by_telegram
from telegram_bot.utils.states import LearnFSM

router = Router()


@router.message(Command("support"))
async def support_start(message: Message, state: FSMContext):
    user = await get_user_by_telegram(message.from_user.id)
    if not user:
        await message.answer("Avval kiring.")
        return
    await state.set_state(LearnFSM.support)
    await message.answer("Savolingizni yozing. O‘qituvchi/admin veb-admin panelida ko‘radi.", reply_markup=cancel_keyboard())


@router.message(LearnFSM.support)
async def support_save(message: Message, state: FSMContext):
    user = await get_user_by_telegram(message.from_user.id)
    await state.clear()
    pk = await create_support(user, message.text or "")
    await message.answer(f"So‘rov #{pk} qabul qilindi.", reply_markup=main_keyboard_for(user))
