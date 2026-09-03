"""
Bilingual layer for English-for-Banking lessons.

English words / examples / dialogues stay in English.
Goals, meanings, and short notes follow the UI language.
"""

from __future__ import annotations

import html as html_lib
import re

from .languages import LANG_CYRL, LANG_EN, LANG_RU, LANG_UZ, normalize_language

# UI chrome for section titles (shown next to English headings)
HEADINGS = {
    "Lesson goal": {
        LANG_UZ: "Dars maqsadi",
        LANG_CYRL: "Дарс мақсади",
        LANG_RU: "Цель урока",
        LANG_EN: "Lesson goal",
    },
    "Warm-up": {
        LANG_UZ: "Qizdirish",
        LANG_CYRL: "Қиздириш",
        LANG_RU: "Разминка",
        LANG_EN: "Warm-up",
    },
    "Key vocabulary": {
        LANG_UZ: "Asosiy so‘zlar",
        LANG_CYRL: "Асосий сўзлар",
        LANG_RU: "Ключевая лексика",
        LANG_EN: "Key vocabulary",
    },
    "Useful phrases": {
        LANG_UZ: "Foydali iboralar",
        LANG_CYRL: "Фойдали иборалар",
        LANG_RU: "Полезные фразы",
        LANG_EN: "Useful phrases",
    },
    "Key phrases": {
        LANG_UZ: "Asosiy iboralar",
        LANG_CYRL: "Асосий иборалар",
        LANG_RU: "Ключевые фразы",
        LANG_EN: "Key phrases",
    },
    "Offers and choices": {
        LANG_UZ: "Takliflar va tanlovlar",
        LANG_CYRL: "Таклифлар ва танловлар",
        LANG_RU: "Предложения и выбор",
        LANG_EN: "Offers and choices",
    },
    "Useful phrases (memorise)": {
        LANG_UZ: "Foydali iboralar (yodlang)",
        LANG_CYRL: "Фойдали иборалар (ёдланг)",
        LANG_RU: "Полезные фразы (выучите)",
        LANG_EN: "Useful phrases (memorise)",
    },
    "Grammar focus": {
        LANG_UZ: "Grammatika",
        LANG_CYRL: "Грамматика",
        LANG_RU: "Грамматика",
        LANG_EN: "Grammar focus",
    },
    "Speaking prompt": {
        LANG_UZ: "Gapirish topshirig‘i",
        LANG_CYRL: "Гапириш топшириғи",
        LANG_RU: "Задание на говорение",
        LANG_EN: "Speaking prompt",
    },
    "Speaking practice": {
        LANG_UZ: "Gapirish amaliyoti",
        LANG_CYRL: "Гапириш амалиёти",
        LANG_RU: "Практика говорения",
        LANG_EN: "Speaking practice",
    },
    "Speaking": {
        LANG_UZ: "Gapirish",
        LANG_CYRL: "Гапириш",
        LANG_RU: "Говорение",
        LANG_EN: "Speaking",
    },
    "Reading": {
        LANG_UZ: "O‘qish",
        LANG_CYRL: "Ўқиш",
        LANG_RU: "Чтение",
        LANG_EN: "Reading",
    },
    "Quick review": {
        LANG_UZ: "Qisqa takror",
        LANG_CYRL: "Қисқа такрор",
        LANG_RU: "Краткое повторение",
        LANG_EN: "Quick review",
    },
    "Common mistakes": {
        LANG_UZ: "Ko‘p uchraydigan xatolar",
        LANG_CYRL: "Кўп учрайдиган хатолар",
        LANG_RU: "Частые ошибки",
        LANG_EN: "Common mistakes",
    },
    "Example sentences": {
        LANG_UZ: "Namuna gaplar",
        LANG_CYRL: "Намуна гаплар",
        LANG_RU: "Примеры предложений",
        LANG_EN: "Example sentences",
    },
    "Word": {
        LANG_UZ: "So‘z",
        LANG_CYRL: "Сўз",
        LANG_RU: "Слово",
        LANG_EN: "Word",
    },
    "Meaning": {
        LANG_UZ: "Ma’nosi",
        LANG_CYRL: "Маъноси",
        LANG_RU: "Значение",
        LANG_EN: "Meaning",
    },
    "Example": {
        LANG_UZ: "Misol",
        LANG_CYRL: "Мисол",
        LANG_RU: "Пример",
        LANG_EN: "Example",
    },
    "Term": {
        LANG_UZ: "Termin",
        LANG_CYRL: "Термин",
        LANG_RU: "Термин",
        LANG_EN: "Term",
    },
}

BANNER = {
    LANG_UZ: "Inglizcha o‘rganasiz — tushuntirish tanlangan tilda.",
    LANG_CYRL: "Инглизча ўрганасиз — тушунтириш танланган тилда.",
    LANG_RU: "Учите английский — пояснения на выбранном языке.",
    LANG_EN: "Learn in English — explanations follow your UI language.",
}

EXPLAIN_LABEL = {
    LANG_UZ: "Tushuntirish",
    LANG_CYRL: "Тушунтириш",
    LANG_RU: "Пояснение",
    LANG_EN: "Explanation",
}


def L(uz: str, cyrl: str, ru: str, en: str) -> dict[str, str]:
    return {LANG_UZ: uz, LANG_CYRL: cyrl, LANG_RU: ru, LANG_EN: en}


def _t(pack: dict[str, str], lang: str) -> str:
    return pack.get(lang) or pack.get(LANG_UZ) or next(iter(pack.values()), "")


def V(word: str, uz: str, cyrl: str, ru: str, en: str) -> tuple:
    """word (EN) + meaning in 4 UI languages."""
    return (word, L(uz, cyrl, ru, en))


