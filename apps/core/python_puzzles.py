"""
Python Data Analytics — dars mashqlari va modul “puzzle” testlari.
Boshlang‘ich → o‘rta (CodeChef/W3 style, lekin analyticsga mos).
"""

from apps.core.python_content import _quiz


# Har dars uchun qo‘shimcha (2-chi) mashq — medium
EXTRA_LECTURE_PRACTICE: dict[str, dict] = {
    "py-noldan-start": _quiz(
        "py-p-noldan-repl",
        "Puzzle: REPL",
        "Sinov.",
        "Bitta qatorni tez sinash uchun qulay?",
        [
            "A) Faqat Word",
            "B) Python REPL yoki Notebook katak",
            "C) Faqat printer",
            "D) Email",
        ],
        "B",
        difficulty="medium",
    ),
    "py-noldan-run": _quiz(
        "py-p-noldan-ext",
        "Puzzle: fayl kengaytmasi",
        "Skript.",
        "Python skript fayli odatda qaysi kengaytma?",
        ["A) .docx", "B) .py", "C) .jpg", "D) .sql"],
        "B",
        difficulty="easy",
    ),
    "py-noldan-errors": _quiz(
        "py-p-noldan-name",
        "Puzzle: NameError",
        "amount deb yozilgan, lekin kodda amout ishlatilgan.",
        "Bu qanday xato?",
        ["A) SyntaxError", "B) NameError", "C) FileNotFoundError", "D) ImportError"],
        "B",
        difficulty="medium",
    ),
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
        "VIP >= 10mln, Regular >= 2mln, aks holda New. revenue=2000000.",
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
    "py-noldan": [
        _quiz(
            "py-ex-noldan-path",
            "Puzzle: ishga tushirish",
            "Skript ishlamayapti.",
            "Birinchi tekshiruv?",
            [
                "A) To‘g‘ri papkada python fayl.py",
                "B) Kompyuterni formatlash",
                "C) Internet tezligini oshirish",
                "D) Excelni qayta o‘rnatish",
            ],
            "A",
            difficulty="easy",
        ),
        _quiz(
            "py-ex-noldan-fix",
            "Puzzle: tuzatish",
            "SyntaxError: unterminated string.",
            "Ehtimol sabab?",
            [
                "A) Qo‘shtirnoq yopilmagan",
                "B) CPU yetishmaydi",
                "C) Pandas yo‘q",
                "D) Wi-Fi",
            ],
            "A",
            difficulty="medium",
        ),
    ],
    "py-asoslari": [
        _quiz(
            "py-ex-repl-vs-file",
            "Puzzle: REPL vs fayl",
            "Har dushanba bir xil hisobot skripti kerak.",
            "Nima saqlab qo‘yish kerak?",
            [
                "A) .py skript fayl (versiya nazorati bilan)",
                "B) Faqat REPL tarixidagi qatorlar",
                "C) Word hujjat",
                "D) Skrinshot",
            ],
            "A",
            difficulty="easy",
        ),
        _quiz(
            "py-ex-str-int",
            "Puzzle: input",
            "Foydalanuvchi kiritgan '250' matn.",
            "Son sifatida ishlatish?",
            ["A) int('250')", "B) '250' + 1", "C) str(250) + str(1)", "D) Hech narsa"],
            "A",
            difficulty="medium",
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
        _quiz(
            "py-ex-segment-order",
            "Puzzle: tartib",
            "Avval Regular (>=2mln), keyin VIP (>=10mln) yozilgan.",
            "Nima bo‘ladi?",
            [
                "A) VIP to‘g‘ri ishlaydi",
                "B) 10mln+ ham Regular ga tushishi mumkin — avval katta chegara",
                "C) SyntaxError",
                "D) Hech narsa",
            ],
            "B",
            difficulty="hard",
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
            "py-ex-tuple-key",
            "Puzzle: tuple kalit",
            "(region, month) juftligini dict kaliti sifatida ishlatmoqchisiz.",
            "Qaysi tur mos?",
            ["A) tuple", "B) list", "C) set", "D) dict ichida dict"],
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
            "py-ex-head-tail",
            "Puzzle: tekshiruv",
            "Yangi CSV keldi, 50 ming qator.",
            "Birinchi qadam?",
            [
                "A) df.head() va df.info() bilan ustun/tur ko‘rish",
                "B) Darhol groupby",
                "C) Barcha qatorni print",
                "D) Faylni o‘chirish",
            ],
            "A",
            difficulty="easy",
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
        _quiz(
            "py-ex-setting-copy",
            "Puzzle: SettingWithCopy",
            "tosh = df[df.city=='Toshkent']; tosh['vat']=1",
            "Xavfsizroq?",
            [
                "A) Shu usul yaxshi",
                "B) df.loc[mask, 'vat'] = ... yoki assign",
                "C) del df",
                "D) while True",
            ],
            "B",
            difficulty="hard",
        ),
    ],
    "py-clean": [
        _quiz(
            "py-ex-audit-trail",
            "Puzzle: jurnal",
            "Qaysi qator o‘chirilganini keyin bilmoqchisiz.",
            "Yaxshi amaliyot?",
            [
                "A) Tozalash qadamini alohida jurnal faylga yozish",
                "B) Xom CSV ni ustiga yozish",
                "C) Hech narsa saqlamaslik",
                "D) Faqat grafik",
            ],
            "A",
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
        _quiz(
            "py-ex-nan-zero",
            "Puzzle: NaN siyosati",
            "amount NaN ni 0 qilib AOV hisoblandi — o‘rtacha tushdi.",
            "Asosiy muammo?",
            [
                "A) Pandas bug",
                "B) Noma’lum va haqiqiy 0 aralashdi — avval flag, keyin qoida",
                "C) Encoding",
                "D) GPU",
            ],
            "B",
            difficulty="hard",
        ),
    ],
    "py-agg": [
        _quiz(
            "py-ex-pivot-table",
            "Puzzle: pivot jadval",
            "Region × oy matritsasi kerak (qator=region, ustun=oy, qiymat=sum).",
            "Pandas usuli?",
            ["A) pivot_table", "B) faqat head()", "C) dropna()", "D) str.upper"],
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
        _quiz(
            "py-ex-aov-join",
            "Puzzle: AOV join",
            "Merge dan keyin revenue 2× katta, orders ham ko‘paygan.",
            "Birinchi tekshiruv?",
            [
                "A) Pie chart",
                "B) Kalit dublikat / fan-out — merge oldidan nunique tekshirish",
                "C) Drop database",
                "D) Ignore",
            ],
            "B",
            difficulty="hard",
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
        _quiz(
            "py-ex-corr-trap",
            "Puzzle: korrelyatsiya",
            "corr = 0.9 ikki ustun.",
            "To‘g‘ri xulosa?",
            [
                "A) Aniq sabab-oqibat",
                "B) Kuchli bog‘liqlik signal — sababni alohida tekshirish kerak",
                "C) Drop both columns",
                "D) Always fraud",
            ],
            "B",
            difficulty="hard",
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
        _quiz(
            "py-ex-cap-pipeline",
            "Puzzle: pipeline",
            "Har oy bir xil CSV keladi.",
            "Eng to‘g‘ri?",
            [
                "A) Har safar qo‘lda Notebook",
                "B) Parametrli skript/funksiya + tozalash jurnali + qayta ishga tushirish",
                "C) Faqat screenshot",
                "D) One-off Excel without save",
            ],
            "B",
            difficulty="hard",
        ),
    ],
}


def _quiz_blob(quiz: dict) -> str:
    parts = [
        quiz.get("slug") or "",
        quiz.get("title") or "",
        quiz.get("description") or "",
        quiz.get("quiz_prompt") or quiz.get("task") or "",
    ]
    return " ".join(str(p) for p in parts).lower()


def _quiz_topic_fingerprint(quiz: dict) -> frozenset[str]:
    """Rough topic key — bir darsda ikki marta segment/encoding kabi takror bo‘lmasin."""
    blob = _quiz_blob(quiz)
    tags: set[str] = set()
    rules: tuple[tuple[str, tuple[str, ...]], ...] = (
        ("segment", ("segment", "vip", "regular", "10mln", "10 mln", "2mln")),
        ("encoding", ("encoding", "utf-8", "utf-8-sig", "mojibake", "buzilib", "cp1251")),
        ("bare_except", ("except:", "yalang", "yutib yubor", "yalang‘och")),
        ("boolean_mask", ("mask", "arr[arr", "x[x", "arr > 0")),
        ("recency", ("recency", "120 kun", "90 kun", "xarid qilmagan", "oxirgi xarid", "recency_days")),
        ("line_chart", ("line chart", "trendi", "oylik revenue", "oylik savdo")),
        ("boxplot", ("boxplot", "outlier")),
        ("foiz_change", ("foiz", "o‘zgarish", "yangi 45", "50→45", "aov 50")),
        ("unique_set", ("unique", "set(cities", "set(ids", "unikal")),
        ("aov_safety", ("orders = 0", "orders=0", "0 ga bo‘lish", "xavfsiz aov")),
        ("describe_eda", ("describe()", "taqsimot")),
        ("groupby_sum", ("groupby", "yig‘indisi")),
        ("merge_left", ("left merge", "how='left'", "how=\"left\"")),
        ("dup_drop", ("drop_duplicates", "dublikat")),
        ("coerce_numeric", ("to_numeric", "errors='coerce'", "coerce")),
        ("nan_mean", ("nanmean", "nan bo‘lsa")),
        ("shape_df", ("shape", "200 qator", "8 ustun")),
        ("pandas_and_filter", ("& (df", "df[(df")),
        ("capstone_order", ("loyiha tartibi", "birinchi ish", "xomni saqlash")),
        ("kpi_definition", ("kpi ta’rifi", "faol mijoz", "ta’rifni hujjat")),
    )
    for tag, needles in rules:
        if any(n in blob for n in needles):
            tags.add(tag)
    return frozenset(tags)


def merge_python_practice(module: dict) -> dict:
    """Asosiy mashq + faqat mavzusi takrorlanmagan qo‘shimcha puzzle."""
    practice = dict(module.get("practice") or {})
    merged = {}
    for lecture in module.get("lectures") or []:
        slug = lecture["slug"]
        items: list[dict] = []
        topic_tags: set[str] = set()
        base = practice.get(slug)
        if base:
            bases = [base] if isinstance(base, dict) else list(base)
            for q in bases:
                items.append(q)
                topic_tags |= set(_quiz_topic_fingerprint(q))
        extra = EXTRA_LECTURE_PRACTICE.get(slug)
        if extra:
            extra_tags = set(_quiz_topic_fingerprint(extra))
            if not (extra_tags & topic_tags):
                items.append(extra)
                topic_tags |= extra_tags
        if items:
            merged[slug] = items
    module["practice"] = merged
    return module


def merge_python_exercises(module: dict) -> dict:
    existing = list(module.get("exercises") or [])
    extra = MODULE_EXERCISES.get(module["slug"], [])
    seen_slugs = {ex["slug"] for ex in existing}
    module_tags: set[str] = set()
    practice = module.get("practice") or {}
    for items in practice.values():
        batch = items if isinstance(items, list) else [items]
        for q in batch:
            module_tags |= set(_quiz_topic_fingerprint(q))
    for ex in extra:
        if ex["slug"] in seen_slugs:
            continue
        ex_tags = set(_quiz_topic_fingerprint(ex))
        if ex_tags & module_tags:
            continue
        existing.append(ex)
        seen_slugs.add(ex["slug"])
        module_tags |= ex_tags
    module["exercises"] = existing
    return module
