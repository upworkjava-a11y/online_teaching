"""Translated dialogue lines for English-for-Banking lessons (UI language)."""

from __future__ import annotations

from .languages import LANG_CYRL, LANG_EN, LANG_RU, LANG_UZ


def L(uz: str, cyrl: str, ru: str, en: str) -> dict[str, str]:
    return {LANG_UZ: uz, LANG_CYRL: cyrl, LANG_RU: ru, LANG_EN: en}

ROLES = {
    "Security": L("Xavfsizlik", "Хавфсизлик", "Охрана", "Security"),
    "Customer": L("Mijoz", "Мижоз", "Клиент", "Customer"),
    "Teller": L("Kassir", "Кассир", "Кассир", "Teller"),
    "Intern": L("Stajyor", "Стажёр", "Стажёр", "Intern"),
    "Mentor": L("Mentor", "Ментор", "Наставник", "Mentor"),
    "Officer": L("Xodim", "Ходим", "Сотрудник", "Officer"),
    "Hotline": L("Ishonch telefoni", "Ишонч телефони", "Горячая линия", "Hotline"),
    "HR": L("HR", "HR", "HR", "HR"),
    "Candidate": L("Nomzod", "Номзод", "Кандидат", "Candidate"),
    "Agent": L("Operator", "Оператор", "Оператор", "Agent"),
    "Caller": L("Qo‘ng‘iroq qiluvchi", "Қўнғироқ қилувчи", "Звонящий", "Caller"),
    "Supervisor": L("Nazoratchi", "Назоратчи", "Руководитель", "Supervisor"),
    "RM": L("Mijoz menejeri (RM)", "Мижоз менежери (RM)", "Клиентский менеджер (RM)", "RM"),
    "Owner": L("Biznes egasi", "Бизнес эгаси", "Владелец бизнеса", "Owner"),
    "Importer": L("Importyor", "Импортёр", "Импортёр", "Importer"),
    "Trade officer": L("Trade xodimi", "Trade ходими", "Сотрудник trade finance", "Trade officer"),
    "Contractor": L("Pudratchi", "Пудратчи", "Подрядчик", "Contractor"),
    "A": L("A", "A", "A", "A"),
    "B": L("B", "B", "B", "B"),
}

DIALOGUE_LABEL = L(
    "Dialog tarjimasi",
    "Диалог таржимаси",
    "Перевод диалога",
    "Dialogue translation",
)


def _line(role: str, uz: str, cyrl: str, ru: str, en: str) -> tuple:
    return (role, L(uz, cyrl, ru, en))


