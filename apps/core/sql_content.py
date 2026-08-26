from apps.core.sql_teacher_lessons import LECTURES

COURSE_DESCRIPTION = (
    "Ma’lumotlar tahlili uchun SQL: noldan, o‘qituvchi bilan gaplashgandek. "
    "Bank mijozlari va tranzaksiyalar jadvalida SELECT, WHERE, JOIN, GROUP BY, CTE va window funksiyalarini "
    "qadamma-qadam o‘rganasiz. Har darsdan keyin mashq bor."
)

HOMEWORK = {
    "sql-asoslari": (
        "1) SQL nima ekanini 4–5 jumlada yozing (RDBMS, jadval, qator, ustun).\n"
        "2) SELECT sintaksisini yozing.\n"
        "3) customers dan name va city oladigan so‘rov + DISTINCT city so‘rovi.\n"
        "Fayl: .txt, UTF-8."
    ),
    "filtrlash-va-saralash": (
        "1) WHERE da matn va son qanday yozilishini tushuntiring.\n"
        "2) AND vs OR va qavs uchun 1 ta o‘z misolingiz.\n"
        "3) Debit + amount DESC to‘liq so‘rov.\n"
        "4) LIKE da % va _ farqi."
    ),
    "agregatsiyalar": (
        "1) COUNT(*), COUNT(ustun), COUNT(DISTINCT) farqi.\n"
        "2) SUM va AVG misollari.\n"
        "3) GROUP BY so‘rovi: mijoz bo‘yicha COUNT va SUM.\n"
        "4) WHERE vs HAVING — qachon qaysi."
    ),
}

SQL_EXAMPLES = {
    "select-nima": [
        "SELECT name FROM customers;",
        "SELECT * FROM customers;",
        "SELECT * FROM customers LIMIT 5;",
    ],
    "ustunlarni-tanlash": [
        "SELECT name, city FROM customers;",
        "SELECT id, name, city FROM customers;",
        "SELECT name AS mijoz, city AS shahar FROM customers;",
    ],
    "natijani-oqish": [
        "SELECT city FROM customers;",
        "SELECT DISTINCT city FROM customers;",
        "SELECT COUNT(DISTINCT city) AS shahar_soni FROM customers;",
    ],
    "where-operatori": [
        "SELECT name, city FROM customers WHERE city = 'Toshkent';",
        "SELECT id, amount FROM transactions WHERE amount > 100000;",
        "SELECT id, amount, transaction_type FROM transactions WHERE transaction_type = 'debit';",
    ],
    "order-by": [
        "SELECT id, amount FROM transactions ORDER BY amount;",
        "SELECT id, amount FROM transactions ORDER BY amount DESC;",
        "SELECT name, city FROM customers ORDER BY city ASC, name ASC;",
    ],
    "bir-nechta-shart": [
        "SELECT * FROM customers WHERE city = 'Toshkent' AND name LIKE 'A%';",
        "SELECT * FROM customers WHERE city IN ('Toshkent', 'Samarqand');",
        "SELECT id, amount FROM transactions WHERE amount BETWEEN 10000 AND 50000;",
        "SELECT id, amount FROM transactions WHERE amount >= 50000 AND transaction_type = 'debit';",
    ],
    "count": [
        "SELECT COUNT(*) AS total FROM customers;",
        "SELECT COUNT(*) AS total FROM customers WHERE city = 'Toshkent';",
        "SELECT COUNT(DISTINCT city) AS shaharlar FROM customers;",
    ],
    "sum-va-avg": [
        "SELECT SUM(amount) AS total FROM transactions;",
        "SELECT AVG(amount) AS avg_amount FROM transactions;",
        "SELECT MIN(amount) AS eng_kichik, MAX(amount) AS eng_katta FROM transactions;",
    ],
    "group-by-asoslari": [
        "SELECT customer_id, COUNT(*) AS cnt FROM transactions GROUP BY customer_id;",
        "SELECT customer_id, SUM(amount) AS total FROM transactions GROUP BY customer_id;",
        "SELECT customer_id, COUNT(*) AS cnt FROM transactions GROUP BY customer_id HAVING COUNT(*) > 5;",
    ],
}

