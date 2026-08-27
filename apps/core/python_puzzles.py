"""
Python Data Analytics — dars mashqlari va modul “puzzle” testlari.
Boshlang‘ich → o‘rta (CodeChef/W3 style, lekin analyticsga mos).
"""

from apps.core.python_content import _quiz


# Har dars uchun qo‘shimcha (2-chi) mashq — medium
EXTRA_LECTURE_PRACTICE: dict[str, dict] = {
    "py-nima": _quiz(
        "py-p-raw",
        "Puzzle: raw papka",
        "Hamkasb xom CSV ni to‘g‘ridan o‘zgartirib saqlagan.",
        "Nima xato?",
        [
            "A) Hech narsa",
            "B) Xom manba yo‘qoladi — raw/nusxa saqlash kerak edi",
            "C) Faqat f-string xato",
            "D) type() ishlatilgan",
        ],
        "B",
        difficulty="medium",
    ),
    "py-turlar": _quiz(
        "py-p-cast",
        "Puzzle: tur o‘girish",
        's = "12.5"; kerak: son sifatida 2 ga ko‘paytirish.',
        "To‘g‘ri?",
        ["A) s * 2", "B) float(s) * 2", "C) int(s) * 2 doim", "D) str(2) + s"],
        "B",
        difficulty="medium",
    ),
    "py-ifodalar": _quiz(
        "py-p-zero-div",
        "Puzzle: AOV",
        "orders = 0, revenue = 1000.",
        "Xavfsiz AOV?",
        [
            "A) revenue / orders",
            "B) revenue / orders if orders else None (yoki 0 siyosati)",
            "C) orders / revenue",
            "D) revenue * orders",
        ],
        "B",
        difficulty="medium",
    ),
    "py-if": _quiz(
        "py-p-segment",
        "Puzzle: segment",
        "VIP >= 10mln, Regular >= 2mln, aks holda New. revenue=2_000_000.",
        "Natija?",
        ["A) VIP", "B) Regular", "C) New", "D) Xato"],
        "B",
        difficulty="medium",
    ),
    "py-loop": _quiz(
        "py-p-sum-loop",
        "Puzzle: yig‘indi",
        "amounts = [10, 20, 30]. for bilan yig‘indi.",
        "Natija?",
        ["A) 60", "B) 30", "C) 10", "D) 3"],
        "A",
    ),
    "py-func": _quiz(
        "py-p-func-ret",
        "Puzzle: return",
        "Funksiya print qiladi, lekin return yo‘q. Chaqiruvchi o‘zgaruvchiga yozsa?",
        "Odatda nima bo‘ladi?",
        ["A) Qiymat keladi", "B) None keladi", "C) List", "D) Crash doim"],
        "B",
        difficulty="medium",
    ),
    "py-collections": _quiz(
        "py-p-index",
        "Puzzle: indeks",
        "cities = ['A','B','C']; cities[-1]?",
        "Natija?",
        ["A) A", "B) B", "C) C", "D) Xato"],
        "C",
    ),
    "py-file": _quiz(
        "py-p-enc",
        "Puzzle: encoding",
        "CSV o‘zbekcha harflar buzilib chiqdi.",
        "Birinchi qadam?",
        [
            "A) encoding sinash (utf-8 / utf-8-sig)",
            "B) Drop file",
            "C) Faqat print",
            "D) Ignore",
        ],
        "A",
        difficulty="medium",
    ),
    "py-except": _quiz(
        "py-p-except",
        "Puzzle: except",
        "except:  (yalang‘och) nima uchun yomon?",
        "Sabab?",
        [
            "A) Juda yaxshi",
            "B) Haqiqiy xatoni yashiradi — aniq exception tuting",
            "C) Tezlashtiradi",
            "D) Import qiladi",
        ],
        "B",
        difficulty="medium",
    ),
    "np-ndarray": _quiz(
        "py-p-np-mean",
        "Puzzle: mean",
        "np.mean([10, 20, 30])?",
        "Natija?",
        ["A) 20", "B) 60", "C) 30", "D) 3"],
        "A",
    ),
    "np-index": _quiz(
        "py-p-mask",
        "Puzzle: mask",
        "arr = np.array([0, 2, -1, 4]); arr[arr > 0]?",
        "Qaysi?",
        ["A) [0,2,-1,4]", "B) [2,4]", "C) [-1]", "D) [0]"],
        "B",
        difficulty="medium",
    ),
    "np-nan": _quiz(
        "py-p-nanmean",
        "Puzzle: NaN",
        "Oddiy mean NaN bo‘lsa odatda?",
        "Nima bo‘ladi?",
        ["A) Doim 0", "B) Natija NaN bo‘lishi mumkin — nanmean/tozalash kerak", "C) Crash HTML", "D) List"],
        "B",
        difficulty="medium",
    ),
    "pd-df": _quiz(
        "py-p-shape",
        "Puzzle: shape",
        "df 200 qator, 8 ustun. shape?",
        "Natija?",
        ["A) (8, 200)", "B) (200, 8)", "C) 208", "D) (200,)"],
        "B",
    ),
    "pd-filter": _quiz(
        "py-p-and-filter",
        "Puzzle: filtr",
        "Toshkent va amount > 0.",
        "Pandas uslubi?",
        [
            "A) df[df.city=='Toshkent' and df.amount>0]",
            "B) df[(df['city']=='Toshkent') & (df['amount']>0)]",
            "C) df.filter_sql",
            "D) df.drop_all()",
        ],
        "B",
        difficulty="medium",
        hints=["Python and o‘rniga &; qavslar muhim."],
    ),
    "pd-assign": _quiz(
        "py-p-newcol",
        "Puzzle: yangi ustun",
        "AOV ustuni.",
        "To‘g‘ri?",
        [
            "A) df.aov = revenue/orders (Series emas)",
            "B) df['aov'] = df['revenue'] / df['orders']",
            "C) df.append('aov')",
            "D) np.aov(df)",
        ],
        "B",
        difficulty="medium",
    ),
    "pd-na": _quiz(
        "py-p-isna-sum",
        "Puzzle: missing soni",
        "Har ustunda NaN sonini ko‘rish?",
        "Qaysi?",
        ["A) df.isna().sum()", "B) df.head()", "C) df.merge()", "D) df.plot()"],
        "A",
    ),
    "pd-dup": _quiz(
        "py-p-dup",
        "Puzzle: dublikat",
        "order_id bo‘yicha dublikatni olib tashlash (birinchisini saqlash).",
        "Usul?",
        [
            "A) drop_duplicates(subset=['order_id'], keep='first')",
            "B) dropna()",
            "C) head(1)",
            "D) sort_values only",
        ],
        "A",
        difficulty="medium",
    ),
    "pd-cast": _quiz(
        "py-p-coerce",
        "Puzzle: coerce",
        "amount ichida 'N/A' matni bor.",
        "Eng yumshoq konversiya?",
        [
            "A) int(amount) har qator",
            "B) pd.to_numeric(df['amount'], errors='coerce')",
            "C) drop whole table",
            "D) ignore",
        ],
        "B",
        difficulty="medium",
    ),
    "pd-groupby": _quiz(
        "py-p-gb-sum",
        "Puzzle: groupby",
        "Region bo‘yicha amount yig‘indisi.",
        "Qisqa yozuv?",
        [
            "A) df.groupby('region')['amount'].sum()",
            "B) df.head().sum()",
            "C) df.isna()",
            "D) df.columns.sum()",
        ],
        "A",
    ),
    "pd-merge": _quiz(
        "py-p-merge-left",
        "Puzzle: left merge",
        "orders asos, customers dan city qo‘shish.",
        "how?",
        ["A) how='left'", "B) how='inner' doim majburiy", "C) how='cross' only", "D) how='delete'"],
        "A",
        difficulty="medium",
    ),
    "pd-dt": _quiz(
        "py-p-dt",
        "Puzzle: datetime",
        "order_date matn. Oylik guruhlash uchun?",
        "Birinchi qadam?",
        [
            "A) pd.to_datetime(...)",
            "B) drop column",
            "C) mean(city)",
            "D) pie chart",
        ],
        "A",
        difficulty="medium",
    ),
    "pd-eda": _quiz(
        "py-p-describe",
        "Puzzle: describe",
        "amount taqsimotini tez ko‘rish.",
        "Birinchi qadam?",
        ["A) df['amount'].describe()", "B) DROP TABLE", "C) CSS", "D) f-string only"],
        "A",
    ),
    "py-mpl": _quiz(
        "py-p-chart",
        "Puzzle: chart tanlash",
        "Oylik revenue trendi.",
        "Eng mos?",
        ["A) Pie 24 bo‘lak", "B) Line chart", "C) Word cloud", "D) QR"],
        "B",
    ),
    "py-sns": _quiz(
        "py-p-box",
        "Puzzle: outlier",
        "amount outlier larini ko‘rish.",
        "Qaysi?",
        ["A) Boxplot", "B) Pie", "C) Title only", "D) iloc"],
        "A",
        difficulty="medium",
    ),
    "py-kpi": _quiz(
        "py-p-kpi-def",
        "Puzzle: KPI ta’rifi",
        "Ikki jamoa 'faol mijoz' ni boshqacha hisoblaydi.",
        "Nima qilish?",
        [
            "A) E’tibor bermaslik",
            "B) Ta’rifni hujjatlashtirib kelishish",
            "C) Pie chart ko‘paytirish",
            "D) Parol almashtirish",
        ],
        "B",
        difficulty="medium",
    ),
    "py-rfm": _quiz(
        "py-p-recency-days",
        "Puzzle: recency",
        "Bugun 1-avgust, oxirgi xarid 1-iyun.",
        "Taxminiy recency (kun)?",
        ["A) ~61", "B) 1", "C) 365", "D) 0"],
        "A",
        difficulty="medium",
    ),
    "py-final": _quiz(
        "py-p-cap-order",
        "Puzzle: loyiha tartibi",
        "CSV keldi. Birinchi ish?",
        "Eng to‘g‘ri?",
        [
            "A) Darhol 20 grafik",
            "B) Xomni saqlash + tozalash jurnali + tur/missing tekshiruvi",
            "C) Model deploy",
            "D) Drop all NaN without looking",
        ],
        "B",
        difficulty="medium",
    ),
}


