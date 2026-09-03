"""Exact translations for lesson, puzzle, and test titles. SQL keywords stay in Latin."""

from __future__ import annotations


def S(cyrl: str, ru: str, en: str) -> dict[str, str]:
    return {"uz-cyrl": cyrl, "ru": ru, "en": en}


TITLE_STRINGS: dict[str, dict[str, str]] = {
    # Module 1 lectures + extras
    "SELECT nima?": S("SELECT нима?", "Что такое SELECT?", "What is SELECT?"),
    "Ustunlarni tanlash": S("Устунларни танлаш", "Выбор столбцов", "Selecting columns"),
    "Natijani o‘qish": S("Натижани ўқиш", "Чтение результата", "Reading the result"),
    "Mijoz ismlari": S("Мижоз исмлари", "Имена клиентов", "Customer names"),
    "Toshkent mijozlari": S("Тошкент мижозлари", "Клиенты из Ташкента", "Tashkent customers"),
    "Katta tranzaksiyalar": S("Катта транзакциялар", "Крупные транзакции", "Large transactions"),
    "SELECT, ustunlar va oddiy so‘rovlar.": S(
        "SELECT, устунлар ва оддий сўровлар.",
        "SELECT, столбцы и простые запросы.",
        "SELECT, columns, and simple queries.",
    ),
    "SQL asoslari uy vazifasi": S(
        "SQL асослари уй вазифаси",
        "Домашнее задание: основы SQL",
        "SQL basics homework",
    ),
    # Module 2
    "WHERE operatori": S("WHERE оператори", "Оператор WHERE", "The WHERE operator"),
    "Bir nechta shart": S("Бир нечта шарт", "Несколько условий", "Multiple conditions"),
    "Debit operatsiyalar": S("Дебит операциялар", "Дебетовые операции", "Debit operations"),
    "Summa bo‘yicha saralash": S("Сумма бўйича саралаш", "Сортировка по сумме", "Sort by amount"),
    "Faol mijozlar": S("Фаол мижозлар", "Активные клиенты", "Active customers"),
    "WHERE va ORDER BY.": S("WHERE ва ORDER BY.", "WHERE и ORDER BY.", "WHERE and ORDER BY."),
    "Filtrlash va saralash uy vazifasi": S(
        "Филтрлаш ва саралаш уй вазифаси",
        "Домашнее задание: фильтр и сортировка",
        "Filtering and sorting homework",
    ),
    # Module 3
    "SUM va AVG": S("SUM ва AVG", "SUM и AVG", "SUM and AVG"),
    "GROUP BY asoslari": S("GROUP BY асослари", "Основы GROUP BY", "GROUP BY basics"),
    "Jami summa": S("Жами сумма", "Общая сумма", "Total amount"),
    "Mijozlar bo‘yicha soni": S("Мижозлар бўйича сони", "Количество по клиентам", "Count by customer"),
    "Mijozlar yig‘indisi": S("Мижозлар йиғиндиси", "Сумма по клиентам", "Sum by customer"),
    "COUNT, SUM, AVG.": S("COUNT, SUM, AVG.", "COUNT, SUM, AVG.", "COUNT, SUM, AVG."),
    "Agregatsiyalar uy vazifasi": S(
        "Агрегатсиялар уй вазифаси",
        "Домашнее задание: агрегации",
        "Aggregations homework",
    ),
    # Advanced lectures
    "HAVING nima?": S("HAVING нима?", "Что такое HAVING?", "What is HAVING?"),
    "Ko‘p ustunli GROUP BY": S("Кўп устунли GROUP BY", "GROUP BY по нескольким столбцам", "GROUP BY with multiple columns"),
    "Agregat + filtr": S("Агрегат + фильтр", "Агрегат + фильтр", "Aggregate + filter"),
    "JOIN va NULL": S("JOIN ва NULL", "JOIN и NULL", "JOIN and NULL"),
    "WHERE subquery": S("WHERE subquery", "Подзапрос в WHERE", "WHERE subquery"),
    "FROM subquery": S("FROM subquery", "Подзапрос в FROM", "FROM subquery"),
    "IN / EXISTS": S("IN / EXISTS", "IN / EXISTS", "IN / EXISTS"),
    "CTE asoslari": S("CTE асослари", "Основы CTE", "CTE basics"),
    "Bir nechta CTE": S("Бир нечта CTE", "Несколько CTE", "Multiple CTEs"),
    "CTE amaliyoti": S("CTE амалиёти", "Практика CTE", "CTE practice"),
    "CASE SELECT da": S("CASE SELECT да", "CASE в SELECT", "CASE in SELECT"),
    "CASE agregatda": S("CASE агрегатда", "CASE в агрегации", "CASE in aggregates"),
    "Sana filtri": S("Сана филтри", "Фильтр по дате", "Date filter"),
    "Sana bo‘yicha GROUP BY": S("Сана бўйича GROUP BY", "GROUP BY по дате", "GROUP BY date"),
    "Kunlik ko‘rsatkichlar": S("Кунлик кўрсаткичлар", "Дневные показатели", "Daily metrics"),
    "NULL va COALESCE": S("NULL ва COALESCE", "NULL и COALESCE", "NULL and COALESCE"),
    "Combine Two Tables": S("Combine Two Tables", "Объединение двух таблиц", "Combine Two Tables"),
    "Yakuniy takrorlash": S("Якуний такрорлаш", "Итоговое повторение", "Final review"),
    "Guruhlash va HAVING filtri.": S(
        "Гуруҳлаш ва HAVING филтри.",
        "Группировка и фильтр HAVING.",
        "Grouping and the HAVING filter.",
    ),
    "INNER JOIN, LEFT JOIN, NULL.": S(
        "INNER JOIN, LEFT JOIN, NULL.",
        "INNER JOIN, LEFT JOIN, NULL.",
        "INNER JOIN, LEFT JOIN, NULL.",
    ),
    "WHERE/FROM subquery, IN.": S(
        "WHERE/FROM subquery, IN.",
        "Подзапрос в WHERE/FROM, IN.",
        "WHERE/FROM subquery, IN.",
    ),
    "WITH asoslari va amaliyot.": S(
        "WITH асослари ва амалиёт.",
        "Основы WITH и практика.",
        "WITH basics and practice.",
    ),
    "CASE WHEN shartlari.": S("CASE WHEN шартлари.", "Условия CASE WHEN.", "CASE WHEN conditions."),
    "Sana filtri va guruhlash.": S(
        "Сана филтри ва гуруҳлаш.",
        "Фильтр по дате и группировка.",
        "Date filter and grouping.",
    ),
    "ROW_NUMBER, RANK, window OVER.": S(
        "ROW_NUMBER, RANK, window OVER.",
        "ROW_NUMBER, RANK, window OVER.",
        "ROW_NUMBER, RANK, window OVER.",
    ),
    "NULL, COALESCE, murakkab JOIN.": S(
        "NULL, COALESCE, мураккаб JOIN.",
        "NULL, COALESCE, сложный JOIN.",
        "NULL, COALESCE, and advanced JOIN.",
    ),
    # Advanced extra exercises
    "2+ mijozli shaharlar": S("2+ мижозли шаҳарлар", "Города с 2+ клиентами", "Cities with 2+ customers"),
    "3+ tranzaksiyali mijozlar": S(
        "3+ транзакцияли мижозлар",
        "Клиенты с 3+ транзакциями",
        "Customers with 3+ transactions",
    ),
    "Mijoz va tranzaksiya": S("Мижоз ва транзакция", "Клиент и транзакция", "Customer and transaction"),
    "O‘rtachadan katta summalar": S(
        "Ўртачадан катта суммалар",
        "Суммы выше среднего",
        "Amounts above average",
    ),
    "CTE: debit yig‘indisi": S("CTE: дебит йиғиндиси", "CTE: сумма дебета", "CTE: debit total"),
    "Katta/kichik to‘lov": S("Катта/кичик тўлов", "Крупный/мелкий платёж", "Large/small payment"),
    "Summa bo‘yicha tartib": S("Сумма бўйича тартиб", "Порядок по сумме", "Rank by amount"),
    "Debit ulushi": S("Дебит улуши", "Доля дебета", "Debit share"),
    # Lesson-attached Easy practices
    "Easy · Mahsulot identifikatorlari": S(
        "Easy · Маҳсулот идентификаторлари",
        "Easy · Идентификаторы продуктов",
        "Easy · Product IDs",
    ),
    "Easy · Davlat ustunlarini tanlash": S(
        "Easy · Давлат устунларини танлаш",
        "Easy · Выбор столбцов стран",
        "Easy · Choosing country columns",
    ),
    "Easy · Takrorsiz qit’alar": S(
        "Easy · Такрорсиз қитъалар",
        "Easy · Уникальные континенты",
        "Easy · Distinct continents",
    ),
    "1683. Noto‘g‘ri tvitlar": S(
        "1683. Нотўғри твитлар",
        "1683. Некорректные твиты",
        "1683. Invalid tweets",
    ),
    "1148. Maqola ko‘rishlari I": S(
        "1148. Мақола кўришлари I",
        "1148. Просмотры статей I",
        "1148. Article views I",
    ),
    "1527. Muayyan tashxisli bemorlar": S(
        "1527. Муайян ташхисли беморлар",
        "1527. Пациенты с диагнозом",
        "1527. Patients with a condition",
    ),
    "Easy · Obunalar jami": S("Easy · Обуналар жами", "Easy · Всего подписок", "Easy · Total follows"),
    "Easy · Jami ish daqiqalari": S(
        "Easy · Жами иш дақиқалари",
        "Easy · Сумма рабочих минут",
        "Easy · Total work minutes",
    ),
    "1729. Obunachilar soni": S(
        "1729. Обуначилар сони",
        "1729. Число подписчиков",
        "1729. Followers count",
    ),
    # Medium/Hard extras
    "Medium — Katta davlatlar (qattiq shart)": S(
        "Medium — Катта давлатлар (қаттиқ шарт)",
        "Medium — Большие страны (жёсткое условие)",
        "Medium — Big countries (strict)",
    ),
    "Medium — Eng yuqori 2 reyting": S(
        "Medium — Энг юқори 2 рейтинг",
        "Medium — Два лучших рейтинга",
        "Medium — Top 2 ratings",
    ),
    "Hard — Yuqori zichlikli iqtisod": S(
        "Hard — Юқори зичликли иқтисод",
        "Hard — Экономика с высокой плотностью",
        "Hard — High-density economy",
    ),
    "1757. Qayta ishlanadigan va kam yog‘li mahsulotlar": S(
        "1757. Қайта ишланадиган ва кам ёғли маҳсулотлар",
        "1757. Перерабатываемые и низкожировые продукты",
        "1757. Recyclable and low-fat products",
    ),
    "595. Katta davlatlar": S("595. Катта давлатлар", "595. Большие страны", "595. Big countries"),
    "Medium — Kam yog‘li YOKI qayta ishlanadi": S(
        "Medium — Кам ёғли ЁКИ қайта ишланади",
        "Medium — Низкожировые ИЛИ перерабатываемые",
        "Medium — Low-fat OR recyclable",
    ),
    "2356. O‘qituvchi o‘qitgan unikal fanlar": S(
        "2356. Ўқитувчи ўқитан уникал фанлар",
        "2356. Уникальные предметы преподавателя",
        "2356. Unique subjects taught",
    ),
    "1741. Xodimning ishda o‘tkazgan vaqti": S(
        "1741. Ходимнинг ишда ўтказган вақти",
        "1741. Время сотрудника на работе",
        "1741. Find total time spent",
    ),
    "Medium — O‘qituvchi fanlari (tartib bilan)": S(
        "Medium — Ўқитувчи фанлари (тартиб билан)",
        "Medium — Предметы преподавателя (с порядком)",
        "Medium — Teacher subjects (ordered)",
    ),
    "Medium — Faol foydalanuvchilar": S(
        "Medium — Фаол фойдаланувчилар",
        "Medium — Активные пользователи",
        "Medium — Active users",
    ),
    "Medium — Kamida 3 talabali sinflar": S(
        "Medium — Камида 3 талабали синфлар",
        "Medium — Классы минимум с 3 студентами",
        "Medium — Classes with at least 3 students",
    ),
    "Hard — Eng ko‘p talabali sinf": S(
        "Hard — Энг кўп талабали синф",
        "Hard — Класс с наибольшим числом студентов",
        "Hard — Class with most students",
    ),
    "Medium — Sotuv + mahsulot nomi": S(
        "Medium — Сотув + маҳсулот номи",
        "Medium — Продажа + название продукта",
        "Medium — Sales + product name",
    ),
    "Medium — Bonussiz xodimlar": S(
        "Medium — Бонуссиз ходимлар",
        "Medium — Сотрудники без бонуса",
        "Medium — Employees without bonus",
    ),
    "Hard — Manzilsiz shaxslar ham": S(
        "Hard — Манзилсиз шахслар ҳам",
        "Hard — В том числе без адреса",
        "Hard — People without address too",
    ),
    "Medium — Buyurtma bermagan mijozlar": S(
        "Medium — Буюртма бермаган мижозлар",
        "Medium — Клиенты без заказов",
        "Medium — Customers who never ordered",
    ),
    "Medium — CTE: eng yuqori maosh": S(
        "Medium — CTE: энг юқори маош",
        "Medium — CTE: самая высокая зарплата",
        "Medium — CTE: highest salary",
    ),
    "Medium — Maosh diapazoni": S(
        "Medium — Маош диапазони",
        "Medium — Диапазон зарплат",
        "Medium — Salary range",
    ),
    "Medium — Ballarni reytinglash": S(
        "Medium — Балларни рейтинглаш",
        "Medium — Рейтинг баллов",
        "Medium — Rank scores",
    ),
    "Hard — O‘rinlarni almashtirish": S(
        "Hard — Ўринларни алмаштириш",
        "Hard — Обмен местами",
        "Hard — Swap seats",
    ),
    "596. Kamida 5 talabali sinflar": S(
        "596. Камида 5 талабали синфлар",
        "596. Классы минимум с 5 студентами",
        "596. Classes with at least 5 students",
    ),
    "1050. Aktyor va rejissyor (kamida 3)": S(
        "1050. Актёр ва режиссёр (камида 3)",
        "1050. Актёр и режиссёр (минимум 3)",
        "1050. Actor and director (at least 3)",
    ),
    "619. Eng katta yagona son": S(
        "619. Энг катта ягона сон",
        "619. Наибольшее уникальное число",
        "619. Biggest single number",
    ),
    "1068. Mahsulot sotuv tahlili I": S(
        "1068. Маҳсулот сотув таҳлили I",
        "1068. Анализ продаж продуктов I",
        "1068. Product sales analysis I",
    ),
    "1378. Xodim unique_id": S(
        "1378. Ходим unique_id",
        "1378. unique_id сотрудника",
        "1378. Employee unique_id",
    ),
    "577. Xodim bonusi": S("577. Ходим бонуси", "577. Бонус сотрудника", "577. Employee bonus"),
    "619. Yagona sonlar (HAVING)": S(
        "619. Ягона сонлар (HAVING)",
        "619. Уникальные числа (HAVING)",
        "619. Single numbers (HAVING)",
    ),
    "619. Eng katta yagona (subquery)": S(
        "619. Энг катта ягона (subquery)",
        "619. Наибольшее уникальное (подзапрос)",
        "619. Biggest single (subquery)",
    ),
    "Easy · Sotilgan mahsulotlar": S(
        "Easy · Сотилган маҳсулотлар",
        "Easy · Проданные продукты",
        "Easy · Products sold",
    ),
    "619. CTE bilan eng katta yagona": S(
        "619. CTE билан энг катта ягона",
        "619. Наибольшее уникальное через CTE",
        "619. Biggest single with CTE",
    ),
    "596. CTE bilan sinflar": S(
        "596. CTE билан синфлар",
        "596. Классы через CTE",
        "596. Classes with CTE",
    ),
    "1050. CTE bilan juftliklar": S(
        "1050. CTE билан жуфтликлар",
        "1050. Пары через CTE",
        "1050. Pairs with CTE",
    ),
    "610. Uchburchak tekshiruvi": S(
        "610. Учбурчак текшируви",
        "610. Проверка треугольника",
        "610. Triangle judgement",
    ),
    "1873. Maxsus bonus": S("1873. Махсус бонус", "1873. Расчёт бонуса", "1873. Calculate special bonus"),
    "Easy · CASE bilan sotuv sanash": S(
        "Easy · CASE билан сотув санаш",
        "Easy · Подсчёт продаж через CASE",
        "Easy · Count sales with CASE",
    ),
    "Easy · Kunlik faol foydalanuvchilar": S(
        "Easy · Кунлик фаол фойдаланувчилар",
        "Easy · Ежедневные активные пользователи",
        "Easy · Daily active users",
    ),
    "1141. 30 kunlik faollik": S(
        "1141. 30 кунлик фаоллик",
        "1141. Активность за 30 дней",
        "1141. User activity for 30 days",
    ),
    "1693. Kunlik lead va partner": S(
        "1693. Кунлик lead ва partner",
        "1693. Ежедневные lead и partner",
        "1693. Daily leads and partners",
    ),
    "Easy · ROW_NUMBER o‘rindiqlar": S(
        "Easy · ROW_NUMBER ўриндиқлар",
        "Easy · Места через ROW_NUMBER",
        "Easy · Seats with ROW_NUMBER",
    ),
    "Easy · RANK o‘rindiqlar": S(
        "Easy · RANK ўриндиқлар",
        "Easy · Места через RANK",
        "Easy · Seats with RANK",
    ),
    "Easy · Jami o‘rindiqlar (window)": S(
        "Easy · Жами ўриндиқлар (window)",
        "Easy · Сумма мест (window)",
        "Easy · Total seats (window)",
    ),
    "175. COALESCE bilan shahar": S(
        "175. COALESCE билан шаҳар",
        "175. Город через COALESCE",
        "175. City with COALESCE",
    ),
    "175. Ikki jadvalni birlashtirish": S(
        "175. Икки жадвални бирлаштириш",
        "175. Объединение двух таблиц",
        "175. Combine two tables",
    ),
    "Easy · Mahsulot bo‘yicha sotuvlar": S(
        "Easy · Маҳсулот бўйича сотувлар",
        "Easy · Продажи по продукту",
        "Easy · Sales by product",
    ),
    # Common skill-test titles
    "SELECT nima qiladi?": S("SELECT нима қилади?", "Что делает SELECT?", "What does SELECT do?"),
    "Modul bilim testi. To‘g‘ri javobni tanlang.": S(
        "Модул билим тести. Тўғри жавобни танланг.",
        "Тест знаний модуля. Выберите правильный ответ.",
        "Module skill test. Choose the correct answer.",
    ),
    # Homework instructions (full text — SQL keywords stay)
    (
        "1) SQL nima ekanini 4–5 jumlada yozing (RDBMS, jadval, qator, ustun).\n"
        "2) SELECT sintaksisini yozing.\n"
        "3) customers dan name va city oladigan so‘rov + DISTINCT city so‘rovi.\n"
        "Fayl: .txt, UTF-8."
    ): S(
        "1) SQL нима эканини 4–5 жумлада ёзинг (RDBMS, жадвал, қатор, устун).\n"
        "2) SELECT синтаксисини ёзинг.\n"
        "3) customers дан name ва city оладиган сўров + DISTINCT city сўрови.\n"
        "Файл: .txt, UTF-8.",
        "1) Напишите 4–5 предложений, что такое SQL (RDBMS, таблица, строка, столбец).\n"
        "2) Напишите синтаксис SELECT.\n"
        "3) Запрос, который берёт name и city из customers, плюс запрос DISTINCT city.\n"
        "Файл: .txt, UTF-8.",
        "1) In 4–5 sentences, write what SQL is (RDBMS, table, row, column).\n"
        "2) Write the SELECT syntax.\n"
        "3) A query that takes name and city from customers + a DISTINCT city query.\n"
        "File: .txt, UTF-8.",
    ),
    (
        "1) WHERE da matn va son qanday yozilishini tushuntiring.\n"
        "2) AND vs OR va qavs uchun 1 ta o‘z misolingiz.\n"
        "3) Debit + amount DESC to‘liq so‘rov.\n"
        "4) LIKE da % va _ farqi."
    ): S(
        "1) WHERE да матн ва сон қандай ёзилишини тушунтиринг.\n"
        "2) AND vs OR ва қавс учун 1 та ўз мисолингиз.\n"
        "3) Debit + amount DESC тўлиқ сўров.\n"
        "4) LIKE да % ва _ фарқи.",
        "1) Объясните, как в WHERE записывают текст и числа.\n"
        "2) Один свой пример для AND vs OR и скобок.\n"
        "3) Полный запрос: debit + amount DESC.\n"
        "4) Разница между % и _ в LIKE.",
        "1) Explain how text and numbers are written in WHERE.\n"
        "2) Give 1 example of your own for AND vs OR and parentheses.\n"
        "3) A full query: debit + amount DESC.\n"
        "4) The difference between % and _ in LIKE.",
    ),
    (
        "1) COUNT(*), COUNT(ustun), COUNT(DISTINCT) farqi.\n"
        "2) SUM va AVG misollari.\n"
        "3) GROUP BY so‘rovi: mijoz bo‘yicha COUNT va SUM.\n"
        "4) WHERE vs HAVING — qachon qaysi."
    ): S(
        "1) COUNT(*), COUNT(устун), COUNT(DISTINCT) фарқи.\n"
        "2) SUM ва AVG мисоллари.\n"
        "3) GROUP BY сўрови: мижоз бўйича COUNT ва SUM.\n"
        "4) WHERE vs HAVING — қачон қайси.",
        "1) Разница между COUNT(*), COUNT(столбец) и COUNT(DISTINCT).\n"
        "2) Примеры SUM и AVG.\n"
        "3) Запрос GROUP BY: COUNT и SUM по клиенту.\n"
        "4) WHERE vs HAVING — когда что использовать.",
        "1) The difference between COUNT(*), COUNT(column), and COUNT(DISTINCT).\n"
        "2) Examples of SUM and AVG.\n"
        "3) A GROUP BY query: COUNT and SUM by customer.\n"
        "4) WHERE vs HAVING — when to use which.",
    ),
    (
        "WHERE va HAVING farqini jadval qilib yozing (qachon, nimaga).\n"
        "Har bir shahar bo‘yicha COUNT va “kamida 2 mijoz” HAVING so‘rovini yozing.\n"
        "596 mashqini o‘z so‘zingiz bilan tushuntiring."
    ): S(
        "WHERE ва HAVING фарқини жадвал қилиб ёзинг (қачон, нимага).\n"
        "Ҳар бир шаҳар бўйича COUNT ва “камида 2 мижоз” HAVING сўровини ёзинг.\n"
        "596 машқини ўз сўзингиз билан тушунтиринг.",
        "WHERE и HAVING — запишите разницу таблицей (когда и зачем).\n"
        "Напишите запрос: COUNT по каждому городу и HAVING «минимум 2 клиента».\n"
        "Объясните задачу 596 своими словами.",
        "Write the difference between WHERE and HAVING as a table (when, why).\n"
        "Write a COUNT per city query and a HAVING “at least 2 customers” query.\n"
        "Explain exercise 596 in your own words.",
    ),
    (
        "INNER JOIN va LEFT JOIN ni 5 jumlada farqlang.\n"
        "Bitta kalit ustunli misol chizing (mijoz–to‘lov).\n"
        "“To‘lovi yo‘q mijozlar” ni LEFT JOIN + IS NULL bilan yozing."
    ): S(
        "INNER JOIN ва LEFT JOIN ни 5 жумлада фарқланг.\n"
        "Битта калит устунли мисол чизинг (мижоз–тўлов).\n"
        "“Тўлови йўқ мижозлар” ни LEFT JOIN + IS NULL билан ёзинг.",
        "За 5 предложений отличите INNER JOIN и LEFT JOIN.\n"
        "Нарисуйте пример с одним ключевым столбцом (клиент–платёж).\n"
        "Запишите «клиенты без платежей» через LEFT JOIN + IS NULL.",
        "In 5 sentences, contrast INNER JOIN and LEFT JOIN.\n"
        "Draw an example with one key column (customer–payment).\n"
        "Write “customers with no payments” using LEFT JOIN + IS NULL.",
    ),
    (
        "IN va EXISTS farqi.\n"
        "NOT IN da NULL xavfini 3 jumlada yozing.\n"
        "O‘rtachadan katta amount uchun subquery yozing."
    ): S(
        "IN ва EXISTS фарқи.\n"
        "NOT IN да NULL хавфини 3 жумлада ёзинг.\n"
        "Ўртачадан катта amount учун subquery ёзинг.",
        "Разница IN и EXISTS.\n"
        "За 3 предложения опишите опасность NULL в NOT IN.\n"
        "Напишите подзапрос для amount выше среднего.",
        "The difference between IN and EXISTS.\n"
        "In 3 sentences, explain the NULL risk with NOT IN.\n"
        "Write a subquery for amount above the average.",
    ),
    (
        "CTE nima ekanini W3 uslubida: nima bu, sintaksis, 1 misol.\n"
        "619 ni WITH bilan qayta yozing."
    ): S(
        "CTE нима эканини W3 услубида: нима бу, синтаксис, 1 мисол.\n"
        "619 ни WITH билан қайта ёзинг.",
        "Что такое CTE в стиле W3: что это, синтаксис, 1 пример.\n"
        "Перепишите 619 через WITH.",
        "What a CTE is, in W3 style: what it is, syntax, 1 example.\n"
        "Rewrite 619 using WITH.",
    ),
    (
        "CASE WHEN tartibini tushuntiring (birinchi rost shart).\n"
        "amount ni kichik/orta/katta ga ajrating.\n"
        "SUM(CASE WHEN ...) ni 1 misolda yozing."
    ): S(
        "CASE WHEN тартибини тушунтиринг (биринчи рост шарт).\n"
        "amount ни кичик/ўрта/катта га ажратинг.\n"
        "SUM(CASE WHEN ...) ни 1 мисолда ёзинг.",
        "Объясните порядок CASE WHEN (первое истинное условие).\n"
        "Разделите amount на kichik/orta/katta.\n"
        "Напишите SUM(CASE WHEN ...) в одном примере.",
        "Explain CASE WHEN order (first true condition).\n"
        "Split amount into small/medium/large.\n"
        "Write SUM(CASE WHEN ...) in 1 example.",
    ),
    (
        "Sana qanday formatda yoziladi?\n"
        "BETWEEN bilan mart oyi filtri.\n"
        "Kunlik COUNT(DISTINCT ...) g‘oyasini yozing."
    ): S(
        "Сана қандай форматда ёзилади?\n"
        "BETWEEN билан март ойи филтри.\n"
        "Кунлик COUNT(DISTINCT ...) ғоясини ёзинг.",
        "В каком формате записывается дата?\n"
        "Фильтр марта через BETWEEN.\n"
        "Опишите идею дневного COUNT(DISTINCT ...).",
        "How is a date written (format)?\n"
        "A March filter using BETWEEN.\n"
        "Write the idea of a daily COUNT(DISTINCT ...).",
    ),
    (
        "GROUP BY va window farqi (qator soni).\n"
        "ROW_NUMBER, RANK, DENSE_RANK jadvali.\n"
        "Seat uchun ROW_NUMBER so‘rovi."
    ): S(
        "GROUP BY ва window фарқи (қатор сони).\n"
        "ROW_NUMBER, RANK, DENSE_RANK жадвали.\n"
        "Seat учун ROW_NUMBER сўрови.",
        "Разница GROUP BY и window (число строк).\n"
        "Таблица ROW_NUMBER, RANK, DENSE_RANK.\n"
        "Запрос ROW_NUMBER для Seat.",
        "GROUP BY vs window (row count).\n"
        "A table of ROW_NUMBER, RANK, DENSE_RANK.\n"
        "A ROW_NUMBER query for Seat.",
    ),
    (
        "NULL nima, IS NULL nima uchun = NULL emas.\n"
        "COALESCE sintaksisi va 1 misol.\n"
        "Person LEFT JOIN Address ni tushuntiring."
    ): S(
        "NULL нима, IS NULL нима учун = NULL эмас.\n"
        "COALESCE синтаксиси ва 1 мисол.\n"
        "Person LEFT JOIN Address ни тушунтиринг.",
        "Что такое NULL и почему IS NULL, а не = NULL.\n"
        "Синтаксис COALESCE и 1 пример.\n"
        "Объясните Person LEFT JOIN Address.",
        "What NULL is, and why IS NULL — not = NULL.\n"
        "COALESCE syntax and 1 example.\n"
        "Explain Person LEFT JOIN Address.",
    ),
}
