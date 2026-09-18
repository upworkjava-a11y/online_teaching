"""Bilingual lesson meta for Русский для IT (module 1)."""

from __future__ import annotations

from .english_banking_bilingual import L, V
from .languages import LANG_CYRL, LANG_EN, LANG_RU, LANG_UZ

RIT_BANNER = {
    LANG_UZ: "IT ruschasini o‘rganasiz — tushuntirish tanlangan tilda.",
    LANG_CYRL: "IT русчасини ўрганасиз — тушунтириш танланган тилда.",
    LANG_RU: "Учите IT-русский — пояснения на выбранном языке.",
    LANG_EN: "Learn IT Russian — explanations follow your UI language.",
}

RIT_LESSONS: dict[str, dict] = {
    "rit-welcome-it": {
        "goal": L(
            "Dars oxirida IT jamoada ruscha tanishtirasiz, asosiy ish so‘zlarini bilasiz va oddiy ish kunini tasvirlaysiz.",
            "Дарс охирида IT жамоада русча таништирасиз, асосий иш сўзларини биласиз ва оддий иш кунини тасвирлайсиз.",
            "К концу урока вы представитесь в IT-команде по-русски, назовёте рабочие слова и опишете простой день.",
            "By the end you can introduce yourself in Russian in an IT team and describe a simple workday.",
        ),
        "vocab": [
            V("IT-отдел", "IT bo‘limi", "IT бўлими", "IT-отдел", "team that builds and supports technology"),
            V("рабочее место", "ish joyi", "иш жойи", "рабочее место", "place where you work"),
            V("коллега", "hamkasb", "ҳамкасб", "коллега", "person you work with"),
            V("ноутбук", "noutbuk", "ноутбук", "ноутбук", "portable computer"),
            V("митинг / встреча", "miting / uchrashuv", "митинг / учрашув", "митинг / встреча", "planned discussion"),
            V("тикет", "ticket / ariza", "ticket / ариза", "тикет", "recorded work request"),
            V("дедлайн", "muddat", "муддат", "дедлайн", "deadline"),
            V("гибридная работа", "gibrid ish", "гибрид иш", "гибридная работа", "office + remote"),
        ],
    },
    "rit-it-roles": {
        "goal": L(
            "IT rollarni ruscha nomlaysiz va vazifalarini qisqa aytasiz.",
            "IT ролларни русча номлайсиз ва вазифаларини қисқа айтасиз.",
            "Назовёте IT-роли по-русски и кратко объясните обязанности.",
            "Name IT roles in Russian and say what each person does.",
        ),
        "vocab": [
            V("разработчик", "dasturchi", "дастурчи", "разработчик", "writes code"),
            V("QA / тестировщик", "QA / tester", "QA / tester", "QA / тестировщик", "checks quality"),
            V("сисадмин", "tizim administratori", "тизим администратори", "сисадмин", "manages servers"),
            V("сетевой инженер", "tarmoq muhandisi", "тармоқ муҳандиси", "сетевой инженер", "supports networks"),
            V("DevOps-инженер", "DevOps muhandisi", "DevOps муҳандиси", "DevOps-инженер", "dev + ops"),
            V("продакт-оунер", "product owner", "product owner", "продакт-оунер", "prioritises work"),
            V("техлид", "tech lead", "tech lead", "техлид", "guides the team"),
            V("стажёр", "stajyor", "стажёр", "стажёр", "intern"),
        ],
    },
    "rit-office-remote": {
        "goal": L(
            "Ofis, udalyonka va gibrid haqida ruscha gapirasiz; muloyim yordam so‘raysiz.",
            "Офис, удалёнка ва гибрид ҳақида русча гапирасиз; мулойим ёрдам сўрайсиз.",
            "Говорите об офисе, удалёнке и гибриде; вежливо просите помощь.",
            "Talk about office/remote/hybrid in Russian; ask for help politely.",
        ),
        "vocab": [
            V("удалённая работа", "masofaviy ish", "масофавий иш", "удалённая работа", "remote work"),
            V("в офисе", "ofisda", "офисда", "в офисе", "on-site"),
            V("VPN", "VPN", "VPN", "VPN", "secure company connection"),
            V("гарнитура", "garnitura", "гарнитура", "гарнитура", "headset"),
            V("общий календарь", "umumiy kalendar", "умумий календарь", "общий календарь", "shared calendar"),
            V("статус-апдейт", "status yangilanishi", "статус янгиланиши", "статус-апдейт", "status update"),
            V("часовой пояс", "vaqt mintaqasi", "вақт минтақаси", "часовой пояс", "timezone"),
            V("асинхронно", "asinxron", "асинхрон", "асинхронно", "async"),
        ],
    },
}