# Per-lesson: short goal note + vocabulary meanings (English headword → localized gloss)
LESSONS: dict[str, dict] = {
    "eb-welcome": {
        "goal": L(
            "Dars oxirida mijozni salomlashasiz, asosiy rollarni ayta olasiz va filialdagi oddiy kun tartibini inglizcha tasvirlaysiz.",
            "Дарс охирида мижозни саломлашасиз, асосий ролларни айта оласиз ва филиалдаги оддий кун тартибини инглизча тасвирлайсиз.",
            "К концу урока вы сможете поприветствовать клиента, назвать основные роли и описать простой распорядок отделения на английском.",
            "By the end you can greet a customer, name main roles, and describe a simple branch routine in English.",
        ),
        "vocab": [
            V("branch", "mahalliy bank ofisi / filial", "маҳаллий банк офиси / филиал", "местное отделение банка", "a local bank office"),
            V("head office", "bosh ofis", "бош офис", "головной офис", "main central office"),
            V("teller / cashier", "kassir (mijozlarga xizmat qiladi)", "кассир (мижозларга хизмат қилади)", "кассир / операционист", "person who serves customers at the counter"),
            V("customer / client", "mijoz", "мижоз", "клиент", "person who uses bank services"),
            V("manager", "menejer / rahbar", "менежер / раҳбар", "менеджер", "person who leads a team or branch"),
            V("ATM", "bankomat", "банкомат", "банкомат", "machine for cash without a teller"),
            V("counter / desk", "kassa / stol", "касса / стол", "стойка / окно обслуживания", "place where staff serve clients"),
            V("queue / line", "navbat", "навбат", "очередь", "people waiting"),
        ],
    },
    "eb-departments": {
        "goal": L(
            "Bank bo‘limlarini nomlaysiz va har biri nima qilishini oddiy inglizchada aytasiz.",
            "Банк бўлимларини номлайсиз ва ҳар бири нима қилишини оддий инглизчада айтасиз.",
            "Вы научитесь называть отделы банка и кратко объяснять, чем они занимаются.",
            "Name bank departments and say what each one does in simple English.",
        ),
        "vocab": [
            V("Retail banking", "jismoniy shaxslarga xizmat", "жисмоний шахсларга хизмат", "розничный банкинг", "services for individuals"),
            V("Corporate banking", "kompaniyalarga xizmat", "компанияларга хизмат", "корпоративный банкинг", "services for companies"),
            V("Credit / Lending", "kredit bo‘limi", "кредит бўлими", "кредитный отдел", "reviews and decides on loans"),
            V("HR (Human Resources)", "kadrlar bo‘limi", "кадрлар бўлими", "отдел кадров (HR)", "hiring and staff support"),
            V("Compliance", "qoidaga rioya / compliance", "қоидага риоя / compliance", "комплаенс", "follows laws and bank rules"),
            V("Operations / Back office", "operatsiyalar / orqa ofis", "операциялар / орқа офис", "операции / бэк-офис", "processes payments day to day"),
            V("Risk", "risk bo‘limi", "риск бўлими", "риск-менеджмент", "identifies and controls risks"),
            V("IT / Digital", "IT / raqamli xizmatlar", "IT / рақамли хизматлар", "IT / цифровые сервисы", "apps and online systems"),
            V("Call centre / Contact centre", "aloqa markazi", "алоқа маркази", "контакт-центр", "helps clients by phone or chat"),
        ],
    },
    "eb-polite-talk": {
        "goal": L(
            "Hujjat so‘rash, tanlov taklif qilish va “yo‘q”ni muloyim aytishni o‘rganasiz.",
            "Ҳужжат сўраш, танлов таклиф қилиш ва “йўқ”ни мулойим айтишни ўрганасиз.",
            "Научитесь вежливо просить документы, предлагать выбор и отказывать.",
            "Ask for documents, offer choices, and say no politely.",
        ),
        "vocab": [
            V("Could you…?", "muloyim so‘rov", "мулойим сўров", "вежливая просьба", "polite request"),
            V("Would you like…?", "taklif / tanlov", "таклиф / танлов", "предложение / выбор", "polite offer or choice"),
            V("I’m afraid…", "yumshoq yomon xabar", "юмшоқ ёмон хабар", "мягкое сообщение о проблеме", "soft way to give bad news"),
        ],
    },
    "eb-account-types": {
        "goal": L(
            "Hisob turlarini solishtirasiz va mijozga oddiy inglizchada tanlashda yordam berasiz.",
            "Ҳисоб турларини солиштирасиз ва мижозга оддий инглизчада танлашда ёрдам берасиз.",
            "Сравните типы счетов и помогите клиенту выбрать на простом английском.",
            "Compare account types and help a customer choose in simple English.",
        ),
        "vocab": [
            V("current / checking account", "joriy hisob (kundalik to‘lovlar)", "жорий ҳисоб (кундалик тўловлар)", "текущий счёт", "for everyday payments"),
            V("savings account", "jamg‘arma hisobi", "жамғарма ҳисоби", "сберегательный счёт", "to keep money and earn interest"),
            V("joint account", "qo‘shma hisob", "қўшма ҳисоб", "совместный счёт", "shared by two or more people"),
            V("deposit", "pul qo‘yish / depozit", "пул қўйиш / депозит", "внести деньги / депозит", "put money into an account"),
            V("withdrawal", "naqd yechish", "нақд ечиш", "снятие средств", "take money out"),
            V("balance", "qoldiq / balans", "қолдиқ / баланс", "остаток / баланс", "money available now"),
            V("statement", "ko‘chirma", "кўчирма", "выписка", "list of transactions"),
            V("interest", "foiz", "фоиз", "проценты", "money earned on savings (or paid on loans)"),
            V("minimum balance", "minimal qoldiq", "минимал қолдиқ", "минимальный остаток", "lowest amount the bank may require"),
        ],
    },
    "eb-deposit-withdraw": {
        "goal": L(
            "Pul qo‘yish, yechish va o‘tkazish fe’llarini to‘g‘ri ishlatasiz.",
            "Пул қўйиш, ечиш ва ўтказиш феълларини тўғри ишлатасиз.",
            "Правильно используйте глаголы внесения, снятия и перевода денег.",
            "Use the correct verbs for putting money in, taking it out, and transferring.",
        ),
        "vocab": [
            V("deposit", "hisobga pul qo‘yish", "ҳисобга пул қўйиш", "внести деньги", "put money in"),
            V("withdraw", "hisobdan pul yechish", "ҳисобдан пул ечиш", "снять деньги", "take money out"),
            V("transfer", "o‘tkazma qilish", "ўтказма қилиш", "перевести", "send money to another account"),
            V("check the balance", "balansni tekshirish", "балансни текшириш", "проверить баланс", "see available money"),
        ],
    },
    "eb-statement": {
        "goal": L(
            "Ko‘chirmadagi sana, izoh, summa va qoldiqni o‘qib tushuntirasiz.",
            "Кўчирмадаги сана, изоҳ, сумма ва қолдиқни ўқиб тушунтирасиз.",
            "Научитесь читать и объяснять строки выписки.",
            "Read statement lines: date, description, amount, and balance.",
        ),
        "vocab": [
            V("transaction", "operatsiya", "операция", "операция / транзакция", "one money movement"),
            V("credit", "kirim (+)", "кирим (+)", "зачисление (+)", "money in"),
            V("debit", "chiqim (−)", "чиқим (−)", "списание (−)", "money out"),
            V("running balance", "joriy qoldiq", "жорий қолдиқ", "текущий остаток", "balance after each line"),
        ],
    },
    "eb-cards": {
        "goal": L(
            "Debet va kredit kartani aniq farqlaysiz, limit va PIN haqida gaplashasiz.",
            "Дебет ва кредит картани аниқ фарқлайсиз, лимит ва PIN ҳақида гаплашасиз.",
            "Чётко объясните разницу между дебетовой и кредитной картой.",
            "Explain debit vs credit clearly; talk about limits and PINs.",
        ),
        "vocab": [
            V("debit card", "debet karta (o‘z pulingiz)", "дебет карта (ўз пулингиз)", "дебетовая карта", "pays with your own money"),
            V("credit card", "kredit karta (bankdan qarz)", "кредит карта (банкдан қарз)", "кредитная карта", "borrows up to a limit"),
            V("credit limit", "kredit limiti", "кредит лимити", "кредитный лимит", "maximum you can borrow"),
            V("PIN", "maxfiy kod", "махфий код", "ПИН-код", "secret personal code"),
            V("expiry date", "amal qilish muddati", "амал қилиш муддати", "срок действия", "when the card stops working"),
            V("CVV / security code", "xavfsizlik kodi", "хавфсизлик коди", "CVV / код безопасности", "code for online payments"),
            V("contactless", "kontaktssiz to‘lov", "контактсиз тўлов", "бесконтактная оплата", "pay by tapping the card"),
        ],
    },
    "eb-transfers": {
        "goal": L(
            "O‘tkazma, komissiya va rekvizitlarni tekshirish haqida gaplashasiz.",
            "Ўтказма, комиссия ва реквизитларни текшириш ҳақида гаплашасиз.",
            "Говорите о переводах, комиссиях и проверке реквизитов.",
            "Talk about transfers, fees, and careful checking of details.",
        ),
        "vocab": [
            V("transfer", "pul o‘tkazmasi", "пул ўтказмаси", "перевод", "send money between accounts"),
            V("beneficiary", "oluvchi", "олувчи", "получатель", "person who receives the money"),
            V("account number / IBAN", "hisob raqami / IBAN", "ҳисоб рақами / IBAN", "номер счёта / IBAN", "account identifier"),
            V("fee / charge / commission", "komissiya", "комиссия", "комиссия / сбор", "money charged for a service"),
            V("online banking / mobile app", "internet-banking / ilova", "интернет-банкинг / илова", "интернет-банк / приложение", "banking on internet/phone"),
            V("payment reference", "to‘lov izohi", "тўлов изоҳи", "назначение платежа", "note that explains the payment"),
        ],
    },
    "eb-atm-safety": {
        "goal": L(
            "ATM va karta xavfsizligi bo‘yicha aniq maslahat berasiz.",
            "ATM ва карта хавфсизлиги бўйича аниқ маслаҳат берасиз.",
            "Даёте чёткие советы по безопасности карты и банкомата.",
            "Give clear ATM and card safety advice.",
        ),
        "vocab": [
            V("PIN", "maxfiy kod — hech kimga bermang", "махфий код — ҳеч кимга берманг", "ПИН — никому не сообщайте", "secret code — keep it private"),
            V("block a card", "kartani bloklash", "картани блоклаш", "заблокировать карту", "stop the card from working"),
            V("lost card", "yo‘qolgan karta", "йўқолган карта", "утерянная карта", "card you cannot find"),
        ],
    },
    "eb-loan-basics": {
        "goal": L(
            "Kredit atamalarini to‘g‘ri ishlatasiz; borrow/lend xatosidan saqlanasiz.",
            "Кредит атамаларини тўғри ишлатасиз; borrow/lend хатосидан сақланасиз.",
            "Точно используете кредитную лексику и не путаете borrow/lend.",
            "Use accurate loan vocabulary; avoid the borrow/lend mistake.",
        ),
        "vocab": [
            V("loan / credit", "qarz / kredit", "қарз / кредит", "кредит / заём", "borrowed money you must repay"),
            V("borrower", "qarz oluvchi", "қарз олувчи", "заёмщик", "person who takes the loan"),
            V("lender", "qarz beruvchi (bank)", "қарз берувчи (банк)", "кредитор (банк)", "bank that gives the loan"),
            V("interest rate", "foiz stavkasi", "фоиз ставкаси", "процентная ставка", "% charged for borrowing"),
            V("principal", "asosiy qarz summasi", "асосий қарз суммаси", "основная сумма долга", "original amount borrowed"),
            V("repayment / installment", "to‘lov / muddatli to‘lov", "тўлов / муддатли тўлов", "платёж / взнос", "regular payment to repay"),
            V("maturity", "kredit tugash sanasi", "кредит тугаш санаси", "срок погашения", "end date of the loan"),
            V("application", "ariza", "ариза", "заявка", "formal request for a loan"),
        ],
    },
    "eb-mortgage": {
        "goal": L(
            "Ipoteka va garovni oddiy, aniq inglizchada tushuntirasiz.",
            "Ипотека ва гаровни оддий, аниқ инглизчада тушунтирасиз.",
            "Просто и точно объясняете ипотеку и залог.",
            "Describe mortgages and collateral in accurate simple English.",
        ),
        "vocab": [
            V("mortgage", "ipoteka (uy-joy krediti)", "ипотека (уй-жой кредити)", "ипотека", "loan to buy property"),
            V("collateral / security", "garov", "гаров", "залог / обеспечение", "asset given as guarantee"),
            V("secured loan", "garovli kredit", "гаровли кредит", "обеспеченный кредит", "loan protected by collateral"),
            V("unsecured loan", "garovsiz kredit", "гаровсиз кредит", "необеспеченный кредит", "loan without collateral"),
            V("overdraft", "overdraft", "овердрафт", "овердрафт", "allowed short negative balance"),
            V("down payment", "boshlang‘ich to‘lov", "бошланғич тўлов", "первоначальный взнос", "first part the buyer pays"),
        ],
    },
    "eb-overdue": {
        "goal": L(
            "Kechikkan to‘lovni muloyim tushuntirasiz va first conditional ishlatasiz.",
            "Кечиккан тўловни мулойим тушунтирасиз ва first conditional ишлатасиз.",
            "Вежливо объясняете просрочку и используете first conditional.",
            "Explain overdue payments politely; use first conditional.",
        ),
        "vocab": [
            V("due date", "to‘lov sanasi", "тўлов санаси", "срок платежа", "when payment must be made"),
            V("overdue / late payment", "kechikkan to‘lov", "кечиккан тўлов", "просроченный платёж", "payment after the due date"),
            V("penalty / late fee", "jarima", "жарима", "штраф / пеня", "extra charge for being late"),
            V("default", "jiddiy to‘lamaslik", "жиддий тўламаслик", "дефолт", "serious failure to repay"),
        ],
    },
    "eb-fx-basics": {
        "goal": L(
            "Valyuta ayirboshlashni aniq bank atamalari bilan tushuntirasiz.",
            "Валюта айирбошлашни аниқ банк атамалари билан тушунтирасиз.",
            "Объясняете обмен валюты точными банковскими терминами.",
            "Explain currency exchange with accurate banking terms.",
        ),
        "vocab": [
            V("foreign exchange (FX)", "valyuta ayirboshlash", "валюта айирбошлаш", "валютный обмен (FX)", "changing one currency into another"),
            V("exchange rate", "ayirboshlash kursi", "айирбошлаш курси", "обменный курс", "price of one currency in another"),
            V("buy rate / sell rate", "sotib olish / sotish kursi", "сотиб олиш / сотиш курси", "курс покупки / продажи", "bank rates for buying or selling"),
            V("spread", "kurslar farqi (margin)", "курслар фарқи (маржа)", "спред (разница курсов)", "difference between buy and sell rates"),
            V("currency pair", "valyuta juftligi", "валюта жуфтлиги", "валютная пара", "two currencies quoted together"),
        ],
    },
    "eb-remittance": {
        "goal": L(
            "Xalqaro pul o‘tkazmasi: remittance, SWIFT, komissiya va muddat.",
            "Халқаро пул ўтказмаси: remittance, SWIFT, комиссия ва муддат.",
            "Международные переводы: remittance, SWIFT, комиссия и сроки.",
            "Talk about remittances, wires, fees, and timing.",
        ),
        "vocab": [
            V("remittance", "xorijga/oilaga pul yuborish", "хорижга/оилага пул юбориш", "денежный перевод (часто семье)", "money sent across borders"),
            V("wire transfer / TT", "banklararo elektron o‘tkazma", "банклараро электрон ўтказма", "банковский перевод", "bank-to-bank electronic transfer"),
            V("SWIFT", "xalqaro bank xabar tarmog‘i", "халқаро банк хабар тармоғи", "система сообщений SWIFT", "messaging network for cross-border payments"),
            V("BIC / SWIFT code", "bank identifikatori", "банк идентификатори", "BIC / SWIFT-код банка", "bank identifier"),
            V("value date", "pul keladigan sana", "пул келадиган сана", "дата валютирования", "date when funds are available"),
            V("cut-off time", "shu kun uchun oxirgi muddat", "шу кун учун охирги муддат", "время cut-off", "deadline to send same-day"),
        ],
    },
    "eb-fx-fees": {
        "goal": L(
            "O‘tkazma narxi va muddatini mijozni chalkashtirmasdan tushuntirasiz.",
            "Ўтказма нархи ва муддатини мижозни чалкаштирмасдан тушунтирасиз.",
            "Прозрачно объясняете стоимость и сроки перевода.",
            "Explain transfer costs and timing clearly.",
        ),
        "vocab": [
            V("transfer fee", "o‘tkazma komissiyasi", "ўтказма комиссияси", "комиссия за перевод", "charge for sending money"),
            V("FX margin / spread", "kursdagi bank margini", "курсдаги банк маржини", "валютная маржа / спред", "built into the exchange rate"),
            V("intermediary charges", "oraliq bank komissiyasi", "оралиқ банк комиссияси", "комиссии банков-посредников", "fees from correspondent banks"),
        ],
    },
    "eb-sme-basics": {
        "goal": L(
            "SME va korporativ mijozlarga bank qanday xizmat qilishini oddiy aytasiz.",
            "SME ва корпоратив мижозларга банк қандай хизмат қилишини оддий айтасиз.",
            "Просто объясняете, как банк обслуживает SME и компании.",
            "Describe how banks serve SMEs and companies in simple English.",
        ),
        "vocab": [
            V("SME", "kichik va o‘rta biznes", "кичик ва ўрта бизнес", "малый и средний бизнес", "small and medium-sized enterprise"),
            V("working capital", "aylanma mablag‘", "айланма маблағ", "оборотный капитал", "money for day-to-day business needs"),
            V("cash flow", "pul oqimi", "пул оқими", "денежный поток", "money moving in and out"),
            V("relationship manager (RM)", "mijoz menejeri", "мижоз менежери", "клиентский менеджер", "banker for company clients"),
            V("merchant acquiring", "do‘konda karta qabul qilish", "дўконда карта қабул қилиш", "эквайринг", "accepting card payments for shops"),
        ],
    },
    "eb-letter-of-credit": {
        "goal": L(
            "Akkreditiv (LC) ni oddiy darajada: kim kim, nima uchun.",
            "Аккредитив (LC) ни оддий даражада: ким ким, нима учун.",
            "Простое объяснение аккредитива (LC): роли и смысл.",
            "Explain a letter of credit at a basic level.",
        ),
        "vocab": [
            V("letter of credit (LC)", "akkreditiv", "аккредитив", "аккредитив (LC)", "bank pays if documents comply"),
            V("applicant", "arizachi (odatda xaridor)", "аризачи (одатда харидор)", "аппликант (обычно покупатель)", "buyer who requests the LC"),
            V("beneficiary", "benefitsiar (odatda sotuvchi)", "бенефициар (одатда сотувчи)", "бенефициар (обычно продавец)", "seller who gets paid"),
            V("issuing bank", "akkreditiv ochgan bank", "аккредитив очган банк", "банк-эмитент", "opens the LC"),
            V("shipping documents", "yetkazib berish hujjatlari", "етказиб бериш ҳужжатлари", "отгрузочные документы", "papers that prove shipment"),
        ],
    },
    "eb-guarantees": {
        "goal": L(
            "Bank kafolatini oddiy tushuntirasiz va LC dan farqini aytasiz.",
            "Банк кафолатини оддий тушунтирасиз ва LC дан фарқини айтасиз.",
            "Просто объясняете банковскую гарантию и отличие от LC.",
            "Describe a bank guarantee and contrast it lightly with an LC.",
        ),
        "vocab": [
            V("bank guarantee", "bank kafolati", "банк кафолати", "банковская гарантия", "bank promise if client fails a duty"),
            V("performance guarantee", "ijro kafolati", "ижро кафолати", "гарантия исполнения", "supports completing a contract"),
            V("bid bond", "tender kafolati", "тендер кафолати", "тендерная гарантия", "guarantee often used in tenders"),
        ],
    },
    "eb-digital-channels": {
        "goal": L(
            "Raqamli kanallarni nomlaysiz va xavfsiz self-service iboralarini o‘rgatasiz.",
            "Рақамли каналларни номлайсиз ва хавфсиз self-service ибораларини ўргатасиз.",
            "Называете цифровые каналы и учите безопасным фразам self-service.",
            "Name digital channels and guide safe self-service phrases.",
        ),
        "vocab": [
            V("mobile banking app", "mobil banking ilovasi", "мобил банкинг иловаси", "мобильное приложение банка", "bank services on a smartphone"),
            V("OTP", "bir martalik kod", "бир марталик код", "одноразовый пароль (OTP)", "one-time password/code"),
            V("two-factor authentication (2FA)", "ikkiga bosqichli himoya", "иккига босқичли ҳимоя", "двухфакторная аутентификация", "password + second factor"),
            V("card controls", "karta sozlamalari (blok/limit)", "карта созламалари (блок/лимит)", "управление картой в приложении", "limits, freeze, region settings"),
        ],
    },
    "eb-phishing": {
        "goal": L(
            "Firibgarlik sxemalarini taniysiz va mijozni xotirjam ogohlantirasiz.",
            "Фирибгарлик схемаларини танийсиз ва мижозни хотиржам огоҳлантирасиз.",
            "Узнаёте схемы мошенничества и спокойно предупреждаете клиента.",
            "Recognise fraud patterns and warn customers calmly.",
        ),
        "vocab": [
            V("phishing", "soxta sayt/xabar orqali ma’lumot o‘g‘irlash", "сўхта сайт/хабар орқали маълумот ўғирлаш", "фишинг", "fake emails/sites to steal data"),
            V("smishing", "SMS orqali phishing", "SMS орқали phishing", "смишинг (SMS-фишинг)", "phishing by SMS"),
            V("vishing", "telefon qo‘ng‘irog‘i orqali firibgarlik", "телефон қўнғироғи орқали фирибгарлик", "вишинг (телефонный обман)", "phishing by voice call"),
            V("social engineering", "odamni aldab ma’lumot olish", "одамни алдаб маълумот олиш", "социальная инженерия", "manipulating people to give data"),
        ],
    },
    "eb-fraud-cases": {
        "goal": L(
            "Filialdagi firibgarlik holatlari va escalate tilini bilasiz.",
            "Филиалдаги фирибгарлик ҳолатлари ва escalate тилини биласиз.",
            "Знаете типы мошенничества в отделении и язык эскалации.",
            "Describe fraud case types and escalation language.",
        ),
        "vocab": [
            V("account takeover", "hisobni egallab olish", "ҳисобни эгаллаб олиш", "захват аккаунта", "criminal controls customer access"),
            V("identity theft", "shaxsni o‘g‘irlash", "шахсни ўғирлаш", "кража личности", "using stolen ID details"),
            V("scam / fraud", "firibgarlik", "фирибгарлик", "мошенничество", "criminal deception for money"),
        ],
    },
    "eb-job-titles": {
        "goal": L(
            "Bank lavozimlarini nomlaysiz va o‘zingizni bir jumlada tanishtirasiz.",
            "Банк лавозимларини номлайсиз ва ўзингизни бир жумлада таништирасиз.",
            "Называете должности и представляетесь одним предложением.",
            "Name bank jobs and introduce your role in one sentence.",
        ),
        "vocab": [
            V("credit analyst", "kredit tahlilchisi", "кредит таҳлилчиси", "кредитный аналитик", "reviews loan applications"),
            V("compliance officer", "compliance mutaxassisi", "compliance мутахассиси", "сотрудник комплаенса", "rules, KYC, monitoring"),
            V("relationship manager", "mijozlar bilan ishlash menejeri", "мижозлар билан ишлаш менежери", "менеджер по работе с клиентами", "long-term client relationships"),
            V("intern / trainee", "stajyor", "стажёр", "стажёр", "learning role with supervision"),
        ],
    },
    "eb-cv-interview": {
        "goal": L(
            "CV va intervyu iboralari; tajriba uchun present perfect.",
            "CV ва интервью иборалари; тажриба учун present perfect.",
            "Фразы для CV и интервью; present perfect для опыта.",
            "CV/interview phrases; present perfect for experience.",
        ),
        "vocab": [
            V("I’m responsible for…", "men … uchun mas’ulman", "мен … учун масъулман", "я отвечаю за…", "describes your duties"),
            V("experience", "tajriba", "тажриба", "опыт", "what you have done before"),
            V("strengths", "kuchli tomonlar", "кучли томонлар", "сильные стороны", "what you do well"),
        ],
    },
    "eb-interview-speak": {
        "goal": L(
            "Odatiy intervyu savollariga 20–40 soniyada javob berasiz.",
            "Одатий интервью саволларига 20–40 сонияда жавоб берасиз.",
            "Отвечаете на типовые вопросы интервью за 20–40 секунд.",
            "Answer common interview questions in 20–40 seconds.",
        ),
        "vocab": [
            V("Tell me about yourself", "O‘zingiz haqingizda gapiring", "Ўзингиз ҳақингизда гапиринг", "Расскажите о себе", "classic interview opener"),
            V("strengths", "kuchli tomonlar", "кучли томонлар", "сильные стороны", "positive workplace traits"),
            V("weakness", "zaif tomon (halol + reja)", "заиф томон (ҳалол + режа)", "слабая сторона (честно + план)", "area you are improving"),
        ],
    },
    "eb-complaints": {
        "goal": L(
            "Shikoyatga empatiya, aniqlashtirish va keyingi qadam bilan javob berasiz.",
            "Шикоятга эмпатия, аниқлаштириш ва кейинги қадам билан жавоб берасиз.",
            "Отвечаете на жалобу: эмпатия, уточнение, следующий шаг.",
            "Respond to complaints with empathy, clarity, and a next step.",
        ),
        "vocab": [
            V("inconvenience", "noqulaylik", "ноқулайлик", "неудобство", "trouble caused to the customer"),
            V("escalate", "yuqori bosqichga uzatish", "юқори босқичга узатиш", "эскалировать", "pass to a higher level"),
            V("concern", "tashvish / e’tiroz", "ташвиш / эътироз", "беспокойство", "what worries the customer"),
        ],
    },
    "eb-phone": {
        "goal": L(
            "Telefonda salomlashish, identifikatsiya va hold iboralarini ishlatasiz.",
            "Телефонда саломлашиш, идентификация ва hold ибораларини ишлатасиз.",
            "Используете фразы приветствия, проверки личности и hold.",
            "Use clear phone phrases for ID checks and hold time.",
        ),
        "vocab": [
            V("hotline", "ishonch telefoni / call centre", "ишонч телефони / call centre", "горячая линия", "phone service for customers"),
            V("on hold", "kuting (chiziqda)", "кутинг (чизиқда)", "ожидание на линии", "please wait on the line"),
            V("verify", "tekshirish / tasdiqlash", "текшириш / тасдиқлаш", "проверить / подтвердить", "check that information is correct"),
        ],
    },
    "eb-complaint-email": {
        "goal": L(
            "Shikoyat emailini o‘qiysiz va professional qisqa javob yozasiz.",
            "Шикоят emailини ўқийсиз ва профессионал қисқа жавоб ёзасиз.",
            "Читаете жалобное письмо и пишете короткий профессиональный ответ.",
            "Read a complaint email and write a short professional reply.",
        ),
        "vocab": [
            V("refund", "pulni qaytarish", "пулни қайтариш", "возврат денег", "give money back"),
            V("double charge", "ikkita yechilish", "иккита ечилиш", "двойное списание", "charged twice"),
            V("confirm", "tasdiqlash", "тасдиқлаш", "подтвердить", "say that something is true/done"),
        ],
    },
    "eb-kyc": {
        "goal": L(
            "KYC ni oddiy va to‘g‘ri tushuntirasiz; hujjatlarni muloyim so‘raysiz.",
            "KYC ни оддий ва тўғри тушунтирасиз; ҳужжатларни мулойим сўрайсиз.",
            "Просто и точно объясняете KYC; вежливо просите документы.",
            "Explain KYC accurately; ask for documents politely.",
        ),
        "vocab": [
            V("KYC (Know Your Customer)", "mijozni bilish / identifikatsiya", "мижозни билиш / идентификация", "знай своего клиента (KYC)", "identifying and verifying the client"),
            V("proof of address", "yashash manzili tasdig‘i", "яшаш манзили тасдиғи", "подтверждение адреса", "shows where the client lives"),
            V("beneficial owner", "yakuniy egasi", "якуний эгаси", "бенефициарный владелец", "person who ultimately owns/controls a company"),
            V("onboarding", "yangi mijozni qabul qilish", "янги мижозни қабул қилиш", "онбординг клиента", "accepting a new client"),
        ],
    },
    "eb-aml": {
        "goal": L(
            "AML ni pre-intermediate darajada tushunasiz va qachon escalate qilishni bilasiz.",
            "AML ни pre-intermediate даражада тушунасиз ва қачон escalate қилишни биласиз.",
            "Понимаете AML на уровне pre-intermediate и когда эскалировать.",
            "Understand AML at pre-intermediate level; know when to escalate.",
        ),
        "vocab": [
            V("AML (Anti-Money Laundering)", "pul yuvishga qarshi kurash", "пул ювишга қарши кураш", "ПОД/ФТ (AML)", "rules against cleaning illegal money"),
            V("suspicious transaction", "shubhali operatsiya", "шубҳали операция", "подозрительная операция", "unusual activity that needs review"),
            V("source of funds", "pul manbai", "пул манбаи", "источник средств", "where the money comes from"),
        ],
    },
    "eb-ask-docs": {
        "goal": L(
            "KYC hujjatlarini qat’iy, lekin muloyim so‘raysiz.",
            "KYC ҳужжатларини қатъий, лекин мулойим сўрайсиз.",
            "Просите KYC-документы твёрдо, но вежливо.",
            "Ask for KYC documents firmly and politely.",
        ),
        "vocab": [
            V("passport / ID", "passport / shaxsni tasdiqlovchi hujjat", "паспорт / шахсни тасдиқловчи ҳужжат", "паспорт / удостоверение", "identity document"),
            V("originals", "asl nusxa", "асл нусха", "оригиналы", "original documents, not only photos"),
            V("complete KYC", "to‘liq KYC to‘plami", "тўлиқ KYC тўплами", "полный комплект KYC", "all required identity documents"),
        ],
    },
    "eb-email-write": {
        "goal": L(
            "Qisqa, muloyim, maqsadi aniq bank email yozasiz.",
            "Қисқа, мулойим, мақсади аниқ банк email ёзасиз.",
            "Пишете короткое вежливое письмо с ясной целью.",
            "Write short, polite, purpose-first banking emails.",
        ),
        "vocab": [
            V("Kind regards", "hurmat bilan (yopish)", "ҳурмат билан (ёпиш)", "С уважением", "professional email closing"),
            V("I am writing to…", "yozishdan maqsadim…", "ёзишдан мақсадим…", "Пишу, чтобы…", "states the email purpose"),
            V("deadline", "oxirgi muddat", "охирги муддат", "срок", "date by which something is needed"),
        ],
    },
    "eb-meetings": {
        "goal": L(
            "Qisqa ichki uchrashuvlarda ishtirok iboralarini ishlatasiz.",
            "Қисқа ички учрашувларада иштирок ибораларини ишлатасиз.",
            "Используете фразы для коротких внутренних встреч.",
            "Join short internal meetings with useful phrases.",
        ),
        "vocab": [
            V("Shall we start?", "Boshlaylikmi?", "Бошлайликми?", "Начнём?", "polite way to begin"),
            V("In my opinion…", "Menimcha…", "Менимча…", "По моему мнению…", "soft opinion opener"),
            V("Let’s summarise…", "Xulosalaylik…", "Хулосалайлик…", "Подведём итоги…", "close with clear actions"),
        ],
    },
    "eb-present-product": {
        "goal": L(
            "Bank mahsulotini 60–90 soniyada taqdim etasiz.",
            "Банк маҳсулотини 60–90 сонияда тақдим этасиз.",
            "Презентуете банковский продукт за 60–90 секунд.",
            "Present a simple bank product in 60–90 seconds.",
        ),
        "vocab": [
            V("benefit", "foyda / afzallik", "фойда / афзаллик", "выгода / преимущество", "main good point for the client"),
            V("call to action", "keyingi qadamga chorlash", "кейинги қадамга чорлаш", "призыв к действию", "ask the client to do something next"),
            V("fee / condition", "komissiya / shart", "комиссия / шарт", "комиссия / условие", "cost or rule to mention"),
        ],
    },
}


