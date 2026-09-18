"""Bilingual lesson meta for English-for-IT (module 1 first)."""

from __future__ import annotations

from .english_banking_bilingual import L, V
from .languages import LANG_CYRL, LANG_EN, LANG_RU, LANG_UZ

EIT_BANNER = {
    LANG_UZ: "IT inglizchasini o‘rganasiz — tushuntirish tanlangan tilda.",
    LANG_CYRL: "IT инглизчасини ўрганасиз — тушунтириш танланган тилда.",
    LANG_RU: "Учите IT-английский — пояснения на выбранном языке.",
    LANG_EN: "Learn IT English — explanations follow your UI language.",
}

EIT_LESSONS: dict[str, dict] = {
    "eit-welcome-it": {
        "goal": L(
            "Dars oxirida IT jamoada o‘zingizni tanishtirasiz, asosiy ish so‘zlarini bilasiz va oddiy ish kunini inglizcha tasvirlaysiz.",
            "Дарс охирида IT жамоада ўзингизни таништирасиз, асосий иш сўзларини биласиз ва оддий иш кунини инглизча тасвирлайсиз.",
            "К концу урока вы представитесь в IT-команде, назовёте рабочие слова и опишете простой рабочий день на английском.",
            "By the end you can introduce yourself in an IT team, name workplace words, and describe a simple workday in English.",
        ),
        "vocab": [
            V("IT department", "IT bo‘limi", "IT бўлими", "IT-отдел", "team that builds and supports technology"),
            V("workplace", "ish joyi", "иш жойи", "рабочее место", "place where you do your job"),
            V("colleague / teammate", "hamkasb / jamoa a’zosi", "ҳамкасб / жамоа аъзоси", "коллега / товарищ по команде", "person you work with"),
            V("laptop", "noutbuk", "ноутбук", "ноутбук", "portable computer"),
            V("meeting", "uchrashuv / miting", "учрашув / митинг", "встреча / митинг", "planned discussion"),
            V("ticket", "ticket / ariza", "ticket / ариза", "тикет / заявка", "recorded work request or issue"),
            V("deadline", "muddat / deadline", "муддат / deadline", "дедлайн / срок", "time when work must be finished"),
            V("hybrid work", "gibrid ish", "гибрид иш", "гибридная работа", "mix of office and remote days"),
        ],
    },
    "eit-it-roles": {
        "goal": L(
            "Asosiy IT rollarni nomlaysiz va har biri nima qilishini oddiy inglizchada aytasiz.",
            "Асосий IT ролларни номлайсиз ва ҳар бири нима қилишини оддий инглизчада айтасиз.",
            "Назовёте основные IT-роли и кратко объясните обязанности на английском.",
            "Name common IT roles and say what each person does in simple English.",
        ),
        "vocab": [
            V("software developer / engineer", "dasturchi", "дастурчи", "разработчик", "writes and maintains code"),
            V("QA / tester", "QA / tester", "QA / tester", "QA / тестировщик", "checks quality and finds defects"),
            V("sysadmin", "tizim administratori", "тизим администратори", "сисадмин", "manages servers and systems"),
            V("network engineer", "tarmoq muhandisi", "тармоқ муҳандиси", "сетевой инженер", "designs and supports networks"),
            V("DevOps engineer", "DevOps muhandisi", "DevOps муҳандиси", "DevOps-инженер", "connects development and operations"),
            V("product owner", "product owner", "product owner", "продакт-оунер", "prioritises product work"),
            V("tech lead", "tech lead", "tech lead", "техлид", "senior engineer who guides the team"),
            V("intern", "stajyor", "стажёр", "стажёр", "trainee gaining workplace experience"),
        ],
    },
    "eit-office-remote": {
        "goal": L(
            "Ofis, remote va hybrid haqida gapirasiz; vositalar bo‘yicha muloyim yordam so‘raysiz.",
            "Офис, remote ва hybrid ҳақида гапирасиз; воситалар бўйича мулойим ёрдам сўрайсиз.",
            "Говорите об офисе, удалёнке и гибриде; вежливо просите помощь с инструментами.",
            "Talk about office, remote, and hybrid setups; ask for help with tools politely.",
        ),
        "vocab": [
            V("remote work", "masofaviy ish", "масофавий иш", "удалённая работа", "working from outside the office"),
            V("on-site / in the office", "ofisda / on-site", "офисда / on-site", "в офисе", "working at the company location"),
            V("VPN", "VPN", "VPN", "VPN", "secure connection to the company network"),
            V("headset", "garnitura", "гарнитура", "гарнитура", "headphones with a microphone"),
            V("shared calendar", "umumiy kalendar", "умумий календарь", "общий календарь", "calendar everyone can see"),
            V("status update", "status yangilanishi", "статус янгиланиши", "статус-апдейт", "short report of progress"),
            V("timezone", "vaqt mintaqasi", "вақт минтақаси", "часовой пояс", "local time region"),
            V("async", "asinxron", "асинхрон", "асинхронно", "not happening at the same moment"),
        ],
    },
}
