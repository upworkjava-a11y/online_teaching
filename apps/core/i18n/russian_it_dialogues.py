"""Dialogue translations for Русский для IT module 1 (Uzbek / English UI)."""

from __future__ import annotations

from .english_banking_dialogues import L, _line

RIT_ROLES = {
    "Новичок": L("Yangi xodim", "Янги ходим", "Новичок", "New hire"),
    "Стажёр": L("Stajyor", "Стажёр", "Стажёр", "Intern"),
    "Ментор": L("Mentor", "Ментор", "Ментор", "Mentor"),
    "Лид": L("Lider", "Лидер", "Лид", "Lead"),
    "Камола": L("Kamola", "Камола", "Камола", "Kamola"),
}

RIT_DIALOGUES: dict[str, list[dict]] = {
    "rit-welcome-it": [
        {
            "match": "первый день",
            "lines": [
                _line(
                    "HR",
                    "SoftNovaga xush kelibsiz. Qanday yordam bera olaman?",
                    "SoftNovaга хуш келибсиз. Қандай ёрдам бера оламан?",
                    "Добро пожаловать в SoftNova. Чем могу помочь?",
                    "Welcome to SoftNova. How can I help?",
                ),
                _line(
                    "Новичок",
                    "Men IT jamoaga chiqyapman. Qayerga o‘tsam bo‘ladi?",
                    "Мен IT жамоага чиқяпман. Қаерга ўтсам бўлади?",
                    "Я выхожу в IT-команду. Куда пройти?",
                    "I’m joining the IT team. Where should I go?",
                ),
                _line(
                    "HR",
                    "O‘tiring. Rahbar besh daqiqada keladi.",
                    "Ўтиринг. Раҳбар беш дақиқада келади.",
                    "Присаживайтесь. Руководитель встретит вас через пять минут.",
                    "Please take a seat. Your manager will meet you in five minutes.",
                ),
                _line(
                    "Новичок",
                    "Noutbuk kerakmi?",
                    "Ноутбук керакми?",
                    "Нужен ноутбук?",
                    "Do I need a laptop?",
                ),
                _line(
                    "HR",
                    "Ha. Access beramiz va vositalarni ko‘rsatamiz.",
                    "Ҳа. Access берамиз ва воситаларни кўрсатамиз.",
                    "Да. Выдадим доступы и покажем инструменты.",
                    "Yes. We’ll give you access and show the tools.",
                ),
            ],
        },
    ],
    "rit-it-roles": [
        {
            "match": "К кому обратиться",
            "lines": [
                _line(
                    "Стажёр",
                    "Sayt sekin. Kimga qo‘ng‘iroq qilay?",
                    "Сайт секин. Кимга қўнғироқ қилай?",
                    "Сайт тормозит. Кому звонить?",
                    "The site is slow. Who should I call?",
                ),
                _line(
                    "Ментор",
                    "Avval support. Agar tarmoq bo‘lsa — сетевой инженер.",
                    "Аввал support. Агар тармоқ бўлса — сетевой инженер.",
                    "Сначала поддержка. Если сеть — сетевой инженер.",
                    "Start with support. If it’s the network — network engineer.",
                ),
                _line(
                    "Стажёр",
                    "Agar kodda bug bo‘lsa-chi?",
                    "Агар кодда bug бўлса-чи?",
                    "А если баг в коде?",
                    "And if the bug is in the code?",
                ),
                _line(
                    "Ментор",
                    "Dasturchilarga ticket va tech leadga nusxa.",
                    "Дастурчиларга ticket ва tech leadга нусха.",
                    "Тикет разработчикам и копия техлиду.",
                    "Ticket to developers and copy the tech lead.",
                ),
            ],
        },
    ],
    "rit-office-remote": [
        {
            "match": "удалённый стендап",
            "lines": [
                _line(
                    "Лид",
                    "Kamola, bizni eshityapsizmi?",
                    "Камола, бизни эшитяпсизми?",
                    "Камола, вы нас слышите?",
                    "Kamola, can you hear us?",
                ),
                _line(
                    "Камола",
                    "Ha, VPN ni qayta uladim.",
                    "Ҳа, VPN ни қайта уладим.",
                    "Да, переподключала VPN.",
                    "Yes, I reconnected the VPN.",
                ),
                _line(
                    "Лид",
                    "Update’ingiz qanday?",
                    "Update’ингиз қандай?",
                    "Какой апдейт?",
                    "What’s your update?",
                ),
                _line(
                    "Камола",
                    "Login fix tayyor, bugun testlar.",
                    "Login fix тайёр, бугун тестлар.",
                    "Фикс логина готов, сегодня тесты.",
                    "Login fix is done; tests today.",
                ),
                _line(
                    "Лид",
                    "PR tayyor bo‘lganda QA ga yozing.",
                    "PR тайёр бўлганда QA га ёзинг.",
                    "Напишите QA, когда PR готов.",
                    "Message QA when the PR is ready.",
                ),
            ],
        },
    ],
}
