"""SQL modules 4–11: mashqlar va homework. Darslar sql_teacher_lessons da."""

from apps.core.sql_teacher_lessons import ADVANCED_LECTURES

ADVANCED_EXAMPLES = {
    "having-nima": [
        "SELECT city, COUNT(*) AS cnt\nFROM customers\nGROUP BY city\nHAVING COUNT(*) >= 2;"
    ],
    "group-by-kop-ustun": [
        "SELECT city, COUNT(*) AS cnt\nFROM customers\nGROUP BY city;"
    ],
    "agregat-filtr": [
        "SELECT MAX(amount) AS amount\nFROM (\n  SELECT amount FROM transactions\n  GROUP BY amount\n  HAVING COUNT(*) = 1\n) AS t;"
    ],
    "inner-join": [
        "SELECT c.name, t.amount\nFROM customers AS c\nINNER JOIN transactions AS t ON c.id = t.customer_id;",
    ],
    "left-join": [
        "SELECT c.name, t.id\nFROM customers AS c\nLEFT JOIN transactions AS t ON c.id = t.customer_id;",
    ],
    "join-null": [
        "SELECT c.name\nFROM customers AS c\nLEFT JOIN transactions AS t ON c.id = t.customer_id\nWHERE t.id IS NULL;"
    ],
    "subquery-where": [
        "SELECT id, amount FROM transactions\nWHERE amount > (SELECT AVG(amount) FROM transactions);"
    ],
    "subquery-from": [
        "SELECT MAX(amount) AS amount FROM (\n  SELECT amount FROM transactions GROUP BY amount HAVING COUNT(*) = 1\n) AS singles;"
    ],
    "exists-in": [
        "SELECT name FROM customers\nWHERE city IN ('Toshkent', 'Samarqand');"
    ],
    "cte-asoslari": [
        "WITH debitlar AS (\n  SELECT * FROM transactions WHERE transaction_type = 'debit'\n)\nSELECT SUM(amount) AS total FROM debitlar;"
    ],
    "cte-bir-nechta": [
        "WITH c AS (\n  SELECT city, COUNT(*) AS cnt FROM customers GROUP BY city\n)\nSELECT city FROM c WHERE cnt >= 2;"
    ],
    "cte-amal": [
        "WITH j AS (\n  SELECT customer_id, COUNT(*) AS c FROM transactions GROUP BY customer_id\n)\nSELECT customer_id FROM j WHERE c >= 3;"
    ],
    "case-when": [
        "SELECT id, amount,\n  CASE WHEN amount < 20000 THEN 'kichik' ELSE 'katta' END AS segment\nFROM transactions;"
    ],
    "case-select": [
        "SELECT id,\n  CASE WHEN amount >= 50000 THEN amount ELSE 0 END AS katta_summa\nFROM transactions;"
    ],
    "case-agregat": [
        "SELECT transaction_type,\n  SUM(CASE WHEN amount >= 50000 THEN 1 ELSE 0 END) AS katta_soni\nFROM transactions\nGROUP BY transaction_type;"
    ],
    "sana-filtr": [
        "SELECT id, amount FROM transactions\nWHERE transaction_date = '2024-03-01';"
    ],
    "sana-group": [
        "SELECT transaction_date AS day, COUNT(*) AS cnt\nFROM transactions\nGROUP BY transaction_date;"
    ],
    "sana-farq": [
        "SELECT transaction_date, transaction_type, COUNT(*) AS cnt\nFROM transactions\nGROUP BY transaction_date, transaction_type;"
    ],
    "window-asos": [
        "SELECT id, amount, ROW_NUMBER() OVER (ORDER BY amount DESC) AS rn\nFROM transactions;"
    ],
    "window-rank": [
        "SELECT id, amount, RANK() OVER (ORDER BY amount DESC) AS rnk\nFROM transactions;"
    ],
    "window-sum": [
        "SELECT id, amount, SUM(amount) OVER () AS jami\nFROM transactions;"
    ],
    "null-coalesce": [
        "SELECT id, COALESCE(amount, 0) AS amount FROM transactions;"
    ],
    "combine-tables": [
        "SELECT c.name, t.amount\nFROM customers AS c\nLEFT JOIN transactions AS t ON c.id = t.customer_id;"
    ],
    "advanced-review": [
        "SELECT c.name, COUNT(*) AS cnt\nFROM customers AS c\nJOIN transactions AS t ON c.id = t.customer_id\nGROUP BY c.name;"
    ],
}

