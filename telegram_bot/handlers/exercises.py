from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from telegram_bot.keyboards.menus import cancel_keyboard, inline_rows, main_keyboard_for
from telegram_bot.services.platform import exercise_payload, run_sql
from telegram_bot.services.users import get_user_by_telegram
from telegram_bot.utils.states import LearnFSM
from telegram_bot.utils.text import tg_escape

router = Router()


@router.callback_query(F.data.startswith("ex:"))
async def open_exercise(query: CallbackQuery, state: FSMContext):
    user = await get_user_by_telegram(query.from_user.id)
    if not user:
        await query.answer("Avval kiring", show_alert=True)
        return
    exercise_id = int(query.data.split(":")[1])
    data = await exercise_payload(user, exercise_id)
    if not data:
        await query.message.answer("Mashq topilmadi.")
        await query.answer()
        return
    if data.get("error"):
        await query.message.answer(data["error"])
        await query.answer()
        return
    solved = "Ha" if data["solved"] else "Yo‘q"
    preview_lines = []
    for item in data["previews"][:2]:
        prev = item.get("preview") or {}
        cols = prev.get("columns") or []
        rows = prev.get("rows") or []
        preview_lines.append(f"{item['name']}: {', '.join(str(c) for c in cols)}")
        for row in rows[:3]:
            preview_lines.append("  " + " | ".join(str(c) for c in row))
    text = (
        f"<b>{tg_escape(data['title'])}</b>\n"
        f"Yechilgan (veb/bot): {solved}\n\n"
        f"{tg_escape(data['description'][:1500])}\n\n"
        f"<b>Topshiriq:</b> {tg_escape(data['task'])}\n"
        f"Jadvallar: {', '.join(data['tables'])}\n"
    )
    if preview_lines:
        text += "\nNamuna:\n" + "\n".join(preview_lines)
    buttons = [("SQL yuborish", f"sql:{data['id']}")]
    if data["lecture_id"]:
        buttons.append(("Darsga qaytish", f"lec:{data['lecture_id']}"))
    await query.message.answer(text[:4000], reply_markup=inline_rows(buttons))
    await query.answer()


@router.callback_query(F.data.startswith("sql:"))
async def start_sql(query: CallbackQuery, state: FSMContext):
    user = await get_user_by_telegram(query.from_user.id)
    if not user:
        await query.answer("Avval kiring", show_alert=True)
        return
    exercise_id = int(query.data.split(":")[1])
    await state.set_state(LearnFSM.sql)
    await state.update_data(exercise_id=exercise_id)
    await query.message.answer(
        "SQL so‘rovini yuboring (faqat SELECT). Natija veb-sandbox bilan bir xil tekshiriladi.",
        reply_markup=cancel_keyboard(),
    )
    await query.answer()


@router.message(LearnFSM.sql)
async def receive_sql(message: Message, state: FSMContext):
    user = await get_user_by_telegram(message.from_user.id)
    if not user:
        await state.clear()
        return
    data = await state.get_data()
    result = await run_sql(user, int(data["exercise_id"]), message.text or "")
    await state.clear()
    if not result.get("ok"):
        await message.answer(result.get("message") or "Xato", reply_markup=main_keyboard_for(user))
        return
    if result["correct"]:
        msg = f"✅ To‘g‘ri! Ball: {result['score']}\nBu natija vebda ham saqlanadi."
    else:
        msg = f"❌ Noto‘g‘ri.\n{result.get('message') or ''}"
    if result.get("table"):
        msg += "\n\n<pre>" + tg_escape(result["table"][:1500]) + "</pre>"
    await message.answer(msg, reply_markup=main_keyboard_for(user))
