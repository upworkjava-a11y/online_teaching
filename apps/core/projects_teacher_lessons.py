"""
Amaliy loyihalar darslari — o‘qituvchi ovozida, noldan.
Har dars junior tahlilchini briefing qilgandek yozilgan; bir xil qolip takrorlanmaydi.
"""

LECTURES = {
    "prj-brief": """
<p>Shu paytgacha sizga “shu so‘rovni yozing”, “shu grafikni chizing” deyilgan. Endi boshqacha. Siz tahlilchisiz. Rahbar kabinetdan chiqib, qisqa brief tashlaydi va javob kutadi — to‘g‘ri JOIN emas, qaror.</p>

<p>Brief — bu topshiriq varaqasi. Unda soha, muammo, qanday jadvallar borligi yoziladi. Lekin “qaysi grafik chiroyli” yozilmaydi. Savolni siz aniqlashtirasiz. Cheklovni siz yozasiz. Himoyani siz qilasiz. Agar savol noaniq bo‘lsa, tahlilni boshlashdan oldin qaytasiz: populyatsiya kim, oyna qancha, nima “muvaffaqiyat”.</p>

<p>Har loyihada men sizdan bir xil zanjirni kutaman. Avval <strong>one-pager</strong>: bitta sahifada savol, kimlarni hisoblaymiz (populyatsiya), KPI ning aniq ta’rifi. Bu sahifa yo‘q bo‘lsa, keyingi yetti sahifa behuda. Keyin <strong>tozalash jurnali</strong>: qaysi qatorni tashladingiz, nima uchun, nechta qoldi. “dropna qildim” — jurnal emas.</p>

<p>Keyin ish izi: SQL so‘rovlari, Excel yoki Python notebook — kimdir takrorlay olishi kerak. Yonida dashboard yoki hech bo‘lmaganda <strong>bitta sahifa vizual</strong>. Chiroyli bo‘lishi shart emas, savolga javob berishi shart. Va matn: <strong>5–8 ta insight</strong> va ulardan chiqadigan <strong>3 ta harakat</strong>. “Savdo oshsin” harakat emas. Kim, qayerda, nima qiladi — shu.</p>

<p>Oxirida og‘zaki himoya. Beshta daqiqa. Slayd ko‘p bo‘lsa, vaqtni o‘ldirasiz. Tuzilmani oldindan yozib qo‘ying: muammo, yondashuv, uchta topilma, tavsiya, keyingi ma’lumot so‘rovi. Rahbar savol beradi — “ta’rif o‘zgarsa nima bo‘ladi?” ga javobsiz qolmang.</p>

<p>Vosita brendi baholanmaydi. SQL, Excel, Python, Power BI — qaysi bilan qilsangiz bo‘ladi. Baholanadigan narsa: savol aniqmi, ma’lumot tozami, KPI bitta haqiqatmi, xulosa son bilanmi, harakat egasi bormi. Keyingi darsda shu “bitta haqiqat” ni ochib beramiz.</p>
""",
    "prj-kpi-def": """
<p>Ikki bo‘lim, ikki “daromad”. Finance aytadi: revenue — <em>to‘langan</em> buyurtma. Marketing aytadi: revenue — <em>yaratilgan</em> buyurtma. Dushanba ertalab ikkala hisobot stolga tushadi, sonlar mos kelmaydi, yig‘ilish buziladi. Aybdor ma’lumot emas. Aybdor — ta’rif yozilmagani.</p>

<p>Siz tahlilchisiz. Loyihada o‘zingizning ta’rifingizni qog‘ozga tushirasiz va o‘zgartirmaysiz. O‘zgartirish kerak bo‘lsa — yangi versiya, eski bilan yonma-yon. “Kecha boshqacha hisoblagandim” himoyada o‘qilmaydi. Bitta asosiy KPI, ixtiyoriy ikkinchi — lekin aralashtirib yashirish yo‘q.</p>

<p>Yaxshi ta’rif uch qismdan iborat. <strong>Kim:</strong> qaysi populyatsiya (test hisoblar, ichki xodimlar, bekor qilinganlar kirmaydimi?). <strong>Qachon:</strong> qaysi oyna, qaysi sana ustuni. <strong>Nima:</strong> qaysi status, qaysi summa (grossmi, netmi, chegirmadan keyinmi). Shu uchtasi yo‘q bo‘lsa, KPI hali taxmin.</p>

<p>Namuna, yodlab qo‘ymang — uslubni oling. <strong>Faol mijoz:</strong> oxirgi 90 kunda kamida bitta <em>to‘langan</em> buyurtma; test va ichki buyurtmalar yo‘q. “Kirgan” emas, “savatga qo‘ygan” emas — to‘langan. 90 kun — oyna; 60 yoki 120 qilsangiz, ranking o‘zgarishi mumkin, shuning uchun oynani yozasiz.</p>

<p>Bo‘limlar zid kelsa nima qilaman? Ikkalasini ham hisoblab, asosiysini tanlaysiz va ikkinchisini izohda qoldirasiz. “Marketing created, Finance paid — asosiy hisobot paid.” Shu jumla sizni yig‘ilishda qutqaradi. P-value bu yerda yordam bermaydi. Avval tilni kelishasiz, keyin model.</p>

<p>Uyga vazifada bank loyihasi uchun one-pager to‘ldirasiz — hali to‘liq tahlilsiz. Savol, populyatsiya, uchta KPI ta’rifi, ikkita xavf (missing yoki bias). Bitta sahifa. Ta’rifni yozish tahlildan oldin bo‘lishi kerakligini shu yerda mashq qilasiz.</p>
""",
    "prj-rubric": """
<p>Chiroyli dashboard — bahoning yarmi ham emas. Men sizning loyihangizni shu stolga qo‘yib, to‘rt savol beraman. Savolga javob bormi? Ma’lumotga ishonch bormi? Xulosa ishlatiladimi? Cheklov yashirilganmi? Qolgani bezak.</p>

<p>Quyidagi jadval — “yomon” va “yaxshi” ning qisqa tarjimasi. O‘zingizni shu yerdan o‘qing, himoyadan oldin:</p>
<table>
  <tr><th>Mezon</th><th>Yomon</th><th>Yaxshi</th></tr>
  <tr><td>Savol</td><td>Hamma narsani chizdim</td><td>3 ta aniq savolga javob</td></tr>
  <tr><td>Ma’lumot</td><td>dropna ko‘r-ko‘rona</td><td>Jurnal: nima, nima uchun</td></tr>
  <tr><td>Insight</td><td>“Savdo oshsin”</td><td>“X kanalda AOV −12%, sabab Y, sinab ko‘rish Z”</td></tr>
  <tr><td>Cheklov</td><td>Yo‘q</td><td>Namuna, missing, mavsum</td></tr>
</table>

<p>Savol haqida. O‘n ikkita pie — savol emas, shovqin. Uchta aniq savolga javob bersangiz, qolgan grafikni ilovaga tashlaysiz. “Hamma narsani ko‘rsatdim” himoyada zaif eshitiladi: demak, muhimini tanlay olmadiniz.</p>

<p>Ma’lumot haqida. Bo‘sh qatorni jimgina o‘chirish — tahlilni buzishi mumkin. Missing o‘zi signal bo‘lishi mumkin: login yo‘qligi, zaxira teshigi, terminate_date kelajakda. Jurnalga yozing: nechta tashlandi, qoida nima, qolgan populyatsiya kim. Keyin kimdir so‘rasa, javobingiz bor.</p>

<p>Insight — son + kesim + ehtimoliy sabab + sinab ko‘rish. “Hammasi yaxshi emas” — shikoyat. “Shu kanalda o‘rtacha chek shuncha tushgan, mix o‘zgargan bo‘lishi mumkin, shu testni qilaylik” — tahlil. Sababni aniq bilmasligingiz mumkin; gipotezani yozasiz, ishonchni oshirib yubormaysiz.</p>

<p>Cheklov yozilmasa, men sizning soningizni butun bozor deb o‘qiyman. Namuna kichikmi? Bayram oyi bormi? Last-clickmi? n=3 bo‘limmi? Shu jumlalarni hisobotning boshiga qo‘ying, oxiriga emas. Yaxshi tahlilchi o‘z ishining chegarasini birinchi aytadi.</p>
""",
    "prj-bank-brief": """
<p>Siz tahlilchisiz. Chakana bank — O‘zbekiston bozori uslubidagi senariy — rahbariyati sizdan javob kutmoqda. Raqobat kuchaygan. Raqamli banklar yosh mijozlarni tortmoqda. Sizga 18 oy davomida kartalar, depozit qoldiqlari va digital loginlar beriladi. Kredit skor modeli qurilmaydi. Sizning ishingiz — tahlil va monitoring: qaysi segmentlarda faollik tushayapti va qaysi mahsulot kombinatsiyasi ushlab qolish bilan bog‘liq.</p>

<p>Ma’lumot to‘rt joyda yotadi. Avval tanishing, keyin so‘rov yozing. <code>customers</code> — bir qator bir mijoz: <code>customer_id</code>, viloyat, yosh guruhi (<code>age_band</code>), segment (<code>mass</code> yoki <code>affluent</code>), hisob ochilgan sana. <code>accounts</code> — mijozda bir nechta bo‘lishi mumkin: karta, depozit, kredit; status va ochilgan sana bor. Statusni e’tiborsiz qoldirmang — keyinroq tushuntiraman.</p>

<table>
  <tr><th>Jadval</th><th>Ustunlar</th><th>Izoh</th></tr>
  <tr><td>customers</td><td>customer_id, region, age_band, segment (mass/affluent), open_date</td><td>1 qator = 1 mijoz</td></tr>
  <tr><td>accounts</td><td>account_id, customer_id, type (card/deposit/loan), status, open_date</td><td>Mijozda bir nechta</td></tr>
  <tr><td>transactions</td><td>txn_id, account_id, txn_date, amount, channel (POS/ecom/atm/p2p), mcc</td><td>Debit&gt;0 shartini o‘zingiz belgilang</td></tr>
  <tr><td>logins</td><td>customer_id, login_date, app (ios/android/web)</td><td>Kunlik unique login hisoblang</td></tr>
</table>
<p>Tranzaksiyada kanal POS, e-com, bankomat, P2P. MCC savdo turini aytadi. Debit nima ekanini siz ta’riflaysiz — masalan amount musbat. Loginlar kunlik unique: bir kunda o‘n marta kirgan odam — bir faol kun. SQL sandboxdagi <code>customers</code>/<code>transactions</code> yoki o‘xshash CSV bilan simulyatsiya qilishingiz mumkin. Yetishmasa generator yoki ochiq namuna — lekin dictionary ni saqlang, ustun nomini o‘ylab o‘zgartirmang.</p>

<p>Rahbarning savollari aniq, lekin javobi siznik. Oxirgi 90 kunda karta tranzaksiyasi yo‘q, lekin depoziti bor mijozlar ulushi qanday o‘zgaradi? Qaysi region yoki yosh guruhida ilova login tushgan? Karta bilan depozit birga bo‘lganlar faqat kartaga nisbatan faollikda qanday farq qiladi? Shu uchtasiga javob bermasangiz, qolgan grafik bezak.</p>

<p>Tozalashni jurnalda yozasiz. Test yoki xodim hisoblari flag bo‘lsa — ajrating, asosiy populyatsiyaga qo‘shmang. Manfiy amount, nol summa, takroriy <code>txn_id</code> — har biri alohida qaror: tashlashmi, tuzatishmi, alohida oqimmi. Sana formatlari chalkash bo‘lishi mumkin; kelajakdagi sanalar ham uchraydi — ularni “ertangi to‘lov” deb yutib yubormang.</p>

<p>KPI ni o‘zingiz ta’riflaysiz va one-pagerga yozasiz. Oylik faol karta foydalanuvchi (MAU) — kim: oyda kamida bitta karta tranzaksiyasimi, login ham hisoblanadimi? Faol mijozga o‘rtacha tranzaksiya soni. Depozit qoldig‘i mediani — agar qoldiq ustuni bo‘lmasa, tranzaksiya proxy bilan cheklov yozing, “qoldiq bor” deb da’vo qilmang. Multi-product rate: bir mijozda karta+depozit (yoki boshqa juftlik) ulushi. Ta’rifni o‘rtada almashtirmang.</p>

<p>Tahlilda oylik trend va ochilgan oy bo‘yicha kohort kerak. Churn-risk ro‘yxati: 60 kundan beri tranzaksiya yo‘qlar — lekin bu hali “ketgan” emas, flag. SQL da GROUP BY, JOIN, ixtiyoriy window yetarli. Vizual: trend chiziq, region ustunlari; funnel yoki sankey o‘rniga oddiy ikki bosqichli filtr ham bo‘ladi. Power BI yoki Excel — bitta sahifa. Vosita brendi muhim emas.</p>

<p>Insightni men bermayman. Qayerda tushish keskin ekanini o‘zingiz topasiz. Qaysi mahsulot juftligi “sog‘lomroq” ko‘rinishini son bilan aytasiz. Bitta arzon aralashuv taklif qilasiz: push, paket, filial — qaysi segmentga, nima uchun. Hisobot 8–10 sahifa: executive bir sahifa, metod, natija, ilovada so‘rov. Cheklovni ochiq yozing: bu skor kartasi emas. Taqdimot — besh slayd: muammo, yondashuv, uchta topilma, tavsiya, keyingi ma’lumot so‘rovi.</p>
""",
    "prj-bank-map": """
<p>Brief ni o‘qidingiz. Endi qayerdan boshlaysiz — shu savolga javob beramiz. Ko‘p kishi darhol churn ro‘yxati va chiroyli xarita chizadi. Men boshqacha ketma-ketlikni tavsiya qilaman. Avval oddiy son, keyin taqsimot, keyin kesim, oxirida dashboard.</p>

<p>Birinchi qadam — SQL. Oylik faol mijoz va tranzaksiya soni. Oy, COUNT DISTINCT mijoz, COUNT tranzaksiya. Trend chiqmasa, qolgan tahlil havoda. JOIN ni shu yerda ishlatasiz: mijoz–hisob–tranzaksiya. MAU ta’rifingiz one-pagerdagi bilan bir xil bo‘lsin.</p>

<p>Ikkinchi — Python yoki Excel da recency taqsimoti. Har mijozning oxirgi karta tranzaksiyasidan beri necha kun o‘tgan. Gistogramma: 0–30, 30–60, 60–90, 90+. Shu yerda “jim”lar ko‘rinadi. O‘rtacha recency yolg‘on gapirishi mumkin — dumi uzun bo‘lsa medianni ham qarang.</p>

<p>Uchinchi — statistika. Tranzaksiya sonida mean va median. Bitta katta P2P o‘tkazma o‘rtachani osmondan ko‘taradi; MCC yoki kanal bo‘yicha outlier ni ajrating. P2P ni “savdo”ga qo‘shsangiz, faollik oshgandek ko‘rinishi mumkin — ta’rifda savdo va o‘tkazmani yozing.</p>

<p>To‘rtinchi — Power BI yoki Excel: viloyat slicer, oy, kanal. Bitta sahifa. Kohort (ochilgan oy) ni ikkinchi sahifaga qo‘yishingiz mumkin, lekin asosiy savol birinchi sahifada javob topsin.</p>

<ol>
  <li>SQL da oylik faol mijoz va txn soni.</li>
  <li>Python/Excel da recency taqsimoti.</li>
  <li>Statistika: median vs mean txn, outlier MCC (katta P2P).</li>
  <li>Power BI: region slicer, oy, kanal.</li>
</ol>

<p>Eng katta xato: barcha noldan faol mijozni “churn” deb atash. Hisob yopilganmi yoki shunchaki jim? Status ustunini izlang. Depoziti bor, kartasi jim — bu boshqa hikoya, “ketgan mijoz” emas. 60 kun tranzaksiya yo‘q — xavf flag. Darhol churn deb yozsangiz, himoyada yiqilasiz.</p>
""",
    "prj-bank-qa": """
<p>Yig‘ilishda slayd chiqarishingiz bilan savol yog‘iladi. Bu yomonlik emas. Yaxshi tahlil shu savollarga oldindan javob tayyorlagan tahlil. Uchta savolni deyarli har doim so‘rashadi. Ularning javobini yodlamang — hisoblab keling.</p>

<p>Birinchi: “Faolning ta’rifi o‘zgarsa, ranking o‘zgaradimi?” Siz 90 kun dedingiz, biznes 30 yoki 60 so‘raydi. Javob bahslashib to‘xtash emas. Ikkala ta’rifni yonma-yon ko‘rsatasiz: qaysi segmentlar o‘rin almashadi, qaysilari barqaror. Bu — sezgirlik (sensitivity). 60, 90, 120 kun qilib qayta hisoblang. Jadval kichik bo‘lsin, uchta ustun, xulosa bir jumla.</p>

<p>Ikkinchi: “Bayram oylari buzadimi?” Navro‘z, yakuniy oylar, aksiya davrlari login va POS ni ko‘tarishi yoki tushirishi mumkin. Trendga qarab “raqamli bank olib ketdi” demasdan oldin o‘sha oylarni belgilab qo‘ying. Mavsumni yozmasangiz, kohortni ham noto‘g‘ri o‘qiysiz.</p>

<p>Uchinchi: “P2P ni savdoga qo‘shdingizmi?” Katta o‘tkazmalar MAU ni va o‘rtacha chekni shishiradi. Kanal yoki MCC bilan ajratilganini ayting. Qo‘shgan bo‘lsangiz — ta’rifda yozilgan bo‘lsin. Yashirish yo‘q, ignore dates yo‘q.</p>

<ul>
  <li>Faolning ta’rifi o‘zgarsa, ranking o‘zgaradimi?</li>
  <li>Bayram oylari buzadimi?</li>
  <li>P2P ni “savdo”ga qo‘shdingizmi?</li>
</ul>

<p>Qisqa formula: stakeholder boshqa oyna so‘rasa, ma’lumotni o‘chirmaysiz va pie chizmaysiz. Ikkala ta’rifni solishtirib ko‘rsatasiz. Himoya shu. Keyingi modulda retail — u yerda ham ta’rif va tavsiya formati sizni saqlaydi.</p>
""",
    "prj-retail-brief": """
<p>Kategoriya menejeri eshikni ochib aytadi: “Suv va non aylanmasi yaxshi, kosmetika jim.” Siz tahlilchisiz. Oziq-ovqat va uy-ro‘zg‘or retail zanjiri, yigirmadan ortiq filial. Ma’lumot: savdo, qoldiq, kirim. Rahbar sizdan his qilishni emas, qayerda pul muzlaganini va qayerda yo‘qolgan savdo borligini kutmoqda.</p>

<p>Muammo ikki tomonlama. Yuqori zaxira, past aylanma — pul tokchada uxlaydi. Zaxira nol, talab bor edi — stockout, yo‘qotilgan savdo. Menejer “kosmetika jim” desa, bu past aylanmami yoki do‘konda umuman yo‘qmi — ma’lumotsiz ajratolmaysiz. Sizning ishingiz: qaysi SKU va kategoriya muzlatadi, qayerda stockout yo‘qotilgan savdo beradi.</p>

<table>
  <tr><th>Jadval</th><th>Maydonlar</th></tr>
  <tr><td>sales</td><td>date, store_id, sku, qty, net_amount, promo_flag</td></tr>
  <tr><td>sku</td><td>sku, category, brand, pack_size</td></tr>
  <tr><td>inventory</td><td>date, store_id, sku, on_hand</td></tr>
  <tr><td>stores</td><td>store_id, city, format (hyper/mini)</td></tr>
</table>
<p>Savdoda promo belgisi bor — oddiy kun bilan aralashtirmang. SKU da kategoriya, brend, o‘ram. Zaxira kunlik <code>on_hand</code>. Do‘kon formati gipermarket yoki mini — aylanma va zaxira siyosati boshqacha bo‘lishi tabiiy, shuning uchun kesim qilasiz.</p>

<p>Uchta biznes savol. Margin yo‘q — aylanmani qty×proxy yoki <code>net_amount</code> bilan qiling, “rentabellik” deb oshirib yubormang. Promo kunlari oddiy kunlardan qanday farq qiladi? Mini va hyper formati bir xilmi? Shu savollarga kategoriya kesimida javob qidiring, butun tarmoqni bitta o‘rtachaga yig‘ib qo‘ymang.</p>

<p>Tozalash. Manfiy qty — qaytarish. Uni abs qilib savdoga qo‘shmang va jimgina o‘chirmang; alohida oqim yoki net ni aniq ta’riflang. SKU mappingi yo‘q qatorlar — “noma’lum kategoriya” deb qoldiring yoki tashlang, lekin jurnalda nechtaligini yozing. <code>on_hand</code> teshiklari: oldingi kun bilan to‘ldirish yoki flag — qaysi yo‘lni tanlasangiz, yozing. Teshikni “nol zaxira” deb o‘qisangiz, soxta stockout chiqadi.</p>

<p>KPI. Sell-through yoki soddaroq: savdo miqdori / o‘rtacha zaxira. Stockout kunlari: <code>on_hand = 0</code> va keyin savdo ham 0 — lekin talab bor edi mi, degan savol ochiq qoladi, keyingi darsda proksi beraman. Promo ulushi: savdo ichida promo_flag ulushi. Tahlilda ABC–XYZ ni soddalashtiring: aylanma yuqori/past × barqaror/beqaror. Filial kesimi majburiy — “butun zanjirda kosmetika yomon” yetarli emas.</p>

<p>Vizual: kategoriya × format heatmap, ombor vs savdo trendi. Insight yo‘nalishi — javobni men aytmayman: uchta SKU kamaytirish (zaxira), uchta SKU to‘ldirish (stockout), promo kannibalizatsiyasi gipotezasi. Hisobot menejerga ikki sahifa: nima qilish, qaysi do‘konda. Taqdimot to‘rt slayd va bitta “bu hafta qilamiz” ro‘yxati. SQL, Excel yoki Python, Power BI yoki Excel — zanjir muhim, brend emas.</p>
""",
    "prj-retail-metrics": """
<p>Aylanma so‘zini hisobotda ishlatish oson. Uni to‘g‘ri hisoblash qiyinroq. Darslikda yillik savdo / o‘rtacha zaxira deyiladi. Sizda sakkiz hafta bo‘lsa, buni 52 ga ko‘paytirib “yillik aylanma” demang. Yolg‘on aniqlik. Oynani yozing: “sakkiz haftalik aylanma” yoki kunlik zaxira kuni. R² bu yerda yordam bermaydi.</p>

<p>Sodda formula, o‘zingizga moslang. Savdo miqdori (yoki net_amount) shu oynada, bo‘luvchi — o‘rtacha <code>on_hand</code>. Natija 0.2 bo‘lsa, zaxira sekin aylanayapti; yuqori bo‘lsa, tokcha tez bo‘shayapti. Mini va hyper ni bir xil chegarada baholamang — format turlicha ishlaydi. Promo kunlarini alohida qatordan oling: aksiya aylanmani sun’iy ko‘taradi.</p>

<p>Stockout yanada nozik. <code>on_hand = 0</code> — zaxira yo‘q. Lekin talab bormidi? Bugun savdo 0 bo‘lishi ikki xil: hech kim so‘ramadi, yoki tokcha bo‘sh edi. Siz talabni to‘g‘ridan-to‘g‘ri ko‘rmasligingiz mumkin. Proksi: o‘tgan to‘rt hafta o‘rtacha savdo noldan katta, bugun zaxira nol. Bu taxmin. Uni “aniq yo‘qotilgan savdo” deb yozmang; “ehtimoliy stockout kuni” deb yozing.</p>

<p>Qaytarishlar aylanmani buzadi. Manfiy qty ni savdoga qo‘shib yuborsangiz, aylanma tushib ketadi yoki teskari ishora chiqadi. Net ta’rifini one-pagerda belgilang: qaytarish ayiriladimi, alohida oqimmi. Promo_flag ni unutmang — aksiya kuni stockout boshqa hikoya.</p>

<p>Hisobotda ikkita son yonma-yon tursin: aylanma (oyna yozilgan) va stockout kunlari (proksi yozilgan). Bitta o‘rtacha “kategoriya yomon” — rubrikadagi yomon insight. SKU va do‘kon gabariti keyingi darsda tavsiyaga aylanadi.</p>
""",
    "prj-retail-action": """
<p>Tahlil yaxshi bo‘lishi mumkin, tavsiya esa “zaxirani optimallashtirish kerak” bo‘lib qoladi. Bu jumlani eshitgan menejer hech narsa qilolmaydi. Siz tahlilchisiz — harakat aniq, o‘lchamli, asosli bo‘lishi kerak. Fe’l yetarli emas. Jargon ham yetarli emas. Pie ham yetarli emas.</p>

<p>Yaxshi tavsiya shunaqa eshitiladi: “SKU 8821 ni olti mini-do‘konda 30% kamaytirib buyurtma qiling; oxirgi sakkiz haftada aylanma 0.2, zaxira 45 kun.” Bu yerda SKU bor, joy bor, o‘lcham bor, asos — son — bor. Kim nima qilishini ertaga ertalab tushunadi. Formatni yodlang: ob’yekt, joy, o‘zgarish, asos. Bittasi tushib qolsa, tavsiya yana “optimallashtiring”ga qaytadi.</p>

<p>Yomon tavsiya: “Zaxirani optimallashtirish kerak.” Qaysi SKU? Qaysi filial? Qancha? Nima asos? Yo‘q. Shu jumlani o‘zingizning qoralamada ko‘rsangiz, o‘chiring va qayta yozing.</p>

<p>To‘ldirish tomoni ham xuddi shu format. “SKU 1104 ni uchta hyperda zaxira kunini 4 dan 10 ga chiqaring; o‘tgan to‘rt hafta o‘rtacha savdo musbat, stockout 6 kun.” Kamaytirish va to‘ldirishni bitta ro‘yxatda aralashtirmang — menejer ikki xil aksiyani aralashtirib yuboradi.</p>

<p>Promo gipotezasi ham harakatga bog‘lanadi. “Kannibalizatsiya bor” yetarli emas. “Shu kategoriya promo kunida qo‘shni SKU savdosi tushganini tekshiring; agar tasdiqlansa, aksiya chuqurligini shu do‘konlarda kamaytiring.” Sinov, shart, joy. Hisobotdagi “bu hafta qilamiz” ro‘yxati shu tilda yoziladi — to‘rtta qator, ko‘p emas.</p>
""",
    "prj-ecom-brief": """
<p>Trafik oshgan. Marketing xursand. CFO esa o‘rtacha chek (AOV) tushganini ko‘rib, o‘yga botgan. Yonida ops: buyurtma tasdiqi va yetkazib berish kechikishi shikoyat keltirmoqda. Siz tahlilchisiz. Marketplace / e-com, O‘zbekiston yetkazib berish shaharlar kesimida. Rahbar bitta rasm kutmoqda: funnel qayerda oqayapti, qaysi viloyatda SLA buziladi, chegirma AOV ni “o‘ldirmoqdami”?</p>

<p>To‘rt jadval, zanjir sessiondan kuryergacha. <code>sessions</code> — session_id, sana, kanal, qurilma, shahar. <code>orders</code> — status: created, paid, cancelled, delivered; GMV, chegirma, created_at. <code>order_items</code> — sku, miqdor, narx. <code>shipments</code> — va’da qilingan sana, yetkazilgan sana, kuryer. Shu zanjirni buzmasdan JOIN qiling. Status inkonsistensiyasi — masalan delivered lekin paid emas — tozalashda chiqadi, uni yashirmang.</p>

<table>
  <tr><th>Jadval</th><th>Maydonlar</th></tr>
  <tr><td>sessions</td><td>session_id, date, channel, device, city</td></tr>
  <tr><td>orders</td><td>order_id, session_id, status (created/paid/cancelled/delivered), gmv, discount, created_at</td></tr>
  <tr><td>order_items</td><td>order_id, sku, qty, price</td></tr>
  <tr><td>shipments</td><td>order_id, promised_date, delivered_date, courier</td></tr>
</table>

<p>Savollar. Session → created → paid → delivered konversiyasi. AOV paid bilan delivered da bir xilmi? SLA: yetkazilgan minus va’da qilingan (ish kuni qilish ixtiyoriy, qilsangiz yozing). Created GMV ni asosiy AOV qilmang — yetkazilmagan buyurtma pul emas. Paid yoki delivered ta’rifini yozib, bitta asosiy qilasiz.</p>

<p>Tozalash. Bot va test session. Status ziddiyati. Chegirma GMV dan katta — bu xato yoki agressiv aksiya, qatorni tashlamasdan oldin sanab yozing. KPI: CR (session→paid), AOV, discount rate, o‘z vaqtida yetkazish ulushi (on-time %), bekor qilish darajasi sabab bilan (ustun bo‘lsa). Tahlil: kanal × qurilma funnel, shahar SLA, chegirma bucketiga qarshi AOV — o‘rtacha emas, median. Statistika shu yerda ishlaydi: dum uzun bo‘lsa mean yolg‘on gapiradi.</p>

<p>Grafik: funnel ustunlari, xarita o‘rniga shahar jadvali, AOV trendi. Insight yo‘nalishi — o‘zingiz topasiz: eng yomon bitta kanal va bitta shahar, chegirma siyosati gipotezasi, kuryerlar orasidagi farq. Hisobotda funnel sonlari aniq ta’rif bilan. Taqdimotda growth va ops ni ajrating: kim nima qiladi. “Hammasi yomon” — harakat emas.</p>
""",
    "prj-ecom-funnel": """
<p>Funnel chizish oson. Uni buzish ham oson. Ko‘p session bitta buyurtmaga tegishli. Bir odam uchtta sessiyada aylanadi, to‘rtinchisida to‘laydi. Agar konversiyani session bazasida sanasangiz, CR pastroq chiqadi. Unique user bazasida — boshqacha. Ikkalasini aralashtirish — xato. Bitta baza tanlang va hujjatlashtiring. Pie bu yerda yordam bermaydi.</p>

<p>Aralashtirish qanday ko‘rinadi. Sarlavhada “session conversion”, jadvallda unique user, izohda “trafik”. Stakeholder solishtirib bo‘lmaydi. One-pagerda bir jumla: “CR = paid buyurtma / session; user emas.” Yoki teskarisi. O‘zgartirsangiz — yangi versiya.</p>

<p>Attribution. Sessiondagi kanal odatda last-click. Marketing boshqa model so‘rashi mumkin. Loyihada shunday yozing: <code>session.channel</code> ni last-click deb olyapmiz. First-click yoki data-driven yo‘q. Shu cheklov funneldagi “yomon kanal” ni ehtiyot qiladi: u oxirgi tegish bo‘lishi mumkin, sabab emas.</p>

<p>Status zanjirini buzmang. Created dan paid ga, paid dan delivered ga. Cancelled ni qayerga qo‘yishingizni yozing — funneldan chiqariladimi, alohida oqimmi. Delivered lekin paid emas qatorlar — ma’lumot sifati, konversiya “mo‘jizasi” emas.</p>

<p>Himoyada so‘rashadi: nima uchun session, nima uchun user? Javob: savol nima. Trafik samaradorligi — session. Mijoz yo‘li — user. Sizning briefingizda trafik va tasdiq bor, shuning uchun session mantiqiy bo‘lishi mumkin — lekin yozing. Keyingi darsda AOV va chegirma shu funnelning oxirgi bosqichini ochadi.</p>
""",
    "prj-ecom-aov": """
<p>Chegirma oshdi, AOV tushdi. Qo‘lni kesib chegirmani yopish — tahlil emas. CFO “o‘ldiryapti” deyishi mumkin. Sizning ishingiz — aralashuvni ajratish. Yuqori chegirma bucketida AOV past bo‘lishi kannibalizatsiya ham, arzon tovar mixi ham, yangi mijoz ulushi ham bo‘lishi mumkin. Darhol yopish — A, B, C ni tekshirmasdan qaror.</p>

<p>Mix. Kategoriya ulushini qarang. Chegirma oshgan oylarda arzon SKU ulushi oshganmi? Unda AOV tushishi kutilgan, marja boshqa savol. Mix o‘zgarmagan, faqat chegirma chuqurlashgan — boshqa hikoya. order_items shu yerda kerak: GMV ni faqat order qatoridan o‘qib, mixni ko‘rmasdan xulosa chiqarmang.</p>

<p>Yangi mijoz. Birinchi xarid odatda kichikroq. Chegirma yangi oqimni tortgan bo‘lsa, AOV tushadi, lekin LTV keyinroq. Sizda LTV to‘liq bo‘lmasligi mumkin — cheklov yozing. Lekin yangi vs qaytgan ulushini ko‘rsatish — “chegirma yomon” ni yumshatadi yoki tasdiqlaydi.</p>

<p>Median. O‘rtacha chek bitta katta buyurtmadan shishadi. Bucket tahlilida median AOV ni qo‘ying. Scatter yoki bucket — ikkalasi ham bo‘ladi, lekin o‘q imzosi: chegirma foizi vs AOV, paid yoki delivered ta’rifingiz bilan.</p>

<p>Harakat tili. “Chegirmani yopamiz” o‘rniga: “shu bucketda mix va yangi mijoz ulushini tekshirdik; agar mix barqaror bo‘lsa, chuqurlikni X dan Y ga tushirish testini qilamiz.” Sinov, shart, o‘lcham. Funneldagi yomon kanal bilan chegirmani bir slaydda aralashtirmang — boshqa egasi, boshqa harakat.</p>
""",
    "prj-fin-brief": """
<p>CFO oylik variance yig‘ilishini ochadi. Marketing: “biz oshib ketdik, lekin savdo ham oshdi.” Savdo: “bizning o‘sishimiz OPEX ni oqlaydi.” Ikkalasi ham o‘z slaydini ko‘rsatadi. Siz tahlilchisiz — o‘rta biznes moliyasi, savdo plus OPEX. Mustaqil rasm berasiz. Qaysi xarajat markazlari byudjetdan ±10% og‘di? Qaysi og‘ish savdo hajmiga bog‘liq (o‘zgaruvchan), qaysi biri boshqaruv qarori?</p>

<p>Uchta jadval, yoki simulyatsiya. Bosh kitob (<code>gl</code>): sana, schyot kodi, cost center, summa, debit/credit. Byudjet: oy, schyot, cost center, summa. Xarita (<code>map</code>): schyot qaysi P&amp;L qatoriga tushadi — revenue, COGS, opex_… Agar GL yo‘q bo‘lsa, Excelda 12 oy × 8 qator P&amp;L simulyatsiyasi qiling. Lekin mapping qoidasini yozing. Schyotni “taxminan marketing” deb qo‘lda surish — tahlil emas.</p>

<table>
  <tr><th>Jadval</th><th>Maydonlar</th></tr>
  <tr><td>gl</td><td>date, account_code, cost_center, amount, debit_credit</td></tr>
  <tr><td>budget</td><td>month, account_code, cost_center, amount</td></tr>
  <tr><td>map</td><td>account_code, pnl_line (revenue, cogs, opex_...)</td></tr>
</table>

<p>Savollar. Gross margin foizi trendi. OPEX / revenue. Eng katta noqulay variance. Tozalash: valyuta aralashuvi bo‘lsa ajrating; ichki aylanma dublikati; byudjet oyiga noto‘g‘ri tushgan yozuvlar. Ishora qoidasini hisobot boshida belgilamasa, CFO adashadi — keyingi darsda tilni ochamiz.</p>

<p>KPI. Variance = fakt minus byudjet. Noqulay xarajat musbatmi manfiymi — belgilang va o‘zgartirmang. Flex: savdo o‘zgarsa kutilgan COGS. Tahlil: waterfall byudjetdan faktga, cost center reytingi. Vizual: waterfall, oy × qator jadvali, sparklines. Pie emas.</p>

<p>Insight yo‘nalishi: uchta boshqariladigan OPEX, bitta “savdo bilan tushuntiriladigan” COGS. Javobni men aytmayman — flex sizga yo‘l ochadi. Hisobot: CFO uchun bir sahifa plus ilova. Taqdimot o‘n daqiqa: variance hikoyasi. “Hammasi oshib ketdi” hikoya emas. Qaysi qator, qancha, hajm yoki qaror.</p>
""",
    "prj-fin-var": """
<p>Variance jadvalidagi plus va minus — til. Tilni qoidalamasangiz, CFO adashadi. Favorable va unfavorable. Xarajat byudjetdan past — odatda favorable. Savdo byudjetdan past — unfavorable. Lekin xarajat pastligi har doim yaxshi emas: underinvest, kechikkan kampaniya, yollash muzlatilgan. “Doim yaxshi” deb yozmang.</p>

<p>Ishorani hisobotning birinchi sahifasida qoidalang. Masalan: “xarajat variance = actual − budget; musbat = noqulay (ko‘p sarfladik).” Yoki teskarisi, finance an’anangizga qarab. Muhimi — bitta qoida, barcha jadvallarda bir xil. Belgilanmasa, bitta slaydda yashil “yaxshi”, boshqasida o‘sha son qizil.</p>

<p>Marketing byudjetdan 40% past. Favorable ko‘rinishi mumkin. Savol: kampaniya o‘tkazilmadi mi, kanal yopildimi, sanalar keyingi oyga surildimi? Faktni “tejash” deb taqdim etish — tahlilni siyosatga aylantiradi. Yoniga savdo va lead sonini qo‘ying. Tejashmi yoki ish qilinmaganmi — ma’lumot aytadi, taxminni yozasiz.</p>

<p>Savdo oshgan, marketing ham oshgan. Bu avtomatik “marketing aybdor” emas. Avval hajm, keyin stavka. Shu ajratish flex darsida. Hozir eslab qoling: variance hikoyasi har qator uchun “nima bo‘ldi” va “bu yaxshimi” ni ajratadi. P-value va pie bu tilda yo‘q.</p>

<p>Himoyada ishora haqida so‘rashsa, qoidani o‘qib bering, bahslashmang. Keyin sezgirlik: ishorani teskarisiga o‘girib, ranking o‘zgarmasligini (faqat rang) ko‘rsating. Rang emas, qator muhim.</p>
""",
    "prj-fin-flex": """
<p>Savdo oshgan, COGS ham oshgan. Hammasini OPEX deb ayblash — yig‘ilishni buzadi. Avval hajm. Sodda flex g‘oyasi: kutilgan COGS = byudjetdagi COGS × (fakt savdo / byudjet savdo). Fakt COGS shu kutilgandan ko‘p bo‘lsa — stavka yoki mix muammosi. Teng bo‘lsa — savdo o‘sgani uchun tabiiy. Mappingni ignore qilsangiz, bu formula ishlamaydi: noto‘g‘ri qatorni COGS deb olgan bo‘lasiz.</p>

<p>Misol o‘ylab ko‘ring. Byudjet savdo 100, COGS 60. Fakt savdo 120. Kutilgan COGS 72. Fakt COGS 71 — hajm tushuntiradi, “xarajat oshib ketdi” degan slayd yolg‘on. Fakt COGS 85 — 13 birlik qoladi, shu yerda narx, yo‘qotish, mix. Marketing shu 13 ning ichida emas.</p>

<p>OPEX ni ham shu mantiqda ajratish mumkin, lekin ehtiyot. Ko‘p OPEX hajmga to‘g‘ri proportsional emas. Ijara savdo 20% oshgani uchun 20% oshmaydi. Shuning uchun flex ni avval COGS ga qo‘llang. OPEX da “boshqaruv qarori” degan ustunni qo‘lda belgilaysiz: qaysi cost center kesilishi yoki kechikishi mumkin.</p>

<p>Waterfall. Byudjet → hajm effekti → stavka/mix → OPEX qarorlari → fakt. Har pog‘ona bitta jumla. O‘n ta pog‘ona — hikoya yo‘qoladi. Uch-to‘rtta yetarli.</p>

<p>A/B bu yerda yo‘q. Sizning qurolingiz — mapping, ishora, flex. CFO o‘n daqiqada shu ketma-ketlikni eshitishi kerak: avval hajmga mos kutilgan COGS, keyin qolgan noqulay OPEX. Keyingi modul HR — u yerda ham “avval formula, keyin bonus” degan tuzoq bor.</p>
""",
    "prj-hr-brief": """
<p>HRBP aytadi: “IT da odam ketayapti.” Board retention bonus so‘raydi. Siz tahlilchisiz, 500+ xodimli kompaniya. Fakt berasiz: qayerda, qachon, kim — staj, bo‘lim. Ism-sharif yo‘q. Ixtiyoriy aylanma qayerda yuqori? Yollash voronkasi qayerda qimmat — vaqt yoki taklif radimi?</p>

<p>Uchta jadval. <code>employees</code>: emp_id, bo‘lim, grade, hire_date, terminate_date, sabab — voluntary, involuntary yoki bo‘sh. <code>headcount_month</code>: oy, bo‘lim, HC; yo‘q bo‘lsa snapshot ni o‘zingiz qilasiz. <code>recruiting</code>: vakansiya, ochilgan, to‘ldirilgan, manba, offer qabul qilinganmi. Turnover KPI da voluntary va involuntary (qisqartirish) ni ajratmasangiz, “IT ketayapti” ni qisqartirish bilan adashtirasiz.</p>

<table>
  <tr><th>Jadval</th><th>Maydonlar</th></tr>
  <tr><td>employees</td><td>emp_id, dept, grade, hire_date, terminate_date, reason (voluntary/involuntary/null)</td></tr>
  <tr><td>headcount_month</td><td>month, dept, hc (yoki o‘zingiz snapshot qiling)</td></tr>
  <tr><td>recruiting</td><td>req_id, dept, opened, filled, source, offer_accepted</td></tr>
</table>

<p>Savollar. Voluntary turnover foizi — yilliklashtirish ehtiyot, oynani yozasiz. 90 kun ichida ketish (early turnover). Time-to-fill. Tozalash: kelajakdagi terminate_date; ichki o‘tishni termination deb olish; bo‘sh lavozim dublikati. Ichki o‘tish ketish emas — headcount bo‘limdan bo‘limga o‘tadi, kompaniyadan chiqmaydi.</p>

<p>KPI ta’rifi. Turnover = ketishlar / o‘rtacha HC — qaysi ketish, qaysi o‘rtacha, qaysi oyna. Early turnover alohida. Offer accept rate. Tahlil: bo‘lim × staj kohorti, sabab kodlari agar bor. Vizual: HC trend, turnover ustunlari, recruiting funnel. PII ni olib tashlang, ism yo‘q. Kichik n haqida keyingi darsda qoida bor — hozir shuni biling: uchta ketishni ism bilan yozish taqiqlanadi.</p>

<p>Insight yo‘nalishi: qaysi bo‘lim va staj guruhi; bonus versus jarayon. So‘rovnoma yo‘q — ehtiyot xulosa. “Bonus bering” yagona yechim bo‘lmasin. Hisobot va taqdimot: HRBP bilan besh slayd, ism-sharifsiz. Board ga ham shu. GPS va fotosurat — yo‘q.</p>
""",
    "prj-hr-turn": """
<p>Oylik ikki foiz ketishni o‘n ikkiga ko‘paytirib “yigirma to‘rt foiz yillik” deyish — tuzoq. Oy davomida ketish / oy boshidagi HC — bu oylik ko‘rsatkich. Uni 12× qilish qo‘pol annualize. Mavsum, kichik HC, bitta ommaviy ketish — hammasi ko‘paytiriladi. p=0.02 ham, AOV ham bu yerda yo‘q.</p>

<p>Qisqa oyna uchun shunday atang: “uch oylik voluntary turnover.” Annualize qilsangiz — yozing: qanday formula, qanday taxmin. Yozmasangiz, Board 24% ni yillik haqiqat deb o‘qiydi va bonus byudjetini shu son ustiga quradi.</p>

<p>Bo‘luvchi ham tuzoq. Oy boshidagi HC, oy oxiridagi, o‘rtacha? Ketishlar oy davomida bo‘lsa, o‘rtacha HC odatda to‘g‘riroq. Formula one-pagerda. Early turnover ni umumiy turnoverga qo‘shib yubormang — yangi xodim ketishi boshqa chora: onboarding, menejer, va’da qilingan rol.</p>

<p>Bo‘lim kesimi. IT da yuqori ko‘rinishi mumkin, chunki HC kichik: ikkita ketish katta foiz. Yoniga son qo‘ying: ketishlar soni va HC. Faqat foiz — kichik bo‘limni “yong‘in” qilib ko‘rsatadi. n&lt;5 qoidasi keyingi dars — lekin foizni ham ehtiyot o‘qing.</p>

<p>Himoyada “24% yillikmi?” desalar: “Bu oylikdan qo‘pol yilliklashtirish, oyna va mavsumni yozganman; asosiy ko‘rsatkich — shu oyna.” Bonus qarori shu ehtiyotdan keyin. Formula avval, siyosat keyin.</p>
""",
    "prj-hr-pii": """
<p>Kichik bo‘limda uchta ketish. Ism yozmasangiz ham, odamni tanib bo‘ladi. “Mart oyida IT da senior ketdi” — ofis buni ismga tarjima qiladi. Siz tahlilchisiz, lekin HR ma’lumoti — odamlar. Etika bu yerda bezak emas, qoida. Email dump, foto, GPS — hisobotga kirmaydi, tahlilga ham.</p>

<p>Loyihada ism ishlatilmasin. Email dump yo‘q, foto yo‘q. emp_id tahlilda qolishi mumkin, hisobotda yo‘q. Kichik hujayra: n&lt;5 bo‘lsa yashirish yoki yuqori agregat. “Yashirish” — sonni yozmaslik, “boshqa” ga qo‘shish, yoki “n kichik, foiz ko‘rsatilmaydi” deb belgilash. Qoidani bir marta yozib, barcha jadvallarda qo‘llang.</p>

<p>Grade × bo‘lim × oy — juda mayda kesim. Uch o‘lchamni birga qo‘ysangiz, n=1 chiqadi. Himoya slaydida bo‘lim darajasi, ilovada ehtiyot kohort. Board “kim ketdi?” deb so‘rasa, ism emas, profil: staj guruhi, voluntary, early yoki yo‘q. Profil ham n kichik bo‘lsa yopiladi.</p>

<p>Recruiting tomoni ham PII. Taklif rad etilgan nomzodlar ro‘yxati hisobotga kirmaydi. Source va accept rate — ha. Funnel sonlari — ha, lekin bitta vakansiyada bitta nomzod bo‘lsa, yana n kichik.</p>

<p>Qisqa qoida, yodlang: kichik bo‘limda n=3 ketish — agregat yoki n&lt;5 yashirish. Hisobot ism-sharifsiz. Bu sizni nafaqat etik, balki rubrikada ham saqlaydi: cheklov yozilgan tahlil — yaxshi tahlil.</p>
""",
    "prj-mkt-brief": """
<p>Haftalik spend uch kanalga ketadi. CAC oshgan. Kreativlar to‘rt haftadan keyin “o‘lik”. CMO so‘raydi: pullarni qayerga? Siz tahlilchisiz — D2C brend, performance marketing. Qaysi kanal incremental ko‘rinadi — ehtiyotkor javob. Qayerda frequency haddan oshgan. Last-click ROAS ni aniq incremental deb yozmang. Bu attribution ko‘rsatkichi.</p>

<p>Uchta jadval. <code>spend</code>: sana, kanal, kampaniya, spend, impressions, clicks. <code>leads</code>: lead_id, sana, kanal, kampaniya, is_qualified. <code>customers</code>: customer_id, lead_id, birinchi xarid vaqti, birinchi xarid GMV. UTM chalkashligi tozalashda chiqadi. Organic ni paidga yozish — klassik zahar. Refund dan keyin GMV ni “sotuv” deb qoldirmang.</p>

<table>
  <tr><th>Jadval</th><th>Maydonlar</th></tr>
  <tr><td>spend</td><td>date, channel, campaign, spend, impressions, clicks</td></tr>
  <tr><td>leads</td><td>lead_id, date, channel, campaign, is_qualified</td></tr>
  <tr><td>customers</td><td>customer_id, lead_id, first_order_at, first_order_gmv</td></tr>
</table>

<p>Savollar. CPL, CAC (birinchi xarid), ROAS — last-click ehtiyoti bilan. CTR va frequency proksi: reach yo‘q bo‘lsa impressions/click yoki kampaniya yoshi bilan CTR. KPI: CAC = spend / yangi mijozlar, oyna mos bo‘lsin. Qualified rate. Payback sodda: CAC / oylik margin gipotezasi — gipotezani yozing, “6 oyda qaytadi” ni fact qilmang.</p>

<p>Tahlil. Kanal haftalik. Kampaniya yoshi versus CTR — charchash shu yerda ko‘rinadi. Spend versus yangi mijozlar, 7 kunlik lag — keyingi dars. Bar CAC. Insight yo‘nalishi: qaysi kampaniyani to‘xtatish (yosh + CAC); attribution cheklovi bitta paragraf. Javobni men aytmayman.</p>

<p>Hisobot CMO uchun bir sahifa: to‘xtat / kengaytir / test. Taqdimot uch slayd, last-click ogohlantirishi bilan. SQL shart emas, lekin zanjir shart. CAC ni nol qilib ko‘rsatish yoki PII dump — yo‘q.</p>
""",
    "prj-mkt-lag": """
<p>Bugungi reklama puli, ertangi xarid. CAC ni shu kunning spendini shu kunning xaridorlariga bo‘lsangiz, yangi kampaniyani o‘ldirasiz. Kampaniya dushanba boshlandi, xaridor juma keldi — dushanba CAC osmon, juma “arzon”. Same-day only har doim yaxshi amaliyot emas. Oyna mosligi va lag sezgirligi — shu.</p>

<p>Amaliyot. Spend ni 7 kun siljitib qayta hisoblang. 0 kun, 7 kun, 14 kun. Ranking o‘zgaradimi? Yangi kanal kech konversiya qilsa, lag sizni aldaydi. Oynani one-pagerga yozing: “CAC = o‘tgan 7 kun spend / shu hafta yangi mijoz” yoki “shu hafta spend / shu hafta mijoz” — qaysi biri ekanini aniq ayting.</p>

<p>Kampaniya yoshi. To‘rt haftadan keyin CTR tushishi charchash bo‘lishi mumkin, lag emas. Ikkalasini aralashtirmang. Yangi kreativning birinchi kunlari yuqori CPC, keyin tushishi ham bo‘ladi. Haftalik qator: spend, clicks, leads, customers, kampaniya yoshi. Shu jadvalsiz “kanal yomonlashdi” demang.</p>

<p>Spend ni ignore qilib faqat lead sanash — CPL yo‘qoladi. Teskari: faqat spend, mijoz yo‘q — CAC yo‘q. Ikkala tomon ham kerak, vaqt siljishi bilan.</p>

<p>Himoyada “nima uchun 7 kun?” desalar: “Sezgirlik qildim, 0/7/14; asosiy hisobotda shu, chunki birinchi xarid odatda shu oynada.” Aniq bilim bo‘lmasa — cheklov. PII dump lagni tuzatmaydi.</p>
""",
    "prj-mkt-incr": """
<p>Brand qidiruvi ROAS da qahramon. Ko‘p qismi baribir kelgan bo‘lishi mumkin. Last-click o‘sha odamni “reklama olib keldi” deb yozadi, chunki oxirgi bosish shu. Incremental emas. Hisobotda shunday yozing: bu attribution, geo-lift yoki A/B yo‘q. 10× byudjet darhol — yo‘q. Kanalni tashlash ham yo‘q. Median = ROAS ham yo‘q.</p>

<p>Nima qilasiz? Kichik holdout test tavsiya qilasiz. Bitta shahar, bitta hafta, brand search ni pasaytirib, organik va to‘g‘ridan-to‘g‘ri kirishni kuzatasiz. Natija yo‘q — shuning uchun hozirgi sonni incremental deb da’vo qilmaysiz. CMO “qahramon kanal” ni kengaytirmoqchi bo‘lsa, slaydda sariq ogohlantirish: last-click, holdout yo‘q.</p>

<p>Charchagan kreativ boshqa narsa. CTR tushgan, CAC oshgan, kampaniya yoshi katta — to‘xtatish asosi attribution emas, charchash. Shu ikkisini bir slaydda aralashtirmang. To‘xtat / kengaytir / test — uch xil quti. Brand search ko‘pincha “test” qutisiga tushadi, “kengaytir” ga emas.</p>

<p>Organic ni paid UTM ga yozish incrementalni yanada yolg‘on qiladi. Tozalashda shu chalkashlikni sanang. Refund GMV ni ROAS ni shishiradi — birinchi xarid netmi grossmi, yozing.</p>

<p>Yakun: ROAS yuqori bo‘lsa ham, “ko‘p qismi baribir kelgan bo‘lishi mumkin — test/holdout.” Shu jumla sizni tahlilchi qiladi. Keyingi modul ishlab chiqarish: u yerda ham “other” qahramon bo‘lib qolishi mumkin — ehtiyot bir xil.</p>
""",
    "prj-mfg-brief": """
<p>Smena boshlig‘i aytadi: “B liniya ko‘p to‘xtaydi.” Sifat bo‘limi qayta ishlash (rework) oshganini aytadi. Savdo bonus kechikishidan noliydi. Siz tahlilchisiz — oziq-ovqat ishlab chiqarish, ikki liniya. Downtime sabablari qayerda? Defect rate qaysi SKU va smenada? Bu savdo bonusini kechiktiradimi? OEE ni bitta sehrli foiz ta’rifsiz qo‘ymang. Availability, performance, quality — har biri yoziladi.</p>

<p>Uchta jadval. <code>production</code>: sana, smena, liniya, SKU, planned_qty, actual_qty. <code>downtime</code>: boshlanish, tugash, liniya, reason_code, daqiqa. <code>quality</code>: batch_id, SKU, defect_qty, inspect_qty. Overlap smena — bir to‘xtash ikki smenaga yozilmasin. inspect_qty = 0 ga bo‘lish — xato, o‘sha batch ni sifat foiziga qo‘shmang. Sabab kodi “other” 40% bo‘lsa — bu topilma emas, ma’lumot sifati; Pareto darsida to‘xtaymiz.</p>

<table>
  <tr><th>Jadval</th><th>Maydonlar</th></tr>
  <tr><td>production</td><td>date, shift, line, sku, planned_qty, actual_qty</td></tr>
  <tr><td>downtime</td><td>start, end, line, reason_code, minutes</td></tr>
  <tr><td>quality</td><td>batch_id, sku, defect_qty, inspect_qty</td></tr>
</table>

<p>OEE ni soddalashtirasiz, komponentlarni yozasiz. Availability = ish vaqti / reja. Performance = actual / planned (ishlagan vaqt ichida). Quality = (inspect − defect) / inspect. Defect ppm yoki foiz — birini tanlang. Tahlil: Pareto downtime, SKU defect, smena solishtiruvi. Statistika: kichik n. Bitta smenada uchta batch — “B yomon” deyish erta.</p>

<p>Vizual: Pareto, trend, smena boxplot. Insight yo‘nalishi: eng katta ikkita downtime sabab (soat bilan), bitta SKU sifat hold, “other” ni kamaytirish uchun ma’lumot ishi. Plant manager ga ikki sahifa. Capstone da shu loyiha yoki oldingi bittasini 8–10 daqiqa himoya qilasiz — oxirgi darsda tuzilma bor.</p>

<p>CAC bu yerda yo‘q. Faqat downtime ham OEE emas. Bitta sehrli foiz ta’rifsiz — rubrikada yomon. Komponentlar yozilgan OEE — yaxshi. Bonus kechikishini OEE ga bog‘lash gipoteza: yetkazib berish kechikdimi, reja bajarilmadi mi — son bilan, lekin sababni oshirib yubormang.</p>
""",
    "prj-mfg-pareto": """
<p>Pareto chizdingiz, birinchi ustun “other”. Tahlilni to‘xtating. Daqiqalarning 80 foizi uchta sababda bo‘lishi mumkin — shu 80/20. Agar “other” birinchi o‘rinda bo‘lsa, avval kodlashni tuzating. Aks holda tahlil yolg‘on. Other ni ignore qilish, B liniyani tashlash, R² — yo‘q. Avval qayta tasnif.</p>

<p>Nima qilinasiz. “Other” qatorlarini sana, smena, operator izohi (agar bor) bilan chiqarib, 20–30 tasini qo‘lda o‘qib, yangi kod taklif qilasiz. Smena boshlig‘iga: “shu daqiqalarni mexanik, xomashyo, kutilish deb ajratamizmi?” Kod sifati tuzalmaguncha “B liniya aybdor” demang — balki B da “other” ko‘proq yoziladi, A da aniqroq.</p>

<p>To‘g‘ri Pareto. Sabablar daqiqa bo‘yicha kamayish tartibida, kumulativ foiz. Top 2–3 ni soatga aylantiring — plant manager daqiqa eshitmaydi, smenani yo‘qotishni eshitadi. Qolgan mayda sabablar “boshqa aniq kodlar” — lekin “other” emas, agar kodlar ishlayotgan bo‘lsa.</p>

<p>Sifat tomoni ham Pareto. Defect qaysi SKU da. Bitta SKU hold: qancha batch, qancha ppm, qaysi liniya. n kichik bo‘lsa, ehtiyot. Boxplot smena bo‘yicha: farq bor ko‘rinsa ham, kichik n da “tungi smena yomon” ni siyosat qilmang — gipoteza, qo‘shimcha kuzatuv.</p>

<p>Ma’lumot ishi ham tavsiya. “Other ni 40 dan 10 foizga tushirish — ikki haftalik kodlash loyihasi, egasi sifat muhandisi.” Bu ham plant manager sahifasiga kiradi. Mashina tuzatish bilan bir qatorda. Aks holda keyingi oy yana o‘sha Pareto.</p>
""",
    "prj-capstone": """
<p>Sakkiz daqiqa. Shu vaqtda rahbar qaror qilishi kerak — sizning Python importlaringizni emas. Yigirma ta grafik, faqat complete lesson, PII, tasodifiy chart — himoya emas. Yaxshi himoya: uchta topilma va aniq egasi bor tavsiya. Portfel: bitta chuqur loyiha yaxshiroq, yetti ta sayoz slayddan. Ishlab chiqarishni chuqurlashtirasiz yoki oldingi loyihalardan bittasini — tanlang, hammasini emas.</p>

<p>Tuzilmani soatga bog‘lang, slayd soniga emas. Yarim daqiqa — biznes savol: kim nima deb noliydi, siz qaysi savolga javob berasiz. Bir daqiqa — ma’lumot va cheklov: qaysi jadvallar, nima yo‘q, ta’rif. To‘rt daqiqa — uchta topilma, har biri son bilan. Ikki daqiqa — tavsiya va egasi: kim, qachon, nima. Yarim daqiqa — keyingi ma’lumot yoki test. Qolgan vaqt savol-javob, u ham sezgirlik bilan.</p>

<ol>
  <li>0:30 — biznes savol</li>
  <li>1:00 — ma’lumot va cheklov</li>
  <li>4:00 — 3 topilma (son)</li>
  <li>2:00 — tavsiya va egasi</li>
  <li>0:30 — keyingi ma’lumot / test</li>
</ol>

<p>“Agar ta’rif o‘zgarsa?” — sezgirlik. Bankda 60/90/120, marketda lag, moliyada flex, HR da oyna. Tayyorlab keling. Savol yo‘qligini kutmang. Chuqur loyiha: bank, retail, e-com, moliya, HR, marketing yoki ishlab chiqarish — bittasini oling, hammasini sayoz qilib yig‘mang.</p>

<p>Slaydlarni oldindan ovoz chiqarib o‘qing. To‘rt daqiqalik “uch topilma” qismida har topilma: kesim, son, nima demak. Grafik gapirmaydi — siz gapirasiz. Tavsiyada egasi lavozim bilan: kategoriya menejeri, kuryer ops, HRBP, CMO. “Kimdir qilsin” — harakat emas.</p>

<p>Topshiriq. Hisobot 5–10 sahifa yoki teng notebook, plus sakkiz daqiqalik slayd tuzilmasi. Majburiy: ta’riflar, cheklov, uchta insight, uchta harakat — egasi bilan. Akademiya yakuni shu zanjir: savol → toza ma’lumot → KPI ta’rifi → tahlil → insight → harakat. Vosita brendini yodlash — yo‘q. Siz tahlilchisiz. Rahbar javob kutmoqda. Endi o‘zingiz bering.</p>
""",
}
