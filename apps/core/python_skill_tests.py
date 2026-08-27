"""
Python (Data Analytics) — har modul uchun bilim testlari (11 ta, 4 variant).
Daraja: boshlang‘ich → o‘rta. O‘zbekcha.
"""


def _q(num: int, title: str, task: str, options: list[str], answer: str, editorial: str, difficulty: str = "easy"):
    assert answer in "ABCD"
    assert len(options) == 4
    return {
        "num": num,
        "title": title,
        "description": "Modul bilim testi. To‘g‘ri javobni tanlang.",
        "task": task,
        "kind": "quiz",
        "difficulty": difficulty,
        "is_skill_test": True,
        "quiz_options": options,
        "hints": ["Darsdagi asosiy g‘oyani eslang.", "Noto‘g‘ri variantlarni chiqarib tashlang."],
        "editorial": editorial,
        "columns": ["javob"],
        "rows": [[answer]],
    }


MODULE_SKILL_TESTS: dict[str, list[dict]] = {
    "py-asoslari": [
        _q(1, "Nima uchun Python?", "Tahlilchiga Python asosan nima uchun kerak?", [
            "A) Faqat o‘yin yozish", "B) Takrorlanadigan tozalash va hisobotni avtomatlashtirish",
            "C) Word o‘rniga", "D) Faqat veb-sayt dizayni",
        ], "B", "Python — takroriy tahlil ishlarini kodga aylantiradi."),
        _q(2, "Excel vs Python", "Har oy 20 ta CSV ni bir xil qoida bilan tozalash — eng yaxshi vosita?", [
            "A) Har safar qo‘lda Excel", "B) Python/Pandas skripti", "C) Faqat kalkulyator", "D) PowerPoint",
        ], "B", "Ko‘p fayl + bir xil qoida = skript."),
        _q(3, "int turi", "orders = 12  — bu qaysi tur?", [
            "A) str", "B) int", "C) list", "D) dict",
        ], "B", "Butun son — int."),
        _q(4, "str ko‘paytirish", 'amount = "100"; amount * 2 natijasi?', [
            "A) 200", "B) '100100'", "C) Xato doim", "D) None",
        ], "B", "Matn * 2 — matnni ikki marta yozadi; avval float/int ga o‘tkazing."),
        _q(5, "type()", "O‘zgaruvchi turini bilish uchun nima ishlatiladi?", [
            "A) typeof()", "B) type()", "C) classof()", "D) kind()",
        ], "B", "Python da type()."),
        _q(6, "f-string", 'f"AOV: {aov}" nima qiladi?', [
            "A) Fayl ochadi", "B) Matnga o‘zgaruvchi qiymatini joylaydi", "C) Jadval o‘chiradi", "D) Loop yaratadi",
        ], "B", "f-string — formatlash."),
        _q(7, "Foiz o‘zgarish", "Yangi 80, eski 100. To‘g‘ri formula?", [
            "A) yangi / eski", "B) (yangi - eski) / eski", "C) eski - yangi", "D) yangi * eski",
        ], "B", "O‘zgarish = (yangi − eski) / eski."),
        _q(8, "None", "None nima anglatadi?", [
            "A) 0", "B) Bo‘sh matn", "C) Qiymat yo‘qligi", "D) True",
        ], "C", "None — qiymat mavjud emas."),
        _q(9, "bool", "bool(0) natijasi?", [
            "A) True", "B) False", "C) 0", "D) None",
        ], "B", "0, bo‘sh matn, None — False hisoblanadi."),
        _q(10, "Notebook", "Jupyter Notebook asosan nima uchun?", [
            "A) Faqat PDF o‘qish", "B) Tadqiqot: kod + natija + izoh bir joyda", "C) Video montaj", "D) Tarmoq sozlash",
        ], "B", "Notebook — tahlil tadqiqoti uchun qulay."),
        _q(11, "Professional odat", "Xom CSV bilan ishlashda eng to‘g‘ri?", [
            "A) Xom faylni to‘g‘ridan o‘zgartirish", "B) raw/ nusxa saqlab, tozalangan nusxa bilan ishlash",
            "C) Parolni kodga yozish", "D) Natijani hech qachon saqlamaslik",
        ], "B", "Xom ma’lumotni saqlang, tozalashni alohida qiling.", "medium"),
    ],
    "py-mantiq": [
        _q(1, "if sharti", "if amount > 0:  — bu nima?", [
            "A) Tayinlash", "B) Shart tekshiruvi", "C) Loop", "D) Import",
        ], "B", "if — shart."),
        _q(2, "== vs =", "Taqqoslash uchun to‘g‘ri belgi?", [
            "A) =", "B) ==", "C) :=", "D) === faqat",
        ], "B", "= tayinlash, == taqqoslash."),
        _q(3, "elif", "elif nima uchun?", [
            "A) Import", "B) Qo‘shimcha shart tarmog‘i", "C) Fayl yopish", "D) Print o‘chirish",
        ], "B", "elif — aks holda agar."),
        _q(4, "and", 'city == "Toshkent" and amount > 0  True bo‘lishi uchun?', [
            "A) Faqat city to‘g‘ri", "B) Ikkala shart ham True", "C) Faqat amount", "D) Hech qachon",
        ], "B", "and — ikkalasi ham."),
        _q(5, "for", "for x in [1,2,3]: nima qiladi?", [
            "A) Faqat bir marta", "B) Har element uchun blokni bajaradi", "C) Jadval o‘chiradi", "D) Random tanlaydi",
        ], "B", "for — iteratsiya."),
        _q(6, "while xavfi", "while True: ichida hisoblagich o‘zgarmasa?", [
            "A) Yaxshi", "B) Cheksiz tsikl xavfi", "C) Avtomatik break", "D) Python o‘chadi xavfsiz",
        ], "B", "Shart hech o‘zgarmasa — osilib qoladi."),
        _q(7, "funksiya", "def aov(revenue, orders): ...  nima beradi?", [
            "A) Qayta ishlatiladigan blok", "B) Faqat izoh", "C) CSV o‘qish", "D) Grafik",
        ], "A", "def — funksiya e’loni."),
        _q(8, "return", "return nima qiladi?", [
            "A) Print qiladi doim", "B) Funksiyadan qiymat qaytaradi", "C) Loop boshlaydi", "D) Fayl ochadi",
        ], "B", "return — natijani qaytarish."),
        _q(9, "Segment", "revenue >= 10mln → VIP. Bu qayerda yoziladi?", [
            "A) Faqat Excel da majburiy", "B) if/elif bilan funksiyada", "C) Faqat SQL DELETE", "D) HTML da",
        ], "B", "Biznes qoidasi — if bilan."),
        _q(10, "Katta jadval", "Million qatorni sof Python for da yig‘ish?", [
            "A) Eng tez usul", "B) Odatda sekin; Pandas vektorlash afzal", "C) Mumkin emas", "D) Faqat while",
        ], "B", "Katta data → Pandas.", "medium"),
        _q(11, "enumerate", "enumerate(rows) nima beradi?", [
            "A) Faqat qiymat", "B) Indeks va qiymat juftligi", "C) Faqat uzunlik", "D) Random",
        ], "B", "enumerate — (i, item).", "medium"),
    ],
    "py-tuzilma": [
        _q(1, "list", "prices = [10, 20, 30]  — bu nima?", [
            "A) dict", "B) list", "C) set", "D) tuple faqat",
        ], "B", "Kvadrat qavs — list."),
        _q(2, "indeks", "prices[0] nima?", [
            "A) Oxirgi element", "B) Birinchi element", "C) Uzunlik", "D) Xato doim",
        ], "B", "Indeks 0 dan boshlanadi."),
        _q(3, "dict", "Mijoz = {\"id\": 1, \"city\": \"Samarqand\"} — bu?", [
            "A) list", "B) dict (kalit→qiymat)", "C) int", "D) set",
        ], "B", "dict — mapping."),
        _q(4, "dict kalit", 'mijoz["city"] nima beradi?', [
            "A) id", "B) city qiymati", "C) Butun dict", "D) None doim",
        ], "B", "Kalit orqali qiymat."),
        _q(5, "list append", "Ro‘yxatga element qo‘shish?", [
            "A) add()", "B) append()", "C) push()", "D) insert_only()",
        ], "B", "list.append()."),
        _q(6, "len", "len(prices) nima?", [
            "A) Yig‘indi", "B) Elementlar soni", "C) O‘rtacha", "D) Max",
        ], "B", "len — uzunlik."),
        _q(7, "tuple", "(1, 2) odatda nima?", [
            "A) O‘zgarmas ketma-ketlik (tuple)", "B) dict", "C) set", "D) DataFrame",
        ], "A", "tuple odatda immutable."),
        _q(8, "set", "set nima uchun foydali?", [
            "A) Tartibli jadval", "B) Unikal qiymatlar to‘plami", "C) Grafik", "D) SQL join",
        ], "B", "set — unikal."),
        _q(9, "JSON g‘oya", "API dan kelgan mijoz yozuvi ko‘pincha qaysi tuzilma?", [
            "A) Faqat int", "B) dict / nested dict", "C) Faqat print", "D) HTML table majburiy",
        ], "B", "JSON → dict."),
        _q(10, "list comprehension", "[x*2 for x in nums] nima?", [
            "A) Loop ni qisqa yozish", "B) Fayl o‘qish", "C) Import", "D) Delete",
        ], "A", "Comprehension — qisqa list yaratish.", "medium"),
        _q(11, "Kalit yo‘q", 'd.get("region", "Noma’lum")  afzalligi?', [
            "A) Doim xato", "B) Kalit bo‘lmasa default qaytaradi", "C) List yaratadi", "D) Loop",
        ], "B", "get — xavfsiz o‘qish.", "medium"),
    ],
    "py-numpy": [
        _q(1, "NumPy nima?", "NumPy asosan nima uchun?", [
            "A) Matn muharriri", "B) Tezkor massiv/hisob-kitob", "C) Brauzer", "D) Email",
        ], "B", "NumPy — numeric arrays."),
        _q(2, "import", "Odatdagi import?", [
            "A) import numpy as np", "B) import excel as np", "C) from sql import np", "D) include numpy",
        ], "A", "import numpy as np."),
        _q(3, "array", "np.array([1,2,3]) nima beradi?", [
            "A) dict", "B) ndarray", "C) DataFrame", "D) str",
        ], "B", "NumPy array."),
        _q(4, "shape", "arr.shape nima?", [
            "A) Rang", "B) O‘lcham (qator, ustun…)", "C) Sum", "D) dtype nomi faqat",
        ], "B", "shape — o‘lcham."),
        _q(5, "mean", "np.mean(x) nima?", [
            "A) Mediana", "B) O‘rtacha", "C) Max", "D) Std faqat",
        ], "B", "mean — o‘rtacha."),
        _q(6, "Vektorlash", "arr * 2 NumPy da nima qiladi?", [
            "A) Faqat birinchi element", "B) Har elementni 2 ga ko‘paytiradi", "C) Matn qo‘shadi", "D) Xato",
        ], "B", "Element-wise amal."),
        _q(7, "nan", "np.nan nima?", [
            "A) 0", "B) Yetishmayotgan son qiymati", "C) True", "D) Bo‘sh list",
        ], "B", "NaN — missing numeric."),
        _q(8, "Pandas bog‘liqligi", "Pandas ichida ko‘p hisob nima ustida?", [
            "A) Faqat HTML", "B) NumPy massivlari", "C) Faqat Word", "D) PDF",
        ], "B", "Pandas NumPy ga tayanadi."),
        _q(9, "dtype", "dtype nima?", [
            "A) Fayl nomi", "B) Massiv elementlari turi", "C) Grafik turi", "D) URL",
        ], "B", "dtype — ma’lumot turi."),
        _q(10, "std", "np.std nima o‘lchaydi?", [
            "A) Yig‘indi", "B) Tarqoqlik (standart og‘ish)", "C) Min", "D) Count",
        ], "B", "std — dispersion.", "medium"),
        _q(11, "Boolean mask", "arr[arr > 0] nima?", [
            "A) Sort", "B) Shartga mos elementlar", "C) Delete all", "D) Import",
        ], "B", "Boolean indexing.", "medium"),
    ],
    "py-pandas": [
        _q(1, "DataFrame", "pd.DataFrame nima?", [
            "A) Bitta son", "B) Jadval (qator×ustun)", "C) Faqat grafik", "D) Matn fayl",
        ], "B", "DataFrame — asosiy jadval."),
        _q(2, "read_csv", "CSV o‘qish?", [
            "A) pd.read_csv(...)", "B) pd.open_excel_only", "C) np.csv()", "D) sql.read",
        ], "A", "pd.read_csv."),
        _q(3, "head", "df.head() nima?", [
            "A) Oxirgi 5", "B) Birinchi qatorlar (default 5)", "C) Schema drop", "D) Plot",
        ], "B", "head — ko‘rib chiqish."),
        _q(4, "columns", "df.columns nima beradi?", [
            "A) Ustun nomlari", "B) Faqat qator soni", "C) Parol", "D) Index type faqat",
        ], "A", "columns — ustunlar."),
        _q(5, "shape", "df.shape → (100, 5) nima?", [
            "A) 100 ustun, 5 qator", "B) 100 qator, 5 ustun", "C) Fayl hajmi MB", "D) NaN soni",
        ], "B", "(rows, cols)."),
        _q(6, "filtr", "df[df['amount'] > 0] nima?", [
            "A) Sort", "B) Shart bo‘yicha qatorlar", "C) Drop columns", "D) Merge",
        ], "B", "Boolean filter."),
        _q(7, "loc/iloc", "iloc asosan nima?", [
            "A) Nom bo‘yicha", "B) Pozitsiya (raqam) bo‘yicha tanlash", "C) SQL join", "D) Plot",
        ], "B", "iloc — integer location."),
        _q(8, "dtype tekshiruv", "df.dtypes nima uchun?", [
            "A) Rang", "B) Har ustun turi", "C) Unique cities", "D) Password",
        ], "B", "dtypes — turlar."),
        _q(9, "Series", "Bitta ustun odatda nima?", [
            "A) Series", "B) set", "C) tuple faqat", "D) HTML",
        ], "A", "Series — 1D."),
        _q(10, "assign", "Yangi ustun yaratish odatiy usul?", [
            "A) df['aov'] = df['revenue'] / df['orders']", "B) df.delete('aov')", "C) np.plot", "D) print only",
        ], "A", "Yangi ustun = hisob.", "medium"),
        _q(11, "info()", "df.info() nima beradi?", [
            "A) Faqat sum", "B) Ustunturi, non-null, xotira haqida qisqa ma’lumot", "C) PDF", "D) API key",
        ], "B", "info — tezkor diagnostika.", "medium"),
    ],
    "py-clean": [
        _q(1, "NaN", "Pandas da yetishmayotgan qiymat ko‘pincha?", [
            "A) NaN / None", "B) 999999 doim", "C) True", "D) 'NULL' matn faqat",
        ], "A", "NaN — missing."),
        _q(2, "isna", "Yetishmovchilikni topish?", [
            "A) df.isna()", "B) df.plot_all()", "C) df.sql()", "D) df.password()",
        ], "A", "isna / isnull."),
        _q(3, "dropna", "dropna nima qiladi?", [
            "A) NaN qator/ustunni tashlaydi (parametrga qarab)", "B) Random qo‘shadi", "C) Sort", "D) Merge",
        ], "A", "dropna — olib tashlash."),
        _q(4, "fillna", "fillna(0) nima?", [
            "A) NaN ni 0 bilan to‘ldirish", "B) 0 ni o‘chirish", "C) Plot", "D) Join",
        ], "A", "fillna — to‘ldirish."),
        _q(5, "dublikat", "Bir xil order_id ikki marta — nima?", [
            "A) Yaxshi", "B) Dublikat — tekshirish/drop_duplicates kerak", "C) NaN emas", "D) dtype",
        ], "B", "Dublikat kalit xavfli."),
        _q(6, "astype", "amount matndan songa?", [
            "A) astype(float) / to_numeric", "B) dropna only", "C) head()", "D) pivot",
        ], "A", "Tur konversiyasi."),
        _q(7, "to_numeric", "pd.to_numeric(..., errors='coerce') nima qiladi?", [
            "A) Xato matnni NaN qiladi", "B) Hammasini o‘chiradi", "C) SQL yozadi", "D) True qiladi",
        ], "A", "coerce — xatolarni NaN."),
        _q(8, "strip", "Shahar nomida bo‘sh joy: ' Toshkent ' — nima qilish?", [
            "A) strip() / str.strip", "B) drop column", "C) mean()", "D) iloc[999]",
        ], "A", "Matnni tozalash."),
        _q(9, "Jurnal", "Tozalashda professional odat?", [
            "A) Hech narsa yozmaslik", "B) Nechta qator tashlangani / nima o‘zgarganini yozish", "C) Faqat pie chart", "D) Parol saqlash",
        ], "B", "Cleaning log."),
        _q(10, "Siyosat", "3% NaN amount da — nima qilish kerak?", [
            "A) Doim o‘ylab ko‘rmasdan dropna", "B) Biznes qoidasi: tashlash / to‘ldirish / alohida flag", "C) Ignore forever", "D) Multiply by 0",
        ], "B", "Siyosat aniq bo‘lsin.", "medium"),
        _q(11, "Ketma-ketlik", "Eng mantiqiy tartib?", [
            "A) Model → tozalash", "B) Turlar → missing → dublikat → KPI", "C) Plot → raw overwrite", "D) Delete all rows",
        ], "B", "Avval toza, keyin tahlil.", "medium"),
    ],
    "py-agg": [
        _q(1, "groupby", "df.groupby('region') nima?", [
            "A) Sort only", "B) Guruhlash", "C) Drop", "D) Plot 3D",
        ], "B", "groupby — guruh."),
        _q(2, "sum", "Guruh bo‘yicha yig‘indi?", [
            "A) .sum()", "B) .head()", "C) .info()", "D) .isna()",
        ], "A", "agg sum."),
        _q(3, "agg", ".agg({'amount':'sum','order_id':'nunique'}) nima?", [
            "A) Bir nechta agregat birga", "B) Faqat plot", "C) Delete", "D) Merge reverse",
        ], "A", "agg — ko‘p metrika."),
        _q(4, "nunique", "nunique nima o‘lchaydi?", [
            "A) NaN soni", "B) Unikal qiymatlar soni", "C) Max length string", "D) File size",
        ], "B", "nunique — distinct count."),
        _q(5, "merge", "Ikki jadvalni kalit bo‘yicha birlashtirish?", [
            "A) merge / join", "B) dropna", "C) head", "D) dtype",
        ], "A", "pd.merge."),
        _q(6, "how='left'", "left join g‘oyasi?", [
            "A) Chap jadvaldagi barcha qatorlar saqlanadi", "B) Faqat o‘ng", "C) O‘chirish", "D) Random sample",
        ], "A", "left — chap asos."),
        _q(7, "pivot_table", "pivot_table nima uchun?", [
            "A) Kesimli jamlanma jadval", "B) Parol", "C) Git", "D) CSS",
        ], "A", "Pivot — summary."),
        _q(8, "reset_index", "groupby dan keyin reset_index nima uchun?", [
            "A) Guruh kalitini oddiy ustunga qaytarish", "B) Delete data", "C) Plot color", "D) SQL inject",
        ], "A", "Index → column."),
        _q(9, "AOV guruhda", "Region bo‘yicha AOV?", [
            "A) sum(amount)/nunique(order_id) (ta’rifga qarab)", "B) mean(city)", "C) len(columns)", "D) drop_duplicates only",
        ], "A", "AOV = revenue / orders.", "medium"),
        _q(10, "Ko‘p kalit", "groupby(['region','channel']) nima?", [
            "A) Bitta guruh", "B) Ikki o‘lchovli guruhlash", "C) Error doim", "D) Only numeric index",
        ], "B", "Multi-key groupby.", "medium"),
        _q(11, "Xato join", "Kalit dublikat bo‘lsa merge da nima bo‘lishi mumkin?", [
            "A) Hech narsa", "B) Qatorlar ko‘payib ketishi (fan-out)", "C) Avtomatik drop", "D) Faster always",
        ], "B", "Join oldidan kalitni tekshiring.", "medium"),
    ],
    "py-eda": [
        _q(1, "EDA", "EDA nima?", [
            "A) Faqat model deploy", "B) Ma’lumotni o‘rganish: taqsimot, outlier, bog‘liqlik", "C) Parol reset", "D) CSS",
        ], "B", "Exploratory Data Analysis."),
        _q(2, "describe", "df.describe() nima beradi?", [
            "A) Sonli ustunlarning qisqa statistikasi", "B) HTML", "C) API token", "D) Git log",
        ], "A", "describe — summary stats."),
        _q(3, "value_counts", "value_counts nima uchun?", [
            "A) Kategoriyalar chastotasi", "B) Merge", "C) Dropna reverse", "D) f-string",
        ], "A", "Chastota jadvali."),
        _q(4, "hist", "Miqdoriy taqsimot uchun oddiy grafik?", [
            "A) Histogram", "B) Pie 50 bo‘lak", "C) Word cloud only", "D) 3D map majburiy",
        ], "A", "hist — taqsimot."),
        _q(5, "bar", "Region bo‘yicha revenue solishtirish?", [
            "A) Bar chart", "B) FAQ only", "C) Binary tree", "D) CSS grid",
        ], "A", "Bar — kategoriya solishtirish."),
        _q(6, "line", "Vaqt bo‘yicha trend?", [
            "A) Line chart", "B) Pie", "C) Stack overflow", "D) QR code",
        ], "A", "Line — trend."),
        _q(7, "boxplot", "Outlier ko‘rish uchun?", [
            "A) Boxplot", "B) Pie 3D", "C) Title only", "D) print(df)",
        ], "A", "Boxplot — outlier."),
        _q(8, "Insight", "Yaxshi insight qanday?", [
            "A) 'Chiroyli grafik'", "B) Aniq, tekshiriladigan, harakatga yaroqli xulosa", "C) Faqat emoji", "D) Random guess",
        ], "B", "Insight = biznes qiymati."),
        _q(9, "matplotlib", "Odatdagi import?", [
            "A) import matplotlib.pyplot as plt", "B) import excel as plt", "C) from sql import plt", "D) include plot",
        ], "A", "plt — pyplot."),
        _q(10, "Korelatsiya", "df.corr() nima haqida?", [
            "A) Sonli ustunlar o‘rtasidagi bog‘liqlik (ehtiyotkorlik bilan)", "B) Parol kuchliligi", "C) File path", "D) HTML id",
        ], "A", "corr — correlation.", "medium"),
        _q(11, "Overplot", "Juda ko‘p kategoriya pie da?", [
            "A) Ideal", "B) O‘qish qiyin — bar yoki top-N yaxshiroq", "C) Majburiy 3D", "D) Delete data",
        ], "B", "Oddiy vizual tanlang.", "medium"),
    ],
    "py-capstone": [
        _q(1, "KPI", "KPI nima?", [
            "A) Tasodifiy son", "B) Biznes uchun muhim o‘lchanadigan ko‘rsatkich", "C) CSS class", "D) Git branch",
        ], "B", "Key Performance Indicator."),
        _q(2, "AOV", "AOV odatda?", [
            "A) mijozlar / revenue", "B) revenue / buyurtmalar soni (ta’rifga qarab)", "C) mean(city)", "D) count NaN",
        ], "B", "Average Order Value."),
        _q(3, "Ta’rif", "“Faol mijoz” ta’rifi nima uchun muhim?", [
            "A) Muhim emas", "B) Hisobotlar zid kelmasligi uchun hujjatlashtirish kerak", "C) Faqat dizayn", "D) SQL DROP",
        ], "B", "Ta’rif = ishonch."),
        _q(4, "Recency", "120 kundan beri xarid yo‘q — signal?", [
            "A) Albatta firibgar", "B) Churn / qayta faollashtirish xavfi (chegara biznes bilan)", "C) AOV oshgan", "D) Join xato",
        ], "B", "Recency — sodda churn signal."),
        _q(5, "Deliverable", "Yakuniy loyihada eng muhimi?", [
            "A) 20 ta 3D chart", "B) Toza pipeline + aniq KPI + harakatga yaroqli tavsiya", "C) Faqat print(df)", "D) Parolni kodga",
        ], "B", "Sifatli tahlil yetkazib berish."),
        _q(6, "Tozalash jurnali", "Nima yoziladi?", [
            "A) Hech narsa", "B) Qatorlar soni, tashlanganlar, qoidalar", "C) Faqat emoji", "D) Admin parol",
        ], "B", "Reproducible cleaning."),
        _q(7, "Tavsiya", "Yaxshi tavsiya qanday?", [
            "A) 'Yaxshilash kerak'", "B) Aniq: kim, nima, qachon, qanday o‘lchash", "C) Faqat grafik rangi", "D) Random",
        ], "B", "Actionable recommendation."),
        _q(8, "Pipeline", "Qayta ishlatiladigan tahlil nima demak?", [
            "A) Har safar qo‘lda boshidan", "B) Funksiya/parametr bilan qayta ishga tushirish mumkin", "C) Faqat screenshot", "D) One-off Excel without save",
        ], "B", "Automation mindset."),
        _q(9, "Kesim", "Region × kanal pivot nima beradi?", [
            "A) Kesimli performance ko‘rinishi", "B) Parol", "C) DNS", "D) CSS",
        ], "A", "Segment performance."),
        _q(10, "Tekshiruv", "KPI g‘alati katta chiqsa birinchi qadam?", [
            "A) Darhol biznesga yuborish", "B) Filtr, dublikat, tur, join fan-out ni tekshirish", "C) Ignore", "D) Drop database",
        ], "B", "Sanity check.", "medium"),
        _q(11, "Capstone tartib", "Eng to‘g‘ri ketma-ketlik?", [
            "A) Vizual → xom overwrite → KPI", "B) Tozalash → KPI/agg → vizual → tavsiya", "C) Model without data", "D) Only pie charts",
        ], "B", "Clean → measure → explain.", "medium"),
    ],
}


def skill_tests_for_module(module_slug: str) -> list[dict]:
    items = MODULE_SKILL_TESTS.get(module_slug, [])
    result = []
    for item in items:
        data = dict(item)
        num = data.pop("num")
        data["slug"] = f"bt-{module_slug}-{num:02d}"
        result.append(data)
    return result