# Modul banki — SQL dagi qo‘shimcha mashqlarga o‘xshash “puzzle”lar
MODULE_EXERCISES: dict[str, list[dict]] = {
    "py-asoslari": [
        _quiz(
            "py-ex-types",
            "Puzzle: turlar aralashuvi",
            "Hisobotda amount ba’zan matn, ba’zan son.",
            "Birinchi tuzatish?",
            [
                "A) Darhol o‘rtacha olish",
                "B) Turini tekshirib songa o‘girish (to_numeric/astype)",
                "C) Ustunni o‘chirish",
                "D) Faqat pie",
            ],
            "B",
            difficulty="easy",
        ),
        _quiz(
            "py-ex-pct",
            "Puzzle: foiz",
            "AOV 50→45.",
            "Foiz o‘zgarish?",
            ["A) -10%", "B) +10%", "C) 45%", "D) 50%"],
            "A",
            difficulty="medium",
            hints=["(45-50)/50 = -0.1"],
        ),
    ],
    "py-mantiq": [
        _quiz(
            "py-ex-if-bug",
            "Puzzle: = xatosi",
            "if amount = 0:",
            "Muammo?",
            ["A) To‘g‘ri", "B) = tayinlash; taqqoslash == kerak", "C) for kerak", "D) import kerak"],
            "B",
        ),
        _quiz(
            "py-ex-func",
            "Puzzle: qayta ishlatish",
            "3 joyda bir xil AOV formulasi nusxa.",
            "Yaxshiroq?",
            ["A) Yana 3 nusxa", "B) def aov(...): return ...", "C) Faqat Excel", "D) O‘chirish"],
            "B",
            difficulty="medium",
        ),
    ],
    "py-tuzilma": [
        _quiz(
            "py-ex-dict-row",
            "Puzzle: qator",
            "CSV qatori dastlab qanday tuzilma bo‘lishi odatiy?",
            "Eng yaqin?",
            ["A) dict kalit=ustun", "B) int", "C) bool only", "D) HTML"],
            "A",
        ),
        _quiz(
            "py-ex-unique",
            "Puzzle: unique city",
            "Ro‘yxatda shaharlar takrorlanadi. Unikal son?",
            "Tez usul?",
            ["A) len(set(cities))", "B) cities[0]", "C) sum(cities)", "D) type(cities)"],
            "A",
            difficulty="medium",
        ),
    ],
    "py-numpy": [
        _quiz(
            "py-ex-vector",
            "Puzzle: vektor",
            "Har narxga 12% QQS.",
            "NumPy uslubi?",
            ["A) for bilan sekin", "B) prices * 1.12", "C) prices + '12%'", "D) drop"],
            "B",
        ),
        _quiz(
            "py-ex-std",
            "Puzzle: tarqoqlik",
            "Ikki region o‘rtacha bir xil, lekin biri beqaror.",
            "Qaysi metrika?",
            ["A) std / dispersion", "B) head()", "C) columns", "D) f-string"],
            "A",
            difficulty="medium",
        ),
    ],
    "py-pandas": [
        _quiz(
            "py-ex-read",
            "Puzzle: encoding",
            "O‘zbekcha CSV mojibake.",
            "Birinchi urinish?",
            [
                "A) encoding='utf-8' / 'utf-8-sig' / 'cp1251' sinash",
                "B) Drop file",
                "C) Only Excel forever",
                "D) Ignore",
            ],
            "A",
            difficulty="medium",
        ),
        _quiz(
            "py-ex-filter-chain",
            "Puzzle: zanjir",
            "amount>0 va status=='paid'.",
            "To‘g‘ri?",
            [
                "A) df[(df.amount>0) & (df.status=='paid')]",
                "B) df.amount>0 and df.status",
                "C) df.sql_delete",
                "D) df[0:0]",
            ],
            "A",
        ),
    ],
    "py-clean": [
        _quiz(
            "py-ex-order",
            "Puzzle: tozalash tartibi",
            "Dublikat, matn amount, NaN bor.",
            "Eng mantiqiy?",
            [
                "A) KPI → tozalash",
                "B) Tur → missing siyosati → dublikat → KPI",
                "C) Plot only",
                "D) Random drop",
            ],
            "B",
            difficulty="medium",
        ),
        _quiz(
            "py-ex-fill",
            "Puzzle: fillna",
            "region NaN — 'Noma’lum' qo‘yish.",
            "Usul?",
            ["A) fillna('Noma’lum')", "B) mean()", "C) merge how=cross", "D) iloc"],
            "A",
        ),
    ],
    "py-agg": [
        _quiz(
            "py-ex-aov-region",
            "Puzzle: region AOV",
            "Har region: sum(amount)/nunique(order_id).",
            "Vositalar?",
            ["A) groupby + agg", "B) only head", "C) dropna reverse", "D) CSS"],
            "A",
            difficulty="medium",
        ),
        _quiz(
            "py-ex-fanout",
            "Puzzle: join xavfi",
            "customers da customer_id dublikat, orders bilan merge.",
            "Xavf?",
            ["A) Yo‘q", "B) Qatorlar sun’iy ko‘payishi", "C) Faster", "D) Auto unique"],
            "B",
            difficulty="medium",
        ),
    ],
    "py-eda": [
        _quiz(
            "py-ex-insight",
            "Puzzle: insight",
            "Grafik chiroyli, lekin xulosa yo‘q.",
            "Nima yetishmayapti?",
            ["A) Hech narsa", "B) Aniq, tekshiriladigan biznes xulosasi", "C) Ko‘proq 3D", "D) Parol"],
            "B",
        ),
        _quiz(
            "py-ex-topn",
            "Puzzle: top-N",
            "40 ta kategoriya bar da siqilib qolgan.",
            "Yaxshiroq?",
            ["A) Top-10 + 'boshqalar'", "B) Barchasini pie", "C) Delete data", "D) Ignore"],
            "A",
            difficulty="medium",
        ),
    ],
    "py-capstone": [
        _quiz(
            "py-ex-cap-kpi",
            "Puzzle: 3 KPI",
            "Retail mini-loyiha.",
            "Minimal to‘plam?",
            [
                "A) Faqat pie",
                "B) Revenue, orders/unique mijoz, AOV (ta’rif bilan)",
                "C) Faqat abs(corr)",
                "D) Random forest only",
            ],
            "B",
            difficulty="medium",
        ),
        _quiz(
            "py-ex-cap-rec",
            "Puzzle: tavsiya",
            "Region X da AOV tushgan.",
            "Yaxshi tavsiya?",
            [
                "A) 'Yaxshilang'",
                "B) 'X regionida chegirma/mix ni tekshiring; 2 hafta AOV kuzating'",
                "C) Drop region",
                "D) More 3D charts",
            ],
            "B",
            difficulty="hard",
        ),
    ],
}


def merge_python_practice(module: dict) -> dict:
    """Mavjud practice (1 ta) + EXTRA (2-chi mashq) → list."""
    practice = dict(module.get("practice") or {})
    merged = {}
    for lecture in module.get("lectures") or []:
        slug = lecture["slug"]
        items = []
        base = practice.get(slug)
        if base:
            items.append(base)
        extra = EXTRA_LECTURE_PRACTICE.get(slug)
        if extra:
            items.append(extra)
        if items:
            merged[slug] = items
    module["practice"] = merged
    return module


def merge_python_exercises(module: dict) -> dict:
    existing = list(module.get("exercises") or [])
    extra = MODULE_EXERCISES.get(module["slug"], [])
    # slug bo‘yicha dedupe
    seen = {ex["slug"] for ex in existing}
    for ex in extra:
        if ex["slug"] not in seen:
            existing.append(ex)
            seen.add(ex["slug"])
    module["exercises"] = existing
    return module
