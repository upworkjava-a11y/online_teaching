"""UI and content string maps. msgid = original Uzbek (Latin)."""

from __future__ import annotations

import re


def S(cyrl: str, ru: str, en: str) -> dict[str, str]:
    return {"uz-cyrl": cyrl, "ru": ru, "en": en}


# Exact-match strings (chrome, buttons, short labels, course titles).
STRINGS: dict[str, dict[str, str]] = {
    # Brand / guest
    "Data analitikani biz bilan o‘rganing": S(
        "Дата аналитикани биз билан ўрганинг",
        "Изучайте data analytics с нами",
        "Learn data analytics with us",
    ),
    "Code with me o‘quv platformasi": S(
        "Code with me ўқув платформаси",
        "Обучающая платформа Code with me",
        "Code with me learning platform",
    ),
    "Kanalga o‘tish": S("Каналга ўтиш", "Перейти в канал", "Open channel"),
    "Mehmon": S("Меҳмон", "Гость", "Guest"),
    "Ro‘yxatsiz ko‘rish mumkin": S(
        "Рўйхатсиз кўриш мумкин",
        "Можно смотреть без регистрации",
        "Browse without signing in",
    ),
    "Bilim sari birinchi qadam — bugun boshlang": S(
        "Билим сари биринчи қадам — бугун бошланг",
        "Первый шаг к знаниям — начните сегодня",
        "Your first step to knowledge — start today",
    ),
    "Mashq, test yoki uy vazifasini boshlashda kirish so‘raladi.": S(
        "Машқ, тест ёки уй вазифасини бошлашда кириш сўралади.",
        "Чтобы начать упражнение, тест или домашнее задание, войдите в аккаунт.",
        "Sign in to start an exercise, test, or homework.",
    ),
    # Nav
    "Mening panelim": S("Менинг панелим", "Моя панель", "My dashboard"),
    "Kurslarim": S("Курсларим", "Мои курсы", "My courses"),
    "Kurslar": S("Курслар", "Курсы", "Courses"),
    "Amaliyot": S("Амалиёт", "Практика", "Practice"),
    "Musobaqalar": S("Мусобақалар", "Соревнования", "Contests"),
    "Progressim": S("Прогрессим", "Мой прогресс", "My progress"),
    "Reyting": S("Рейтинг", "Рейтинг", "Leaderboard"),
    "Sertifikatlar": S("Сертификатлар", "Сертификаты", "Certificates"),
    "Uy vazifasi": S("Уй вазифаси", "Домашнее задание", "Homework"),
    "Profil": S("Профил", "Профиль", "Profile"),
    "Chiqish": S("Чиқиш", "Выйти", "Log out"),
    "Kirish": S("Кириш", "Войти", "Sign in"),
    "Ro‘yxatdan o‘tish": S("Рўйхатдан ўтиш", "Регистрация", "Sign up"),
    "Natijalar paneli": S("Натижалар панели", "Панель результатов", "Results dashboard"),
    "Bilim testi": S("Билим тести", "Проверка знаний", "Skill test"),
    "Progress dashboard": S("Progress dashboard", "Дашборд прогресса", "Progress dashboard"),
    "Talabalar": S("Талабалар", "Студенты", "Students"),
    "Admin": S("Admin", "Админ", "Admin"),
    # Auth
    "Tizimga kirish": S("Тизимга кириш", "Вход", "Sign in"),
    "Email va parol bilan kiring.": S(
        "Email ва парол билан киринг.",
        "Войдите с email и паролем.",
        "Sign in with email and password.",
    ),
    "This password is too common.": S(
        "Бу парол жуда оддий (кўп ишлатилади).",
        "Этот пароль слишком простой (часто используется).",
        "This password is too common.",
    ),
    "This password is too short. It must contain at least 10 characters.": S(
        "Парол жуда қисқа. Камида 10 белги бўлиши керак.",
        "Пароль слишком короткий. Минимум 10 символов.",
        "This password is too short. It must contain at least 10 characters.",
    ),
    "This password is entirely numeric.": S(
        "Парол фақат рақамлардан иборат бўлмаслиги керак.",
        "Пароль не должен состоять только из цифр.",
        "This password is entirely numeric.",
    ),
    "This field is required.": S(
        "Bu maydon majburiy.",
        "Обязательное поле.",
        "This field is required.",
    ),
    "To‘g‘ri!": S("Тўғри!", "Верно!", "Correct!"),
    "Noto‘g‘ri.": S("Нотўғри.", "Неверно.", "Incorrect."),
    "Noto‘g‘ri javob. Qayta urinib ko‘ring.": S(
        "Нотўғри жавоб. Қайта уриниб кўринг.",
        "Неверный ответ. Попробуйте ещё раз.",
        "Incorrect answer. Try again.",
    ),
    "Hisobingiz yo‘qmi?": S("Ҳисобингиз йўқми?", "Нет аккаунта?", "No account?"),
    "Ro‘yxatdan o‘ting": S("Рўйхатдан ўтинг", "Зарегистрируйтесь", "Sign up"),
    "Allaqachon hisobingiz bormi?": S(
        "Аллақачон ҳисобингиз борми?",
        "Уже есть аккаунт?",
        "Already have an account?",
    ),
    "← Kurslarni ko‘rish": S("← Курсларни кўриш", "← К курсам", "← Browse courses"),
    "Kirish kerak": S("Кириш керак", "Нужен вход", "Sign in required"),
    "Progressingiz saqlanadi": S(
        "Прогрессингиз сақланади",
        "Ваш прогресс сохранится",
        "Your progress is saved",
    ),
    "Reyting va sertifikatlarga chiqasiz": S(
        "Рейтинг ва сертификатларга чиқасиз",
        "Попадёте в рейтинг и получите сертификаты",
        "You can reach the leaderboard and certificates",
    ),
    "Uy vazifasi va testlarni topshirasiz": S(
        "Уй вазифаси ва тестларни топширасиз",
        "Сдаёте домашку и тесты",
        "You can submit homework and tests",
    ),
    "← Kurslarni ko‘rishda davom etish": S(
        "← Курсларни кўришда давом этиш",
        "← Продолжить просмотр курсов",
        "← Keep browsing courses",
    ),
    "Ism": S("Исм", "Имя", "First name"),
    "Familiya": S("Фамилия", "Фамилия", "Last name"),
    "Parol": S("Парол", "Пароль", "Password"),
    "Parolni tasdiqlang": S("Паролни тасдиқланг", "Подтвердите пароль", "Confirm password"),
    "Email": S("Email", "Email", "Email"),
    "Foydalanuvchi nomi": S("Фойдаланувчи номи", "Имя пользователя", "Username"),
    "Joriy parol": S("Жорий парол", "Текущий пароль", "Current password"),
    "Yangi parol": S("Янги парол", "Новый пароль", "New password"),
    "Yangi parolni tasdiqlang": S("Янги паролни тасдиқланг", "Подтвердите новый пароль", "Confirm new password"),
    "Talaba": S("Талаба", "Студент", "Student"),
    "O‘qituvchi": S("Ўқитувчи", "Преподаватель", "Teacher"),
    "Administrator": S("Администратор", "Администратор", "Administrator"),
    # Courses
    "Mening kurslarim": S("Менинг курсларим", "Мои курсы", "My courses"),
    "Hozircha SQL ochiq. Boshqa kurslar — Hozir jarayonda.": S(
        "Ҳозирча SQL очиқ. Бошқа курслар — Ҳозир жараёнда.",
        "Сейчас открыт SQL. Остальные курсы — в разработке.",
        "SQL is open for now. Other courses are coming soon.",
    ),
    "Hozir jarayonda": S("Ҳозир жараёнда", "В разработке", "Coming soon"),
    "🔒 Hozir jarayonda": S("🔒 Ҳозир жараёнда", "🔒 В разработке", "🔒 Coming soon"),
    "Progress:": S("Прогресс:", "Прогресс:", "Progress:"),
    "To‘liq kurs ochiq": S("Тўлиқ курс очиқ", "Курс полностью открыт", "Full course unlocked"),
    "Dastlabki 5 modul ochiq · qolgani 🔒": S(
        "Дастлабки 5 модул очиқ · қолгани 🔒",
        "Первые 5 модулей открыты · остальные 🔒",
        "First 5 modules open · rest 🔒",
    ),
    "Kursni ochish": S("Курсни очиш", "Открыть курс", "Open course"),
    "Bu bo‘lim siz uchun hozircha yopilgan.": S(
        "Бу бўлим сиз учун ҳозирча ёпилган.",
        "Этот раздел для вас пока закрыт.",
        "This section is closed for you right now.",
    ),
    "Bu kurs hozircha yashirin.": S(
        "Бу курс ҳозирча яширин.",
        "Этот курс пока скрыт.",
        "This course is hidden for now.",
    ),
    "Kurs": S("Курс", "Курс", "Course"),
    "Umumiy progress:": S("Умумий прогресс:", "Общий прогресс:", "Overall progress:"),
    "Dastlabki 5 modul ochiq. Qolganlari 🔒 Premium.": S(
        "Дастлабки 5 модул очиқ. Қолганлари 🔒 Premium.",
        "Первые 5 модулей открыты. Остальные 🔒 Premium.",
        "First 5 modules are open. The rest are 🔒 Premium.",
    ),
    "Dastlabki 5 modul mashqlari ochiq. Qolganlari 🔒 Premium.": S(
        "Дастлабки 5 модул машқлари очиқ. Қолганлари 🔒 Premium.",
        "Задачи первых 5 модулей открыты. Остальные 🔒 Premium.",
        "Tasks from the first 5 modules are open. The rest are 🔒 Premium.",
    ),
    "Premium ochish — narx va to‘lov →": S(
        "Premium очиш — нарх ва тўлов →",
        "Открыть Premium — цена и оплата →",
        "Unlock Premium — price and payment →",
    ),
    "Yopiq": S("Ёпиқ", "Закрыто", "Closed"),
    "Yashirin": S("Яширин", "Скрыто", "Hidden"),
    "Bu modul Premium. To‘liq ochish uchun narx va to‘lov yo‘riqnomasini ko‘ring.": S(
        "Бу модул Premium. Тўлиқ очиш учун нарх ва тўлов йўриқномасини кўринг.",
        "Этот модуль Premium. Смотрите цену и инструкцию по оплате.",
        "This module is Premium. See the price and payment guide.",
    ),
    "Narx va to‘lov": S("Нарх ва тўлов", "Цена и оплата", "Price and payment"),
    "Premium ochish": S("Premium очиш", "Открыть Premium", "Unlock Premium"),
    "Yopiq bo‘lim": S("Ёпиқ бўлим", "Закрытый раздел", "Closed section"),
    "Kirish cheklangan": S("Кириш чекланган", "Доступ ограничен", "Access limited"),
    "Kurslarga qaytish": S("Курсларга қайтиш", "К курсам", "Back to courses"),
    # Practice / exercises
    "Amaliyot — mashqlar": S("Амалиёт — машқлар", "Практика — задачи", "Practice — exercises"),
    "Mashqlar katalogi": S("Машқлар каталоги", "Каталог задач", "Exercise catalog"),
    "SQL mashqlari — oson, o‘rta va qiyin.": S(
        "SQL машқлари — осон, ўрта ва қийин.",
        "Задачи SQL — лёгкие, средние и сложные.",
        "SQL exercises — easy, medium, and hard.",
    ),
    "SQL va English for Banking mashqlari — oson, o‘rta va qiyin.": S(
        "SQL ва English for Banking машқлари — осон, ўрта ва қийин.",
        "Задачи SQL и English for Banking — лёгкие, средние и сложные.",
        "SQL and English for Banking exercises — easy, medium, and hard.",
    ),
    "Qidiruv": S("Қидирув", "Поиск", "Search"),
    "Qiyinlik": S("Қийинлик", "Сложность", "Difficulty"),
    "Holat": S("Ҳолат", "Статус", "Status"),
    "Barchasi": S("Барчаси", "Все", "All"),
    "Oson": S("Осон", "Лёгкий", "Easy"),
    "O‘rta": S("Ўрта", "Средний", "Medium"),
    "Qiyin": S("Қийин", "Сложный", "Hard"),
    "Yechilmagan": S("Ечилмаган", "Не решено", "Unsolved"),
    "Yechilgan": S("Ечилган", "Решено", "Solved"),
    "Masala nomi...": S("Масала номи...", "Название задачи...", "Exercise name..."),
    "Topshiriq": S("Топшириқ", "Задание", "Task"),
    "Mavjud jadvallar": S("Мавжуд жадваллар", "Доступные таблицы", "Available tables"),
    "Maslahat": S("Маслаҳат", "Подсказка", "Hint"),
    "Darsga qaytish": S("Дарсга қайтиш", "К уроку", "Back to lesson"),
    "Amaliyot katalogi": S("Амалиёт каталоги", "Каталог практики", "Practice catalog"),
    "Modul bilim testi": S("Модул билим тести", "Тест модуля", "Module skill test"),
    "Javobni tanlang:": S("Жавобни танланг:", "Выберите ответ:", "Choose an answer:"),
    "Javob (A/B/C/D)": S("Жавоб (A/B/C/D)", "Ответ (A/B/C/D)", "Answer (A/B/C/D)"),
    "Test": S("Тест", "Тест", "Quiz"),
    "Tavsiya etilgan mashqlar": S(
        "Тавсия этилган машқлар",
        "Рекомендуемые задачи",
        "Recommended exercises",
    ),
    "Darsdan keyin Easy → Medium → Hard tartibida yeching.": S(
        "Дарсдан кейин Easy → Medium → Hard тартибида ечинг.",
        "После урока решайте в порядке Easy → Medium → Hard.",
        "After the lesson, solve Easy → Medium → Hard.",
    ),
    "Amaliy test": S("Амалий тест", "Практический тест", "Practice quiz"),
    "SQL amaliyot": S("SQL амалиёт", "Практика SQL", "SQL practice"),
    "Dars mavzusi bo‘yicha test savoli. Javob vebda tekshiriladi.": S(
        "Дарс мавзуси бўйича тест саволи. Жавоб вебда текширилади.",
        "Тест по теме урока. Ответ проверяется на сайте.",
        "A quiz on this lesson. The answer is checked on the site.",
    ),
    "Dars mavzusi bo‘yicha SQL yozing. Natija to‘plami tekshiriladi.": S(
        "Дарс мавзуси бўйича SQL ёзинг. Натижа тўплами текширилади.",
        "Напишите SQL по теме урока. Набор строк будет проверен.",
        "Write SQL for this lesson. The result set is checked.",
    ),
    "Testni yechish": S("Тестни ечиш", "Решить тест", "Take the quiz"),
    "Kod yozish": S("Код ёзиш", "Писать код", "Write code"),
    "Uy vazifasi yuborish": S("Уй вазифаси юбориш", "Отправить домашку", "Submit homework"),
    "Oldingi dars": S("Олдинги дарс", "Предыдущий урок", "Previous lesson"),
    "Keyingi dars": S("Кейинги дарс", "Следующий урок", "Next lesson"),
    "Darsni tugalladim": S("Дарсни тугалладим", "Урок пройден", "I finished this lesson"),
    "Dars o‘qildi — amaliyot hali yechilmagan": S(
        "Дарс ўқилди — амалиёт ҳали ечилмаган",
        "Урок прочитан — практика ещё не решена",
        "Lesson read — practice not solved yet",
    ),
    "Bu dars tugallangan": S("Бу дарс тугалланган", "Этот урок завершён", "This lesson is complete"),
    "Darsni saqlash uchun kiring": S(
        "Дарсни сақлаш учун киринг",
        "Войдите, чтобы сохранить урок",
        "Sign in to save the lesson",
    ),
    "🔒 Keyingi modul — Premium ochish": S(
        "🔒 Кейинги модул — Premium очиш",
        "🔒 Следующий модуль — открыть Premium",
        "🔒 Next module — unlock Premium",
    ),
    "Maslahat — yo‘nalish, yechim emas. Avval o‘zingiz urinib ko‘ring.": S(
        "Маслаҳат — йўналиш, ечим эмас. Аввал ўзингиз уриниб кўринг.",
        "Подсказка — направление, не решение. Сначала попробуйте сами.",
        "Hints are direction, not the solution. Try it yourself first.",
    ),
    # Contests / other
    "Haftalik musobaqalar": S("Ҳафталик мусобақалар", "Еженедельные соревнования", "Weekly contests"),
    "so‘m": S("сўм", "сум", "so'm"),
    "Premium": S("Premium", "Premium", "Premium"),
    "Modul": S("Модул", "Модуль", "Module"),
    "Dars": S("Дарс", "Урок", "Lesson"),
    "Mashq": S("Машқ", "Задача", "Exercise"),
    "Til": S("Тил", "Язык", "Language"),
    # Course titles (keep SQL/Excel/Python/Power BI)
    "Statistika": S("Статистика", "Статистика", "Statistics"),
    "Amaliy loyihalar": S("Амалий лойиҳалар", "Практические проекты", "Real projects"),
    # SQL modules
    "SQL asoslari": S("SQL асослари", "Основы SQL", "SQL basics"),
    "Filtrlash va saralash": S("Филтрлаш ва саралаш", "Фильтрация и сортировка", "Filtering and sorting"),
    "Agregatsiyalar": S("Агрегатсиялар", "Агрегации", "Aggregations"),
    "GROUP BY va HAVING": S("GROUP BY ва HAVING", "GROUP BY и HAVING", "GROUP BY and HAVING"),
    "JOINlar": S("JOINлар", "JOIN-ы", "JOINs"),
    "Subquerylar": S("Subqueryлар", "Подзапросы", "Subqueries"),
    "CTElar": S("CTEлар", "CTE", "CTEs"),
    "CASE": S("CASE", "CASE", "CASE"),
    "Sana va vaqt": S("Сана ва вақт", "Дата и время", "Date and time"),
    "Window funksiyalar": S("Window функциялар", "Оконные функции", "Window functions"),
    "Murakkab SQL": S("Муракаб SQL", "Продвинутый SQL", "Advanced SQL"),
    # Auth gates / messages
    "Davom etish uchun hisob kerak": S(
        "Давом этиш учун ҳисоб керак",
        "Чтобы продолжить, нужен аккаунт",
        "You need an account to continue",
    ),
    "Mashq, test yoki uy vazifasini bajarish uchun tizimga kiring yoki ro‘yxatdan o‘ting.": S(
        "Машқ, тест ёки уй вазифасини бажариш учун тизимга киринг ёки рўйхатдан ўтинг.",
        "Чтобы решать задачи, тесты или домашку, войдите или зарегистрируйтесь.",
        "Sign in or register to complete exercises, tests, or homework.",
    ),
    "Masalani yechish uchun hisob kerak": S(
        "Масалани ечиш учун ҳисоб керак",
        "Чтобы решать задачу, нужен аккаунт",
        "You need an account to solve this",
    ),
    "SQL mashqlari va testlarni yechish, natijani saqlash uchun tizimga kiring yoki ro‘yxatdan o‘ting.": S(
        "SQL машқлари ва тестларни ечиш, натижани сақлаш учун тизимга киринг ёки рўйхатдан ўтинг.",
        "Чтобы решать SQL-задачи и тесты и сохранять результат, войдите или зарегистрируйтесь.",
        "Sign in or register to solve SQL exercises and quizzes and save results.",
    ),
    "Bilim testi uchun hisob kerak": S(
        "Билим тести учун ҳисоб керак",
        "Для теста знаний нужен аккаунт",
        "You need an account for the skill test",
    ),
    "Modul bilim testini boshlash va natijani ko‘rish uchun tizimga kiring yoki ro‘yxatdan o‘ting.": S(
        "Модул билим тестини бошлаш ва натижани кўриш учун тизимга киринг ёки рўйхатдан ўтинг.",
        "Чтобы начать тест модуля и увидеть результат, войдите или зарегистрируйтесь.",
        "Sign in or register to start the module skill test and see results.",
    ),
    "Kabinet uchun hisob kerak": S(
        "Кабинет учун ҳисоб керак",
        "Для кабинета нужен аккаунт",
        "You need an account for the dashboard",
    ),
    "Uy vazifasi uchun hisob kerak": S(
        "Уй вазифаси учун ҳисоб керак",
        "Для домашнего задания нужен аккаунт",
        "You need an account for homework",
    ),
    "Sertifikatlar uchun hisob kerak": S(
        "Сертификатлар учун ҳисоб керак",
        "Для сертификатов нужен аккаунт",
        "You need an account for certificates",
    ),
    "Darsni belgilash uchun hisob kerak": S(
        "Дарсни белгилаш учун ҳисоб керак",
        "Чтобы отметить урок, нужен аккаунт",
        "You need an account to mark the lesson",
    ),
    "Darsni tugallangan deb belgilash, progress saqlash uchun tizimga kiring yoki ro‘yxatdan o‘ting.": S(
        "Дарсни тугалланган деб белгилаш, прогресс сақлаш учун тизимга киринг ёки рўйхатдан ўтинг.",
        "Чтобы отметить урок пройденным и сохранить прогресс, войдите или зарегистрируйтесь.",
        "Sign in or register to mark the lesson complete and save progress.",
    ),
    "Bu modul premium. To‘liq ochish uchun shu kursga to‘lov qiling.": S(
        "Бу модул premium. Тўлиқ очиш учун шу курсга тўлов қилинг.",
        "Этот модуль premium. Оплатите курс, чтобы открыть его полностью.",
        "This module is premium. Pay for this course to unlock it.",
    ),
    "Hozir jarayonda": S("Ҳозир жараёнда", "В разработке", "Coming soon"),
    "Bu kurs hozircha mavjud emas.": S(
        "Бу курс ҳозирча мавжуд эмас.",
        "Этого курса пока нет.",
        "This course is not available yet.",
    ),
    "Hisobingiz bloklangan. Administrator bilan bog‘laning.": S(
        "Ҳисобингиз блокланган. Администратор билан боғланинг.",
        "Ваш аккаунт заблокирован. Свяжитесь с администратором.",
        "Your account is blocked. Contact an administrator.",
    ),
    "Email yoki parol noto‘g‘ri.": S(
        "Email ёки парол нотўғри.",
        "Неверный email или пароль.",
        "Incorrect email or password.",
    ),
    "Bu email allaqachon ro‘yxatdan o‘tgan.": S(
        "Бу email аллақачон рўйхатдан ўтган.",
        "Этот email уже зарегистрирован.",
        "This email is already registered.",
    ),
    "Hisob yaratish": S("Ҳисоб яратиш", "Создать аккаунт", "Create account"),
    "Email va parol bilan hisob yarating.": S(
        "Email ва парол билан ҳисоб яратинг.",
        "Создайте аккаунт с email и паролем.",
        "Create an account with email and password.",
    ),
    "Nima uchun Premium?": S("Нима учун Premium?", "Почему Premium?", "Why Premium?"),
    "To‘lov yo‘riqnomasi": S("Тўлов йўриқномаси", "Инструкция по оплате", "Payment guide"),
    "To‘liq kurs, barcha modullar va mentor yordami — bir marta to‘lov qilib, o‘qishni to‘xtovsiz davom ettiring.": S(
        "Тўлиқ курс, барча модуллар ва ментор ёрдами — бир марта тўлов қилиб, ўқишни тўхтовсиз давом эттиринг.",
        "Полный курс, все модули и помощь ментора — один платёж, и учёба без остановок.",
        "Full course, all modules, and mentor help — pay once and keep learning without interruption.",
    ),
    "Sizda bu kurs uchun to‘liq ruxsat bor.": S(
        "Сизда бу курс учун тўлиқ рухсат бор.",
        "У вас уже полный доступ к этому курсу.",
        "You already have full access to this course.",
    ),
    "Kursga qaytish": S("Курсга қайтиш", "Вернуться к курсу", "Back to course"),
    "← Kursga qaytish": S("← Курсга қайтиш", "← Вернуться к курсу", "← Back to course"),
    "to‘liq Premium": S("тўлиқ Premium", "полный Premium", "full Premium"),
    "Barcha yopiq modullar va bilim testlari ochiladi": S(
        "Барча ёпиқ модуллар ва билим тестлари очилади",
        "Открываются все закрытые модули и тесты знаний",
        "All locked modules and skill tests unlock",
    ),
    "Uy vazifalari tekshirib boriladi": S(
        "Уй вазифалари текшириб борилади",
        "Домашние задания проверяются",
        "Homework is reviewed",
    ),
    "o‘qituvchi baho va izoh beradi": S(
        "ўқитувчи баҳо ва изоҳ беради",
        "преподаватель ставит оценку и комментарий",
        "the teacher gives a grade and feedback",
    ),
    "Qo‘shimcha mentor izohlari": S(
        "Қўшимча ментор изоҳлари",
        "Дополнительные комментарии ментора",
        "Extra mentor notes",
    ),
    "xatolarni tuzatish va keyingi qadamlar bo‘yicha yo‘l-yo‘riq": S(
        "хатоларни тузатиш ва кейинги қадамлар бўйича йўл-йўриқ",
        "исправление ошибок и подсказки по следующим шагам",
        "fixing mistakes and guidance on next steps",
    ),
    "Amaliyot, musobaqa va sertifikat yo‘liga to‘liq kirish": S(
        "Амалиёт, мусобақа ва сертификат йўлига тўлиқ кириш",
        "Полный доступ к практике, соревнованиям и пути к сертификату",
        "Full access to practice, contests, and the certificate path",
    ),
    "Quyidagi kartaga summani o‘tkazing:": S(
        "Қуйидаги картага суммани ўтказинг:",
        "Переведите на карту ниже сумму:",
        "Transfer this amount to the card below:",
    ),
    "To‘lov cheki (screenshot) ni Telegram orqali yuboring.": S(
        "Тўлов чеки (screenshot) ни Telegram орқали юборинг.",
        "Отправьте чек оплаты (screenshot) в Telegram.",
        "Send the payment receipt (screenshot) via Telegram.",
    ),
    "Ism-familiyangiz va qaysi kurs uchun to‘laganingizni yozing — faqat shu kurs ochiladi.": S(
        "Исм-фамилиянгиз ва қайси курс учун тўлаганингизни ёзинг — фақат шу курс очилади.",
        "Напишите ФИО и за какой курс оплатили — откроется только этот курс.",
        "Write your full name and which course you paid for — only that course will unlock.",
    ),
    "Karta raqami": S("Карта рақами", "Номер карты", "Card number"),
    "Raqamni nusxalash": S("Рақамни нусхалаш", "Скопировать номер", "Copy number"),
    "Nusxa olindi ✓": S("Нусха олинди ✓", "Скопировано ✓", "Copied ✓"),
    "Chek screenshotini yuboring": S(
        "Чек screenshotини юборинг",
        "Отправьте screenshot чека",
        "Send the receipt screenshot",
    ),
    "Invoice / chek rasmini shu akkauntga yuboring — Premium tez ochiladi.": S(
        "Invoice / чек расмини шу аккаунтга юборинг — Premium тез очилади.",
        "Отправьте фото чека на этот аккаунт — Premium откроется быстро.",
        "Send the receipt photo to this account — Premium unlocks quickly.",
    ),
    "Chek yuborish": S("Чек юбориш", "Отправить чек", "Send receipt"),
    "Sana va vaqt funksiyalari": S(
        "Сана ва вақт функциялари",
        "Функции даты и времени",
        "Date and time functions",
    ),
    "CTElar": S("CTEлар", "CTE", "CTEs"),
    "Ilg‘or SQL": S("Илғор SQL", "Продвинутый SQL", "Advanced SQL"),
    "Murakkab SQL": S("Муракаб SQL", "Продвинутый SQL", "Advanced SQL"),
}

