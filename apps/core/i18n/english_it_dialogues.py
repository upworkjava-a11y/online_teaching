"""Dialogue translations for English-for-IT module 1."""

from __future__ import annotations

from .english_banking_dialogues import L, _line

EIT_ROLES = {
    "New hire": L("Yangi xodim", "Янги ходим", "Новичок", "New hire"),
    "Lead": L("Lider", "Лидер", "Лид", "Lead"),
    "Kamola": L("Kamola", "Камола", "Камола", "Kamola"),
}

EIT_DIALOGUES: dict[str, list[dict]] = {
    "eit-welcome-it": [
        {
            "match": "first day",
            "lines": [
                _line(
                    "HR",
                    "SoftNovaga xush kelibsiz. Bugun sizga qanday yordam bera olaman?",
                    "SoftNovaга хуш келибсиз. Бугун сизга қандай ёрдам бера оламан?",
                    "Добро пожаловать в SoftNova. Чем могу помочь сегодня?",
                    "Welcome to SoftNova. How can I help you today?",
                ),
                _line(
                    "New hire",
                    "Xayrli tong. Men IT jamoada ish boshlayapman. Qayerga borishim kerak?",
                    "Хайрли тонг. Мен IT жамоада иш бошлаяпман. Қаерга боришим керак?",
                    "Доброе утро. Я выхожу в IT-команду. Куда пройти?",
                    "Good morning. I’m starting in the IT team. Where should I go?",
                ),
                _line(
                    "HR",
                    "Iltimos, o‘tiring. Menejeringiz besh daqiqada uchrashadi.",
                    "Илтимос, ўтиринг. Менежерингиз беш дақиқада учрашади.",
                    "Присаживайтесь. Ваш руководитель встретит вас через пять минут.",
                    "Please take a seat. Your manager will meet you in five minutes.",
                ),
                _line(
                    "New hire",
                    "Rahmat. Noutbukim kerakmi?",
                    "Раҳмат. Ноутбуким керакми?",
                    "Спасибо. Нужен ноутбук?",
                    "Thank you. Do I need my laptop?",
                ),
                _line(
                    "HR",
                    "Ha. Sizga akkauntlar va vositalar bo‘yicha qisqa ekskursiya beriladi.",
                    "Ҳа. Сизга аккаунтлар ва воситалар бўйича қисқа экскурсия берилади.",
                    "Да. Выдадим доступы и покажем инструменты.",
                    "Yes. You’ll get your accounts and a quick tour of the tools.",
                ),
            ],
        },
    ],
    "eit-it-roles": [
        {
            "match": "Who should I ask",
            "lines": [
                _line(
                    "Intern",
                    "Sayt ba’zi foydalanuvchilar uchun sekin. Kimga murojaat qilay?",
                    "Сайт баъзи фойдаланувчилар учун секин. Кимга мурожаат қилай?",
                    "Сайт тормозит у части пользователей. Кому звонить?",
                    "The website is slow for some users. Who should I call?",
                ),
                _line(
                    "Mentor",
                    "Avval support bilan boshlang. Agar tarmoq muammosi bo‘lsa — network engineer.",
                    "Аввал support билан бошланг. Агар тармоқ муаммоси бўлса — network engineer.",
                    "Сначала поддержка. Если сеть — сетевой инженер.",
                    "Start with support. If it’s a network issue, involve the network engineer.",
                ),
                _line(
                    "Intern",
                    "Agar muammo kodda bo‘lsa-chi?",
                    "Агар муаммо кодда бўлса-чи?",
                    "А если проблема в коде?",
                    "And if the problem is in the code?",
                ),
                _line(
                    "Mentor",
                    "Dasturchilar uchun ticket oching va tech leadni copy qiling.",
                    "Дастурчилар учун ticket очинг ва tech leadни copy қилинг.",
                    "Создайте тикет разработчикам и скопируйте техлида.",
                    "Create a ticket for the developers and copy the tech lead.",
                ),
                _line(
                    "Intern",
                    "Tushundim. Rahmat!",
                    "Тушундим. Раҳмат!",
                    "Понял. Спасибо!",
                    "Got it. Thanks!",
                ),
            ],
        },
    ],
    "eit-office-remote": [
        {
            "match": "remote standup",
            "lines": [
                _line(
                    "Lead",
                    "Xayrli tong, hamma. Kamola, bizni eshityapsizmi?",
                    "Хайрли тонг, ҳамма. Камола, бизни эшитяпсизми?",
                    "Доброе утро, все. Камола, вы нас слышите?",
                    "Good morning, everyone. Kamola, can you hear us?",
                ),
                _line(
                    "Kamola",
                    "Ha — kechirasiz, VPN ga qayta ulanishim kerak edi.",
                    "Ҳа — кечирасиз, VPN га қайта уланишим керак эди.",
                    "Да — извините, пришлось переподключить VPN.",
                    "Yes — sorry, I had to reconnect to the VPN.",
                ),
                _line(
                    "Lead",
                    "Muammo yo‘q. Update’ingiz nima?",
                    "Муаммо йўқ. Update’ингиз нима?",
                    "Без проблем. Какой апдейт?",
                    "No problem. What’s your update?",
                ),
                _line(
                    "Kamola",
                    "Login fixni tugatdim. Bugun test yozaman.",
                    "Login fixни тугатдим. Бугун тест ёзаман.",
                    "Фикс логина готов. Сегодня напишу тесты.",
                    "I finished the login fix. Today I’ll write tests.",
                ),
                _line(
                    "Lead",
                    "Ajoyib. PR tayyor bo‘lganda QA ga ping qiling.",
                    "Ажойиб. PR тайёр бўлганда QA га ping қилинг.",
                    "Отлично. Напишите QA, когда PR готов.",
                    "Great. Ping QA when the PR is ready.",
                ),
            ],
        },
    ],
}
