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
    # English for Banking — UI titles (English learning body stays English)
    "English for Banking": S(
        "English for Banking",
        "English for Banking",
        "English for Banking",
    ),
    (
        "Bank sohasi uchun pre-intermediate ingliz tili: mijoz xizmati, hisoblar, kartalar, "
        "kredit, HR, KYC va ish yozishmalari. Grammatika, so‘z boyligi, o‘qish va gapirish "
        "mashqlari — SQL kursidagi kabi modullar, puzzle va bilim testlari bilan."
    ): S(
        (
            "Банк соҳаси учун pre-intermediate инглиз тили: мижоз хизмати, ҳисоблар, карталар, "
            "кредит, HR, KYC ва иш ёзишмалари. Грамматика, сўз бойлиги, ўқиш ва гапириш "
            "машқлари — SQL курсидаги каби модуллар, puzzle ва билим тестлари билан."
        ),
        (
            "Английский для банковской сферы (pre-intermediate): обслуживание клиентов, счета, карты, "
            "кредиты, HR, KYC и деловая переписка. Грамматика, лексика, чтение и говорение — "
            "модули, задания и тесты знаний, как в курсе SQL."
        ),
        (
            "Pre-intermediate English for banking: customer service, accounts, cards, "
            "credit, HR, KYC, and workplace writing. Grammar, vocabulary, reading, and speaking — "
            "with modules, puzzles, and skill tests like the SQL course."
        ),
    ),
    (
        "Bank sohasi uchun pre-intermediate ingliz tili (11 modul): asoslar, hisoblar, kartalar, "
        "kredit, FX/remittance, SME/trade finance, raqamli banking va firibgarlik, HR, mijoz xizmati, "
        "KYC/compliance, email va uchrashuvlar. Grammatika, so‘z boyligi, o‘qish va gapirish — "
        "puzzle va bilim testlari bilan."
    ): S(
        (
            "Банк соҳаси учун pre-intermediate инглиз тили (11 модул): асослар, ҳисоблар, карталар, "
            "кредит, FX/remittance, SME/trade finance, рақамли banking ва фирибгарлик, HR, мижоз хизмати, "
            "KYC/compliance, email ва учрашувлар. Грамматика, сўз бойлиги, ўқиш ва гапириш — "
            "puzzle ва билим тестлари билан."
        ),
        (
            "Английский для банковской сферы (pre-intermediate, 11 модулей): основы, счета, карты, "
            "кредиты, FX/переводы, SME/trade finance, цифровой банкинг и мошенничество, HR, "
            "обслуживание клиентов, KYC/compliance, email и встречи. Грамматика, лексика, чтение и говорение — "
            "с заданиями и тестами знаний."
        ),
        (
            "Pre-intermediate English for banking (11 modules): basics, accounts, cards, "
            "credit, FX/remittances, SME/trade finance, digital banking and fraud, HR, customer service, "
            "KYC/compliance, emails and meetings. Grammar, vocabulary, reading, and speaking — "
            "with puzzles and skill tests."
        ),
    ),
    "Bank asoslari (Bank basics)": S(
        "Банк асослари (Bank basics)",
        "Основы банка (Bank basics)",
        "Bank basics",
    ),
    "Hisoblar va depozitlar (Accounts)": S(
        "Ҳисоблар ва депозитлар (Accounts)",
        "Счета и депозиты (Accounts)",
        "Accounts & deposits",
    ),
    "Kartalar va to‘lovlar (Cards & payments)": S(
        "Карталар ва тўловлар (Cards & payments)",
        "Карты и платежи (Cards & payments)",
        "Cards & payments",
    ),
    "Kredit va qarzlar (Loans & credit)": S(
        "Кредит ва қарзлар (Loans & credit)",
        "Кредиты и займы (Loans & credit)",
        "Loans & credit",
    ),
    "Bankda HR (HR in banking)": S(
        "Банкда HR (HR in banking)",
        "HR в банке (HR in banking)",
        "HR in banking",
    ),
    "Mijozlarga xizmat (Customer service)": S(
        "Мижозларга хизмат (Customer service)",
        "Обслуживание клиентов (Customer service)",
        "Customer service",
    ),
    "KYC va compliance": S(
        "KYC ва compliance",
        "KYC и compliance",
        "KYC & compliance",
    ),
    "Email va uchrashuvlar (Emails & meetings)": S(
        "Email ва учрашувлар (Emails & meetings)",
        "Email и встречи (Emails & meetings)",
        "Emails & meetings",
    ),
    "Valyuta va pul o‘tkazmalari (FX & remittances)": S(
        "Валюта ва пул ўтказмалари (FX & remittances)",
        "Валюта и переводы (FX & remittances)",
        "FX & remittances",
    ),
    "Biznes va trade finance (SME & trade)": S(
        "Бизнес ва trade finance (SME & trade)",
        "Бизнес и trade finance (SME & trade)",
        "SME & trade finance",
    ),
    "Raqamli banking va firibgarlik (Digital & fraud)": S(
        "Рақамли banking ва фирибгарлик (Digital & fraud)",
        "Цифровой банкинг и мошенничество (Digital & fraud)",
        "Digital banking & fraud",
    ),
    # DevEnglish — UI titles (brand stays; subtitle lives in course description)
    "DevEnglish": S(
        "DevEnglish",
        "DevEnglish",
        "DevEnglish",
    ),
    "DevRussian": S(
        "DevRussian",
        "DevRussian",
        "DevRussian",
    ),
    "English for IT": S(
        "DevEnglish",
        "DevEnglish",
        "DevEnglish",
    ),
    "Русский для IT": S(
        "DevRussian",
        "DevRussian",
        "DevRussian",
    ),
    (
        "IT uchun ingliz tili — workplace, intervyu va akademik darslar (17 modul). "
        "Hardware, software/OS, networking, programming, databases, web, cloud/DevOps, "
        "cybersecurity, QA, Agile, tech support, documentation, team communication, email/career. "
        "Grammatika, so‘z boyligi, dialoglar, puzzle va bilim testlari bilan."
    ): S(
        (
            "IT учун инглиз тили — workplace, интервью ва академик дарслар (17 модул). "
            "Hardware, software/OS, networking, programming, databases, web, cloud/DevOps, "
            "cybersecurity, QA, Agile, tech support, documentation, team communication, email/career. "
            "Грамматика, сўз бойлиги, диалоглар, puzzle ва билим тестлари билан."
        ),
        (
            "Английский для IT — workplace, собеседование и академические уроки (17 модулей). "
            "Hardware, software/OS, networking, programming, databases, web, cloud/DevOps, "
            "кибербезопасность, QA, Agile, техподдержка, документация, командная коммуникация, email/карьера. "
            "Грамматика, лексика, диалоги, задания и тесты знаний."
        ),
        (
            "English for IT — workplace, interviews, and academic lessons (17 modules). "
            "Hardware, software/OS, networking, programming, databases, web, cloud/DevOps, "
            "cybersecurity, QA, Agile, tech support, documentation, team communication, email/career. "
            "Grammar, vocabulary, dialogues, puzzles, and skill tests."
        ),
    ),
    (
        "IT uchun ingliz tili. Pre-intermediate–intermediate (17 modul): workplace, hardware, "
        "software/OS, networking, programming, databases, web, cloud/DevOps, cybersecurity, "
        "QA/testing, Agile/Scrum, tech support, documentation, team communication, email/career, "
        "akademik ingliz tili, intervyu. Grammatika, so‘z boyligi, dialoglar, puzzle va bilim testlari bilan."
    ): S(
        "IT учун инглиз тили — workplace, интервью ва академик дарслар (17 модул).",
        "Английский для IT — workplace, собеседование и академические уроки (17 модулей).",
        "English for IT — workplace, interviews, and academic lessons (17 modules).",
    ),
    (
        "IT sohasi uchun pre-intermediate–intermediate ingliz tili (17 modul): IT workplace, "
        "hardware, software/OS, networking, programming, databases, web, cloud/DevOps, "
        "cybersecurity, QA/testing, Agile/Scrum, tech support, documentation, team communication, "
        "email/career, akademik ingliz tili, intervyu. "
        "Grammatika, so‘z boyligi, dialoglar, puzzle va bilim testlari bilan."
    ): S(
        "IT учун инглиз тили — workplace, интервью ва академик дарслар (17 модул).",
        "Английский для IT — workplace, собеседование и академические уроки (17 модулей).",
        "English for IT — workplace, interviews, and academic lessons (17 modules).",
    ),
    (
        "IT uchun rus tili. 17 modul: workplace, hardware, software/OS, networking, programming, "
        "databases, web, cloud/DevOps, cybersecurity, QA, Agile, tech support, documentation, "
        "team communication, email/career, akademik rus tili, intervyu. "
        "Grammatika, so‘z boyligi, dialoglar, puzzle va bilim testlari bilan."
    ): S(
        "IT учун рус тили — workplace, интервью ва академик дарслар (17 модул).",
        "Русский для IT — workplace, собеседование и академические уроки (17 модулей).",
        "Russian for IT — workplace, interviews, and academic lessons (17 modules).",
    ),
    (
        "IT sohasi uchun rus tili (17 modul): workplace, hardware, software/OS, networking, "
        "programming, databases, web, cloud/DevOps, cybersecurity, QA, Agile, tech support, "
        "documentation, team communication, email/career, akademik rus tili, intervyu. "
        "Grammatika, so‘z boyligi, dialoglar, puzzle va bilim testlari bilan."
    ): S(
        "IT учун рус тили — workplace, интервью ва академик дарслар (17 модул).",
        "Русский для IT — workplace, собеседование и академические уроки (17 модулей).",
        "Russian for IT — workplace, interviews, and academic lessons (17 modules).",
    ),
    "Akademik ingliz tili (Academic English for IT)": S(
        "Академик инглиз тили (Academic English for IT)",
        "Академический английский (Academic English for IT)",
        "Academic English for IT",
    ),
    "CS/IT talabalari uchun: abstract, paper o‘qish, iqtibos, hisobot va taqdimot.": S(
        "CS/IT талабалари учун: abstract, paper ўқиш, иқтибос, ҳисобот ва тақдимот.",
        "Для студентов CS/IT: abstract, чтение статей, цитирование, отчёт и презентация.",
        "For CS/IT students: abstracts, reading papers, citations, reports, and presentations.",
    ),
    "IT intervyu (Interview prep)": S(
        "IT интервью (Interview prep)",
        "IT-собеседование (Interview prep)",
        "IT interview prep",
    ),
    "IT suhbatiga tayyorgarlik: STAR, texnik savollar, salary va follow-up.": S(
        "IT суҳбатига тайёргарлик: STAR, техник саволлар, salary ва follow-up.",
        "Подготовка к IT-собеседованию: STAR, технические вопросы, salary и follow-up.",
        "Prep for IT interviews: STAR, technical questions, salary, and follow-up.",
    ),
    "IT asoslari (IT workplace basics)": S(
        "IT асослари (IT workplace basics)",
        "Основы IT (IT workplace basics)",
        "IT workplace basics",
    ),
    "Qurilmalar (Hardware & devices)": S(
        "Қурилмалар (Hardware & devices)",
        "Оборудование (Hardware & devices)",
        "Hardware & devices",
    ),
    "Dasturiy ta’minot va OS (Software & OS)": S(
        "Дастурий таъминот ва OS (Software & OS)",
        "ПО и ОС (Software & OS)",
        "Software & OS",
    ),
    "Tarmoq va Internet (Networking)": S(
        "Тармоқ ва Интернет (Networking)",
        "Сети и Интернет (Networking)",
        "Networking",
    ),
    "Dasturlash inglizchasi (Programming English)": S(
        "Дастурлаш инглизчаси (Programming English)",
        "Английский для программирования",
        "Programming English",
    ),
    "Ma’lumotlar bazasi (Databases)": S(
        "Маълумотлар базаси (Databases)",
        "Базы данных (Databases)",
        "Databases",
    ),
    "Veb dasturlash (Web development)": S(
        "Веб дастурлаш (Web development)",
        "Веб-разработка (Web development)",
        "Web development",
    ),
    "Cloud va DevOps": S(
        "Cloud ва DevOps",
        "Cloud и DevOps",
        "Cloud & DevOps",
    ),
    "Kiberxavfsizlik (Cybersecurity)": S(
        "Киберхавфсизлик (Cybersecurity)",
        "Кибербезопасность (Cybersecurity)",
        "Cybersecurity",
    ),
    "QA va testlash (QA & testing)": S(
        "QA ва тестлаш (QA & testing)",
        "QA и тестирование (QA & testing)",
        "QA & testing",
    ),
    "Agile va Scrum": S(
        "Agile ва Scrum",
        "Agile и Scrum",
        "Agile & Scrum",
    ),
    "Texnik yordam (Tech support)": S(
        "Техник ёрдам (Tech support)",
        "Техподдержка (Tech support)",
        "Tech support",
    ),
    "Hujjatlar (Documentation)": S(
        "Ҳужжатлар (Documentation)",
        "Документация (Documentation)",
        "Documentation",
    ),
    "Jamoa aloqasi (Team communication)": S(
        "Жамоа алоқаси (Team communication)",
        "Командная коммуникация (Team communication)",
        "Team communication",
    ),
    "Email va karyera (Emails & career)": S(
        "Email ва карьера (Emails & career)",
        "Email и карьера (Emails & career)",
        "Emails & career",
    ),
    # English for IT — module descriptions
    "IT workplace, rollar, ofis va remote ish uchun asosiy so‘zlar.": S(
        "IT workplace, роллар, офис ва remote иш учун асосий сўзлар.",
        "Базовая лексика IT workplace, роли, офис и удалёнка.",
        "Core vocabulary for IT workplace, roles, office, and remote work.",
    ),
    "Kompyuter qismlari, periferiya va texnik xususiyatlar.": S(
        "Компьютер қисмлари, периферия ва техник хусусиятлар.",
        "Комплектующие, периферия и технические характеристики.",
        "Computer parts, peripherals, and specs.",
    ),
    "Operatsion tizim, ilovalar, litsenziya, o‘rnatish va yangilash.": S(
        "Операцион тизим, иловалар, лицензия, ўрнатиш ва янгилаш.",
        "ОС, приложения, лицензии, установка и обновление.",
        "OS, apps, licenses, install, and updates.",
    ),
    "Tarmoq asoslari, protokollar va Wi-Fi muammolarini hal qilish.": S(
        "Тармоқ асослари, протоколлар ва Wi-Fi муаммоларини ҳал қилиш.",
        "Основы сетей, протоколы и решение проблем Wi‑Fi.",
        "Networking basics, protocols, and Wi‑Fi troubleshooting.",
    ),
    "Kod so‘z boyligi, algoritmlar haqida gapirish va Git asoslari.": S(
        "Код сўз бойлиги, алгоритмлар ҳақида гапириш ва Git асослари.",
        "Лексика кода, разговор об алгоритмах и основы Git.",
        "Coding vocabulary, talking about algorithms, and Git basics.",
    ),
    "DB tushunchalari, SQL haqida gapirish va ma’lumot maxfiyligi.": S(
        "DB тушунчалари, SQL ҳақида гапириш ва маълумот махфийлиги.",
        "Понятия БД, разговор о SQL и конфиденциальность данных.",
        "DB concepts, talking about SQL, and data privacy.",
    ),
    "Frontend/backend, API/HTTP va veb deploy haqida inglizcha.": S(
        "Frontend/backend, API/HTTP ва веб deploy ҳақида инглизча.",
        "Frontend/backend, API/HTTP и веб-deploy на английском.",
        "English for frontend/backend, API/HTTP, and web deploy.",
    ),
    "Cloud asoslari, konteynerlar/CI va monitoring.": S(
        "Cloud асослари, контейнерлар/CI ва мониторинг.",
        "Основы cloud, контейнеры/CI и мониторинг.",
        "Cloud basics, containers/CI, and monitoring.",
    ),
    "Xavfsizlik asoslari, parol/MFA va phishingdan himoya.": S(
        "Хавфсизлик асослари, парол/MFA ва phishingдан ҳимоя.",
        "Основы безопасности, пароль/MFA и защита от phishing.",
        "Security basics, password/MFA, and phishing defense.",
    ),
    "QA rollari, bug report va test turlari.": S(
        "QA роллари, bug report ва тест турлари.",
        "Роли QA, bug report и виды тестов.",
        "QA roles, bug reports, and test types.",
    ),
    "Agile qiymatlari, Scrum voqealari va user story’lar.": S(
        "Agile қийматлари, Scrum воқеалари ва user story’лар.",
        "Ценности Agile, события Scrum и user story.",
        "Agile values, Scrum events, and user stories.",
    ),
    "Ticket tili, troubleshooting qadamlari va escalate qilish.": S(
        "Ticket тили, troubleshooting қадамлари ва escalate қилиш.",
        "Язык тикетов, шаги troubleshooting и escalate.",
        "Ticket language, troubleshooting steps, and escalation.",
    ),
    "README/spec, user guide va change log yozish inglizchasi.": S(
        "README/spec, user guide ва change log ёзиш инглизчаси.",
        "Английский для README/spec, user guide и changelog.",
        "English for README/spec, user guides, and changelogs.",
    ),
    "Standup inglizchasi, Slack/Teams va muloyim feedback.": S(
        "Standup инглизчаси, Slack/Teams ва мулойим feedback.",
        "Английский для standup, Slack/Teams и мягкий feedback.",
        "Standup English, Slack/Teams, and polite feedback.",
    ),
    "Email shablonlari, IT intervyu va LinkedIn/CV inglizchasi.": S(
        "Email шаблонлари, IT интервью ва LinkedIn/CV инглизчаси.",
        "Шаблоны email, IT-интервью и LinkedIn/CV на английском.",
        "Email templates, IT interviews, and LinkedIn/CV English.",
    ),
    (
        "IT uchun rus tili — workplace, intervyu va akademik darslar (17 modul). "
        "Hardware, software/OS, networking, programming, databases, web, cloud/DevOps, "
        "cybersecurity, QA, Agile, tech support, documentation, team communication, email/career. "
        "Grammatika, so‘z boyligi, dialoglar, puzzle va bilim testlari bilan."
    ): S(
        (
            "IT учун рус тили — workplace, интервью ва академик дарслар (17 модул). "
            "Hardware, software/OS, networking, programming, databases, web, cloud/DevOps, "
            "cybersecurity, QA, Agile, tech support, documentation, team communication, email/career. "
            "Грамматика, сўз бойлиги, диалоглар, puzzle ва билим тестлари билан."
        ),
        (
            "Русский для IT — workplace, собеседование и академические уроки (17 модулей). "
            "Hardware, software/OS, networking, programming, databases, web, cloud/DevOps, "
            "кибербезопасность, QA, Agile, техподдержка, документация, командная коммуникация, email/карьера. "
            "Грамматика, лексика, диалоги, задания и тесты знаний."
        ),
        (
            "Russian for IT — workplace, interviews, and academic lessons (17 modules). "
            "Hardware, software/OS, networking, programming, databases, web, cloud/DevOps, "
            "cybersecurity, QA, Agile, tech support, documentation, team communication, email/career. "
            "Grammar, vocabulary, dialogues, puzzles, and skill tests."
        ),
    ),
    "IT asoslari (Основы IT)": S(
        "IT асослари (Основы IT)",
        "Основы IT",
        "IT basics (Russian)",
    ),
    "Qurilmalar (Оборудование)": S(
        "Қурилмалар (Оборудование)",
        "Оборудование",
        "Hardware (Russian)",
    ),
    "ПО и ОС (Программное обеспечение и ОС)": S(
        "ПО и ОС (Программное обеспечение и ОС)",
        "ПО и ОС",
        "Software & OS (Russian)",
    ),
    "Сети (Networking)": S(
        "Сети (Networking)",
        "Сети (Networking)",
        "Networking (Russian)",
    ),
    "Язык программиста (Programming)": S(
        "Язык программиста (Programming)",
        "Язык программиста",
        "Programming language (Russian)",
    ),
    "Базы данных (Databases)": S(
        "Базы данных (Databases)",
        "Базы данных",
        "Databases (Russian)",
    ),
    "Веб (Web)": S(
        "Веб (Web)",
        "Веб",
        "Web (Russian)",
    ),
    "Cloud и DevOps": S(
        "Cloud и DevOps",
        "Cloud и DevOps",
        "Cloud & DevOps (Russian)",
    ),
    "Kiberxavfsizlik (Кибербезопасность)": S(
        "Киберхавфсизлик (Кибербезопасность)",
        "Кибербезопасность",
        "Cybersecurity (Russian)",
    ),
    "QA ва тестлаш (QA и тестирование)": S(
        "QA ва тестлаш (QA и тестирование)",
        "QA и тестирование",
        "QA & testing (Russian)",
    ),
    "Texnik yordam (Техподдержка)": S(
        "Техник ёрдам (Техподдержка)",
        "Техподдержка",
        "Tech support (Russian)",
    ),
    "Hujjatlar (Документация)": S(
        "Ҳужжатлар (Документация)",
        "Документация",
        "Documentation (Russian)",
    ),
    "Jamoa aloqasi (Командная коммуникация)": S(
        "Жамоа алоқаси (Командная коммуникация)",
        "Командная коммуникация",
        "Team communication (Russian)",
    ),
    "Email va karyera (Email и карьера)": S(
        "Email ва карьера (Email и карьера)",
        "Email и карьера",
        "Email & career (Russian)",
    ),
    "Akademik rus tili (Академический русский для IT)": S(
        "Академик рус тили (Академический русский для IT)",
        "Академический русский для IT",
        "Academic Russian for IT",
    ),
    "IT intervyu (Подготовка к собеседованию)": S(
        "IT интервью (Подготовка к собеседованию)",
        "Подготовка к собеседованию",
        "Interview prep (Russian)",
    ),
    "IT workplace, rollar, ofis va remote ish uchun asosiy ruscha so‘zlar.": S(
        "IT workplace, роллар, офис ва remote иш учун асосий русча сўзлар.",
        "Базовая русская лексика IT workplace, роли, офис и удалёнка.",
        "Core Russian vocabulary for IT workplace, roles, office, and remote work.",
    ),
    "Компьютер қисмлари, периферия ва техник хусусиятлар — русча.": S(
        "Компьютер қисмлари, периферия ва техник хусусиятлар — русча.",
        "Комплектующие, периферия и характеристики — на русском.",
        "Computer parts, peripherals, and specs — in Russian.",
    ),
    "Operatsion tizim, ilovalar, litsenziya, o‘rnatish va yangilash — ruscha.": S(
        "Операцион тизим, иловалар, лицензия, ўрнатиш ва янгилаш — русча.",
        "ОС, приложения, лицензии, установка и обновление — на русском.",
        "OS, apps, licenses, install, and updates — in Russian.",
    ),
    "Tarmoq asoslari, protokollar va Wi‑Fi muammolari — ruscha.": S(
        "Тармоқ асослари, протоколлар ва Wi‑Fi муаммолари — русча.",
        "Основы сетей, протоколы и проблемы Wi‑Fi — на русском.",
        "Networking basics, protocols, and Wi‑Fi issues — in Russian.",
    ),
    "Kod so‘z boyligi, algoritmlar va Git asoslari — ruscha.": S(
        "Код сўз бойлиги, алгоритмлар ва Git асослари — русча.",
        "Лексика кода, алгоритмы и основы Git — на русском.",
        "Coding vocabulary, algorithms, and Git basics — in Russian.",
    ),
    "DB tushunchalari, SQL haqida gapirish va maxfiylik — ruscha.": S(
        "DB тушунчалари, SQL ҳақида гапириш ва махфийлик — русча.",
        "Понятия БД, разговор о SQL и конфиденциальность — на русском.",
        "DB concepts, talking about SQL, and privacy — in Russian.",
    ),
    "Frontend/backend, API/HTTP va deploy — ruscha.": S(
        "Frontend/backend, API/HTTP ва deploy — русча.",
        "Frontend/backend, API/HTTP и deploy — на русском.",
        "Frontend/backend, API/HTTP, and deploy — in Russian.",
    ),
    "Cloud asoslari, konteynerlar/CI va monitoring — ruscha.": S(
        "Cloud асослари, контейнерлар/CI ва мониторинг — русча.",
        "Основы cloud, контейнеры/CI и мониторинг — на русском.",
        "Cloud basics, containers/CI, and monitoring — in Russian.",
    ),
    "Xavfsizlik asoslari, parol/MFA va phishing — ruscha.": S(
        "Хавфсизлик асослари, парол/MFA ва phishing — русча.",
        "Основы безопасности, пароль/MFA и phishing — на русском.",
        "Security basics, password/MFA, and phishing — in Russian.",
    ),
    "QA rollari, bug report va test turlari — ruscha.": S(
        "QA роллари, bug report ва тест турлари — русча.",
        "Роли QA, bug report и виды тестов — на русском.",
        "QA roles, bug reports, and test types — in Russian.",
    ),
    "Agile qiymatlari, Scrum voqealari va user story — ruscha.": S(
        "Agile қийматлари, Scrum воқеалари ва user story — русча.",
        "Ценности Agile, события Scrum и user story — на русском.",
        "Agile values, Scrum events, and user stories — in Russian.",
    ),
    "Ticket tili, troubleshooting va escalate — ruscha.": S(
        "Ticket тили, troubleshooting ва escalate — русча.",
        "Язык тикетов, troubleshooting и escalate — на русском.",
        "Ticket language, troubleshooting, and escalate — in Russian.",
    ),
    "README/spec, user guide va changelog — ruscha.": S(
        "README/spec, user guide ва changelog — русча.",
        "README/spec, user guide и changelog — на русском.",
        "README/spec, user guides, and changelogs — in Russian.",
    ),
    "Standup, Slack/Teams va muloyim feedback — ruscha.": S(
        "Standup, Slack/Teams ва мулойим feedback — русча.",
        "Standup, Slack/Teams и мягкий feedback — на русском.",
        "Standup, Slack/Teams, and polite feedback — in Russian.",
    ),
    "Email shablonlari, intervyu asoslari va LinkedIn/CV — ruscha.": S(
        "Email шаблонлари, интервью асослари ва LinkedIn/CV — русча.",
        "Шаблоны email, основы интервью и LinkedIn/CV — на русском.",
        "Email templates, interview basics, and LinkedIn/CV — in Russian.",
    ),
    "CS/IT talabalari uchun: abstract, iqtibos, hisobot va taqdimot — ruscha.": S(
        "CS/IT талабалари учун: abstract, иқтибос, ҳисобот ва тақдимот — русча.",
        "Для студентов CS/IT: abstract, цитирование, отчёт и презентация — на русском.",
        "For CS/IT students: abstracts, citations, reports, and presentations — in Russian.",
    ),
    "IT suhbatiga tayyorgarlik: STAR, texnik savollar, salary va follow-up — ruscha.": S(
        "IT суҳбатига тайёргарлик: STAR, техник саволлар, salary ва follow-up — русча.",
        "Подготовка к IT-собеседованию: STAR, технические вопросы, salary и follow-up — на русском.",
        "Prep for IT interviews: STAR, technical questions, salary, and follow-up — in Russian.",
    ),
    # Module descriptions
    "Bankda ishlash, rollar, salomlashish va asosiy so‘zlar.": S(
        "Банкда ишлаш, роллар, саломлашиш ва асосий сўзлар.",
        "Работа в банке, роли, приветствия и базовая лексика.",
        "Working in a bank, roles, greetings, and basic vocabulary.",
    ),
    "Account types, deposit, withdraw, balance.": S(
        "Ҳисоб турлари, депозит, ечиш, баланс.",
        "Типы счетов, депозит, снятие, баланс.",
        "Account types, deposit, withdraw, balance.",
    ),
    "Debit/credit cards, transfers, ATM, online payments.": S(
        "Дебет/кредит карталар, ўтказмалар, ATM, онлайн тўловлар.",
        "Дебетовые/кредитные карты, переводы, банкомат, онлайн-платежи.",
        "Debit/credit cards, transfers, ATM, online payments.",
    ),
    "Loan types, interest, collateral, overdue payments.": S(
        "Кредит турлари, фоиз, гаров, кечиккан тўловлар.",
        "Типы кредитов, проценты, залог, просрочки.",
        "Loan types, interest, collateral, overdue payments.",
    ),
    "Exchange rates, buying/selling currency, remittances, and wire basics.": S(
        "Валюта курслари, сотиб олиш/сотиш, ўтказмалар ва wire асослари.",
        "Курсы валют, покупка/продажа, переводы и основы wire.",
        "Exchange rates, buying/selling currency, remittances, and wire basics.",
    ),
    "SME banking, working capital, letters of credit and guarantees — simplified.": S(
        "SME банкинг, айланма маблағ, аккредитив ва кафолатлар — соддалаштирилган.",
        "SME-банкинг, оборотный капитал, аккредитивы и гарантии — упрощённо.",
        "SME banking, working capital, letters of credit and guarantees — simplified.",
    ),
    "Mobile/internet banking, OTP, phishing, and fraud awareness English.": S(
        "Мобил/интернет-банкинг, OTP, фишинг ва фирибгарлик хавфсизлиги.",
        "Мобильный/интернет-банкинг, OTP, фишинг и антифрод-английский.",
        "Mobile/internet banking, OTP, phishing, and fraud awareness English.",
    ),
    "Jobs, CV, interviews, and workplace English in a bank.": S(
        "Лавозимлар, CV, суҳбатлар ва банкдаги иш инглизчаси.",
        "Вакансии, CV, интервью и рабочий английский в банке.",
        "Jobs, CV, interviews, and workplace English in a bank.",
    ),
    "Complaints, phone English, problem solving.": S(
        "Шикоятлар, телефон инглизчаси, муаммо ечиш.",
        "Жалобы, телефонный английский, решение проблем.",
        "Complaints, phone English, problem solving.",
    ),
    "Identity checks, KYC/AML basics in clear English.": S(
        "Шахсни текшириш, KYC/AML асослари оддий инглизчада.",
        "Проверка личности, основы KYC/AML на понятном английском.",
        "Identity checks, KYC/AML basics in clear English.",
    ),
    "Workplace emails, meetings, and short presentations.": S(
        "Иш emailлари, учрашувлар ва қисқа тақдимотлар.",
        "Рабочие письма, встречи и короткие презентации.",
        "Workplace emails, meetings, and short presentations.",
    ),
    # Exercise UI descriptions (second side)
    "Hisob turlari.": S("Ҳисоб турлари.", "Типы счетов.", "Account types."),
    "Ish o‘rinlari.": S("Иш ўринлари.", "Должности.", "Job roles."),
    "Bo‘limlar.": S("Бўлимлар.", "Отделы.", "Departments."),
    "Mijoz bilan gaplashish.": S("Мижоз билан гаплашиш.", "Общение с клиентом.", "Talking with a customer."),
    "Salomlashish.": S("Саломлашиш.", "Приветствие.", "Greeting."),
    "Fe’llar.": S("Феъллар.", "Глаголы.", "Verbs."),
    "Statement.": S("Кўчирма.", "Выписка.", "Statement."),
    "Kartalar.": S("Карталар.", "Карты.", "Cards."),
    "O‘tkazmalar.": S("Ўтказмалар.", "Переводы.", "Transfers."),
    "Xavfsizlik.": S("Хавфсизлик.", "Безопасность.", "Security."),
    "Terminologiya.": S("Терминология.", "Терминология.", "Terminology."),
    "Kredit turlari.": S("Кредит турлари.", "Типы кредитов.", "Loan types."),
    "Kechikish.": S("Кечикиш.", "Просрочка.", "Overdue."),
    "Grammatika.": S("Грамматика.", "Грамматика.", "Grammar."),
    "Lavozimlar.": S("Лавозимлар.", "Должности.", "Job titles."),
    "Gapirish.": S("Гапириш.", "Говорение.", "Speaking."),
    "Shikoyat.": S("Шикоят.", "Жалоба.", "Complaint."),
    "Telefon.": S("Телефон.", "Телефон.", "Phone."),
    "O‘qish.": S("Ўқиш.", "Чтение.", "Reading."),
    "Jarayon.": S("Жараён.", "Процесс.", "Process."),
    "Yozish.": S("Ёзиш.", "Письмо.", "Writing."),
    "Uchrashuv.": S("Учрашув.", "Встреча.", "Meeting."),
    "Taqdimot.": S("Тақдимот.", "Презентация.", "Presentation."),
    "Yozishma.": S("Ёзишма.", "Переписка.", "Correspondence."),
    "Muloyim tilak.": S("Мулойим тилак.", "Вежливое пожелание.", "Polite wish."),
    "Kredit karta.": S("Кредит карта.", "Кредитная карта.", "Credit card."),
    "Ish tavsifi.": S("Иш тавсифи.", "Описание работы.", "Job description."),
    "Risk.": S("Риск.", "Риск.", "Risk."),
    "Termin.": S("Термин.", "Термин.", "Term."),
    "FX.": S("FX.", "FX.", "FX."),
    "SME.": S("SME.", "SME.", "SME."),
    "Trade.": S("Trade.", "Trade.", "Trade."),
    "Security.": S("Хавфсизлик.", "Безопасность.", "Security."),
    "Fraud.": S("Фирибгарлик.", "Мошенничество.", "Fraud."),
    "Fraud terms.": S("Фирибгарлик терминлари.", "Термины мошенничества.", "Fraud terms."),
    "Compliance.": S("Compliance.", "Комплаенс.", "Compliance."),
    "Python": S("Python", "Python", "Python"),
    # --- Python course: modules, lectures, descriptions ---
    "Python noldan": S("Python нолдан", "Python с нуля", "Python from zero"),
    "O‘rnatish, birinchi qator kod, xatolarni o‘qish — hech narsa bilmasdan boshlash.": S(
        "Ўрнатиш, биринчи қатор код, хатоларни ўқиш — ҳеч нарса билмасдан бошлаш.",
        "Установка, первая строка кода, чтение ошибок — старт с нуля.",
        "Install, first lines of code, reading errors — start from absolute zero.",
    ),
    "Python va birinchi qator": S("Python ва биринчи қатор", "Python и первая строка", "Python and your first line"),
    "Skript fayl va izoh": S("Скрипт файл ва изоҳ", "Файл скрипта и комментарии", "Script file and comments"),
    "Xatolarni o‘qish": S("Хатоларни ўқиш", "Чтение ошибок", "Reading errors"),
    "Python asoslari": S("Python асослари", "Основы Python", "Python basics"),
    "Nima uchun tahlilchiga Python, o‘zgaruvchilar, turlar va ifodalar.": S(
        "Нима учун таҳлилчига Python, ўзгарувчилар, турлар ва ифодалар.",
        "Зачем аналитику Python, переменные, типы и выражения.",
        "Why analysts need Python: variables, types, and expressions.",
    ),
    "Tahlilchi uchun Python": S("Таҳлилчи учун Python", "Python для аналитика", "Python for analysts"),
    "O‘zgaruvchilar va ma’lumot turlari": S(
        "Ўзгарувчилар ва маълумот турлари",
        "Переменные и типы данных",
        "Variables and data types",
    ),
    "Ifodalar va chop etish": S("Ифодалар ва чоп этиш", "Выражения и вывод", "Expressions and printing"),
    "Shartlar, tsikllar, funksiyalar": S(
        "Шартлар, цикллар, функциялар",
        "Условия, циклы, функции",
        "Conditions, loops, functions",
    ),
    "if/elif, for/while, qayta ishlatiladigan funksiyalar.": S(
        "if/elif, for/while, қайта ишлатиладиган функциялар.",
        "if/elif, for/while, переиспользуемые функции.",
        "if/elif, for/while, reusable functions.",
    ),
    "Shartlar: if, elif, else": S("Шартлар: if, elif, else", "Условия: if, elif, else", "Conditions: if, elif, else"),
    "Tsikllar: for va while": S("Цикллар: for ва while", "Циклы: for и while", "Loops: for and while"),
    "Funksiyalar": S("Функциялар", "Функции", "Functions"),
    "To‘plamlar, fayl va xatolar": S(
        "Тўпламлар, файл ва хатолар",
        "Коллекции, файлы и ошибки",
        "Collections, files, and errors",
    ),
    "list/dict/set/tuple, CSV o‘qish, try/except, modullar.": S(
        "list/dict/set/tuple, CSV ўқиш, try/except, модуллар.",
        "list/dict/set/tuple, чтение CSV, try/except, модули.",
        "list/dict/set/tuple, reading CSV, try/except, modules.",
    ),
    "List, tuple, set, dict": S("List, tuple, set, dict", "List, tuple, set, dict", "List, tuple, set, dict"),
    "Fayl va CSV": S("Файл ва CSV", "Файлы и CSV", "Files and CSV"),
    "Istisnolar va modullar": S("Истиснолар ва модуллар", "Исключения и модули", "Exceptions and modules"),
    "NumPy": S("NumPy", "NumPy", "NumPy"),
    "Massivlar, vektor hisob, nan va statistik qisqa yo‘l.": S(
        "Массивлар, вектор ҳисоб, nan ва статистик қисқа йўл.",
        "Массивы, векторные вычисления, nan и краткая статистика.",
        "Arrays, vector math, NaN, and quick stats.",
    ),
    "ndarray nima?": S("ndarray нима?", "Что такое ndarray?", "What is ndarray?"),
    "Indeks, filtr, broadcasting": S(
        "Индекс, фильтр, broadcasting",
        "Индекс, фильтр, broadcasting",
        "Indexing, filters, broadcasting",
    ),
    "NaN va agregatlar": S("NaN ва агрегатлар", "NaN и агрегаты", "NaN and aggregates"),
    "Pandas: DataFrame": S("Pandas: DataFrame", "Pandas: DataFrame", "Pandas: DataFrame"),
    "Series/DataFrame, o‘qish, tanlash, filtr.": S(
        "Series/DataFrame, ўқиш, танлаш, фильтр.",
        "Series/DataFrame, чтение, выбор, фильтр.",
        "Series/DataFrame, reading, selecting, filtering.",
    ),
    "Series va DataFrame": S("Series ва DataFrame", "Series и DataFrame", "Series and DataFrame"),
    "Ustun tanlash va filtr": S("Устун танлаш ва фильтр", "Выбор столбцов и фильтр", "Column select and filter"),
    "Yangi ustun va assign": S("Янги устун ва assign", "Новый столбец и assign", "New columns and assign"),
    "Tozalash: NaN, dublikat, transform": S(
        "Тозалаш: NaN, дубликат, transform",
        "Очистка: NaN, дубликаты, transform",
        "Cleaning: NaN, duplicates, transform",
    ),
    "Missing, duplicates, matn/son konvertatsiya.": S(
        "Missing, duplicates, матн/сон конвертация.",
        "Missing, duplicates, текст/число конвертация.",
        "Missing values, duplicates, text/number conversion.",
    ),
    "Yetishmayotgan qiymatlar": S("Етишмаётган қийматлар", "Пропущенные значения", "Missing values"),
    "Dublikatlar": S("Дубликатлар", "Дубликаты", "Duplicates"),
    "Matn va tur konvertatsiyasi": S(
        "Матн ва тур конвертацияси",
        "Конвертация текста и типов",
        "Text and type conversion",
    ),
    "Guruhlash, merge, sana": S("Гуруҳлаш, merge, сана", "Группировка, merge, даты", "Grouping, merge, dates"),
    "groupby, agg, merge/join, datetime tahlil.": S(
        "groupby, agg, merge/join, datetime таҳлил.",
        "groupby, agg, merge/join, анализ datetime.",
        "groupby, agg, merge/join, datetime analysis.",
    ),
    "groupby va aggregatsiya": S("groupby ва агрегация", "groupby и агрегация", "groupby and aggregation"),
    "merge / join": S("merge / join", "merge / join", "merge / join"),
    "Sana/vaqt tahlili": S("Сана/вақт таҳлили", "Анализ даты/времени", "Date/time analysis"),
    "EDA va vizualizatsiya": S("EDA ва визуализация", "EDA и визуализация", "EDA and visualization"),
    "Tavsiflovchi tahlil, Matplotlib, Seaborn.": S(
        "Тавсифловчи таҳлил, Matplotlib, Seaborn.",
        "Описательный анализ, Matplotlib, Seaborn.",
        "Descriptive analysis, Matplotlib, Seaborn.",
    ),
    "EDA tartibi": S("EDA тартиби", "Порядок EDA", "EDA workflow"),
    "Matplotlib": S("Matplotlib", "Matplotlib", "Matplotlib"),
    "Seaborn": S("Seaborn", "Seaborn", "Seaborn"),
    "Biznes tahlil va yakuniy loyiha": S(
        "Бизнес таҳлил ва якуний лойиҳа",
        "Бизнес-анализ и итоговый проект",
        "Business analysis and capstone",
    ),
    "KPI, kohort/recency g‘oya, yakuniy analytics project.": S(
        "KPI, когорт/recency ғоя, якуний analytics project.",
        "KPI, идея когорт/recency, итоговый analytics-проект.",
        "KPIs, cohort/recency idea, final analytics project.",
    ),
    "KPI ni kodda hisoblash": S("KPI ни кодда ҳисоблаш", "Расчёт KPI в коде", "Computing KPIs in code"),
    "Mijoz kesimi: recency g‘oyasi": S(
        "Мижоз кесими: recency ғояси",
        "Сегмент клиентов: идея recency",
        "Customer slice: recency idea",
    ),
    "Yakuniy loyiha: retail savdo": S(
        "Якуний лойиҳа: retail савдо",
        "Итоговый проект: розничные продажи",
        "Capstone: retail sales",
    ),
    (
        "Python noldan — tahlilchi va yangi boshlovchi uchun. 10 modul: birinchi qator kod, "
        "o‘zgaruvchi va turlar, if/tsikl/funksiya, tuzilmalar, NumPy, Pandas, tozalash, EDA va mini-loyiha. "
        "Har darsda aniq maqsad, kod namuna, mashq va puzzle."
    ): S(
        (
            "Python нолдан — таҳлилчи ва янги бошловчи учун. 10 модул: биринчи қатор код, "
            "ўзгарувчи ва турлар, if/цикл/функция, тузилмалар, NumPy, Pandas, тозалаш, EDA ва мини-лойиҳа. "
            "Ҳар дарсда аниқ мақсад, код намуна, машқ ва puzzle."
        ),
        (
            "Python с нуля — для аналитиков и начинающих. 10 модулей: первая строка кода, "
            "переменные и типы, if/цикл/функции, структуры, NumPy, Pandas, очистка, EDA и мини-проект. "
            "В каждом уроке цель, пример кода, задания и головоломки."
        ),
        (
            "Python from zero — for analysts and beginners. 10 modules: first lines of code, "
            "variables and types, if/loops/functions, structures, NumPy, Pandas, cleaning, EDA, and a mini-project. "
            "Each lesson has a clear goal, code sample, practice, and puzzles."
        ),
    ),
    "Bank sohasidagi asosiy so‘z.": S(
        "Банк соҳасидаги асосий сўз.",
        "Ключевое банковское слово.",
        "A basic banking word.",
    ),
    "FX terminlari.": S("FX терминлари.", "FX-термины.", "FX terms."),
    "Xalqaro o‘tkazma.": S("Халқаро ўтказма.", "Международный перевод.", "International transfer."),
    "Muddat.": S("Муддат.", "Срок.", "Deadline / timing."),
    "Biznes banking.": S("Бизнес банкинг.", "Бизнес-банкинг.", "Business banking."),
    "Trade finance.": S("Trade finance.", "Trade finance.", "Trade finance."),
    "Guarantee.": S("Кафолат.", "Гарантия.", "Guarantee."),
    "Digital banking.": S("Рақамли банкинг.", "Цифровой банкинг.", "Digital banking."),
}