ADVANCED_PRACTICE = {
    "having-nima": {
        "slug": "lc-596",
        "title": "596. Kamida 5 talabali sinflar",
        "dataset_names": ["Courses"],
        "description": (
            "LeetCode 596. Classes With at Least 5 Students (Easy)\n\n"
            "Jadval: Courses — student, class.\n"
            "Kamida 5 talabasi bor sinflarni toping. Tartib ixtiyoriy."
        ),
        "task": "Ustun: class. Kamida 5 talabasi bor sinflar.",
        "hints": ["Avval sinf bo‘yicha sanang, keyin kichik guruhlarni tashlang"],
        "columns": ["class"],
        "rows": [["Math"]],
    },
    "group-by-kop-ustun": {
        "slug": "lc-1050",
        "title": "1050. Aktyor va rejissyor (kamida 3)",
        "dataset_names": ["ActorDirector"],
        "description": (
            "LeetCode 1050. Actors and Directors Who Cooperated At Least Three Times (Easy)\n\n"
            "Jadval: ActorDirector — actor_id, director_id, timestamp.\n"
            "Kamida 3 marta birga ishlagan juftliklarni toping."
        ),
        "task": "actor_id va director_id. Kamida 3 marta birga ishlagan juftliklar.",
        "hints": ["Juftlik — ikkita kalit. Sanash juftlik ichida bo‘lishi kerak"],
        "columns": ["actor_id", "director_id"],
        "rows": [[1, 1]],
    },
    "agregat-filtr": {
        "slug": "lc-619",
        "title": "619. Eng katta yagona son",
        "dataset_names": ["MyNumbers"],
        "description": (
            "LeetCode 619. Biggest Single Number (Easy)\n\n"
            "Jadval: MyNumbers — num.\n"
            "Faqat bir marta uchragan sonlar ichidan eng kattasini qaytaring.\n"
            "Agar yo‘q bo‘lsa — null (bu datasetda bor)."
        ),
        "task": "Bitta ustun: num. Yolg‘iz sonlar ichidagi eng katta.",
        "hints": ["Avval qaysi sonlar bir marta uchraydi — shuni toping", "Keyin qolganlardan eng kattasini oling"],
        "columns": ["num"],
        "rows": [[6]],
    },
    "inner-join": {
        "slug": "lc-1068",
        "title": "1068. Mahsulot sotuv tahlili I",
        "dataset_names": ["Sales", "Product"],
        "description": (
            "LeetCode 1068. Product Sales Analysis I (Easy)\n\n"
            "Jadvallar: Sales, Product.\n"
            "Har bir sotuv uchun product_name, year, price ni qaytaring."
        ),
        "task": "product_name, year, price. Sotuvga mahsulot nomini qo‘shing.",
        "hints": ["Nom boshqa jadvalda — kalit orqali bog‘lang"],
        "columns": ["product_name", "year", "price"],
        "rows": [["Nokia", 2008, 5000], ["Nokia", 2009, 5000], ["Apple", 2011, 9000]],
    },
    "left-join": {
        "slug": "lc-1378",
        "title": "1378. Xodim unique_id",
        "dataset_names": ["Employees", "EmployeeUNI"],
        "description": (
            "LeetCode 1378. Replace Employee ID With The Unique Identifier (Easy)\n\n"
            "Jadvallar: Employees (id, name), EmployeeUNI (id, unique_id).\n"
            "Har bir xodimning unique_id sini ko‘rsating; yo‘q bo‘lsa null."
        ),
        "task": "unique_id va name. Identifikatori yo‘q xodimlar ham chiqsin.",
        "hints": ["Chapda barcha xodimlar qolishi kerak", "Mos kelmasa unique_id bo‘sh bo‘lishi normal"],
        "columns": ["unique_id", "name"],
        "rows": [
            [None, "Alice"],
            [None, "Bob"],
            [2, "Meir"],
            [3, "Winston"],
            [1, "Jonathan"],
        ],
    },
    "join-null": {
        "slug": "lc-577",
        "title": "577. Xodim bonusi",
        "dataset_names": ["Employee", "Bonus"],
        "description": (
            "LeetCode 577. Employee Bonus (Easy)\n\n"
            "Jadvallar: Employee, Bonus.\n"
            "Bonus &lt; 1000 yoki bonus umuman yo‘q xodimlarning name va bonusini qaytaring."
        ),
        "task": "name va bonus. Bonus 1000 dan kam yoki umuman yo‘qlar.",
        "hints": ["Bonus yo‘q qatorni oddiy solishtirish yutib yuborishi mumkin", "NULL ni 0 deb o‘qish yoki alohida tekshirish"],
        "columns": ["name", "bonus"],
        "rows": [["Brad", None], ["John", None], ["Dan", 500]],
    },
    "subquery-where": {
        "slug": "lc-619b",
        "title": "619. Yagona sonlar (HAVING)",
        "dataset_names": ["MyNumbers"],
        "description": (
            "LeetCode 619 (qisman). MyNumbers dan faqat bir marta uchragan sonlarni toping."
        ),
        "task": "Ustun: num. Faqat bir marta uchragan sonlar.",
        "hints": ["Guruhlab sanang, keyin soni 1 bo‘lganlarni qoldiring"],
        "columns": ["num"],
        "rows": [[1], [4], [5], [6]],
    },
    "subquery-from": {
        "slug": "lc-619c",
        "title": "619. Eng katta yagona (subquery)",
        "dataset_names": ["MyNumbers"],
        "description": (
            "LeetCode 619. Subquery bilan: ichki so‘rovda yagona sonlar, tashqida MAX."
        ),
        "task": "Ustun: num. Yolg‘iz sonlar ichidagi eng katta — ichki so‘rov bilan.",
        "hints": ["Ichki natija — vaqtinchalik jadval", "Tashqi qism undan agregat oladi"],
        "columns": ["num"],
        "rows": [[6]],
    },
    "exists-in": {
        "slug": "lc-product-sold",
        "title": "Easy · Sotilgan mahsulotlar",
        "dataset_names": ["Product", "Sales"],
        "description": (
            "Product jadvalidan Sales da hech bo‘lmaganda bir marta uchragan mahsulotlarni oling."
        ),
        "task": "product_id va product_name. Faqat sotilganlar.",
        "hints": ["Mahsulot ID si sotuvlar ro‘yxatida bormi — shu savol"],
        "columns": ["product_id", "product_name"],
        "rows": [[100, "Nokia"], [200, "Apple"]],
    },
    "cte-asoslari": {
        "slug": "lc-619-cte",
        "title": "619. CTE bilan eng katta yagona",
        "dataset_names": ["MyNumbers"],
        "description": "LeetCode 619 ni WITH (CTE) yordamida yeching: yolg‘iz sonlar ichidan eng kattasi.",
        "task": "Ustun: num. Avval yolg‘izlar, keyin eng katta.",
        "hints": ["Bosqichga nom bering, keyin undan o‘qing"],
        "columns": ["num"],
        "rows": [[6]],
    },
    "cte-bir-nechta": {
        "slug": "lc-596-cte",
        "title": "596. CTE bilan sinflar",
        "dataset_names": ["Courses"],
        "description": "596 ni CTE bilan: avval sanang, keyin kamida 5 talabali sinflarni qoldiring.",
        "task": "Ustun: class.",
        "hints": ["CTE da son, tashqida filtr"],
        "columns": ["class"],
        "rows": [["Math"]],
    },
    "cte-amal": {
        "slug": "lc-1050-cte",
        "title": "1050. CTE bilan juftliklar",
        "dataset_names": ["ActorDirector"],
        "description": "1050 ni CTE bilan yeching: juftliklar necha marta uchraganini avval hisoblang.",
        "task": "actor_id, director_id. Kamida 3 marta.",
        "hints": ["Sanashni CTE ichida qoldiring, tashqida faqat filtr"],
        "columns": ["actor_id", "director_id"],
        "rows": [[1, 1]],
    },
    "case-when": {
        "slug": "lc-610",
        "title": "610. Uchburchak tekshiruvi",
        "dataset_names": ["Triangle"],
        "description": (
            "LeetCode 610. Triangle Judgement (Easy)\n\n"
            "Jadval: Triangle — x, y, z.\n"
            "Uchburchak bo‘la oladimi? Yes/No (CASE)."
        ),
        "task": "x, y, z va triangle (Yes yoki No). Uchburchak tengsizligini tekshiring.",
        "hints": ["Har tomon qolgan ikkisining yig‘indisidan kichik bo‘lishi kerak"],
        "columns": ["x", "y", "z", "triangle"],
        "rows": [[13, 15, 30, "No"], [10, 20, 15, "Yes"]],
    },
    "case-select": {
        "slug": "lc-1873",
        "title": "1873. Maxsus bonus",
        "dataset_names": ["Employee"],
        "description": (
            "LeetCode 1873. Calculate Special Bonus (Easy)\n\n"
            "Jadval: Employee — empId, name, supervisor, salary.\n"
            "Bonus = salary, agar empId toq VA ism 'M' bilan boshlanmasa; aks holda 0.\n"
            "Ustunlar: empId, name (employee_id, bonus emas — shu dataset: empId, bonus)."
        ),
        "task": "empId va bonus. Toq empId va M bilan boshlanmagan ismga maosh, qolganlarga 0.",
        "hints": ["Ikki shart birga; aks holda nol", "Natija yangi ustun — jadvalni o‘zgartirmaysiz"],
        "columns": ["empId", "bonus"],
        "rows": [[3, 4000], [1, 1000], [2, 0], [4, 0]],
    },
    "case-agregat": {
        "slug": "lc-case-sales",
        "title": "Easy · CASE bilan sotuv sanash",
        "dataset_names": ["DailySales"],
        "description": "Har bir make_name uchun qatorlar sonini COUNT bilan oling (CASE mashqi uchun tayyorgarlik).",
        "task": "make_name va cnt. Har brend necha qator.",
        "hints": ["Brend bo‘yicha guruhlab sanang"],
        "columns": ["make_name", "cnt"],
        "rows": [["toyota", 5], ["honda", 5]],
    },
    "sana-filtr": {
        "slug": "lc-activity-day",
        "title": "Easy · Kunlik faol foydalanuvchilar",
        "dataset_names": ["Activity"],
        "description": "2019-07-20 kundagi unikal user_id larni toping.",
        "task": "Faqat user_id, takrorsiz. Faqat 2019-07-20.",
        "hints": ["Aniq bir kun — sana tengligi", "Bir kishi ikki marta kirsada, bir marta chiqsin"],
        "columns": ["user_id"],
        "rows": [[1], [2]],
    },
    "sana-group": {
        "slug": "lc-1141",
        "title": "1141. 30 kunlik faollik",
        "dataset_names": ["Activity"],
        "description": (
            "LeetCode 1141. User Activity for the Past 30 Days I (Easy)\n\n"
            "activity_date 2019-07-27 dan oldingi 30 kun oralig‘ida (shu kun bilan)\n"
            "har bir kunda nechta unikal foydalanuvchi bo‘lganini toping.\n"
            "Ustunlar: day, active_users. Faqat faollik bo‘lgan kunlar."
        ),
        "task": "day va active_users. Faqat faollik bo‘lgan kunlar, oxirgi 30 kun (27-iyul bilan).",
        "hints": ["Kun bo‘yicha guruhlang", "Bir kishini bir kunda bir marta sanang"],
        "columns": ["day", "active_users"],
        "rows": [["2019-07-20", 2], ["2019-07-21", 2]],
    },
    "sana-farq": {
        "slug": "lc-1693",
        "title": "1693. Kunlik lead va partner",
        "dataset_names": ["DailySales"],
        "description": (
            "LeetCode 1693. Daily Leads and Partners (Easy)\n\n"
            "Jadval: DailySales — date_id, make_name, lead_id, partner_id.\n"
            "Har bir date_id + make_name uchun unikal lead va partner sonini toping."
        ),
        "task": "date_id, make_name, unique_leads, unique_partners.",
        "hints": ["Kesim: kun va brend birga", "Lead va partnerni alohida, takrorsiz sanang"],
        "columns": ["date_id", "make_name", "unique_leads", "unique_partners"],
        "rows": [
            ["2020-12-7", "honda", 3, 2],
            ["2020-12-7", "toyota", 1, 2],
            ["2020-12-8", "honda", 2, 2],
            ["2020-12-8", "toyota", 2, 3],
        ],
    },
    "window-asos": {
        "slug": "lc-seat-rn",
        "title": "Easy · ROW_NUMBER o‘rindiqlar",
        "dataset_names": ["Seat"],
        "require_row_order": True,
        "description": "Seat jadvalida id tartibida har qatorga tartib raqami (rn) qo‘ying. Barcha qatorlar qolsin.",
        "task": "id, student, rn. id o‘sish tartibida.",
        "hints": ["Guruhlab siqmang — har o‘quvchi o‘z qatorida qolsin", "Oyna tartibi id bo‘yicha"],
        "columns": ["id", "student", "rn"],
        "rows": [
            [1, "Abbot", 1],
            [2, "Doris", 2],
            [3, "Emerson", 3],
            [4, "Green", 4],
            [5, "Jeames", 5],
        ],
    },
    "window-rank": {
        "slug": "lc-seat-rank",
        "title": "Easy · RANK o‘rindiqlar",
        "dataset_names": ["Seat"],
        "require_row_order": True,
        "description": "Seat: har qatorga id tartibidagi o‘rin (rnk). Tenglik bo‘lsa RANK qoidasini eslang.",
        "task": "id, student, rnk",
        "hints": ["Bu yerda id lar unique — RANK va ROW_NUMBER bir xil chiqishi mumkin"],
        "columns": ["id", "student", "rnk"],
        "rows": [
            [1, "Abbot", 1],
            [2, "Doris", 2],
            [3, "Emerson", 3],
            [4, "Green", 4],
            [5, "Jeames", 5],
        ],
    },
    "window-sum": {
        "slug": "lc-seat-total",
        "title": "Easy · Jami o‘rindiqlar (window)",
        "dataset_names": ["Seat"],
        "description": "Har qatorda jami o‘rindiqlar soni (total_seats) ko‘rinsin. Qatorlar yo‘qolmasin.",
        "task": "id, student, total_seats",
        "hints": ["Jami butun jadval uchun bir xil son", "Guruhlab bitta qator qoldirmang"],
        "columns": ["id", "student", "total_seats"],
        "rows": [
            [1, "Abbot", 5],
            [2, "Doris", 5],
            [3, "Emerson", 5],
            [4, "Green", 5],
            [5, "Jeames", 5],
        ],
    },
    "null-coalesce": {
        "slug": "lc-175-city",
        "title": "175. COALESCE bilan shahar",
        "dataset_names": ["Person", "Address"],
        "description": "Person va Address. Shahar yo‘q bo‘lsa 'Noma’lum' deb yozing.",
        "task": "firstName, lastName, city",
        "hints": ["Manzilsiz odamlar ham chiqishi kerak", "Bo‘sh joyni matn bilan almashtiring"],
        "columns": ["firstName", "lastName", "city"],
        "rows": [["Allen", "Wang", "Noma’lum"], ["Bob", "Alice", "New York City"]],
    },
    "combine-tables": {
        "slug": "lc-175",
        "title": "175. Ikki jadvalni birlashtirish",
        "dataset_names": ["Person", "Address"],
        "description": (
            "LeetCode 175. Combine Two Tables (Easy)\n\n"
            "Person va Address. Har shaxs: firstName, lastName, city, state. Manzil bo‘lmasa — bo‘sh (NULL)."
        ),
        "task": "firstName, lastName, city, state. Manzilsizlar ham.",
        "hints": ["Odamlar asosiy jadval — hech kim tushib qolmasin"],
        "columns": ["firstName", "lastName", "city", "state"],
        "rows": [
            ["Allen", "Wang", None, None],
            ["Bob", "Alice", "New York City", "New York"],
        ],
    },
    "advanced-review": {
        "slug": "lc-sales-count",
        "title": "Easy · Mahsulot bo‘yicha sotuvlar",
        "dataset_names": ["Sales", "Product"],
        "description": "Har bir mahsulot nomi necha marta sotilganini toping.",
        "task": "product_name va sales_cnt",
        "hints": ["Avval nomni bog‘lang, keyin nom bo‘yicha sanang"],
        "columns": ["product_name", "sales_cnt"],
        "rows": [["Nokia", 2], ["Apple", 1]],
    },
}