EXERCISE_COPY = {
    "mijoz-ismlari": {
        "description": "Hisobot uchun mijozlar ro‘yxati kerak. customers jadvalidan barcha mijozlarning ismini oling. Natijada faqat name ustuni bo‘lishi kerak.",
        "task": "Faqat name ustunini qaytaring. Qator tartibi muhim emas.",
    },
    "toshkent-mijozlari": {
        "description": "Filial Toshkentdagi mijozlarni alohida ko‘rmoqchi. Faqat shu shahardagi qatorlarni oling.",
        "task": "name va city ustunlarini qaytaring. Faqat Toshkent.",
    },
    "katta-tranzaksiyalar": {
        "description": "Risk-nazorat 100 000 so‘mdan katta to‘lovlarni ko‘rmoqchi. transactions jadvalidan shunday qatorlarni toping.",
        "task": "id va amount. 100 000 dan qat’iy katta summalar.",
    },
    "debit-operatsiyalar": {
        "description": "Moliya bo‘limi faqat debit operatsiyalarni hisobotga oladi.",
        "task": "id va transaction_type. Faqat debit qatorlar.",
    },
    "summa-boyicha-saralash": {
        "description": "Eng katta to‘lovlardan boshlang. Barcha tranzaksiyalarni summa kamayish tartibida chiqaring.",
        "task": "id va amount. Eng katta summa tepada. Qator tartibi tekshiriladi.",
    },
    "faol-mijozlar": {
        "description": "Marketing 5 tadan ko‘p tranzaksiya qilgan mijozlarni VIP deb belgilamoqchi.",
        "task": "Faqat customer_id. 5 tadan ko‘p to‘lovi borlar.",
    },
    "jami-summa": {
        "description": "Kunlik tushumni baholash: barcha tranzaksiyalar yig‘indisi.",
        "task": "Bitta qator, ustun nomi total.",
    },
    "mijozlar-boyicha-soni": {
        "description": "Har bir mijoz qancha operatsiya qilganini ko‘ring. Bu faollik hisoboti.",
        "task": "customer_id va cnt — har mijoz uchun operatsiyalar soni.",
    },
    "mijozlar-yigindisi": {
        "description": "Har bir mijozning umumiy to‘lov hajmi. LTV ga yaqin ko‘rsatkich.",
        "task": "customer_id va total — har mijoz uchun summalar yig‘indisi.",
    },
}

