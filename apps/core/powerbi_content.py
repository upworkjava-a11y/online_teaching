"""
Power BI kursi — Microsoft Learn darajasida to‘liq o‘zbekcha ma’ruzalar va senariy testlar.
"""

COURSE_DESCRIPTION = (
    "Power BI ni noldan: Get Data, Power Query, model, DAX, vizual, Service. "
    "Exceldan kelgan tahlilchi uchun — qayerni bosish va nima uchun, "
    "filial va savdo misollari bilan."
)


def _lec(title, slug, html, examples=None):
    return {"title": title, "slug": slug, "content": html.strip(), "sql_examples": examples or []}


def _quiz(slug, title, description, task, options, answer, hints=None):
    return {
        "slug": slug,
        "title": title,
        "description": description.strip(),
        "task": task,
        "hints": hints or [],
        "kind": "quiz",
        "quiz_options": options,
        "columns": ["answer"],
        "rows": [[answer]],
    }


def _hw(text):
    return text.strip()


MODULES = [
    {
        "order": 1,
        "title": "Power BI ga kirish",
        "slug": "pbi-kirish",
        "description": "Platforma arxitekturasi, rollar, Desktop/Service/Mobile va end-to-end workflow.",
        "lectures": [
            _lec(
                "Power BI nima?",
                "pbi-nima",
                """
<h2>Dars maqsadi</h2>
<p>Ushbu dars oxirida Power BI ekotizimini tushunasiz, qaysi vazifa uchun qaysi mahsulot ishlatilishini ajratasiz va tahlilchi vs developer rollarini farqlaysiz.</p>

<h2>Biznes konteksti</h2>
<p>Tashkilotlarda qarorlar ko‘pincha Excel jadvallari, ERP eksportlari va SQL hisobotlariga asoslanadi. Muammo: ma’lumot tarqoq, versiyalar chalkash, rahbariyat esa <em>yangilangan</em> va <em>ishonchli</em> ko‘rsatkichlarni xohlaydi. Power BI shu bo‘shliqni to‘ldirish uchun yaratilgan: bir nechta manbadan ma’lumotni birlashtirib, interaktiv hisobot va dashboardlarga aylantirish.</p>

<h2>Uchta asosiy mahsulot</h2>
<table>
  <tr><th>Mahsulot</th><th>Qayerda</th><th>Asosiy vazifa</th></tr>
  <tr><td><strong>Power BI Desktop</strong></td><td>Windows ilova</td><td>Authoring: ulanish, model, DAX, vizual, .pbix</td></tr>
  <tr><td><strong>Power BI Service</strong></td><td>app.powerbi.com</td><td>Nashr, ulashish, refresh, workspace, apps</td></tr>
  <tr><td><strong>Power BI Mobile</strong></td><td>iOS/Android</td><td>Tayyor hisobotlarni ko‘rish, ogohlantirishlar</td></tr>
</table>
<p>Amaliy qoida: <strong>yaratish</strong> — Desktop; <strong>tarqatish va boshqarish</strong> — Service; <strong>yo‘lda ko‘rish</strong> — Mobile.</p>

<h2>Power BI vs Excel</h2>
<ul>
  <li>Excel — hujjat markazli; Power BI — <strong>dataset + report</strong> modeli, filtr konteksti, rollar.</li>
  <li>Katta hajm va ko‘p foydalanuvchi ulashishda Service qulayroq.</li>
  <li>Excel ham manba bo‘lishi mumkin; lekin yakuniy “bitta haqiqat” odatda Power BI datasetida bo‘ladi.</li>
</ul>

<h2>Microsoft Learn bog‘lanishi</h2>
<p>Bu modul Microsoft Learn dagi <em>Get started with Microsoft data analytics</em> va Power BI kirish yo‘nalishlaridagi kompetentsiyalarga mos: platformani tanish, asosiy tushunchalar, ish oqimi.</p>

<h2>Tekshiruv savoli (o‘zingizga)</h2>
<p>Agar CFO har kuni yangilanadigan savdo dashboardini so‘rasa — qaysi mahsulotda yaratasiz, qaysida ulashasiz?</p>
""",
            ),
            _lec(
                "Ish jarayoni (workflow)",
                "pbi-workflow",
                """
<h2>Dars maqsadi</h2>
<p>Power BI loyihasining standart zanjirini bosqichma-bosqich bilib olasiz va har bosqichda qanday xatolar bo‘lishini oldindan ko‘rasiz.</p>

<h2>End-to-end zanjir</h2>
<ol>
  <li><strong>Connect (Get Data)</strong> — Excel, SQL, API, SharePoint…</li>
  <li><strong>Transform (Power Query)</strong> — tozalash, tip, merge/append, Applied Steps.</li>
  <li><strong>Model</strong> — relationships, star schema, yashirin kalitlar.</li>
  <li><strong>Calculate (DAX)</strong> — measure lar: KPI, foiz, o‘tgan yil.</li>
  <li><strong>Visualize</strong> — sahifa, vizual, slicer, bookmark.</li>
  <li><strong>Share</strong> — Publish → workspace → app / share / RLS.</li>
</ol>

<h2>Nima uchun tartib muhim?</h2>
<p>Ko‘pchilik darhol vizual chizadi. Natija: noto‘g‘ri tip, chalkash bog‘lanish, sekin hisobot. Professional yondashuv — avval <strong>tozalangan va modellashtirilgan</strong> ma’lumot, keyin chiroyli dizayn.</p>

<h2>Import vs DirectQuery (qisqa)</h2>
<ul>
  <li><strong>Import</strong> — ma’lumot modelga yuklanadi; tez vizual; refresh kerak.</li>
  <li><strong>DirectQuery</strong> — so‘rov manbaga ketadi; “jonli” ma’lumot; perfomans manbaga bog‘liq.</li>
</ul>
<p>O‘rganish va aksariyat dashboardlar uchun Import bilan boshlang.</p>

<h2>Amaliy ssenariy</h2>
<p>Do‘kon tarmog‘i: kunlik savdo Excel + mijozlar SQL da. Workflow: CSV/Excel + SQL ni ulash → Power Query da mijoz_id ni bir xillashtirish → FactSales–DimCustomer bog‘lash → Total Sales measure → rahbariyat sahifasi → Service ga publish.</p>
""",
            ),
            _lec(
                "Desktop interfeysi",
                "pbi-desktop-ui",
                """
<h2>Dars maqsadi</h2>
<p>Power BI Desktop dagi asosiy panellar va ko‘rinishlarni ishonchli navigatsiya qilasiz.</p>

<h2>Uchta asosiy view</h2>
<ul>
  <li><strong>Report</strong> — sahifalar va vizuallar (oxirgi foydalanuvchi ko‘radigan narsa).</li>
  <li><strong>Data</strong> — jadval ko‘rinishi (ustunlar, qatorlar namuna).</li>
  <li><strong>Model</strong> — jadvallar va relationship chizig‘i.</li>
</ul>

<h2>Muhim panellar</h2>
<ul>
  <li><strong>Fields</strong> — jadvallar, ustunlar, measure lar.</li>
  <li><strong>Visualizations</strong> — vizual turi + field wells (Axis, Values, Legend…).</li>
  <li><strong>Filters</strong> — Visual / Page / Report filtrlari.</li>
  <li><strong>Ribbon</strong> — Get data, Transform, New measure, Publish.</li>
</ul>

<h2>Fayl turlari</h2>
<table>
  <tr><th>Kengaytma</th><th>Ma’nosi</th></tr>
  <tr><td><code>.pbix</code></td><td>To‘liq loyiha (ma’lumot + model + hisobot)</td></tr>
  <tr><td><code>.pbit</code></td><td>Template — tuzilma bor, ma’lumot keyin yuklanadi</td></tr>
</table>

<h2>Yaxshi odatlar</h2>
<ul>
  <li>Jadval va measure nomlarini tushunarli yozing (<code>FactSales</code>, <code>[Total Sales]</code>).</li>
  <li>Keraksiz ustunlarni Power Query da olib tashlang — model yengil bo‘lsin.</li>
  <li>Har 15–20 daqiqada saqlang; katta transformatsiyadan oldin nusxa oling.</li>
</ul>
""",
            ),
        ],
        "practice": {
            "pbi-nima": _quiz(
                "pbi-q1-product",
                "Senariy · Qayerda yaratiladi?",
                """
IT direktori: “Savdo KPI dashboardini birinchi marta yasab, keyin 40 ta menejerga ulashamiz.”

Sizning vazifangiz — to‘g‘ri vositalarni tanlash.
""",
                "Hisobotni YARATISH (model + vizual) asosan qayerda bajariladi?",
                [
                    "A) Faqat Power BI Mobile da, chunki u eng yangi",
                    "B) Power BI Desktop da (.pbix), keyin Service orqali ulashiladi",
                    "C) Faqat Excel Online da, Power BI kerak emas",
                    "D) Faqat SQL Server Agent da, vizualsiz",
                ],
                "B",
                ["Desktop = authoring; Service = distribute"],
            ),
            "pbi-workflow": _quiz(
                "pbi-q1-flow",
                "Senariy · Qaysi bosqich o‘tkazib yuborilgan?",
                """
Tahlilchi darhol Get Data qilib, hech narsa tozalamasdan 12 ta vizual chizdi. Keyin summalar “g‘alati”, sanalar matn bo‘lib qolgan, ikki jadval bog‘lanmagan.
""",
                "Eng muhim o‘tkazib yuborilgan bosqichlar qaysilar?",
                [
                    "A) Faqat Mobile ilovani o‘rnatish",
                    "B) Transform (Power Query) va Model (relationships) bosqichlari",
                    "C) Faqat Theme rangini o‘zgartirish",
                    "D) Faqat PDF eksport qilish",
                ],
                "B",
                ["Connect → Transform → Model → Visualize → Share"],
            ),
            "pbi-desktop-ui": _quiz(
                "pbi-q1-pbix",
                "Senariy · Fayl formati",
                """
Hamkasbingizga loyihani yubormoqchisiz: ichida ma’lumot modeli, measure lar va 3 sahifali hisobot bor.
""",
                "Qaysi fayl formati to‘g‘ri?",
                [
                    "A) .docx — chunki hisobot matn",
                    "B) .pbix — Desktop loyihasining standart formati",
                    "C) .exe — o‘rnatish paketi",
                    "D) .css — dizayn uchun",
                ],
                "B",
            ),
        },
        "exercises": [
            _quiz(
                "pbi-m1-service",
                "Senariy · Service roli",
                """
.pbix tayyor. Endi har dushanba ertalab avtomatik yangilanishi va 20 ta foydalanuvchi brauzerda ko‘rishi kerak.
""",
                "Bu talablar asosan qayerda hal qilinadi?",
                [
                    "A) Faqat Desktop Filter pane da",
                    "B) Power BI Service (workspace, dataset refresh, share/app)",
                    "C) Faqat Notepad",
                    "D) Faqat Windows Calculator",
                ],
                "B",
            ),
            _quiz(
                "pbi-m1-views",
                "Senariy · Qaysi view?",
                """
Siz FactSales va DimProduct o‘rtasida bog‘lanish chizig‘ini ko‘rmoqchisiz va 1:* ekanini tekshirmoqchisiz.
""",
                "Qaysi Desktop ko‘rinishi kerak?",
                [
                    "A) Report view — faqat vizual",
                    "B) Model view — jadvallar va relationships",
                    "C) Faqat Mobile landscape",
                    "D) Task Manager → Performance",
                ],
                "B",
            ),
        ],
        "homework": _hw(
            """Modul 1 uy vazifasi (kamida 300 so‘z yoki aniq bandlar):

1) Power BI Desktop, Service, Mobile ni jadval ko‘rinishida solishtiring (vazifa, kim ishlatadi, misol).
2) O‘z tashkilotingiz/do‘kon misolida Connect→Transform→Model→Visualize→Share zanjirini yozing.
3) Nima uchun “darhol vizual” yomon odat ekanini 3 ta xavf bilan tushuntiring.
Fayl: .txt, UTF-8."""
        ),
    },
    {
        "order": 2,
        "title": "Ma’lumot ulash (Get Data)",
        "slug": "pbi-get-data",
        "description": "Manbalar, Import/DirectQuery, credentials, Navigator va yuklash strategiyasi.",
        "lectures": [
            _lec(
                "Get Data asoslari",
                "pbi-get-data-asos",
                """
<h2>Dars maqsadi</h2>
<p>Get Data oynasidan to‘g‘ri manba tanlash, Import va DirectQuery farqini ish kontekstida qo‘llash.</p>

<h2>Get Data qanday ishlaydi?</h2>
<p>Home → Get data. Power BI yuzlab connectorlarni taklif qiladi, lekin ishda eng ko‘p: Excel/CSV, SQL Server/Azure SQL, SharePoint, Dataverse, Web/API, Folder (ko‘p fayl).</p>

<h2>Import vs DirectQuery — qaror jadvali</h2>
<table>
  <tr><th>Savol</th><th>Import</th><th>DirectQuery</th></tr>
  <tr><td>Ma’lumot hajmi</td><td>Odatda milyonlar (optimallashtirilgan)</td><td>Juda katta / “jonli”</td></tr>
  <tr><td>Tezlik</td><td>Vizual tez (in-memory)</td><td>Har interaksiya = manba so‘rovi</td></tr>
  <tr><td>Yangilanish</td><td>Scheduled refresh</td><td>Deyarli real-time</td></tr>
  <tr><td>DAX imkoniyati</td><td>Kengroq</td><td>Ba’zi cheklovlar</td></tr>
</table>
<p><strong>Tavsiya:</strong> o‘rganish va 80% dashboardlar uchun Import. DirectQuery — aniq talab bo‘lsa.</p>

<h2>Navigator</h2>
<p>Ulangach Navigator da jadvallar/varaqlar tanlanadi. Keraksiz varaqni olmang — model shishadi. “Transform data” — darhol Power Query; “Load” — to‘g‘ridan-to‘g‘ri yuklash (keyinroq transform qilish mumkin, lekin ertasiga qiyinlashadi).</p>
""",
            ),
            _lec(
                "Excel va CSV",
                "pbi-excel-csv",
                """
<h2>Dars maqsadi</h2>
<p>Jadval ko‘rinishidagi fayllarni xatosiz yuklash: header, delimiter, locale, merged cells muammolari.</p>

<h2>Eng ko‘p uchraydigan muammolar</h2>
<ul>
  <li>Birinchi qator sarlavha emas — “Use first row as headers”.</li>
  <li>O‘nlik ajratuvchi: <code>1,5</code> vs <code>1.5</code> (locale).</li>
  <li>Excel da birlashtirilgan kataklar — Power Query da null bo‘lib ketadi.</li>
  <li>Bir nechta header qatori — “Remove top rows” + promote headers.</li>
  <li>Bo‘sh ustunlar / “Unnamed” — darhol olib tashlang.</li>
</ul>

<h2>Folder connector</h2>
<p>Har oy yangi CSV keladigan papka bo‘lsa: Get data → Folder → Combine. Keyin refresh da yangi fayllar qo‘shiladi. Bu Microsoft Learn dagi “get data from files” amaliyotiga mos.</p>

<h2>Yaxshi odat</h2>
<p>Manba fayl nomida sana bo‘lsin (<code>sales_2024_03.csv</code>). Power Query da “Source” qadamini hujjatlang.</p>
""",
            ),
            _lec(
                "SQL va boshqa manbalar",
                "pbi-sql-source",
                """
<h2>Dars maqsadi</h2>
<p>Ma’lumotlar bazasi va bulut manbalariga xavfsiz ulanish, credentials va query folding tushunchasini bilish.</p>

<h2>SQL Server ulanishi</h2>
<ol>
  <li>Server nomi / instance</li>
  <li>Database</li>
  <li>Data Connectivity mode: Import yoki DirectQuery</li>
  <li>Authentication: Windows / Database / Microsoft account</li>
</ol>
<p>Imkon bo‘lsa, xom jadvallar o‘rniga <strong>view</strong> yoki saqlangan so‘rovdan oling — DBA bilan kelishilgan “tozalangan” qatlam.</p>

<h2>Query folding (muhim)</h2>
<p>Power Query dagi ba’zi amallar manba SQL ga “qaytariladi” (folding). Bu katta jadvallarda muhim: filtrni erta qo‘ying, aks holda millionlab qator Desktop ga keladi.</p>

<h2>Credentials xavfsizligi</h2>
<ul>
  <li>Shaxsiy parolni .pbix ichida “hardcode” qilmang.</li>
  <li>Service da dataset credentials alohida sozlanadi.</li>
  <li>On-prem SQL uchun gateway kerak bo‘ladi (9-modul).</li>
</ul>

<h2>Web / API</h2>
<p>Web connector yoki dataflow orqali JSON. Ko‘pincha Expand record/list qadamlari kerak. Rate limit va autentifikatsiyani (OAuth/key) oldindan rejalang.</p>
""",
            ),
        ],
        "practice": {
            "pbi-get-data-asos": _quiz(
                "pbi-q2-import",
                "Senariy · Import yoki DirectQuery?",
                """
Marketing jamoasi kechagi kampaniya natijasini ertalab ko‘rmoqchi. Ma’lumot hajmi ~2 mln qator, yangilanish kuni 1 marta yetarli. Vizual sekin bo‘lmasligi kerak.
""",
                "Qaysi ulanish rejimi mos?",
                [
                    "A) DirectQuery — chunki “har doim jonli” deb o‘ylashadi",
                    "B) Import + kechasi scheduled refresh — tez vizual, kunlik yangilanish yetarli",
                    "C) Faqat Mobile offline cache",
                    "D) Hech qanday ulanishsiz rasm qo‘yish",
                ],
                "B",
            ),
            "pbi-excel-csv": _quiz(
                "pbi-q2-header",
                "Senariy · CSV buzilgan",
                """
Yuklangan CSV da birinchi qator: “Hisobot 2024”. Ikkinchi qator: haqiqiy ustun nomlari (Sana, Summa…). Qiymatlar 3-qatordan.
""",
                "Power Query da eng to‘g‘ri birinchi qadamlar?",
                [
                    "A) Hech narsa qilmasdan measure yozish",
                    "B) Remove top rows (1) → Use first row as headers → tipni to‘g‘rilash",
                    "C) Faqat DirectQuery ga o‘tish",
                    "D) Jadvalni o‘chirib, Word ga ko‘chirish",
                ],
                "B",
            ),
            "pbi-sql-source": _quiz(
                "pbi-q2-cred",
                "Senariy · Xavfsizlik",
                """
Hamkasbingiz .pbix ichiga SQL parolini matn sifatida yozib qo‘ygan va faylni email orqali yuborgan.
""",
                "Bu amaliyot nima uchun xavfli va to‘g‘ri yondashuv qanday?",
                [
                    "A) Xavfsiz — .pbix hech kim ocholmaydi",
                    "B) Xavfli: credentials alohida boshqariladi; Service/gateway da sozlanadi, parolni faylga yozilmaydi",
                    "C) Faqat Theme o‘zgartirish kerak",
                    "D) RLS o‘zi parolni yashiradi",
                ],
                "B",
            ),
        },
        "exercises": [
            _quiz(
                "pbi-m2-dq",
                "Senariy · DirectQuery xavfi",
                """
DirectQuery da har bir slicer o‘zgarishi manba SQL ga so‘rov yuboradi. Manba sekin, 200 foydalanuvchi bir vaqtda ochgan.
""",
                "Eng ehtimoliy muammo?",
                [
                    "A) Hech qanday muammo bo‘lmaydi",
                    "B) Sekin hisobot + manba yuklamasi oshishi",
                    "C) Faqat shrift o‘zgaradi",
                    "D) .pbix avtomatik .xlsx ga aylanadi",
                ],
                "B",
            ),
        ],
        "homework": _hw(
            """Modul 2 uy vazifasi:

1) Import vs DirectQuery ni o‘z misolingiz bilan solishtiring (qachon qaysi).
2) Bitta CSV/Excel ni Get Data qiling: Navigator da nima tanladingiz, Transform da birinchi 5 Applied Step ni ro‘yxatlang.
3) Credentials ni qayerda saqlash xavfsiz/xavfli ekanini 5 bandda yozing.
.txt, UTF-8."""
        ),
    },
    {
        "order": 3,
        "title": "Power Query — tozalash",
        "slug": "pbi-power-query",
        "description": "Applied Steps, tozalash amallari, Merge/Append, query folding amaliyoti.",
        "lectures": [
            _lec(
                "Power Query Editor",
                "pbi-pq-editor",
                """
<h2>Dars maqsadi</h2>
<p>Power Query Editor ni ishchi vosita sifatida ishlatasiz: Applied Steps, Preview, Close & Apply.</p>

<h2>Nima uchun Power Query?</h2>
<p>Ma’lumot “kir” keladi: null, dublikat, noto‘g‘ri tip, bir ustunda ikki ma’no. Excel da qo‘lda tozalash takrorlanmaydi. Power Query da har qadam yoziladi — ertaga yangi fayl kelganda refresh yetarli.</p>

<h2>Applied Steps</h2>
<p>O‘ng panel — transformatsiya tarixi. Har qadamni bosib oldingi holatni ko‘rasiz. Nomini o‘zgartiring: <code>Removed null cities</code> — keyinroq o‘zingizga yordam.</p>
<p>Xato bo‘lsa: oxirgi qadamni o‘chirish yoki oldingisini tahrirlash. “Insert step” ehtiyot — oraliq mantiqni buzishi mumkin.</p>

<h2>M tili (qisqa)</h2>
<p>Advanced Editor da M kodi ko‘rinadi. Hozircha GUI yetarli; lekin “Source” va “Navigation” qadamlari M ekanini biling. Microsoft Learn “Clean, transform, and load” modulida shu muhit o‘rgatiladi.</p>

<h2>Close & Apply vs Close</h2>
<ul>
  <li><strong>Close & Apply</strong> — o‘zgarishlar modelga yuklanadi.</li>
  <li><strong>Close</strong> — tahrirni bekor qilish/chiqish (saqlanmagan o‘zgarishlar yo‘qolishi mumkin).</li>
</ul>
""",
            ),
            _lec(
                "Tozalash amallari",
                "pbi-pq-clean",
                """
<h2>Dars maqsadi</h2>
<p>Eng kerakli tozalash amallarini tanlab, “tozalangan jadval” mezonini tushunasiz.</p>

<h2>Asosiy amallar (ishda 90%)</h2>
<ul>
  <li><strong>Remove columns / Choose columns</strong> — keraksiz ID/izohlarni olib tashlash.</li>
  <li><strong>Filter rows</strong> — test qatorlari, bo‘sh sana, manfiy narx.</li>
  <li><strong>Replace values / Replace errors</strong></li>
  <li><strong>Split column</strong> — “Toshkent, Chilonzor” → shahar + tuman.</li>
  <li><strong>Change type</strong> — Date, Decimal, Whole number, Text (erta qiling).</li>
  <li><strong>Remove duplicates</strong> — dimension kaliti bo‘yicha.</li>
  <li><strong>Fill down</strong> — Excel merge qoldiqlari.</li>
  <li><strong>Unpivot</strong> — oy ustunlari (Yan, Fev…) → Attribute/Value (analitik model uchun oltin).</li>
</ul>

<h2>Tipni erta qo‘ying</h2>
<p>Matn bo‘lib qolgan “Summa” ustunida SUM ishlamaydi yoki xato qiladi. Change type dan keyin Preview da xatolarni ko‘ring.</p>

<h2>Sifat tekshiruvi</h2>
<p>Column profile / quality (agar yoqilgan bo‘lsa): null %, valid/error. Yuklashdan oldin 0 error maqsad qiling.</p>
""",
            ),
            _lec(
                "Append va Merge",
                "pbi-pq-merge",
                """
<h2>Dars maqsadi</h2>
<p>Append va Merge ni JOIN/UNION mantiqida to‘g‘ri tanlaysiz.</p>

<h2>Append (vertical)</h2>
<p>Bir xil ustunli jadvallar: 2023-savdo + 2024-savdo. Natija — uzunroq fact. Ustun nomlari mos kelishi kerak; aks holda null ustunlar paydo bo‘ladi.</p>

<h2>Merge (horizontal / JOIN)</h2>
<table>
  <tr><th>Join kind</th><th>Qachon</th></tr>
  <tr><td>Left outer</td><td>Chapdagi barcha fact + o‘ngdan mos dimension</td></tr>
  <tr><td>Inner</td><td>Faqat mos kelganlar (mos kelmagan fact yo‘qoladi!)</td></tr>
  <tr><td>Full outer</td><td>Kamdan-kam; tahlilda chalkashtiradi</td></tr>
</table>
<p>Merge dan keyin Expand qilib kerakli ustunlarni oling. Kalit dublikatlari bo‘lsa — qatorlar ko‘payadi (fan-out) — ehtiyot!</p>

<h2>Modelda JOIN vs Power Query Merge</h2>
<p>Ko‘pincha dimensionlarni alohida qoldirib, <strong>Model relationship</strong> qilish yaxshiroq (star schema). Merge ni “manbani birlashtirish shart” bo‘lganda ishlating.</p>
""",
            ),
        ],
        "practice": {
            "pbi-pq-editor": _quiz(
                "pbi-q3-steps",
                "Senariy · Applied Steps",
                """
Siz 8 ta transformatsiya qildingiz. 5-qadamda xato chiqdi. Rahbar “kechagi holatga qayt” deydi.
""",
                "Eng to‘g‘ri yondashuv?",
                [
                    "A) Butun .pbix ni o‘chirib, boshidan",
                    "B) Applied Steps da xato qadamni topib tuzatish/o‘chirish — tarix saqlangan",
                    "C) Faqat Report view da Filter qo‘yish",
                    "D) DAX CALCULATE yozish — Query ni tuzatadi",
                ],
                "B",
            ),
            "pbi-pq-clean": _quiz(
                "pbi-q3-type",
                "Senariy · Noto‘g‘ri tip",
                """
[Amount] ustuni Text. Card da Sum qo‘yganingizda Power BI yig‘indi bermayapti yoki xato.
""",
                "Birinchi tuzatish?",
                [
                    "A) Yangi custom visual o‘rnatish",
                    "B) Power Query da Change type → Decimal Number (locale ni tekshirib)",
                    "C) RLS yoqish",
                    "D) Publish qilib kutish",
                ],
                "B",
            ),
            "pbi-pq-merge": _quiz(
                "pbi-q3-merge",
                "Senariy · Append yoki Merge?",
                """
Yanvar va Fevral savdo fayllari bir xil ustunlarga ega. Ularni bitta uzun jadval qilmoqchisiz.
""",
                "Qaysi amal?",
                [
                    "A) Merge (Left join) — gorizontal",
                    "B) Append queries — vertikal birlashtirish",
                    "C) New measure",
                    "D) Bookmark",
                ],
                "B",
            ),
        },
        "exercises": [
            _quiz(
                "pbi-m3-append",
                "Senariy · Fan-out xavfi",
                """
FactSales ni DimCustomer ga Merge (Left) qildingiz. Customer kaliti Dim da dublikat. Natijada savdo qatorlari ko‘payib ketdi, Total Sales shishdi.
""",
                "Asosiy sabab?",
                [
                    "A) Theme noto‘g‘ri",
                    "B) Merge kalitida dublikat → qatorlar ko‘payishi (fan-out)",
                    "C) Mobile layout",
                    "D) Gateway o‘chirilgan",
                ],
                "B",
            ),
        ],
        "homework": _hw(
            """Modul 3 uy vazifasi:

1) “Kir” CSV/Excel oling (yoki ataylab buzing): null, noto‘g‘ri tip, qo‘shimcha sarlavha qatori.
2) Power Query da kamida 6 Applied Step bilan tozalang; har qadam nomini .txt ga yozing.
3) Append va Merge farqini o‘z misolingiz bilan tushuntiring; fan-out xavfini 1 paragrafda yozing."""
        ),
    },
    {
        "order": 4,
        "title": "Ma’lumot modeli",
        "slug": "pbi-model",
        "description": "Star schema, cardinality, filter direction, hide/sort by column.",
        "lectures": [
            _lec(
                "Jadvallar bog‘lanishi",
                "pbi-rel",
                """
<h2>Dars maqsadi</h2>
<p>Relationship yaratish, cardinality va cross-filter direction ni to‘g‘ri sozlash.</p>

<h2>Nima uchun model?</h2>
<p>Bitta “yassi” Excel jadvali bilan ham ishlash mumkin, lekin takroriy mijoz/mahsulot ma’lumoti shishadi. Modelda Fact (hodisalar) va Dimension (kataloglar) ajratiladi — tahlil toza, DAX oson.</p>

<h2>Cardinality</h2>
<ul>
  <li><strong>1:* (one-to-many)</strong> — odatiy: bir mijoz → ko‘p savdo.</li>
  <li><strong>1:1</strong> — kamdan-kam.</li>
  <li><strong>*:* </strong> — murakkab; ko‘pincha bridging table kerak. Boshlang‘ichda qoching.</li>
</ul>

<h2>Cross-filter direction</h2>
<ul>
  <li><strong>Single</strong> — filtr odatda dimension → fact (tavsiya).</li>
  <li><strong>Both</strong> — ikki tomonlama; ba’zi hisobotlar uchun qulay, lekin ambiguous path xavfi bor.</li>
</ul>

<h2>Yaxshi amaliyot</h2>
<p>Kalit ustunlar bir xil tipda bo‘lsin (ikkalasi ham Whole number). Matn-kalit sekinroq. “Assume referential integrity” DirectQuery da ehtiyot bilan.</p>
""",
            ),
            _lec(
                "Star schema",
                "pbi-star",
                """
<h2>Dars maqsadi</h2>
<p>Star schema ni chizib, fact/dimension ni ajratasiz — Microsoft ning rasmiy tavsiyasi.</p>

<h2>Fact jadval</h2>
<p>O‘lchovlar (amount, quantity) + foreign key lar (CustomerKey, DateKey, ProductKey). Ko‘p qator, kam takroriy matn.</p>

<h2>Dimension</h2>
<p>Mijoz, mahsulot, sana, do‘kon — tavsiflovchi ustunlar. Kamroq qator, boy atributlar (segment, kategoriya).</p>

<h2>Nima uchun muhim?</h2>
<ul>
  <li>Filtrlar tushunarli ishlaydi.</li>
  <li>DAX time intelligence uchun Date dimension kerak.</li>
  <li>RLS ni dimension bo‘yicha yozish oson.</li>
</ul>

<h2>Snowflake</h2>
<p>Dimension ichida yana dimension (Product → Category). Ishlaydi, lekin boshlang‘ichda star yetarli; kerak bo‘lsa flatten qiling.</p>
""",
            ),
            _lec(
                "Kalitlar va yashirish",
                "pbi-keys",
                """
<h2>Dars maqsadi</h2>
<p>Hisobotni foydalanuvchi uchun toza qilish: Hide, Sort by column, display folders.</p>

<h2>Hide in report view</h2>
<p>Surrogate key, helper ustunlar Fields da ko‘rinmasin — foydalanuvchi chalkashtirmasin. Modelda relationship uchun kerak bo‘lsa ham yashirish mumkin.</p>

<h2>Sort by column</h2>
<p>“Yanvar, Fevral…” alifbo bo‘yicha emas, MonthNumber bo‘yicha tartiblansin: MonthName → Sort by → MonthNumber.</p>

<h2>Display folders</h2>
<p>Measure larni “KPI”, “Time intel” papkalariga joylashtiring — katta modelda navigatsiya oson.</p>

<h2>Data category</h2>
<p>City/Country uchun Data category = City/Country — xarita vizuallari yaxshiroq ishlaydi.</p>
""",
            ),
        ],
        "practice": {
            "pbi-rel": _quiz(
                "pbi-q4-card",
                "Senariy · Cardinality",
                """
DimCustomer da CustomerID unique. FactSales da har qator — bitta chek, CustomerID takrorlanadi.
""",
                "To‘g‘ri relationship?",
                [
                    "A) Many-to-many, Both, hech narsani tekshirmasdan",
                    "B) DimCustomer (1) → FactSales (*) , odatda Single filter",
                    "C) Fact (1) → Dim (*) — teskari",
                    "D) Relationship shart emas",
                ],
                "B",
            ),
            "pbi-star": _quiz(
                "pbi-q4-star",
                "Senariy · Qayer markaz?",
                """
Siz savdo tahlili modelini chizmoqdasiz: mijozlar, mahsulotlar, sanalar va savdo hodisalari.
""",
                "Star schema da markazda qaysi jadval?",
                [
                    "A) DimCustomer — chunki mijoz muhim",
                    "B) FactSales (yoki Fact) — o‘lchovlar va FK lar",
                    "C) Faqat Theme jadvali",
                    "D) Gateway konfiguratsiyasi",
                ],
                "B",
            ),
            "pbi-keys": _quiz(
                "pbi-q4-hide",
                "Senariy · Oy tartibi",
                """
Line chart da oylar: Apr, Aug, Dec, Feb… alifbo tartibida. Biznes “Yanvar→Dekabr” xohlaydi.
""",
                "To‘g‘ri yechim?",
                [
                    "A) Har oy uchun alohida vizual",
                    "B) MonthName ustuniga Sort by column = MonthNumber",
                    "C) RLS",
                    "D) DirectQuery ga o‘tish",
                ],
                "B",
            ),
        },
        "exercises": [
            _quiz(
                "pbi-m4-both",
                "Senariy · Both filter",
                """
Modelda ikkita yo‘l bilan Fact ga yetib bo‘ladi. Both cross-filter yoqilgach Power BI “ambiguous path” ogohlantiradi / filtrlar g‘alati.
""",
                "Eng to‘g‘ri xulosa?",
                [
                    "A) Both har doim xavfsiz",
                    "B) Both ehtiyot bilan; ambiguous path va chalkash filtr xavfi bor",
                    "C) Faqat Theme muammosi",
                    "D) .pbix buzilgan",
                ],
                "B",
            ),
        ],
        "homework": _hw(
            """Modul 4 uy vazifasi:

1) Kamida 1 Fact + 2 Dimension star schema chizing (matn yoki ASCII).
2) Desktop da relationship yarating: cardinality va filter direction ni yozing.
3) Bitta ustunni Hide qiling; oy/nom uchun Sort by column ni sozlab, nima o‘zgarganini .txt da yozing."""
        ),
    },
    {
        "order": 5,
        "title": "DAX asoslari",
        "slug": "pbi-dax",
        "description": "Measure vs column, asosiy agregatlar, CALCULATE va filtr konteksti.",
        "lectures": [
            _lec(
                "Column vs Measure",
                "pbi-dax-col-meas",
                """
<h2>Dars maqsadi</h2>
<p>Calculated column va measure farqini tushunib, qachon qaysi ekanini tanlaysiz.</p>

<h2>Calculated column</h2>
<p>Har qator uchun hisoblanadi, modelda saqlanadi (xotira). Misol: <code>FullName = [First] &amp; " " &amp; [Last]</code>. Row context.</p>

<h2>Measure</h2>
<p>Agregat; vizualning filtr kontekstiga qarab qayta hisoblanadi. Misol: <code>Total Sales = SUM(FactSales[Amount])</code>. Ko‘pincha KPI lar measure.</p>

<h2>Qachon column?</h2>
<ul>
  <li>Slicer/filter/category sifatida kerak bo‘lsa.</li>
  <li>Qator darajasida klassifikatsiya (segment).</li>
</ul>
<h2>Qachon measure?</h2>
<ul>
  <li>Yig‘indi, o‘rtacha, foiz, “o‘tgan yil”.</li>
  <li>Xotirani tejash — og‘ir hisoblarni column qilmang.</li>
</ul>

<pre>Total Sales = SUM(FactSales[Amount])
Order Count = COUNTROWS(FactSales)
Avg Check = DIVIDE([Total Sales], [Order Count])</pre>
""",
            ),
            _lec(
                "Asosiy funksiyalar",
                "pbi-dax-basic",
                """
<h2>Dars maqsadi</h2>
<p>SUM, COUNTROWS, DISTINCTCOUNT, DIVIDE, AVERAGE — ishda eng kerakli blok.</p>

<h2>DIVIDE</h2>
<p><code>A/B</code> da B=0 bo‘lsa xato/infinity. <code>DIVIDE([Sales],[Qty], 0)</code> — uchinchi argument alternativ natija.</p>

<h2>DISTINCTCOUNT</h2>
<p>Unikal mijozlar: <code>DISTINCTCOUNT(FactSales[CustomerKey])</code>. “Nechta chek” vs “nechta mijoz” ni aralashtirmang.</p>

<h2>Iterator lar (tanishuv)</h2>
<p>SUMX, AVERAGEX — qatorma-qator ifoda, keyin yig‘indi. Hozircha SUM yetarli; keyinroq kerak bo‘ladi.</p>

<h2>Format</h2>
<p>Measure formatini (currency, %) Model da belgilang — hisobotda bir xil ko‘rinsin.</p>
""",
            ),
            _lec(
                "CALCULATE va filtr",
                "pbi-dax-calculate",
                """
<h2>Dars maqsadi</h2>
<p>CALCULATE orqali filtr kontekstini o‘zgartirish — DAX ning markaziy g‘oyasi (Microsoft Learn “Create calculations in DAX”).</p>

<h2>Nima qiladi?</h2>
<p><code>CALCULATE(expression, filter1, filter2, …)</code> — measure ni berilgan filtrlar bilan qayta hisoblaydi.</p>

<pre>Sales Toshkent =
CALCULATE(
    [Total Sales],
    DimCustomer[City] = "Toshkent"
)</pre>

<h2>Filter context</h2>
<p>Vizualdagi slicer, axis, legend — filter context. CALCULATE shu kontekstga qo‘shimcha filtr qo‘shadi yoki o‘zgartiradi.</p>

<h2>ALL / REMOVEFILTERS (kirish)</h2>
<p>Foiz hisoblashda ba’zan umumiy yig‘indi kerak: <code>DIVIDE([Total Sales], CALCULATE([Total Sales], ALL(DimProduct)))</code>. Keyingi darslarda chuqurlashtiriladi.</p>

<h2>Xato</h2>
<p>Column ni “measure o‘rnida” yozmang. Measure ni Fields da tanlab vizualga tashlang.</p>
""",
            ),
        ],
        "practice": {
            "pbi-dax-col-meas": _quiz(
                "pbi-q5-measure",
                "Senariy · Column yoki Measure?",
                """
Sizga kerak: (1) “Premium/Standard” segmenti slicer sifatida; (2) “Jami savdo” KPI card.
""",
                "To‘g‘ri juftlik?",
                [
                    "A) Ikkalasi ham calculated column — har doim",
                    "B) Segment — column (yoki dim atribut); Jami savdo — measure",
                    "C) Ikkalasi ham faqat bookmark",
                    "D) Faqat DirectQuery o‘zgartirish",
                ],
                "B",
            ),
            "pbi-dax-basic": _quiz(
                "pbi-q5-divide",
                "Senariy · Nolga bo‘lish",
                """
Avg Check = Sales / Orders. Ba’zi filtrda Orders = 0. Hisobotda xato chiqmoqda.
""",
                "Eng to‘g‘ri DAX yondashuvi?",
                [
                    "A) Sales / Orders — shunday qoldirish",
                    "B) DIVIDE([Sales], [Orders], 0) yoki BLANK()",
                    "C) RLS o‘chirish",
                    "D) Pie chart ga o‘tkazish",
                ],
                "B",
            ),
            "pbi-dax-calculate": _quiz(
                "pbi-q5-calc",
                "Senariy · CALCULATE",
                """
Card da “Faqat 2024-yil savdosi” ko‘rsatmoqchisiz. Date slicer bo‘lmasa ham 2024 qotib qolsin.
""",
                "Qaysi yondashuv mos?",
                [
                    "A) Faqat Theme da 2024 yozish",
                    "B) CALCULATE([Total Sales], DimDate[Year] = 2024)",
                    "C) Hide all visuals",
                    "D) Gateway restart",
                ],
                "B",
            ),
        },
        "exercises": [
            _quiz(
                "pbi-m5-distinct",
                "Senariy · Unikal mijoz",
                """
FactSales da 10 000 qator, lekin mijozlar takrorlanadi. “Nechta unik mijoz xarid qilgan?”
""",
                "Qaysi ifoda to‘g‘ri yo‘nalish?",
                [
                    "A) SUM(CustomerKey)",
                    "B) DISTINCTCOUNT(FactSales[CustomerKey])",
                    "C) TODAY()",
                    "D) FORMAT(Amount)",
                ],
                "B",
            ),
        ],
        "homework": _hw(
            """Modul 5 uy vazifasi:

1) Kamida 3 measure yozing: SUM, COUNTROWS/DISTINCTCOUNT, DIVIDE. Formulalarni .txt ga qo‘ying.
2) Bitta CALCULATE misoli (shahar yoki yil filtri bilan) — nima uchun kerakligini tushuntiring.
3) Qachon column, qachon measure — 2 ta real misol."""
        ),
    },
    {
        "order": 6,
        "title": "Vizualizatsiyalar",
        "slug": "pbi-visuals",
        "description": "Vizual tanlash mezonlari, field wells, format, custom visual xavflari.",
        "lectures": [
            _lec(
                "Vizual turlari",
                "pbi-vis-types",
                """
<h2>Dars maqsadi</h2>
<p>Savol turiga qarab to‘g‘ri vizualni tanlaysiz — “chiroyli” emas, “tushunarli”.</p>

<h2>Tanlash jadvali</h2>
<table>
  <tr><th>Savol</th><th>Vizual</th></tr>
  <tr><td>Bitta KPI</td><td>Card / KPI</td></tr>
  <tr><td>Vaqt bo‘yicha trend</td><td>Line</td></tr>
  <tr><td>Kategoriyalarni taqqoslash</td><td>Bar / Column</td></tr>
  <tr><td>Ulush (2–5 kategoriya)</td><td>Donut (ehtiyot) / Stacked bar yaxshiroq</td></tr>
  <tr><td>Jadval detallari</td><td>Table / Matrix</td></tr>
  <tr><td>Geo</td><td>Map (tozalangan manzil/country)</td></tr>
</table>

<h2>Pie chart muammosi</h2>
<p>Ko‘p bo‘lak, yaqin foizlar — odam farqni ko‘rmaydi. Microsoft ham ehtiyotkorlikni tavsiya qiladi. Bar chart ko‘pincha aniqroq.</p>

<h2>Matrix</h2>
<p>Excel pivot ga o‘xshash: rows/columns/values. Drill-down ierarxiya uchun qulay.</p>
""",
            ),
            _lec(
                "Format va field wells",
                "pbi-vis-format",
                """
<h2>Dars maqsadi</h2>
<p>Field wells va Format pane orqali professional ko‘rinish berasiz.</p>

<h2>Field wells</h2>
<p>Axis, Legend, Values, Tooltips, Small multiples. Noto‘g‘ri well — chalkash chart. Measure odatda Values ga.</p>

<h2>Formatlash</h2>
<ul>
  <li>Title — aniq savol (“2024 oylik savdo”).</li>
  <li>Data labels — kerak bo‘lsa; haddan oshirmang.</li>
  <li>X/Y axis start = 0 (ustun/bar da aldovchi scale dan saqlaning).</li>
  <li>Tooltip — qo‘shimcha measure (margin %).</li>
</ul>

<h2>Accessibility</h2>
<p>Rang kontrast, faqat rangga tayanmaslik (pattern/label). Alt text (kerak bo‘lsa).</p>
""",
            ),
            _lec(
                "Custom va AppSource",
                "pbi-vis-custom",
                """
<h2>Dars maqsadi</h2>
<p>Custom visual ni qachon ishlatish/ishlatmaslikni bilasiz.</p>

<h2>Xavflar</h2>
<ul>
  <li>Xavfsizlik — noma’lum muallif.</li>
  <li>Performance — og‘ir vizuallar.</li>
  <li>Export/Service da qo‘llab-quvvatlanmasligi.</li>
</ul>

<h2>Qoida</h2>
<p>Avval built-in. Custom — aniq ehtiyoj + IT/security ruxsati. Certified visuals afzal.</p>
""",
            ),
        ],
        "practice": {
            "pbi-vis-types": _quiz(
                "pbi-q6-card",
                "Senariy · KPI",
                """
CEO birinchi ekranda faqat “Bugungi savdo (so‘m)” ni katta ko‘rmoqchi, trend keyingi sahifada.
""",
                "Birinchi sahifa uchun eng mos vizual?",
                [
                    "A) 20 bo‘lakli Pie",
                    "B) Card (yoki KPI)",
                    "C) Scatter majburiy",
                    "D) Shape map without data",
                ],
                "B",
            ),
            "pbi-vis-format": _quiz(
                "pbi-q6-axis",
                "Senariy · Trend",
                """
Oxirgi 12 oy savdosini vaqt bo‘yicha ko‘rsatish kerak.
""",
                "Eng mos vizual?",
                [
                    "A) Line chart (Date axis + Sales)",
                    "B) Faqat Gauge",
                    "C) Faqat Card without date",
                    "D) QR code visual",
                ],
                "A",
            ),
            "pbi-vis-custom": _quiz(
                "pbi-q6-custom",
                "Senariy · Custom visual",
                """
Internetdan “chiroyli” noma’lum custom visual o‘rnatmoqchisiz. Kompaniya banking sektorida.
""",
                "Eng to‘g‘ri yondashuv?",
                [
                    "A) Hech kimga aytmasdan o‘rnatish — xavf yo‘q",
                    "B) Built-in yetadimi tekshirish; custom bo‘lsa certified + security kelishuvi",
                    "C) Har doim custom — Microsoft tavsiyasi",
                    "D) RLS o‘zi xavfsizlikni yechadi",
                ],
                "B",
            ),
        },
        "exercises": [
            _quiz(
                "pbi-m6-pie",
                "Senariy · Pie limito",
                """
15 ta mahsulot kategoriyasi ulushini pie da chizdingiz. Stakeholder “hech narsa tushunmadim” deydi.
""",
                "Yaxshiroq alternativ?",
                [
                    "A) Yana ko‘proq bo‘lak qo‘shish",
                    "B) Bar/column (yoki top N + Other) — taqqoslash oson",
                    "C) Barcha ranglarni bir xil qilish",
                    "D) Gateway o‘chirish",
                ],
                "B",
            ),
        ],
        "homework": _hw(
            """Modul 6 uy vazifasi:

1) Bitta sahifada Card + Line + Bar joylashtiring.
2) Har bir vizual uchun: qanday biznes savolga javob beradi?
3) Pie ishlatgan/ishlatmaganligingizni asoslang.
.txt"""
        ),
    },
    {
        "order": 7,
        "title": "Hisobot dizayni",
        "slug": "pbi-report-design",
        "description": "Sahifa hikoyasi, theme, bookmark, drillthrough, mobile layout.",
        "lectures": [
            _lec(
                "Sahifa tuzilishi",
                "pbi-pages",
                """
<h2>Dars maqsadi</h2>
<p>“Bir sahifa = bir hikoya” tamoyilini qo‘llaysiz.</p>

<h2>Yaxshi tuzilma</h2>
<ol>
  <li>Yuqori: KPI cards (3–5 ta).</li>
  <li>O‘rta: asosiy trend/taqqoslash.</li>
  <li>Past: detal table/matrix yoki slicer lar yon panel.</li>
</ol>
<p>Ortiqcha vizual — kognitiv yuk. White space qoldiring. Alignment va grid.</p>

<h2>Nomlash</h2>
<p>Sahifa nomi: “01 Overview”, “02 Region”, “03 Details” — tartib va ma’no.</p>
""",
            ),
            _lec(
                "Theme va brand",
                "pbi-theme",
                """
<h2>Dars maqsadi</h2>
<p>Korxona brendiga mos theme qo‘llash.</p>

<h2>Themes</h2>
<p>View → Themes yoki JSON import. Ranglar, shrift, vizual stillar bir xillashtiriladi. Har vizualni qo‘lda bo‘yash — vaqt va nomuvofiqlik.</p>

<h2>Zichlik</h2>
<p>Compact vs comfortable — auditoriya (proyektor / noutbuk) ga qarab.</p>
""",
            ),
            _lec(
                "Bookmark va navigatsiya",
                "pbi-bookmark",
                """
<h2>Dars maqsadi</h2>
<p>Bookmark, button navigation, drillthrough bilan “ilova” tajribasi yaratasiz.</p>

<h2>Bookmark</h2>
<p>Filtr + ko‘rinadigan vizuallar holatini saqlaydi. “Reset filters” tugmasi uchun qulay.</p>

<h2>Buttons</h2>
<p>Insert → Buttons → Page navigation / Bookmark. Tooltip yozing.</p>

<h2>Drillthrough</h2>
<p>Umumiy sahifadan detal sahifaga kontekst bilan o‘tish (masalan, mahsulot bo‘yicha). Drillthrough filter page da sozlanadi.</p>

<h2>Mobile layout</h2>
<p>View → Mobile layout — telefon uchun alohida joylashuv. Desktop ni “siqib” yubormang.</p>
""",
            ),
        ],
        "practice": {
            "pbi-pages": _quiz(
                "pbi-q7-story",
                "Senariy · Ortga vizual",
                """
Bitta sahifada 25 ta vizual, slicer yo‘q, sarlavhalar “Chart1”. Menejer yo‘qolgan.
""",
                "Eng muhim tuzatish?",
                [
                    "A) Yana 10 ta vizual qo‘shish",
                    "B) Sahifani soddalashtirish: aniq hikoya, KPI+asosiy chart, tushunarli nomlar",
                    "C) Faqat qora fon",
                    "D) Barcha measure larni o‘chirish",
                ],
                "B",
            ),
            "pbi-theme": _quiz(
                "pbi-q7-theme",
                "Senariy · Brend",
                """
Kompaniya rangari: ko‘k #003366 va oq. Har safar qo‘lda bo‘yash charchatmoqda.
""",
                "Yechim?",
                [
                    "A) Theme / JSON theme bilan bir xil stillar",
                    "B) Faqat Paint da skrinshot bo‘yash",
                    "C) DROP TABLE",
                    "D) RLS o‘chirish",
                ],
                "A",
            ),
            "pbi-bookmark": _quiz(
                "pbi-q7-bm",
                "Senariy · Reset",
                """
Foydalanuvchilar filtrni “buzib” qo‘yadi va boshlang‘ich holatga qaytishni xohlaydi.
""",
                "Eng qulay yechim?",
                [
                    "A) Bookmark + Button (Reset)",
                    "B) Har safar .pbix ni qayta yuborish",
                    "C) Parolni o‘zgartirish",
                    "D) Gateway o‘chirish",
                ],
                "A",
            ),
        },
        "exercises": [
            _quiz(
                "pbi-m7-drill",
                "Senariy · Drillthrough",
                """
Overview da kategoriya ustunini bosib, “Kategoriya detali” sahifasiga o‘tish kerak — filtr saqlangan holda.
""",
                "Qaysi mexanizm?",
                [
                    "A) Drillthrough page + field",
                    "B) Task Manager",
                    "C) Faqat CSV export",
                    "D) Measure o‘chirish",
                ],
                "A",
            ),
        ],
        "homework": _hw(
            """Modul 7 uy vazifasi:

1) Kamida 2 sahifa: Overview + Details.
2) Button navigatsiya va Reset bookmark.
3) (Ixtiyoriy) Drillthrough sozlang.
Har birini qanday qilganingizni .txt da bosqichma-bosqich yozing."""
        ),
    },
    {
        "order": 8,
        "title": "Filtr va interaktivlik",
        "slug": "pbi-filters",
        "description": "Slicer, filter levels, Edit interactions, sync slicers — chuqur.",
        "lectures": [
            _lec(
                "Slicer va Filter pane",
                "pbi-slicer",
                """
<h2>Dars maqsadi</h2>
<p>Filtr darajalarini farqlab, foydalanuvchi tajribasini boshqarasiz.</p>

<h2>Uch daraja</h2>
<table>
  <tr><th>Daraja</th><th>Ta’sir</th></tr>
  <tr><td>Visual</td><td>Faqat bitta vizual</td></tr>
  <tr><td>Page</td><td>Joriy sahifa</td></tr>
  <tr><td>Report</td><td>Butun hisobot</td></tr>
</table>

<h2>Slicer</h2>
<p>Foydalanuvchi uchun “ochiq” filtr. Dropdown/list/between. “Select all” ni o‘ylab qo‘ying. Ko‘p slicer — chalkashlik.</p>

<h2>Locked / hidden filters</h2>
<p>Editorda report-level filtrni qulflash mumkin — foydalanuvchi o‘zgartira olmasin (masalan, faqat faol mijozlar).</p>
""",
            ),
            _lec(
                "Edit interactions",
                "pbi-interactions",
                """
<h2>Dars maqsadi</h2>
<p>Vizual-vizual ta’sirni boshqarish: Filter / Highlight / None.</p>

<h2>Muammo</h2>
<p>Default: bir vizualni bosish boshqalarini filtrlaydi. Ba’zan KPI “umumiy” qolishi kerak — None qiling.</p>

<h2>Qanday</h2>
<p>Vizualni tanlang → Format → Edit interactions → boshqa vizuallar ustidagi ikonalar.</p>

<h2>Highlight vs Filter</h2>
<p>Highlight — ulushni ko‘rsatadi; Filter — qatorlarni kesadi. Auditoriyaga qarab tanlang.</p>
""",
            ),
            _lec(
                "Sync slicers",
                "pbi-sync",
                """
<h2>Dars maqsadi</h2>
<p>Ko‘p sahifali hisobotda slicer holatini sinxronlash.</p>

<h2>Sync slicers</h2>
<p>View → Sync slicers. Qaysi sahifada ko‘rinsin / sinxron bo‘lsin — alohida. Ba’zan slicer faqat Overview da ko‘rinadi, lekin Details ga ham ta’sir qiladi.</p>

<h2>Microsoft Learn</h2>
<p>“Design a report in Power BI Desktop” dagi interaktivlik va filtr mavzulariga mos.</p>
""",
            ),
        ],
        "practice": {
            "pbi-slicer": _quiz(
                "pbi-q8-levels",
                "Senariy · Report filter",
                """
Barcha sahifalarda faqat “Status = Active” qatorlari ko‘rinsin; foydalanuvchi buni olib tashlay olmasin.
""",
                "Qayerda sozlash to‘g‘riroq?",
                [
                    "A) Faqat bitta Card ning visual filterida",
                    "B) Report level filter (+ lock/hide kerak bo‘lsa)",
                    "C) Faqat Theme",
                    "D) Mobile layout only",
                ],
                "B",
            ),
            "pbi-interactions": _quiz(
                "pbi-q8-edit",
                "Senariy · KPI qotib qolsin",
                """
Bar chart ni bosganda Total Sales Card ham o‘zgaradi. Biznes: Card doim umumiy yig‘indi bo‘lsin.
""",
                "Yechim?",
                [
                    "A) Edit interactions → Card uchun None",
                    "B) Desktop ni o‘chirish",
                    "C) Faqat Publish",
                    "D) Barcha DAX ni o‘chirish",
                ],
                "A",
            ),
            "pbi-sync": _quiz(
                "pbi-q8-sync",
                "Senariy · Sync",
                """
Region slicer Overview da tanlansa, Details sahifasi ham shu regionni ko‘rsatishi kerak.
""",
                "Mexanizm?",
                [
                    "A) Sync slicers",
                    "B) SQL Serverni o‘chirish",
                    "C) Faqat print PDF",
                    "D) Yangi measure = 1",
                ],
                "A",
            ),
        },
        "exercises": [
            _quiz(
                "pbi-m8-page",
                "Senariy · Page filter",
                """
Faqat “Region” sahifasida Region=“Toshkent” bo‘lsin; boshqa sahifalar butun mamlakatni ko‘rsatsin.
""",
                "Qaysi daraja?",
                [
                    "A) Report level — hamma joyga",
                    "B) Page level filter (Region sahifasida)",
                    "C) Tenant admin only",
                    "D) Mobile only",
                ],
                "B",
            ),
        ],
        "homework": _hw(
            """Modul 8 uy vazifasi:

1) Visual/Page/Report filtrlariga bittadan misol yozing.
2) Edit interactions da kamida bitta None sozlang — nima uchun?
3) Sync slicers ni 2 sahifada sinab ko‘ring; natijani .txt da yozing."""
        ),
    },
    {
        "order": 9,
        "title": "Power BI Service",
        "slug": "pbi-service",
        "description": "Workspace, publish, dataset refresh, gateway, sharing va Apps.",
        "lectures": [
            _lec(
                "Publish va Workspace",
                "pbi-publish",
                """
<h2>Dars maqsadi</h2>
<p>Desktop dan Service ga nashr qilish va workspace tushunchasini egallash.</p>

<h2>Publish</h2>
<p>Home → Publish → workspace tanlash. Natija: <strong>Dataset</strong> + <strong>Report</strong>. Keyin Dashboard yasash ixtiyoriy (pin tiles).</p>

<h2>Workspace</h2>
<p>Jamoa ish maydoni. Rollar: Admin, Member, Contributor, Viewer. Shaxsiy “My workspace” — faqat test; production uchun shared workspace.</p>

<h2>Dashboard vs Report</h2>
<ul>
  <li><strong>Report</strong> — sahifali, interaktiv, filtrlar boy.</li>
  <li><strong>Dashboard</strong> — bir ekran, pin qilingan tile lar; “bosh sahifa” uchun.</li>
</ul>
""",
            ),
            _lec(
                "Refresh va Gateway",
                "pbi-refresh",
                """
<h2>Dars maqsadi</h2>
<p>Scheduled refresh va on-premises gateway ni tushunasiz.</p>

<h2>Scheduled refresh</h2>
<p>Dataset settings → Refresh. Kuniga necha marta (licenziyaga bog‘liq). Muvaffaqiyatsiz refresh — credentials/gateway/xato query.</p>

<h2>On-premises data gateway</h2>
<p>Ichki tarmoqdagi SQL/Excel papkaga Service dan yetish uchun gateway o‘rnatiladi. Personal vs Standard (enterprise) mode.</p>

<h2>Import refresh vs DirectQuery</h2>
<p>Import — refresh jadvali. DirectQuery — so‘rov vaqtida manba; gateway baribir on-prem uchun kerak bo‘lishi mumkin.</p>
""",
            ),
            _lec(
                "Ulashish va Apps",
                "pbi-share-apps",
                """
<h2>Dars maqsadi</h2>
<p>Share, App, huquqlar — to‘g‘ri tarqatish modeli.</p>

<h2>Share report</h2>
<p>Tez, lekin boshqaruv qiyin (ko‘p individual share). Kichik auditoriya uchun.</p>

<h2>Power BI App</h2>
<p>Workspace → Create app. Foydalanuvchilar “Apps” dan ochadi. Yangilanishni bir joydan boshqarasiz. Microsoft tavsiya etadigan tarqatish usuli.</p>

<h2>Sensitivity / endorsement</h2>
<p>Certified / Promoted dataset — ishonch. Sensitivity labels — korporativ siyosat.</p>
""",
            ),
        ],
        "practice": {
            "pbi-publish": _quiz(
                "pbi-q9-ws",
                "Senariy · Workspace",
                """
3 ta tahlilchi bitta savdo hisoboti ustida ishlashi kerak; test fayllar “My workspace” da qolmasin.
""",
                "Qayerga publish?",
                [
                    "A) Faqat lokal Disk C",
                    "B) Shared workspace (to‘g‘ri rollar bilan)",
                    "C) Faqat email ilova",
                    "D) CPU registry",
                ],
                "B",
            ),
            "pbi-refresh": _quiz(
                "pbi-q9-gw",
                "Senariy · Gateway",
                """
Dataset ichki SQL Serverga ulangan (Import). Service da refresh “failed – can’t connect”.
""",
                "Eng ehtimoliy yechim yo‘nalishi?",
                [
                    "A) On-premises data gateway + credentials tekshiruvi",
                    "B) Faqat Paint o‘rnatish",
                    "C) Faqat Mobile dark mode",
                    "D) Bookmark qo‘shish",
                ],
                "A",
            ),
            "pbi-share-apps": _quiz(
                "pbi-q9-app",
                "Senariy · App",
                """
200 ta foydalanuvchiga bir xil hisobot paketini berish, keyin yangilanishni markazdan boshqarish kerak.
""",
                "Eng mos usul?",
                [
                    "A) 200 marta individual .pbix email",
                    "B) Workspace dan Power BI App yaratish va auditoriyaga tarqatish",
                    "C) Har kimga Admin huquqi",
                    "D) Theme o‘chirish",
                ],
                "B",
            ),
        },
        "exercises": [
            _quiz(
                "pbi-m9-dash",
                "Senariy · Dashboard",
                """
Rahbariyat “bir ekranli bosh sahifa” so‘raydi; chuqur tahlil alohida.
""",
                "Yondashuv?",
                [
                    "A) Dashboard (pin tiles) + batafsil Report alohida",
                    "B) Farq yo‘q — hammasi bir xil",
                    "C) Faqat Excel",
                    "D) Faqat PDF print",
                ],
                "A",
            ),
        ],
        "homework": _hw(
            """Modul 9 uy vazifasi:

1) Publish qadamlari (yoki imkonsiz bo‘lsa — to‘liq reja) ni yozing.
2) Workspace rollarini jadval qilib tushuntiring.
3) Gateway qachon kerak? Refresh muvaffaqiyatsiz bo‘lsa tekshiradigan 5 band.
.txt"""
        ),
    },
    {
        "order": 10,
        "title": "Xavfsizlik va best practices",
        "slug": "pbi-security",
        "description": "RLS, performance, governance, sertifikatlash — yakuniy modul.",
        "lectures": [
            _lec(
                "Row-Level Security (RLS)",
                "pbi-rls",
                """
<h2>Dars maqsadi</h2>
<p>RLS rollarini yozib, Desktop da “View as” bilan tekshirasiz.</p>

<h2>Nima uchun RLS?</h2>
<p>Bitta dataset — turli foydalanuvchi turli qatorlarni ko‘radi (filial, menejer). Alomat: “har filialga alohida .pbix” emas.</p>

<h2>Qanday</h2>
<ol>
  <li>Modeling → Manage roles</li>
  <li>Rol: <code>DimCustomer[City] = "Toshkent"</code> yoki dinamik: foydalanuvchi email jadvali bilan</li>
  <li>View as → role ni simulyatsiya</li>
  <li>Service da workspace access + role assignment</li>
</ol>

<pre>// Oddiy statik misol
[Region] = "Toshkent"

// Dinamik (soddalashtirilgan g‘oya)
[ManagerEmail] = USERPRINCIPALNAME()</pre>

<h2>Eslatma</h2>
<p>RLS measure yashirmaydi — qatorlarni filtrlaydi. Admin/Member rollari RLS ni chetlab o‘tishi mumkin — huquqlarni to‘g‘ri bering.</p>
""",
            ),
            _lec(
                "Performance maslahatlari",
                "pbi-perf",
                """
<h2>Dars maqsadi</h2>
<p>Sekin hisobotni tuzatish uchun checklist bilasiz.</p>

<h2>Checklist</h2>
<ul>
  <li>Keraksiz ustun/jadvalni Power Query da olib tashlash.</li>
  <li>To‘g‘ri data types; matn-kalitdan qochish.</li>
  <li>Star schema; haddan tashqari Both filter yo‘q.</li>
  <li>Og‘ir custom visual / haddan tashqari vizual soni.</li>
  <li>DAX: iteratorlarni ehtiyot; keraksiz calculated column.</li>
  <li>Import aggregations / incremental refresh (katta model).</li>
</ul>

<h2>Performance analyzer</h2>
<p>View → Performance analyzer — qaysi vizual sekinligini ko‘ring.</p>
""",
            ),
            _lec(
                "Boshqaruv va yakun",
                "pbi-governance",
                """
<h2>Dars maqsadi</h2>
<p>Governance: endorsement, documentation, naming — kurs yakuni.</p>

<h2>Endorsement</h2>
<p><strong>Promoted</strong> / <strong>Certified</strong> dataset — foydalanuvchi ishonchli manbani tanlaydi.</p>

<h2>Naming convention</h2>
<p>Fact/Dim prefikslari, measure larda fe’l yo‘q (“Total Sales”), bir xil til.</p>

<h2>Dokumentatsiya</h2>
<p>Har dataset: egasi, yangilanish vaqti, manbalar, RLS qoidalari. Description maydonlaridan foydalaning.</p>

<h2>Kurs xulosasi</h2>
<p>Siz Microsoft Learn Power BI yo‘nalishidagi asosiy bloklarni qopladingiz: Get Data → Transform → Model → DAX → Visuals → Service → Security. Keyingi qadam — real loyiha va (ixtiyoriy) PL-300 mavzularini chuqurlashtirish.</p>
""",
            ),
        ],
        "practice": {
            "pbi-rls": _quiz(
                "pbi-q10-rls",
                "Senariy · RLS",
                """
Bitta savdo datasetida Toshkent menejeri faqat Toshkent qatorlarini ko‘rsin; boshqa shaharlar ko‘rinmasin. Alohida .pbix ko‘paytirishni xohlamaysiz.
""",
                "Yechim?",
                [
                    "A) Row-Level Security (rol + DAX filtr) + Service da assign",
                    "B) Faqat shriftni kichraytirish",
                    "C) SQL Serverni o‘chirish",
                    "D) Theme JSON",
                ],
                "A",
            ),
            "pbi-perf": _quiz(
                "pbi-q10-perf",
                "Senariy · Sekin report",
                """
Modelda 80 ta keraksiz matn ustuni, 40 ta vizual, Both filter ko‘p joyda. Hisobot ochilishi 20 soniya.
""",
                "Birinchi optimallashtirish?",
                [
                    "A) Keraksiz ustunlarni olib tashlash + vizual sonini kamaytirish + filter yo‘nalishini soddalashtirish",
                    "B) Har doim Both ni ko‘paytirish",
                    "C) 100 ta custom visual",
                    "D) Har qatorga calculated column",
                ],
                "A",
            ),
            "pbi-governance": _quiz(
                "pbi-q10-cert",
                "Senariy · Certified",
                """
Tashkilotda 50 ta o‘xshash dataset. Foydalanuvchilar “qaysi ishonchli?” deb so‘raydi.
""",
                "Power BI dagi mexanizm?",
                [
                    "A) Certified (va/yoki Promoted) endorsement",
                    "B) Virus yuborish",
                    "C) Reportni o‘chirish",
                    "D) Faqat Mobile dark mode",
                ],
                "A",
            ),
        },
        "exercises": [
            _quiz(
                "pbi-m10-test-role",
                "Senariy · View as",
                """
RLS rolini yozdingiz. Service ga chiqmasdan oldin Desktop da tekshirmoqchisiz.
""",
                "Qaysi buyruq?",
                [
                    "A) Modeling → View as (rolni tanlash)",
                    "B) Task Manager → End task",
                    "C) Faqat CSV saqlash",
                    "D) Delete .pbix",
                ],
                "A",
            ),
        ],
        "homework": _hw(
            """Modul 10 yakuniy uy vazifasi:

1) Bitta RLS rol yarating (statik filtr yetarli). DAX qoidasini yozing.
2) View as bilan tekshirish natijasini tavsiflang.
3) Performance checklist bo‘yicha o‘z .pbix ingizni baholang (5 band).
4) Kurs bo‘yicha 10 ta muhim xulosa (har moduldan 1).
.txt, UTF-8."""
        ),
    },
]


def build_powerbi_modules():
    from apps.core.powerbi_teacher_lessons import LECTURES

    for module in MODULES:
        for lecture in module["lectures"]:
            html = LECTURES.get(lecture["slug"])
            if html:
                lecture["content"] = html.strip()
    return MODULES