ADVANCED_HOMEWORK = {
    "group-by-having": (
        "WHERE va HAVING farqini jadval qilib yozing (qachon, nimaga).\n"
        "Har bir shahar bo‘yicha COUNT va “kamida 2 mijoz” HAVING so‘rovini yozing.\n"
        "596 mashqini o‘z so‘zingiz bilan tushuntiring."
    ),
    "joins": (
        "INNER JOIN va LEFT JOIN ni 5 jumlada farqlang.\n"
        "Bitta kalit ustunli misol chizing (mijoz–to‘lov).\n"
        "“To‘lovi yo‘q mijozlar” ni LEFT JOIN + IS NULL bilan yozing."
    ),
    "subqueries": (
        "IN va EXISTS farqi.\n"
        "NOT IN da NULL xavfini 3 jumlada yozing.\n"
        "O‘rtachadan katta amount uchun subquery yozing."
    ),
    "ctes": (
        "CTE nima ekanini W3 uslubida: nima bu, sintaksis, 1 misol.\n"
        "619 ni WITH bilan qayta yozing."
    ),
    "case": (
        "CASE WHEN tartibini tushuntiring (birinchi rost shart).\n"
        "amount ni kichik/orta/katta ga ajrating.\n"
        "SUM(CASE WHEN ...) ni 1 misolda yozing."
    ),
    "date-time": (
        "Sana qanday formatda yoziladi?\n"
        "BETWEEN bilan mart oyi filtri.\n"
        "Kunlik COUNT(DISTINCT ...) g‘oyasini yozing."
    ),
    "window-functions": (
        "GROUP BY va window farqi (qator soni).\n"
        "ROW_NUMBER, RANK, DENSE_RANK jadvali.\n"
        "Seat uchun ROW_NUMBER so‘rovi."
    ),
    "advanced-sql": (
        "NULL nima, IS NULL nima uchun = NULL emas.\n"
        "COALESCE sintaksisi va 1 misol.\n"
        "Person LEFT JOIN Address ni tushuntiring."
    ),
}