# Course descriptions (full original strings from content files).
STRINGS.update(
    {
        (
            "Ma’lumotlar tahlili uchun SQL: noldan, o‘qituvchi bilan gaplashgandek. "
            "Bank mijozlari va tranzaksiyalar jadvalida SELECT, WHERE, JOIN, GROUP BY, CTE va window funksiyalarini "
            "qadamma-qadam o‘rganasiz. Har darsdan keyin mashq bor."
        ): S(
            "Маълумотлар таҳлили учун SQL: нолдан, ўқитувчи билан гаплашгандек. "
            "Банк мижозлари ва транзаксиялар жадвалида SELECT, WHERE, JOIN, GROUP BY, CTE ва window функцияларини "
            "қадамма-қадам ўрганасиз. Ҳар дарсдан кейин машқ бор.",
            "SQL для анализа данных: с нуля, как разговор с преподавателем. "
            "На таблицах клиентов банка и транзакций вы шаг за шагом изучаете SELECT, WHERE, JOIN, GROUP BY, CTE и оконные функции. "
            "После каждого урока есть практика.",
            "SQL for data analysis: from scratch, like talking with a teacher. "
            "On bank customer and transaction tables you learn SELECT, WHERE, JOIN, GROUP BY, CTE and window functions step by step. "
            "Every lesson has practice.",
        ),
        (
            "Excelni noldan, o‘qituvchi bilan gaplashgandek: katak, tur, Table, formulalar, "
            "XLOOKUP, Pivot va Power Query. Toshkent savdosi va bank fayllari misolida — "
            "hisobot chiqarishgacha. Har darsdan keyin mashq bor."
        ): S(
            "Excelни нолдан, ўқитувчи билан гаплашгандек: катак, тур, Table, формулалар, "
            "XLOOKUP, Pivot ва Power Query. Тошкент савдоси ва банк файллари мисолида — "
            "ҳисобот чиқаришгача. Ҳар дарсдан кейин машқ бор.",
            "Excel с нуля, как разговор с преподавателем: ячейка, типы, Table, формулы, "
            "XLOOKUP, Pivot и Power Query. На примерах продаж Ташкента и банковских файлов — "
            "до готового отчёта. После каждого урока есть практика.",
            "Excel from scratch, like talking with a teacher: cells, types, Table, formulas, "
            "XLOOKUP, Pivot and Power Query. Using Tashkent sales and bank files — through to a report. "
            "Every lesson has practice.",
        ),
        (
            "Statistika — formula yodlash emas: o‘rtacha yolg‘on gapirganda nima qilish, "
            "A/B ni rahbarga qanday aytish, p-value ni qo‘rqitmasdan tushunish. "
            "Do‘kon, bank va landing misollari bilan, o‘zbekcha."
        ): S(
            "Статистика — формула ёдлаш эмас: ўртача ёлғон гапирганда нима қилиш, "
            "A/B ни раҳбарга қандай айтиш, p-value ни қўрқитмасдан тушуниш. "
            "Дўкон, банк ва landing мисоллари билан.",
            "Статистика — не заучивание формул: что делать, когда среднее врёт, "
            "как объяснить A/B руководителю, как понять p-value без страха. "
            "На примерах магазина, банка и лендинга.",
            "Statistics is not memorizing formulas: what to do when the average lies, "
            "how to explain A/B to a manager, how to understand p-value without fear. "
            "With shop, bank, and landing-page examples.",
        ),
        (
            "Python data analytics — boshlang‘ichdan o‘rtagacha: o‘zgaruvchi, mantiq, NumPy, Pandas, "
            "tozalash, groupby/merge, EDA va mini-loyiha. Har darsda mashq + puzzle, modul oxirida bilim testi "
            "(W3Schools/CodeChef ruhida, lekin tahlilchiga mos)."
        ): S(
            "Python data analytics — бошланғичдан ўртагача: ўзгарувчи, мантиқ, NumPy, Pandas, "
            "тозалаш, groupby/merge, EDA ва мини-лойиҳа. Ҳар дарсда машқ + puzzle, модул охирида билим тести.",
            "Python для data analytics — с начального до среднего: переменные, логика, NumPy, Pandas, "
            "очистка, groupby/merge, EDA и мини-проект. На каждом уроке практика и puzzle, в конце модуля — тест.",
            "Python for data analytics — beginner to intermediate: variables, logic, NumPy, Pandas, "
            "cleaning, groupby/merge, EDA and a mini-project. Practice + puzzle each lesson, skill test at module end.",
        ),
        (
            "Power BI ni noldan: Get Data, Power Query, model, DAX, vizual, Service. "
            "Exceldan kelgan tahlilchi uchun — qayerni bosish va nima uchun, "
            "filial va savdo misollari bilan."
        ): S(
            "Power BI ни нолдан: Get Data, Power Query, model, DAX, визуал, Service. "
            "Excelдан келган таҳлилчи учун — қаерни босиш ва нима учун, "
            "филиал ва савдо мисоллари билан.",
            "Power BI с нуля: Get Data, Power Query, модель, DAX, визуалы, Service. "
            "Для аналитика из Excel — куда нажимать и зачем, "
            "на примерах филиалов и продаж.",
            "Power BI from scratch: Get Data, Power Query, model, DAX, visuals, Service. "
            "For an analyst coming from Excel — what to click and why, "
            "with branch and sales examples.",
        ),
        (
            "Yakuniy bosqich: bank, do‘kon, e-commerce, HR va marketingda haqiqiy brief. "
            "O‘qituvchi sizni junior tahlilchidek yo‘naltiradi — javobni o‘zingiz topasiz. "
            "SQL, Excel, Python, statistika va Power BI shu yerda qo‘shiladi."
        ): S(
            "Якуний босқич: банк, дўкон, e-commerce, HR ва маркетингда ҳақиқий brief. "
            "Ўқитувчи сизни junior таҳлилчидек йўналтиради — жавобни ўзингиз топасиз. "
            "SQL, Excel, Python, статистика ва Power BI шу ерда қўшилади.",
            "Финальный этап: реальный бриф в банке, магазине, e-commerce, HR и маркетинге. "
            "Преподаватель ведёт вас как junior-аналитика — ответ находите сами. "
            "Здесь сходятся SQL, Excel, Python, статистика и Power BI.",
            "Final stage: a real brief in banking, retail, e-commerce, HR and marketing. "
            "The teacher guides you like a junior analyst — you find the answer. "
            "SQL, Excel, Python, statistics and Power BI come together here.",
        ),
    }
)

