"""
Excel kursi — Data Analyst yo‘nalishi uchun chuqur o‘zbekcha ma’ruzalar va testlar.
"""

COURSE_DESCRIPTION = (
    "Excelni noldan, o‘qituvchi bilan gaplashgandek: katak, tur, Table, formulalar, "
    "XLOOKUP, Pivot va Power Query. Toshkent savdosi va bank fayllari misolida — "
    "hisobot chiqarishgacha. Har darsdan keyin mashq bor."
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
        "title": "Excel asoslari",
        "slug": "excel-asoslari",
        "description": "Interfeys, ma’lumot turlari, Table va toza ish kitobi madaniyati.",
        "lectures": [
            _lec(
                "Excel tahlilchi uchun nima?",
                "excel-nima",
                """
<h2>Dars maqsadi</h2>
<p>Excelni oddiy jadval emas, balki <strong>tahlil vositasi</strong> sifatida ko‘rasiz: qayerda Excel yetarli, qachon SQL/Power BI kerak.</p>

<h2>Biznes konteksti</h2>
<p>Ko‘pchilik kompaniyalarda ma’lumot avval Excelda yashaydi: savdo eksporti, HR ro‘yxati, byudjet. Tahlilchi vazifasi — chalkash hujjatni <em>ishonchli</em> hisobotga aylantirish.</p>

<h2>Asosiy tushunchalar</h2>
<ul>
  <li><strong>Workbook</strong> — fayl (.xlsx)</li>
  <li><strong>Worksheet</strong> — varaq</li>
  <li><strong>Cell</strong> — katak (A1 manzili)</li>
  <li><strong>Range</strong> — oralik (A1:D100)</li>
  <li><strong>Table</strong> — strukturali jadval (Ctrl+T) — filtr, strukturali havolalar</li>
</ul>

<h2>Qachon Excel?</h2>
<table>
  <tr><th>Vazifa</th><th>Excel</th><th>Boshqa vosita</th></tr>
  <tr><td>Tezkor tozalash, kichik hajm</td><td>Ha</td><td>—</td></tr>
  <tr><td>Millionlab qator, umumiy manba</td><td>Cheklangan</td><td>SQL / Power Query + model</td></tr>
  <tr><td>Interaktiv dashboard, rollar</td><td>Cheklangan</td><td>Power BI</td></tr>
</table>

<h2>Professional odatlar</h2>
<ol>
  <li>Xom ma’lumotni alohida varaqda saqlang (<code>raw_</code>).</li>
  <li>Hisob-kitobni alohida qatlamda qiling (<code>calc_</code>).</li>
  <li>Yakuniy chiqishni alohida ko‘rsating (<code>report_</code>).</li>
  <li>Rang bilan “bezash” emas — mantiq bilan tuzish.</li>
</ol>

<h2>Xulosa</h2>
<p>Excel — tahlilchining tez laboratoriya stoli. Keyingi darslarda Table, tozalash va formulalarni chuqurlashtiramiz.</p>
""",
            ),
            _lec(
                "Ma’lumot turlari va format",
                "excel-turlar",
                """
<h2>Dars maqsadi</h2>
<p>Matn, son, sana, mantiqiy qiymat farqini bilasiz va noto‘g‘ri format tufayli yuzaga keladigan xatolarni oldini olasiz.</p>

<h2>Nima uchun muhim?</h2>
<p><code>01.02.2024</code> matn bo‘lsa, sana filtrlari ishlamaydi. <code>1 200</code> matn bo‘lsa, SUM 0 beradi. Bu — real auditlarda eng ko‘p uchraydigan muammo.</p>

<h2>Asosiy turlar</h2>
<ul>
  <li><strong>Number</strong> — hisob-kitob</li>
  <li><strong>Text</strong> — kodlar (masalan, 00123 — boshidagi 0 muhim)</li>
  <li><strong>Date/Time</strong> — Excelda aslida serial number</li>
  <li><strong>Boolean</strong> — TRUE/FALSE (IF natijasi)</li>
  <li><strong>Error</strong> — #N/A, #DIV/0!, #VALUE!</li>
</ul>

<h2>Amaliy tekshiruv</h2>
<p><code>=ISTEXT(A2)</code>, <code>=ISNUMBER(A2)</code>, <code>=ISDATE</code> yo‘q — sana uchun <code>=CELL("format",A2)</code> yoki Power Query da tur belgilash.</p>

<h2>Biznes misol</h2>
<p>Bank tranzaksiya faylida amount ustuni chapga tekislangan — demak matn. To‘g‘rilash: <code>VALUE</code>, <code>NUMBERVALUE</code>, yoki Power Query <em>Change Type</em>.</p>

<h2>Maslahat</h2>
<p>Hisobotda ko‘rsatish formati (ming ajratgich, so‘m) va hisoblash turi alohida. Format — ko‘rinish; tur — mantiq.</p>
""",
            ),
            _lec(
                "Excel Table (Ctrl+T)",
                "excel-table",
                """
<h2>Dars maqsadi</h2>
<p>Oddiy diapazonni Table ga aylantirasiz va strukturali havolalardan foydalanasiz.</p>

<h2>Nima beradi Table?</h2>
<ul>
  <li>Avtomatik filtr va saralash</li>
  <li>Yangi qator qo‘shilganda formula kengayadi</li>
  <li>Nomlangan ustunlar: <code>=[@Amount]</code>, <code>=SUM(Sales[Amount])</code></li>
  <li>Pivot / Power Query uchun barqaror manba</li>
</ul>

<h2>Qoidalar</h2>
<ol>
  <li>Birinchi qator — unique header.</li>
  <li>Bo‘sh qator/ustun qo‘ymang.</li>
  <li>Birlashtirilgan kataklar (merge) — Table dushmani.</li>
  <li>Har bir Table ga tushunarli nom: <code>tbl_Sales</code>.</li>
</ol>

<h2>Demo mantiq</h2>
<p>A1:D1 header, pastda ma’lumot → Ctrl+T → My table has headers → OK. Formula: <code>=[@Qty]*[@Price]</code> yangi ustunda.</p>

<h2>Xato</h2>
<p>“Chiroyli” merge qilingan sarlavha bilan Table yaratib bo‘lmaydi. Avval unmerge, bitta header qatori.</p>
""",
            ),
        ],
        "practice": {
            "excel-nima": _quiz(
                "ex-q-when-excel",
                "Qachon Excel?",
                "Senariy: har kuni yangilanadigan 50 mln qatorli savdo, 200 foydalanuvchi.",
                "Eng to‘g‘ri yondashuv?",
                [
                    "A) Hammasi bitta Excel faylda",
                    "B) SQL/ombor + Power BI (Excel faqat ad-hoc)",
                    "C) Faqat Google Sheets",
                    "D) Faqat Word jadvali",
                ],
                "B",
                difficulty="easy",
            ),
            "excel-turlar": _quiz(
                "ex-q-text-number",
                "Matnmi yoki son?",
                "Amount ustuni chapga tekis, SUM 0 qaytardi.",
                "Eng ehtimoliy sabab?",
                [
                    "A) Formula sintaksisi noto‘g‘ri",
                    "B) Qiymatlar matn sifatida saqlangan",
                    "C) Pivot kerak",
                    "D) VLOOKUP kerak",
                ],
                "B",
                difficulty="easy",
            ),
            "excel-table": _quiz(
                "ex-q-table-benefit",
                "Table afzalligi",
                "Yangi savdo qatori qo‘shildi.",
                "Table ning asosiy foydasi?",
                [
                    "A) Rang o‘zgaradi",
                    "B) Formulalar va nomlangan diapazon avtomatik kengayadi",
                    "C) Fayl hajmi kamayadi",
                    "D) Internet kerak bo‘ladi",
                ],
                "B",
                difficulty="easy",
            ),
        },
        "exercises": [
            _quiz(
                "ex-m1-layers",
                "Ish kitobi qatlamlari",
                "Professional Excel tuzilmasi.",
                "raw / calc / report qatlamlari nima uchun?",
                [
                    "A) Faqat chiroy uchun",
                    "B) Xom ma’lumot, hisob va chiqishni ajratish — xato va auditni kamaytiradi",
                    "C) Faqat Power BI uchun",
                    "D) Kerak emas",
                ],
                "B",
                difficulty="medium",
            ),
        ],
        "homework": _hw(
            "1) O‘z savdo CSV (yoki namuna)ni oching.\n"
            "2) raw_Sales varag‘iga joylashtiring.\n"
            "3) Table yarating (tbl_Sales).\n"
            "4) calc_ varag‘ida 3 ta metrika yozing: qatorlar soni, jami summa, unique mijoz (taxminan).\n"
            "5) Qisqa izoh: qaysi ustunlar matn/son/sana ekanini yozing."
        ),
    },
    {
        "order": 2,
        "title": "Tozalash, saralash, filtr",
        "slug": "excel-tozalash",
        "description": "Duplicate, bo‘sh qiymat, Text to Columns, Filter, Sort.",
        "lectures": [
            _lec(
                "Ma’lumotni tozalash",
                "excel-clean",
                """
<h2>Dars maqsadi</h2>
<p>Tahlildan oldin ma’lumotni “ishlatishga yaroqli” holatga keltirish bosqichlarini bilasiz.</p>

<h2>Tipik iflosliklar</h2>
<ul>
  <li>Bo‘sh qatorlar, bo‘shliqli matn (<code>" Ali "</code>)</li>
  <li>Duplicate mijoz/ID</li>
  <li>Bir ustunda aralash format (sana + matn)</li>
  <li>Bir katakda bir nechta qiymat (vergul bilan)</li>
  <li>Yashirin belgilar, non-breaking space</li>
</ul>

<h2>Asosiy vositalar</h2>
<ol>
  <li><code>TRIM</code>, <code>CLEAN</code>, <code>SUBSTITUTE</code></li>
  <li>Remove Duplicates (ehtiyot: qaysi ustunlar bo‘yicha?)</li>
  <li>Text to Columns / Flash Fill</li>
  <li>Find &amp; Replace</li>
  <li>Power Query (keyingi modullar) — takrorlanadigan tozalash uchun eng yaxshi</li>
</ol>

<h2>Biznes qoida</h2>
<p>Duplicate o‘chirishdan oldin: bu haqiqiy dublikatmi yoki bir mijozning ikki buyurtmasimi? Kalit ustunlarni aniqlang (OrderID vs CustomerID).</p>
""",
            ),
            _lec(
                "Sort va Filter",
                "excel-sort-filter",
                """
<h2>Dars maqsadi</h2>
<p>Ko‘p ustunli saralash va Autofilter / Advanced Filter bilan ishlaysiz.</p>

<h2>Sort</h2>
<p>Data → Sort: avval Region, keyin Amount DESC. Custom list (oy tartibi) muhim.</p>

<h2>Filter</h2>
<p>Table filtrida Number Filters, Text Filters, Date Filters. “Top 10” — tez ko‘zdan kechirish uchun.</p>

<h2>Xato</h2>
<p>Faqat bir ustunni belgilab Sort qilish — qatorlar “buziladi”. Butun jadvalni tanlang yoki Table ishlating.</p>

<h2>Amaliy senariy</h2>
<p>“Toshkent + Amount &gt; 1 000 000 + oxirgi 30 kun” — filtr zanjiri. Natijani alohida varaqqa Copy → Paste Values (hisobot uchun).</p>
""",
            ),
            _lec(
                "Conditional Formatting kirish",
                "excel-cf",
                """
<h2>Dars maqsadi</h2>
<p>Shartli formatlash bilan anomaliya va KPI holatini vizual ko‘rasiz — lekin hisobotni “chiroy” bilan to‘ldirmaysiz.</p>

<h2>Foydali qoidalar</h2>
<ul>
  <li>Color scales — taqsimot</li>
  <li>Data bars — solishtirish</li>
  <li>Icon sets — status (ehtiyot: rangi ko‘rlar uchun)</li>
  <li>Formula-based rule: <code>=$C2&lt;Target</code></li>
</ul>

<h2>Professional maslahat</h2>
<p>CF — tahlil vositasi, yakuniy stakeholder hisobotida minimal ishlating. Asosiy xabar son va matnda bo‘lsin.</p>
""",
            ),
        ],
        "practice": {
            "excel-clean": _quiz(
                "ex-q-dup-key",
                "Duplicate kaliti",
                "Buyurtmalar jadvali: OrderID unique, CustomerID takrorlanadi.",
                "Remove Duplicates ni qaysi ustun bo‘yicha qilish xato?",
                [
                    "A) OrderID",
                    "B) CustomerID (buyurtmalar yo‘qoladi)",
                    "C) Hech qachon qilmaslik",
                    "D) Faqat Amount",
                ],
                "B",
            ),
            "excel-sort-filter": _quiz(
                "ex-q-sort-break",
                "Sort xatosi",
                "Faqat Amount ustuni tanlanib Sort qilindi.",
                "Natija?",
                [
                    "A) Hammasi yaxshi",
                    "B) Qatorlar chalkashishi mumkin — bog‘liq ustunlar noto‘g‘ri juftlashadi",
                    "C) Excel o‘chadi",
                    "D) Pivot yaratiladi",
                ],
                "B",
            ),
            "excel-cf": _quiz(
                "ex-q-cf-role",
                "CF roli",
                "Stakeholder PDF hisoboti.",
                "Eng yaxshi yondashuv?",
                [
                    "A) Har katakda icon set",
                    "B) Minimal CF, asosiy xabar son/matn",
                    "C) Faqat qizil shrift",
                    "D) CF o‘rniga WordArt",
                ],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "Berilgan (yoki o‘zingiz yuklagan) mijozlar jadvalida:\n"
            "1) TRIM bilan ismlarni tozalang.\n"
            "2) Duplicate CustomerID larni aniqlang (lekin o‘chirmasdan count qiling).\n"
            "3) Region=Toshkent filtrini qo‘llang.\n"
            "4) Amount bo‘yicha Color scale qo‘ying.\n"
            "Qisqa hisobot: nechta qator, nechta dublikat, top-5 mijoz."
        ),
    },
    {
        "order": 3,
        "title": "Asosiy formulalar",
        "slug": "excel-formulalar",
        "description": "IF/AND/OR, SUMIFS/COUNTIFS, xato tutish.",
        "lectures": [
            _lec(
                "IF, AND, OR",
                "excel-if",
                """
<h2>Dars maqsadi</h2>
<p>Shartli mantiq bilan segmentatsiya va flag ustunlarini yozasiz.</p>

<h2>Sintaksis</h2>
<pre>=IF(A2&gt;=1000000;"VIP";"Oddiy")
=IF(AND(B2="Toshkent";C2&gt;0);"Lokal faol";"Boshqa")
=IF(OR(D2="debit";D2="credit");"Tranzaksiya";"Noma’lum")</pre>

<h2>Biznes misol</h2>
<p>Mijoz statusi: oxirgi xarid &gt; 90 kun → "Churn risk"; aks holda "Active". Bu — CRM uchun oddiy, lekin foydali qoida.</p>

<h2>Ichma-ich IF</h2>
<p>3–4 darajadan oshsa — o‘qish qiyin. Yechim: <code>IFS</code>, yordamchi ustun, yoki lookup jadvali.</p>

<h2>Xato</h2>
<p>Matnni son bilan solishtirish: <code>"1000"&gt;500</code> kutilmagan natija. Turini avval tozalang.</p>
""",
                examples=["=IF(AND([@City]=\"Toshkent\",[@Amount]>=500000),\"Focus\",\"Other\")"],
            ),
            _lec(
                "SUMIFS, COUNTIFS, AVERAGEIFS",
                "excel-sumifs",
                """
<h2>Dars maqsadi</h2>
<p>Bir nechta shartli agregatsiya — tahlilchining kundalik quroli.</p>

<h2>Nima uchun SUMIF emas SUMIFS?</h2>
<p>SUMIFS ko‘p shartni qo‘llab-quvvatlaydi va argument tartibi barqaror: avval sum_range, keyin criteria.</p>

<pre>=SUMIFS(Amount; Region; "Toshkent"; Month; 3)
=COUNTIFS(Status; "Paid"; Channel; "Online")
=AVERAGEIFS(Score; Team; "A"; Score; "&gt;0")</pre>

<h2>Biznes savol</h2>
<p>“Mart oyida online kanaldan Toshkent bo‘yicha to‘langan buyurtmalar summasi?” — bitta SUMIFS.</p>

<h2>Pivot vs SUMIFS</h2>
<p>Tez ad-hoc → SUMIFS. Ko‘p kesim, o‘zgaruvchan → PivotTable. Ikkalasini ham biling.</p>
""",
            ),
            _lec(
                "Xatolarni tutish",
                "excel-errors",
                """
<h2>Dars maqsadi</h2>
<p>#N/A, #DIV/0!, #VALUE! ni tushunasiz va IFERROR/IFNA bilan boshqarasiz.</p>

<h2>Qachon yashirish?</h2>
<p>Foydalanuvchi hisobotida #N/A ko‘rinsa — ishonchsizlik. Lekin debug paytida xatoni yashirmang — sababni toping.</p>

<pre>=IFERROR(VLOOKUP(...);0)
=IFNA(XLOOKUP(...);"Topilmadi")</pre>

<h2>Professional tip</h2>
<p>0 bilan #N/A ni aralashtirmang. Ba’zan “topilmadi” alohida flag bo‘lishi kerak.</p>
""",
            ),
        ],
        "practice": {
            "excel-if": _quiz(
                "ex-q-and",
                "AND mantiqi",
                "City=Toshkent VA Amount&gt;0.",
                "To‘g‘ri formula g‘oyasi?",
                [
                    "A) =IF(OR(...))",
                    "B) =IF(AND(City=\"Toshkent\";Amount&gt;0);...)",
                    "C) =SUMIFS faqat",
                    "D) =CONCAT",
                ],
                "B",
            ),
            "excel-sumifs": _quiz(
                "ex-q-sumifs-order",
                "SUMIFS tartibi",
                "SUMIFS argumentlari.",
                "To‘g‘ri ketma-ketlik?",
                [
                    "A) criteria, sum_range",
                    "B) sum_range, criteria_range1, criteria1, ...",
                    "C) faqat bitta argument",
                    "D) VLOOKUP bilan bir xil",
                ],
                "B",
            ),
            "excel-errors": _quiz(
                "ex-q-iferror",
                "IFERROR",
                "Hisobotda #N/A ko‘rinmasin, lekin 0 ham chalkashtirmasin.",
                "Yaxshiroq yondashuv?",
                [
                    "A) Doim IFERROR(...,0)",
                    "B) IFNA + aniq xabar yoki alohida status ustuni",
                    "C) Xatolarni e’tiborsiz",
                    "D) Faqat Pivot",
                ],
                "B",
                difficulty="medium",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "tbl_Sales ustida:\n"
            "1) Status ustuni: Amount&gt;=1mln → High, aks holda Normal (IF).\n"
            "2) SUMIFS: har bir Region uchun jami.\n"
            "3) COUNTIFS: Status=High soni.\n"
            "Natijani report_ varag‘iga joylashtiring."
        ),
    },
    {
        "order": 4,
        "title": "Qidiruv formulalari",
        "slug": "excel-lookup",
        "description": "XLOOKUP, INDEX/MATCH, VLOOKUP cheklovlari.",
        "lectures": [
            _lec(
                "XLOOKUP",
                "excel-xlookup",
                """
<h2>Dars maqsadi</h2>
<p>Zamonaviy qidiruv: XLOOKUP — VLOOKUP o‘rnini bosuvchi standart.</p>

<pre>=XLOOKUP(lookup_value; lookup_array; return_array; [if_not_found]; [match_mode]; [search_mode])</pre>

<h2>Afzalliklar</h2>
<ul>
  <li>Chapga ham qaytarish mumkin (VLOOKUP cheklovi yo‘q)</li>
  <li>if_not_found o‘rnatiladi</li>
  <li>Taxminiy moslik, qidiruv yo‘nalishi</li>
</ul>

<h2>Biznes</h2>
<p>OrderID bo‘yicha CustomerName, Price list dan ProductID → Price.</p>

<h2>Eslatma</h2>
<p>Eski Excel (2016) da XLOOKUP yo‘q — INDEX/MATCH biling.</p>
""",
            ),
            _lec(
                "INDEX + MATCH",
                "excel-index-match",
                """
<h2>Dars maqsadi</h2>
<p>Moslashuvchan qidiruv: MATCH pozitsiya topadi, INDEX qiymat oladi.</p>

<pre>=INDEX(return_range; MATCH(key; key_range; 0))</pre>

<h2>Nima uchun hali ham kerak?</h2>
<p>Eski fayllar, murakkab 2D qidiruv (MATCH ikki marta), ba’zi array senariylari.</p>

<h2>Xato</h2>
<p>match_type 1/-1 taxminiy — tartiblangan diapazon talab qiladi. Aniq qidiruv uchun 0.</p>
""",
            ),
            _lec(
                "VLOOKUP cheklovlari",
                "excel-vlookup",
                """
<h2>Dars maqsadi</h2>
<p>VLOOKUP ni tushunasiz, lekin yangi ishlarda XLOOKUP/INDEX-MATCH ni afzal ko‘rasiz.</p>

<h2>Muammolar</h2>
<ul>
  <li>Qidiruv ustuni chapda bo‘lishi shart</li>
  <li>Ustun indeksi (col_index) — ustun qo‘shilsa buziladi</li>
  <li>Taxminiy moslik default (range_lookup) — xavfli</li>
</ul>

<pre>=VLOOKUP(A2; Table; 3; FALSE)</pre>

<h2>Migratsiya</h2>
<p>Eski modelni buzmasdan ishlating; yangi varaqlarda XLOOKUP yozing.</p>
""",
            ),
        ],
        "practice": {
            "excel-xlookup": _quiz(
                "ex-q-xlookup",
                "XLOOKUP",
                "Chapdagi ustundan qiymat kerak.",
                "Eng qulay vosita?",
                ["A) VLOOKUP", "B) XLOOKUP yoki INDEX/MATCH", "C) SUMIF", "D) CONCAT"],
                "B",
            ),
            "excel-index-match": _quiz(
                "ex-q-match0",
                "MATCH aniqligi",
                "ID bo‘yicha aniq qidiruv.",
                "match_type?",
                ["A) 1", "B) -1", "C) 0", "D) 2"],
                "C",
            ),
            "excel-vlookup": _quiz(
                "ex-q-vlookup-risk",
                "VLOOKUP xavfi",
                "range_lookup o‘tkazib yuborildi.",
                "Xavf?",
                [
                    "A) Yo‘q",
                    "B) Taxminiy moslik — noto‘g‘ri juftlik mumkin",
                    "C) Faqat sekinlashadi",
                    "D) Pivot ochiladi",
                ],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "Products va Orders jadvallarini XLOOKUP bilan bog‘lang:\n"
            "Orders ga ProductName va UnitPrice qo‘shing.\n"
            "Topilmagan ID lar uchun \"NO_MATCH\" yozilsin.\n"
            "Qisqa izoh: nima uchun VLOOKUP qiyin bo‘lardi?"
        ),
    },
    {
        "order": 5,
        "title": "Matn va sana funksiyalari",
        "slug": "excel-text-date",
        "description": "LEFT/RIGHT/MID, TEXT, DATE, EOMONTH, ish kunlari.",
        "lectures": [
            _lec(
                "Matn funksiyalari",
                "excel-text-fn",
                """
<h2>Dars maqsadi</h2>
<p>Kodlardan qism ajratish, birlashtirish, tozalash.</p>

<pre>=LEFT(A2;3)
=RIGHT(A2;4)
=MID(A2;5;2)
=TEXTJOIN(", ";TRUE; range)
=UPPER / LOWER / PROPER</pre>

<h2>Biznes</h2>
<p>SKU = "UZ-TSH-041" → kategoriya LEFT, rang MID. Telefon formatini bir xillashtirish.</p>
""",
            ),
            _lec(
                "Sana funksiyalari",
                "excel-date-fn",
                """
<h2>Dars maqsadi</h2>
<p>Sana serial ekanini tushunib, oy/kvartal/KPI oynalarini hisoblaysiz.</p>

<pre>=YEAR(A2)
=EOMONTH(A2;0)
=EDATE(A2;1)
=NETWORKDAYS(start; end)
=TODAY()</pre>

<h2>Biznes KPI</h2>
<p>Oy yakuni, rolling 30 kun, yetkazib berish SLA (ish kunlari).</p>

<h2>Xato</h2>
<p>Matn sanani DATEVALUE yoki Power Query bilan konvert qiling.</p>
""",
            ),
            _lec(
                "Amaliy: buyurtma yoshi",
                "excel-order-age",
                """
<h2>Dars maqsadi</h2>
<p>OrderDate dan “necha kun o‘tdi” va aging bucket yasaysiz.</p>

<pre>=TODAY()-[@OrderDate]
=IFS(age&lt;30;"0-29";age&lt;60;"30-59";TRUE;"60+")</pre>

<h2>Nima uchun?</h2>
<p>Debitorlik, ombor zaxirasi, churn — aging tahlili klassikasi.</p>
""",
            ),
        ],
        "practice": {
            "excel-text-fn": _quiz(
                "ex-q-left",
                "LEFT",
                "SKU boshidagi 2 harf — mamlakat kodi.",
                "Funksiya?",
                ["A) LEFT", "B) SUM", "C) VLOOKUP", "D) RANK"],
                "A",
            ),
            "excel-date-fn": _quiz(
                "ex-q-networkdays",
                "NETWORKDAYS",
                "SLA — faqat ish kunlari.",
                "Qaysi funksiya?",
                ["A) DAYS", "B) NETWORKDAYS", "C) HOUR", "D) RAND"],
                "B",
            ),
            "excel-order-age": _quiz(
                "ex-q-aging",
                "Aging",
                "60+ kun bucket.",
                "Asosiy g‘oya?",
                [
                    "A) Faqat Pivot Charts",
                    "B) Kun farqi + IFS/IF bilan diapazon",
                    "C) Faqat rang",
                    "D) Macro shart",
                ],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "OrderDate ustunidan Year, Month, AgeDays, AgingBucket yarating.\n"
            "Har bir bucket bo‘yicha COUNTIFS hisoblang.\n"
            "report_Aging varag‘iga jadval qo‘ying."
        ),
    },
    {
        "order": 6,
        "title": "PivotTable va PivotChart",
        "slug": "excel-pivot",
        "description": "Kesimlar, value settings, slicer, chart.",
        "lectures": [
            _lec(
                "PivotTable asoslari",
                "excel-pivot-base",
                """
<h2>Dars maqsadi</h2>
<p>Kattaa jadvalni tez kesib, agregat hisobot olasiz.</p>

<h2>Maydonlar</h2>
<ul>
  <li>Rows / Columns — o‘qlar</li>
  <li>Values — SUM/COUNT/AVERAGE</li>
  <li>Filters — sahifa filtri</li>
</ul>

<h2>Qoida</h2>
<p>Manba — Table. Refresh — ma’lumot yangilanganda. Calculated Field ehtiyot bilan.</p>

<h2>Biznes</h2>
<p>Region × Month bo‘yicha Revenue; Count of Orders.</p>
""",
            ),
            _lec(
                "Value settings va foizlar",
                "excel-pivot-values",
                """
<h2>Dars maqsadi</h2>
<p>% of Grand Total, Running Total, Difference From — tahlilchi uchun muhim.</p>

<h2>Misollar</h2>
<ul>
  <li>Ulush: regionning umumiy savdodagi %</li>
  <li>O‘sish: oldingi oyga nisbatan</li>
  <li>Running total: yil boshidan</li>
</ul>

<h2>Xato</h2>
<p>COUNT o‘rniga SUM — ID ustunida. Qiymat maydonini tekshiring.</p>
""",
            ),
            _lec(
                "Slicer va PivotChart",
                "excel-pivot-slicer",
                """
<h2>Dars maqsadi</h2>
<p>Interaktiv filtr (Slicer) va grafik bilan boshqaruvchi uchun ko‘rinish.</p>

<h2>Maslahat</h2>
<p>Bir nechta Pivotni bir slicer ga bog‘lang. Chart turini xabarga moslang (ulush — pie emas, bar ko‘proq aniq).</p>
""",
            ),
        ],
        "practice": {
            "excel-pivot-base": _quiz(
                "ex-q-pivot-source",
                "Pivot manbasi",
                "Barqaror yangilanish.",
                "Eng yaxshi manba?",
                ["A) Merge kataklar", "B) Excel Table", "C) Rasm", "D) PDF"],
                "B",
            ),
            "excel-pivot-values": _quiz(
                "ex-q-count-sum",
                "COUNT vs SUM",
                "Values ga OrderID qo‘yildi.",
                "Odatda nima kerak?",
                ["A) SUM OrderID", "B) COUNT OrderID (buyurtmalar soni)", "C) MAX City", "D) CONCAT"],
                "B",
            ),
            "excel-pivot-slicer": _quiz(
                "ex-q-slicer",
                "Slicer",
                "Bir nechta Pivot birgalikda filtrlanadi.",
                "Vosita?",
                ["A) Slicer (Report Connections)", "B) Word", "C) Only CF", "D) Freeze Panes"],
                "A",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "Pivot: Rows=Region, Columns=Month, Values=Sum of Amount va Count of OrderID.\n"
            "Show values as % of Grand Total qo‘shing.\n"
            "Slicer: Channel. PivotChart (clustered column) yarating.\n"
            "3 ta insight yozing."
        ),
    },
    {
        "order": 7,
        "title": "Power Query",
        "slug": "excel-power-query",
        "description": "Get Data, transform, merge/append, qayta ishlatiladigan tozalash.",
        "lectures": [
            _lec(
                "Power Query nima?",
                "excel-pq-intro",
                """
<h2>Dars maqsadi</h2>
<p>Takroriy tozalashni UI + M tili bilan avtomatlashtirasiz.</p>

<h2>Nima uchun?</h2>
<p>Har oy CSV keladi. Qo‘lda TRIM/qayta format — xato manbai. Power Query — qadamlar yozuvini saqlaydi, Refresh bilan qayta ishlaydi.</p>

<h2>Oqim</h2>
<ol>
  <li>Data → Get Data</li>
  <li>Transform (tur, split, filter, group)</li>
  <li>Close &amp; Load (jadval / connection only)</li>
</ol>
""",
            ),
            _lec(
                "Merge va Append",
                "excel-pq-merge",
                """
<h2>Dars maqsadi</h2>
<p>SQL JOIN/UNION g‘oyasini Power Query da qo‘llaysiz.</p>

<ul>
  <li><strong>Append</strong> — bir xil sxemali fayllarni vertikal birlashtirish (oylik CSV lar)</li>
  <li><strong>Merge</strong> — kalit bo‘yicha (Left/Inner/…) — masalan Order + Customer</li>
</ul>

<h2>Biznes</h2>
<p>12 oy fayl → Append → bitta fact. Keyin dim_Customer bilan Merge.</p>
""",
            ),
            _lec(
                "Turlar va xatolar",
                "excel-pq-types",
                """
<h2>Dars maqsadi</h2>
<p>Change Type, Replace Errors, Remove Errors — modelga chiqishdan oldin.</p>

<h2>Maslahat</h2>
<p>Locale (decimal vergul/nuqta) ni hisobga oling. O‘zbekiston CSV lari ko‘pincha ; separator.</p>
""",
            ),
        ],
        "practice": {
            "excel-pq-intro": _quiz(
                "ex-q-pq-why",
                "PQ sababi",
                "Har oy bir xil tozalash.",
                "Eng yaxshi?",
                ["A) Har safar qo‘lda", "B) Power Query + Refresh", "C) Faqat Notepad", "D) Email"],
                "B",
            ),
            "excel-pq-merge": _quiz(
                "ex-q-append",
                "Append",
                "Yanvar+Fevral CSV bir xil ustunlar.",
                "Operatsiya?",
                ["A) Merge", "B) Append", "C) Unpivot", "D) Pivot only"],
                "B",
            ),
            "excel-pq-types": _quiz(
                "ex-q-locale",
                "Locale",
                "1.234,56 son sifatida o‘qilmayapti.",
                "Nimani tekshirasiz?",
                ["A) Faqat shrift", "B) Locale / decimal separator", "C) Chart tipi", "D) Zoom"],
                "B",
                difficulty="medium",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "2 ta oylik CSV ni Power Query da Append qiling.\n"
            "Amount turini Decimal ga o‘zgartiring.\n"
            "Customer kaliti bo‘yicha dim jadvaliga Merge (Left Outer).\n"
            "Qadamlar ro‘yxatini screenshot yoki matn bilan yuboring."
        ),
    },
    {
        "order": 8,
        "title": "Dashboard va biznes hisobot",
        "slug": "excel-dashboard",
        "description": "KPI, layout, chart tanlash, stakeholder uchun hikoya.",
        "lectures": [
            _lec(
                "Dashboard printsiplari",
                "excel-dash-principles",
                """
<h2>Dars maqsadi</h2>
<p>Bitta ekranda: vaziyat → sabab → harakat. Ordati bezak emas.</p>

<h2>Tuzilma</h2>
<ol>
  <li>Header: davr, filtrlar</li>
  <li>KPI qatori (3–5 ta)</li>
  <li>Asosiy trend / taqqos</li>
  <li>Detal jadval</li>
</ol>

<h2>Qoida</h2>
<p>Har bir vizual bitta savolga javob bersin. Rang — ma’no uchun (qizil = xavf).</p>
""",
            ),
            _lec(
                "KPI tanlash",
                "excel-kpi",
                """
<h2>Dars maqsadi</h2>
<p>Vanity metric emas, qaror metric.</p>

<ul>
  <li>Revenue, Orders, AOV</li>
  <li>Conversion, Retention (agar ma’lumot bo‘lsa)</li>
  <li>Margin — moliyaviy</li>
</ul>

<h2>Formula misol</h2>
<pre>AOV = Revenue / Orders
Yo‘qolgan mijoz flag = IF(LastOrder&lt;TODAY()-90;1;0)</pre>
""",
            ),
            _lec(
                "Yakuniy amaliyot senariysi",
                "excel-final-case",
                """
<h2>Biznes senariy</h2>
<p>Retail zanjir: savdo CSV + mijoz jadvali. Rahbariyat so‘raydi:</p>
<ol>
  <li>Qaysi region o‘syoqti?</li>
  <li>Qaysi kanal foydali?</li>
  <li>Qaysi mahsulotlar “og‘ir” zaxira / past aylanma?</li>
</ol>

<h2>Sizning ish oqimingiz</h2>
<p>raw → Power Query → tbl_Fact → Pivot/KPI → dashboard → 5 jumlalik insight + tavsiya.</p>

<h2>Keyingi qadam</h2>
<p>Shu modelni Power BI ga ko‘chirish — keyingi kurs. Excelda ishonchli fact jadvali bo‘lsa, migratsiya oson.</p>
""",
            ),
        ],
        "practice": {
            "excel-dash-principles": _quiz(
                "ex-q-dash-one",
                "Bitta savol",
                "Dashboard vizuali.",
                "Eng yaxshi amaliyot?",
                [
                    "A) Bitta grafikda 12 metrika",
                    "B) Har vizual bitta aniq savol",
                    "C) Faqat 3D pie",
                    "D) Matnsiz faqat rang",
                ],
                "B",
            ),
            "excel-kpi": _quiz(
                "ex-q-aov",
                "AOV",
                "Average Order Value.",
                "Formula?",
                ["A) Orders/Revenue", "B) Revenue/Orders", "C) SUM only", "D) COUNTIF City"],
                "B",
            ),
            "excel-final-case": _quiz(
                "ex-q-flow",
                "Ish oqimi",
                "Yangi oy fayli keldi.",
                "Ketma-ketlik?",
                [
                    "A) Darhol chart",
                    "B) raw → PQ/tozalash → model → KPI/dashboard → insight",
                    "C) Faqat email",
                    "D) Merge kataklar",
                ],
                "B",
                difficulty="medium",
            ),
        },
        "exercises": [
            _quiz(
                "ex-m8-capstone",
                "Capstone tushuncha",
                "Excel kursi yakuni.",
                "Eng muhim natija?",
                [
                    "A) Chiroyli shrift",
                    "B) Takrorlanadigan, ishonchli tahlil zanjiri va aniq biznes xulosalar",
                    "C) Faqat VLOOKUP bilish",
                    "D) Macro yozish majburiy",
                ],
                "B",
                difficulty="hard",
            ),
        ],
        "homework": _hw(
            "Mini-dashboard (1 sahifa):\n"
            "• 4 KPI\n"
            "• 1 trend chart\n"
            "• 1 Pivot jadval + slicer\n"
            "• 5 ta bullet insight (o‘zbekcha)\n"
            "Faylni uy vazifasi sifatida yuklang."
        ),
    },
]


def build_excel_modules():
    from apps.core.excel_teacher_lessons import LECTURES

    for module in MODULES:
        for lecture in module["lectures"]:
            html = LECTURES.get(lecture["slug"])
            if html:
                lecture["content"] = html.strip()
    return MODULES
