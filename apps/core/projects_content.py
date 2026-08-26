"""
Amaliy loyihalar — SQL + Excel + Python + Statistika + Power BI ni birlashtirish.
Talaba haqiqiy tahlilchi kabi ishlaydi: savol, tozalash, KPI, vizual, hisobot.
"""

COURSE_DESCRIPTION = (
    "Yakuniy bosqich: bank, do‘kon, e-commerce, HR va marketingda haqiqiy brief. "
    "O‘qituvchi sizni junior tahlilchidek yo‘naltiradi — javobni o‘zingiz topasiz. "
    "SQL, Excel, Python, statistika va Power BI shu yerda qo‘shiladi."
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


def _project_body(industry, scenario, problem, dictionary, questions, cleaning, kpis, analysis, viz, insights, report, present):
    return f"""
<h2>Soha</h2>
<p>{industry}</p>

<h2>Biznes senariy</h2>
<p>{scenario}</p>

<h2>Biznes muammo</h2>
<p>{problem}</p>

<h2>Dataset va data dictionary</h2>
{dictionary}

<h2>Biznes savollar</h2>
<ol>
{questions}
</ol>

<h2>Tozalash talablari</h2>
<ul>
{cleaning}
</ul>

<h2>KPI talablari</h2>
<ul>
{kpis}
</ul>

<h2>Tahlil talablari</h2>
<ul>
{analysis}
</ul>

<h2>Vizualizatsiya talablari</h2>
<ul>
{viz}
</ul>

<h2>Kutilgan biznes insightlar</h2>
<p>Quyidagi yo‘nalishda <em>o‘zingiz</em> xulosa chiqaring (tayyor javob yo‘q):</p>
<ul>
{insights}
</ul>

<h2>Yakuniy hisobot</h2>
<ul>
{report}
</ul>

<h2>Taqdimot</h2>
<ul>
{present}
</ul>

<h2>Vositalar</h2>
<p>SQL (so‘rovlar), Excel yoki Python (tozalash/EDA), Power BI yoki Excel dashboard. Muhimi — zanjir va qaror, vosita brendi emas.</p>
""".strip()


MODULES = [
    {
        "order": 1,
        "title": "Tahlilchi ish oqimi",
        "slug": "prj-workflow",
        "description": "Brief, ta’riflar, deliverable, sifat mezonlari.",
        "lectures": [
            _lec(
                "Loyiha qanday topshiriladi?",
                "prj-brief",
                """
<h2>Dars maqsadi</h2>
<p>Keyingi modullar “to‘g‘ri SQL yozing” emas. Sizga brief beriladi. Siz savolni aniqlashtirasiz, cheklov yozasiz, tahlil qilasiz, himoya qilasiz.</p>
<h2>Majburiy artefaktlar</h2>
<ol>
  <li>One-pager: savol, populyatsiya, KPI ta’rifi</li>
  <li>Tozalash jurnali</li>
  <li>Jadval/so‘rov yoki notebook</li>
  <li>Dashboard yoki 1 sahifa vizual</li>
  <li>5–8 ta insight + 3 ta harakat</li>
  <li>5 daqiqalik og‘zaki tuzilma (taqdimot)</li>
</ol>
""",
            ),
            _lec(
                "KPI ta’rifi va “bitta haqiqat”",
                "prj-kpi-def",
                """
<h2>Nima uchun?</h2>
<p>Finance “revenue = to‘langan”, Marketing “revenue = created order”. Hisobotlar zid. Loyihada o‘z ta’rifingizni yozing va o‘zgartirmang.</p>
<h2>Namuna</h2>
<p><strong>Faol mijoz:</strong> oxirgi 90 kunda kamida 1 to‘langan buyurtma, test/ichki buyurtmalar yo‘q.</p>
""",
            ),
            _lec(
                "Sifat: nima baholanadi?",
                "prj-rubric",
                """
<h2>Mezonlar</h2>
<table>
  <tr><th>Mezon</th><th>Yomon</th><th>Yaxshi</th></tr>
  <tr><td>Savol</td><td>Hamma narsani chizdim</td><td>3 ta aniq savolga javob</td></tr>
  <tr><td>Ma’lumot</td><td>dropna ko‘r-ko‘rona</td><td>Jurnal: nima, nima uchun</td></tr>
  <tr><td>Insight</td><td>“Savdo oshsin”</td><td>“X kanalda AOV −12%, sabab Y, sinab ko‘rish Z”</td></tr>
  <tr><td>Cheklov</td><td>Yo‘q</td><td>Namuna, missing, mavsum</td></tr>
</table>
""",
            ),
        ],
        "practice": {
            "prj-brief": _quiz(
                "prj-q-art",
                "Artefakt",
                "Loyiha topshirig‘i.",
                "Yetarli emas?",
                ["A) Faqat chiroyli dashboard, ta’rif va insight yo‘q", "B) One-pager + jurnal + insight", "C) KPI ta’rifi", "D) Cheklovlar"],
                "A",
            ),
            "prj-kpi-def": _quiz(
                "prj-q-rev",
                "Revenue",
                "Marketing created, Finance paid.",
                "Siz nima qilasiz?",
                ["A) Ikkalasini aralashtirib yashirish", "B) Ta’rifni yozib, bitta asosiy + ixtiyoriy ikkinchi", "C) KPI ni o‘chirish", "D) p-value"],
                "B",
            ),
            "prj-rubric": _quiz(
                "prj-q-insight",
                "Insight",
                "Yaxshi xulosa?",
                "Qaysi?",
                [
                    "A) Hammasi yaxshi emas",
                    "B) Aniq kesim + son + ehtimoliy sabab + taklif etilgan sinov",
                    "C) 12 ta pie",
                    "D) Faqat mean",
                ],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "Keyingi bank loyihasi uchun one-pager shablonini to‘ldiring (hali to‘liq tahlilsiz):\n"
            "savol, populyatsiya, 3 KPI ta’rifi, 2 xavf (missing/bias).\n"
            "1 sahifa."
        ),
    },
    {
        "order": 2,
        "title": "Loyiha: Bank",
        "slug": "prj-bank",
        "description": "Chakana bank — tranzaksiya, churn risk, mahsulot penetratsiyasi.",
        "lectures": [
            _lec(
                "Brief: depozit va karta faolligi",
                "prj-bank-brief",
                _project_body(
                    "Chakana bank (O‘zbekiston bozori uslubidagi senariy).",
                    "Bank 18 oy davomida kartalar, depozit qoldiqlari va digital loginlar bo‘yicha ma’lumot beradi. Raqobat kuchaygan, raqamli banklar yosh mijozlarni tortmoqda.",
                    "Qaysi segmentlarda faollik tushayapti va qaysi mahsulot kombinatsiyasi ushlab qolish bilan bog‘liq? Kredit skor modeli qurilmaydi — tahlil va monitoring.",
                    """<table>
<tr><th>Jadval</th><th>Ustunlar</th><th>Izoh</th></tr>
<tr><td>customers</td><td>customer_id, region, age_band, segment (mass/affluent), open_date</td><td>1 qator = 1 mijoz</td></tr>
<tr><td>accounts</td><td>account_id, customer_id, type (card/deposit/loan), status, open_date</td><td>Mijozda bir nechta</td></tr>
<tr><td>transactions</td><td>txn_id, account_id, txn_date, amount, channel (POS/ecom/atm/p2p), mcc</td><td>Debit&gt;0 shartini o‘zingiz belgilang</td></tr>
<tr><td>logins</td><td>customer_id, login_date, app (ios/android/web)</td><td>Kunlik unique login hisoblang</td></tr>
</table>
<p>Ma’lumotni SQL sandbox (customers/transactions) yoki o‘xshash CSV bilan simulyatsiya qilishingiz mumkin. Yetishmasa — generator yoki ochiq namuna, lekin dictionary ni saqlang.</p>""",
                    "<li>Oxirgi 90 kunda karta tranzaksiyasi yo‘q, lekin depoziti bor mijozlar ulushi qanday o‘zgaradi?</li>\n<li>Qaysi region/yosh guruhida app login tushgan?</li>\n<li>Karta+depozit kombinatsiyasi faqat kartaga nisbatan qanday farq qiladi (faollik)?</li>",
                    "<li>Test/employee hisoblarini (agar flag bo‘lsa) ajrating.</li>\n<li>Manfiy amount, 0-summa, dublikat txn_id.</li>\n<li>Sana formatlari va kelajakdagi sanalar.</li>",
                    "<li>MAU (oylik faol karta foydalanuvchi) — ta’rifingiz.</li>\n<li>O‘rtacha txn soni / faol mijoz.</li>\n<li>Depozit qoldig‘i median (agar ustun bo‘lmasa — txn proxy bilan cheklov yozing).</li>\n<li>Multi-product rate.</li>",
                    "<li>Oylik trend + kohort (ochilgan oy).</li>\n<li>Churn-risk ro‘yxati: 60+ kun txn yo‘q.</li>\n<li>SQL: GROUP BY, JOIN, ixtiyoriy window.</li>",
                    "<li>Trend chiziq, region bar, funnel yoki sankey o‘rniga oddiy 2 bosqichli filtr.</li>\n<li>Power BI yoki Excel 1 sahifa.</li>",
                    "<li>Qayerda tushish keskin.</li>\n<li>Qaysi mahsulot juftligi “sog‘lomroq”. </li>\n<li>1 ta arzon aralashuv (push, paket, filial).</li>",
                    "<li>8–10 sahifa: executive 1 sahifa, metod, natija, ilova (so‘rov).</li>\n<li>Cheklov: bu skor kartasi emas.</li>",
                    "<li>5 slayd: muammo, yondashuv, 3 topilma, tavsiya, keyingi ma’lumot so‘rovi.</li>",
                ),
            ),
            _lec(
                "Bank: tahlil yo‘l xaritasi",
                "prj-bank-map",
                """
<h2>Tavsiya etilgan ketma-ketlik</h2>
<ol>
  <li>SQL da oylik faol mijoz va txn soni.</li>
  <li>Python/Excel da recency taqsimoti.</li>
  <li>Statistika: median vs mean txn, outlier MCC (katta P2P).</li>
  <li>Power BI: region slicer, oy, kanal.</li>
</ol>
<h2>Xato</h2>
<p>Barcha 0-faol mijozni “churn” deb atash. Hisob yopilganmi yoki shunchaki jim? Status ustunini izlang.</p>
""",
            ),
            _lec(
                "Bank: himoya savollari",
                "prj-bank-qa",
                """
<h2>Sizdan so‘rashlari mumkin</h2>
<ul>
  <li>Faolning ta’rifi o‘zgarsa, ranking o‘zgaradimi?</li>
  <li>Bayram oylari buzadimi?</li>
  <li>P2P ni “savdo”ga qo‘shdingizmi?</li>
</ul>
<p>Javob: sezgirlik (sensitivity) — ta’rifni 60/90/120 kun qilib qayta hisoblang.</p>
""",
            ),
        ],
        "practice": {
            "prj-bank-brief": _quiz(
                "prj-q-bank-churn",
                "Churn",
                "60 kun txn yo‘q.",
                "Darhol churn?",
                ["A) Ha, 100%", "B) Xavf flag; hisob statusi va depozitni ham ko‘rish", "C) Kredit modeli", "D) drop customer"],
                "B",
            ),
            "prj-bank-map": _quiz(
                "prj-q-p2p",
                "P2P",
                "Katta o‘tkazmalar.",
                "KPI da?",
                ["A) Yashirish", "B) Ta’rifda: savdo vs o‘tkazmani ajratish", "C) Hammasini MCC=grocery", "D) Ignore dates"],
                "B",
            ),
            "prj-bank-qa": _quiz(
                "prj-q-sens",
                "Sezgirlik",
                "Stakeholder 90 kun o‘rniga 30 so‘raydi.",
                "Nima qilasiz?",
                ["A) Bahslashib to‘xtash", "B) Ikkala ta’rifni solishtirib ko‘rsatish", "C) Ma’lumotni o‘chirish", "D) Faqat pie"],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "Bank loyihasi 1-versiya:\n"
            "• KPI ta’riflari\n"
            "• SQL yoki Pandas: oylik faol mijoz\n"
            "• Recency histogram g‘oyasi\n"
            "• 3 insight (gipoteza bo‘lsa ham, son bilan)\n"
            "Fayl + 1 sahifa xulosa."
        ),
    },
    {
        "order": 3,
        "title": "Loyiha: Retail",
        "slug": "prj-retail",
        "description": "Do‘kon tarmog‘i — zaxira, kategoriya, ombor vs savdo zali.",
        "lectures": [
            _lec(
                "Brief: kategoriya rentabelligi",
                "prj-retail-brief",
                _project_body(
                    "Oziq-ovqat va uy-ro‘zg‘or retail zanjiri (20+ filial).",
                    "Kategoriya menejeri “suv va non aylanmasi yaxshi, kosmetika jim” deydi. Ma’lumot: savdo, qoldiq, kirim.",
                    "Qaysi SKU/kategoriya pulni muzlatadi (yuqori zaxira, past aylanma) va qayerda stockout yo‘qotilgan savdo beradi?",
                    """<table>
<tr><th>Jadval</th><th>Maydonlar</th></tr>
<tr><td>sales</td><td>date, store_id, sku, qty, net_amount, promo_flag</td></tr>
<tr><td>sku</td><td>sku, category, brand, pack_size</td></tr>
<tr><td>inventory</td><td>date, store_id, sku, on_hand</td></tr>
<tr><td>stores</td><td>store_id, city, format (hyper/mini)</td></tr>
</table>""",
                    "<li>Top/bottom kategoriya margin yo‘q — qty×proxy yoki net_amount bilan aylanma.</li>\n<li>Promo kunlari oddiy kunlardan qanday farq qiladi?</li>\n<li>Mini vs hyper format.</li>",
                    "<li>Manfiy qty (qaytarish) ni alohida oqim.</li>\n<li>SKU mapping yo‘q qatorlar.</li>\n<li>on_hand teshiklari: oldingi kun bilan to‘ldirish yoki flag.</li>",
                    "<li>Sell-through yoki oddiy: savdo qty / o‘rtacha zaxira.</li>\n<li>Stockout kunlari (on_hand=0 va keyin savdo 0).</li>\n<li>Promo ulushi.</li>",
                    "<li>ABC-xyz soddalashtirilgan: aylanma yuqori/past × barqaror/beqaror.</li>\n<li>Filial kesimi.</li>",
                    "<li>Heatmap: kategoriya × format.</li>\n<li>Trend: ombor vs savdo.</li>",
                    "<li>3 SKU: kamaytirish (zaxira).</li>\n<li>3 SKU: to‘ldirish (stockout).</li>\n<li>Promo kannibalizatsiyasi gipotezasi.</li>",
                    "<li>Menejerga 2 sahifa: nima qilish, qaysi do‘konda.</li>",
                    "<li>4 slayd, 1 ta “bu hafta qilamiz” ro‘yxati.</li>",
                ),
            ),
            _lec(
                "Retail: aylanma va stockout",
                "prj-retail-metrics",
                """
<h2>Aylanma</h2>
<p>Yillik savdo / o‘rtacha zaxira. Sizda 8 hafta bo‘lsa — yilliklashtirmang, “haftalik aylanma” deb atang.</p>
<h2>Stockout</h2>
<p>on_hand=0 lekin talab bor edi mi? Talabni ko‘rmaslik mumkin. Proksi: o‘tgan 4 hafta o‘rtacha savdo &gt; 0 va bugun 0 zaxira.</p>
""",
            ),
            _lec(
                "Retail: tavsiya formati",
                "prj-retail-action",
                """
<h2>Yaxshi tavsiya</h2>
<p>“SKU 8821 ni 6 mini-do‘konda 30% kamaytirib buyurtma qiling; oxirgi 8 haftada aylanma 0.2, zaxira 45 kun.”</p>
<h2>Yomon</h2>
<p>“Zaxirani optimallashtirish kerak.”</p>
""",
            ),
        ],
        "practice": {
            "prj-retail-brief": _quiz(
                "prj-q-neg-qty",
                "Manfiy qty",
                "Qaytarish.",
                "?",
                ["A) abs qilib savdoga qo‘shish", "B) Alohida oqim / net ni aniq ta’riflash", "C) O‘chirish jimgina", "D) SKU=null"],
                "B",
            ),
            "prj-retail-metrics": _quiz(
                "prj-q-turn",
                "Aylanma",
                "8 haftalik oyna.",
                "Yaxshi nom?",
                ["A) Yillik aylanma deb yolg‘on", "B) 8 haftalik aylanma / kunlik zaxira kuni — oyna yoziladi", "C) R²", "D) p"],
                "B",
            ),
            "prj-retail-action": _quiz(
                "prj-q-sku",
                "Tavsiya",
                "Yaxshi format?",
                "Nima bor?",
                ["A) Faqat fe’l", "B) SKU, joy, o‘lcham, asos (son)", "C) 20 ta jargon", "D) Pie only"],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "Retail: kamida 1 kategoriya uchun aylanma proksi va 5 SKU ro‘yxati (kamaytirish yoki to‘ldirish).\n"
            "Hisob usuli + 1 grafik."
        ),
    },
    {
        "order": 4,
        "title": "Loyiha: E-commerce",
        "slug": "prj-ecom",
        "description": "Onlayn savdo — funnel, AOV, logistika SLA.",
        "lectures": [
            _lec(
                "Brief: savatdan yetkazib berishgacha",
                "prj-ecom-brief",
                _project_body(
                    "Marketplace/e-com (O‘zbekiston yetkazib berish shaharlar kesimida).",
                    "Trafic oshgan, lekin buyurtma tasdiq va yetkazib berish kechikishi shikoyat keltirmoqda. CFO AOV tushganini ko‘rmoqda.",
                    "Funnel qayerda oqayapti? Qaysi viloyatda SLA buziladi? Chegirma AOV ni “o‘ldirmoqdami”?",
                    """<table>
<tr><th>Jadval</th><th>Maydonlar</th></tr>
<tr><td>sessions</td><td>session_id, date, channel, device, city</td></tr>
<tr><td>orders</td><td>order_id, session_id, status (created/paid/cancelled/delivered), gmv, discount, created_at</td></tr>
<tr><td>order_items</td><td>order_id, sku, qty, price</td></tr>
<tr><td>shipments</td><td>order_id, promised_date, delivered_date, courier</td></tr>
</table>""",
                    "<li>Session → created → paid → delivered konversiyasi.</li>\n<li>AOV paid vs delivered.</li>\n<li>SLA: delivered − promised (ish kuni ixtiyoriy).</li>",
                    "<li>Bot/test session.</li>\n<li>status inkonsistensiya (delivered lekin paid emas).</li>\n<li>Chegirma &gt; GMV.</li>",
                    "<li>CR (session→paid).</li>\n<li>AOV, discount rate.</li>\n<li>On-time %.</li>\n<li>Cancel rate sabab bilan (agar ustun bo‘lsa).</li>",
                    "<li>Kanal × qurilma funnel.</li>\n<li>Shahar SLA.</li>\n<li>Chegirma bucket vs AOV (statistika: median).</li>",
                    "<li>Funnel bar.</li>\n<li>Map o‘rniga shahar jadvali.</li>\n<li>Trend AOV.</li>",
                    "<li>Eng yomon 1 kanal va 1 shahar.</li>\n<li>Chegirma siyosati gipotezasi.</li>\n<li>Logistika courier farqi.</li>",
                    "<li>Funnel sonlari aniq ta’rif bilan.</li>",
                    "<li>Growth vs ops: kim nima qiladi.</li>",
                ),
            ),
            _lec(
                "Funnel tuzog‘i",
                "prj-ecom-funnel",
                """
<h2>Session va buyurtma</h2>
<p>Ko‘p session 1 buyurtmaga. Konversiyani session bazasida yoki unique user bazasida — tanlang va aralashtirmang.</p>
<h2>Attribution</h2>
<p>Last-click kanal bahslashadi. Loyihada “session.channel” last-click deb yozing.</p>
""",
            ),
            _lec(
                "AOV va chegirma",
                "prj-ecom-aov",
                """
<h2>Tahlil</h2>
<p>Chegirma yuqori bucket da AOV past bo‘lishi kannibalizatsiya yoki arzon tovar mixi. Mix ni kategoriya ulushi bilan tekshiring.</p>
""",
            ),
        ],
        "practice": {
            "prj-ecom-brief": _quiz(
                "prj-q-gmv",
                "GMV vs revenue",
                "Yetkazilmagan buyurtma.",
                "AOV asosiy?",
                ["A) Created GMV doim", "B) Paid/delivered ta’rifini yozib asosiy qilish", "C) Discount=GMV", "D) Session AOV"],
                "B",
            ),
            "prj-ecom-funnel": _quiz(
                "prj-q-session",
                "Funnel bazasi",
                "Session vs user.",
                "?",
                ["A) Aralashtirish OK", "B) Bitta baza tanlash va hujjatlashtirish", "C) Faqat pie", "D) Ignore channel"],
                "B",
            ),
            "prj-ecom-aov": _quiz(
                "prj-q-mix",
                "AOV tushishi",
                "Chegirma oshdi.",
                "Keyingi tekshiruv?",
                ["A) Darhol chegirma yopish", "B) Mix/kategoriya va yangi mijoz ulushi", "C) dropna", "D) R²"],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "Funnel 4 bosqich soni (real yoki simulyatsiya).\n"
            "1 shahar on-time %.\n"
            "AOV vs discount scatter yoki bucket.\n"
            "3 ta ops/marketing harakati."
        ),
    },
    {
        "order": 5,
        "title": "Loyiha: Moliya",
        "slug": "prj-fin",
        "description": "P&L yaqinligi — xarajat markazi, variance, cash-ish ko‘rinish.",
        "lectures": [
            _lec(
                "Brief: byudjet vs fakt",
                "prj-fin-brief",
                _project_body(
                    "O‘rta biznes moliyasi (savdo + OPEX).",
                    "CFO oylik variance yig‘ilishida “marketing oshib ketdi, lekin savdo ham” deb bahslashadi. Siz mustaqil rasm berasiz.",
                    "Qaysi xarajat markazlari byudjetdan ±10% og‘di? Qaysi og‘ish savdo hajmiga bog‘liq (o‘zgaruvchan), qaysi biri boshqaruv qarori?",
                    """<table>
<tr><th>Jadval</th><th>Maydonlar</th></tr>
<tr><td>gl</td><td>date, account_code, cost_center, amount, debit_credit</td></tr>
<tr><td>budget</td><td>month, account_code, cost_center, amount</td></tr>
<tr><td>map</td><td>account_code, pnl_line (revenue, cogs, opex_...)</td></tr>
</table>
<p>Agar GL yo‘q bo‘lsa: Excelda 12 oy × 8 qator P&amp;L simulyatsiyasi qiling — lekin mapping qoidasini yozing.</p>""",
                    "<li>Gross margin % trend.</li>\n<li>OPEX / revenue.</li>\n<li>Eng katta noqulay variance.</li>",
                    "<li>Valyuta aralashuvi (agar bor).</li>\n<li>Ichki aylanma dublikat.</li>\n<li>Byudjet oyiga to‘g‘ri qo‘yilmagan.</li>",
                    "<li>Variance = actual − budget (ishora: noqulay xarajat musbat yoki manfiy — belgilang).</li>\n<li>Flex: savdo o‘zgarsa kutilgan COGS.</li>",
                    "<li>Waterfall: byudjet → fakt.</li>\n<li>Cost center ranking.</li>",
                    "<li>Waterfall, jadval (oy × qator), sparklines.</li>",
                    "<li>3 ta boshqariladigan OPEX.</li>\n<li>1 ta “savdo bilan tushuntiriladigan” COGS.</li>",
                    "<li>CFO 1 sahifa + ilova.</li>",
                    "<li>10 daqiqa: variance hikoyasi.</li>",
                ),
            ),
            _lec(
                "Variance tili",
                "prj-fin-var",
                """
<h2>Favorable / unfavorable</h2>
<p>Xarajat byudjetdan past — odatda favorable (lekin underinvest ham bo‘lishi mumkin). Savdo past — unfavorable. Ishorani hisobot boshida qoidalang.</p>
""",
            ),
            _lec(
                "Flex g‘oyasi",
                "prj-fin-flex",
                """
<h2>Hajm</h2>
<p>Savdo +20%, COGS +20% — “marketing aybdor” emas. Avval volume, keyin rate/mix. Sodda flex: expected_cogs = budget_cogs × (actual_rev/budget_rev).</p>
""",
            ),
        ],
        "practice": {
            "prj-fin-brief": _quiz(
                "prj-q-sign",
                "Variance ishora",
                "Hisobot.",
                "Muhim?",
                ["A) Belgilanmasa CFO adashadi", "B) Kerak emas", "C) Faqat p", "D) Pie"],
                "A",
            ),
            "prj-fin-var": _quiz(
                "prj-q-under",
                "Kam xarajat",
                "Marketing byudjetdan 40% past.",
                "?",
                ["A) Doim yaxshi", "B) Favorable ko‘rinishi mumkin, lekin underinvest/kechikkan kampaniya tekshirilsin", "C) Fraud", "D) drop"],
                "B",
            ),
            "prj-fin-flex": _quiz(
                "prj-q-flex",
                "Flex",
                "Savdo oshgan, COGS oshgan.",
                "Avval?",
                ["A) Hammasini OPEX deb ayblash", "B) Hajmga mos kutilgan COGS bilan solishtirish", "C) Ignore map", "D) A/B"],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "8–12 qatorlik mini P&amp;L (byudjet vs fakt).\n"
            "Variance jadvali + 1 waterfall g‘oyasi.\n"
            "3 jumla hikoya CFO uchun."
        ),
    },
    {
        "order": 6,
        "title": "Loyiha: HR",
        "slug": "prj-hr",
        "description": "Headcount, aylanma (turnover), yollash voronkasi.",
        "lectures": [
            _lec(
                "Brief: xodim aylanmasi",
                "prj-hr-brief",
                _project_body(
                    "500+ xodimli kompaniya HR analytics.",
                    "HRBP “IT da odam ketayapti” deydi. Board retention bonus so‘raydi. Siz fakt berasiz: qayerda, qachon, kim (staj, bo‘lim).",
                    "Ixtiyoriy aylanma qayerda yuqori? Yollash voronkasi qayerda qimmat (vaqt/taklif rad)?",
                    """<table>
<tr><th>Jadval</th><th>Maydonlar</th></tr>
<tr><td>employees</td><td>emp_id, dept, grade, hire_date, terminate_date, reason (voluntary/involuntary/null)</td></tr>
<tr><td>headcount_month</td><td>month, dept, hc (yoki o‘zingiz snapshot qiling)</td></tr>
<tr><td>recruiting</td><td>req_id, dept, opened, filled, source, offer_accepted</td></tr>
</table>""",
                    "<li>Voluntary turnover % (yilliklashtirish ehtiyot — oyna yozing).</li>\n<li>90 kun ichida ketish (early turnover).</li>\n<li>Time-to-fill.</li>",
                    "<li>Kelajak terminate_date.</li>\n<li>Ichki o‘tishni termination deb olish.</li>\n<li>Bo‘sh lavozim dublikati.</li>",
                    "<li>Turnover = ketishlar / o‘rtacha HC (ta’rif).</li>\n<li>Early turnover.</li>\n<li>Offer accept rate.</li>",
                    "<li>Bo‘lim × staj kohort.</li>\n<li>Sabab kodlari (agar bor).</li>",
                    "<li>HC trend, turnover bar, funnel recruiting.</li>",
                    "<li>Qaysi bo‘lim + staj guruhi.</li>\n<li>Bonus vs jarayon (so‘rovnoma yo‘q — ehtiyot xulosa).</li>",
                    "<li>PII ni olib tashlang (ism yo‘q).</li>",
                    "<li>HRBP bilan 5 slayd, ism-sharifsiz.</li>",
                ),
            ),
            _lec(
                "Turnover formulasi",
                "prj-hr-turn",
                """
<h2>Ehtiyot</h2>
<p>Oy davomida ketish / oy boshidagi HC ≠ yillik 12×. Qisqa oyna uchun “3 oylik voluntary turnover” deb atang. Annualize qilsangiz — yozing.</p>
""",
            ),
            _lec(
                "Etika va PII",
                "prj-hr-pii",
                """
<h2>Qoida</h2>
<p>Kichik bo‘limda n=3 ketish — odamni tanib bo‘ladi. Agregat yoki “n&lt;5 yashirish”. Loyihada ism ishlatilmasin.</p>
""",
            ),
        ],
        "practice": {
            "prj-hr-brief": _quiz(
                "prj-q-vol",
                "Voluntary",
                "Turnover KPI.",
                "Nima ajratiladi?",
                ["A) Hech narsa", "B) Voluntary vs involuntary (qisqartirish)", "C) Faqat grade", "D) GPS"],
                "B",
            ),
            "prj-hr-turn": _quiz(
                "prj-q-ann",
                "12×",
                "1 oy 2% ketish.",
                "24% yillik?",
                ["A) Doim to‘g‘ri", "B) Qo‘pol annualize — oyna va mavsumni yozing", "C) p=0.02", "D) AOV"],
                "B",
            ),
            "prj-hr-pii": _quiz(
                "prj-q-n3",
                "Kichik n",
                "Bo‘limda 3 ketish.",
                "Hisobot?",
                ["A) Ism bilan", "B) Agregat / yashirish qoidasi", "C) Email dump", "D) Foto"],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "Bo‘limlar bo‘yicha mini turnover (o‘ylab yoki CSV).\n"
            "Early turnover alohida.\n"
            "n&lt;5 yashirish qoidasini qo‘llang.\n"
            "3 ta jarayon tavsiyasi (bonusni yagona yechim qilmang)."
        ),
    },
    {
        "order": 7,
        "title": "Loyiha: Marketing",
        "slug": "prj-mkt",
        "description": "Kanal ROI, kreativ charchash, attribution ehtiyoti.",
        "lectures": [
            _lec(
                "Brief: pullarni qayerga?",
                "prj-mkt-brief",
                _project_body(
                    "D2C brend + performance marketing.",
                    "Haftalik spend 3 kanalga ketadi. CAC oshgan. Kreativlar 4 haftadan keyin “o‘lik”.",
                    "Qaysi kanal incremental ko‘rinadi (ehtiyotkor)? Qayerda frequency haddan oshgan?",
                    """<table>
<tr><th>Jadval</th><th>Maydonlar</th></tr>
<tr><td>spend</td><td>date, channel, campaign, spend, impressions, clicks</td></tr>
<tr><td>leads</td><td>lead_id, date, channel, campaign, is_qualified</td></tr>
<tr><td>customers</td><td>customer_id, lead_id, first_order_at, first_order_gmv</td></tr>
</table>""",
                    "<li>CPL, CAC (birinchi xarid), ROAS (ehtiyot: last-click).</li>\n<li>CTR va frequency proksi (impr / reach yo‘q bo‘lsa impr/click).</li>",
                    "<li>Utm chalkashligi.</li>\n<li>Organic ni paidga yozish.</li>\n<li>Refund dan keyin GMV.</li>",
                    "<li>CAC = spend / new customers (oyna mos).</li>\n<li>Qualified rate.</li>\n<li>Payback oddiy: CAC / oylik margin gipotezasi (yozing).</li>",
                    "<li>Kanal haftalik.</li>\n<li>Kampaniya yoshi vs CTR.</li>",
                    "<li>Spend vs new customers (lag 7 kun).</li>\n<li>Bar CAC.</li>",
                    "<li>Qaysi kampaniyani to‘xtatish (yosh + CAC).</li>\n<li>Attribution cheklovi 1 paragraf.</li>",
                    "<li>CMO: 1 sahifa “to‘xtat / kengaytir / test”. </li>",
                    "<li>3 slayd, last-click ogohlantirishi bilan.</li>",
                ),
            ),
            _lec(
                "CAC oynasi",
                "prj-mkt-lag",
                """
<h2>Lag</h2>
<p>Bugungi spend, ertangi xarid. CAC ni 7 kun siljitib sezgirlik qiling. Aks holda “kanal yomonlashdi” deb yangi kampaniyani o‘ldirasiz.</p>
""",
            ),
            _lec(
                "Incremental emas",
                "prj-mkt-incr",
                """
<h2>Cheklov</h2>
<p>Last-click ROAS brand qidiruvini “qahramon” qiladi. Hisobotda: bu attribution, geo-lift/A/B yo‘q. Tavsiya: kichik holdout test.</p>
""",
            ),
        ],
        "practice": {
            "prj-mkt-brief": _quiz(
                "prj-q-roas",
                "ROAS",
                "Last-click.",
                "?",
                ["A) Aniq incremental", "B) Attribution ko‘rsatkichi, incremental deb da’vo qilmaslik", "C) CAC=0", "D) SQL yo‘q"],
                "B",
            ),
            "prj-mkt-lag": _quiz(
                "prj-q-lag",
                "Lag",
                "CAC hisobi.",
                "Yaxshi amaliyot?",
                ["A) Same-day only doim", "B) Oyna mosligi / lag sezgirligi", "C) Ignore spend", "D) PII dump"],
                "B",
            ),
            "prj-mkt-incr": _quiz(
                "prj-q-brand",
                "Brand search",
                "ROAS yuqori.",
                "?",
                ["A) 10x budget darhol", "B) Ko‘p qismi baribir kelgan bo‘lishi mumkin — test/holdout", "C) drop channel", "D) median=ROAS"],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "3 kanal: spend, leads, customers (8 hafta).\n"
            "CPL/CAC jadvali.\n"
            "1 kampaniya “to‘xtatish” asoslari.\n"
            "Attribution cheklovi paragrafiga."
        ),
    },
    {
        "order": 8,
        "title": "Loyiha: Ishlab chiqarish va capstone",
        "slug": "prj-mfg",
        "description": "Sifat, downtime, yakuniy portfel himoyasi.",
        "lectures": [
            _lec(
                "Brief: liniya samaradorligi",
                "prj-mfg-brief",
                _project_body(
                    "Oziq-ovqat ishlab chiqarish (2 liniya).",
                    "Smena boshlig‘i “B liniya ko‘p to‘xtaydi” deydi. Sifat bo‘limi qayta ishlash (rework) oshganini aytadi.",
                    "Downtime sabablari qayerda? Defect rate qaysi SKU/smenada? Bu savdo bonusini kechiktiradimi?",
                    """<table>
<tr><th>Jadval</th><th>Maydonlar</th></tr>
<tr><td>production</td><td>date, shift, line, sku, planned_qty, actual_qty</td></tr>
<tr><td>downtime</td><td>start, end, line, reason_code, minutes</td></tr>
<tr><td>quality</td><td>batch_id, sku, defect_qty, inspect_qty</td></tr>
</table>""",
                    "<li>OEE soddalashtirish: availability × performance × quality (komponentlarni yozing).</li>\n<li>Defect ppm yoki %.</li>",
                    "<li>Overlap smena.</li>\n<li>0 ga bo‘lish (inspect_qty=0).</li>\n<li>Sabab kodi “other” 40% — ma’lumot sifati.</li>",
                    "<li>Availability = ish vaqti / reja.</li>\n<li>Performance = actual/planned (ishlagan vaqt).</li>\n<li>Quality = (inspect−defect)/inspect.</li>",
                    "<li>Pareto downtime.</li>\n<li>SKU defect.</li>\n<li>Smena solishtiruv (statistika: kichik n).</li>",
                    "<li>Pareto, trend, shift boxplot.</li>",
                    "<li>Top 2 downtime sabab (soat).</li>\n<li>1 SKU sifat hold.</li>\n<li>Ma’lumot: “other” ni kamaytirish.</li>",
                    "<li>Plant manager 2 sahifa.</li>",
                    "<li>Capstone: shu loyiha yoki oldingi 1 tasini 8–10 daqiqa himoya.</li>",
                ),
            ),
            _lec(
                "Pareto va “other”",
                "prj-mfg-pareto",
                """
<h2>80/20</h2>
<p>Daqiqalarning 80% 3 sababda bo‘lishi mumkin. Agar “other” birinchi o‘rinda — avval kodlashni tuzating, aks holda tahlil yolg‘on.</p>
""",
            ),
            _lec(
                "Capstone himoya",
                "prj-capstone",
                """
<h2>8 daqiqa tuzilma</h2>
<ol>
  <li>0:30 — biznes savol</li>
  <li>1:00 — ma’lumot va cheklov</li>
  <li>4:00 — 3 topilma (son)</li>
  <li>2:00 — tavsiya va egasi</li>
  <li>0:30 — keyingi ma’lumot / test</li>
</ol>
<h2>Savol-javob</h2>
<p>“Agar ta’rif o‘zgarsa?” ga sezgirlik bilan javob bering. Portfel: 1 ta chuqur loyiha yaxshiroq, 7 ta sayoz slayddan.</p>
""",
            ),
        ],
        "practice": {
            "prj-mfg-brief": _quiz(
                "prj-q-oee",
                "OEE",
                "Komponentlar.",
                "Nima yoziladi?",
                ["A) Bitta sehrli % ta’rifsiz", "B) Availability, performance, quality — har biri ta’riflangan", "C) Faqat downtime", "D) CAC"],
                "B",
            ),
            "prj-mfg-pareto": _quiz(
                "prj-q-other",
                "Other 40%",
                "Downtime.",
                "Avval?",
                ["A) Other ni ignore", "B) Kodlash sifatini tuzatish / qayta tasnif", "C) drop line B", "D) R²"],
                "B",
            ),
            "prj-capstone": _quiz(
                "prj-q-port",
                "Himoya",
                "Vaqt kam.",
                "Yaxshi?",
                ["A) 20 ta grafik", "B) 3 topilma + aniq egasi bor tavsiya", "C) Faqat Python import", "D) PII"],
                "B",
                difficulty="medium",
            ),
        },
        "exercises": [
            _quiz(
                "prj-final",
                "Akademiya yakuni",
                "Talaba nima qilishi kerak?",
                "Asosiy?",
                [
                    "A) Vosita brendini yodlash",
                    "B) Savol → toza ma’lumot → KPI ta’rifi → tahlil → insight → harakat",
                    "C) Faqat complete lesson",
                    "D) Random chart",
                ],
                "B",
                difficulty="hard",
            ),
        ],
        "homework": _hw(
            "Capstone: ishlab chiqarish YOKI oldingi loyihalardan birini chuqurlashtiring.\n"
            "Topshiriq: hisobot (5–10 sahifa yoki teng notebook) + 8 daqiqa slayd tuzilmasi.\n"
            "Majburiy: ta’riflar, cheklov, 3 insight, 3 harakat (egasi bilan)."
        ),
    },
]


def build_projects_modules():
    from apps.core.projects_teacher_lessons import LECTURES

    for module in MODULES:
        for lecture in module["lectures"]:
            html = LECTURES.get(lecture["slug"])
            if html:
                lecture["content"] = html.strip()
    return MODULES
