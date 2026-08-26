from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from telegram_bot.keyboards.menus import inline_rows
from telegram_bot.services.platform import complete_lecture, lecture_payload
from telegram_bot.services.users import get_user_by_telegram
from telegram_bot.utils.text import extract_links, html_to_text, tg_escape

router = Router()


@router.callback_query(F.data.startswith("lec:"))
async def open_lecture(query: CallbackQuery):
    user = await get_user_by_telegram(query.from_user.id)
    if not user:
        await query.answer("Avval kiring", show_alert=True)
        return
    lecture_id = int(query.data.split(":")[1])
    data = await lecture_payload(user, lecture_id)
    if not data:
        await query.message.answer("Dars topilmadi.")
        await query.answer()
        return
    if data.get("error"):
        await query.message.answer(data["error"])
        await query.answer()
        return
    body = html_to_text(data["content"])
    links = extract_links(data["content"])
    header = f"<b>{tg_escape(data['title'])}</b>\n{tg_escape(data['course'])} · {tg_escape(data['module'])}\n"
    status = "Tugallangan" if data["completed"] else "Hali tugallanmagan"
    text = header + f"Holat: {status}\n\n" + tg_escape(body)
    if data["sql_examples"]:
        text += "\n\n<b>SQL misollar:</b>\n" + "\n".join(f"<code>{tg_escape(s)}</code>" for s in data["sql_examples"][:4])
    if links:
        text += "\n\n<b>Video/fayl havolalari:</b>\n" + "\n".join(links)
    buttons = []
    if not data["completed"]:
        buttons.append(("Darsni tugalladim", f"done:{data['id']}"))
    if data["practice_id"]:
        buttons.append(("SQL amaliyot (LeetCode)", f"ex:{data['practice_id']}"))
    if data["homework_id"]:
        buttons.append(("Uy vazifasi (.txt)", f"hw:{data['homework_id']}"))
    if data["next_id"]:
        buttons.append(("Keyingi dars", f"lec:{data['next_id']}"))
    await query.message.answer(text[:4000], reply_markup=inline_rows(buttons) if buttons else None)
    await query.answer()


@router.callback_query(F.data.startswith("done:"))
async def done_lecture(query: CallbackQuery):
    user = await get_user_by_telegram(query.from_user.id)
    if not user:
        await query.answer("Avval kiring", show_alert=True)
        return
    lecture_id = int(query.data.split(":")[1])
    code = await complete_lecture(user, lecture_id)
    if code != "ok":
        await query.answer("Xato", show_alert=True)
        return
    await query.message.answer("Dars tugallandi. Bu holat veb-platformada ham ko‘rinadi.")
    await query.answer("Saqlandi")
