from aiogram import Bot, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from telegram_bot.keyboards.menus import BTN_TEACHER, cancel_keyboard, inline_rows, main_keyboard_for
from telegram_bot.services.platform import (
    pending_homework,
    publish_announcement,
    review_homework,
    send_direct,
    teacher_overview,
    teacher_student_list,
)
from telegram_bot.services.users import get_user_by_telegram
from telegram_bot.utils.states import LearnFSM
from telegram_bot.utils.text import tg_escape

router = Router()


def _staff(user) -> bool:
    return bool(user and (user.is_teacher or user.is_admin))


@router.message(F.text == BTN_TEACHER)
async def teacher_home(message: Message):
    user = await get_user_by_telegram(message.from_user.id)
    if not _staff(user):
        await message.answer("Bu bo‘lim faqat o‘qituvchi/admin uchun.")
        return
    ov = await teacher_overview(user)
    text = (
        "<b>O‘qituvchi paneli</b> (veb /teacher bilan bir xil ma’lumot)\n\n"
        f"Talabalar: {ov['total_students']}\n"
        f"Faol (7 kun): {ov['active_students']}\n"
        f"O‘rtacha ball: {ov['average_score']}%\n"
        f"Kutayotgan uy vazifasi: {ov['pending_reviews']}"
    )
    buttons = [
        ("Talabalar", "t:students"),
        ("Topshiriqlar", "t:hw"),
        ("Xabar yuborish", "t:msg"),
        ("E’lon", "t:ann"),
    ]
    await message.answer(text, reply_markup=inline_rows(buttons, cols=2))


@router.callback_query(F.data == "t:students")
async def t_students(query: CallbackQuery):
    user = await get_user_by_telegram(query.from_user.id)
    if not _staff(user):
        await query.answer("Ruxsat yo‘q", show_alert=True)
        return
    rows = await teacher_student_list(user)
    if not rows:
        await query.message.answer("Talaba yo‘q.")
        await query.answer()
        return
    lines = ["<b>Talabalar monitoringi</b>\n"]
    buttons = []
    for r in rows:
        lines.append(f"• {tg_escape(r['name'])} — {r['percent']}% · ball {r['score']}% · HV: {r['hw']}")
        buttons.append((r["name"][:32], f"tstu:{r['id']}"))
    await query.message.answer("\n".join(lines)[:4000], reply_markup=inline_rows(buttons))
    await query.answer()


@router.callback_query(F.data.startswith("tstu:"))
async def t_pick_student(query: CallbackQuery, state: FSMContext):
    user = await get_user_by_telegram(query.from_user.id)
    if not _staff(user):
        await query.answer("Ruxsat yo‘q", show_alert=True)
        return
    sid = int(query.data.split(":")[1])
    await state.set_state(LearnFSM.teacher_msg)
    await state.update_data(student_id=sid)
    await query.message.answer("Talabaga xabar matnini yozing.", reply_markup=cancel_keyboard())
    await query.answer()


@router.message(LearnFSM.teacher_msg)
async def t_send_msg(message: Message, state: FSMContext, bot: Bot):
    user = await get_user_by_telegram(message.from_user.id)
    if not _staff(user):
        await state.clear()
        return
    data = await state.get_data()
    await state.clear()
    code, tg_id = await send_direct(user, int(data["student_id"]), message.text or "")
    if code != "ok":
        await message.answer("Talaba topilmadi.", reply_markup=main_keyboard_for(user))
        return
    if tg_id:
        try:
            await bot.send_message(tg_id, f"O‘qituvchidan xabar:\n{message.text}")
        except Exception:
            pass
    await message.answer("Xabar saqlandi (veb xabarlarida ham).", reply_markup=main_keyboard_for(user))


@router.callback_query(F.data == "t:msg")
async def t_msg_hint(query: CallbackQuery):
    await query.message.answer("Avval «Talabalar» dan talabani tanlang, keyin xabar yozing.")
    await query.answer()


@router.callback_query(F.data == "t:hw")
async def t_hw(query: CallbackQuery):
    user = await get_user_by_telegram(query.from_user.id)
    if not _staff(user):
        await query.answer("Ruxsat yo‘q", show_alert=True)
        return
    rows = await pending_homework(user)
    if not rows:
        await query.message.answer("Kutayotgan topshiriq yo‘q.")
        await query.answer()
        return
    buttons = [(f"{r['student'][:20]} · {r['title'][:20]}", f"trev:{r['id']}") for r in rows]
    await query.message.answer("Tekshirish uchun tanlang:", reply_markup=inline_rows(buttons))
    await query.answer()


@router.callback_query(F.data.startswith("trev:"))
async def t_rev_start(query: CallbackQuery, state: FSMContext):
    await state.set_state(LearnFSM.review_score)
    await state.update_data(submission_id=int(query.data.split(":")[1]))
    await query.message.answer("Ballni yozing (0–100).", reply_markup=cancel_keyboard())
    await query.answer()


@router.message(LearnFSM.review_score)
async def t_rev_score(message: Message, state: FSMContext):
    try:
        score = int((message.text or "").strip())
    except ValueError:
        await message.answer("Raqam yozing.")
        return
    await state.update_data(score=score)
    await state.set_state(LearnFSM.review_feedback)
    await message.answer("Izoh / feedback yozing.")


@router.message(LearnFSM.review_feedback)
async def t_rev_feedback(message: Message, state: FSMContext):
    user = await get_user_by_telegram(message.from_user.id)
    data = await state.get_data()
    await state.clear()
    code = await review_homework(user, int(data["submission_id"]), int(data["score"]), message.text or "")
    await message.answer("Tekshirildi." if code == "ok" else code, reply_markup=main_keyboard_for(user))


@router.callback_query(F.data == "t:ann")
async def t_ann(query: CallbackQuery, state: FSMContext):
    user = await get_user_by_telegram(query.from_user.id)
    if not _staff(user):
        await query.answer("Ruxsat yo‘q", show_alert=True)
        return
    await state.set_state(LearnFSM.announce_title)
    await query.message.answer("E’lon sarlavhasi:", reply_markup=cancel_keyboard())
    await query.answer()


@router.message(LearnFSM.announce_title)
async def t_ann_title(message: Message, state: FSMContext):
    await state.update_data(title=(message.text or "").strip())
    await state.set_state(LearnFSM.announce_body)
    await message.answer("E’lon matni:")


@router.message(LearnFSM.announce_body)
async def t_ann_body(message: Message, state: FSMContext, bot: Bot):
    user = await get_user_by_telegram(message.from_user.id)
    data = await state.get_data()
    await state.clear()
    ids = await publish_announcement(user, data.get("title") or "E’lon", message.text or "")
    text = f"<b>{tg_escape(data.get('title') or 'E’lon')}</b>\n{message.text}"
    for tid in ids:
        try:
            await bot.send_message(tid, "Yangi e’lon:\n" + text[:3500])
        except Exception:
            pass
    await message.answer(f"E’lon chiqarildi. {len(ids)} ta Telegram foydalanuvchiga yuborildi.", reply_markup=main_keyboard_for(user))
