"""
Python for Data Analytics — chuqur o‘zbekcha ma’ruzalar, kod namuna va testlar.
"""

COURSE_DESCRIPTION = (
    "Pythonni tahlilchi sifatida, noldan: o‘zgaruvchi, pandas, tozalash, grafik. "
    "Excelda qo‘lda qilgan ishingizni qayta-qayta ishlatiladigan kodga aylantirasiz. "
    "Har muhim mavzuda qisqa kod namunasi bor."
)


def _lec(title, slug, html, examples=None):
    return {"title": title, "slug": slug, "content": html.strip(), "sql_examples": examples or []}


def _quiz(slug, title, description, task, options, answer, hints=None, difficulty="easy"):
    return {
        "slug": slug,
        "title": title,
        "description": description.strip(),
        "task": task,
        "hints": hints or [],
        "kind": "quiz",
        "difficulty": difficulty,
        "quiz_options": options,
        "columns": ["answer"],
        "rows": [[answer]],
    }


def _hw(text):
    return text.strip()


MODULES = [
    {
        "order": 1,
        "title": "Python asoslari",
        "slug": "py-asoslari",
        "description": "Nima uchun tahlilchiga Python, o‘zgaruvchilar, turlar va ifodalar.",
        "lectures": [
            _lec(
                "Tahlilchi uchun Python",
                "py-nima",
                """
<h2>Dars maqsadi</h2>
<p>Pythonni “dasturlash tili” emas, balki <strong>takrorlanadigan tahlil laboratoriyasi</strong> sifatida ko‘rasiz: qachon Excel yetarli, qachon Python kerak.</p>

<h2>Biznes konteksti</h2>
<p>Haftalik savdo hisobotini har dushanba qo‘lda yig‘ish — xato va kechikish manbai. Python skripti CSV ni o‘qiydi, tozalaydi, KPI hisoblaydi va natijani Excel/Power BI ga chiqaradi. Bir marta yozasiz, har hafta ishlatasiz.</p>

<h2>Qachon Python?</h2>
<table>
  <tr><th>Vazifa</th><th>Excel</th><th>Python</th></tr>
  <tr><td>Tezkor 5 daqiqalik filtr</td><td>Qulay</td><td>Ortiqcha</td></tr>
  <tr><td>Har oy 12 ta faylni birlashtirish</td><td>Charchatadi</td><td>Ideal</td></tr>
  <tr><td>100 ming+ qator, bir nechta join</td><td>Sekin / xato</td><td>Pandas</td></tr>
  <tr><td>Statistik test, A/B</td><td>Cheklangan</td><td>scipy / statsmodels</td></tr>
</table>

<h2>Ish muhiti</h2>
<p>Tahlilchilar odatda Jupyter Notebook yoki VS Code + <code>.py</code> ishlatadi. Notebook — tadqiqot; skript — ishlab chiqarish (pipeline). Ikkisini ham biling.</p>

<h2>Professional odat</h2>
<ol>
  <li>Xom faylni o‘zgartirmang — nusxa yoki <code>raw/</code> papka.</li>
  <li>Har qadamni izohlang: nima qildingiz va nima uchun.</li>
  <li>Natijani qayta ishlatish mumkin qiling (funksiya, parametr).</li>
</ol>
""",
                examples=[
                    'print("Savdo tahlili boshlandi")\nregion = "Toshkent"\nprint(region)',
                ],
            ),
            _lec(
                "O‘zgaruvchilar va ma’lumot turlari",
                "py-turlar",
                """
<h2>Dars maqsadi</h2>
<p><code>int</code>, <code>float</code>, <code>str</code>, <code>bool</code>, <code>None</code> farqini bilasiz va tur xatosidan qanday qochishni ko‘rasiz.</p>

<h2>Nima uchun muhim?</h2>
<p>CSV dan kelgan <code>"1 200"</code> matn. Uni <code>amount * 1.12</code> qilsangiz — xato. Avval turini tozalash — tahlilning 40% vaqti.</p>

<h2>Asosiy turlar</h2>
<ul>
  <li><strong>int</strong> — butun son (buyurtma soni)</li>
  <li><strong>float</strong> — o‘nli (narx, foiz)</li>
  <li><strong>str</strong> — matn (viloyat, SKU)</li>
  <li><strong>bool</strong> — True/False (VIP flag)</li>
  <li><strong>None</strong> — qiymat yo‘q (SQL dagi NULL ga yaqin)</li>
</ul>

<h2>Tekshiruv</h2>
<p><code>type(x)</code>, <code>isinstance(x, (int, float))</code>. Matndan songa: <code>float(s.replace(" ", "").replace(",", "."))</code> — lekin locale ni unutmang.</p>

<h2>Xato</h2>
<p><code>True + 1</code> Python da 2 beradi. Hisobotda boolean ni songa aralashtirmang — avval aniq flag yarating.</p>
""",
                examples=[
                    'revenue = 12_500_000\norders = 250\naov = revenue / orders\nprint(type(aov), round(aov, 2))',
                ],
            ),
            _lec(
                "Ifodalar va chop etish",
                "py-ifodalar",
                """
<h2>Dars maqsadi</h2>
<p>Arifmetika, f-string va yaxlitlash bilan o‘qiladigan KPI chiqarasiz.</p>

<h2>f-string</h2>
<p>Hisobot matni: <code>f"AOV: {aov:,.0f} so‘m"</code>. Rahbar sonni, tahlilchi esa formatni boshqaradi.</p>

<h2>Taqqoslash</h2>
<p><code>==</code> tenglik, <code>!=</code> teng emas, <code>&gt;</code> <code>&lt;</code>. Matn taqqoslash katta-kichik harfga sezgir: avval <code>.casefold()</code>.</p>

<h2>Biznes misol</h2>
<p>Agar AOV o‘tgan oydan 10% past bo‘lsa — ogohlantirish chiqaring. Bu keyingi darsdagi shartlarning ildizi.</p>
""",
                examples=[
                    'aov = 50000\nprev = 56000\nchange = (aov - prev) / prev\nprint(f"AOV o‘zgarishi: {change:.1%}")',
                ],
            ),
        ],
        "practice": {
            "py-nima": _quiz(
                "py-q-when",
                "Qachon Python?",
                "Har oy 24 ta filial CSV sini bir xil qoidalar bilan tozalash kerak.",
                "Eng to‘g‘ri vosita?",
                [
                    "A) Har safar qo‘lda Excel",
                    "B) Python/Pandas skripti + qayta ishga tushirish",
                    "C) Faqat Word jadvali",
                    "D) Faqat kalkulyator",
                ],
                "B",
            ),
            "py-turlar": _quiz(
                "py-q-str-num",
                "Tur xatosi",
                'amount = "150000"  (qo‘shtirnoq ichida)',
                "amount * 2 natijasi nima bo‘ladi?",
                [
                    "A) 300000",
                    "B) Matn ikki marta takrorlanadi: '150000150000'",
                    "C) Xato, dastur o‘chadi doim",
                    "D) None",
                ],
                "B",
            ),
            "py-ifodalar": _quiz(
                "py-q-pct",
                "Foiz o‘zgarish",
                "Yangi 45, eski 50.",
                "To‘g‘ri formula?",
                [
                    "A) yangi / eski",
                    "B) (yangi - eski) / eski",
                    "C) eski - yangi",
                    "D) yangi * eski",
                ],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "Jupyter yoki .py faylda:\n"
            "1) region, revenue, orders o‘zgaruvchilarini yarating.\n"
            "2) AOV hisoblang va f-string bilan chiqaring.\n"
            "3) type() bilan har bir o‘zgaruvchi turini yozing.\n"
            "Natija skrinshotini yoki kodni uy vazifasiga yuklang."
        ),
    },
    {
        "order": 2,
        "title": "Shartlar, tsikllar, funksiyalar",
        "slug": "py-mantiq",
        "description": "if/elif, for/while, qayta ishlatiladigan funksiyalar.",
        "lectures": [
            _lec(
                "Shartlar: if, elif, else",
                "py-if",
                """
<h2>Dars maqsadi</h2>
<p>Mijozni segmentga ajratish va flag yaratishni shartlar bilan yozasiz.</p>

<h2>Biznes qoida</h2>
<pre>agar revenue &gt;= 10 mln → "VIP"
aks holda agar revenue &gt;= 2 mln → "Regular"
aks holda → "New"</pre>
<p>Bu Excel IF ga o‘xshaydi, lekin o‘qish osonroq va test qilish mumkin.</p>

<h2>and / or / not</h2>
<p><code>city == "Toshkent" and amount &gt; 0</code>. Bo‘sh satr va 0 ni True deb hisoblamang — aniq solishtiring.</p>

<h2>Xato</h2>
<p><code>if amount = 0</code> — bu tayinlash, taqqoslash emas. Taqqoslash: <code>==</code>.</p>
""",
                examples=[
                    'def segment(revenue):\n    if revenue >= 10_000_000:\n        return "VIP"\n    if revenue >= 2_000_000:\n        return "Regular"\n    return "New"\nprint(segment(3_500_000))',
                ],
            ),
            _lec(
                "Tsikllar: for va while",
                "py-loop",
                """
<h2>Dars maqsadi</h2>
<p>Ro‘yxat bo‘ylab yurib, yig‘indi va filtrlashni tushunasiz. Keyin Pandas buni vektorlab qiladi — lekin mantiq shu yerda tug‘iladi.</p>

<h2>for</h2>
<p><code>for row in rows:</code> — har bir element. <code>enumerate</code> indeks kerak bo‘lsa. <code>zip</code> ikki ro‘yxatni juftlaydi.</p>

<h2>while</h2>
<p>Shart to‘g‘ri ekan takrorlash. Cheksiz tsikldan ehtiyot: hisoblagich o‘zgarmasa — osilib qoladi.</p>

<h2>Tahlilchi maslahati</h2>
<p>Million qatorni Python <code>for</code> da yig‘ish sekin. Kichik logika va o‘rganish uchun for; katta jadval uchun Pandas.</p>
""",
                examples=[
                    'amounts = [120000, 45000, 80000]\ntotal = 0\nfor a in amounts:\n    if a >= 50000:\n        total += a\nprint(total)',
                ],
            ),
            _lec(
                "Funksiyalar",
                "py-func",
                """
<h2>Dars maqsadi</h2>
<p>Takrorlanadigan hisobni funksiyaga chiqarasiz: nom, argument, return, docstring.</p>

<h2>Nima uchun?</h2>
<p>AOV ni 12 joyda qo‘lda yozsangiz — birini unutasiz. <code>def aov(revenue, orders):</code> — bitta haqiqat.</p>

<h2>Qoidalar</h2>
<ul>
  <li>Nom fe’l yoki aniq ot: <code>clean_amount</code>, <code>monthly_growth</code></li>
  <li>0 ga bo‘lishni tekshiring</li>
  <li>Yon effekt (print, fayl yozish) va hisobni aralashtirmang</li>
</ul>
""",
                examples=[
                    'def aov(revenue, orders):\n    """Average order value. orders=0 bo‘lsa None."""\n    if orders == 0:\n        return None\n    return revenue / orders\nprint(aov(1_200_000, 40))',
                ],
            ),
        ],
        "practice": {
            "py-if": _quiz(
                "py-q-if",
                "Segment",
                "revenue = 2_000_000, qoida: >=10mln VIP, >=2mln Regular.",
                "Natija?",
                ["A) VIP", "B) Regular", "C) New", "D) Xato"],
                "B",
            ),
            "py-loop": _quiz(
                "py-q-loop",
                "for vs Pandas",
                "2 million qatorli savdo fayli.",
                "Yig‘indi uchun nima?",
                [
                    "A) Faqat for-loop",
                    "B) Pandas/NumPy vektor operatsiyasi",
                    "C) while True",
                    "D) Print har qator",
                ],
                "B",
            ),
            "py-func": _quiz(
                "py-q-zero",
                "0 ga bo‘lish",
                "orders = 0, AOV hisoblash.",
                "Yaxshi xulq?",
                [
                    "A) Darhol bo‘lish, dastur yiqilsin",
                    "B) Tekshirib None yoki aniq xabar qaytarish",
                    "C) 0 ni 1 ga almashtirish sekin",
                    "D) Pass qilish",
                ],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "1) segment(revenue) funksiyasini yozing (VIP/Regular/New).\n"
            "2) 8 ta mijoz revenue ro‘yxatini for bilan aylanib, har birining segmentini chop eting.\n"
            "3) aov() da orders=0 holatini ko‘rsating."
        ),
    },
    {
        "order": 3,
        "title": "To‘plamlar, fayl va xatolar",
        "slug": "py-tuzilma",
        "description": "list/dict/set/tuple, CSV o‘qish, try/except, modullar.",
        "lectures": [
            _lec(
                "List, tuple, set, dict",
                "py-collections",
                """
<h2>Dars maqsadi</h2>
<p>Tahlilda eng ko‘p ishlatiladigan to‘rt tuzilmani farqlaysiz.</p>
<ul>
  <li><strong>list</strong> — tartibli, o‘zgaruvchan (ustun qiymatlari)</li>
  <li><strong>tuple</strong> — o‘zgarmas juftlik (kalit sifatida)</li>
  <li><strong>set</strong> — unique, tezkor a’zolik (unique mijoz ID)</li>
  <li><strong>dict</strong> — kalit→qiymat (region: jami savdo)</li>
</ul>
<h2>Biznes</h2>
<p><code>{"Toshkent": 12.5e6, "Samarqand": 4.1e6}</code> — kichik agregat. Katta hajmda Pandas DataFrame ishlating.</p>
""",
                examples=[
                    'cities = ["Toshkent", "Samarqand", "Toshkent"]\nprint(set(cities))\nrevenue = {"Toshkent": 12_500_000}\nprint(revenue.get("Buxoro", 0))',
                ],
            ),
            _lec(
                "Fayl va CSV",
                "py-file",
                """
<h2>Dars maqsadi</h2>
<p>Matn/CSV ni o‘qish va yozish. Encoding (utf-8) va separator (vergul vs nuqtali vergul) ni tekshirasiz.</p>
<h2>csv moduli</h2>
<p>Kichik fayl uchun yetarli. Tahlilchi ishining 90% — <code>pandas.read_csv</code>. Lekin encoding xatosini tushunish shu yerda boshlanadi.</p>
<h2>Xato</h2>
<p>Windows da kyrill/o‘zbek matn: <code>encoding="utf-8-sig"</code> (Excel CSV). Noto‘g‘ri encoding — “krakozyabra”.</p>
""",
                examples=[
                    'import csv\n# pandas qulayroq:\n# import pandas as pd\n# df = pd.read_csv("sales.csv", encoding="utf-8-sig", sep=";")',
                ],
            ),
            _lec(
                "Istisnolar va modullar",
                "py-except",
                """
<h2>Dars maqsadi</h2>
<p><code>try/except</code> bilan fayl yo‘qligi yoki bo‘linish xatosini boshqarasiz. <code>import</code> bilan kodni bo‘lasiz.</p>
<h2>Qoida</h2>
<p>Keng <code>except:</code> yozmang — xato yashirinadi. Aniq: <code>FileNotFoundError</code>, <code>ValueError</code>.</p>
<h2>Modullar</h2>
<p><code>pandas</code>, <code>numpy</code> tashqi paketlar. O‘zingizning <code>metrics.py</code> — jamoa standarti.</p>
""",
                examples=[
                    'try:\n    orders = int("12a")\nexcept ValueError:\n    orders = None\n    print("orders ustuni tozalanmadi")',
                ],
            ),
        ],
        "practice": {
            "py-collections": _quiz(
                "py-q-set",
                "Unique ID",
                "Ro‘yxatda takroriy customer_id bor.",
                "Tez unique olish?",
                ["A) set(ids)", "B) ids * 2", "C) True + 1", "D) while"],
                "A",
            ),
            "py-file": _quiz(
                "py-q-enc",
                "Excel CSV",
                "O‘zbekcha header buzilib chiqdi.",
                "Birinchi tekshiruv?",
                [
                    "A) Faqat shrift",
                    "B) encoding va sep (utf-8-sig, ;)",
                    "C) Pivot",
                    "D) GPU",
                ],
                "B",
            ),
            "py-except": _quiz(
                "py-q-bare",
                "except",
                "Barcha xatolarni yutib yuborish.",
                "Nima yomon?",
                [
                    "A) Hech narsa",
                    "B) Haqiqiy xato yashirinadi, natija noto‘g‘ri bo‘lishi mumkin",
                    "C) Kod tezroq ishlaydi",
                    "D) Pandas o‘chadi",
                ],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "dict da 5 ta region→revenue saqlang.\n"
            "get() bilan mavjud bo‘lmagan region uchun 0 qaytaring.\n"
            "set bilan unique shaharlar sonini hisoblang.\n"
            "Kodni yuboring."
        ),
    },
    {
        "order": 4,
        "title": "NumPy",
        "slug": "py-numpy",
        "description": "Massivlar, vektor hisob, nan va statistik qisqa yo‘l.",
        "lectures": [
            _lec(
                "ndarray nima?",
                "np-ndarray",
                """
<h2>Dars maqsadi</h2>
<p>NumPy massivi — bir xil turdagi, tezkor, vektorlab ishlaydigan tuzilma. Pandas ostida ham u yotadi.</p>
<h2>Nima beradi?</h2>
<p>Python list da million qo‘shish sekin. <code>np.array</code> C tezligiga yaqin. Tahlilda: filtr, o‘rtacha, standart og‘ish.</p>
""",
                examples=[
                    'import numpy as np\nx = np.array([10, 20, 30, 40], dtype=float)\nprint(x.mean(), x.std(ddof=1))',
                ],
            ),
            _lec(
                "Indeks, filtr, broadcasting",
                "np-index",
                """
<h2>Dars maqsadi</h2>
<p>Boolean mask: <code>x[x &gt; 20]</code>. Broadcasting: massiv − skalyar.</p>
<h2>Biznes</h2>
<p>Chegirma 12% ni barcha narxlarga qo‘llash: <code>price * 0.88</code> — tsiklsiz.</p>
<h2>Ehtiyot</h2>
<p>Ko‘rinish (view) vs nusxa. Asl massivni tasodifan o‘zgartirmaslik uchun kerak bo‘lsa <code>.copy()</code>.</p>
""",
                examples=[
                    'import numpy as np\nprice = np.array([100, 250, 80])\nprint(price[price >= 100])\nprint(price * 0.88)',
                ],
            ),
            _lec(
                "NaN va agregatlar",
                "np-nan",
                """
<h2>Dars maqsadi</h2>
<p><code>np.nan</code> o‘rtachani “zaharlaydi”. <code>np.nanmean</code> NaN ni o‘tkazib yuboradi.</p>
<h2>Qachon?</h2>
<p>Sensor/eksport teshiklari. Avval nechta NaN borligini sanang — keyin to‘ldirish yoki tashlash qarori.</p>
""",
                examples=[
                    'import numpy as np\nx = np.array([10, np.nan, 30])\nprint(np.mean(x), np.nanmean(x))',
                ],
            ),
        ],
        "practice": {
            "np-ndarray": _quiz(
                "np-q-why",
                "NumPy sababi",
                "Katta sonli hisob.",
                "Asosiy foyda?",
                ["A) Chiroyli rang", "B) Vektorlab, tezkor bir xil turdagi hisob", "C) Internet", "D) SQL o‘rnini bosadi doim"],
                "B",
            ),
            "np-index": _quiz(
                "np-q-mask",
                "Mask",
                "x[x > 20]",
                "Bu nima?",
                ["A) Matn qidiruv", "B) Boolean filtr — shartga mos elementlar", "C) Join", "D) Pivot"],
                "B",
            ),
            "np-nan": _quiz(
                "np-q-nanmean",
                "nanmean",
                "Massivda NaN bor.",
                "Oddiy mean?",
                ["A) Doim to‘g‘ri", "B) NaN qaytarishi mumkin; nanmean NaN ni e’tiborsiz qiladi", "C) 0", "D) Xato chiqarmaydi hech"],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "NumPy da 15 ta amount yarating (ba’zilari nan).\n"
            "nanmean, nanstd, 100000 dan katta qiymatlar maskasini chiqaring.\n"
            "Kodni yuboring."
        ),
    },
    {
        "order": 5,
        "title": "Pandas: DataFrame",
        "slug": "py-pandas",
        "description": "Series/DataFrame, o‘qish, tanlash, filtr.",
        "lectures": [
            _lec(
                "Series va DataFrame",
                "pd-df",
                """
<h2>Dars maqsadi</h2>
<p>DataFrame — nomlangan ustunli jadval (Excel Table / SQL natija). Series — bitta ustun.</p>
<h2>Yaratish</h2>
<p><code>pd.DataFrame({...})</code> yoki <code>read_csv</code>. Index — qator identifikatori; tahlilda ko‘pincha RangeIndex qoldiriladi yoki sana index qilinadi.</p>
""",
                examples=[
                    'import pandas as pd\ndf = pd.DataFrame({"city": ["Toshkent", "Samarqand"], "amount": [120000, 80000]})\nprint(df.head())\nprint(df.dtypes)',
                ],
            ),
            _lec(
                "Ustun tanlash va filtr",
                "pd-filter",
                """
<h2>Dars maqsadi</h2>
<p><code>df["amount"]</code>, <code>df[["city","amount"]]</code>, <code>df.loc[]</code>, <code>df.iloc[]</code>.</p>
<h2>Filtr</h2>
<p><code>df[df["city"]=="Toshkent"]</code>. Bir nechta shart: qavs va <code>&amp;</code> / <code>|</code> (and/or kalit so‘z emas).</p>
<h2>Xato</h2>
<p><code>df[df.city == "Toshkent" &amp; df.amount &gt; 0]</code> — operator prioriteti. To‘g‘ri: <code>(df.city=="Toshkent") &amp; (df.amount&gt;0)</code>.</p>
""",
                examples=[
                    'import pandas as pd\ndf = pd.DataFrame({"city":["Toshkent","Buxoro"], "amount":[5, 12]})\nprint(df[(df["city"]=="Toshkent") | (df["amount"]>10)])',
                ],
            ),
            _lec(
                "Yangi ustun va assign",
                "pd-assign",
                """
<h2>Dars maqsadi</h2>
<p>Hisoblangan ustun: <code>df["vat"] = df["amount"] * 0.12</code>. Zanjir: <code>assign</code>.</p>
<h2>SettingWithCopy</h2>
<p>Filtrlangan bo‘lakka yozish ogohlantirish berishi mumkin. Yaxshi: <code>.loc[mask, "col"] = ...</code> yoki yangi df.</p>
""",
                examples=[
                    'import pandas as pd\ndf = pd.DataFrame({"amount": [100, 200]})\ndf = df.assign(vat=lambda x: x["amount"] * 0.12)\nprint(df)',
                ],
            ),
        ],
        "practice": {
            "pd-df": _quiz(
                "pd-q-head",
                "Tekshiruv",
                "Yangi CSV o‘qildi.",
                "Birinchi qadam?",
                ["A) Darhol model", "B) head, dtypes, shape, isna().sum()", "C) Faqat plot", "D) dropna ko‘r-ko‘rona"],
                "B",
            ),
            "pd-filter": _quiz(
                "pd-q-and",
                "Ikki shart",
                "city va amount birga.",
                "To‘g‘ri?",
                [
                    "A) and kalit so‘zi qatorlar uchun",
                    "B) (mask1) & (mask2)",
                    "C) && Java kabi",
                    "D) SUMIFS",
                ],
                "B",
            ),
            "pd-assign": _quiz(
                "pd-q-copy",
                "SettingWithCopy",
                "Filtrlangan df ga yozish.",
                "Xavfsizroq?",
                ["A) E’tiborsiz", "B) loc[mask, col] yoki assign bilan yangi jadval", "C) del df", "D) while"],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "Kichik DataFrame (8 qator: city, amount, channel) yarating.\n"
            "Toshkent VA amount>=50000 ni filtring.\n"
            "vat ustunini qo‘shing.\n"
            "head va dtypes ni izoh bilan yuboring."
        ),
    },
    {
        "order": 6,
        "title": "Tozalash: NaN, dublikat, transform",
        "slug": "py-clean",
        "description": "Missing, duplicates, matn/son konvertatsiya.",
        "lectures": [
            _lec(
                "Yetishmayotgan qiymatlar",
                "pd-na",
                """
<h2>Dars maqsadi</h2>
<p><code>isna</code>, tashlash, to‘ldirish (median, flag) qarorini biznesga qarab qilasiz.</p>
<h2>Qachon dropna?</h2>
<p>Kalit maydon (order_id) bo‘sh bo‘lsa — qator ishonchsiz. Amount ning 2% teshi — median bilan to‘ldirish mumkin, lekin <code>amount_missing</code> flagini saqlang.</p>
<h2>Xato</h2>
<p>Hamma NaN ni 0 qilish — o‘rtacha va konversiyani buzadi. 0 — haqiqiy nol savdo; NaN — noma’lum.</p>
""",
                examples=[
                    'import pandas as pd\ndf = pd.DataFrame({"amount":[10, None, 30]})\nprint(df["amount"].isna().mean())\ndf["amount_missing"] = df["amount"].isna()\ndf["amount"] = df["amount"].fillna(df["amount"].median())',
                ],
            ),
            _lec(
                "Dublikatlar",
                "pd-dup",
                """
<h2>Dars maqsadi</h2>
<p><code>duplicated</code>, <code>drop_duplicates(subset=...)</code>. Kalitni aniqlang.</p>
<h2>Biznes</h2>
<p>OrderID unique bo‘lishi kerak. CustomerID takrorlanishi normal. Noto‘g‘ri subset — butun buyurtmalar yo‘qoladi.</p>
""",
                examples=[
                    'import pandas as pd\ndf = pd.DataFrame({"order_id":[1,1,2], "amount":[10,10,5]})\nprint(df.duplicated(subset=["order_id"]).sum())\nprint(df.drop_duplicates("order_id"))',
                ],
            ),
            _lec(
                "Matn va tur konvertatsiyasi",
                "pd-cast",
                """
<h2>Dars maqsadi</h2>
<p><code>str.strip</code>, <code>replace</code>, <code>to_numeric(errors="coerce")</code>, <code>to_datetime</code>.</p>
<h2>Pipeline</h2>
<ol>
  <li>Ustun nomlarini snake_case</li>
  <li>Bo‘shliqlarni trim</li>
  <li>Son/sana turini belgilash</li>
  <li>Kutilmagan qiymatlarni hisobotga yozish</li>
</ol>
""",
                examples=[
                    'import pandas as pd\ns = pd.Series([" 1 200 ", "abc", "3,5"])\nclean = s.str.replace(" ", "", regex=False).str.replace(",", ".", regex=False)\nprint(pd.to_numeric(clean, errors="coerce"))',
                ],
            ),
        ],
        "practice": {
            "pd-na": _quiz(
                "pd-q-zero",
                "NaN vs 0",
                "Yetkazib berilmagan buyurtma amount=NaN.",
                "0 ga to‘ldirish?",
                [
                    "A) Har doim to‘g‘ri",
                    "B) Nol va noma’lumni aralashtiradi — avval flag, keyin qoida",
                    "C) dropna yetarli doim",
                    "D) Ignore",
                ],
                "B",
                difficulty="medium",
            ),
            "pd-dup": _quiz(
                "pd-q-subset",
                "drop_duplicates",
                "CustomerID bo‘yicha unique qilindi, buyurtmalar yo‘qoldi.",
                "Sabab?",
                ["A) Pandas bug", "B) Noto‘g‘ri subset — takrorlanishi kerak bo‘lgan kalit", "C) Encoding", "D) GPU"],
                "B",
            ),
            "pd-cast": _quiz(
                "pd-q-coerce",
                "to_numeric",
                "Noto‘g‘ri matn bor.",
                "errors='coerce' nima qiladi?",
                ["A) Dastur yiqiladi", "B) Noto‘g‘ri qiymatni NaN qiladi", "C) 0 qiladi", "D) O‘chiradi faylni"],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "CSV (yoki o‘zingiz yaratgan) da:\n"
            "1) isna().sum() hisobot.\n"
            "2) amount ni to_numeric(coerce).\n"
            "3) order_id dublikatlarini sanang, faqat shu kalit bo‘yicha drop qiling.\n"
            "Qisqa izoh: nechta qator yo‘qaldi va nima uchun."
        ),
    },
    {
        "order": 7,
        "title": "Guruhlash, merge, sana",
        "slug": "py-agg",
        "description": "groupby, agg, merge/join, datetime tahlil.",
        "lectures": [
            _lec(
                "groupby va aggregatsiya",
                "pd-groupby",
                """
<h2>Dars maqsadi</h2>
<p>SQL GROUP BY ning Pandasdagi ekvivalenti.</p>
<pre>df.groupby("region").agg(revenue=("amount","sum"), orders=("order_id","nunique"))</pre>
<h2>observed va as_index</h2>
<p>Kategoriyalar va indekssiz natija hisobotga qulay. <code>named aggregation</code> — ustun nomlari chalkashmasin.</p>
""",
                examples=[
                    'import pandas as pd\ndf = pd.DataFrame({"region":["Toshkent","Toshkent","Buxoro"], "amount":[10,20,5], "oid":[1,2,3]})\nprint(df.groupby("region").agg(revenue=("amount","sum"), n=("oid","nunique")))',
                ],
            ),
            _lec(
                "merge / join",
                "pd-merge",
                """
<h2>Dars maqsadi</h2>
<p>SQL JOIN: <code>how="left"|"inner"|"outer"</code>. Kalitlar: <code>on</code> yoki <code>left_on/right_on</code>.</p>
<h2>Tekshiruv</h2>
<p>Merge dan keyin qatorlar soni kutilganmi? Ko‘p-ko‘p kalit — fan-out (qatorlar ko‘payadi). <code>validate="many_to_one"</code> yordam beradi.</p>
""",
                examples=[
                    'import pandas as pd\norders = pd.DataFrame({"cid":[1,2], "amount":[10,20]})\ncust = pd.DataFrame({"cid":[1,3], "name":["Ali","Nodira"]})\nprint(orders.merge(cust, on="cid", how="left"))',
                ],
            ),
            _lec(
                "Sana/vaqt tahlili",
                "pd-dt",
                """
<h2>Dars maqsadi</h2>
<p><code>to_datetime</code>, <code>.dt.to_period("M")</code>, resample, rolling.</p>
<h2>Biznes</h2>
<p>Oylik savdo, 7 kunlik sliding o‘rtacha, so‘nggi xariddan beri kunlar (recency).</p>
<h2>Xato</h2>
<p>Kun/oy/yil aralash format. <code>dayfirst=True</code> ni faqat ma’lum bo‘lsa qo‘ying.</p>
""",
                examples=[
                    'import pandas as pd\ndf = pd.DataFrame({"dt":["2024-01-31","2024-02-01"], "amount":[10, 20]})\ndf["dt"] = pd.to_datetime(df["dt"])\nprint(df.groupby(df["dt"].dt.to_period("M"))["amount"].sum())',
                ],
            ),
        ],
        "practice": {
            "pd-groupby": _quiz(
                "pd-q-nunique",
                "Buyurtmalar soni",
                "groupby region.",
                "Unique order_id?",
                ["A) sum", "B) nunique", "C) mean", "D) concat"],
                "B",
            ),
            "pd-merge": _quiz(
                "pd-q-fanout",
                "Fan-out",
                "Merge dan keyin qatorlar kutilganidan ko‘p.",
                "Ehtimol?",
                ["A) Encoding", "B) Ko‘p-ko‘p kalit / dublikat o‘ng jadvalda", "C) GPU", "D) f-string"],
                "B",
                difficulty="medium",
            ),
            "pd-dt": _quiz(
                "pd-q-period",
                "Oy kesimi",
                "Kunlik savdoni oyga yig‘ish.",
                "Qulay yo‘l?",
                ["A) str[:7] faqat", "B) to_datetime + dt.to_period('M') yoki resample", "C) set()", "D) while"],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "orders va customers ni left merge qiling.\n"
            "region bo‘yicha revenue va nunique(order_id).\n"
            "Sana ustunidan oy period yarating.\n"
            "Natija jadvalini yuboring."
        ),
    },
    {
        "order": 8,
        "title": "EDA va vizualizatsiya",
        "slug": "py-eda",
        "description": "Tavsiflovchi tahlil, Matplotlib, Seaborn.",
        "lectures": [
            _lec(
                "EDA tartibi",
                "pd-eda",
                """
<h2>Dars maqsadi</h2>
<p>Exploratory Data Analysis — savol berish, taqsimotni ko‘rish, anomaliyani topish. Model/dashboarddan oldin.</p>
<ol>
  <li>Hajm, turlar, yetishmovchilik</li>
  <li>Tavsiflovchi statistika (describe)</li>
  <li>Kategoriyalar chastotasi</li>
  <li>Taqsimot va outlier</li>
  <li>Kesimlar (region × kanal)</li>
  <li>Qisqa xulosa: nima o‘zgardi, nima shubhali</li>
</ol>
""",
                examples=[
                    'import pandas as pd\ndf = pd.DataFrame({"amount":[1,2,3,1000], "city":["A","A","B","B"]})\nprint(df.describe())\nprint(df["city"].value_counts(normalize=True))',
                ],
            ),
            _lec(
                "Matplotlib",
                "py-mpl",
                """
<h2>Dars maqsadi</h2>
<p>Chiziqli va ustunli grafik: trend va taqqos. Sarlavha, o‘q nomlari, grid — stakeholder o‘qishi uchun.</p>
<h2>Qoida</h2>
<p>3D pie emas. Vaqt — line; kategoriya taqqos — bar; taqsimot — hist.</p>
""",
                examples=[
                    'import matplotlib.pyplot as plt\n# plt.plot(months, revenue); plt.title("Oylik savdo"); plt.ylabel("so‘m")\n# plt.tight_layout(); plt.savefig("revenue.png", dpi=120)',
                ],
            ),
            _lec(
                "Seaborn",
                "py-sns",
                """
<h2>Dars maqsadi</h2>
<p>Seaborn — statistik grafika: boxplot (outlier), heatmap (korrelyatsiya), barplot (CI ixtiyoriy).</p>
<h2>Biznes</h2>
<p>Region bo‘yicha amount boxplot — qaysi viloyatda “dum” uzun (katta chegirma/katta buyurtma).</p>
""",
                examples=[
                    'import seaborn as sns\n# sns.boxplot(data=df, x="region", y="amount")\n# sns.heatmap(df.select_dtypes("number").corr(), annot=True)',
                ],
            ),
        ],
        "practice": {
            "pd-eda": _quiz(
                "pd-q-eda-first",
                "EDA tartibi",
                "Yangi dataset.",
                "Avval nima?",
                ["A) Neural net", "B) Hajm, tur, missing, describe, kesimlar", "C) Faqat pie", "D) Drop all"],
                "B",
            ),
            "py-mpl": _quiz(
                "py-q-chart",
                "Grafik tanlash",
                "12 oylik savdo.",
                "Eng mos?",
                ["A) 3D pie", "B) Line chart", "C) Word cloud", "D) Scatter 50 o‘lchov"],
                "B",
            ),
            "py-sns": _quiz(
                "py-q-box",
                "Boxplot",
                "Outlier ko‘rish.",
                "Qaysi?",
                ["A) Pie", "B) Boxplot / violin", "C) Stacked 20 series", "D) Map only"],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "describe() + value_counts.\n"
            "1 hist (amount), 1 bar (region revenue), 1 boxplot.\n"
            "Har grafik ostiga 1 jumla insight.\n"
            "PNG yoki notebook yuboring."
        ),
    },
    {
        "order": 9,
        "title": "Biznes tahlil va yakuniy loyiha",
        "slug": "py-capstone",
        "description": "KPI, kohort/recency g‘oya, yakuniy analytics project.",
        "lectures": [
            _lec(
                "KPI ni kodda hisoblash",
                "py-kpi",
                """
<h2>Dars maqsadi</h2>
<p>Revenue, Orders, AOV, Conversion (agar traffic bo‘lsa), Repeat rate — aniq ta’rif bilan.</p>
<h2>Ta’rif muhim</h2>
<p>“Faol mijoz” — 90 kun ichida xarid qilganmi yoki status=active ustunimi? Hujjatlashtiring, aks holda hisobotlar zid keladi.</p>
""",
                examples=[
                    'def kpi_summary(df):\n    orders = df["order_id"].nunique()\n    revenue = df["amount"].sum()\n    return {"orders": orders, "revenue": revenue, "aov": revenue / orders if orders else None}',
                ],
            ),
            _lec(
                "Mijoz kesimi: recency g‘oyasi",
                "py-rfm",
                """
<h2>Dars maqsadi</h2>
<p>So‘nggi xarid sanasi (Recency) — churn signalining sodda shakli. RFM to‘liq marketing kursi, lekin tahlilchi Recency ni hisoblashi shart.</p>
<pre>last = df.groupby("customer_id")["order_date"].max()
recency = (as_of - last).dt.days</pre>
<p>90+ kun — qayta faollashtirish ro‘yxati (biznes bilan kelishilgan chegara).</p>
""",
            ),
            _lec(
                "Yakuniy loyiha: retail savdo",
                "py-final",
                """
<h2>Biznes senariy</h2>
<p>O‘rta hajmdagi do‘kon tarmog‘i 6 oylik savdo CSV beradi. Savol: qaysi region/kanal o‘sadi, qayerda AOV tushgan, qaysi mijozlar jim.</p>
<h2>Talab</h2>
<ol>
  <li>Tozalash jurnali (nechta qator, nima tashlandi)</li>
  <li>Oylik revenue, AOV, unique mijoz</li>
  <li>Region × kanal pivot (Pandas)</li>
  <li>2 ta grafik</li>
  <li>5 ta aniq tavsiya (emas “yaxshilash kerak”)</li>
</ol>
<h2>Baholash</h2>
<p>Kod ishlashi, ta’riflar aniqligi, insight sifatida — “grafik chiroyi” emas.</p>
""",
            ),
        ],
        "practice": {
            "py-kpi": _quiz(
                "py-q-aov-def",
                "AOV",
                "Average Order Value.",
                "Formula?",
                ["A) mijozlar / revenue", "B) revenue / unique orders (ta’rifga qarab)", "C) mean(city)", "D) count nan"],
                "B",
            ),
            "py-rfm": _quiz(
                "py-q-recency",
                "Recency",
                "Mijoz 120 kundan beri xarid qilmagan.",
                "Bu nima signal?",
                ["A) Albatta firibgar", "B) Churn/qayta faollashtirish xavfi (chegara biznes bilan)", "C) AOV oshgan", "D) Join xato"],
                "B",
            ),
            "py-final": _quiz(
                "py-q-deliver",
                "Deliverable",
                "Yakuniy loyiha.",
                "Eng muhimi?",
                [
                    "A) 20 ta 3D chart",
                    "B) Toza pipeline + aniq KPI ta’rifi + harakatga yaroqli insight",
                    "C) Faqat print(df)",
                    "D) Parolni kodga yozish",
                ],
                "B",
                difficulty="medium",
            ),
        },
        "exercises": [
            _quiz(
                "py-cap-clean",
                "Capstone tozalash",
                "order_id dublikat, amount matn, 3% NaN.",
                "Ketma-ketlik?",
                [
                    "A) Darhol model",
                    "B) Turlar → NaN siyosati → kalit dublikat → KPI",
                    "C) dropna hamma ustun",
                    "D) Faqat plot",
                ],
                "B",
                difficulty="hard",
            ),
        ],
        "homework": _hw(
            "Mini-loyiha (notebook yoki .py + qisqa PDF/markdown):\n"
            "• tozalash jurnali\n"
            "• 3 KPI (oylik)\n"
            "• 1 merge yoki groupby kesim\n"
            "• 2 grafik\n"
            "• 5 ta tavsiya\n"
            "Ixtiyoriy dataset: o‘z CSV yoki darsdagi savdo namunasi."
        ),
    },
]


def build_python_modules():
    from apps.core.python_teacher_lessons import LECTURES

    for module in MODULES:
        for lecture in module["lectures"]:
            html = LECTURES.get(lecture["slug"])
            if html:
                lecture["content"] = html.strip()
    return MODULES
