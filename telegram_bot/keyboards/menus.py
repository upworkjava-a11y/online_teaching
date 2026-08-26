from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

BTN_COURSES = "Kurslar"
BTN_PROGRESS = "Progress"
BTN_SCORES = "Ballar"
BTN_HOMEWORK = "Uy vazifasi"
BTN_ANNOUNCE = "E’lonlar"
BTN_PROFILE = "Profil"
BTN_HELP = "Yordam"
BTN_MESSAGES = "Xabarlar"
BTN_TEACHER = "O‘qituvchi paneli"
BTN_LOGOUT = "Chiqish"
BTN_LOGIN = "Kirish"
BTN_REGISTER = "Ro‘yxatdan o‘tish"
BTN_CANCEL = "Bekor qilish"


def guest_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=BTN_LOGIN), KeyboardButton(text=BTN_REGISTER)],
            [KeyboardButton(text=BTN_HELP)],
        ],
        resize_keyboard=True,
    )


def student_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=BTN_COURSES), KeyboardButton(text=BTN_PROGRESS)],
            [KeyboardButton(text=BTN_SCORES), KeyboardButton(text=BTN_HOMEWORK)],
            [KeyboardButton(text=BTN_ANNOUNCE), KeyboardButton(text=BTN_MESSAGES)],
            [KeyboardButton(text=BTN_PROFILE), KeyboardButton(text=BTN_HELP)],
            [KeyboardButton(text=BTN_LOGOUT)],
        ],
        resize_keyboard=True,
    )


def staff_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=BTN_TEACHER), KeyboardButton(text=BTN_ANNOUNCE)],
            [KeyboardButton(text=BTN_COURSES), KeyboardButton(text=BTN_MESSAGES)],
            [KeyboardButton(text=BTN_PROFILE), KeyboardButton(text=BTN_HELP)],
            [KeyboardButton(text=BTN_LOGOUT)],
        ],
        resize_keyboard=True,
    )


def cancel_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=BTN_CANCEL)]], resize_keyboard=True)


def main_keyboard_for(user) -> ReplyKeyboardMarkup:
    if user is None:
        return guest_keyboard()
    if user.is_teacher or user.is_admin:
        return staff_keyboard()
    return student_keyboard()


def inline_rows(buttons: list[tuple[str, str]], cols: int = 1) -> InlineKeyboardMarkup:
    rows = []
    row = []
    for text, data in buttons:
        row.append(InlineKeyboardButton(text=text, callback_data=data))
        if len(row) >= cols:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    return InlineKeyboardMarkup(inline_keyboard=rows)
