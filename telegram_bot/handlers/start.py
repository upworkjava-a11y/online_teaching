from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from telegram_bot.keyboards.menus import (
    BTN_CANCEL,
    BTN_HELP,
    guest_keyboard,
    main_keyboard_for,
)
from telegram_bot.services.users import get_user_by_telegram

router = Router()

HELP = (
    "Bu bot va veb-platforma <b>bir xil akkaunt</b>dan foydalanadi.\n\n"
    "• Telegramda kirish/ro‘yxatdan o‘tish — Django foydalanuvchisi\n"
    "• Darslar, mashqlar, ballar va progress vebda ham ko‘rinadi\n"
    "• Vebda qilgan ishingiz shu yerda yangilanadi\n\n"
    "Buyruqlar: /start /help /menu\n"
    "Veb: http://127.0.0.1:8000"
)


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    user = await get_user_by_telegram(message.from_user.id)
    if user:
        role = user.get_role_display()
        await message.answer(
            f"Salom, {user.get_full_name()}!\nRol: {role}\nVeb va Telegram — bitta akkaunt.",
            reply_markup=main_keyboard_for(user),
        )
        return
    await message.answer(
        "Data Analytics o‘quv platformasi.\nAvval kirish yoki ro‘yxatdan o‘ting. "
        "Email/parol veb-saytdagi bilan bir xil.",
        reply_markup=guest_keyboard(),
    )


@router.message(Command("help"))
@router.message(F.text == BTN_HELP)
async def cmd_help(message: Message):
    await message.answer(HELP)


@router.message(Command("menu"))
async def cmd_menu(message: Message):
    user = await get_user_by_telegram(message.from_user.id)
    await message.answer("Menyu", reply_markup=main_keyboard_for(user))


@router.message(F.text == BTN_CANCEL)
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    user = await get_user_by_telegram(message.from_user.id)
    await message.answer("Bekor qilindi.", reply_markup=main_keyboard_for(user))
