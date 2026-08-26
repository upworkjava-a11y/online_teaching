"""
SQL LeetCode-style Medium/Hard mashqlar — dars slugiga biriktirilgan.
Faqat shu dars (va oldingilar) o‘rgatgan narsalar kerak bo‘lishi shart.
"""

# lecture_slug -> [exercise dict, ...]
EXTRA_LECTURE_PRACTICE = {
    "where-operatori": [
        {
            "slug": "lc-m-big-countries-strict",
            "title": "Medium — Katta davlatlar (qattiq shart)",
            "difficulty": "medium",
            "dataset_names": ["World"],
            "description": (
                "Biznes: geografik tahlil uchun “yirik bozor” davlatlarini ajrating.\n\n"
                "Jadval: World (name, continent, area, population, gdp).\n\n"
                "Davlatni qaytaring, agar BIR VAQTNING O‘ZIDA:\n"
                "• area >= 3 000 000 VA\n"
                "• population >= 25 000 000.\n\n"
                "Ustunlar: name, population, area. Tartib ixtiyoriy."
            ),
            "task": "name, population, area. Ikkalasi ham: katta maydon VA katta aholi.",
            "hints": ["Ikki shart birga — AND", "Namunadagi qatorlarni qoida bilan solishtiring"],
            "columns": ["name", "population", "area"],
            "rows": [["Algeria", 37100000, 2381741]],
        },
    ],
    "order-by": [
        {
            "slug": "lc-m-cinema-top2",
            "title": "Medium — Eng yuqori 2 reyting",
            "difficulty": "medium",
            "dataset_names": ["cinema"],
            "require_row_order": True,
            "description": (
                "Biznes: kinoteatr katalogidan top-2 film.\n\n"
                "cinema jadvalidan rating bo‘yicha eng yuqori 2 ta filmni qaytaring.\n"
                "Ustunlar: id, movie, rating. rating DESC."
            ),
            "task": "id, movie, rating. Faqat eng yuqori ikkita.",
            "hints": ["Avval reyting bo‘yicha tushing", "Keyin natijani 2 qatorgacha qisqartiring"],
            "columns": ["id", "movie", "rating"],
            "rows": [[5, "House card", 9.1], [1, "War", 8.9]],
        },
        {
            "slug": "lc-h-gdp-density",
            "title": "Hard — Yuqori zichlikli iqtisod",
            "difficulty": "hard",
            "dataset_names": ["World"],
            "description": (
                "Biznes: aholi zichligi yuqori va iqtisodi kuchli bozorlar.\n\n"
                "World jadvalidan davlatlarni tanlang:\n"
                "• aholi zichligi (aholi / maydon) 90 dan qat’iy katta\n"
                "• VA gdp kamida 10 milliard\n\n"
                "Ustunlar: name, continent, density (zichlik, 2 kasrga yaxlitlangan).\n"
                "density kamayish tartibida."
            ),
            "task": "name, continent, density. Zichlik yuqori va iqtisod katta.",
            "hints": ["population * 1.0 / area — kasr uchun", "ROUND(..., 2) AS density, ORDER BY density DESC"],
            "require_row_order": True,
            "columns": ["name", "continent", "density"],
            "rows": [["Albania", "Europe", 98.5]],
        },
    ],
    "bir-nechta-shart": [
        {
            "slug": "lc-1757",
            "title": "1757. Qayta ishlanadigan va kam yog‘li mahsulotlar",
            "difficulty": "medium",
            "dataset_names": ["Products"],
            "description": (
                "LeetCode 1757. Recyclable and Low Fat Products (Easy)\n\n"
                "Jadval: Products — product_id, low_fats, recyclable.\n"
                "low_fats va recyclable: 'Y' yoki 'N'.\n\n"
                "Ham kam yog‘li, ham qayta ishlanadigan mahsulotlarning product_id sini toping.\n"
                "Tartib ixtiyoriy."
            ),
            "task": "Faqat product_id. Ikkalasi ham 'Y'.",
            "hints": ["Ikki shart birga — AND", "Jadval: Products"],
            "columns": ["product_id"],
            "rows": [[1], [3]],
        },
        {
            "slug": "lc-595",
            "title": "595. Katta davlatlar",
            "difficulty": "medium",
            "dataset_names": ["World"],
            "description": (
                "LeetCode 595. Big Countries (Easy)\n\n"
                "Jadval: World — name, continent, area, population, gdp.\n\n"
                "Davlat katta hisoblanadi, agar:\n"
                "• maydoni kamida 3 000 000 km², YOKI\n"
                "• aholisi kamida 25 000 000 kishi.\n\n"
                "Katta davlatlarning name, population va area ustunlarini qaytaring.\n"
                "Tartib ixtiyoriy."
            ),
            "task": "name, population, area. Katta = maydon YOKI aholi chegarasi.",
            "hints": ["Bittasi yetarli — OR", "Faqat so‘ralgan uchta ustun"],
            "columns": ["name", "population", "area"],
            "rows": [["Afghanistan", 25500100, 652230], ["Algeria", 37100000, 2381741]],
        },
        {
            "slug": "lc-m-products-or",
            "title": "Medium — Kam yog‘li YOKI qayta ishlanadi",
            "difficulty": "medium",
            "dataset_names": ["Products"],
            "description": (
                "Products: kam yog‘li YOKI qayta ishlanadigan mahsulotlarning product_id sini qaytaring. "
                "Tartib ixtiyoriy."
            ),
            "task": "Faqat product_id. Bittasi yetarli.",
            "hints": ["AND emas — OR", "Kamida bitta 'Y'"],
            "columns": ["product_id"],
            "rows": [[0], [1], [2], [3]],
        },
    ],
    "group-by-asoslari": [
        {
            "slug": "lc-2356",
            "title": "2356. O‘qituvchi o‘qitgan unikal fanlar",
            "difficulty": "medium",
            "dataset_names": ["Teacher"],
            "description": (
                "LeetCode 2356. Number of Unique Subjects Taught by Each Teacher (Easy)\n\n"
                "Jadval: Teacher — teacher_id, subject_id, dept_id.\n"
                "Bir fan turli kafedralarda o‘qitilishi mumkin.\n\n"
                "Har bir o‘qituvchi nechta turli fanni o‘qitishini hisoblang.\n"
                "Ustunlar: teacher_id, cnt. Tartib ixtiyoriy."
            ),
            "task": "teacher_id va cnt. Har o‘qituvchi nechta turli fan.",
            "hints": ["COUNT(DISTINCT subject_id)", "GROUP BY teacher_id"],
            "columns": ["teacher_id", "cnt"],
            "rows": [[1, 2], [2, 4]],
        },
        {
            "slug": "lc-1741",
            "title": "1741. Xodimning ishda o‘tkazgan vaqti",
            "difficulty": "medium",
            "dataset_names": ["EmployeeAttendance"],
            "description": (
                "LeetCode 1741. Find Total Time Spent by Each Employee (Easy)\n\n"
                "Jadval: EmployeeAttendance — emp_id, event_day, in_time, out_time.\n"
                "Vaqt daqiqalarda: out_time - in_time.\n\n"
                "Har bir xodim har bir kunda jami qancha daqiqa ishlaganini hisoblang.\n"
                "Ustunlar: day (event_day), emp_id, total_time. Tartib ixtiyoriy."
            ),
            "task": "day, emp_id, total_time. Har xodim–kun juftligi.",
            "hints": [
                "GROUP BY event_day, emp_id",
                "SUM(out_time - in_time) AS total_time, event_day AS day",
            ],
            "columns": ["day", "emp_id", "total_time"],
            "rows": [
                ["2020-11-28", 1, 173],
                ["2020-11-28", 2, 30],
                ["2020-12-03", 1, 41],
                ["2020-12-09", 2, 27],
            ],
        },
        {
            "slug": "lc-m-teacher-subjects",
            "title": "Medium — O‘qituvchi fanlari (tartib bilan)",
            "difficulty": "medium",
            "dataset_names": ["Teacher"],
            "require_row_order": True,
            "description": (
                "Teacher: teacher_id, subject_id, dept_id.\n"
                "Har bir o‘qituvchi nechta unique fan o‘qitishini hisoblang.\n"
                "Ustunlar: teacher_id, cnt. teacher_id o‘sish tartibida."
            ),
            "task": "teacher_id va cnt, teacher_id o‘sish tartibida.",
            "hints": ["COUNT(DISTINCT subject_id)", "ORDER BY teacher_id"],
            "columns": ["teacher_id", "cnt"],
            "rows": [[1, 2], [2, 4]],
        },
    ],
    "having-nima": [
        {
            "slug": "lc-m-followers-active",
            "title": "Medium — Faol foydalanuvchilar",
            "difficulty": "medium",
            "dataset_names": ["Followers"],
            "require_row_order": True,
            "description": (
                "Biznes: ijtimoiy tarmoqda kamida 2 obunachisi bor foydalanuvchilar.\n\n"
                "Followers: user_id, follower_id.\n"
                "Kamida 2 follower ga ega user_id larni toping.\n"
                "Ustun: user_id. O‘sish tartibida."
            ),
            "task": "Faqat user_id, o‘sish tartibida. Kamida 2 obunachi.",
            "hints": ["GROUP BY user_id, keyin HAVING", "ORDER BY user_id"],
            "columns": ["user_id"],
            "rows": [[2]],
        },
        {
            "slug": "lc-m-classes-3plus",
            "title": "Medium — Kamida 3 talabali sinflar",
            "difficulty": "medium",
            "dataset_names": ["Courses"],
            "description": (
                "Courses jadvalidan kamida 3 talabasi bor sinflarni toping.\n"
                "Ustun: class."
            ),
            "task": "Ustun: class. Kamida 3 talaba.",
            "hints": ["Easy dagi chegara 5 edi — bu yerda 3"],
            "columns": ["class"],
            "rows": [["Math"]],
        },
        {
            "slug": "lc-h-class-majority",
            "title": "Hard — Eng ko‘p talabali sinf",
            "difficulty": "hard",
            "dataset_names": ["Courses"],
            "description": (
                "Eng ko‘p talabasi bor sinf(lar)ni toping.\n"
                "Agar tenglik bo‘lsa — barcha eng yuqori sinflarni qaytaring.\n"
                "Ustun: class."
            ),
            "task": "Ustun: class. Eng ko‘p talabali sinf(lar).",
            "hints": ["Avval har sinfning sonini oling", "Keyin shu sonlar ichidagi maksimumga tenglarini qoldiring"],
            "columns": ["class"],
            "rows": [["Math"]],
        },
    ],
    "inner-join": [
        {
            "slug": "lc-m-sales-product-join",
            "title": "Medium — Sotuv + mahsulot nomi",
            "difficulty": "medium",
            "dataset_names": ["Sales", "Product"],
            "require_row_order": True,
            "description": (
                "Biznes: savdo hisobotiga mahsulot nomini qo‘shing.\n\n"
                "Sales va Product. Ustunlar: product_name, year, price.\n"
                "year o‘sish tartibida."
            ),
            "task": "product_name, year, price. year o‘sish tartibida.",
            "hints": ["Nom boshqa jadvalda — kalit orqali qo‘shing"],
            "columns": ["product_name", "year", "price"],
            "rows": [["Nokia", 2008, 5000], ["Nokia", 2009, 5000], ["Apple", 2011, 9000]],
        },
    ],
    "left-join": [
        {
            "slug": "lc-m-no-bonus",
            "title": "Medium — Bonussiz xodimlar",
            "difficulty": "medium",
            "dataset_names": ["Employee", "Bonus"],
            "require_row_order": True,
            "description": (
                "Biznes: HR — bonus olmagan xodimlarni topish.\n\n"
                "Bonus jadvalida yozuvi yo‘q xodimlarning name va salary sini qaytaring.\n"
                "name o‘sish tartibida."
            ),
            "task": "name, salary. Faqat bonussizlar. Ism o‘sish tartibida.",
            "hints": ["Xodimlar asosiy — bonus yo‘qlar ham chapda qolsin", "Bonus tomoni bo‘sh qatorlarni qoldiring"],
            "columns": ["name", "salary"],
            "rows": [["Brad", 4000], ["John", 1000]],
        },
        {
            "slug": "lc-h-combine-address",
            "title": "Hard — Manzilsiz shaxslar ham",
            "difficulty": "hard",
            "dataset_names": ["Person", "Address"],
            "require_row_order": True,
            "description": (
                "LeetCode 175 uslubi (chuqurroq).\n\n"
                "Har bir shaxs: firstName, lastName, city, state.\n"
                "Manzil bo‘lmasa — city/state NULL.\n"
                "personId o‘sish tartibida.\n"
                "Address da bor, Person da yo‘q odam chiqmasin."
            ),
            "task": "firstName, lastName, city, state. Manzilsiz shaxslar ham. personId tartibida.",
            "hints": ["Asosiy jadval — Person", "Manzili yo‘q odamda city/state bo‘sh qoladi"],
            "columns": ["firstName", "lastName", "city", "state"],
            "rows": [
                ["Allen", "Wang", None, None],
                ["Bob", "Alice", "New York City", "New York"],
            ],
        },
    ],
    "subquery-where": [
        {
            "slug": "lc-m-customers-never-order",
            "title": "Medium — Buyurtma bermagan mijozlar",
            "difficulty": "medium",
            "dataset_names": ["LCCustomers", "LCOrders"],
            "require_row_order": True,
            "description": (
                "LeetCode 183. Customers Who Never Order (Medium uslub).\n\n"
                "LCCustomers(id, name), LCOrders(id, customerId).\n"
                "Hech qachon buyurtma bermagan mijozlarning name sini qaytaring.\n"
                "name o‘sish tartibida."
            ),
            "task": "Ustun: name, o‘sish tartibida. Hech qachon buyurtma bermaganlar.",
            "hints": ["Buyurtmalar ro‘yxatida yo‘q mijoz — ikki yo‘l bor: ro‘yxatda yo‘q, yoki bog‘lanmagan qator"],
            "columns": ["name"],
            "rows": [["Henry"], ["Max"]],
        },
    ],
    "cte-asoslari": [
        {
            "slug": "lc-m-cte-top-salary",
            "title": "Medium — CTE: eng yuqori maosh",
            "difficulty": "medium",
            "dataset_names": ["Employee"],
            "description": (
                "Eng yuqori maoshli xodim(lar)ni toping. WITH dan foydalaning.\n"
                "Ustunlar: name, salary. Tenglik bo‘lsa — barchasi."
            ),
            "task": "name, salary. Eng yuqori maosh(lar).",
            "hints": ["Avval maksimumni ajrating, keyin tenglarini oling", "Bir nechta xodim bir xil yuqori maoshda bo‘lishi mumkin"],
            "columns": ["name", "salary"],
            "rows": [["Brad", 4000], ["Thomas", 4000]],
        },
    ],
    "case-when": [
        {
            "slug": "lc-m-case-salary-band",
            "title": "Medium — Maosh diapazoni",
            "difficulty": "medium",
            "dataset_names": ["Employee"],
            "require_row_order": True,
            "description": (
                "Har bir xodim uchun band ustunini yarating:\n"
                "• salary < 2000 → 'low'\n"
                "• 2000 <= salary < 4000 → 'mid'\n"
                "• aks holda → 'high'\n\n"
                "Ustunlar: name, salary, band. empId o‘sish tartibida."
            ),
            "task": "name, salary, band. empId o‘sish tartibida.",
            "hints": ["Uch tabaqa: past / o‘rta / yuqori — chegaralarni ketma-ket tekshiring"],
            "columns": ["name", "salary", "band"],
            "rows": [
                ["John", 1000, "low"],
                ["Dan", 2000, "mid"],
                ["Brad", 4000, "high"],
                ["Thomas", 4000, "high"],
            ],
        },
    ],
    "window-rank": [
        {
            "slug": "lc-m-rank-scores",
            "title": "Medium — Ballarni reytinglash",
            "difficulty": "medium",
            "dataset_names": ["Scores"],
            "require_row_order": True,
            "description": (
                "LeetCode 178. Rank Scores (Medium).\n\n"
                "Scores(id, score).\n"
                "Har bir ball uchun o‘rin: teng ballar bir xil o‘rin, keyingi o‘rin teshiksiz "
                "(1, 1, 2 — 1, 1, 3 emas).\n\n"
                "Ustunlar: score, rank. score kamayish tartibida."
            ),
            "task": "score va rank. Eng yuqori ball — 1-o‘rin. Tartib tekshiriladi.",
            "hints": ["Tenglikda teshik ochilmasin", "Oyna funksiyasi qatorni yo‘qotmaydi"],
            "columns": ["score", "rank"],
            "rows": [[4.0, 1], [4.0, 1], [3.85, 2], [3.65, 3], [3.65, 3], [3.5, 4]],
        },
    ],
    "window-sum": [
        {
            "slug": "lc-h-seat-swap",
            "title": "Hard — O‘rinlarni almashtirish",
            "difficulty": "hard",
            "dataset_names": ["Seat"],
            "require_row_order": True,
            "description": (
                "LeetCode 626. Exchange Seats.\n\n"
                "Seat(id, student). Juft–toq o‘rindiqlarni almashtiring:\n"
                "1↔2, 3↔4, ... Agar oxirgi id toq bo‘lsa — o‘zi qoladi.\n\n"
                "Ustunlar: id, student. id o‘sish tartibida."
            ),
            "task": "id, student. Juft–toq juftliklar almashtirilgan, id o‘sish tartibida.",
            "hints": ["Toq o‘rindiq keyingi o‘quvchini oladi, juft — oldingisini", "Oxirgi toq id o‘zgarmasligi mumkin"],
            "columns": ["id", "student"],
            "rows": [
                [1, "Doris"],
                [2, "Abbot"],
                [3, "Green"],
                [4, "Emerson"],
                [5, "Jeames"],
            ],
        },
    ],
}


def practices_for_lecture(slug: str, base_map: dict) -> list:
    """Bitta dars uchun Easy (base) + Extra Medium/Hard ro‘yxati."""
    items = []
    base = base_map.get(slug)
    if base:
        if isinstance(base, dict):
            item = dict(base)
            item.setdefault("difficulty", "easy")
            items.append(item)
        else:
            for p in base:
                item = dict(p)
                item.setdefault("difficulty", "easy")
                items.append(item)
    for extra in EXTRA_LECTURE_PRACTICE.get(slug, []):
        items.append(dict(extra))
    return items