# Easy mashq — faqat SHU dars (va oldingilar) o‘rgatgan narsalar.
LECTURE_PRACTICE = {
    "select-nima": {
        "slug": "lc-select-products",
        "title": "Easy · Mahsulot identifikatorlari",
        "dataset_names": ["Products"],
        "description": (
            "Jadval: Products — product_id, low_fats, recyclable.\n\n"
            "Barcha mahsulotlarning product_id qiymatlarini oling.\n"
            "Filtr yo‘q — faqat ustun tanlash. Tartib ixtiyoriy."
        ),
        "task": "Faqat product_id ustuni. Barcha qatorlar.",
        "hints": ["SELECT dan keyin qaysi ustun kerakligini yozing", "Jadval nomi: Products"],
        "columns": ["product_id"],
        "rows": [[0], [1], [2], [3], [4]],
    },
    "ustunlarni-tanlash": {
        "slug": "lc-world-columns",
        "title": "Easy · Davlat ustunlarini tanlash",
        "dataset_names": ["World"],
        "description": (
            "Jadval: World — name, continent, area, population, gdp.\n\n"
            "Hisobot uchun faqat name, population va area kerak.\n"
            "Hali filtr yo‘q — barcha davlatlar. Tartib ixtiyoriy."
        ),
        "task": "Ustunlar: name, population, area. Filtr yo‘q.",
        "hints": ["Ustunlarni vergul bilan yozing", "* emas — faqat so‘ralgan uchta"],
        "columns": ["name", "population", "area"],
        "rows": [
            ["Afghanistan", 25500100, 652230],
            ["Albania", 2831741, 28748],
            ["Algeria", 37100000, 2381741],
            ["Andorra", 78115, 468],
            ["Angola", 20609294, 1246700],
        ],
    },
    "natijani-oqish": {
        "slug": "lc-world-continents",
        "title": "Easy · Takrorsiz qit’alar",
        "dataset_names": ["World"],
        "description": (
            "Jadval: World.\n\n"
            "Jadvalda bir qit’a bir necha marta chiqishi mumkin.\n"
            "Qaysi qit’alar bor — har birini bir marta ko‘rsating.\n"
            "Ustun: continent. Tartib ixtiyoriy."
        ),
        "task": "Takrorsiz continent qiymatlari.",
        "hints": ["Takror kerak emas — DISTINCT", "Faqat continent ustuni"],
        "columns": ["continent"],
        "rows": [["Africa"], ["Asia"], ["Europe"]],
    },
    "where-operatori": {
        "slug": "lc-1683",
        "title": "1683. Noto‘g‘ri tvitlar",
        "dataset_names": ["Tweets"],
        "description": (
            "LeetCode 1683. Invalid Tweets (Easy)\n\n"
            "Jadval: Tweets — tweet_id, content.\n\n"
            "Tvit noto‘g‘ri, agar content dagi belgilar soni 15 dan qat’iy katta bo‘lsa.\n"
            "Noto‘g‘ri tvitlarning tweet_id sini qaytaring. Tartib ixtiyoriy."
        ),
        "task": "Faqat tweet_id. Belgilar soni 15 dan qat’iy katta.",
        "hints": ["Tenglik emas — qat’iy katta", "Matn uzunligi: LENGTH(content)"],
        "columns": ["tweet_id"],
        "rows": [[2]],
    },
    "order-by": {
        "slug": "lc-1148",
        "title": "1148. Maqola ko‘rishlari I",
        "dataset_names": ["Views"],
        "require_row_order": True,
        "description": (
            "LeetCode 1148. Article Views I (Easy)\n\n"
            "Jadval: Views — article_id, author_id, viewer_id, view_date.\n"
            "Bir xil author_id va viewer_id — bu bir xil odam.\n"
            "Jadvalda takroriy qatorlar bo‘lishi mumkin.\n\n"
            "O‘z maqolasini kamida bir marta o‘zi ko‘rgan mualliflarni toping.\n"
            "Natijada ustun nomi id bo‘lsin (bu author_id).\n"
            "id o‘sish tartibida saralang."
        ),
        "task": "Ustun nomi id. O‘zini ko‘rgan mualliflar, o‘sish tartibida, takrorsiz.",
        "hints": [
            "WHERE da muallif va tomoshabin bir xil bo‘lsin",
            "DISTINCT + AS id, keyin ORDER BY",
        ],
        "columns": ["id"],
        "rows": [[4], [7]],
    },
    "bir-nechta-shart": {
        "slug": "lc-1527",
        "title": "1527. Muayyan tashxisli bemorlar",
        "dataset_names": ["Patients"],
        "description": (
            "LeetCode 1527. Patients With a Condition (Easy)\n\n"
            "Jadval: Patients — patient_id, patient_name, conditions.\n"
            "conditions — bo‘shliq bilan ajratilgan kodlar (masalan: ACNE DIAB100).\n\n"
            "I turdagi diabet kodi DIAB1 bilan boshlanadi.\n"
            "Shartlar ro‘yxatida DIAB1 bilan boshlanadigan kod bor bemorlarni qaytaring.\n"
            "DIAB100 mos keladi, DIAB201 esa yo‘q (chunki DIAB2...)."
        ),
        "task": "patient_id, patient_name, conditions. Faqat I tur diabet kodi borlar.",
        "hints": [
            "Kod qator boshida: LIKE 'DIAB1%'",
            "Yoki bo‘shliqdan keyin: LIKE '% DIAB1%'",
        ],
        "columns": ["patient_id", "patient_name", "conditions"],
        "rows": [
            [3, "Bob", "DIAB100 MYOP"],
            [4, "George", "ACNE DIAB100"],
        ],
    },
    "count": {
        "slug": "lc-count-followers-total",
        "title": "Easy · Obunalar jami",
        "dataset_names": ["Followers"],
        "description": (
            "Jadval: Followers — user_id, follower_id.\n\n"
            "Jadvalda jami nechta qator (obuna juftligi) bor?\n"
            "Bitta son qaytaring. Ustun nomi: total."
        ),
        "task": "Bitta qator, ustun: total.",
        "hints": ["COUNT(*) AS total", "GROUP BY hozircha kerak emas — butun jadval"],
        "columns": ["total"],
        "rows": [[4]],
    },
    "sum-va-avg": {
        "slug": "lc-sum-work-minutes",
        "title": "Easy · Jami ish daqiqalari",
        "dataset_names": ["EmployeeAttendance"],
        "description": (
            "Jadval: EmployeeAttendance — emp_id, event_day, in_time, out_time.\n"
            "Har qatorda sessiya: out_time - in_time daqiqalar.\n\n"
            "Barcha sessiyalar bo‘yicha jami daqiqani toping.\n"
            "Ustun: total_time."
        ),
        "task": "Bitta qator: total_time — barcha (out_time - in_time) yig‘indisi.",
        "hints": ["SUM ichida ifoda yozish mumkin", "GROUP BY hozircha shart emas"],
        "columns": ["total_time"],
        "rows": [[271]],
    },
    "group-by-asoslari": {
        "slug": "lc-1729",
        "title": "1729. Obunachilar soni",
        "dataset_names": ["Followers"],
        "require_row_order": True,
        "description": (
            "LeetCode 1729. Find Followers Count (Easy)\n\n"
            "Jadval: Followers — user_id, follower_id (juftlik unikal).\n\n"
            "Har bir foydalanuvchining obunachilari sonini hisoblang.\n"
            "Ustunlar: user_id, followers_count.\n"
            "user_id o‘sish tartibida qaytaring."
        ),
        "task": "user_id va followers_count. Har foydalanuvchi, user_id o‘sish tartibida.",
        "hints": ["Har user_id uchun GROUP BY", "COUNT(*) AS followers_count, ORDER BY user_id"],
        "columns": ["user_id", "followers_count"],
        "rows": [[0, 1], [1, 1], [2, 2]],
    },
}