# match: unique part of the Dialogue heading (after “Dialogue”)
DIALOGUES: dict[str, list[dict]] = {
    "eb-welcome": [
        {
            "match": "at the entrance",
            "lines": [
                _line("Security", "Xayrli tong. Sizga qanday yordam bera olaman?", "Хайрли тонг. Сизга қандай ёрдам бера оламан?", "Доброе утро. Чем могу помочь?", "Good morning. How can I help you?"),
                _line("Customer", "Xayrli tong. Yangi hisob haqida kimdir bilan gaplashmoqchiman.", "Хайрли тонг. Янги ҳисоб ҳақида кимдир билан гаплашмоқчиман.", "Доброе утро. Я хотел бы поговорить с кем-нибудь о новом счёте.", "Good morning. I’d like to speak to someone about a new account."),
                _line("Security", "Iltimos, talon oling va retail banking navbatida kuting.", "Илтимос, талон олинг ва retail banking навбатида кутинг.", "Пожалуйста, возьмите талон и подождите в очереди розничного банкинга.", "Please take a ticket and wait in the retail banking queue."),
                _line("Customer", "Rahmat.", "Раҳмат.", "Спасибо.", "Thank you."),
            ],
        },
        {
            "match": "at the counter",
            "lines": [
                _line("Teller", "Keyingi, iltimos. Sizga qanday yordam bera olaman?", "Кейинги, илтимос. Сизга қандай ёрдам бера оламан?", "Следующий, пожалуйста. Чем могу помочь?", "Next, please. How can I help you?"),
                _line("Customer", "Jamg‘arma hisobi ochmoqchiman.", "Жамғарма ҳисоби очмоқчиман.", "Я хотел бы открыть сберегательный счёт.", "I’d like to open a savings account."),
                _line("Teller", "Albatta. Pasportingizni ko‘rsatib berasizmi?", "Албатта. Паспортингизни кўрсатиб берасизми?", "Конечно. Могу я увидеть ваш паспорт?", "Of course. May I see your passport?"),
                _line("Customer", "Marhamat.", "Марҳамат.", "Пожалуйста.", "Here you are."),
                _line("Teller", "Rahmat. O‘tirib turing. Men blankalarni tayyorlayman.", "Раҳмат. Ўтириб туринг. Мен бланкаларни тайёрлайман.", "Спасибо. Присаживайтесь. Я подготовлю бланки.", "Thank you. Please take a seat. I’ll prepare the forms."),
            ],
        },
    ],
    "eb-departments": [
        {
            "match": "Who should I ask",
            "lines": [
                _line("Intern", "Kompaniya katta biznes-kredit olmoqchi. Kimga qo‘ng‘iroq qilay?", "Компания катта бизнес-кредит олмоқчи. Кимга қўнғироқ қилай?", "Компания хочет крупный бизнес-кредит. Кому позвонить?", "A company wants a large business loan. Who should I call?"),
                _line("Mentor", "Bu korporativ banking va kredit. Faylni kredit tahlilchisiga yuboring.", "Бу корпоратив банкинг ва кредит. Файлни кредит таҳлилчисига юборинг.", "Это корпоративный банкинг и кредит. Отправьте файл кредитному аналитику.", "That’s corporate banking and credit. Send the file to the credit analyst."),
                _line("Intern", "Agar mijoz passporti g‘alati ko‘rinsa-chi?", "Агар мижоз паспорти ғалати кўринса-чи?", "А если паспорт клиента выглядит странно?", "And if the client’s passport looks strange?"),
                _line("Mentor", "To‘xtating va Compliance ga escalate qiling. Hali hisob ochmang.", "Тўхтатинг ва Compliance га escalate қилинг. Ҳали ҳисоб очманг.", "Остановитесь и эскалируйте в Compliance. Пока не открывайте счёт.", "Stop and escalate to Compliance. Don’t open the account yet."),
                _line("Intern", "Tushundim. Rahmat!", "Тушундим. Раҳмат!", "Понял. Спасибо!", "Understood. Thanks!"),
            ],
        },
    ],
    "eb-polite-talk": [
        {
            "match": "Missing document",
            "lines": [
                _line("Officer", "Arizangiz uchun rahmat. Afsuski, hali yashash manzili tasdig‘i kerak.", "Аризангиз учун раҳмат. Афсуски, ҳали яшаш манзили тасдиғи керак.", "Спасибо за вашу заявку. К сожалению, нам всё ещё нужно подтверждение адреса.", "Thank you for your application. I’m afraid we still need proof of address."),
                _line("Customer", "Bugun u men bilan emas.", "Бугун у мен билан эмас.", "Сегодня его нет с собой.", "I don’t have it with me today."),
                _line("Officer", "Muammo yo‘q. Ertaga kommunal to‘lov kvitansiyasi yoki ijara shartnomasini olib kelasizmi?", "Муаммо йўқ. Эртага коммунал тўлов квитанцияси ёки ижара шартномасини олиб келасизми?", "Ничего страшного. Не могли бы вы завтра принести квитанцию ЖКХ или договор аренды?", "No problem. Could you bring a utility bill or a rental contract tomorrow?"),
                _line("Customer", "Ha, olib kelaman.", "Ҳа, олиб келаман.", "Да, могу.", "Yes, I can."),
                _line("Officer", "Ajoyib. Faylingizni tayyor holda saqlayman. Tushunganingiz uchun rahmat.", "Ажойиб. Файлингизни тайёр ҳолда сақлайман. Тушунганингиз учун раҳмат.", "Отлично. Я оставлю ваше дело готовым. Спасибо за понимание.", "Great. I’ll keep your file ready. Thank you for understanding."),
            ],
        },
    ],
    "eb-account-types": [
        {
            "match": "Choosing an account",
            "lines": [
                _line("Customer", "Hisob ochmoqchiman. Qaysi turini bilmayman.", "Ҳисоб очмоқчиман. Қайси турини билмайман.", "Я хотел бы открыть счёт. Не уверен, какой тип.", "I’d like to open an account. I’m not sure which type."),
                _line("Officer", "U kundalik to‘lovlar uchunmi yoki asosan jamg‘arish uchunmi?", "У кундалик тўловлар учунми ёки асосан жамғариш учунми?", "Он нужен для ежедневных платежей или в основном для накоплений?", "Do you need it for daily payments or mainly to save?"),
                _line("Customer", "Asosan jamg‘arish, lekin karta ham kerak.", "Асосан жамғариш, лекин карта ҳам керак.", "В основном копить, но карта тоже нужна.", "Mostly to save, but I also want a card."),
                _line("Officer", "Unda jamg‘arma hisobi plus debet karta mos keladi. Foiz va komissiyalarni tushuntiraymi?", "Унда жамғарма ҳисоби плюс дебет карта мос келади. Фоиз ва комиссияларни тушунтирайми?", "Тогда подойдут сберегательный счёт и дебетовая карта. Объяснить ставку и комиссии?", "Then a savings account plus a debit card can work. Would you like me to explain the interest rate and fees?"),
                _line("Customer", "Ha, iltimos.", "Ҳа, илтимос.", "Да, пожалуйста.", "Yes, please."),
            ],
        },
    ],
    "eb-deposit-withdraw": [
        {
            "match": "At the teller",
            "lines": [
                _line("Customer", "Bu naqd pulni jamg‘arma hisobimga qo‘ymoqchiman.", "Бу нақд пулни жамғарма ҳисобимга қўймоқчиман.", "Я хотел бы внести эти наличные на сберегательный счёт.", "I’d like to deposit this cash into my savings account."),
                _line("Teller", "Albatta. Iltimos, depozit blankasini to‘ldiring va shu yerga imzo qo‘ying.", "Албатта. Илтимос, депозит бланкасини тўлдиринг ва шу ерга имзо қўйинг.", "Конечно. Заполните квитанцию и распишитесь здесь.", "Certainly. Please fill in the deposit slip and sign here."),
                _line("Customer", "Tayyor. Dam olish uchun yana 300 000 yecholamanmi?", "Тайёр. Дам олиш учун яна 300 000 ечоламанми?", "Готово. Могу ли я также снять 300 000 на выходные?", "Done. Can I also withdraw 300,000 for the weekend?"),
                _line("Teller", "Ha. ID ko‘rsatib berasizmi? … Rahmat. Naqd va chekingiz.", "Ҳа. ID кўрсатиб берасизми? … Раҳмат. Нақд ва чекингиз.", "Да. Могу увидеть ID? … Спасибо. Вот наличные и чек.", "Yes. May I see your ID? … Thank you. Here is your cash and receipt."),
                _line("Customer", "Yangi balansimni aytib bera olasizmi?", "Янги балансимни айтиб бера оласизми?", "Не могли бы вы сказать мой новый баланс?", "Could you tell me my new balance?"),
                _line("Teller", "Albatta. Mavjud balansingiz 4 250 000 so‘m.", "Албатта. Мавжуд балансингиз 4 250 000 сўм.", "Конечно. Доступный баланс — 4 250 000 сум.", "Of course. Your available balance is 4,250,000 UZS."),
            ],
        },
    ],
    "eb-statement": [
        {
            "match": "Explaining a line",
            "lines": [
                _line("Customer", "Bu minus 400 000 nima?", "Бу минус 400 000 нима?", "Что это за минус 400 000?", "What is this minus 400,000?"),
                _line("Officer", "Bu 14-martdagi ATM dan yechilgan summa.", "Бу 14-мартдаги ATM дан ечилган сумма.", "Это снятие в банкомате 14 марта.", "That is an ATM withdrawal on 14 March."),
                _line("Customer", "Plus 85 000-chi?", "Плюс 85 000-чи?", "А плюс 85 000?", "And the plus 85,000?"),
                _line("Officer", "Bu do‘kondan qaytarilgan pul. Mablag‘ hisobingizga qaytdi.", "Бу дўкондан қайтарилган пул. Маблағ ҳисобингизга қайтди.", "Это возврат из магазина. Деньги вернулись на ваш счёт.", "That’s a refund from a shop. The money came back to your account."),
            ],
        },
    ],
    "eb-cards": [
        {
            "match": "Which card",
            "lines": [
                _line("Customer", "Debet va kredit farqi nima?", "Дебет ва кредит фарқи нима?", "В чём разница между дебетовой и кредитной картой?", "What’s the difference between debit and credit?"),
                _line("Officer", "Debet kartada pul darhol hisobingizdan yechiladi. Kredit kartada limitgacha qarz olasiz va keyin qaytarasiz.", "Дебет картада пул дарҳол ҳисобингиздан ечилади. Кредит картада лимитгача қарз оласиз ва кейин қайтарасиз.", "С дебетовой карты деньги сразу списываются со счёта. С кредитной вы берёте взаймы до лимита и потом возвращаете.", "With a debit card, the money comes from your account immediately. With a credit card, you borrow up to your credit limit and repay later."),
                _line("Customer", "Kredit bepulmi?", "Кредит бепулми?", "Кредит бесплатный?", "Is credit free?"),
                _line("Officer", "Har doim emas. Vaqtida to‘lamasangiz, foiz va komissiya bo‘lishi mumkin. Misol ko‘rsataymi?", "Ҳар доим эмас. Вақтида тўламасангиз, фоиз ва комиссия бўлиши мумкин. Мисол кўрсатайми?", "Не всегда. Если не погасите вовремя, могут быть проценты и комиссии. Показать пример?", "Not always. If you don’t repay on time, you may pay interest and fees. Would you like me to show an example?"),
            ],
        },
    ],
    "eb-transfers": [
        {
            "match": "Transfer desk",
            "lines": [
                _line("Customer", "Yetkazib beruvchimga 1 500 000 so‘m o‘tkazmoqchiman.", "Етказиб берувчимга 1 500 000 сўм ўтказмоқчиман.", "Я хотел бы перевести 1 500 000 сум поставщику.", "I’d like to transfer 1,500,000 UZS to my supplier."),
                _line("Officer", "Albatta. Oluvchining hisob raqami qanday?", "Албатта. Олувчининг ҳисоб рақами қандай?", "Конечно. Какой номер счёта получателя?", "Certainly. What’s the beneficiary’s account number?"),
                _line("Customer", "Mana.", "Мана.", "Вот он.", "Here it is."),
                _line("Officer", "Rahmat. Oxirgi to‘rt raqamni men bilan tekshiring: 7-7-2-1.", "Раҳмат. Охирги тўрт рақамни мен билан текширинг: 7-7-2-1.", "Спасибо. Давайте сверим последние четыре цифры: 7-7-2-1.", "Thank you. Please double-check the last four digits with me: 7-7-2-1."),
                _line("Customer", "Ha, to‘g‘ri. Komissiya bormi?", "Ҳа, тўғри. Комиссия борми?", "Да, верно. Есть комиссия?", "Yes, that’s correct. Is there a fee?"),
                _line("Officer", "Ha, kichik o‘tkazma komissiyasi. Davom ettiraymi?", "Ҳа, кичик ўтказма комиссияси. Давом эттирайми?", "Да, небольшая комиссия за перевод. Продолжить?", "Yes, a small transfer fee. Shall I continue?"),
            ],
        },
    ],
    "eb-atm-safety": [
        {
            "match": "Lost card",
            "lines": [
                _line("Customer", "Salom, debet kartamni yo‘qotdim.", "Салом, дебет картамни йўқотдим.", "Здравствуйте, я потерял дебетовую карту.", "Hello, I’ve lost my debit card."),
                _line("Hotline", "Afsusdaman. Hozir bloklab qo‘yishim mumkin. To‘liq ismingiz va tug‘ilgan sanangizni tasdiqlaysizmi?", "Афсусдаман. Ҳозир блоклаб қўйишим мумкин. Тўлиқ исмингиз ва туғилган санангизни тасдиқлайсизми?", "Сожалею. Могу сразу заблокировать. Подтвердите полное имя и дату рождения?", "I’m sorry to hear that. I can block it now. May I verify your full name and date of birth?"),
                _line("Customer", "Ha…", "Ҳа…", "Да…", "Yes…"),
                _line("Hotline", "Tayyor. Karta bloklandi. Yangisini buyurtma qilasizmi?", "Тайёр. Карта блокланди. Янгисини буюртма қиласизми?", "Готово. Карта заблокирована. Хотите заказать новую?", "Done. Your card is blocked. Would you like to order a replacement?"),
            ],
        },
    ],
    "eb-loan-basics": [
        {
            "match": "First loan questions",
            "lines": [
                _line("Customer", "Iste’mol krediti uchun ariza topshirmoqchiman.", "Истеъмол кредити учун ариза топширмоқчиман.", "Я хотел бы подать заявку на потребительский кредит.", "I’d like to apply for a consumer loan."),
                _line("Officer", "Albatta. Qancha qarz olmoqchisiz va necha oyga?", "Албатта. Қанча қарз олмоқчисиз ва неча ойга?", "Конечно. Какую сумму и на сколько месяцев?", "Certainly. How much would you like to borrow, and for how many months?"),
                _line("Customer", "Taxminan 30 million so‘m, 24 oyga.", "Тахминан 30 миллион сўм, 24 ойга.", "Около 30 миллионов сум на 24 месяца.", "About 30 million UZS for 24 months."),
                _line("Officer", "Daromad, ish joyi va kredit tarixingizni tekshiramiz. Foiz stavkasi profilingizga bog‘liq.", "Даромад, иш жойи ва кредит тарихинигизни текширамиз. Фоиз ставкаси профилингизга боғлиқ.", "Мы проверим доход, занятость и кредитную историю. Ставка зависит от вашего профиля.", "We’ll check your income, employment, and credit history. The interest rate depends on your profile."),
            ],
        },
    ],
    "eb-mortgage": [
        {
            "match": "Dialogue",
            "lines": [
                _line("Customer", "Kvartira uchun ipoteka olmoqchimiz.", "Квартира учун ипотека олмоқчимиз.", "Мы хотим ипотеку на квартиру.", "We want a mortgage for an apartment."),
                _line("Officer", "Rejangiz bilan tabriklayman. Kvartira odatda garov bo‘ladi. Daromad hujjatlari va baholash kerak.", "Режангиз билан табриклайман. Квартира одатда гаров бўлади. Даромад ҳужжатлари ва баҳолаш керак.", "Поздравляю с планом. Квартира обычно будет залогом. Нужны документы о доходе и оценка.", "Congratulations on the plan. The apartment will usually be the collateral. We’ll need income documents and a valuation."),
                _line("Customer", "Tasdiqlash qancha vaqt oladi?", "Тасдиқлаш қанча вақт олади?", "Сколько занимает одобрение?", "How long does approval take?"),
                _line("Officer", "Faylga bog‘liq. Bugun sizga checklist beraman.", "Файлга боғлиқ. Бугун сизга checklist бераман.", "Зависит от дела. Сегодня дам вам чек-лист.", "It depends on the file. I’ll give you a checklist today."),
            ],
        },
    ],
    "eb-overdue": [
        {
            "match": "Overdue call",
            "lines": [
                _line("Officer", "Xayrli kun. Kredit to‘lovingiz haqida qo‘ng‘iroq qilyapman. Afsuski, u 5 kunga kechikkan.", "Хайрли кун. Кредит тўловингиз ҳақида қўнғироқ қиляпман. Афсуски, у 5 кунга кечиккан.", "Добрый день. Звоню по взносу по кредиту. К сожалению, просрочка уже пять дней.", "Good afternoon. I’m calling about your loan installment. I’m afraid it is overdue by five days."),
                _line("Customer", "Oh — oyligim kechikdi.", "Оҳ — ойлигим кечикди.", "Ох — зарплата задержалась.", "Oh — I had a delay with my salary."),
                _line("Officer", "Tushunaman. Ertaga ertalab to‘lasangiz, qo‘shimcha jarimalarni kamaytirasiz. Aniq summani SMS qilaymi?", "Тушунаман. Эртага эрталаб тўласангиз, қўшимча жарималарни камайтирасиз. Аниқ суммани SMS қилайми?", "Понимаю. Если оплатите завтра утром, уменьшите дальнейшие пени. Отправить точную сумму по SMS?", "I understand. If you pay tomorrow morning, you will reduce further penalties. Shall I SMS the exact amount due?"),
            ],
        },
    ],
    "eb-job-titles": [
        {
            "match": "Networking",
            "lines": [
                _line("A", "Salom, bu yerda nima qilasiz?", "Салом, бу ерда нима қиласиз?", "Привет, чем вы здесь занимаетесь?", "Hi, what do you do here?"),
                _line("B", "Men compliance xodiman. KYC fayllari va noodatiy operatsiyalarni ko‘rib chiqaman.", "Мен compliance ходиман. KYC файллари ва ноодатий операцияларни кўриб чиқаман.", "Я сотрудник комплаенса. Проверяю KYC-файлы и необычные операции.", "I’m a compliance officer. I review KYC files and unusual transactions."),
                _line("A", "Muhim ish ekan.", "Муҳим иш экан.", "Звучит важно.", "That sounds important."),
                _line("B", "Ha. Siz-chi?", "Ҳа. Сиз-чи?", "Да. А вы?", "It is. And you?"),
                _line("A", "Men SME mijozlari uchun relationship managerman.", "Мен SME мижозлари учун relationship managerман.", "Я relationship manager по SME-клиентам.", "I’m a relationship manager for SME clients."),
            ],
        },
    ],
    "eb-cv-interview": [
        {
            "match": "Short interview",
            "lines": [
                _line("HR", "O‘zingiz haqingizda gapirib bering.", "Ўзингиз ҳақингизда гапириб беринг.", "Расскажите о себе.", "Tell me about yourself."),
                _line("Candidate", "Men Dilshodman. Retail mijoz xizmatida bir yillik tajribam bor. Hisob va kartalar bo‘yicha mijozlarga yordam beraman. Bankingda o‘sishni xohlayman.", "Мен Дилшодман. Retail мижоз хизматида бир йиллик тажрибам бор. Ҳисоб ва карталар бўйича мижозларга ёрдам бераман. Банкингда ўсишни хоҳлайман.", "Я Дилшод. У меня год опыта в розничном обслуживании. Помогаю клиентам со счетами и картами. Хочу расти в банкинге.", "I’m Dilshod. I have one year of experience in retail customer service. I’m responsible for helping clients with accounts and cards. I’d like to grow in banking."),
                _line("HR", "Kuchli tomonlaringiz nima?", "Кучли томонларингиз нима?", "Какие у вас сильные стороны?", "What are your strengths?"),
                _line("Candidate", "Men tizimli, muloyimman va detallarga e’tiborliman.", "Мен тизимли, мулойимман ва деталларга эътиборлиман.", "Я организованный, вежливый и внимательный к деталям.", "I’m organised, polite, and careful with details."),
            ],
        },
    ],
    "eb-complaints": [
        {
            "match": "Fee surprise",
            "lines": [
                _line("Customer", "Nega bu komissiyani oldingiz? Hech kim aytmagan!", "Нега бу комиссияни олдингиз? Ҳеч ким айтмаган!", "Почему вы взяли эту комиссию? Мне никто не говорил!", "Why did you take this fee? Nobody told me!"),
                _line("Officer", "Noqulaylik uchun uzr. Tarif va sanani tekshiraman… Siz haqsiz — bu komissiyani aniqroq tushuntirishimiz kerak edi. Tafsilotni chop etaman va variantlarni aytaman.", "Ноқулайлик учун узр. Тариф ва санани текшираман… Сиз ҳақсиз — бу комиссияни аниқроқ тушунтиришимиз керак эди. Тафсилотни чоп этаман ва вариантларни айтаман.", "Извините за неудобство. Проверю тариф и дату… Вы правы — мы должны были объяснить комиссию яснее. Распечатаю детали и объясню варианты.", "I’m sorry for the inconvenience. Let me check your tariff and the transaction date… You’re right — we should have explained this fee more clearly. I’ll print the details and explain your options."),
            ],
        },
    ],
    "eb-phone": [
        {
            "match": "Dialogue",
            "lines": [
                _line("Agent", "Orient Bank ishonch telefoni, Jasur gapiryapti. Qanday yordam bera olaman?", "Orient Bank ишонч телефони, Жасур гапиряпти. Қандай ёрдам бера оламан?", "Горячая линия Orient Bank, говорит Жасур. Чем могу помочь?", "Orient Bank hotline, Jasur speaking. How can I help you?"),
                _line("Caller", "Kartam onlaynda ishlamayapti.", "Картам онлайнда ишламаяпти.", "Моя карта не работает онлайн.", "My card isn’t working online."),
                _line("Agent", "Afsusman. Xavfsizlik uchun to‘liq ism va tug‘ilgan sanani tasdiqlaysizmi?", "Афсусман. Хавфсизлик учун тўлиқ исм ва туғилган санани тасдиқлайсизми?", "Сожалею. Для безопасности подтвердите полное имя и дату рождения?", "I’m sorry about that. For security, could you confirm your full name and date of birth?"),
                _line("Caller", "…", "…", "…", "…"),
                _line("Agent", "Rahmat. Tekshirayotganimda biroz kuta olasizmi?", "Раҳмат. Текшираётганимда бироз кута оласизми?", "Спасибо. Могу поставить вас на ожидание на минуту, пока проверю?", "Thank you. Can I put you on hold for a moment while I check?"),
                _line("Caller", "Ha.", "Ҳа.", "Да.", "Yes."),
                _line("Agent", "Kutganingiz uchun rahmat. Onlayn to‘lovlarda vaqtinchalik blok ko‘ryapman. Yana bir tekshiruvdan keyin olib tashlashim mumkin…", "Кутганингиз учун раҳмат. Онлайн тўловларда вақтинчалик блок кўряпман. Яна бир текширувдан кейин олиб ташлашим мумкин…", "Спасибо за ожидание. Вижу временную блокировку онлайн-платежей. После ещё одной проверки смогу снять…", "Thanks for holding. I can see a temporary block for online payments. I can remove it after one more check…"),
            ],
        },
    ],
    "eb-kyc": [
        {
            "match": "Dialogue",
            "lines": [
                _line("Officer", "Compliance sababli passport va yashash manzili tasdig‘ini ko‘rishim kerak.", "Compliance сабабли паспорт ва яшаш манзили тасдиғини кўришим керак.", "По требованиям комплаенса мне нужно увидеть паспорт и подтверждение адреса.", "For compliance reasons, I need to see your passport and proof of address."),
                _line("Customer", "Nega buncha ko‘p hujjat?", "Нега бунча кўп ҳужжат?", "Почему так много документов?", "Why so many documents?"),
                _line("Officer", "Bu Know Your Customer qoidalari. Hisob ochishdan oldin shaxsni tekshiramiz. Bu sizni va bankni himoya qiladi.", "Бу Know Your Customer қоидалари. Ҳисоб очишдан олдин шахсни текширамиз. Бу сизни ва банкни ҳимоя қилади.", "Это правила Know Your Customer. Мы проверяем личность до открытия счёта. Это защищает вас и банк.", "It’s part of Know Your Customer rules. We verify identity before we open an account. It protects you and the bank."),
            ],
        },
    ],
    "eb-aml": [
        {
            "match": "Escalate calmly",
            "lines": [
                _line("Teller", "Bu naqd depozit ushbu hisob uchun odatdagidan ancha katta.", "Бу нақд депозит ушбу ҳисоб учун одатдагидан анча катта.", "Этот наличный депозит намного больше обычного для этого счёта.", "This cash deposit is much larger than usual for this account."),
                _line("Supervisor", "Sezganingiz uchun rahmat. Hali o‘tkazmang. Compliance ga escalate qiling va mijozni muloyim xabardor qiling.", "Сезганингиз учун раҳмат. Ҳали ўтказманг. Compliance га escalate қилинг ва мижозни мулойим хабардор қилинг.", "Спасибо, что заметили. Пока не проводите. Эскалируйте в Compliance и вежливо сообщите клиенту.", "Thank you for noticing. Don’t process it yet. Escalate to Compliance and keep the client informed politely."),
                _line("Teller", "“Suspicious” deb aytaymi?", "“Suspicious” деб айтайми?", "Говорить «подозрительная»?", "Should I say “suspicious”?"),
                _line("Supervisor", "Yaxshiroq: “Qo‘shimcha compliance tekshiruvi kerak.” Xotirjam va faktlarga asoslaning.", "Яхшироқ: “Қўшимча compliance текшируви керак.” Хотиржам ва фактларга асосланинг.", "Лучше: «Нужна дополнительная проверка комплаенса.» Спокойно и по фактам.", "Better: “We need an additional compliance check.” Stay calm and factual."),
            ],
        },
    ],
    "eb-fx-basics": [
        {
            "match": "FX counter",
            "lines": [
                _line("Customer", "Xayrli tong. So‘mni AQSH dollariga ayirboshlamoqchiman.", "Хайрли тонг. Сўмни АҚШ долларига айирбошламоқчиман.", "Доброе утро. Хочу обменять сумы на доллары США.", "Good morning. I’d like to exchange Uzbek sums for US dollars."),
                _line("Officer", "Albatta. Qancha sotib olmoqchisiz?", "Албатта. Қанча сотиб олмоқчисиз?", "Конечно. Сколько хотите купить?", "Certainly. How much would you like to buy?"),
                _line("Customer", "300 dollar.", "300 доллар.", "300 долларов.", "300 dollars."),
                _line("Officer", "Bugungi sotish kursi doskada. ID ko‘rsatib berasizmi? Katta summalar uchun qo‘shimcha tekshiruv bo‘lishi mumkin.", "Бугунги сотиш курси доскада. ID кўрсатиб берасизми? Катта суммалар учун қўшимча текширув бўлиши мумкин.", "Курс продажи сегодня на табло. Могу увидеть ID? Для крупных сумм могут быть доп. проверки.", "Our sell rate today is on the board. May I see your ID? For larger amounts we may need extra checks."),
                _line("Customer", "Marhamat. Komissiya bormi?", "Марҳамат. Комиссия борми?", "Пожалуйста. Есть комиссия?", "Here you are. Are there any fees?"),
                _line("Officer", "Kurs allaqachon spredni o‘z ichiga oladi. Shu yerga imzo qo‘ying va naqdni sanang.", "Курс аллақачон спредни ўз ичига олади. Шу ерга имзо қўйинг ва нақдни сананг.", "Курс уже включает наш спред. Подпишите здесь и пересчитайте наличные.", "The rate already includes our spread. Please sign here and count the cash."),
            ],
        },
    ],
    "eb-remittance": [
        {
            "match": "Sending money home",
            "lines": [
                _line("Customer", "Ota-onamga xorijga pul yuborishim kerak.", "Ота-онамга хорижга пул юборишим керак.", "Мне нужно отправить деньги родителям за границу.", "I need to send money to my parents abroad."),
                _line("Officer", "Xalqaro o‘tkazmada yordam beramiz. Oluvchining to‘liq ismi, hisob ma’lumotlari va bank SWIFT kodi kerak.", "Халқаро ўтказмада ёрдам берамиз. Олувчининг тўлиқ исми, ҳисоб маълумотлари ва банк SWIFT коди керак.", "Поможем с международным переводом. Нужны полное имя получателя, реквизиты и SWIFT-код банка.", "We can help with an international transfer. I’ll need the beneficiary’s full name, account details, and the bank’s SWIFT code."),
                _line("Customer", "Qancha vaqt oladi?", "Қанча вақт олади?", "Сколько времени займёт?", "How long will it take?"),
                _line("Officer", "Odatda 1–3 ish kuni, yo‘nalish va cut-off ga bog‘liq. O‘tkazma komissiyasi bor, valyuta farq qilsa kurs qo‘llanadi.", "Одатда 1–3 иш куни, йўналиш ва cut-off га боғлиқ. Ўтказма комиссияси бор, валюта фарқ қилса курс қўлланади.", "Обычно 1–3 рабочих дня, зависит от коридора и cut-off. Есть комиссия, при разных валютах применяется курс.", "It usually takes one to three working days, depending on the corridor and cut-off time. There is a transfer fee, and the exchange rate applies if currencies differ."),
                _line("Customer", "Kuzatib bora olamanmi?", "Кузатиб бора оламанми?", "Могу ли я отследить перевод?", "Can I track it?"),
                _line("Officer", "Ha. Sizga reference raqam beramiz.", "Ҳа. Сизга reference рақам берамиз.", "Да. Мы дадим вам номер ссылки.", "Yes. We’ll give you a reference number."),
            ],
        },
    ],
    "eb-fx-fees": [
        {
            "match": "Transparent pricing",
            "lines": [
                _line("Customer", "Oilam to‘liq summani oladimi?", "Оилам тўлиқ суммани оладими?", "Семья получит полную сумму?", "Will my family receive the full amount?"),
                _line("Officer", "Taxminiy hisob beraman. Komissiyamiz shu yerda olinadi. Qabul qiluvchi bank o‘z komissiyasini olishi mumkin. Avval kichik test o‘tkazma qilishni xohlaysizmi?", "Тахминий ҳисоб бераман. Комиссиямиз шу ерда олинади. Қабул қилувчи банк ўз комиссиясини олиши мумкин. Аввал кичик тест ўтказма қилишни хоҳлайсизми?", "Дам оценку. Наша комиссия берётся здесь. Банк получателя может взять свою. Хотите сначала небольшой тестовый перевод?", "I’ll give you an estimate. Our fee is charged here. The receiving bank may apply its own fee. Would you like a smaller amount first as a test transfer?"),
            ],
        },
    ],
    "eb-sme-basics": [
        {
            "match": "First business meeting",
            "lines": [
                _line("RM", "Tashrifingiz uchun rahmat. Biznes modelingizni ikki daqiqada aytib bering.", "Ташрифингиз учун раҳмат. Бизнес моделингизни икки дақиқада айтиб беринг.", "Спасибо за визит. Расскажите о бизнес-модели за две минуты.", "Thanks for visiting. Tell me about your business model in two minutes."),
                _line("Owner", "Ehtiyot qismlarni import qilib, mahalliy ustaxonalarga sotamiz.", "Эҳтиёт қисмларни импорт қилиб, маҳаллий устахоналарга сотамиз.", "Импортируем запчасти и продаём местным СТО.", "We import spare parts and sell to local garages."),
                _line("RM", "Tushundim. Biznes joriy hisobi, yetkazib beruvchilar uchun FX va ehtimol aylanma mablag‘ kerak bo‘lishi mumkin. Kompaniya va beneficial owner lar uchun KYC dan boshlaymiz.", "Тушундим. Бизнес жорий ҳисоби, етказиб берувчилар учун FX ва эҳтимол айланма маблағ керак бўлиши мумкин. Компания ва beneficial owner лар учун KYC дан бошлаймиз.", "Понял. Могут понадобиться расчётный счёт, FX для поставщиков и, возможно, оборотный кредит. Начнём с KYC компании и бенефициарных владельцев.", "Understood. You may need a business current account, FX for suppliers, and possibly a working-capital facility. We’ll start with KYC for the company and beneficial owners."),
            ],
        },
    ],
    "eb-letter-of-credit": [
        {
            "match": "Dialogue",
            "lines": [
                _line("Importer", "Yetkazib beruvchimiz LC so‘rayapti, open account emas.", "Етказиб берувчимиз LC сўраяпти, open account эмас.", "Поставщик просит LC, а не open account.", "Our supplier wants an LC, not open account."),
                _line("Trade officer", "Yangi savdo munosabatlarida bu odatiy. Shartnoma, kompaniya hujjatlari, tovar va yetkazib berish tafsilotlari kerak.", "Янги савдо муносабатларида бу одатий. Шартнома, компания ҳужжатлари, товар ва етказиб бериш тафсилотлари керак.", "Это обычно при новых торговых отношениях. Нужны контракт, документы компании, детали товара и поставки.", "That’s common in new trade relationships. We’ll need the contract, company documents, and details of goods and shipment."),
                _line("Importer", "LC kredit bilan bir xilmi?", "LC кредит билан бир хилми?", "LC — это то же самое, что кредит?", "Is an LC the same as a loan?"),
                _line("Trade officer", "Bu shartli to‘lov majburiyati. Kredit liniyangizni band qilishi mumkin, shuning uchun limit va komissiyalarni aniq tushuntiramiz.", "Бу шартли тўлов мажбурияти. Кредит линиянгизни банд қилиши мумкин, шунинг учун лимит ва комиссияларни аниқ тушунтирамиз.", "Это условное платёжное обязательство. Оно может заморозить кредитную линию, поэтому ясно объясним лимиты и комиссии.", "It’s a payment undertaking with conditions. It can also tie up your credit line, so we’ll explain limits and fees clearly."),
            ],
        },
    ],
    "eb-guarantees": [
        {
            "match": "Dialogue",
            "lines": [
                _line("Contractor", "Loyiha egasi performance guarantee so‘rayapti.", "Лойиҳа эгаси performance guarantee сўраяпти.", "Заказчик просит гарантию исполнения.", "The project owner asks for a performance guarantee."),
                _line("Officer", "Ko‘rib chiqamiz. Shartnoma va kompaniya limitlari kerak. Kafolat bank va siz uchun jiddiy shartli majburiyat.", "Кўриб чиқамиз. Шартнома ва компания лимитлари керак. Кафолат банк ва сиз учун жиддий шартли мажбурият.", "Можем рассмотреть. Нужны контракт и лимиты компании. Гарантия — серьёзное условное обязательство для банка и для вас.", "We can review that. We’ll need the contract and your company limits. A guarantee is a serious contingent liability for the bank and for you."),
                _line("Contractor", "Contingent?", "Contingent?", "Условное?", "Contingent?"),
                _line("Officer", "Agar kafolat shartlari bo‘yicha haqiqiy da’vo bo‘lsa, u haqiqiy to‘lovga aylanadi.", "Агар кафолат шартлари бўйича ҳақиқий даъво бўлса, у ҳақиқий тўловга айланади.", "Она становится реальным платежом, если по условиям гарантии предъявлено обоснованное требование.", "It becomes a real payment if a valid claim is made under the guarantee terms."),
            ],
        },
    ],
    "eb-digital-channels": [
        {
            "match": "First app login",
            "lines": [
                _line("Customer", "Ilovaga kira olmayapman.", "Иловага кира олмаяпман.", "Не могу войти в приложение.", "I can’t log in to the app."),
                _line("Officer", "Afsusman. Rasmiy do‘kondagi ilovani ishlatyapsizmi? SMS OTP uchun telefon raqamingizni tekshiramiz… Xavfsizlik uchun OTP ni so‘ramayman. Uni faqat ilovaga kiriting.", "Афсусман. Расмий дўкондаги иловани ишлатяпсизми? SMS OTP учун телефон рақамингизни текширамиз… Хавфсизлик учун OTP ни сўрамайман. Уни фақат иловага киритинг.", "Сожалею. Вы используете официальное приложение из магазина? Проверим номер для SMS OTP… Из соображений безопасности я не попрошу сам OTP. Введите его только в приложении.", "I’m sorry about that. Are you using the official app from the store? Let’s check your phone number for SMS OTP… For security, I won’t ask for the OTP itself. Enter it only in the app."),
            ],
        },
    ],
    "eb-phishing": [
        {
            "match": "Warning call",
            "lines": [
                _line("Customer", "Kimdir qo‘ng‘iroq qilib, bankdan ekanini aytdi. OTP so‘rayapti.", "Кимдир қўнғироқ қилиб, банкдан эканини айтди. OTP сўраяпти.", "Кто-то позвонил и сказал, что из банка. Просят OTP.", "Someone called and said they’re from the bank. They want my OTP."),
                _line("Officer", "Tekshirganingiz uchun rahmat. Quvuring. Biz hech qachon qo‘ng‘iroqda OTP so‘ramaymiz. Kerak bo‘lsa, so‘nggi operatsiyalarni ko‘rib chiqamiz va kirishni yangilaymiz.", "Текширганингиз учун раҳмат. Қувуринг. Биз ҳеч қачон қўнғироқда OTP сўрамаймиз. Керак бўлса, сўнгги операцияларни кўриб чиқамиз ва киришни янгилаймиз.", "Спасибо, что проверили. Положите трубку. Мы никогда не просим OTP по телефону. При необходимости проверим операции и сбросим доступ.", "Thank you for checking. Please hang up. We never ask for OTP on a call. I’ll help you review recent transactions and reset access if needed."),
            ],
        },
    ],
    "eb-fraud-cases": [
        {
            "match": "Suspected scam",
            "lines": [
                _line("Customer", "Telefonimda odam gaplashyapti. Hozir o‘tkazma qilishim kerak, deydi.", "Телефонимда одам гаплашяпти. Ҳозир ўтказма қилишим керак, дейди.", "Я на линии с человеком. Он говорит, что нужно перевести сейчас.", "I’m on the phone with a man. He says I must transfer now."),
                _line("Officer", "O‘tkazmani to‘xtating. Qo‘ng‘iroqni kutishga qo‘ying — yoki quvuring. Biz rasmiy tartibda qayta qo‘ng‘iroq qilamiz. Agar bu firibgarlik bo‘lsa, shoshilish ularga yordam beradi, sizga emas.", "Ўтказмани тўхтатинг. Қўнғироқни кутишга қўйинг — ёки қувуринг. Биз расмий тартибда қайта қўнғироқ қиламиз. Агар бу фирибгарлик бўлса, шошилиш уларга ёрдам беради, сизга эмас.", "Приостановите перевод. Попросите подождать — или положите трубку. Мы перезвоним по официальной процедуре. Если это мошенничество, спешка помогает им, не вам.", "Please pause the transfer. Ask the caller to hold — or hang up. We’ll call you back on the official process. If this is a scam, speed helps them, not you."),
            ],
        },
    ],
}


def pick(pack: dict, lang: str) -> str:
    return pack.get(lang) or pack.get(LANG_UZ) or ""
