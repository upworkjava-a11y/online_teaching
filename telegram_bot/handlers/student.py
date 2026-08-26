from aiogram import F, Router
from aiogram.types import CallbackQuery, Message

from telegram_bot.keyboards.menus import (
    BTN_ANNOUNCE,
    BTN_COURSES,
    BTN_HOMEWORK,
    BTN_MESSAGES,
    BTN_PROFILE,
    BTN_PROGRESS,
    BTN_SCORES,
    inline_rows,
)
from telegram_bot.services.platform import (
    announcements,
    course_modules,
    homework_list,
    inbox,
    list_courses,
    module_items,
    student_progress,
    student_scores,
)
from telegram_bot.services.users import get_user_by_telegram
from telegram_bot.utils.text import tg_escape

router = Router()


async def require_user(message: Message):
    user = await get_user_by_telegram(message.from_user.id)
    if not user:
        await message.answer("Avval kirish yoki ro‘yxatdan o‘ting.")
    return user


@router.message(F.text == BTN_COURSES)
async def show_courses(message: Message):
    user = await require_user(message)
    if not user:
        return
    courses = await list_courses(user)
    if not courses:
        await message.answer("Kurslar yo‘q.")
        return
    buttons = []
    lines = ["<b>Kurslar</b> (veb bilan bir xil ma’lumot)\n"]
    for c in courses:
        mark = f"{c['percent']}%" if c["allowed"] else "🔒"
        lines.append(f"• {tg_escape(c['title'])} — {mark}")
        if c["allowed"]:
            buttons.append((c["title"][:40], f"course:{c['id']}"))
        elif not c["published"]:
            lines.append("  Tez orada (Excel / Power BI va boshqalar vebda ochilganda shu yerda ham chiqadi).")
    await message.answer("\n".join(lines), reply_markup=inline_rows(buttons) if buttons else None)


@router.callback_query(F.data.startswith("course:"))
async def open_course(query: CallbackQuery):
    user = await get_user_by_telegram(query.from_user.id)
    if not user:
        await query.answer("Avval kiring", show_alert=True)
        return
    course_id = int(query.data.split(":")[1])
    title, modules = await course_modules(user, course_id)
    if not modules:
        await query.message.answer(title or "Yopiq kurs.")
        await query.answer()
        return
    buttons = []
    lines = [f"<b>{tg_escape(title)}</b>\n"]
    for m in modules:
        if m["allowed"]:
            lines.append(f"• {tg_escape(m['title'])} — {m['percent']}%")
            buttons.append((m["title"][:40], f"mod:{m['id']}"))
        else:
            lines.append(f"• 🔒 {tg_escape(m['title'])}")
    await query.message.answer("\n".join(lines), reply_markup=inline_rows(buttons) if buttons else None)
    await query.answer()


@router.callback_query(F.data.startswith("mod:"))
async def open_module(query: CallbackQuery):
    user = await get_user_by_telegram(query.from_user.id)
    if not user:
        await query.answer("Avval kiring", show_alert=True)
        return
    module_id = int(query.data.split(":")[1])
    title, lectures, extras = await module_items(user, module_id)
    if title in {"not_found"} or not lectures and "yopiq" in title.lower():
        await query.message.answer(title)
        await query.answer()
        return
    if title == "not_found":
        await query.message.answer("Modul topilmadi.")
        await query.answer()
        return
    buttons = []
    lines = [f"<b>{tg_escape(title)}</b>\nDarslar:"]
    for lec in lectures:
        flag = "✅" if lec["completed"] else ("▶" if lec["allowed"] else "🔒")
        lines.append(f"{flag} {tg_escape(lec['title'])}")
        if lec["allowed"]:
            buttons.append((f"Dars: {lec['title'][:28]}", f"lec:{lec['id']}"))
            if lec["practice_id"]:
                buttons.append((f"Amaliyot: {lec['title'][:22]}", f"ex:{lec['practice_id']}"))
    if extras:
        lines.append("\nQo‘shimcha mashqlar:")
        for ex in extras:
            if ex.get("allowed"):
                buttons.append((f"Mashq: {ex['title'][:28]}", f"ex:{ex['id']}"))
            else:
                lines.append(f"🔒 {tg_escape(ex['title'])} — Premium")
    await query.message.answer("\n".join(lines), reply_markup=inline_rows(buttons) if buttons else None)
    await query.answer()


@router.message(F.text == BTN_PROGRESS)
async def show_progress(message: Message):
    user = await require_user(message)
    if not user:
        return
    rows = await student_progress(user)
    if not rows:
        await message.answer("Hali progress yo‘q.")
        return
    lines = ["<b>Progress</b> (veb-panel bilan sinxron)\n"]
    for row in rows:
        s = row["stats"]
        lines.append(
            f"{tg_escape(row['title'])}: {s['percent']}%\n"
            f"Darslar {s['completed_lectures']}/{s['total_lectures']} · "
            f"Mashqlar {s['completed_exercises']}/{s['total_exercises']} · "
            f"o‘rtacha ball {s['average_score']}%\nOxirgi: {tg_escape(row['last'])}"
        )
    await message.answer("\n\n".join(lines))


@router.message(F.text == BTN_SCORES)
async def show_scores(message: Message):
    user = await require_user(message)
    if not user:
        return
    rows = await student_scores(user)
    if not rows:
        await message.answer("Hali to‘g‘ri yechilgan mashq yo‘q.")
        return
    lines = ["<b>Ballar</b>\n"] + [f"• {tg_escape(r['title'])}: {r['score']}" for r in rows]
    await message.answer("\n".join(lines))


@router.message(F.text == BTN_HOMEWORK)
async def show_hw(message: Message):
    user = await require_user(message)
    if not user:
        return
    rows = await homework_list(user)
    if not rows:
        await message.answer("Ochiq uy vazifasi yo‘q.")
        return
    buttons = []
    lines = ["<b>Uy vazifasi</b> (.txt, vebdagi bilan bir xil)\n"]
    for r in rows:
        lines.append(f"• {tg_escape(r['title'])} — {r['status']}")
        buttons.append((r["title"][:40], f"hw:{r['id']}"))
    await message.answer("\n".join(lines), reply_markup=inline_rows(buttons))


@router.message(F.text == BTN_ANNOUNCE)
async def show_ann(message: Message):
    items = await announcements()
    if not items:
        await message.answer("E’lonlar yo‘q.")
        return
    chunks = []
    for a in items:
        chunks.append(f"<b>{tg_escape(a['title'])}</b>\n{tg_escape(a['body'][:800])}\n— {tg_escape(a['author'])}")
    await message.answer("\n\n".join(chunks)[:4000])


@router.message(F.text == BTN_MESSAGES)
async def show_inbox(message: Message):
    user = await require_user(message)
    if not user:
        return
    items = await inbox(user)
    if not items:
        await message.answer("Yangi xabar yo‘q.")
        return
    text = "\n\n".join(f"<b>{tg_escape(m['from'])}</b>\n{tg_escape(m['body'])}" for m in items)
    await message.answer(text[:4000])


@router.message(F.text == BTN_PROFILE)
async def show_profile(message: Message):
    user = await require_user(message)
    if not user:
        return
    await message.answer(
        f"<b>Profil</b>\nIsm: {tg_escape(user.get_full_name())}\n"
        f"Email: {tg_escape(user.email)}\nRol: {user.get_role_display()}\n"
        f"Telegram ID: {message.from_user.id}\n\n"
        f"Veb-saytga shu email bilan kiring — kurslar va progress bir xil."
    )