_H2_RE = re.compile(r"<h2>(.*?)</h2>", re.I | re.S)
_TH_RE = re.compile(r"<th>(.*?)</th>", re.I | re.S)
_DIALOGUE_BLOCK_RE = re.compile(
    r"(<h2 class=\"eb-h\">\s*Dialogue\b.*?</h2>)\s*(<p\b[^>]*>.*?</p>)",
    re.I | re.S,
)


def _inject_dialogue_translations(html: str, slug: str, lang: str) -> str:
    """Append a selected-language translation box under each English dialogue."""
    if lang == LANG_EN:
        return html

    from .english_banking_dialogues import DIALOGUE_LABEL, DIALOGUES, ROLES, pick

    items = DIALOGUES.get(slug) or []
    if not items:
        return html

    used = set()

    def repl(match: re.Match) -> str:
        heading = match.group(1)
        body = match.group(2)
        heading_plain = re.sub(r"<[^>]+>", "", heading)
        chosen = None
        for idx, item in enumerate(items):
            if idx in used:
                continue
            key = item.get("match") or ""
            if key.lower() in heading_plain.lower() or (
                key == "Dialogue" and heading_plain.strip().startswith("Dialogue") and "—" not in heading_plain and "-" not in heading_plain
            ):
                # Prefer specific matches; bare "Dialogue" only when heading is exactly Dialogue (± loc span)
                if key == "Dialogue":
                    core = re.sub(r"\s*·.*$", "", heading_plain).strip()
                    if core != "Dialogue":
                        continue
                chosen = item
                used.add(idx)
                break
        if chosen is None:
            # fallback: first unused item for this slug
            for idx, item in enumerate(items):
                if idx not in used:
                    chosen = item
                    used.add(idx)
                    break
        if chosen is None:
            return match.group(0)

        label = html_lib.escape(pick(DIALOGUE_LABEL, lang))
        lines_html = []
        for role, text_pack in chosen["lines"]:
            role_pack = ROLES.get(role) or L(role, role, role, role)
            role_loc = html_lib.escape(pick(role_pack, lang))
            text_loc = html_lib.escape(pick(text_pack, lang))
            lines_html.append(f"<p><strong>{role_loc}:</strong> {text_loc}</p>")
        box = (
            f'<aside class="eb-dialogue-tr">'
            f'<div class="eb-explain-label">{label}</div>'
            f'{"".join(lines_html)}'
            f"</aside>"
        )
        return f"{heading}\n{body}\n{box}"

    return _DIALOGUE_BLOCK_RE.sub(repl, html)


