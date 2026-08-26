from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from telegram_bot.keyboards.menus import (
    BTN_LOGIN,
    BTN_LOGOUT,
    BTN_REGISTER,
    cancel_keyboard,
    guest_keyboard,
    main_keyboard_for,
)
from telegram_bot.services.users import get_user_by_telegram, login_user, register_user, unlink_telegram
from telegram_bot.utils.states import AuthFSM

router = Router()


@router.message(F.text == BTN_LOGIN)
async def login_start(message: Message, state: FSMContext):
    if await get_user_by_telegram(message.from_user.id):
        await message.answer("Siz allaqachon kirdingiz.")
        return
    await state.set_state(AuthFSM.login_email)
    await message.answer("Email manzilingizni yuboring (veb-saytdagi bilan bir xil).", reply_markup=cancel_keyboard())


@router.message(AuthFSM.login_email)
async def login_email(message: Message, state: FSMContext):
    await state.update_data(email=(message.text or "").strip())
    await state.set_state(AuthFSM.login_password)
    await message.answer("Parolni yuboring.")


@router.message(AuthFSM.login_password)
async def login_password(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    code, user = await login_user(
        data.get("email", ""),
        message.text or "",
        message.from_user.id,
        message.from_user.username or "",
    )
    errors = {
        "bad_password": "Email yoki parol noto‘g‘ri.",
        "blocked": "Hisob bloklangan.",
        "bu_telegram_boshqa_akkaunt": "Bu Telegram boshqa akkauntga bog‘langan.",
        "akkaunt_boshqa_telegram": "Bu email boshqa Telegramga bog‘langan.",
    }
    if code != "ok":
        await message.answer(errors.get(code, "Kirish muvaffaqiyatsiz."), reply_markup=guest_keyboard())
        return
    await message.answer(
        f"Xush kelibsiz, {user.get_full_name()}!\nEndi veb va Telegram bir xil akkaunt.",
        reply_markup=main_keyboard_for(user),
    )


@router.message(F.text == BTN_REGISTER)
async def reg_start(message: Message, state: FSMContext):
    if await get_user_by_telegram(message.from_user.id):
        await message.answer("Siz allaqachon kirdingiz.")
        return
    await state.set_state(AuthFSM.reg_first)
    await message.answer("Ismingizni yozing.", reply_markup=cancel_keyboard())


@router.message(AuthFSM.reg_first)
async def reg_first(message: Message, state: FSMContext):
    await state.update_data(first_name=(message.text or "").strip())
    await state.set_state(AuthFSM.reg_last)
    await message.answer("Familiyangizni yozing.")


@router.message(AuthFSM.reg_last)
async def reg_last(message: Message, state: FSMContext):
    await state.update_data(last_name=(message.text or "").strip())
    await state.set_state(AuthFSM.reg_email)
    await message.answer("Email (veb-saytga kirish uchun ham shu ishlatiladi).")


@router.message(AuthFSM.reg_email)
async def reg_email(message: Message, state: FSMContext):
    await state.update_data(email=(message.text or "").strip())
    await state.set_state(AuthFSM.reg_password)
    await message.answer("Parol (kamida 10 belgi). Shu parol bilan vebga ham kirasiz.")


@router.message(AuthFSM.reg_password)
async def reg_password(message: Message, state: FSMContext):
    await state.update_data(password=message.text or "")
    await state.set_state(AuthFSM.reg_password2)
    await message.answer("Parolni qayta yozing.")


@router.message(AuthFSM.reg_password2)
async def reg_password2(message: Message, state: FSMContext):
    data = await state.get_data()
    if (message.text or "") != data.get("password"):
        await message.answer("Parollar mos kelmadi. Qaytadan /start")
        await state.clear()
        return
    await state.clear()
    code, user = await register_user(
        data.get("first_name", ""),
        data.get("last_name", ""),
        data.get("email", ""),
        data.get("password", ""),
        message.from_user.id,
        message.from_user.username or "",
    )
    if code == "email_exists":
        await message.answer("Bu email allaqachon bor. Kirish tugmasini bosing.", reply_markup=guest_keyboard())
        return
    if code.startswith("weak_password:"):
        await message.answer(code.replace("weak_password:", "Parol zaif: "), reply_markup=guest_keyboard())
        return
    if code != "ok":
        await message.answer("Ro‘yxatdan o‘tishda xato.", reply_markup=guest_keyboard())
        return
    await message.answer(
        f"Akkaunt yaratildi: {user.email}\nVeb-saytga shu email/parol bilan kiring.",
        reply_markup=main_keyboard_for(user),
    )


@router.message(F.text == BTN_LOGOUT)
async def logout(message: Message, state: FSMContext):
    await state.clear()
    await unlink_telegram(message.from_user.id)
    await message.answer(
        "Telegram bog‘lanishi yechildi. Django akkauntingiz saqlanadi — vebda kirish o‘zgarishsiz.",
        reply_markup=guest_keyboard(),
    )
