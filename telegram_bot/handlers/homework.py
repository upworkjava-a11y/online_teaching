from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from telegram_bot.keyboards.menus import cancel_keyboard, main_keyboard_for
from telegram_bot.services.platform import homework_list, submit_homework_bytes
from telegram_bot.services.users import get_user_by_telegram
from telegram_bot.utils.states import LearnFSM

router = Router()


@router.callback_query(F.data.startswith("hw:"))
async def start_hw(query: CallbackQuery, state: FSMContext):
    user = await get_user_by_telegram(query.from_user.id)
    if not user:
        await query.answer("Avval kiring", show_alert=True)
        return
    assignment_id = int(query.data.split(":")[1])
    items = await homework_list(user)
    item = next((x for x in items if x["id"] == assignment_id), None)
    await state.set_state(LearnFSM.homework_file)
    await state.update_data(assignment_id=assignment_id)
    extra = item["instructions"] if item else ""
    await query.message.answer(
        "Uy vazifasini .txt fayl qilib yuboring (veb bilan bir xil qoida).\n"
        "Excel/Power BI kurslari ochilganda fayl mashqlari shu oqimda qabul qilinadi.\n\n"
        + extra,
        reply_markup=cancel_keyboard(),
    )
    await query.answer()


@router.message(LearnFSM.homework_file, F.document)
async def hw_document(message: Message, state: FSMContext):
    user = await get_user_by_telegram(message.from_user.id)
    if not user:
        await state.clear()
        return
    data = await state.get_data()
    doc = message.document
    file = await message.bot.download(doc)
    content = file.read()
    code = await submit_homework_bytes(user, int(data["assignment_id"]), doc.file_name or "homework.txt", content)
    await state.clear()
    texts = {
        "ok": "Yuborildi. O‘qituvchi veb/bot orqali ko‘radi.",
        "bad_type": "Faqat .txt ruxsat etiladi (hozirgi platforma qoidasi).",
        "not_found": "Topshiriq topilmadi.",
        "forbidden": "Ruxsat yo‘q.",
    }
    await message.answer(texts.get(code, code), reply_markup=main_keyboard_for(user))


@router.message(LearnFSM.homework_file)
async def hw_need_file(message: Message):
    await message.answer("Iltimos, .txt hujjat yuboring yoki Bekor qilish ni bosing.")
