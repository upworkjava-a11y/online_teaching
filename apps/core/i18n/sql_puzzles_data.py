"""Exact Uzbek puzzle copy → English/Russian. Identifiers stay Latin."""

from __future__ import annotations

# (uzbek, russian, english)
PAIRS: list[tuple[str, str, str]] = [
    (
        "Hisobot uchun mijozlar ro‘yxati kerak. customers jadvalidan barcha mijozlarning ismini oling. Natijada faqat name ustuni bo‘lishi kerak.",
        "Для отчёта нужен список клиентов. Из таблицы customers возьмите имена всех клиентов. В результате должен быть только столбец name.",
        "You need a customer list for a report. From the customers table, take every customer’s name. The result must have only the name column.",
    ),
    (
        "Faqat name ustunini qaytaring. Qator tartibi muhim emas.",
        "Верните только столбец name. Порядок строк не важен.",
        "Return only the name column. Row order does not matter.",
    ),
    (
        "Filial Toshkentdagi mijozlarni alohida ko‘rmoqchi. Faqat shu shahardagi qatorlarni oling.",
        "Филиал хочет отдельно видеть клиентов из Toshkent. Возьмите только строки из этого города.",
        "The branch wants to see customers in Toshkent separately. Take only rows from that city.",
    ),
    (
        "name va city ustunlarini qaytaring. Faqat Toshkent.",
        "Верните столбцы name и city. Только Toshkent.",
        "Return the name and city columns. Only Toshkent.",
    ),
    (
        "Risk-nazorat 100 000 so‘mdan katta to‘lovlarni ko‘rmoqchi. transactions jadvalidan shunday qatorlarni toping.",
        "Риск-контроль хочет видеть платежи больше 100 000 сум. Найдите такие строки в таблице transactions.",
        "Risk control wants payments greater than 100 000 som. Find those rows in the transactions table.",
    ),
    (
        "id va amount. 100 000 dan qat’iy katta summalar.",
        "id и amount. Суммы строго больше 100 000.",
        "id and amount. Amounts strictly greater than 100 000.",
    ),
    (
        "Moliya bo‘limi faqat debit operatsiyalarni hisobotga oladi.",
        "Финансовый отдел берёт в отчёт только операции debit.",
        "Finance includes only debit operations in the report.",
    ),
    (
        "id va transaction_type. Faqat debit qatorlar.",
        "id и transaction_type. Только строки debit.",
        "id and transaction_type. Only debit rows.",
    ),
    (
        "Eng katta to‘lovlardan boshlang. Barcha tranzaksiyalarni summa kamayish tartibida chiqaring.",
        "Начните с самых крупных платежей. Выведите все транзакции по убыванию суммы.",
        "Start from the largest payments. List all transactions in descending amount order.",
    ),
    (
        "id va amount. Eng katta summa tepada. Qator tartibi tekshiriladi.",
        "id и amount. Самая большая сумма сверху. Порядок строк проверяется.",
        "id and amount. Largest amount on top. Row order is checked.",
    ),
    (
        "Marketing 5 tadan ko‘p tranzaksiya qilgan mijozlarni VIP deb belgilamoqchi.",
        "Маркетинг хочет пометить VIP клиентов с более чем 5 транзакциями.",
        "Marketing wants to mark customers with more than 5 transactions as VIP.",
    ),
    (
        "Faqat customer_id. 5 tadan ko‘p to‘lovi borlar.",
        "Только customer_id. У кого больше 5 платежей.",
        "Only customer_id. Those with more than 5 payments.",
    ),
    (
        "Kunlik tushumni baholash: barcha tranzaksiyalar yig‘indisi.",
        "Оценка дневной выручки: сумма всех транзакций.",
        "Estimate daily revenue: the sum of all transactions.",
    ),
    (
        "Bitta qator, ustun nomi total.",
        "Одна строка, имя столбца total.",
        "One row, column name total.",
    ),
    (
        "Har bir mijoz qancha operatsiya qilganini ko‘ring. Bu faollik hisoboti.",
        "Посмотрите, сколько операций сделал каждый клиент. Это отчёт по активности.",
        "See how many operations each customer made. This is an activity report.",
    ),
    (
        "customer_id va cnt — har mijoz uchun operatsiyalar soni.",
        "customer_id и cnt — число операций по каждому клиенту.",
        "customer_id and cnt — operation count per customer.",
    ),
    (
        "Har bir mijozning umumiy to‘lov hajmi. LTV ga yaqin ko‘rsatkich.",
        "Общий объём платежей каждого клиента. Показатель близкий к LTV.",
        "Each customer’s total payment volume. A metric close to LTV.",
    ),
    (
        "customer_id va total — har mijoz uchun summalar yig‘indisi.",
        "customer_id и total — сумма по каждому клиенту.",
        "customer_id and total — the sum of amounts per customer.",
    ),
    (
        "Jadval: Products — product_id, low_fats, recyclable.\n\n"
        "Barcha mahsulotlarning product_id qiymatlarini oling.\n"
        "Filtr yo‘q — faqat ustun tanlash. Tartib ixtiyoriy.",
        "Таблица: Products — product_id, low_fats, recyclable.\n\n"
        "Получите значения product_id всех продуктов.\n"
        "Фильтра нет — только выбор столбца. Порядок любой.",
        "Table: Products — product_id, low_fats, recyclable.\n\n"
        "Get the product_id values of all products.\n"
        "No filter — only column selection. Order is optional.",
    ),
    (
        "Faqat product_id ustuni. Barcha qatorlar.",
        "Только столбец product_id. Все строки.",
        "Only the product_id column. All rows.",
    ),
    (
        "SELECT dan keyin qaysi ustun kerakligini yozing",
        "После SELECT напишите, какой столбец нужен",
        "After SELECT, write which column you need",
    ),
    (
        "Jadval nomi: Products",
        "Имя таблицы: Products",
        "Table name: Products",
    ),
    (
        "Jadval: World — name, continent, area, population, gdp.\n\n"
        "Hisobot uchun faqat name, population va area kerak.\n"
        "Hali filtr yo‘q — barcha davlatlar. Tartib ixtiyoriy.",
        "Таблица: World — name, continent, area, population, gdp.\n\n"
        "Для отчёта нужны только name, population и area.\n"
        "Фильтра пока нет — все страны. Порядок любой.",
        "Table: World — name, continent, area, population, gdp.\n\n"
        "For the report you only need name, population, and area.\n"
        "No filter yet — all countries. Order is optional.",
    ),
    (
        "Ustunlar: name, population, area. Filtr yo‘q.",
        "Столбцы: name, population, area. Фильтра нет.",
        "Columns: name, population, area. No filter.",
    ),
    (
        "Ustunlarni vergul bilan yozing",
        "Пишите столбцы через запятую",
        "Write columns separated by commas",
    ),
    (
        "* emas — faqat so‘ralgan uchta",
        "Не * — только три запрошенных",
        "Not * — only the three asked for",
    ),
    (
        "Jadval: World.\n\n"
        "Jadvalda bir qit’a bir necha marta chiqishi mumkin.\n"
        "Qaysi qit’alar bor — har birini bir marta ko‘rsating.\n"
        "Ustun: continent. Tartib ixtiyoriy.",
        "Таблица: World.\n\n"
        "В таблице один континент может встретиться несколько раз.\n"
        "Какие континенты есть — покажите каждый один раз.\n"
        "Столбец: continent. Порядок любой.",
        "Table: World.\n\n"
        "A continent may appear more than once in the table.\n"
        "Which continents exist — show each one once.\n"
        "Column: continent. Order is optional.",
    ),
    (
        "Takrorsiz continent qiymatlari.",
        "Уникальные значения continent.",
        "Distinct continent values.",
    ),
    (
        "Takror kerak emas — DISTINCT",
        "Повторы не нужны — DISTINCT",
        "No duplicates — DISTINCT",
    ),
    (
        "Faqat continent ustuni",
        "Только столбец continent",
        "Only the continent column",
    ),
    (
        "LeetCode 1683. Invalid Tweets (Easy)\n\n"
        "Jadval: Tweets — tweet_id, content.\n\n"
        "Tvit noto‘g‘ri, agar content dagi belgilar soni 15 dan qat’iy katta bo‘lsa.\n"
        "Noto‘g‘ri tvitlarning tweet_id sini qaytaring. Tartib ixtiyoriy.",
        "LeetCode 1683. Invalid Tweets (Easy)\n\n"
        "Таблица: Tweets — tweet_id, content.\n\n"
        "Твит некорректен, если число символов в content строго больше 15.\n"
        "Верните tweet_id некорректных твитов. Порядок любой.",
        "LeetCode 1683. Invalid Tweets (Easy)\n\n"
        "Table: Tweets — tweet_id, content.\n\n"
        "A tweet is invalid if the number of characters in content is strictly greater than 15.\n"
        "Return the tweet_id of invalid tweets. Order is optional.",
    ),
    (
        "Faqat tweet_id. Belgilar soni 15 dan qat’iy katta.",
        "Только tweet_id. Число символов строго больше 15.",
        "Only tweet_id. Character count strictly greater than 15.",
    ),
    (
        "Tenglik emas — qat’iy katta",
        "Не равенство — строго больше",
        "Not equality — strictly greater",
    ),
    (
        "Matn uzunligi: LENGTH(content)",
        "Длина текста: LENGTH(content)",
        "Text length: LENGTH(content)",
    ),
    (
        "LeetCode 1148. Article Views I (Easy)\n\n"
        "Jadval: Views — article_id, author_id, viewer_id, view_date.\n"
        "Bir xil author_id va viewer_id — bu bir xil odam.\n"
        "Jadvalda takroriy qatorlar bo‘lishi mumkin.\n\n"
        "O‘z maqolasini kamida bir marta o‘zi ko‘rgan mualliflarni toping.\n"
        "Natijada ustun nomi id bo‘lsin (bu author_id).\n"
        "id o‘sish tartibida saralang.",
        "LeetCode 1148. Article Views I (Easy)\n\n"
        "Таблица: Views — article_id, author_id, viewer_id, view_date.\n"
        "Одинаковые author_id и viewer_id — это один человек.\n"
        "В таблице могут быть повторяющиеся строки.\n\n"
        "Найдите авторов, которые хотя бы раз смотрели свою статью.\n"
        "В результате столбец пусть называется id (это author_id).\n"
        "Отсортируйте id по возрастанию.",
        "LeetCode 1148. Article Views I (Easy)\n\n"
        "Table: Views — article_id, author_id, viewer_id, view_date.\n"
        "The same author_id and viewer_id means the same person.\n"
        "The table may contain duplicate rows.\n\n"
        "Find authors who viewed their own article at least once.\n"
        "In the result the column name should be id (that is author_id).\n"
        "Sort id in ascending order.",
    ),
    (
        "Ustun nomi id. O‘zini ko‘rgan mualliflar, o‘sish tartibida, takrorsiz.",
        "Имя столбца id. Авторы, смотревшие себя, по возрастанию, без повторов.",
        "Column name id. Authors who viewed themselves, ascending, distinct.",
    ),
    (
        "WHERE da muallif va tomoshabin bir xil bo‘lsin",
        "В WHERE автор и зритель должны совпадать",
        "In WHERE the author and viewer should be the same",
    ),
    (
        "DISTINCT + AS id, keyin ORDER BY",
        "DISTINCT + AS id, затем ORDER BY",
        "DISTINCT + AS id, then ORDER BY",
    ),
    (
        "LeetCode 1527. Patients With a Condition (Easy)\n\n"
        "Jadval: Patients — patient_id, patient_name, conditions.\n"
        "conditions — bo‘shliq bilan ajratilgan kodlar (masalan: ACNE DIAB100).\n\n"
        "I turdagi diabet kodi DIAB1 bilan boshlanadi.\n"
        "Shartlar ro‘yxatida DIAB1 bilan boshlanadigan kod bor bemorlarni qaytaring.\n"
        "DIAB100 mos keladi, DIAB201 esa yo‘q (chunki DIAB2...).",
        "LeetCode 1527. Patients With a Condition (Easy)\n\n"
        "Таблица: Patients — patient_id, patient_name, conditions.\n"
        "conditions — коды через пробел (например: ACNE DIAB100).\n\n"
        "Код диабета I типа начинается с DIAB1.\n"
        "Верните пациентов, у которых в списке условий есть код, начинающийся с DIAB1.\n"
        "DIAB100 подходит, DIAB201 — нет (потому что DIAB2...).",
        "LeetCode 1527. Patients With a Condition (Easy)\n\n"
        "Table: Patients — patient_id, patient_name, conditions.\n"
        "conditions — space-separated codes (for example: ACNE DIAB100).\n\n"
        "A type I diabetes code starts with DIAB1.\n"
        "Return patients who have a code starting with DIAB1 in the conditions list.\n"
        "DIAB100 matches, DIAB201 does not (because it is DIAB2...).",
    ),
    (
        "patient_id, patient_name, conditions. Faqat I tur diabet kodi borlar.",
        "patient_id, patient_name, conditions. Только те, у кого код диабета I типа.",
        "patient_id, patient_name, conditions. Only those with a type I diabetes code.",
    ),
    (
        "Kod qator boshida: LIKE 'DIAB1%'",
        "Код в начале строки: LIKE 'DIAB1%'",
        "Code at the start of the row: LIKE 'DIAB1%'",
    ),
    (
        "Yoki bo‘shliqdan keyin: LIKE '% DIAB1%'",
        "Или после пробела: LIKE '% DIAB1%'",
        "Or after a space: LIKE '% DIAB1%'",
    ),
    (
        "Jadval: Followers — user_id, follower_id.\n\n"
        "Jadvalda jami nechta qator (obuna juftligi) bor?\n"
        "Bitta son qaytaring. Ustun nomi: total.",
        "Таблица: Followers — user_id, follower_id.\n\n"
        "Сколько всего строк (пар подписки) в таблице?\n"
        "Верните одно число. Имя столбца: total.",
        "Table: Followers — user_id, follower_id.\n\n"
        "How many rows (follow pairs) are in the table in total?\n"
        "Return one number. Column name: total.",
    ),
    (
        "Bitta qator, ustun: total.",
        "Одна строка, столбец: total.",
        "One row, column: total.",
    ),
    ("COUNT(*) AS total", "COUNT(*) AS total", "COUNT(*) AS total"),
    (
        "GROUP BY hozircha kerak emas — butun jadval",
        "GROUP BY пока не нужен — вся таблица",
        "GROUP BY is not needed yet — the whole table",
    ),
    (
        "Jadval: EmployeeAttendance — emp_id, event_day, in_time, out_time.\n"
        "Har qatorda sessiya: out_time - in_time daqiqalar.\n\n"
        "Barcha sessiyalar bo‘yicha jami daqiqani toping.\n"
        "Ustun: total_time.",
        "Таблица: EmployeeAttendance — emp_id, event_day, in_time, out_time.\n"
        "В каждой строке сессия: out_time - in_time в минутах.\n\n"
        "Найдите суммарные минуты по всем сессиям.\n"
        "Столбец: total_time.",
        "Table: EmployeeAttendance — emp_id, event_day, in_time, out_time.\n"
        "Each row is a session: out_time - in_time in minutes.\n\n"
        "Find the total minutes across all sessions.\n"
        "Column: total_time.",
    ),
    (
        "Bitta qator: total_time — barcha (out_time - in_time) yig‘indisi.",
        "Одна строка: total_time — сумма всех (out_time - in_time).",
        "One row: total_time — the sum of all (out_time - in_time).",
    ),
    (
        "SUM ichida ifoda yozish mumkin",
        "Внутри SUM можно написать выражение",
        "You can write an expression inside SUM",
    ),
    (
        "GROUP BY hozircha shart emas",
        "GROUP BY пока не обязателен",
        "GROUP BY is not required yet",
    ),
    (
        "LeetCode 1729. Find Followers Count (Easy)\n\n"
        "Jadval: Followers — user_id, follower_id (juftlik unikal).\n\n"
        "Har bir foydalanuvchining obunachilari sonini hisoblang.\n"
        "Ustunlar: user_id, followers_count.\n"
        "user_id o‘sish tartibida qaytaring.",
        "LeetCode 1729. Find Followers Count (Easy)\n\n"
        "Таблица: Followers — user_id, follower_id (пара уникальна).\n\n"
        "Посчитайте число подписчиков каждого пользователя.\n"
        "Столбцы: user_id, followers_count.\n"
        "Верните user_id по возрастанию.",
        "LeetCode 1729. Find Followers Count (Easy)\n\n"
        "Table: Followers — user_id, follower_id (the pair is unique).\n\n"
        "Count each user’s followers.\n"
        "Columns: user_id, followers_count.\n"
        "Return user_id in ascending order.",
    ),
    (
        "user_id va followers_count. Har foydalanuvchi, user_id o‘sish tartibida.",
        "user_id и followers_count. Каждый пользователь, user_id по возрастанию.",
        "user_id and followers_count. Each user, user_id ascending.",
    ),
    (
        "Har user_id uchun GROUP BY",
        "GROUP BY по каждому user_id",
        "GROUP BY for each user_id",
    ),
    (
        "COUNT(*) AS followers_count, ORDER BY user_id",
        "COUNT(*) AS followers_count, ORDER BY user_id",
        "COUNT(*) AS followers_count, ORDER BY user_id",
    ),
    (
        "Biznes: geografik tahlil uchun “yirik bozor” davlatlarini ajrating.\n\n"
        "Jadval: World (name, continent, area, population, gdp).\n\n"
        "Davlatni qaytaring, agar BIR VAQTNING O‘ZIDA:\n"
        "• area >= 2 000 000 VA\n"
        "• population >= 25 000 000.\n\n"
        "Ustunlar: name, population, area. Tartib ixtiyoriy.",
        "Бизнес: для географического анализа отберите страны «крупного рынка».\n\n"
        "Таблица: World (name, continent, area, population, gdp).\n\n"
        "Верните страну, если ОДНОВРЕМЕННО:\n"
        "• area >= 2 000 000 И\n"
        "• population >= 25 000 000.\n\n"
        "Столбцы: name, population, area. Порядок любой.",
        "Business: for geographic analysis, pick out “large market” countries.\n\n"
        "Table: World (name, continent, area, population, gdp).\n\n"
        "Return the country if BOTH of these hold at once:\n"
        "• area >= 2 000 000 AND\n"
        "• population >= 25 000 000.\n\n"
        "Columns: name, population, area. Order is optional.",
    ),
    (
        "name, population, area. Ikkalasi ham: katta maydon VA katta aholi.",
        "name, population, area. Оба сразу: большая площадь И большое население.",
        "name, population, area. Both: large area AND large population.",
    ),
    (
        "Ikki shart birga — AND",
        "Два условия вместе — AND",
        "Two conditions together — AND",
    ),
    (
        "Namunadagi qatorlarni qoida bilan solishtiring",
        "Сверьте строки примера с правилом",
        "Compare the sample rows with the rule",
    ),
    (
        "Biznes: kinoteatr katalogidan top-2 film.\n\n"
        "cinema jadvalidan rating bo‘yicha eng yuqori 2 ta filmni qaytaring.\n"
        "Ustunlar: id, movie, rating. rating DESC.",
        "Бизнес: топ-2 фильма из каталога кинотеатра.\n\n"
        "Из таблицы cinema верните 2 фильма с наивысшим rating.\n"
        "Столбцы: id, movie, rating. rating DESC.",
        "Business: top-2 films from the cinema catalog.\n\n"
        "From the cinema table, return the 2 films with the highest rating.\n"
        "Columns: id, movie, rating. rating DESC.",
    ),
    (
        "id, movie, rating. Faqat eng yuqori ikkita.",
        "id, movie, rating. Только два самых высоких.",
        "id, movie, rating. Only the top two.",
    ),
    (
        "Avval reyting bo‘yicha tushing",
        "Сначала спускайтесь по рейтингу",
        "First sort down by rating",
    ),
    (
        "Keyin natijani 2 qatorgacha qisqartiring",
        "Затем сократите результат до 2 строк",
        "Then cut the result down to 2 rows",
    ),
    (
        "Biznes: aholi zichligi yuqori va iqtisodi kuchli bozorlar.\n\n"
        "World jadvalidan davlatlarni tanlang:\n"
        "• aholi zichligi (aholi / maydon) 90 dan qat’iy katta\n"
        "• VA gdp kamida 10 milliard\n\n"
        "Ustunlar: name, continent, density (zichlik, 2 kasrga yaxlitlangan).\n"
        "density kamayish tartibida.",
        "Бизнес: рынки с высокой плотностью населения и сильной экономикой.\n\n"
        "Из таблицы World выберите страны:\n"
        "• плотность населения (население / площадь) строго больше 90\n"
        "• И gdp не меньше 10 миллиардов\n\n"
        "Столбцы: name, continent, density (плотность, округлённая до 2 знаков).\n"
        "density по убыванию.",
        "Business: markets with high population density and a strong economy.\n\n"
        "From the World table, select countries where:\n"
        "• population density (population / area) is strictly greater than 90\n"
        "• AND gdp is at least 10 billion\n\n"
        "Columns: name, continent, density (density rounded to 2 decimals).\n"
        "density in descending order.",
    ),
    (
        "name, continent, density. Zichlik yuqori va iqtisod katta.",
        "name, continent, density. Высокая плотность и крупная экономика.",
        "name, continent, density. High density and a large economy.",
    ),
    (
        "population * 1.0 / area — kasr uchun",
        "population * 1.0 / area — чтобы была дробь",
        "population * 1.0 / area — for a decimal",
    ),
    (
        "ROUND(..., 2) AS density, ORDER BY density DESC",
        "ROUND(..., 2) AS density, ORDER BY density DESC",
        "ROUND(..., 2) AS density, ORDER BY density DESC",
    ),
    (
        "LeetCode 1757. Recyclable and Low Fat Products (Easy)\n\n"
        "Jadval: Products — product_id, low_fats, recyclable.\n"
        "low_fats va recyclable: 'Y' yoki 'N'.\n\n"
        "Ham kam yog‘li, ham qayta ishlanadigan mahsulotlarning product_id sini toping.\n"
        "Tartib ixtiyoriy.",
        "LeetCode 1757. Recyclable and Low Fat Products (Easy)\n\n"
        "Таблица: Products — product_id, low_fats, recyclable.\n"
        "low_fats и recyclable: 'Y' или 'N'.\n\n"
        "Найдите product_id продуктов, которые и низкожировые, и перерабатываемые.\n"
        "Порядок любой.",
        "LeetCode 1757. Recyclable and Low Fat Products (Easy)\n\n"
        "Table: Products — product_id, low_fats, recyclable.\n"
        "low_fats and recyclable: 'Y' or 'N'.\n\n"
        "Find the product_id of products that are both low-fat and recyclable.\n"
        "Order is optional.",
    ),
    (
        "Faqat product_id. Ikkalasi ham 'Y'.",
        "Только product_id. Оба поля 'Y'.",
        "Only product_id. Both are 'Y'.",
    ),
    (
        "Jadval: Products",
        "Таблица: Products",
        "Table: Products",
    ),
    (
        "LeetCode 595. Big Countries (Easy)\n\n"
        "Jadval: World — name, continent, area, population, gdp.\n\n"
        "Davlat katta hisoblanadi, agar:\n"
        "• maydoni kamida 3 000 000 km², YOKI\n"
        "• aholisi kamida 25 000 000 kishi.\n\n"
        "Katta davlatlarning name, population va area ustunlarini qaytaring.\n"
        "Tartib ixtiyoriy.",
        "LeetCode 595. Big Countries (Easy)\n\n"
        "Таблица: World — name, continent, area, population, gdp.\n\n"
        "Страна считается большой, если:\n"
        "• площадь не меньше 3 000 000 км², ИЛИ\n"
        "• население не меньше 25 000 000 человек.\n\n"
        "Верните столбцы name, population и area больших стран.\n"
        "Порядок любой.",
        "LeetCode 595. Big Countries (Easy)\n\n"
        "Table: World — name, continent, area, population, gdp.\n\n"
        "A country is big if:\n"
        "• its area is at least 3 000 000 km², OR\n"
        "• its population is at least 25 000 000 people.\n\n"
        "Return the name, population, and area columns of big countries.\n"
        "Order is optional.",
    ),
    (
        "name, population, area. Katta = maydon YOKI aholi chegarasi.",
        "name, population, area. Большая = порог площади ИЛИ населения.",
        "name, population, area. Big = the area OR population threshold.",
    ),
    (
        "Bittasi yetarli — OR",
        "Достаточно одного — OR",
        "One is enough — OR",
    ),
    (
        "Faqat so‘ralgan uchta ustun",
        "Только три запрошенных столбца",
        "Only the three requested columns",
    ),
    (
        "Products: kam yog‘li YOKI qayta ishlanadigan mahsulotlarning product_id sini qaytaring. Tartib ixtiyoriy.",
        "Products: верните product_id низкожировых ИЛИ перерабатываемых продуктов. Порядок любой.",
        "Products: return the product_id of low-fat OR recyclable products. Order is optional.",
    ),
    (
        "Faqat product_id. Bittasi yetarli.",
        "Только product_id. Достаточно одного условия.",
        "Only product_id. One condition is enough.",
    ),
    (
        "AND emas — OR",
        "Не AND — OR",
        "Not AND — OR",
    ),
    (
        "Kamida bitta 'Y'",
        "Хотя бы одна 'Y'",
        "At least one 'Y'",
    ),
    (
        "LeetCode 2356. Number of Unique Subjects Taught by Each Teacher (Easy)\n\n"
        "Jadval: Teacher — teacher_id, subject_id, dept_id.\n"
        "Bir fan turli kafedralarda o‘qitilishi mumkin.\n\n"
        "Har bir o‘qituvchi nechta turli fanni o‘qitishini hisoblang.\n"
        "Ustunlar: teacher_id, cnt. Tartib ixtiyoriy.",
        "LeetCode 2356. Number of Unique Subjects Taught by Each Teacher (Easy)\n\n"
        "Таблица: Teacher — teacher_id, subject_id, dept_id.\n"
        "Один предмет могут вести на разных кафедрах.\n\n"
        "Посчитайте, сколько разных предметов ведёт каждый преподаватель.\n"
        "Столбцы: teacher_id, cnt. Порядок любой.",
        "LeetCode 2356. Number of Unique Subjects Taught by Each Teacher (Easy)\n\n"
        "Table: Teacher — teacher_id, subject_id, dept_id.\n"
        "The same subject may be taught in different departments.\n\n"
        "Count how many different subjects each teacher teaches.\n"
        "Columns: teacher_id, cnt. Order is optional.",
    ),
    (
        "teacher_id va cnt. Har o‘qituvchi nechta turli fan.",
        "teacher_id и cnt. Сколько разных предметов у каждого преподавателя.",
        "teacher_id and cnt. How many different subjects per teacher.",
    ),
    ("COUNT(DISTINCT subject_id)", "COUNT(DISTINCT subject_id)", "COUNT(DISTINCT subject_id)"),
    ("GROUP BY teacher_id", "GROUP BY teacher_id", "GROUP BY teacher_id"),
    (
        "LeetCode 1741. Find Total Time Spent by Each Employee (Easy)\n\n"
        "Jadval: EmployeeAttendance — emp_id, event_day, in_time, out_time.\n"
        "Vaqt daqiqalarda: out_time - in_time.\n\n"
        "Har bir xodim har bir kunda jami qancha daqiqa ishlaganini hisoblang.\n"
        "Ustunlar: day (event_day), emp_id, total_time. Tartib ixtiyoriy.",
        "LeetCode 1741. Find Total Time Spent by Each Employee (Easy)\n\n"
        "Таблица: EmployeeAttendance — emp_id, event_day, in_time, out_time.\n"
        "Время в минутах: out_time - in_time.\n\n"
        "Посчитайте, сколько минут каждый сотрудник работал в каждый день.\n"
        "Столбцы: day (event_day), emp_id, total_time. Порядок любой.",
        "LeetCode 1741. Find Total Time Spent by Each Employee (Easy)\n\n"
        "Table: EmployeeAttendance — emp_id, event_day, in_time, out_time.\n"
        "Time in minutes: out_time - in_time.\n\n"
        "Count how many minutes each employee worked on each day.\n"
        "Columns: day (event_day), emp_id, total_time. Order is optional.",
    ),
    (
        "day, emp_id, total_time. Har xodim–kun juftligi.",
        "day, emp_id, total_time. Каждая пара сотрудник–день.",
        "day, emp_id, total_time. Each employee–day pair.",
    ),
    ("GROUP BY event_day, emp_id", "GROUP BY event_day, emp_id", "GROUP BY event_day, emp_id"),
    (
        "SUM(out_time - in_time) AS total_time, event_day AS day",
        "SUM(out_time - in_time) AS total_time, event_day AS day",
        "SUM(out_time - in_time) AS total_time, event_day AS day",
    ),
    (
        "Teacher: teacher_id, subject_id, dept_id.\n"
        "Har bir o‘qituvchi nechta unique fan o‘qitishini hisoblang.\n"
        "Ustunlar: teacher_id, cnt. teacher_id o‘sish tartibida.",
        "Teacher: teacher_id, subject_id, dept_id.\n"
        "Посчитайте, сколько уникальных предметов ведёт каждый преподаватель.\n"
        "Столбцы: teacher_id, cnt. teacher_id по возрастанию.",
        "Teacher: teacher_id, subject_id, dept_id.\n"
        "Count how many unique subjects each teacher teaches.\n"
        "Columns: teacher_id, cnt. teacher_id in ascending order.",
    ),
    (
        "teacher_id va cnt, teacher_id o‘sish tartibida.",
        "teacher_id и cnt, teacher_id по возрастанию.",
        "teacher_id and cnt, teacher_id ascending.",
    ),
    ("ORDER BY teacher_id", "ORDER BY teacher_id", "ORDER BY teacher_id"),
    (
        "Biznes: ijtimoiy tarmoqda kamida 2 obunachisi bor foydalanuvchilar.\n\n"
        "Followers: user_id, follower_id.\n"
        "Kamida 2 follower ga ega user_id larni toping.\n"
        "Ustun: user_id. O‘sish tartibida.",
        "Бизнес: пользователи соцсети хотя бы с 2 подписчиками.\n\n"
        "Followers: user_id, follower_id.\n"
        "Найдите user_id, у которых хотя бы 2 follower.\n"
        "Столбец: user_id. По возрастанию.",
        "Business: social-network users with at least 2 followers.\n\n"
        "Followers: user_id, follower_id.\n"
        "Find user_id values that have at least 2 followers.\n"
        "Column: user_id. Ascending order.",
    ),
    (
        "Faqat user_id, o‘sish tartibida. Kamida 2 obunachi.",
        "Только user_id, по возрастанию. Минимум 2 подписчика.",
        "Only user_id, ascending. At least 2 followers.",
    ),
    (
        "GROUP BY user_id, keyin HAVING",
        "GROUP BY user_id, затем HAVING",
        "GROUP BY user_id, then HAVING",
    ),
    ("ORDER BY user_id", "ORDER BY user_id", "ORDER BY user_id"),
    (
        "Courses jadvalidan kamida 3 talabasi bor sinflarni toping.\nUstun: class.",
        "Из таблицы Courses найдите классы минимум с 3 студентами.\nСтолбец: class.",
        "From the Courses table, find classes with at least 3 students.\nColumn: class.",
    ),
    (
        "Ustun: class. Kamida 3 talaba.",
        "Столбец: class. Минимум 3 студента.",
        "Column: class. At least 3 students.",
    ),
    (
        "Easy dagi chegara 5 edi — bu yerda 3",
        "В Easy порог был 5 — здесь 3",
        "In Easy the threshold was 5 — here it is 3",
    ),
    (
        "Eng ko‘p talabasi bor sinf(lar)ni toping.\n"
        "Agar tenglik bo‘lsa — barcha eng yuqori sinflarni qaytaring.\n"
        "Ustun: class.",
        "Найдите класс(ы) с наибольшим числом студентов.\n"
        "Если ничья — верните все самые большие классы.\n"
        "Столбец: class.",
        "Find the class(es) with the most students.\n"
        "If there is a tie — return all of the top classes.\n"
        "Column: class.",
    ),
    (
        "Ustun: class. Eng ko‘p talabali sinf(lar).",
        "Столбец: class. Класс(ы) с наибольшим числом студентов.",
        "Column: class. The class(es) with the most students.",
    ),
    (
        "Avval har sinfning sonini oling",
        "Сначала получите число по каждому классу",
        "First get the count for each class",
    ),
    (
        "Keyin shu sonlar ichidagi maksimumga tenglarini qoldiring",
        "Затем оставьте те, что равны максимуму среди этих чисел",
        "Then keep those equal to the maximum of those counts",
    ),
    (
        "Biznes: savdo hisobotiga mahsulot nomini qo‘shing.\n\n"
        "Sales va Product. Ustunlar: product_name, year, price.\n"
        "year o‘sish tartibida.",
        "Бизнес: добавьте название продукта в отчёт о продажах.\n\n"
        "Sales и Product. Столбцы: product_name, year, price.\n"
        "year по возрастанию.",
        "Business: add the product name to the sales report.\n\n"
        "Sales and Product. Columns: product_name, year, price.\n"
        "year in ascending order.",
    ),
    (
        "product_name, year, price. year o‘sish tartibida.",
        "product_name, year, price. year по возрастанию.",
        "product_name, year, price. year ascending.",
    ),
    (
        "Nom boshqa jadvalda — kalit orqali qo‘shing",
        "Название в другой таблице — добавьте по ключу",
        "The name is in another table — join on the key",
    ),
    (
        "Biznes: HR — bonus olmagan xodimlarni topish.\n\n"
        "Bonus jadvalida yozuvi yo‘q xodimlarning name va salary sini qaytaring.\n"
        "name o‘sish tartibida.",
        "Бизнес: HR — найти сотрудников без бонуса.\n\n"
        "Верните name и salary сотрудников, которых нет в таблице Bonus.\n"
        "name по возрастанию.",
        "Business: HR — find employees without a bonus.\n\n"
        "Return the name and salary of employees who have no row in Bonus.\n"
        "name in ascending order.",
    ),
    (
        "name, salary. Faqat bonussizlar. Ism o‘sish tartibida.",
        "name, salary. Только без бонуса. Имя по возрастанию.",
        "name, salary. Only those without a bonus. Name ascending.",
    ),
    (
        "Xodimlar asosiy — bonus yo‘qlar ham chapda qolsin",
        "Сотрудники основные — без бонуса тоже останьтесь слева",
        "Employees are the main side — those without a bonus should stay on the left",
    ),
    (
        "Bonus tomoni bo‘sh qatorlarni qoldiring",
        "Оставьте строки, где сторона Bonus пустая",
        "Keep rows where the Bonus side is empty",
    ),
    (
        "LeetCode 175 uslubi (chuqurroq).\n\n"
        "Har bir shaxs: firstName, lastName, city, state.\n"
        "Manzil bo‘lmasa — city/state NULL.\n"
        "personId o‘sish tartibida.\n"
        "Address da bor, Person da yo‘q odam chiqmasin.",
        "Стиль LeetCode 175 (глубже).\n\n"
        "Каждый человек: firstName, lastName, city, state.\n"
        "Если адреса нет — city/state NULL.\n"
        "personId по возрастанию.\n"
        "Человек, который есть в Address, но нет в Person, не должен появиться.",
        "LeetCode 175 style (deeper).\n\n"
        "Each person: firstName, lastName, city, state.\n"
        "If there is no address — city/state NULL.\n"
        "personId in ascending order.\n"
        "Someone in Address but not in Person must not appear.",
    ),
    (
        "firstName, lastName, city, state. Manzilsiz shaxslar ham. personId tartibida.",
        "firstName, lastName, city, state. В том числе без адреса. В порядке personId.",
        "firstName, lastName, city, state. People without an address too. In personId order.",
    ),
    (
        "Asosiy jadval — Person",
        "Основная таблица — Person",
        "The main table is Person",
    ),
    (
        "Manzili yo‘q odamda city/state bo‘sh qoladi",
        "У человека без адреса city/state останутся пустыми",
        "For a person without an address, city/state stay empty",
    ),
    (
        "LeetCode 183. Customers Who Never Order (Medium uslub).\n\n"
        "LCCustomers(id, name), LCOrders(id, customerId).\n"
        "Hech qachon buyurtma bermagan mijozlarning name sini qaytaring.\n"
        "name o‘sish tartibida.",
        "LeetCode 183. Customers Who Never Order (стиль Medium).\n\n"
        "LCCustomers(id, name), LCOrders(id, customerId).\n"
        "Верните name клиентов, которые никогда не заказывали.\n"
        "name по возрастанию.",
        "LeetCode 183. Customers Who Never Order (Medium style).\n\n"
        "LCCustomers(id, name), LCOrders(id, customerId).\n"
        "Return the name of customers who never placed an order.\n"
        "name in ascending order.",
    ),
    (
        "Ustun: name, o‘sish tartibida. Hech qachon buyurtma bermaganlar.",
        "Столбец: name, по возрастанию. Те, кто никогда не заказывал.",
        "Column: name, ascending. Those who never ordered.",
    ),
    (
        "Buyurtmalar ro‘yxatida yo‘q mijoz — ikki yo‘l bor: ro‘yxatda yo‘q, yoki bog‘lanmagan qator",
        "Клиент не в списке заказов — два пути: нет в списке, или несвязанная строка",
        "A customer not in the orders list — two paths: not in the list, or an unmatched row",
    ),
    (
        "Eng yuqori maoshli xodim(lar)ni toping. WITH dan foydalaning.\n"
        "Ustunlar: name, salary. Tenglik bo‘lsa — barchasi.",
        "Найдите сотрудника(ов) с самой высокой зарплатой. Используйте WITH.\n"
        "Столбцы: name, salary. При равенстве — все.",
        "Find the employee(s) with the highest salary. Use WITH.\n"
        "Columns: name, salary. If there is a tie — all of them.",
    ),
    (
        "name, salary. Eng yuqori maosh(lar).",
        "name, salary. Самая высокая зарплата (зарплаты).",
        "name, salary. The highest salary (salaries).",
    ),
    (
        "Avval maksimumni ajrating, keyin tenglarini oling",
        "Сначала отделите максимум, затем возьмите равных ему",
        "First isolate the maximum, then take those equal to it",
    ),
    (
        "Bir nechta xodim bir xil yuqori maoshda bo‘lishi mumkin",
        "Несколько сотрудников могут иметь одну и ту же высокую зарплату",
        "Several employees may share the same top salary",
    ),
    (
        "Har bir xodim uchun band ustunini yarating:\n"
        "• salary < 2000 → 'low'\n"
        "• 2000 <= salary < 4000 → 'mid'\n"
        "• aks holda → 'high'\n\n"
        "Ustunlar: name, salary, band. empId o‘sish tartibida.",
        "Создайте столбец band для каждого сотрудника:\n"
        "• salary < 2000 → 'low'\n"
        "• 2000 <= salary < 4000 → 'mid'\n"
        "• иначе → 'high'\n\n"
        "Столбцы: name, salary, band. empId по возрастанию.",
        "Create a band column for each employee:\n"
        "• salary < 2000 → 'low'\n"
        "• 2000 <= salary < 4000 → 'mid'\n"
        "• otherwise → 'high'\n\n"
        "Columns: name, salary, band. empId in ascending order.",
    ),
    (
        "name, salary, band. empId o‘sish tartibida.",
        "name, salary, band. empId по возрастанию.",
        "name, salary, band. empId ascending.",
    ),
    (
        "Uch tabaqa: past / o‘rta / yuqori — chegaralarni ketma-ket tekshiring",
        "Три уровня: низкий / средний / высокий — проверяйте границы по порядку",
        "Three bands: low / mid / high — check the borders in order",
    ),
    (
        "LeetCode 178. Rank Scores (Medium).\n\n"
        "Scores(id, score).\n"
        "Har bir ball uchun o‘rin: teng ballar bir xil o‘rin, keyingi o‘rin teshiksiz "
        "(1, 1, 2 — 1, 1, 3 emas).\n\n"
        "Ustunlar: score, rank. score kamayish tartibida.",
        "LeetCode 178. Rank Scores (Medium).\n\n"
        "Scores(id, score).\n"
        "Место для каждого балла: равные баллы — одно место, следующее без дырки "
        "(1, 1, 2 — не 1, 1, 3).\n\n"
        "Столбцы: score, rank. score по убыванию.",
        "LeetCode 178. Rank Scores (Medium).\n\n"
        "Scores(id, score).\n"
        "A place for each score: ties share a place, the next place has no gap "
        "(1, 1, 2 — not 1, 1, 3).\n\n"
        "Columns: score, rank. score descending.",
    ),
    (
        "score va rank. Eng yuqori ball — 1-o‘rin. Tartib tekshiriladi.",
        "score и rank. Самый высокий балл — 1-е место. Порядок проверяется.",
        "score and rank. Highest score — 1st place. Order is checked.",
    ),
    (
        "Tenglikda teshik ochilmasin",
        "При равенстве дырки быть не должно",
        "Ties should not open a gap",
    ),
    (
        "Oyna funksiyasi qatorni yo‘qotmaydi",
        "Оконная функция не теряет строку",
        "A window function does not drop the row",
    ),
    (
        "LeetCode 626. Exchange Seats.\n\n"
        "Seat(id, student). Juft–toq o‘rindiqlarni almashtiring:\n"
        "1↔2, 3↔4, ... Agar oxirgi id toq bo‘lsa — o‘zi qoladi.\n\n"
        "Ustunlar: id, student. id o‘sish tartibida.",
        "LeetCode 626. Exchange Seats.\n\n"
        "Seat(id, student). Поменяйте чётные и нечётные места:\n"
        "1↔2, 3↔4, ... Если последний id нечётный — он остаётся.\n\n"
        "Столбцы: id, student. id по возрастанию.",
        "LeetCode 626. Exchange Seats.\n\n"
        "Seat(id, student). Swap even–odd seats:\n"
        "1↔2, 3↔4, ... If the last id is odd — it stays.\n\n"
        "Columns: id, student. id in ascending order.",
    ),
    (
        "id, student. Juft–toq juftliklar almashtirilgan, id o‘sish tartibida.",
        "id, student. Чёт–нечет пары обменены, id по возрастанию.",
        "id, student. Even–odd pairs swapped, id ascending.",
    ),
    (
        "Toq o‘rindiq keyingi o‘quvchini oladi, juft — oldingisini",
        "Нечётное место берёт следующего ученика, чётное — предыдущего",
        "An odd seat takes the next student, an even seat takes the previous one",
    ),
    (
        "Oxirgi toq id o‘zgarmasligi mumkin",
        "Последний нечётный id может не измениться",
        "The last odd id may stay unchanged",
    ),
    (
        "LeetCode 596. Classes With at Least 5 Students (Easy)\n\n"
        "Jadval: Courses — student, class.\n"
        "Kamida 5 talabasi bor sinflarni toping. Tartib ixtiyoriy.",
        "LeetCode 596. Classes With at Least 5 Students (Easy)\n\n"
        "Таблица: Courses — student, class.\n"
        "Найдите классы минимум с 5 студентами. Порядок любой.",
        "LeetCode 596. Classes With at Least 5 Students (Easy)\n\n"
        "Table: Courses — student, class.\n"
        "Find classes with at least 5 students. Order is optional.",
    ),
    (
        "Ustun: class. Kamida 5 talabasi bor sinflar.",
        "Столбец: class. Классы минимум с 5 студентами.",
        "Column: class. Classes with at least 5 students.",
    ),
    (
        "Avval sinf bo‘yicha sanang, keyin kichik guruhlarni tashlang",
        "Сначала посчитайте по классу, затем отбросьте мелкие группы",
        "First count by class, then drop the small groups",
    ),
    (
        "LeetCode 1050. Actors and Directors Who Cooperated At Least Three Times (Easy)\n\n"
        "Jadval: ActorDirector — actor_id, director_id, timestamp.\n"
        "Kamida 3 marta birga ishlagan juftliklarni toping.",
        "LeetCode 1050. Actors and Directors Who Cooperated At Least Three Times (Easy)\n\n"
        "Таблица: ActorDirector — actor_id, director_id, timestamp.\n"
        "Найдите пары, которые работали вместе минимум 3 раза.",
        "LeetCode 1050. Actors and Directors Who Cooperated At Least Three Times (Easy)\n\n"
        "Table: ActorDirector — actor_id, director_id, timestamp.\n"
        "Find pairs that worked together at least 3 times.",
    ),
    (
        "actor_id va director_id. Kamida 3 marta birga ishlagan juftliklar.",
        "actor_id и director_id. Пары, которые работали вместе минимум 3 раза.",
        "actor_id and director_id. Pairs that worked together at least 3 times.",
    ),
    (
        "Juftlik — ikkita kalit. Sanash juftlik ichida bo‘lishi kerak",
        "Пара — два ключа. Считать нужно внутри пары",
        "A pair is two keys. The count must be inside the pair",
    ),
    (
        "LeetCode 619. Biggest Single Number (Easy)\n\n"
        "Jadval: MyNumbers — num.\n"
        "Faqat bir marta uchragan sonlar ichidan eng kattasini qaytaring.\n"
        "Agar yo‘q bo‘lsa — null (bu datasetda bor).",
        "LeetCode 619. Biggest Single Number (Easy)\n\n"
        "Таблица: MyNumbers — num.\n"
        "Верните самое большое среди чисел, которые встретились только один раз.\n"
        "Если таких нет — null (в этом наборе есть).",
        "LeetCode 619. Biggest Single Number (Easy)\n\n"
        "Table: MyNumbers — num.\n"
        "Return the largest among numbers that appear only once.\n"
        "If there is none — null (this dataset has one).",
    ),
    (
        "Bitta ustun: num. Yolg‘iz sonlar ichidagi eng katta.",
        "Один столбец: num. Самое большое среди одиноких чисел.",
        "One column: num. The largest among numbers that appear once.",
    ),
    (
        "Avval qaysi sonlar bir marta uchraydi — shuni toping",
        "Сначала найдите, какие числа встречаются один раз",
        "First find which numbers appear once",
    ),
    (
        "Keyin qolganlardan eng kattasini oling",
        "Затем возьмите самое большое из оставшихся",
        "Then take the largest of what’s left",
    ),
    (
        "LeetCode 1068. Product Sales Analysis I (Easy)\n\n"
        "Jadvallar: Sales, Product.\n"
        "Har bir sotuv uchun product_name, year, price ni qaytaring.",
        "LeetCode 1068. Product Sales Analysis I (Easy)\n\n"
        "Таблицы: Sales, Product.\n"
        "Для каждой продажи верните product_name, year, price.",
        "LeetCode 1068. Product Sales Analysis I (Easy)\n\n"
        "Tables: Sales, Product.\n"
        "For each sale, return product_name, year, price.",
    ),
    (
        "product_name, year, price. Sotuvga mahsulot nomini qo‘shing.",
        "product_name, year, price. Добавьте к продаже название продукта.",
        "product_name, year, price. Add the product name to the sale.",
    ),
    (
        "Nom boshqa jadvalda — kalit orqali bog‘lang",
        "Название в другой таблице — свяжите по ключу",
        "The name is in another table — join on the key",
    ),
    (
        "LeetCode 1378. Replace Employee ID With The Unique Identifier (Easy)\n\n"
        "Jadvallar: Employees (id, name), EmployeeUNI (id, unique_id).\n"
        "Har bir xodimning unique_id sini ko‘rsating; yo‘q bo‘lsa null.",
        "LeetCode 1378. Replace Employee ID With The Unique Identifier (Easy)\n\n"
        "Таблицы: Employees (id, name), EmployeeUNI (id, unique_id).\n"
        "Покажите unique_id каждого сотрудника; если нет — null.",
        "LeetCode 1378. Replace Employee ID With The Unique Identifier (Easy)\n\n"
        "Tables: Employees (id, name), EmployeeUNI (id, unique_id).\n"
        "Show each employee’s unique_id; if there is none — null.",
    ),
    (
        "unique_id va name. Identifikatori yo‘q xodimlar ham chiqsin.",
        "unique_id и name. Сотрудники без идентификатора тоже должны появиться.",
        "unique_id and name. Employees without an identifier should appear too.",
    ),
    (
        "Chapda barcha xodimlar qolishi kerak",
        "Слева должны остаться все сотрудники",
        "All employees must remain on the left",
    ),
    (
        "Mos kelmasa unique_id bo‘sh bo‘lishi normal",
        "Если нет пары, пустой unique_id — это нормально",
        "If there is no match, an empty unique_id is normal",
    ),
    (
        "LeetCode 577. Employee Bonus (Easy)\n\n"
        "Jadvallar: Employee, Bonus.\n"
        "Bonus &lt; 1000 yoki bonus umuman yo‘q xodimlarning name va bonusini qaytaring.",
        "LeetCode 577. Employee Bonus (Easy)\n\n"
        "Таблицы: Employee, Bonus.\n"
        "Верните name и bonus сотрудников, у которых bonus &lt; 1000 или бонуса нет вообще.",
        "LeetCode 577. Employee Bonus (Easy)\n\n"
        "Tables: Employee, Bonus.\n"
        "Return the name and bonus of employees whose bonus is &lt; 1000 or who have no bonus at all.",
    ),
    (
        "name va bonus. Bonus 1000 dan kam yoki umuman yo‘qlar.",
        "name и bonus. Бонус меньше 1000 или его вообще нет.",
        "name and bonus. Bonus under 1000 or no bonus at all.",
    ),
    (
        "Bonus yo‘q qatorni oddiy solishtirish yutib yuborishi mumkin",
        "Строку без бонуса обычное сравнение может проглотить",
        "A plain comparison can swallow a row with no bonus",
    ),
    (
        "NULL ni 0 deb o‘qish yoki alohida tekshirish",
        "Читать NULL как 0 или проверять отдельно",
        "Read NULL as 0 or check it separately",
    ),
    (
        "LeetCode 619 (qisman). MyNumbers dan faqat bir marta uchragan sonlarni toping.",
        "LeetCode 619 (частично). Из MyNumbers найдите числа, которые встретились только один раз.",
        "LeetCode 619 (partial). From MyNumbers, find numbers that appear only once.",
    ),
    (
        "Ustun: num. Faqat bir marta uchragan sonlar.",
        "Столбец: num. Числа, которые встретились только один раз.",
        "Column: num. Numbers that appear only once.",
    ),
    (
        "Guruhlab sanang, keyin soni 1 bo‘lganlarni qoldiring",
        "Сгруппируйте и посчитайте, затем оставьте те, у кого число = 1",
        "Group and count, then keep those whose count is 1",
    ),
    (
        "LeetCode 619. Subquery bilan: ichki so‘rovda yagona sonlar, tashqida MAX.",
        "LeetCode 619. Через подзапрос: внутри одинокие числа, снаружи MAX.",
        "LeetCode 619. With a subquery: unique numbers inside, MAX outside.",
    ),
    (
        "Ustun: num. Yolg‘iz sonlar ichidagi eng katta — ichki so‘rov bilan.",
        "Столбец: num. Самое большое среди одиноких чисел — через внутренний запрос.",
        "Column: num. The largest among once-only numbers — using an inner query.",
    ),
    (
        "Ichki natija — vaqtinchalik jadval",
        "Внутренний результат — временная таблица",
        "The inner result is a temporary table",
    ),
    (
        "Tashqi qism undan agregat oladi",
        "Внешняя часть берёт из неё агрегат",
        "The outer part takes an aggregate from it",
    ),
    (
        "Product jadvalidan Sales da hech bo‘lmaganda bir marta uchragan mahsulotlarni oling.",
        "Из таблицы Product возьмите продукты, которые хотя бы раз встречаются в Sales.",
        "From the Product table, take products that appear at least once in Sales.",
    ),
    (
        "product_id va product_name. Faqat sotilganlar.",
        "product_id и product_name. Только проданные.",
        "product_id and product_name. Only those that were sold.",
    ),
    (
        "Mahsulot ID si sotuvlar ro‘yxatida bormi — shu savol",
        "Есть ли ID продукта в списке продаж — вот вопрос",
        "Is the product ID in the sales list — that’s the question",
    ),
    (
        "LeetCode 619 ni WITH (CTE) yordamida yeching: yolg‘iz sonlar ichidan eng kattasi.",
        "Решите LeetCode 619 через WITH (CTE): самое большое среди одиноких чисел.",
        "Solve LeetCode 619 with WITH (CTE): the largest among once-only numbers.",
    ),
    (
        "Ustun: num. Avval yolg‘izlar, keyin eng katta.",
        "Столбец: num. Сначала одинокие, потом самое большое.",
        "Column: num. First the once-only numbers, then the largest.",
    ),
    (
        "Bosqichga nom bering, keyin undan o‘qing",
        "Дайте шагу имя, затем читайте из него",
        "Name the step, then read from it",
    ),
    (
        "596 ni CTE bilan: avval sanang, keyin kamida 5 talabali sinflarni qoldiring.",
        "596 через CTE: сначала посчитайте, затем оставьте классы минимум с 5 студентами.",
        "596 with a CTE: first count, then keep classes with at least 5 students.",
    ),
    (
        "Ustun: class.",
        "Столбец: class.",
        "Column: class.",
    ),
    (
        "CTE da son, tashqida filtr",
        "В CTE число, снаружи фильтр",
        "The count in the CTE, the filter outside",
    ),
    (
        "1050 ni CTE bilan yeching: juftliklar necha marta uchraganini avval hisoblang.",
        "Решите 1050 через CTE: сначала посчитайте, сколько раз встречалась пара.",
        "Solve 1050 with a CTE: first count how many times each pair appears.",
    ),
    (
        "actor_id, director_id. Kamida 3 marta.",
        "actor_id, director_id. Минимум 3 раза.",
        "actor_id, director_id. At least 3 times.",
    ),
    (
        "Sanashni CTE ichida qoldiring, tashqida faqat filtr",
        "Подсчёт оставьте внутри CTE, снаружи только фильтр",
        "Leave the counting inside the CTE, only filter outside",
    ),
    (
        "LeetCode 610. Triangle Judgement (Easy)\n\n"
        "Jadval: Triangle — x, y, z.\n"
        "Uchburchak bo‘la oladimi? Yes/No (CASE).",
        "LeetCode 610. Triangle Judgement (Easy)\n\n"
        "Таблица: Triangle — x, y, z.\n"
        "Может ли это быть треугольником? Yes/No (CASE).",
        "LeetCode 610. Triangle Judgement (Easy)\n\n"
        "Table: Triangle — x, y, z.\n"
        "Can it be a triangle? Yes/No (CASE).",
    ),
    (
        "x, y, z va triangle (Yes yoki No). Uchburchak tengsizligini tekshiring.",
        "x, y, z и triangle (Yes или No). Проверьте неравенство треугольника.",
        "x, y, z and triangle (Yes or No). Check the triangle inequality.",
    ),
    (
        "Har tomon qolgan ikkisining yig‘indisidan kichik bo‘lishi kerak",
        "Каждая сторона должна быть меньше суммы двух других",
        "Each side must be smaller than the sum of the other two",
    ),
    (
        "LeetCode 1873. Calculate Special Bonus (Easy)\n\n"
        "Jadval: Employee — empId, name, supervisor, salary.\n"
        "Bonus = salary, agar empId toq VA ism 'M' bilan boshlanmasa; aks holda 0.\n"
        "Ustunlar: empId, name (employee_id, bonus emas — shu dataset: empId, bonus).",
        "LeetCode 1873. Calculate Special Bonus (Easy)\n\n"
        "Таблица: Employee — empId, name, supervisor, salary.\n"
        "Bonus = salary, если empId нечётный И имя не начинается с 'M'; иначе 0.\n"
        "Столбцы: empId, name (не employee_id, bonus — в этом наборе: empId, bonus).",
        "LeetCode 1873. Calculate Special Bonus (Easy)\n\n"
        "Table: Employee — empId, name, supervisor, salary.\n"
        "Bonus = salary if empId is odd AND the name does not start with 'M'; otherwise 0.\n"
        "Columns: empId, name (not employee_id, bonus — this dataset: empId, bonus).",
    ),
    (
        "empId va bonus. Toq empId va M bilan boshlanmagan ismga maosh, qolganlarga 0.",
        "empId и bonus. Нечётный empId и имя не на M — зарплата, остальным 0.",
        "empId and bonus. Odd empId and a name not starting with M get salary, others 0.",
    ),
    (
        "Ikki shart birga; aks holda nol",
        "Два условия вместе; иначе ноль",
        "Both conditions together; otherwise zero",
    ),
    (
        "Natija yangi ustun — jadvalni o‘zgartirmaysiz",
        "Результат — новый столбец, таблицу не меняете",
        "The result is a new column — you do not change the table",
    ),
    (
        "Har bir make_name uchun qatorlar sonini COUNT bilan oling (CASE mashqi uchun tayyorgarlik).",
        "Для каждого make_name возьмите число строк через COUNT (подготовка к задаче на CASE).",
        "For each make_name, take the row count with COUNT (warmup for a CASE exercise).",
    ),
    (
        "make_name va cnt. Har brend necha qator.",
        "make_name и cnt. Сколько строк у каждого бренда.",
        "make_name and cnt. How many rows per brand.",
    ),
    (
        "Brend bo‘yicha guruhlab sanang",
        "Сгруппируйте и посчитайте по бренду",
        "Group and count by brand",
    ),
    (
        "2019-07-20 kundagi unikal user_id larni toping.",
        "Найдите уникальные user_id за день 2019-07-20.",
        "Find the unique user_id values on 2019-07-20.",
    ),
    (
        "Faqat user_id, takrorsiz. Faqat 2019-07-20.",
        "Только user_id, без повторов. Только 2019-07-20.",
        "Only user_id, distinct. Only 2019-07-20.",
    ),
    (
        "Aniq bir kun — sana tengligi",
        "Конкретный день — равенство даты",
        "One exact day — date equality",
    ),
    (
        "Bir kishi ikki marta kirsada, bir marta chiqsin",
        "Даже если человек зашёл дважды, пусть появится один раз",
        "Even if a person entered twice, they should appear once",
    ),
    (
        "LeetCode 1141. User Activity for the Past 30 Days I (Easy)\n\n"
        "activity_date 2019-07-27 dan oldingi 30 kun oralig‘ida (shu kun bilan)\n"
        "har bir kunda nechta unikal foydalanuvchi bo‘lganini toping.\n"
        "Ustunlar: day, active_users. Faqat faollik bo‘lgan kunlar.",
        "LeetCode 1141. User Activity for the Past 30 Days I (Easy)\n\n"
        "В интервале 30 дней до activity_date 2019-07-27 (включая этот день)\n"
        "найдите, сколько уникальных пользователей было в каждый день.\n"
        "Столбцы: day, active_users. Только дни, когда была активность.",
        "LeetCode 1141. User Activity for the Past 30 Days I (Easy)\n\n"
        "In the 30 days ending on activity_date 2019-07-27 (that day included)\n"
        "find how many unique users there were on each day.\n"
        "Columns: day, active_users. Only days that had activity.",
    ),
    (
        "day va active_users. Faqat faollik bo‘lgan kunlar, oxirgi 30 kun (27-iyul bilan).",
        "day и active_users. Только дни с активностью, последние 30 дней (включая 27 июля).",
        "day and active_users. Only days with activity, last 30 days (including 27 July).",
    ),
    (
        "Kun bo‘yicha guruhlang",
        "Сгруппируйте по дню",
        "Group by day",
    ),
    (
        "Bir kishini bir kunda bir marta sanang",
        "Одного человека в один день считайте один раз",
        "Count one person once per day",
    ),
    (
        "LeetCode 1693. Daily Leads and Partners (Easy)\n\n"
        "Jadval: DailySales — date_id, make_name, lead_id, partner_id.\n"
        "Har bir date_id + make_name uchun unikal lead va partner sonini toping.",
        "LeetCode 1693. Daily Leads and Partners (Easy)\n\n"
        "Таблица: DailySales — date_id, make_name, lead_id, partner_id.\n"
        "Для каждой пары date_id + make_name найдите число уникальных lead и partner.",
        "LeetCode 1693. Daily Leads and Partners (Easy)\n\n"
        "Table: DailySales — date_id, make_name, lead_id, partner_id.\n"
        "For each date_id + make_name, find the unique lead and partner counts.",
    ),
    (
        "date_id, make_name, unique_leads, unique_partners.",
        "date_id, make_name, unique_leads, unique_partners.",
        "date_id, make_name, unique_leads, unique_partners.",
    ),
    (
        "Kesim: kun va brend birga",
        "Срез: день и бренд вместе",
        "The slice: day and brand together",
    ),
    (
        "Lead va partnerni alohida, takrorsiz sanang",
        "Lead и partner считайте отдельно, без повторов",
        "Count lead and partner separately, without duplicates",
    ),
    (
        "Seat jadvalida id tartibida har qatorga tartib raqami (rn) qo‘ying. Barcha qatorlar qolsin.",
        "В таблице Seat поставьте каждой строке порядковый номер (rn) по id. Все строки должны остаться.",
        "In the Seat table, give each row a sequence number (rn) in id order. All rows must stay.",
    ),
    (
        "id, student, rn. id o‘sish tartibida.",
        "id, student, rn. id по возрастанию.",
        "id, student, rn. id ascending.",
    ),
    (
        "Guruhlab siqmang — har o‘quvchi o‘z qatorida qolsin",
        "Не сжимайте группировкой — каждый ученик остаётся на своей строке",
        "Do not squeeze with grouping — each student stays on their row",
    ),
    (
        "Oyna tartibi id bo‘yicha",
        "Порядок окна по id",
        "Window order is by id",
    ),
    (
        "Seat: har qatorga id tartibidagi o‘rin (rnk). Tenglik bo‘lsa RANK qoidasini eslang.",
        "Seat: каждой строке место по порядку id (rnk). При равенстве вспомните правило RANK.",
        "Seat: give each row a place in id order (rnk). If there is a tie, remember the RANK rule.",
    ),
    ("id, student, rnk", "id, student, rnk", "id, student, rnk"),
    (
        "Bu yerda id lar unique — RANK va ROW_NUMBER bir xil chiqishi mumkin",
        "Здесь id уникальны — RANK и ROW_NUMBER могут совпасть",
        "Here the id values are unique — RANK and ROW_NUMBER may look the same",
    ),
    (
        "Har qatorda jami o‘rindiqlar soni (total_seats) ko‘rinsin. Qatorlar yo‘qolmasin.",
        "В каждой строке пусть видно общее число мест (total_seats). Строки не должны пропасть.",
        "Each row should show the total number of seats (total_seats). Rows must not disappear.",
    ),
    ("id, student, total_seats", "id, student, total_seats", "id, student, total_seats"),
    (
        "Jami butun jadval uchun bir xil son",
        "Итог — одно и то же число для всей таблицы",
        "The total is the same number for the whole table",
    ),
    (
        "Guruhlab bitta qator qoldirmang",
        "Не оставляйте одну строку из-за группировки",
        "Do not collapse to one row with grouping",
    ),
    (
        "Person va Address. Shahar yo‘q bo‘lsa 'Noma’lum' deb yozing.",
        "Person и Address. Если города нет, напишите 'Noma’lum'.",
        "Person and Address. If there is no city, write 'Noma’lum'.",
    ),
    ("firstName, lastName, city", "firstName, lastName, city", "firstName, lastName, city"),
    (
        "Manzilsiz odamlar ham chiqishi kerak",
        "Люди без адреса тоже должны появиться",
        "People without an address should appear too",
    ),
    (
        "Bo‘sh joyni matn bilan almashtiring",
        "Замените пустое место текстом",
        "Replace the empty place with text",
    ),
    (
        "LeetCode 175. Combine Two Tables (Easy)\n\n"
        "Person va Address. Har shaxs: firstName, lastName, city, state. Manzil bo‘lmasa — bo‘sh (NULL).",
        "LeetCode 175. Combine Two Tables (Easy)\n\n"
        "Person и Address. Каждый человек: firstName, lastName, city, state. Если адреса нет — пусто (NULL).",
        "LeetCode 175. Combine Two Tables (Easy)\n\n"
        "Person and Address. Each person: firstName, lastName, city, state. If there is no address — empty (NULL).",
    ),
    (
        "firstName, lastName, city, state. Manzilsizlar ham.",
        "firstName, lastName, city, state. В том числе без адреса.",
        "firstName, lastName, city, state. Those without an address too.",
    ),
    (
        "Odamlar asosiy jadval — hech kim tushib qolmasin",
        "Люди — основная таблица, никто не должен выпасть",
        "People are the main table — nobody should drop out",
    ),
    (
        "Har bir mahsulot nomi necha marta sotilganini toping.",
        "Найдите, сколько раз продавалось каждое название продукта.",
        "Find how many times each product name was sold.",
    ),
    (
        "product_name va sales_cnt",
        "product_name и sales_cnt",
        "product_name and sales_cnt",
    ),
    (
        "Avval nomni bog‘lang, keyin nom bo‘yicha sanang",
        "Сначала свяжите название, затем посчитайте по названию",
        "First join the name, then count by name",
    ),
    (
        "customers dan kamida 2 mijozli shaharlarni toping.",
        "Из customers найдите города минимум с 2 клиентами.",
        "From customers, find cities with at least 2 customers.",
    ),
    (
        "Ustun: city.",
        "Столбец: city.",
        "Column: city.",
    ),
    (
        "Avval shahar bo‘yicha sanang, keyin kichiklarini tashlang",
        "Сначала посчитайте по городу, затем отбросьте мелкие",
        "First count by city, then drop the small ones",
    ),
    (
        "Kamida 3 ta tranzaksiyasi bor mijozlarni toping.",
        "Найдите клиентов минимум с 3 транзакциями.",
        "Find customers with at least 3 transactions.",
    ),
    (
        "Ustun: customer_id.",
        "Столбец: customer_id.",
        "Column: customer_id.",
    ),
    (
        "Mijoz bo‘yicha sanang, keyin chegaradan kichiklarini tashlang",
        "Посчитайте по клиенту, затем отбросьте тех, кто ниже порога",
        "Count by customer, then drop those below the threshold",
    ),
    (
        "Har to‘lov yonida mijoz ismi ko‘rinsin. Ism customers da, summa transactions da.",
        "Рядом с каждым платежом пусть видно имя клиента. Имя в customers, сумма в transactions.",
        "Each payment should show the customer name next to it. The name is in customers, the amount in transactions.",
    ),
    (
        "name va amount.",
        "name и amount.",
        "name and amount.",
    ),
    (
        "Ikki jadvalni umumiy kalit orqali bog‘lang",
        "Свяжите две таблицы по общему ключу",
        "Join the two tables on the shared key",
    ),
    (
        "O‘rtacha to‘lovdan qimmatroq tranzaksiyalarni toping.",
        "Найдите транзакции дороже среднего платежа.",
        "Find transactions more expensive than the average payment.",
    ),
    (
        "id va amount.",
        "id и amount.",
        "id and amount.",
    ),
    (
        "Avval o‘rtachani ichki savol qilib oling, keyin solishtiring",
        "Сначала получите среднее внутренним вопросом, затем сравните",
        "First get the average as an inner question, then compare",
    ),
    (
        "Avval faqat debit qatorlarni ajrating, keyin ularning yig‘indisini oling.",
        "Сначала отберите только строки debit, затем возьмите их сумму.",
        "First isolate only debit rows, then take their sum.",
    ),
    (
        "Ustun: total.",
        "Столбец: total.",
        "Column: total.",
    ),
    (
        "Bosqichga nom bering, keyin undan yig‘indi oling",
        "Дайте шагу имя, затем возьмите из него сумму",
        "Name the step, then take a sum from it",
    ),
    (
        "Har to‘lovga yorliq: 50 000 va undan katta — 'katta', qolgani — 'kichik'.",
        "Каждому платежу метка: 50 000 и больше — 'katta', остальные — 'kichik'.",
        "A label on each payment: 50 000 and above — 'katta', the rest — 'kichik'.",
    ),
    ("id, amount, label", "id, amount, label", "id, amount, label"),
    (
        "Shartli ustun — birinchi mos qoida ishlaydi",
        "Условный столбец — срабатывает первое подходящее правило",
        "A conditional column — the first matching rule wins",
    ),
    (
        "2024-yil mart oyidagi barcha tranzaksiyalar sonini toping.",
        "Найдите число всех транзакций за март 2024 года.",
        "Find the count of all transactions in March 2024.",
    ),
    (
        "Oy boshidan oxirigacha — ikkala chekka ham kirsin",
        "С начала месяца до конца — оба края входят",
        "From the start of the month to the end — both edges are included",
    ),
    (
        "Eng katta 3 to‘lov: id, amount va tartib raqami (rn). Qatorlar siqilmasin.",
        "Три самых крупных платежа: id, amount и порядковый номер (rn). Строки не сжимать.",
        "The largest 3 payments: id, amount, and a sequence number (rn). Do not squeeze the rows.",
    ),
    (
        "id, amount, rn — faqat birinchi 3 o‘rin",
        "id, amount, rn — только первые 3 места",
        "id, amount, rn — only the first 3 places",
    ),
    (
        "Summa kamayish tartibida raqamlang, keyin faqat 1–3 ni qoldiring",
        "Пронумеруйте по убыванию суммы, затем оставьте только 1–3",
        "Number in descending amount order, then keep only 1–3",
    ),
    (
        "Barcha tranzaksiyalar ichida debit ulushi necha foiz? Butun son (pct).",
        "Какой процент среди всех транзакций составляет debit? Целое число (pct).",
        "What percent of all transactions is debit? A whole number (pct).",
    ),
    (
        "Ustun: pct.",
        "Столбец: pct.",
        "Column: pct.",
    ),
    (
        "Debitni 1, qolganini 0 deb sanash mumkin",
        "Debit можно считать как 1, остальное как 0",
        "You can count debit as 1 and the rest as 0",
    ),
    (
        "Keyin 100 ga ko‘paytirib, jami soniga bo‘ling",
        "Затем умножьте на 100 и разделите на общее число",
        "Then multiply by 100 and divide by the total count",
    ),
    (
        "Faqat bitta ustun kerak — ism",
        "Нужен только один столбец — имя",
        "You only need one column — the name",
    ),
    (
        "Shaharni filtrlab oling",
        "Отфильтруйте по городу",
        "Filter by city",
    ),
    (
        "To‘lovlar boshqa jadvalda",
        "Платежи в другой таблице",
        "Payments are in another table",
    ),
    (
        "Operatsiya turini filtrlang",
        "Отфильтруйте тип операции",
        "Filter the operation type",
    ),
    (
        "Summa bo‘yicha tushing — eng katta tepada",
        "Спускайтесь по сумме — самое большое сверху",
        "Sort down by amount — largest on top",
    ),
    (
        "Avval mijoz bo‘yicha sanang, keyin kichiklarini tashlang",
        "Сначала посчитайте по клиенту, затем отбросьте мелких",
        "First count by customer, then drop the small ones",
    ),
    (
        "Barcha qatorlardagi summani bir songa yig‘ing",
        "Сложите сумму всех строк в одно число",
        "Add the amounts of all rows into one number",
    ),
    (
        "Ustun nomini total qiling",
        "Имя столбца сделайте total",
        "Make the column name total",
    ),
    (
        "Har mijoz uchun qatorlar soni",
        "Число строк по каждому клиенту",
        "The number of rows per customer",
    ),
    (
        "Ustun nomini cnt qiling",
        "Имя столбца сделайте cnt",
        "Make the column name cnt",
    ),
    (
        "Har mijoz uchun summalarni yig‘ing",
        "Сложите суммы по каждому клиенту",
        "Sum the amounts for each customer",
    ),
]


def _norm(text: str) -> str:
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


PUZZLES: dict[str, dict[str, str]] = {}
PUZZLES_NORM: dict[str, dict[str, str]] = {}
for uz, ru, en in PAIRS:
    row = {"ru": ru, "en": en}
    PUZZLES[uz] = row
    PUZZLES_NORM[_norm(uz)] = row