STRINGS.update(
    {
        "Xush kelibsiz": S("Хуш келибсиз", "Добро пожаловать", "Welcome"),
        "Bugun darsni davom ettiring. Progressingiz saqlanadi.": S(
            "Бугун дарсни давом эттиринг. Прогрессингиз сақланади.",
            "Продолжите урок сегодня. Прогресс сохранится.",
            "Continue the lesson today. Your progress is saved.",
        ),
        "Davom etish": S("Давом этиш", "Продолжить", "Continue"),
        "Siz": S("Сиз", "Вы", "You"),
        "ball": S("балл", "баллов", "pts"),
        "Masala yechib reytingga chiqing": S(
            "Масала ечиб рейтингга чиқинг",
            "Решайте задачи и попадите в рейтинг",
            "Solve exercises to join the leaderboard",
        ),
        "Oson +1 · O‘rta +2 · Qiyin +3": S(
            "Осон +1 · Ўрта +2 · Қийин +3",
            "Лёгкий +1 · Средний +2 · Сложный +3",
            "Easy +1 · Medium +2 · Hard +3",
        ),
        "Reytingni ko‘rish": S("Рейтингни кўриш", "Смотреть рейтинг", "View leaderboard"),
        "Reytingni ochish": S("Рейтингни очиш", "Открыть рейтинг", "Open leaderboard"),
        "Kunlik zanjir": S("Кунлик занжир", "Дневная серия", "Daily streak"),
        "kun": S("кун", "дн.", "days"),
        "Har kuni kamida 1 masala yeching": S(
            "Ҳар куни камида 1 масала ечинг",
            "Решайте хотя бы 1 задачу каждый день",
            "Solve at least 1 exercise every day",
        ),
        "Oson / O‘rta / Qiyin filter": S(
            "Осон / Ўрта / Қийин фильтр",
            "Фильтр: лёгкий / средний / сложный",
            "Easy / Medium / Hard filter",
        ),
        "Haftalik musobaqa": S("Ҳафталик мусобақа", "Еженедельное соревнование", "Weekly contest"),
        "Alohida reyting bilan": S("Алоҳида рейтинг билан", "С отдельным рейтингом", "With a separate ranking"),
        "Ma’ruzalar:": S("Маърузалар:", "Лекции:", "Lectures:"),
        "Ma’ruzalar": S("Маърузалар", "Лекции", "Lectures"),
        "Mashqlar:": S("Машқлар:", "Задачи:", "Exercises:"),
        "Mashqlar": S("Машқлар", "Задачи", "Exercises"),
        "O‘rtacha ball:": S("Ўртача балл:", "Средний балл:", "Average score:"),
        "O‘rtacha ball": S("Ўртача балл", "Средний балл", "Average score"),
        "Hozircha ochiq kurs yo‘q.": S(
            "Ҳозирча очиқ курс йўқ.",
            "Пока нет открытых курсов.",
            "No open courses yet.",
        ),
        "So‘nggi faoliyat": S("Сўнгги фаолият", "Недавняя активность", "Recent activity"),
        "tugallandi": S("тугалланди", "завершено", "completed"),
        "ko‘rildi": S("кўрилди", "просмотрено", "viewed"),
        "to‘g‘ri": S("тўғри", "верно", "correct"),
        "noto‘g‘ri": S("нотўғри", "неверно", "incorrect"),
        "Hali faoliyat yo‘q.": S("Ҳали фаолият йўқ.", "Пока нет активности.", "No activity yet."),
        "Tekshirilgan": S("Текширилган", "Проверено", "Reviewed"),
        "Qayta topshirish kerak": S("Қайта топшириш керак", "Нужно сдать заново", "Needs revision"),
        "Ko‘rib chiqilmoqda": S("Кўриб чиқилмоқда", "На проверке", "Under review"),
        "Diqqat talab qiladigan uy vazifasi yo‘q.": S(
            "Диққат талаб қиладиган уй вазифаси йўқ.",
            "Нет домашки, требующей внимания.",
            "No homework that needs attention.",
        ),
        "Hozircha faqat SQL ochiq. Boshqa kurslar — Hozir jarayonda.": S(
            "Ҳозирча фақат SQL очиқ. Бошқа курслар — Ҳозир жараёнда.",
            "Сейчас открыт только SQL. Остальные курсы — в разработке.",
            "Only SQL is open for now. Other courses are coming soon.",
        ),
        "Hali modul yo‘q.": S("Ҳали модул йўқ.", "Пока нет модулей.", "No modules yet."),
        "Hozircha progress yo‘q.": S("Ҳозирча прогресс йўқ.", "Пока нет прогресса.", "No progress yet."),
        "Progress": S("Прогресс", "Прогресс", "Progress"),
        "Reyting jadvali": S("Рейтинг жадвали", "Таблица рейтинга", "Leaderboard"),
        "Ko‘proq masala yechganlar yuqorida. Ball:": S(
            "Кўпроқ масала ечганлар юқорида. Балл:",
            "Кто решил больше задач — выше. Баллы:",
            "Those who solved more sit higher. Points:",
        ),
        "Har bir mashq bir marta hisoblanadi.": S(
            "Ҳар бир машқ бир марта ҳисобланади.",
            "Каждая задача считается один раз.",
            "Each exercise counts once.",
        ),
        "Sizning o‘rningiz": S("Сизнинг ўрнингиз", "Ваше место", "Your place"),
        "Yechilgan:": S("Ечилган:", "Решено:", "Solved:"),
        "So‘nggi yechim:": S("Сўнгги ечим:", "Последнее решение:", "Last solve:"),
        "o‘rin": S("ўрин", "место", "place"),
        "masala": S("масала", "задача", "exercise"),
        "Hali hech kim masala yechmagan. Birinchilardan bo‘ling!": S(
            "Ҳали ҳеч ким масала ечмаган. Биринчилардан бўлинг!",
            "Пока никто не решил задачи. Будьте первыми!",
            "Nobody has solved an exercise yet. Be first!",
        ),
        "To‘liq jadval": S("Тўлиқ жадвал", "Полная таблица", "Full table"),
        "To‘liq jadval →": S("Тўлиқ жадвал →", "Полная таблица →", "Full table →"),
        "Ball": S("Балл", "Баллы", "Points"),
        "Masalalar": S("Масалалар", "Задачи", "Exercises"),
        "So‘nggi yechim": S("Сўнгги ечим", "Последнее решение", "Last solve"),
        "Reyting hali bo‘sh.": S("Рейтинг ҳали бўш.", "Рейтинг пока пуст.", "The leaderboard is empty."),
        "So‘nggi yechilgan masalalar": S(
            "Сўнгги ечилган масалалар",
            "Недавно решённые задачи",
            "Recently solved",
        ),
        "Hali yechimlar yo‘q.": S("Ҳали ечимлар йўқ.", "Пока нет решений.", "No solutions yet."),
        "So‘nggi:": S("Сўнгги:", "Последнее:", "Last:"),
        "Hozircha faqat SQL uy vazifasi ochiq. Boshqalar — Hozir jarayonda.": S(
            "Ҳозирча фақат SQL уй вазифаси очиқ. Бошқалар — Ҳозир жараёнда.",
            "Сейчас открыта только домашка по SQL. Остальное — в разработке.",
            "Only SQL homework is open for now. The rest is coming soon.",
        ),
        "Yuborilmagan": S("Юборилмаган", "Не отправлено", "Not submitted"),
        "Yuborilgan": S("Юборилган", "Отправлено", "Submitted"),
        "✅ Tekshirilgan": S("✅ Текширилган", "✅ Проверено", "✅ Reviewed"),
        "🔴 Qayta topshirish kerak": S("🔴 Қайта топшириш керак", "🔴 Нужно сдать заново", "🔴 Needs revision"),
        "🟡 Ko‘rib chiqilmoqda": S("🟡 Кўриб чиқилмоқда", "🟡 На проверке", "🟡 Under review"),
        "Hozircha uy vazifasi yo‘q.": S(
            "Ҳозирча уй вазифаси йўқ.",
            "Пока нет домашнего задания.",
            "No homework yet.",
        ),
        "Yangi .txt fayl bilan almashtirish": S(
            "Янги .txt файл билан алмаштириш",
            "Заменить новым .txt файлом",
            "Replace with a new .txt file",
        ),
        ".txt fayl yuklang": S(".txt файл юкланг", "Загрузите .txt файл", "Upload a .txt file"),
        "Faqat 1 ta .txt fayl. Bir nechta fayl yuborib bo‘lmaydi.": S(
            "Фақат 1 та .txt файл. Бир нечта файл юбориб бўлмайди.",
            "Только 1 файл .txt. Несколько файлов отправить нельзя.",
            "Only one .txt file. You cannot submit multiple files.",
        ),
        "Qayta yuborish": S("Қайта юбориш", "Отправить снова", "Resubmit"),
        "Yuborish": S("Юбориш", "Отправить", "Submit"),
        "Topshiriqlar tarixi": S("Топшириқлар тарихи", "История сдач", "Submission history"),
        "Sizning topshirig‘ingiz": S(
            "Сизнинг топшириғингиз",
            "Ваше задание",
            "Your submission",
        ),
        "Topshiriq": S("Топшириқ", "Задание", "Task"),
        "Yuklab olish": S("Юклаб олиш", "Скачать", "Download"),
        "O‘chirish": S("Ўчириш", "Удалить", "Delete"),
        "Topshiriqni o‘chirasizmi?": S(
            "Топшириқни ўчирасизми?",
            "Удалить задание?",
            "Delete this submission?",
        ),
        "O‘qituvchi bahosi:": S("Ўқитувчи баҳоси:", "Оценка преподавателя:", "Teacher score:"),
        "Hali topshiriq yo‘q.": S("Ҳали топшириқ йўқ.", "Пока нет сдач.", "No submissions yet."),
        "Vaqt ichida masala yeching va alohida reytingda o‘rin egallang.": S(
            "Вақт ичида масала ечинг ва алоҳида рейтингда ўрин эгалланг.",
            "Решайте задачи за время и займите место в отдельном рейтинге.",
            "Solve exercises in time and earn a place on a separate board.",
        ),
        "Hozircha e’lon qilingan musobaqa yo‘q.": S(
            "Ҳозирча эълон қилинган мусобақа йўқ.",
            "Пока нет объявленных соревнований.",
            "No contests have been announced yet.",
        ),
        "Haftalik SQL musobaqasi": S(
            "Ҳафталик SQL мусобақаси",
            "Еженедельное соревнование по SQL",
            "Weekly SQL contest",
        ),
        "Shu hafta ichida SQL masalalarini yeching. Ball: Oson +1, O‘rta +2, Qiyin +3. Musobaqa reytingi umumiy reytingdan alohida.": S(
            "Шу ҳафта ичида SQL масалаларини ечинг. Балл: Осон +1, Ўрта +2, Қийин +3. Мусобақа рейтинги умумий рейтингдан алоҳида.",
            "Решайте SQL-задачи в течение этой недели. Баллы: Лёгкий +1, Средний +2, Сложный +3. Рейтинг соревнования отделён от общего рейтинга.",
            "Solve SQL exercises this week. Points: Easy +1, Medium +2, Hard +3. Contest ranking is separate from the overall leaderboard.",
        ),
        "Musobaqa": S("Мусобақа", "Соревнование", "Contest"),
        "Sizning natijangiz": S("Сизнинг натижангиз", "Ваш результат", "Your result"),
        "Musobaqa masalalari": S("Мусобақа масалалари", "Задачи соревнования", "Contest exercises"),
        "avto": S("авто", "авто", "auto"),
        "Yechish": S("Ечиш", "Решить", "Solve"),
        "Masalalar hali biriktirilmagan.": S(
            "Масалалар ҳали бириктирилмаган.",
            "Задачи ещё не привязаны.",
            "No exercises attached yet.",
        ),
        "Musobaqa reytingi": S("Мусобақа рейтинги", "Рейтинг соревнования", "Contest leaderboard"),
        "Hali hech kim ball olmadi.": S(
            "Ҳали ҳеч ким балл олмади.",
            "Пока никто не набрал баллов.",
            "Nobody has scored yet.",
        ),
        "Tez orada": S("Тез орада", "Скоро", "Upcoming"),
        "Tugagan": S("Тугаган", "Завершено", "Ended"),
        "Davom etmoqda": S("Давом этмоқда", "Идёт", "Live"),
        "Ism, foydalanuvchi nomi, email va parolni yangilashingiz mumkin.": S(
            "Исм, фойдаланувчи номи, email ва паролни янгилашингиз мумкин.",
            "Можно обновить имя, логин, email и пароль.",
            "You can update your name, username, email, and password.",
        ),
        "Saqlash": S("Сақлаш", "Сохранить", "Save"),
        "bog‘langan": S("боғланган", "привязан", "linked"),
        "hali bog‘lanmagan. Botda email/parol bilan kiring — web va Telegram bir xil akkaunt bo‘ladi.": S(
            "ҳали боғланмаган. Ботда email/парол билан киринг — web ва Telegram бир хил аккаунт бўлади.",
            "ещё не привязан. Войдите в боте с email/паролем — web и Telegram будут одним аккаунтом.",
            "not linked yet. Sign in via the bot with email/password — web and Telegram stay the same account.",
        ),
        "Yutuqlar": S("Ютуқлар", "Достижения", "Achievements"),
        "Sertifikatlarim": S("Сертификатларим", "Мои сертификаты", "My certificates"),
        "Modul yoki kursni to‘liq tugatganingizdan keyin sertifikat chiqadi.": S(
            "Модул ёки курсни тўлиқ тугатганингиздан кейин сертификат чиқади.",
            "Сертификат появится после полного завершения модуля или курса.",
            "A certificate appears after you finish a module or course.",
        ),
        "Eng uzun:": S("Энг узун:", "Самая длинная:", "Longest:"),
        "Kod:": S("Код:", "Код:", "Code:"),
        "Hali sertifikat yo‘q. Modullarni tugating.": S(
            "Ҳали сертификат йўқ. Модулларни тугатинг.",
            "Пока нет сертификата. Завершите модули.",
            "No certificates yet. Finish modules.",
        ),
        "Sertifikat": S("Сертификат", "Сертификат", "Certificate"),
        "Ushbu sertifikat": S("Ушбу сертификат", "Этот сертификат", "This certificate"),
        "ga quyidagi yo‘nalishni muvaffaqiyatli tugatgani uchun beriladi:": S(
            "га қуйидаги йўналишни муваффақиятли тугатгани учун берилади:",
            "выдаётся за успешное завершение направления:",
            "is awarded for successfully completing:",
        ),
        "Berilgan sana:": S("Берилган сана:", "Дата выдачи:", "Issued:"),
        "Tasdiqlash kodi:": S("Тасдиқлаш коди:", "Код подтверждения:", "Verification code:"),
        "Orqaga": S("Орқага", "Назад", "Back"),
        "Chop etish": S("Чоп этиш", "Печать", "Print"),
        "Bilim testi:": S("Билим тести:", "Тест знаний:", "Skill test:"),
        "Modul oxirida o‘z bilimingizni tekshiring.": S(
            "Модул охирида ўз билимингизни текширинг.",
            "Проверьте знания в конце модуля.",
            "Check your knowledge at the end of the module.",
        ),
        "yechilgan": S("ечилган", "решено", "solved"),
        "4 ta variant": S("4 та вариант", "4 варианта", "4 options"),
        "Boshlash": S("Бошлаш", "Начать", "Start"),
        "Bu modul uchun bilim testi hali qo‘yilmagan.": S(
            "Бу модул учун билим тести ҳали қўйилмаган.",
            "Для этого модуля тест знаний ещё не добавлен.",
            "No skill test has been added for this module yet.",
        ),
        "Modul sertifikatini olish": S(
            "Модул сертификатини олиш",
            "Получить сертификат модуля",
            "Get the module certificate",
        ),
        "✅ To‘g‘ri!": S("✅ Тўғри!", "✅ Верно!", "✅ Correct!"),
        "Ball:": S("Балл:", "Баллы:", "Score:"),
        "Noto‘g‘ri. Qayta urinib ko‘ring.": S(
            "Нотўғри. Қайта уриниб кўринг.",
            "Неверно. Попробуйте ещё раз.",
            "Incorrect. Try again.",
        ),
        "Yechim yo‘riqnomasi": S("Ечим йўриқномаси", "Разбор решения", "Solution guide"),
        "To‘g‘ri javob darsdagi bank terminiga mos keladi.": S(
            "Тўғри жавоб дарсдаги банк терминига мос келади.",
            "Правильный ответ соответствует банковскому термину из урока.",
            "The correct answer matches the banking term from the lesson.",
        ),
        "Darsdagi inglizcha so‘zlarni eslang.": S(
            "Дарсдаги инглизча сўзларни эсланг.",
            "Вспомните английские слова из урока.",
            "Remember the English words from the lesson.",
        ),
        "Darsdagi bank so‘zlarini eslang.": S(
            "Дарсдаги банк сўзларини эсланг.",
            "Вспомните банковские слова из урока.",
            "Remember the banking words from the lesson.",
        ),
        "Keyingi masala →": S("Кейинги масала →", "Следующая задача →", "Next exercise →"),
        "Keyingi dars →": S("Кейинги дарс →", "Следующий урок →", "Next lesson →"),
        "Bajarilish:": S("Бажарилиш:", "Выполнение:", "Runtime:"),
        "Oldingi urinishlar": S("Олдинги уринишлар", "Предыдущие попытки", "Previous attempts"),
        "Topilmadi": S("Топилмади", "Не найдено", "Not found"),
        "Sahifa topilmadi": S("Саҳифа топилмади", "Страница не найдена", "Page not found"),
        "Bu kontent hozircha mavjud emas.": S(
            "Бу контент ҳозирча мавжуд эмас.",
            "Этого контента пока нет.",
            "This content is not available yet.",
        ),
        "Ruxsat yo‘q": S("Рухсат йўқ", "Нет доступа", "Forbidden"),
        "Filtrlash": S("Филтрлаш", "Фильтровать", "Filter"),
        "Masala": S("Масала", "Задача", "Exercise"),
        "Daraja": S("Даража", "Уровень", "Level"),
        "Tur": S("Тур", "Тип", "Type"),
        "Mos mashq topilmadi.": S("Мос машқ топилмади.", "Подходящих задач нет.", "No matching exercises."),
        "Oldingi": S("Олдинги", "Назад", "Previous"),
        "Keyingi": S("Кейинги", "Далее", "Next"),
        "Sahifa": S("Саҳифа", "Страница", "Page"),
        "Tekshirish": S("Текшириш", "Проверить", "Check"),
        "SQL ni ishga tushirish": S("SQL ни ишга тушириш", "Запустить SQL", "Run SQL"),
        "Tozalash": S("Тозалаш", "Очистить", "Clear"),
        "Muhokama": S("Муҳокама", "Обсуждение", "Discussion"),
        "Savolingizni yozing yoki boshqalarga yordam bering. Yechimni to‘liq ochib yubormang.": S(
            "Саволингизни ёзинг ёки бошқаларга ёрдам беринг. Ечимни тўлиқ очиб юборманг.",
            "Напишите вопрос или помогите другим. Не публикуйте полное решение.",
            "Ask a question or help others. Do not post the full solution.",
        ),
        "Hali izoh yo‘q. Birinchilardan bo‘ling.": S(
            "Ҳали изоҳ йўқ. Биринчилардан бўлинг.",
            "Пока нет комментариев. Будьте первыми.",
            "No comments yet. Be the first.",
        ),
        "Savol yoki foydali maslahat yozing...": S(
            "Савол ёки фойдали маслаҳат ёзинг...",
            "Напишите вопрос или полезный совет...",
            "Write a question or a useful hint...",
        ),
        "Izoh qoldirish": S("Изоҳ қолдириш", "Оставить комментарий", "Post comment"),
        "Holat:": S("Ҳолат:", "Статус:", "Status:"),
        "Google orqali kirish": S("Google орқали кириш", "Войти через Google", "Sign in with Google"),
        "Google orqali ro‘yxatdan o‘tish": S(
            "Google орқали рўйхатдан ўтиш",
            "Регистрация через Google",
            "Sign up with Google",
        ),
        "yoki email orqali": S("ёки email орқали", "или через email", "or with email"),
        "O‘qituvchi paneli": S("Ўқитувчи панели", "Панель преподавателя", "Teacher panel"),
        "Talabalar natijalari": S("Талабалар натижалари", "Результаты студентов", "Student results"),
        "Progress, mashq ballari va faollik bitta joyda.": S(
            "Прогресс, машқ баллари ва фаоллик битта жойда.",
            "Прогресс, баллы задач и активность в одном месте.",
            "Progress, exercise scores, and activity in one place.",
        ),
        "Jami talabalar": S("Жами талабалар", "Всего студентов", "Total students"),
        "Faol (7 kun)": S("Фаол (7 кун)", "Активны (7 дней)", "Active (7 days)"),
        "O‘rtacha progress ball": S("Ўртача прогресс балл", "Средний балл прогресса", "Average progress score"),
        "Kutayotgan uy vazifasi": S("Кутаётган уй вазифаси", "Ожидает проверки", "Pending homework"),
        "Bilim testi natijalari": S("Билим тести натижалари", "Результаты теста знаний", "Skill test results"),
        "Oson +1 · O‘rta +2 · Qiyin +3 — kim ko‘proq masala yechgan.": S(
            "Осон +1 · Ўрта +2 · Қийин +3 — ким кўпроқ масала ечган.",
            "Лёгкий +1 · Средний +2 · Сложный +3 — кто решил больше задач.",
            "Easy +1 · Medium +2 · Hard +3 — who solved more.",
        ),
        "Hali reyting bo‘sh — talabalar masala yechishi kerak.": S(
            "Ҳали рейтинг бўш — талабалар масала ечиши керак.",
            "Рейтинг пока пуст — студенты должны решать задачи.",
            "Leaderboard is empty — students need to solve exercises.",
        ),
        "So‘nggi yechimlar": S("Сўнгги ечимлар", "Последние решения", "Latest solves"),
        "Kamida 10 belgi. Bo‘sh qoldirsangiz — parol o‘zgarmaydi.": S(
            "Камида 10 белги. Бўш қолдирсангиз — парол ўзгармайди.",
            "Не менее 10 символов. Если оставить пустым — пароль не изменится.",
            "At least 10 characters. Leave blank to keep the current password.",
        ),
        "Kamida 10 belgi.": S(
            "Камида 10 белги.",
            "Не менее 10 символов.",
            "At least 10 characters.",
        ),
        "Parol juda qisqa. Kamida 10 belgi bo‘lishi kerak.": S(
            "Парол жуда қисқа. Камида 10 белги бўлиши керак.",
            "Пароль слишком короткий. Минимум 10 символов.",
            "Password is too short. It must contain at least 10 characters.",
        ),
        "Bu parol juda oddiy (ko‘p ishlatiladi).": S(
            "Бу парол жуда оддий (кўп ишлатилади).",
            "Этот пароль слишком простой (часто используется).",
            "This password is too common.",
        ),
        "Parol faqat raqamlardan iborat bo‘lmasligi kerak.": S(
            "Парол фақат рақамлардан иборат бўлмаслиги керак.",
            "Пароль не должен состоять только из цифр.",
            "This password is entirely numeric.",
        ),
        "Parol shaxsiy ma’lumotlarga juda o‘xshash.": S(
            "Парол шахсий маълумотларга жуда ўхшаш.",
            "Пароль слишком похож на ваши личные данные.",
            "The password is too similar to your personal information.",
        ),
        "Parollar mos kelmadi.": S(
            "Пароллар мос келмади.",
            "Пароли не совпадают.",
            "The passwords do not match.",
        ),
        "Foydalanuvchi nomi majburiy.": S(
            "Фойдаланувчи номи мажбурий.",
            "Имя пользователя обязательно.",
            "Username is required.",
        ),
        "Bu foydalanuvchi nomi band.": S(
            "Бу фойдаланувчи номи банд.",
            "Это имя пользователя занято.",
            "This username is taken.",
        ),
        "Email majburiy.": S("Email мажбурий.", "Email обязателен.", "Email is required."),
        "Bu email allaqachon band.": S(
            "Бу email аллақачон банд.",
            "Этот email уже занят.",
            "This email is already taken.",
        ),
        "Yangi parolni ikkala maydonga ham yozing.": S(
            "Янги паролни иккала майдонга ҳам ёзинг.",
            "Введите новый пароль в оба поля.",
            "Enter the new password in both fields.",
        ),
        "Yangi parollar mos kelmadi.": S(
            "Янги пароллар мос келмади.",
            "Новые пароли не совпадают.",
            "The new passwords do not match.",
        ),
        "Parolni o‘zgartirish uchun joriy parolni kiriting.": S(
            "Паролни ўзгартириш учун жорий паролни киритинг.",
            "Чтобы сменить пароль, введите текущий.",
            "Enter your current password to change it.",
        ),
        "Joriy parol noto‘g‘ri.": S("Жорий парол нотўғри.", "Текущий пароль неверен.", "Current password is incorrect."),
        "Bu hisob faol emas.": S("Бу ҳисоб фаол эмас.", "Этот аккаунт неактивен.", "This account is inactive."),
        "Ro‘yxatdan o‘tish muvaffaqiyatli yakunlandi.": S(
            "Рўйхатдан ўтиш муваффақиятли якунланди.",
            "Регистрация успешно завершена.",
            "Registration completed successfully.",
        ),
        "Profil va parol yangilandi.": S(
            "Профил ва парол янгиланди.",
            "Профиль и пароль обновлены.",
            "Profile and password updated.",
        ),
        "Profil yangilandi.": S("Профил янгиланди.", "Профиль обновлён.", "Profile updated."),
        "Google orqali kirish bekor qilindi.": S(
            "Google орқали кириш бекор қилинди.",
            "Вход через Google отменён.",
            "Google sign-in was cancelled.",
        ),
        "Google orqali kirish xavfsizlik tekshiruvidan o‘tmadi. Qayta urinib ko‘ring.": S(
            "Google орқали кириш хавфсизлик текширувидан ўтмади. Қайта уриниб кўринг.",
            "Вход через Google не прошёл проверку безопасности. Попробуйте снова.",
            "Google sign-in failed the security check. Try again.",
        ),
        "Google orqali kirish hozircha sozlanmagan.": S(
            "Google орқали кириш ҳозирча созланмаган.",
            "Вход через Google пока не настроен.",
            "Google sign-in is not configured yet.",
        ),
        "Google bilan bog‘lanib bo‘lmadi. Keyinroq qayta urinib ko‘ring.": S(
            "Google билан боғланиб бўлмади. Кейинроқ қайта уриниб кўринг.",
            "Не удалось связаться с Google. Попробуйте позже.",
            "Could not connect to Google. Try again later.",
        ),
        "Google hisobi orqali ro‘yxatdan o‘tdingiz.": S(
            "Google ҳисоби орқали рўйхатдан ўтдингиз.",
            "Вы зарегистрировались через Google.",
            "You signed up with Google.",
        ),
        "Faqat 1 ta .txt fayl yuborish mumkin.": S(
            "Фақат 1 та .txt файл юбориш мумкин.",
            "Можно отправить только 1 файл .txt.",
            "You can submit only one .txt file.",
        ),
        "Fayl tanlang.": S("Файл танланг.", "Выберите файл.", "Choose a file."),
        "Fayl nomi noto‘g‘ri.": S("Файл номи нотўғри.", "Некорректное имя файла.", "Invalid file name."),
        "Faqat .txt fayl yuborish mumkin.": S(
            "Фақат .txt файл юбориш мумкин.",
            "Можно отправить только файл .txt.",
            "Only .txt files are allowed.",
        ),
        "Fayl hajmi {n} MB dan oshmasligi kerak.": S(
            "Файл ҳажми {n} MB дан ошмаслиги керак.",
            "Размер файла не должен превышать {n} МБ.",
            "File size must not exceed {n} MB.",
        ),
        "Fayl turi qo‘llab-quvvatlanmaydi.": S(
            "Файл тури қўллаб-қувватланмайди.",
            "Тип файла не поддерживается.",
            "File type is not supported.",
        ),
        "Fayl bo‘sh bo‘lmasligi kerak.": S(
            "Файл бўш бўлмаслиги керак.",
            "Файл не должен быть пустым.",
            "File must not be empty.",
        ),
        "Fayl UTF-8 matn formatida bo‘lishi kerak.": S(
            "Файл UTF-8 матн форматида бўлиши керак.",
            "Файл должен быть в текстовом формате UTF-8.",
            "File must be UTF-8 text.",
        ),
        "Ikkilik fayllar qabul qilinmaydi.": S(
            "Иккилик файллар қабул қилинмайди.",
            "Двоичные файлы не принимаются.",
            "Binary files are not accepted.",
        ),
        "Uy vazifasi saqlandi.": S("Уй вазифаси сақланди.", "Домашнее задание сохранено.", "Homework saved."),
        "Topshiriq o‘chirildi.": S("Топшириқ ўчирилди.", "Задание удалено.", "Submission deleted."),
        "Izoh juda qisqa. Kamida 3 ta belgi yozing.": S(
            "Изоҳ жуда қисқа. Камида 3 та белги ёзинг.",
            "Комментарий слишком короткий. Минимум 3 символа.",
            "Comment is too short. Write at least 3 characters.",
        ),
        "Izoh juda uzun (maksimum 2000 belgi).": S(
            "Изоҳ жуда узун (максимум 2000 белги).",
            "Комментарий слишком длинный (максимум 2000 символов).",
            "Comment is too long (maximum 2000 characters).",
        ),
        "Izohingiz qo‘shildi.": S("Изоҳингиз қўшилди.", "Комментарий добавлен.", "Your comment was added."),
        "Sertifikat tayyor!": S("Сертификат тайёр!", "Сертификат готов!", "Certificate ready!"),
        "Kurs hali to‘liq tugallanmagan.": S(
            "Курс ҳали тўлиқ тугалланмаган.",
            "Курс ещё не полностью завершён.",
            "The course is not fully completed yet.",
        ),
        "Kurs sertifikati tayyor!": S(
            "Курс сертификати тайёр!",
            "Сертификат курса готов!",
            "Course certificate ready!",
        ),
        "Ma’ruza tugallandi.": S("Маъруза тугалланди.", "Лекция завершена.", "Lecture completed."),
        "Keyingi modullar Premium. To‘liq kurs uchun admin ruxsati kerak.": S(
            "Кейинги модуллар Premium. Тўлиқ курс учун admin рухсати керак.",
            "Следующие модули Premium. Для полного курса нужно разрешение администратора.",
            "Next modules are Premium. Full course access needs admin approval.",
        ),
        "Modul bilim testi. To‘g‘ri javobni tanlang.": S(
            "Модул билим тести. Тўғри жавобни танланг.",
            "Тест знаний модуля. Выберите правильный ответ.",
            "Module skill test. Choose the correct answer.",
        ),
        "Modul bilim testi. To‘g‘ri inglizcha javobni tanlang.": S(
            "Модул билим тести. Тўғри инглизча жавобни танланг.",
            "Тест знаний модуля. Выберите правильный ответ на английском.",
            "Module skill test. Choose the correct English answer.",
        ),
        "Modul hali tugallanmagan. Barcha darslar, mashqlar va bilim testini yakunlang.": S(
            "Модул ҳали тугалланмаган. Барча дарслар, машқлар ва билим тестини якунланг.",
            "Модуль ещё не завершён. Завершите все уроки, задачи и тест знаний.",
            "The module is not finished yet. Complete all lessons, exercises, and the skill test.",
        ),
        "Dars o‘qildi. Endi amaliyotni yeching — shunda dars to‘liq tugallangan hisoblanadi.": S(
            "Дарс ўқилди. Энди амалиётни ечинг — шунда дарс тўлиқ тугалланган ҳисобланади.",
            "Урок прочитан. Теперь решите практику — тогда урок будет полностью завершён.",
            "Lesson read. Now solve the practice — then the lesson counts as complete.",
        ),
        "Bu modul bilim testi Premium. To‘liq kurs ochilgach yoki dastlabki 5 modulda mavjud.": S(
            "Бу модул билим тести Premium. Тўлиқ курс очилгач ёки дастлабки 5 модулда мавжуд.",
            "Этот тест модуля Premium. Доступен после открытия курса или в первых 5 модулях.",
            "This module skill test is Premium. It is available after unlocking the course or in the first 5 modules.",
        ),
        "Uy vazifasini ko‘rish va yuborish uchun tizimga kiring yoki ro‘yxatdan o‘ting.": S(
            "Уй вазифасини кўриш ва юбориш учун тизимга киринг ёки рўйхатдан ўтинг.",
            "Чтобы смотреть и сдавать домашку, войдите или зарегистрируйтесь.",
            "Sign in or register to view and submit homework.",
        ),
        "Sertifikatlaringizni ko‘rish uchun tizimga kiring yoki ro‘yxatdan o‘ting.": S(
            "Сертификатларингизни кўриш учун тизимга киринг ёки рўйхатдан ўтинг.",
            "Чтобы видеть сертификаты, войдите или зарегистрируйтесь.",
            "Sign in or register to see your certificates.",
        ),
        "Darsdagi asosiy ta’rifni eslang.": S(
            "Дарсдаги асосий таърифни эсланг.",
            "Вспомните основное определение из урока.",
            "Remember the main definition from the lesson.",
        ),
        "Noto‘g‘ri variantlarni chiqarib tashlang.": S(
            "Нотўғри вариантларни чиқариб ташланг.",
            "Отбросьте неверные варианты.",
            "Eliminate the wrong options.",
        ),
        "To‘g‘ri javob:": S("Тўғри жавоб:", "Правильный ответ:", "Correct answer:"),
        "To‘g‘ri javobni tanlang": S(
            "Тўғри жавобни танланг",
            "Выберите правильный ответ",
            "Choose the correct answer",
        ),
        "To‘g‘ri javob": S("Тўғри жавоб", "Правильный ответ", "Correct answer"),
        "Darslar": S("Дарслар", "Уроки", "Lessons"),
        "Qo‘shimcha mashqlar": S("Қўшимча машқлар", "Дополнительные задачи", "Extra exercises"),
        "Amaliyot qoldi": S("Амалиёт қолди", "Осталась практика", "Practice left"),
        "Darsni belgilang": S("Дарсни белгиланг", "Отметьте урок", "Mark the lesson"),
        "Sertifikatni olish": S("Сертификатни олиш", "Получить сертификат", "Get certificate"),
    }
)