def enhance_eb_lesson(html: str, lang: str | None, slug: str | None) -> str:
    """Keep English learning text; localize explanations/meanings + add light structure."""
    if not html:
        return ""
    lang = normalize_language(lang)
    slug = (slug or "").strip()
    meta = LESSONS.get(slug, {})
    goal = _t(meta["goal"], lang) if meta.get("goal") else ""
    vocab_map = {}
    for item in meta.get("vocab") or []:
        word, meanings = item
        vocab_map[word.lower()] = _t(meanings, lang)
        # also key without parenthetical extras
        base = re.sub(r"\s*\(.*?\)$", "", word).strip().lower()
        vocab_map[base] = vocab_map[word.lower()]

    def heading_sub(match: re.Match) -> str:
        inner = match.group(1).strip()
        # Keep English title; add localized subtitle when available
        plain = re.sub(r"<[^>]+>", "", inner).strip()
        # Strip " — ..." tails for lookup of first part
        key = plain.split("—")[0].strip()
        key = key.split(":")[0].strip() if key.startswith("Reading") or key.startswith("Dialogue") else key
        for en_key, pack in HEADINGS.items():
            if plain == en_key or plain.startswith(en_key):
                loc = _t(pack, lang)
                if lang == LANG_EN or loc.lower() == en_key.lower():
                    return f'<h2 class="eb-h">{inner}</h2>'
                return f'<h2 class="eb-h">{inner}<span class="eb-h-loc"> · {html_lib.escape(loc)}</span></h2>'
        if plain.startswith("Dialogue"):
            loc = _t(L("Dialog", "Диалог", "Диалог", "Dialogue"), lang)
            return f'<h2 class="eb-h">{inner}<span class="eb-h-loc"> · {html_lib.escape(loc)}</span></h2>'
        if plain.startswith("Reading"):
            loc = _t(HEADINGS["Reading"], lang)
            return f'<h2 class="eb-h">{inner}<span class="eb-h-loc"> · {html_lib.escape(loc)}</span></h2>'
        if plain.startswith("Grammar"):
            loc = _t(HEADINGS["Grammar focus"], lang)
            return f'<h2 class="eb-h">{inner}<span class="eb-h-loc"> · {html_lib.escape(loc)}</span></h2>'
        return f'<h2 class="eb-h">{inner}</h2>'

    out = _H2_RE.sub(heading_sub, html)

    def th_sub(match: re.Match) -> str:
        inner = match.group(1).strip()
        plain = re.sub(r"<[^>]+>", "", inner).strip()
        pack = HEADINGS.get(plain)
        if not pack:
            return match.group(0)
        loc = _t(pack, lang)
        if lang == LANG_EN:
            return f"<th>{inner}</th>"
        return f'<th>{inner}<span class="eb-th-loc"> / {html_lib.escape(loc)}</span></th>'

    out = _TH_RE.sub(th_sub, out)

    out = _inject_dialogue_translations(out, slug, lang)

    if vocab_map:
        def row_sub_full(match: re.Match) -> str:
            full = match.group(0)
            m_word = re.search(r"<td[^>]*>\s*(?:<strong>)?(.*?)(?:</strong>)?\s*</td>", full, flags=re.I | re.S)
            if not m_word:
                return full
            word_html = m_word.group(1).strip()
            word_plain = re.sub(r"<[^>]+>", "", word_html).strip()
            gloss = vocab_map.get(word_plain.lower()) or vocab_map.get(
                word_plain.split("/")[0].strip().lower()
            )
            if not gloss:
                return full
            replaced_once = {"n": 0}

            def repl_td(m: re.Match) -> str:
                replaced_once["n"] += 1
                if replaced_once["n"] != 2:
                    return m.group(0)
                meaning_html = re.sub(r"^<td[^>]*>|</td>$", "", m.group(0), flags=re.I).strip()
                meaning_html = re.sub(r"^<|>$", "", meaning_html)
                # extract inner of td
                inner = re.sub(r"^<td[^>]*>", "", m.group(0), count=1, flags=re.I)
                inner = re.sub(r"</td>\s*$", "", inner, count=1, flags=re.I)
                return (
                    f'<td class="eb-meaning">'
                    f'<div class="eb-loc-mean">{html_lib.escape(gloss)}</div>'
                    f'<div class="eb-en-mean muted">{inner}</div>'
                    f"</td>"
                )

            return re.sub(r"<td\b[^>]*>.*?</td>", repl_td, full, count=2, flags=re.I | re.S)

        out = re.sub(
            r"<tr>\s*<td\b[^>]*>.*?</td>\s*<td\b[^>]*>.*?</td>.*?</tr>",
            row_sub_full,
            out,
            flags=re.I | re.S,
        )

    banner = html_lib.escape(_t(BANNER, lang))
    explain_lbl = html_lib.escape(_t(EXPLAIN_LABEL, lang))
    goal_box = ""
    if goal:
        goal_box = (
            f'<aside class="eb-explain"><div class="eb-explain-label">{explain_lbl}</div>'
            f"<p>{html_lib.escape(goal)}</p></aside>"
        )

    return (
        f'<div class="eb-lesson">'
        f'<div class="eb-banner">{banner}</div>'
        f"{goal_box}"
        f"{out}"
        f"</div>"
    )