def _bank_ex(slug_suffix, title, description, task, hints, columns, rows, require_row_order=False):
    return {
        "title": title,
        "slug": slug_suffix,
        "description": description,
        "task": task,
        "hints": hints,
        "columns": columns,
        "rows": rows,
        "require_row_order": require_row_order,
    }


def build_advanced_modules():
    """Return modules_data entries for orders 4–11."""
    specs = [
        (
            4,
            "GROUP BY va HAVING",
            "group-by-having",
            "Guruhlash va HAVING filtri.",
            [
                ("HAVING nima?", "having-nima"),
                ("Ko‘p ustunli GROUP BY", "group-by-kop-ustun"),
                ("Agregat + filtr", "agregat-filtr"),
            ],
            [
                _bank_ex(
                    "shahar-2-mijoz",
                    "2+ mijozli shaharlar",
                    "customers dan kamida 2 mijozli shaharlarni toping.",
                    "Ustun: city.",
                    ["Avval shahar bo‘yicha sanang, keyin kichiklarini tashlang"],
                    ["city"],
                    [["Toshkent"]],
                ),
                _bank_ex(
                    "mijoz-3-plus",
                    "3+ tranzaksiyali mijozlar",
                    "Kamida 3 ta tranzaksiyasi bor mijozlarni toping.",
                    "Ustun: customer_id.",
                    ["Mijoz bo‘yicha sanang, keyin chegaradan kichiklarini tashlang"],
                    ["customer_id"],
                    [[1]],
                ),
            ],
        ),
        (
            5,
            "JOINlar",
            "joins",
            "INNER JOIN, LEFT JOIN, NULL.",
            [
                ("INNER JOIN", "inner-join"),
                ("LEFT JOIN", "left-join"),
                ("JOIN va NULL", "join-null"),
            ],
            [
                _bank_ex(
                    "mijoz-tranz-join",
                    "Mijoz va tranzaksiya",
                    "Har to‘lov yonida mijoz ismi ko‘rinsin. Ism customers da, summa transactions da.",
                    "name va amount.",
                    ["Ikki jadvalni umumiy kalit orqali bog‘lang"],
                    ["name", "amount"],
                    # all pairs - many rows - use a simpler expected: just Ali's first?
                    # Better: distinct customers who have transactions
                    [["Ali Valiyev", 120000], ["Ali Valiyev", 45000], ["Ali Valiyev", 80000],
                     ["Ali Valiyev", 15000], ["Ali Valiyev", 22000], ["Ali Valiyev", 31000],
                     ["Malika Karimova", 50000], ["Malika Karimova", 70000],
                     ["Javohir Saidov", 150000], ["Javohir Saidov", 20000],
                     ["Dilnoza Yusupova", 90000], ["Sardor Ergashev", 10000]],
                ),
            ],
        ),
        (
            6,
            "Subquerylar",
            "subqueries",
            "WHERE/FROM subquery, IN.",
            [
                ("WHERE subquery", "subquery-where"),
                ("FROM subquery", "subquery-from"),
                ("IN / EXISTS", "exists-in"),
            ],
            [
                _bank_ex(
                    "avg-yuqori",
                    "O‘rtachadan katta summalar",
                    "O‘rtacha to‘lovdan qimmatroq tranzaksiyalarni toping.",
                    "id va amount.",
                    ["Avval o‘rtachani ichki savol qilib oling, keyin solishtiring"],
                    ["id", "amount"],
                    [[1, 120000], [3, 80000], [8, 70000], [9, 150000], [11, 90000]],
                ),
            ],
        ),
        (
            7,
            "CTElar",
            "ctes",
            "WITH asoslari va amaliyot.",
            [
                ("CTE asoslari", "cte-asoslari"),
                ("Bir nechta CTE", "cte-bir-nechta"),
                ("CTE amaliyoti", "cte-amal"),
            ],
            [
                _bank_ex(
                    "cte-debit",
                    "CTE: debit yig‘indisi",
                    "Avval faqat debit qatorlarni ajrating, keyin ularning yig‘indisini oling.",
                    "Ustun: total.",
                    ["Bosqichga nom bering, keyin undan yig‘indi oling"],
                    ["total"],
                    [[543000]],
                ),
            ],
        ),
        (
            8,
            "CASE",
            "case",
            "CASE WHEN shartlari.",
            [
                ("CASE WHEN", "case-when"),
                ("CASE SELECT da", "case-select"),
                ("CASE agregatda", "case-agregat"),
            ],
            [
                _bank_ex(
                    "katta-kichik",
                    "Katta/kichik to‘lov",
                    "Har to‘lovga yorliq: 50 000 va undan katta — 'katta', qolgani — 'kichik'.",
                    "id, amount, label",
                    ["Shartli ustun — birinchi mos qoida ishlaydi"],
                    ["id", "amount", "label"],
                    [
                        [1, 120000, "katta"], [2, 45000, "kichik"], [3, 80000, "katta"], [4, 15000, "kichik"],
                        [5, 22000, "kichik"], [6, 31000, "kichik"], [7, 50000, "katta"], [8, 70000, "katta"],
                        [9, 150000, "katta"], [10, 20000, "kichik"], [11, 90000, "katta"], [12, 10000, "kichik"],
                    ],
                ),
            ],
        ),
        (
            9,
            "Sana va vaqt funksiyalari",
            "date-time",
            "Sana filtri va guruhlash.",
            [
                ("Sana filtri", "sana-filtr"),
                ("Sana bo‘yicha GROUP BY", "sana-group"),
                ("Kunlik ko‘rsatkichlar", "sana-farq"),
            ],
            [
                _bank_ex(
                    "mart-tranz",
                    "Mart 2024 tranzaksiyalari",
                    "2024-yil mart oyidagi barcha tranzaksiyalar sonini toping.",
                    "Ustun: total.",
                    ["Oy boshidan oxirigacha — ikkala chekka ham kirsin"],
                    ["total"],
                    [[12]],
                ),
            ],
        ),
        (
            10,
            "Window funksiyalar",
            "window-functions",
            "ROW_NUMBER, RANK, window OVER.",
            [
                ("ROW_NUMBER", "window-asos"),
                ("RANK", "window-rank"),
                ("SUM/COUNT OVER", "window-sum"),
            ],
            [
                _bank_ex(
                    "amount-rank",
                    "Summa bo‘yicha tartib",
                    "Eng katta 3 to‘lov: id, amount va tartib raqami (rn). Qatorlar siqilmasin.",
                    "id, amount, rn — faqat birinchi 3 o‘rin",
                    ["Summa kamayish tartibida raqamlang, keyin faqat 1–3 ni qoldiring"],
                    ["id", "amount", "rn"],
                    [[9, 150000, 1], [1, 120000, 2], [11, 90000, 3]],
                    True,
                ),
            ],
        ),
        (
            11,
            "Ilg‘or SQL",
            "advanced-sql",
            "NULL, COALESCE, murakkab JOIN.",
            [
                ("NULL va COALESCE", "null-coalesce"),
                ("Combine Two Tables", "combine-tables"),
                ("Yakuniy takrorlash", "advanced-review"),
            ],
            [
                _bank_ex(
                    "debit-foiz",
                    "Debit ulushi",
                    "Barcha tranzaksiyalar ichida debit ulushi necha foiz? Butun son (pct).",
                    "Ustun: pct.",
                    ["Debitni 1, qolganini 0 deb sanash mumkin", "Keyin 100 ga ko‘paytirib, jami soniga bo‘ling"],
                    ["pct"],
                    [[75]],
                ),
            ],
        ),
    ]

    modules = []
    for order, title, slug, desc, lectures, exercises in specs:
        modules.append(
            {
                "order": order,
                "title": title,
                "slug": slug,
                "description": desc,
                "lectures": [
                    {
                        "title": lt,
                        "slug": ls,
                        "content": ADVANCED_LECTURES[ls],
                        "sql_examples": ADVANCED_EXAMPLES[ls],
                    }
                    for lt, ls in lectures
                ],
                "exercises": exercises,
                "homework": True,
            }
        )
    return modules