from .content_titles import TITLE_STRINGS

STRINGS.update(TITLE_STRINGS)

# Phrase replacements for lesson/puzzle prose (longest first). SQL stays via protect().
PHRASES: list[tuple[str, dict[str, str]]] = [
    ("qadamma-qadam o‘rganasiz", S("қадамма-қадам ўрганасиз", "изучаете шаг за шагом", "you learn step by step")),
    ("Har darsdan keyin mashq bor", S("Ҳар дарсдан кейин машқ бор", "После каждого урока есть практика", "Every lesson has practice")),
    ("o‘qituvchi bilan gaplashgandek", S("ўқитувчи билан гаплашгандек", "как разговор с преподавателем", "like talking with a teacher")),
    ("Natija to‘plami tekshiriladi", S("Натижа тўплами текширилади", "Набор строк проверяется", "The result set is checked")),
    ("Ustunlar:", S("Устунлар:", "Столбцы:", "Columns:")),
    ("Ustun:", S("Устун:", "Столбец:", "Column:")),
    ("Qaytaring", S("Қайтаринг", "Верните", "Return")),
    ("qaytaring", S("қайтаринг", "верните", "return")),
    ("tanlang", S("танланг", "выберите", "choose")),
    ("Tanlang", S("Танланг", "Выберите", "Choose")),
    ("yozing", S("ёзинг", "напишите", "write")),
    ("Yozing", S("Ёзинг", "Напишите", "Write")),
    ("toping", S("топинг", "найдите", "find")),
    ("Toping", S("Топинг", "Найдите", "Find")),
    ("tushuntiring", S("тушунтиринг", "объясните", "explain")),
    ("mijozlar", S("мижозлар", "клиенты", "customers")),
    ("Mijozlar", S("Мижозлар", "Клиенты", "Customers")),
    ("mijoz", S("мижоз", "клиент", "customer")),
    ("Mijoz", S("Мижоз", "Клиент", "Customer")),
    ("tranzaksiya", S("транзаксия", "транзакция", "transaction")),
    ("Tranzaksiya", S("Транзаксия", "Транзакция", "Transaction")),
    ("jadvalidan", S("жадвалидан", "из таблицы", "from the table")),
    ("jadvalida", S("жадвалида", "в таблице", "in the table")),
    ("jadval", S("жадвал", "таблица", "table")),
    ("Jadval", S("Жадвал", "Таблица", "Table")),
    ("ustunlarini", S("устунларини", "столбцы", "columns")),
    ("ustunlari", S("устунлари", "столбцы", "columns")),
    ("ustun", S("устун", "столбец", "column")),
    ("Ustun", S("Устун", "Столбец", "Column")),
    ("qatorlar", S("қаторлар", "строки", "rows")),
    ("qator", S("қатор", "строка", "row")),
    ("so‘rovni", S("сўровни", "запрос", "query")),
    ("so‘rovi", S("сўрови", "запрос", "query")),
    ("so‘rov", S("сўров", "запрос", "query")),
    ("So‘rov", S("Сўров", "Запрос", "Query")),
    ("shaharlar", S("шаҳарлар", "города", "cities")),
    ("shahar", S("шаҳар", "город", "city")),
    ("Shahar", S("Шаҳар", "Город", "City")),
    ("ismlari", S("исмлари", "имена", "names")),
    ("ismlar", S("исмлар", "имена", "names")),
    ("nomini", S("номини", "название", "the name")),
    ("nomi", S("номи", "название", "name")),
    ("mashq", S("машқ", "упражнение", "exercise")),
    ("dars", S("дарс", "урок", "lesson")),
    ("modul", S("модул", "модуль", "module")),
    ("bo‘yicha", S("бўйича", "по", "by")),
    ("uchun", S("учун", "для", "for")),
    ("bilan", S("билан", "с", "with")),
    ("keyin", S("кейин", "затем", "then")),
    ("avval", S("аввал", "сначала", "first")),
    ("Avval", S("Аввал", "Сначала", "First")),
    ("kerakli", S("керакли", "нужные", "required")),
    ("kerak", S("керак", "нужно", "need")),
    ("to‘g‘ri", S("тўғри", "правильный", "correct")),
    ("noto‘g‘ri", S("нотўғри", "неверный", "incorrect")),
    ("oson", S("осон", "лёгкий", "easy")),
    ("qiyin", S("қийин", "сложный", "hard")),
    ("yig‘indisi", S("йиғиндиси", "сумма", "sum")),
    ("soni", S("сони", "количество", "count")),
    ("tartibida", S("тартибида", "в порядке", "in order")),
    ("o‘sish", S("ўсиш", "возрастание", "ascending")),
    ("kamayish", S("камайиш", "убывание", "descending")),
    ("filtrlash", S("филтрлаш", "фильтрация", "filtering")),
    ("saralash", S("саралаш", "сортировка", "sorting")),
    ("guruhlash", S("гуруҳлаш", "группировка", "grouping")),
    ("nima?", S("нима?", "что это?", "what is it?")),
    ("nima qiladi", S("нима қилади", "что делает", "what does it do")),
    ("nima uchun ishlatiladi", S("нима учун ишлатилади", "для чего используется", "what is it used for")),
    ("To‘g‘ri javobni tanlang", S("Тўғри жавобни танланг", "Выберите правильный ответ", "Choose the correct answer")),
    ("To‘g‘ri javob", S("Тўғри жавоб", "Правильный ответ", "Correct answer")),
    ("ma’lumot o‘qish", S("маълумот ўқиш", "чтение данных", "reading data")),
    ("ma’lumot", S("маълумот", "данные", "data")),
    ("nima", S("нима", "что", "what")),
    ("qanday", S("қандай", "как", "how")),
]


def _norm_lookup_key(text: str) -> str:
    return (
        text.replace("\r\n", "\n")
        .replace("\r", "\n")
        .replace("‘", "'")
        .replace("’", "'")
        .replace("ʻ", "'")
        .replace("ʼ", "'")
        .replace("´", "'")
        .strip()
    )


_STRINGS_NORM = {_norm_lookup_key(key): value for key, value in STRINGS.items()}


def lookup_exact(text: str, lang: str) -> str | None:
    row = STRINGS.get(text) or _STRINGS_NORM.get(_norm_lookup_key(text))
    if not row:
        return None
    return row.get(lang)


def apply_phrases(text: str, lang: str) -> str:
    if lang not in ("uz-cyrl", "ru", "en"):
        return text
    phrases = sorted(PHRASES, key=lambda item: len(item[0]), reverse=True)
    out = text
    for src, trans in phrases:
        dst = trans.get(lang)
        if not dst:
            continue
        out = re.sub(r"(?<!\w)" + re.escape(src) + r"(?!\w)", dst, out)
    return out
