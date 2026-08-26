"""
Power BI darslari — o‘qituvchi ovozida, noldan.
Har dars talaba bilan gaplashgandek yozilgan; bir xil qolip takrorlanmaydi.
"""

LECTURES = {
    "pbi-nima": """
<p>Salom. Excelda pivot, VLOOKUP, grafik qilgan bo‘lsangiz — yaxshi. Shu yerda o‘sha ishning keyingi qadami. Power BI yangi dastur, lekin mantiq tanish: jadval, filtr, yig‘indi. Faqat endi bir fayl emas, butun tarmoq: savdo, filial, mahsulot — bir joyda, va rahbar brauzerda ochadi.</p>

<p>Oddiy savol: nima uchun Excel yetmay qoladi? Tasavvur qiling, do‘kon tarmog‘i. Toshkentda 8 ta filial, Samarqandda 3 ta, Farg‘onada 2 ta. Har kuni savdo CSV keladi. CFO so‘raydi: “Bugun qancha? Viloyat Toshkentdan qolganmi?” Siz 12 ta faylni qo‘lda yig‘asiz, pivot qilasiz, email qilasiz. Ertaga yana. Versiya chalkashadi: kimdir “savdo_final2_haqiqiy.xlsx” yuboradi. Power BI shu charchoqni yechish uchun: manbalarni ulaysiz, bir marta tozalaysiz, model qilasiz — keyin yangilash tugmasi.</p>

<p>Uchta narsa, aralashtirmang. <strong>Power BI Desktop</strong> — Windows dasturi. Shu yerda yasaysiz: ulanish, tozalash, DAX, grafik. Fayl <code>.pbix</code>. <strong>Power BI Service</strong> — app.powerbi.com, brauzer. Shu yerda nashr qilasiz, ulashasiz, kechasi avtomatik yangilaysiz. <strong>Mobile</strong> — yo‘lda ko‘rish. Qoida oddiy: yaratish Desktop da, tarqatish Service da. Mobile da model yozilmaydi.</p>

<p>Excel bilan farqni ochiq aytaman. Excel — hujjat: ochdingiz, o‘zgartirdingiz, saqladingiz. Power BI da esa ikki qatlam: avval <em>dataset</em> (tozalangan jadvallar va o‘lchovlar), keyin <em>hisobot</em> (sahifalar, vizuallar). Bir datasetdan bir nechta hisobot chiqishi mumkin. “Bitta haqiqat” shu datasetda turadi — CFO va filial menejeri bir xil summani ko‘radi, har kim o‘z Excelini chizmaydi.</p>

<p>Kim nima qiladi? Siz — tahlilchi: Desktop da model va dashboard. IT ba’zan SQL view, gateway, huquqlarni beradi. Rahbar Service yoki telefonda ochadi, slicer bosadi, raqamni o‘qiydi. Sizning ishingiz — ular ishonadigan raqam va tushunarli sahifa.</p>

<p>Kurs bo‘ylab O‘zbekiston savdo tarmog‘i misolida yuramiz: so‘m, filial, Toshkent vs viloyat, chek, mahsulot. Bank yoki ombor bo‘lsa ham, mantiq bir xil. Keraklisi: qayerga bosasiz, nima uchun, qayerda odamlar yiqiladi.</p>

<p>Quyidagi savolni hozir yodda tuting. CFO har kuni yangilanadigan savdo dashboardini so‘rasa — qayerda yasaysiz, qayerda ulashasiz? Javob: Desktop da .pbix, Service orqali odamlarga. Keyingi darsda shu yo‘lni bosqichma-bosqich ochamiz.</p>
""",
    "pbi-workflow": """
<p>Power BI ni ochib, darhol chiroyli grafik chizish — eng ko‘p qilinadigan xato. Raqam “g‘alati” chiqadi, sana matn bo‘lib qoladi, ikki jadval bir-birini tanimaydi. Sabab: tartib buzilgan. Bugun zanjirni yodlab qo‘yamiz. U Exceldagi “avval xom jadval, keyin pivot” ga o‘xshaydi, faqat aniqroq.</p>

<p>Birinchi bosqich — <strong>ulanish</strong>. Home lentasida <strong>Get data</strong>. Excel, CSV, SQL, ba’zan papkadagi oylik fayllar. Hali hech narsa chizilmaydi: faqat “qayerdan olib kelaman”.</p>

<p>Ikkinchi — <strong>tozalash</strong>. Bu Power Query. Tip, bo‘sh qator, dublikat, “Hisobot 2024” degan keraksiz sarlavha. Excelda qo‘lda tozalagan bo‘lsangiz, farq shunda: bu yerda har qadam yozib qolinadi. Ertaga yangi CSV tushsa, Refresh — qadamlar qayta yuradi.</p>

<p>Uchinchi — <strong>model</strong>. Savdo bitta jadval, filiallar boshqa, mahsulotlar uchinchi. Ularni kalit bilan bog‘laysiz. Nima uchun muhim? Chunki “Toshkent filiali savdosi” degan savol ikki jadvalni talab qiladi. Bog‘lanish bo‘lmasa, slicer ishlamaydi yoki yig‘indi shishadi. Model — hisobotning skeleti. Chiroyli grafik skeletsiz — bezak.</p>

<p>To‘rtinchi — <strong>hisob</strong> (DAX). Excel formulasi katakka yozilardi. Bu yerda odatda <em>measure</em>: Jami savdo, o‘rtacha chek, Toshkent ulushi. Vizual filtrlanganda qayta hisoblanadi. Beshinchi — <strong>chizish</strong>: sahifa, card, chiziq, ustun, slicer. Oltinchi — <strong>ulashish</strong>: Publish, workspace, kim ko‘radi.</p>

<p>Import va DirectQuery haqida ikki gap, chalkashtirmang. <strong>Import</strong> — ma’lumot modelga yuklanadi, vizual tez, kechasi yangilaysiz. O‘rganish va deyarli barcha CFO dashboardlari shu. <strong>DirectQuery</strong> — har bosishda so‘rov bazaga ketadi; “jonli” kerak bo‘lsa, lekin sekin va manbaga og‘ir. Boshlashda Import.</p>

<p>Hayotiy zanjir. Kunlik savdo Excelda, mijozlar SQL da. Get data (ikkala manba) → Power Query da <code>filial_id</code> ni bir xil qilish → FactSavdo ni DimFilial va DimMijoz ga bog‘lash → <code>Jami savdo</code> measure → rahbariyat sahifasi → Service. Transform yoki Model ni o‘tkazib yuborsangiz, 12 ta vizual chizsangiz ham, ishonchsiz hisobot chiqadi. Avval toza ma’lumot, keyin rang.</p>
""",
    "pbi-desktop-ui": """
<p>Dastur ochildi. Birinchi daqiqa: chapda, o‘ngda, tepada hammasi birga gapirayotgandek. Sokin. Sizga uchta ko‘rinish yetarli. Chap pastki burchakda ikonkalar: <strong>Report</strong>, <strong>Data</strong>, <strong>Model</strong>.</p>

<p><strong>Report</strong> — oq varaq. Shu yerda sahifa va grafiklar. Oxirgi foydalanuvchi shuni ko‘radi. <strong>Data</strong> — Exceldagi jadvalga o‘xshash: ustunlar, qatorlar namuna. “Summa haqiqatan sonmi?” ni shu yerda ko‘z bilan tekshirasiz. <strong>Model</strong> — jadvallar qutichalari va ular orasidagi chiziq. Bog‘lanish shu chiziq. Cardinality ni (1 va *) shu yerda o‘qiysiz.</p>

<p>O‘ngda ikkita muhim panel. <strong>Fields</strong> — jadvallar, ustunlar, keyinroq measure lar. Grafikka tashlash uchun shu yerdan tortasiz. <strong>Visualizations</strong> — vizual turi (card, ustun, chiziq…) va pastida “quduqlar”: Axis, Values, Legend. Noto‘g‘ri quduqqa tashlasangiz, grafik g‘alati bo‘ladi — dastur buzilgani emas, joylashuv xato. Yana <strong>Filters</strong> paneli: bitta vizual, butun sahifa yoki butun hisobot.</p>

<p>Tepada lenta (ribbon). Hozir uchta tugma eslab qoling: <strong>Get data</strong>, <strong>Transform data</strong> (Power Query ochiladi), <strong>New measure</strong>. Keyinroq Publish. Qolgani ishga tushganda o‘rganiladi — hammasini bir kunda yodlamang.</p>

<p>Fayl haqida. Sizning loyihangiz — <code>.pbix</code>: ichida ma’lumot (Import bo‘lsa), model, DAX, sahifalar. Hamkasbga yuborsangiz, shu fayl. <code>.pbit</code> — shablon: tuzilma bor, ma’lumot keyin yuklanadi. Hisobotni Word yoki PDF deb o‘ylamang: asosiy ish .pbix da.</p>

<p>Kichik odatlar, keyin minnatdor bo‘lasiz. Jadval nomini tushunarli yozing: <code>FactSavdo</code>, <code>DimFilial</code>, “Table1” emas. Measure: <code>Jami savdo</code>. Keraksiz ustunni Power Query da olib tashlang — Fields toza bo‘lsin. Katta o‘zgarishdan oldin fayl nusxasini oling. Har 15 daqiqada saqlang. Desktop ba’zan og‘ir modelda “o‘ylab” qoladi — saqlanmagan ish achchiq.</p>

<p>Hozir qiling: bo‘sh .pbix oching, uchta view ni bosib chiqing, Fields va Visualizations ni toping. Hali ma’lumot yo‘q — shunday bo‘lishi kerak. Keyingi darsda Get data.</p>
""",
    "pbi-get-data-asos": """
<p>Hisobot bo‘sh varaq emas. Avval ma’lumot kelishi kerak. Home → <strong>Get data</strong>. Oyna ochiladi: Excel, CSV/Text, SQL Server, papka, veb… Ishda 80 foiz holat shu to‘rtta: Excel, CSV, SQL, Folder. Yuzlab connector ko‘rinadi — chalg‘imang. Keragini qidiring.</p>

<p>Ulangach <strong>Navigator</strong> chiqadi. Exceldagi varaqlar, bazadagi jadvallar ro‘yxati. Belgilab, pastda ikki yo‘l: <strong>Load</strong> — to‘g‘ridan-to‘g‘ri modelga; <strong>Transform data</strong> — avval Power Query. Mening maslahatim: o‘rganishda doim Transform. Load qilsangiz ham keyin Transform data bilan qaytasiz, lekin “ertalab tozalayman” odatda unutiladi. Keraksiz varaqni belgilamang: “Pivot_eski”, “Sheet3” modelni shishiradi.</p>

<p>Ulanish rejimi. Navigator yonida yoki SQL oynasida: <strong>Import</strong> yoki <strong>DirectQuery</strong>. Import — ma’lumot .pbix / dataset xotirasiga ko‘chadi. Slicer tez. Yangilash — jadval bo‘yicha (ertalab, kechasi). DirectQuery — ma’lumot joyida qoladi, har filtrda so‘rov ketadi. “Har doim jonli” jozibali eshitiladi. Lekin 200 menejer bir vaqtda ochsa, SQL server ingillaydi, dashboard sekin. Marketing kechagi kampaniyani ertalab ko‘rmoqchi, 2 million qator, kuni bir marta yangilash yetarli — Import + kechasi refresh. Omborda har 5 daqiqada qoldiq kerak va DBA ruxsat bergan — unda DirectQuery ni o‘ylab ko‘ring.</p>

<p>Credential — kimligingiz. Excel mahalliy fayl bo‘lsa, odatda Windows. SQL da Windows, database login yoki Microsoft hisobi. Parolni jadval ichiga yozib qo‘ymang, .pbix ni email qilmang. Service da dataset uchun alohida login sozlanadi. Shu yerdan xavfsizlik boshlanadi.</p>

<p>Yana bir tuzoq: “hamma narsani olamiz, keyin keragini tanlaymiz.” Millionlab qator, 80 ta izoh ustuni. Desktop og‘irlashadi, refresh uziladi. Avval biznes savoli: CFO ga nima kerak? Savdo, filial, sana, mahsulot. Qolganini olmang. Kerak bo‘lsa keyin qo‘shasiz.</p>

<p>Amaliy ssenariy. Savdo tarmog‘i: kunlik Excel + mijozlar SQL da. Get data → Excel (savdo varag‘i, Transform) → yana Get data → SQL (mijozlar view, Import). Ikkalasi Fields da paydo bo‘ladi. Hali bog‘lanmagan — bu keyingi modullar. Bugun: to‘g‘ri manba, to‘g‘ri rejim, Navigator da kerakli varaq, Transform.</p>
""",
    "pbi-excel-csv": """
<p>Ko‘pchilikning birinchi manbasi — tanish fayl: Excel yoki CSV. “Oddiy” deb o‘ylamang. Ishdagi fayllar chiroyli emas: tepada “Savdo hisoboti — mart 2024”, birlashtirilgan kataklar, vergul o‘rniga nuqta, bo‘sh ustunlar. Power BI ularni “tushunadi” deb kutmang. Siz aytasiz.</p>

<p>Get data → Excel yoki Text/CSV. CSV da delimiter so‘ralishi mumkin: vergul, nuqtali vergul, tab. O‘zbekistonda Excel ko‘pincha <code>;</code> yoki vergul, o‘nlik esa <code>1,5</code> yoki <code>1.5</code>. Locale noto‘g‘ri bo‘lsa, summa matn bo‘lib qoladi yoki 150000 “15” bo‘lib ketadi. Preview ni diqqat bilan o‘qing. Keyin Transform.</p>

<p>Eng ko‘p uchraydigan manzara: birinchi qator sarlavha emas, balki “Hisobot 2024”. Haqiqiy ustun nomlari ikkinchi qatorda. Power Query da: avval <strong>Remove top rows</strong> (1 qator), keyin <strong>Use first row as headers</strong>. Aks holda ustunlar Column1, Column2 bo‘ladi, DAX yozolmayiz. Uch qatorli “chiroyli” header — yana Remove top rows.</p>

<p>Exceldagi birlashtirilgan kataklar (merged cells) dushman. Filial nomi faqat birinchi qatorda yozilgan, pastdagilar bo‘sh. Power Query da null. Yechim: <strong>Fill down</strong> — bo‘sh joylarni yuqoridagi qiymat bilan to‘ldirish. Qo‘lda 500 qatorni to‘ldirmang.</p>

<p>Bo‘sh ustunlar, “Unnamed”, oxiridagi bo‘sh qatorlar — darhol olib tashlang. Sana ba’zan matn: <code>19.03.2024</code>. Change type → Date, locale ni tekshiring. Xato (error) chiqsa, Preview qizil katak beradi — yashirma, tuzating yoki filtrlang.</p>

<p>Har oy yangi CSV papkaga tushadimi? Get data → <strong>Folder</strong> → Combine. Birinchi fayl namuna, qolganlari shu qolipta yig‘iladi. Refresh da yangi oy o‘zi qo‘shiladi. Fayl nomida sana bo‘lsin: <code>savdo_2024_03.csv</code>. “final_haqiqiy(2).csv” — ertaga kimdir adashadi.</p>

<p>Yaxshi odat: manba faylni o‘zgartirishdan oldin nusxa. Power Query “Source” qadami yo‘lni eslab qoladi. Faylni boshqa papkaga ko‘chirsangiz, refresh sinadi. Yo‘lni barqaror qiling yoki keyinroq parametr. Bugun: bitta haqiqiy (yoki ataylab “kir”) Excel/CSV ni ulab, header va tipni tuzating. Measure yozish hali erta.</p>
""",
    "pbi-sql-source": """
<p>Excel yetmasa, ma’lumot odatda bazada yotadi. SQL kursini o‘qigan bo‘lsangiz, jadval va view tanish. Power BI ularni “Get data → SQL Server” (yoki PostgreSQL, Azure SQL) orqali o‘qiydi. Siz Desktop dasiz, server boshqa xonada yoki bulutda. Shuning uchun login va ba’zan gateway kerak.</p>

<p>Oyna: server nomi, ixtiyoriy database, Import yoki DirectQuery, Authentication. Windows — ofis kompyuteridagi hisob. Database — SQL login. Microsoft account — bulut. Noto‘g‘ri rejim: “baza katta, demak DirectQuery.” Hajm yolg‘iz mezon emas. Kuniga bir marta yangilash yetarli bo‘lsa, Import tinchroq. DBA dan so‘rang: qaysi <strong>view</strong> hisobot uchun? Xom <code>savdo_log</code> da millionlab texnik qator bo‘lishi mumkin. View — kelishilgan qatlam: kerakli ustunlar, filtrlangan holat.</p>

<p><strong>Query folding</strong> — og‘zaki: Power Query dagi filtr, ustun tanlash bazaga SQL qilib qaytariladimi? Qaytarilsa, million qator kompyuteringizga kelmaydi, serverning o‘zi qisqartiradi. Folding uzilsa (murakkab M, ba’zi amallar), hammasi Desktop ga oqadi — sekin, xotira. Amaliy qoida: filtrni erta qo‘ying, “avval hammasini olib, keyin Toshkentni qoldiraman” demang. Advanced Editor da sariq “View Native Query” bo‘lsa — folding ishlayapti, degan ishora.</p>

<p>Parolni .pbix ichidagi calculated table ga yozib, email qilish — yomon odat. Faylni ochgan odam manbaga yaqinlashishi mumkin. Service da dataset credentials alohida. Ichki SQL (ofis tarmog‘i) uchun Service to‘g‘ridan-to‘g‘ri kira olmaydi — <strong>on-premises data gateway</strong> kerak. Buni refresh darsida ochamiz. Hozir biling: Desktop da ishlashi Service da ishlashini bildirmaydi.</p>

<p>Web/API ham manba. JSON keladi, Expand record/list qadamlari kerak. Kalit, OAuth, rate limit — oldindan. Boshlang‘ich dashboardda SQL + Excel yetarli. API ni “qiziq” deb olmang, IT bilan kelishmasdan.</p>

<p>Xato: SELECT * ni Native Query ga yozib, keraksiz ustunlarni keyin olib tashlash — folding va tarmoq uchun og‘ir. Yaxshisi: view yoki aniq ustunlar. Yana: test bazasiga ulanib, production raqamini kutish. Server nomini yozib qo‘ying. Kichik mashq: bitta view ni Import qilib oling, Data view da 20 qator ko‘ring, tiplarni tekshiring. Query yozishni Power BI da mashq qilish shart emas — toza view DBA bilan qimmatroq.</p>
""",
    "pbi-pq-editor": """
<p>Yukladik. Lekin “kir” keldi: null, dublikat, noto‘g‘ri tip. Excelda qo‘lda tozalash ertaga takrorlanmaydi. Power Query shu takrorlanadigan retsept. Home → <strong>Transform data</strong>. Yangi oyna: chapda so‘rovlar (har jadval — query), o‘rtada preview, o‘ngda <strong>Applied Steps</strong>.</p>

<p>Applied Steps — oltin. Har marta Filter, Change type, Remove column qilsangiz, yangi qadam qo‘shiladi. Bosib, o‘sha paytgi holatni ko‘rasiz. Xato 5-qadamda chiqsa, butun .pbix ni o‘chirmang: shu qadamni tuzating yoki o‘chiring. Qadam nomini o‘zgartiring: “Changed Type1” o‘rniga “Summani songa o‘tkazdim”. Olti oy keyin o‘zingiz tushunasiz.</p>

<p>Chapda query nomi ham muhim. <code>Savdo_2024</code> yaxshi, <code>Query1</code> yomon. O‘ng tugma: Duplicate (xavfsiz tajriba), Reference (boshqa query shunga tayanadi — ehtiyot). Disable load — yordamchi query modelga kirmasin, faqat oraliq. Katta modelda shu bilan xotira tejaladi.</p>

<p>M tili. Advanced Editor da kod ko‘rinadi. Hozircha GUI yetarli. Lekin biling: “Source” va “Navigation” — M. Qo‘lda o‘chirsangiz, query o‘ladi. Qo‘rquv shart emas; tushunish uchun bir marta ochib ko‘ring, yoping.</p>

<p>Tugagach: <strong>Close &amp; Apply</strong> — o‘zgarishlar modelga yuklanadi, Report view ga qaytasiz. Shunchaki Close — ba’zan saqlanmagan qadamlarni tashlaydi. Farqni aralashtirmang. Apply uzoq tursa, qator ko‘p yoki folding yo‘q — bekor qilib, filtrni erta qo‘ying.</p>

<p>Preview faqat namuna (ko‘pincha 1000 qator atrofida). “Preview da null yo‘q” — butun jadvalda yo‘q degani emas. Column quality / profile ni View dan yoqib ko‘ring (katta faylda sekin bo‘lishi mumkin). Refresh da to‘liq ma’lumot yuradi.</p>

<p>Keng tarqalgan xato: DAX bilan tozalash. “Null ni measure da yashiraman.” Yo‘q. Kir ma’lumot — Query da. DAX hisob uchun. Ikkinchi xato: oraliqqa Insert step qilib, keyingi qadamlarni sindirish. Avval oxiriga qo‘shing, tushunsangiz keyin joyini o‘zgartirasiz. Bugun: Transform data oching, 2–3 qadam qiling, nomini yozing, Close &amp; Apply. Retsept paydo bo‘ldi.</p>
""",
    "pbi-pq-clean": """
<p>Power Query da o‘nlab tugma bor. Ishda 8–10 tasi 90 foizni yopadi. Maqsad: “tozalangan jadval” — har ustunning tipi to‘g‘ri, keraksiz yo‘q, kalit takrorlanmasa dimension da unique, fact da har qator — bitta hodisa (chek qatori, kunlik savdo).</p>

<p><strong>Choose columns / Remove columns.</strong> Izoh, ichki kod, bo‘sh ustun. Modelga kirmasin. <strong>Filter rows:</strong> test qatorlari (“TEST”, summa = 0 va izoh “o‘chirish”), bo‘sh sana, manfiy narx — biznesdan so‘rang: qaytarish manfiymi yoki xato? <strong>Replace values / Replace errors:</strong> “n/a” ni null qilish, xato tipni tuzatish.</p>

<p><strong>Split column.</strong> “Toshkent, Chilonzor” — vergul bo‘yicha shahar va tuman. <strong>Change type</strong> — erta qiling. Summa Text bo‘lsa, Card dagi Sum ishlamaydi yoki chalkashadi. Decimal vs Whole: so‘m tiyin bilan — Decimal. Sana — Date, DateTime emas, agar soat kerak bo‘lmasa. Locale: <code>1 250,50</code> ni o‘qiy olmasligi mumkin.</p>

<p><strong>Remove duplicates</strong> — dimension kaliti bo‘yicha. Fact da o‘ylamasdan Remove duplicates qilsangiz, ikki chek bir xil summada yo‘qolishi mumkin. Fact da dublikat bo‘lsa, avval nima ekanini tushuning. <strong>Fill down</strong> — merged Excel qoldig‘i. <strong>Unpivot:</strong> Yanvar, Fevral, Mart ustunlari — bu tahlil uchun noqulay. Unpivot qilsangiz: Oy | Summa qatorlari. Star schema va DAX shunda yashaydi. “Keng” Excel hisoboti ko‘pincha unpivot kutadi.</p>

<p>Tipni qo‘ygach Preview da error. Qizil katak — o‘sha qator. Yashirish (error ni replace) ba’zan yashirin yo‘qotish. Yaxshisi: filtrlab ko‘ring, manbani tuzating. Column profile: null foizi. 40% null shahar — slicer “bo‘sh” to‘la bo‘ladi; to‘ldirasizmi, “Noma’lum” qilasizmi — biznes savoli.</p>

<p>Tartib. Avval keraksiz qator/ustun, keyin tip, keyin split va hisob. Aksincha qilsangiz, o‘chiriladigan ustunga vaqt ketadi. Har qadamga nom.</p>

<p>CFO dashboardida “Jami savdo” Card bo‘sh yoki xato — birinchi gumon: Amount hali Text. Transform data → Change type → Decimal, locale. Keyin Close &amp; Apply. DAX ni ayblashdan oldin tipni tekshiring. Bu darsning amaliy yadrosi shu.</p>
""",
    "pbi-pq-merge": """
<p>Ikki xil “birlashtirish” bor. Odamlar aralashtiradi, keyin yig‘indi ikki barobar. Excelda ham shunday: ostiga yopishtirish vs VLOOKUP. Power Query da: <strong>Append</strong> va <strong>Merge</strong>.</p>

<p><strong>Append</strong> — vertikal. Yanvar savdosi va Fevral savdosi, ustunlari bir xil. Natija — uzunroq fact. Home → Append queries. Ustun nomlari mos kelishi kerak: birida <code>Summa</code>, ikkinchisida <code>Amount</code> bo‘lsa, ikkita ustun, yarmi null. Avval nomni bir xillashtiring. Yil ustunini qo‘shib qo‘ying, aks holda 2023 va 2024 aralashib ketadi.</p>

<p><strong>Merge</strong> — gorizontal, JOIN. FactSavdo da <code>filial_id</code>, DimFilial da ham. Merge, kalitni belgilaysiz, Join kind tanlaysiz. <strong>Left outer</strong> — chapdagi barcha savdo qatorlari, o‘ngdan nom topilsa yoziladi, topilmasa null. Odatda fact chapda. <strong>Inner</strong> — faqat mos kelganlar. Filiali yo‘q savdo yo‘qoladi — ba’zan kerak, ko‘pincha yo‘q. CFO “barcha savdo” desa, Inner xavfli. Full outer — kamdan-kam, tahlilda chalkashtiradi.</p>

<p>Merge dan keyin yangi ustun “Table” ko‘rinadi. Expand — kerakli maydonlar: filial nomi, shahar. Hammasini ochmang. Keyin kalitni fact da qoldirasiz (model uchun) yoki o‘ylangan holda olib tashlaysiz.</p>

<p>Tuzoq: <strong>fan-out</strong>. DimFilial da <code>filial_id</code> takrorlangan (ikki marta “Chilonzor”). Left merge qilsangiz, har savdo qatori ikkiga ko‘payadi. Jami savdo shishadi. Rahbar baxtli, raqam yolg‘on. Merge oldidan dimension da Remove duplicates (kalit bo‘yicha) yoki nima uchun dublikat ekanini tuzating. Fact ni dimension ga “yopishtirish” har doim shart emas.</p>

<p>Modelda relationship vs Query da Merge. Ko‘pincha yaxshisi: jadvallarni alohida qoldirish, Model view da bog‘lash — star schema. Merge ni qachon? Manba umuman alohida keladi va bitta jadval qilish shart (masalan, kurs jadvali faqat Query da). Har narsani bitta yassi Excelga yig‘ish — eski odat, katta modelda og‘ir.</p>

<p>Qisqa: bir xil ustun, uzunroq jadval — Append. Yoniga ustun, kalit — Merge, odatda Left, dublikatni tekshir. Keyingi modulda shu jadvallarni modelda “yulduz” qilib qo‘yamiz.</p>
""",
    "pbi-rel": """
<p>Jadvallar Fields da yonma-yon turibdi. Lekin Power BI ularni tanimaydi. Slicer da “Toshkent” ni bossangiz, savdo o‘zgarmaydi. Sabab: <strong>relationship</strong> yo‘q. Exceldagi VLOOKUP o‘rniga bu yerda chiziq: qaysi ustun bir xil narsani bildiradi.</p>

<p>Model view. <code>DimFilial[filial_id]</code> ni <code>FactSavdo[filial_id]</code> ga tortasiz. Oyna: cardinality, filter direction. <strong>1:* (one-to-many)</strong> — odatiy. Bir filial — ko‘p savdo qatori. Bir tomonda unique kalit (dimension), ko‘p tomonda takror (fact). Agar ikkala tomonda takror bo‘lsa, Power BI many-to-many taklif qiladi. Boshlang‘ichda qoching: odatda dimension tozalanmagan.</p>

<p>Kalit tipi bir xil bo‘lsin. Biri Whole number, ikkinchisi Text — bog‘lanmaydi yoki yomon ishlaydi. “001” va 1 — turli narsa. Power Query da ikkalasini ham Whole yoki ikkalasini ham Text qiling, ongli ravishda.</p>

<p><strong>Cross-filter direction.</strong> Single — filtr odatda dimension dan fact ga: shaharni tanladingiz, savdo kesiladi. Bu tavsiya. Both — ikki tomonlama. Ba’zan “mahsulotdan mijozga ham yuray” deyishadi. Lekin modelda ikkita yo‘l bo‘lsa, Power BI “ambiguous path” deydi, filtrlar g‘alati. Both ni “hamma joyda yoqib qo‘yish” — sekinlik va chalkashlik. Kerak bo‘lsa, bitta joyda, tushunib.</p>

<p>Active vs inactive. Ikki xil sana: savdo sanasi va yetkazib berish sanasi. Ikkinchi chiziqni inactive qilib, DAX da USERELATIONSHIP bilan ochasiz. Hozircha bitta sana kaliti yetarli. Ikkalasini ham active qilsangiz — yana noaniq yo‘l.</p>

<p>Yomon belgi: Power BI o‘zi avtomatik relationship yasaydi, ism o‘xshash deb. <code>id</code> ni <code>id</code> ga ulab, umuman boshqa narsani bog‘lashi mumkin. Avtomatikni o‘chirib, o‘zingiz torting. “Assume referential integrity” DirectQuery da tezroq, lekin yetim qatorlar yo‘qolishi mumkin — ehtiyot.</p>

<p>Tekshiruv: Report da filial slicer, yonida Jami savdo. Toshkent — boshqa son, Samarqand — boshqa. O‘zgarmasa, chiziq yo‘q yoki noto‘g‘ri ustun. Data view da fact dagi filial_id lar dim da bormi? Yo‘q bo‘lsa, Left qolganda ham “bo‘sh filial” chiqadi — manba teshigi. Avval kalit sifati, keyin chiroyli DAX.</p>
""",
    "pbi-star": """
<p>Modelni chizmoqchi bo‘lsangiz, yulduzni eslang. O‘rtada fact — hodisalar. Atrofida dimension — “kim, nima, qayerda, qachon.” Microsoft ham shuni tavsiya qiladi, lekin nom muhim emas: muhimi, savdo qatorida mijozning to‘liq manzili, mahsulotning uzoq tavsifi takrorlanmasin.</p>

<p>Kichik misol. Savdo tarmog‘i, so‘m.</p>
<table>
  <tr><th colspan="4">FactSavdo (o‘rtada)</th></tr>
  <tr><th>sana</th><th>filial_id</th><th>mahsulot_id</th><th>summa</th></tr>
  <tr><td>2024-03-01</td><td>1</td><td>10</td><td>150000</td></tr>
  <tr><td>2024-03-01</td><td>2</td><td>10</td><td>80000</td></tr>
  <tr><td>2024-03-02</td><td>1</td><td>11</td><td>210000</td></tr>
</table>
<table>
  <tr><th colspan="3">DimFilial</th></tr>
  <tr><th>filial_id</th><th>nom</th><th>shahar</th></tr>
  <tr><td>1</td><td>Chilonzor</td><td>Toshkent</td></tr>
  <tr><td>2</td><td>Registon</td><td>Samarqand</td></tr>
</table>
<table>
  <tr><th colspan="3">DimMahsulot</th></tr>
  <tr><th>mahsulot_id</th><th>nom</th><th>kategoriya</th></tr>
  <tr><td>10</td><td>Sut 1L</td><td>Oziq-ovqat</td></tr>
  <tr><td>11</td><td>Non</td><td>Oziq-ovqat</td></tr>
</table>
<p>Fact — ko‘p qator, kam matn: kalitlar va o‘lchov (summa, soni). Dimension — kamroq qator, boy matn: shahar, kategoriya. Slicer va sarlavha shu matndan. Yig‘indi fact dagi songa tushadi.</p>

<p>Nima uchun yassi Excel yomon? Har qatorda “Chilonzor, Toshkent, Yunusobod tumani…” takror. Fayl shishadi, “Toshkent” ni bir joyda “Toshkent ”, boshqasida “toshkent” yozilsa, filtr ikkiga bo‘linadi. Dimension da shahar bitta qatorda — tuzatasiz, hammasi tuzaladi.</p>

<p>Sana alohida dimension bo‘lsin: yil, oy, hafta, ish kuni. DAX da “o‘tgan oy” shunda oson. Fact da faqat sana kaliti (yoki Date ustuni, lekin oy nomi fact da takrorlanmasin). Snowflake: mahsulot → kategoriya alohida jadval. Ishlaydi, lekin boshlang‘ichda kategoriyani DimMahsulot ichiga qo‘ying — oddiy yulduz. Kerak bo‘lsa keyin ajratasiz.</p>

<p>Markazda nima turadi? Fact. Mijoz muhim, lekin mijoz — qanot. Savdo hodisasi — markaz. Bir nechta fact bo‘lishi mumkin (savdo va qaytarish) — ikkita yulduz, umumiy DimSana, DimFilial. Hamma narsani bitta Fact ga tiqmang, agar hodisa boshqacha bo‘lsa.</p>

<p>CFO dashboardi: Toshkent vs viloyat. DimFilial[shahar] yoki mintaqa ustuni. Fact ga “mintaqa” ni yozib qo‘yish shart emas — bog‘lanish filtrni olib keladi. Chizing: o‘rtada FactSavdo, atrofida 2–3 ta Dim. Keyin Desktop da shu chiziqlarni torting. Model toza bo‘lsa, DAX qisqa bo‘ladi. Model iflos bo‘lsa, CALCULATE ham yordam bermaydi.</p>
""",
    "pbi-keys": """
<p>Model ishlaydi. Lekin Fields ro‘yxati chalkash: <code>filial_id</code>, <code>mahsulot_id</code>, <code>SortOy</code>, <code>Helper</code>… Menejer slicer qidiradi, kalitni topib, “nima bu?” deydi. Hisobot foydalanuvchi uchun. Yordamchi ustunlar yashiriladi.</p>

<p>Ustun yoki jadvalni o‘ng tugma → <strong>Hide in report view</strong>. Modelda relationship uchun <code>filial_id</code> kerak — yashirsangiz ham chiziq qoladi. Fields da ko‘rinmaydi. Measure larni yashirmang, ular asosiy. Fact dagi xom <code>summa</code> ni ham yashirib, faqat <code>Jami savdo</code> measure qoldirish — yaxshi odat: odam Sum ni ikki marta qo‘ymaydi.</p>

<p><strong>Sort by column.</strong> Oy nomlari: Apr, Aug, Dec, Feb… alifbo. Biznes Yanvar→Dekabr xohlaydi. DimSana da <code>OyNomi</code> va <code>OyRaqami</code> (1–12). OyNomi ni tanlab, Column tools → Sort by column → OyRaqami. Hafta kunlari ham: Dushanba birinchi, alifbo emas. Raqamsiz sort ishlamaydi — avval sonli yordamchi ustun (Query da yoki calculated column).</p>

<p><strong>Display folders.</strong> Measure ko‘paysa: “KPI”, “O‘tgan yil”, “Foiz”. Model view da measure ni tanlab, Display folder yozasiz. Fields da papka ochiladi. Jamoa minnatdor.</p>

<p>Data category: shahar, mamlakat. Column tools → Data category → City / Country. Xarita vizuali “Toshkent” ni shahar deb tushunadi. Noto‘g‘ri kategoriya — xarita bo‘sh yoki noto‘g‘ri nuqta. Ierarxiya: Mahsulot → Kategoriya (yoki teskari, mantiqiy tartibda). Drill-down shunda ishlaydi.</p>

<p>Nomlash. Inglizcha Fact/Dim prefiksi ishda keng tarqalgan; o‘zbekcha ham bo‘ladi, lekin aralashtirmang. <code>Jami savdo</code> — tushunarli. <code>M1</code>, <code>calc2</code> — bir hafta keyin unutasiz. Bo‘sh joy measure nomida ruxsat, lekin DAX da <code>'Jami savdo'</code> yoki <code>[Jami savdo]</code>.</p>

<p>Xato: kalitni yashirmasdan slicer qilish — foydalanuvchi ID tanlaydi, nom emas. Xato: oy ni sort qilmasdan chiziqli grafik — “trend” siniq ko‘rinadi. Xato: 40 ta measure ni ildizda qoldirish. 15 daqiqa yashirish va sort — hisobot “professional” bo‘lib qoladi, DAX o‘zgarmasa ham.</p>
""",
    "pbi-dax-col-meas": """
<p>Excelda formula hamma katakka yozilardi, pastida Sum. Power BI da ikki xil hisob: <strong>calculated column</strong> va <strong>measure</strong>. Shu farqni tushunmasangiz, model shishadi yoki Card noto‘g‘ri son beradi. Sokin tushuntiraman.</p>

<p><strong>Column</strong> — qator darajasi. Har savdo qatori uchun bitta qiymat, modelda saqlanadi (xotira). Misol: to‘liq nom, “Katta chek” ha/yo‘q, segment. Slicer, o‘q, kategoriya sifatida kerak bo‘lsa — column (yoki undan ham yaxshisi: Power Query da yoki dimension atributi). U qator bilan “yopishib” turadi.</p>

<p><strong>Measure</strong> — yig‘indi, o‘rtacha, foiz, “nechta”. U saqlanmaydi har qatorga; vizual so‘raganda, o‘sha filtr bilan hisoblanadi. Toshkent slicer — Toshkent yig‘indisi. Butun tarmoq — butun yig‘indi. Bitta formula, ko‘p javob. KPI lar — measure.</p>

<p>Qachon column? “Premium / Standard” ni slicer qilmoqchisiz — bu yorliq, qatorga tegishli. Qachon measure? “Jami savdo”, “Cheklar soni”, “O‘rtacha chek”. Xotira: og‘ir ifodani million qatorga column qilmang. SUMX ni har qatorga yozib saqlash — sekin model.</p>

<p>Yozish. Modeling → New measure, yoki Fields da o‘ng tugma. Formula satri:</p>
<pre>Jami savdo = SUM(FactSavdo[summa])
Cheklar soni = COUNTROWS(FactSavdo)
Ortacha chek = DIVIDE([Jami savdo], [Cheklar soni])</pre>
<p><code>DIVIDE</code> — nolga bo‘lishda xato bermaslik. Exceldagi <code>/</code> ba’zi filtrda infinity. Ustunni measure o‘rnida Card ga tashlasangiz, Power BI ba’zan Sum ni o‘zi qo‘yadi — ishlaydi, lekin yashirin. Aniq measure yozing, formatini (so‘m, butun son) belgilang.</p>

<p>Column misoli (row context — “shu qator”):</p>
<pre>TolovTuri = IF(FactSavdo[summa] &gt;= 200000, "Katta", "Oddiy")</pre>
<p>Buni slicer qilish mumkin. <code>Jami savdo</code> ni column qilish esa mantiqsiz: har qatorda “jami” degan narsa yo‘q.</p>

<p>Xatolar. Measure ni “calculated column” deb New column ga yozish. Column ni VALUES ga tashlab, yig‘indi kutish. Ikkalasini ham “formula” deb atash — jamoa tushunmaydi. Qoida: filtrlanadigan yorliq — column/atribut; filtrga qarab o‘zgaradigan son — measure. Keyingi darsda SUM, COUNT, DIVIDE ni sekinroq. Undan keyin CALCULATE — DAX ning yuragi.</p>
""",
    "pbi-dax-basic": """
<p>Measure yozishni boshlaymiz. Avval to‘rtta tushuncha, Exceldagi Sum, Count, Average ga yaqin. Farqi: ular filtr kontekstida ishlaydi. Slicer, ustun, satr — hammasi “qaysi qatorlar kiradi” ni aytadi. Siz faqat “shu qatorlarda nima qilay” ni yozasiz.</p>

<p><code>SUM</code> — son ustunini qo‘shadi. <code>COUNTROWS</code> — jadvalda nechta qator (chek qatori). <code>COUNT</code> bitta ustunni sanaydi, NULL ni tashlashi mumkin; “nechta savdo yozuvi” uchun COUNTROWS aniqroq. <code>DISTINCTCOUNT</code> — nechta <em>xil</em> qiymat. 10 000 qator savdo, 800 mijoz takrorlangan. “Nechta chek?” — COUNTROWS. “Nechta mijoz xarid qilgan?” — DISTINCTCOUNT(FactSavdo[mijoz_id]). SUM(mijoz_id) — bema’ni, ID larni qo‘shish.</p>

<pre>Jami savdo = SUM(FactSavdo[summa])
Cheklar soni = COUNTROWS(FactSavdo)
Unikal mijoz = DISTINCTCOUNT(FactSavdo[mijoz_id])
Ortacha chek = DIVIDE([Jami savdo], [Cheklar soni], 0)
Ortacha qator = AVERAGE(FactSavdo[summa])</pre>
<p><code>AVERAGE</code> — qatorlardagi summaning o‘rtasi. <code>Ortacha chek</code> esa jami / chek soni. Ba’zan bir xil, ba’zan yo‘q (bo‘sh, filtr). CFO “o‘rtacha chek” desa, odatda ikkinchisi. Aniqlashtiring.</p>

<p><code>DIVIDE(a, b, 0)</code> — b nol yoki bo‘sh bo‘lsa, uchinchi argument (0 yoki BLANK). <code>a/b</code> yozsangiz, ba’zi vizualda xato. Foiz ham DIVIDE: Toshkent / jami.</p>

<p>Iterator: SUMX, AVERAGEX — har qator uchun ifoda, keyin yig‘indi. Masalan, <code>soni * narx</code> alohida ustun bo‘lmasa. Hozircha fact da <code>summa</code> bo‘lsa, SUM yetarli. SUMX ni “professionalroq” deb har joyga yozmang — sekinroq bo‘lishi mumkin.</p>

<p>Format. Measure ni tanlab, so‘m, ming ajratgich, foiz, kasr. Hisobotda bir measure Card da 150000, boshqasida 150 000,00 — ishonchsiz. BLANK va 0: ba’zi filtrda savdo yo‘q — 0 ko‘rsatishmi, bo‘shmi? Rahbariyat odatda 0 ni tushunadi; BLANK ba’zan chiziqni uzadi.</p>

<p>Yozish odatlari. Avval Jami savdo, keyin boshqalar uni <code>[Jami savdo]</code> deb chaqiradi. Qayta SUM yozmang. Nom o‘zbekcha, tushunarli. Mashq: uchta measure — SUM, COUNTROWS yoki DISTINCTCOUNT, DIVIDE. Card ga tashlang, slicer bilan o‘ynang. Son o‘zgarsa — filtr ishlayapti. O‘zgarmasa — relationship yoki noto‘g‘ri jadval.</p>
""",
    "pbi-dax-calculate": """
<p>Endi kursning eng muhim DAX darsi. <code>CALCULATE</code>. Qo‘rqitadigan nom. Odmi tilda: “Shu o‘lchovni hisobla, <em>lekin</em> filtrni men aytgandek qil.” Exceldagi SUMIF ga yaqin, lekin kuchliroq. SUMIF bitta shart. CALCULATE esa slicer, jadval, yil — mavjud kontekstni o‘zgartiradi: qo‘shadi, almashtiradi, ba’zan olib tashlaydi.</p>

<p>Vizualda allaqachon filtr bor. Ustun chart da har ustun — o‘z kategoriyasi. Slicer — foydalanuvchi tanlovi. Buni <strong>filter context</strong> deyishadi: “hozir qaysi qatorlar ko‘rinadi.” Oddiy <code>[Jami savdo]</code> shu kontekstda yig‘adi. Ba’zan esa kontekstni buzib, boshqacha so‘raymiz: “Jami savdo, lekin faqat Toshkent — slicer nima desayam.” Yoki: “Shu mahsulotning jami ichidagi ulushi.”</p>

<pre>Savdo Toshkent =
CALCULATE(
    [Jami savdo],
    DimFilial[shahar] = "Toshkent"
)

Savdo 2024 =
CALCULATE(
    [Jami savdo],
    DimSana[Yil] = 2024
)</pre>
<p>O‘qish: “Jami savdoni ol, shahar Toshkent bo‘lsin.” Card da slicer bo‘lmasa ham Toshkent qotadi. Slicer da Samarqand tursa ham, bu measure Toshkentni ko‘rsatadi — chunki siz qat’iy aytdingiz. Ba’zan shu kerak (KPI “doim Toshkent”), ba’zan yo‘q (unda oddiy Jami savdo + slicer).</p>

<p>Foiz — klassika. “Bu filialning tarmoqdagi ulushi.” Payg‘ambarlik yo‘q: avval shu filtr dagi savdo, keyin filtrni kengaytirib butun savdo, keyin bo‘lish.</p>
<pre>Ulush tarmoqda =
DIVIDE(
    [Jami savdo],
    CALCULATE([Jami savdo], ALL(DimFilial))
)</pre>
<p><code>ALL(DimFilial)</code> — filial/shahar filtrini olib tashla, qolgan filtrlar (sana, mahsulot) tursin. Natija: Toshkent tanlanganda ham maxraj — butun tarmoq (shu sanada). <code>REMOVEFILTERS</code> ham o‘xshash g‘oya, yangiroq yozuv. Hozir ALL ni tushuning: “shu jadvalning filtrini unut.”</p>

<p>CALCULATE filtrni qanday “yutadi”? Qisqa: bir xil ustunga yangi shart — odatda eski shartning o‘rnini bosadi. Boshqa ustun — qo‘shiladi. Chuqur qoidalar bor; boshlang‘ichda shuni biling va Measure da sinab ko‘ring. FILTER funksiyasi — jadval ifodasi, murakkabroq shart. Ko‘pincha <code>DimFilial[shahar] = "Toshkent"</code> yetarli.</p>

<p>Xatolar. CALCULATE ni column da yozib, “har qator uchun Toshkent” deb o‘ylash — kontekst boshqacha, bosh og‘riydi. Measure ni Fields dan tashlamasdan, column ni Sum qilish. ALL ni butun modelga qo‘llab, maxrajni umuman boshqa qilish. Avval kichik Card: Toshkent measure vs slicer. Sonni qo‘lda Excelda tekshiring. Mos kelsa — tushundingiz. DAX yodlanmaydi, savol bilan yoziladi: “Qanday filtr kerak? Qaysini olib tashlash kerak?” CALCULATE shu savolning javobi.</p>
""",
    "pbi-vis-types": """
<p>Model tayyor, measure bor. Endi odam ko‘radigan narsa. Xato: “qaysi grafik chiroyli?” To‘g‘ri savol: “qanday savolga javob?” CFO birinchi ekranda bitta son xohlaydi. Menejer — Toshkent vs viloyat. Tahlilchi — oylar. Har savol — o‘z vizuali.</p>

<p><strong>Card</strong> (yoki KPI) — bitta son: bugungi savdo, so‘m. Katta, toza. Birinchi sahifa shu bilan boshlanadi. <strong>Line</strong> — vaqt: oylar, kunlar. Trend, tushish. Sana o‘qida bo‘lsin, kategoriya matnida emas. <strong>Bar / Column</strong> — filiallar, kategoriyalar taqqoslash. Odamiy ko‘z uzunlikni yaxshi solishtiradi. Gorizontal bar — uzun nomlar (filial) uchun qulay.</p>

<p><strong>Table / Matrix</strong> — detal. Matrix — Excel pivot: satrda kategoriya, ustunda oy, qiymatda savdo. Drill. Pie / donut — 2–4 bo‘lak, aniq ulush. 15 ta kategoriya pie da — hech kim o‘qimaydi, yaqin foizlar ajralmaydi. Stakeholder “tushunmadim” desa, bar yoki top N + “Boshqalar”. Scatter — ikki o‘lchov (savdo vs marja), boshlang‘ich dashboardda shart emas. Xarita — toza shahar/mamlakat, kategoriya to‘g‘ri.</p>

<p>Field wells. Measure — odatda Values. O‘q / Axis — sana yoki kategoriya (ustun, slicer emas). Legend — bo‘lish: Toshkent/viloyat. Noto‘g‘ri: measure ni Axis ga, shahar ni Values ga (Count of shahar). Grafik “ishlaydi”, savolga javob bermaydi.</p>

<p>Ko‘p vizual — kognitiv yuk. Bitta sahifada 3–6 ta yetarli: 3 card, 1 trend, 1 taqqoslash, ixtiyoriy jadval. 25 ta kichik chart — bezak, tahlil emas.</p>

<p>CFO savdo dashboardi: yuqorida Jami savdo, Cheklar, Ortacha chek. O‘rtada oylik chiziq. Yonida filiallar bar (Toshkent tepada yoki sort). Pastda mahsulot matrix. Pie yo‘q. Ranglar keyingi dars. Bugun: savolni yozing, vizualni tanlang, tashlang, slicer bilan tekshiring. “Chiroyli” keyin.</p>
""",
    "pbi-vis-format": """
<p>To‘g‘ri vizual tanlandi. Lekin hali hisobot emas: “Chart1”, o‘q 80 000 dan boshlanadi, raqamlar o‘qilmaydi, tooltip bo‘sh. Format — bezak emas, o‘qilishi. Vizualni bosing, Format (bo‘yash rulosiga o‘xshash ikonka) va Visualizations quduqlari.</p>

<p>Sarlavha. Avtomatik “Sum of summa” — tashlang. “2024 oylik savdo, so‘m” yoki “Filiallar: jami savdo”. Savol ko‘rinsin. Data labels — 4–6 ustunda foydali; 24 oylik chiziqda har nuqtada son — chigallik. Kerakli joyda yoqing.</p>

<p>O‘q. Ustun/bar da Y o‘qni 0 dan boshlang. 80 000–85 000 oralig‘ini “katta farq” qilib ko‘rsatish — aldov. Chiziqda ba’zan boshqacha, lekin rahbariyat oldida 0 halolroq. Ming, million: display units (thousands) — yozib qo‘ying “ming so‘m”, aks holda 150 ni 150 so‘m deb o‘qiydi.</p>

<p>Tooltip. Standart — o‘sha son. Qo‘shimcha: marja %, cheklar soni. Foydalanuvchi ustiga olib boradi, sahifa to‘lmaydi. Small multiples — kichik panellar (har viloyat). 12 ta bo‘lsa, o‘qiladi; 40 ta — yo‘q.</p>

<p>Rang. Hali theme darsiga qoladi, lekin bitta ogohlantirish: qizil-yashil faqat “yomon-yaxshi” bo‘lsa, va rang ko‘rish muammosini unutmang. Yozuv yoki ikonka qo‘shing. Kontrast: och kul rangda och kul grafik — proyektorda yo‘qoladi.</p>

<p>Xatolar. Har katakni boshqa shrift. Legend ni yashirib, rangga ma’no yuklash. O‘qni teskariga aylantirish. Conditional formatting ni matrix da ehtiyot: foydali (yuqori savdo to‘qroq), lekin 5 xil qoida — archa. Avval bir vizualni “tugallangan” qiling: sarlavha, 0 o‘q, formatlangan so‘m, tushunarli tooltip. Keyin nusxa uslubini boshqasiga. Tez va bir xil.</p>
""",
    "pbi-vis-custom": """
<p>Internetda “chiroyli” vizuallar bor: AppSource, noma’lum saytlar. Qo‘l qichiydi. Bank, moliya, yirik tarmoqda esa bu xavf. Built-in (Microsoft dagi oddiy card, bar, line, matrix) yetarli bo‘lsa — shu. Custom — aniq teshik: masalan, maxsus Gantt, IT ruxsati bilan.</p>

<p>Xavflar, ochiq. Noma’lum muallif kodi hisobotda yuradi — ma’lumot sizniki. Certified visual — tekshiruvdan o‘tgan, afzal, lekin baribir kerakmi, deb so‘rang. Performance: ba’zi custom og‘ir, sahifa sekin. Service, Mobile, export da ishlamasligi mumkin. Ertaga muallif yangilamaydi — hisobot sindi.</p>

<p>Qachon o‘ylab ko‘rish mumkin? Built-in bilan savolga javob yo‘q, xavfsizlik jamoasi certified ro‘yxatni tasdiqlagan, kichik testda tezlik maqbul. Qachon yo‘q: “dashboard zamonaviy ko‘rinsin”, banking, shaxsiy ma’lumot, 10 daqiqada GitHub dan .pbiviz.</p>

<p>O‘rnatish: Visualizations pastida ellipsis → Get more visuals. Faqat keragini. Har vizual — qo‘shimcha yuk. 100 ta custom — kinoya emas, ba’zi fayllarda uchraydi, ochilishi 20 soniya.</p>

<p>Alternativ. “Chiroyli” ni theme, toza layout, yaxshi sarlavha beradi. KPI ni custom gauge o‘rniga Card + rang. Timeline o‘rniga slicer va line. Ko‘p “wow” vizual tahlilni yomonlashtiradi.</p>

<p>CFO oldida: ishonchli son, 3 soniyada ochiladigan sahifa, tushunarli filtr. Uchburchakli 3D pie — taqdimotda kulgi, qarorda yo‘q. Qoida: avval built-in. Custom — ehtiyoj + ruxsat. RLS custom ni “xavfsiz” qilmaydi. Shu dars qisqa, chunki yaxshi maslahat ham qisqa: o‘rnatmasdan oldin ikki marta o‘ylang.</p>
""",
    "pbi-pages": """
<p>Bitta sahifaga hamma narsani tiqish — Exceldagi “bitta varaqda 15 ta grafik.” Menejer yo‘qoladi. Qoida: <strong>bir sahifa — bir hikoya</strong>. Birinchi: tarmoq holati. Ikkinchi: Toshkent vs viloyat. Uchinchi: mahsulot detali. Har biri o‘z savoli.</p>

<p>Yaxshi tartib, yuqoridan pastga. Ko‘z chap-yuqoridan boshlaydi. Shu yerda 3–5 ta Card: jami savdo, o‘sish, cheklar, o‘rtacha chek. O‘rtada asosiy grafik: oylik trend yoki filial taqqoslash — sahifaning “qahramoni.” Past yoki o‘ng: detal jadval, yoki slicer lar. Oq joy qoldiring. Hamma narsani chetiga yopishtirish — charchatadi. Alignment: chiziqqa tekislang, o‘lchamlar bir xil card lar.</p>

<p>Sahifa nomi. “Page 1”, “Chart1” — yomon. “01 Umumiy”, “02 Filiallar”, “03 Mahsulot” — tartib va ma’no. Foydalanuvchi pastki yorliqlarni o‘qiydi. Ko‘p sahifa bo‘lsa, keyinroq tugma bilan navigatsiya.</p>

<p>Zichlik. Proyektor — katta shrift, kam vizual. Noutbuk — biroz zichroq. Ikkalasiga bir xil 25 vizual sig‘maydi. Mobile alohida layout (bookmark darsida). Desktop ni siqib telefonga tiqmang.</p>

<p>Hikoya ketma-ketligi. Umumiy son → qayerda o‘sgan/tushgan → nima sabab (kategoriya). Detalni birinchi sahifaga ko‘chirmang. Drillthrough keyinroq: umumiy ustunni bosib, detal sahifaga o‘tish.</p>

<p>Xato: slicersiz 20 ta filtr faqat Filter pane da — foydalanuvchi topmaydi. Xato: har sahifada boshqacha o‘lchamdagi card. Xato: bir xil measure ni 8 marta turli grafikda. Ikki sahifa chizing: Overview va Details. Overview da 4 card + 1 line + 1 bar, nomlari o‘zbekcha. To‘lsa, yangi sahifa oching, yana tiqmang. Dizayn — tahlilning bir qismi, “keyin bezayman” emas.</p>
""",
    "pbi-theme": """
<p>CFO dashboardida har grafik boshqa ko‘k, boshqa shrift — ishonchsiz ko‘rinadi, garchi raqam to‘g‘ri bo‘lsa ham. Brend: masalan, to‘q ko‘k va oq. Har vizualni qo‘lda bo‘yash — charchoq va ertaga yangi chart yana “default sariq.” Yechim: <strong>theme</strong>.</p>

<p>View → Themes. Tayyor to‘plam yoki import JSON. JSON da rang palitrasi, shrift, default vizual stillari. Bir marta sozlasangiz, yangi vizual ham shu rangdan oladi. Kompaniya dizayneri bo‘lsa, ulardan kod so‘rang; bo‘lmasa, 4–6 ta rang: asosiy ko‘k, kul, bitta aksent (masalan, yashil o‘sish uchun), ehtiyot qizil.</p>

<p>Nima theme qilmaydi? Yomon modelni, noto‘g‘ri pie ni, 25 vizualni. U faqat bir xillik. Avval tuzilma, keyin theme.</p>

<p>Zichlik: compact vs comfortable. Ko‘p jadval — compact. Rahbariyat taqdimoti — kengroq. Proyektor: kontrast yuqori, och kul fonda och chiziq yo‘q.</p>

<p>Logo. Insert → Image, yuqori chap. Katta qilib sahifani yemang. Sarlavha matni theme shrifti bilan. Qorong‘u fon — moda, lekin chop etish va ba’zi xonalar yomon. Ko‘p ofislar ochiq fonda qoladi.</p>

<p>Xato: har sahifada boshqa theme. Xato: 12 ta yorqin rang, “hamma kategoriya boshqacha.” 6 dan oshsa, ko‘z charchaydi; qolganini “Boshqalar” yoki ketma-ket bir palitra. Xato: qizilni Toshkent, yashilni Samarqand qilish — ma’no yo‘q, qizil “xavf” deb o‘qiladi. Mintaqani ketma-ket ko‘k-kul qiling. Bir marta theme qo‘llang, 2–3 vizualni tekshiring: card, bar, line. Bir xil ko‘k — brend. Shu yetarli.</p>
""",
    "pbi-bookmark": """
<p>Foydalanuvchi slicer ni “buzib” qo‘ydi: 2019-yil, bitta mahsulot, yashirin filtr. “Qanday qaytaman?” deydi. Siz emailda “Clear filters” o‘rgatasiz — u unutadi. Yechim: <strong>bookmark</strong> + tugma. Bookmark — sahifaning surat: qaysi filtr, qaysi vizual ko‘rinadi, ba’zan qaysi holat.</p>

<p>View → Bookmarks. Avval sahifani “boshlang‘ich” holatga keltiring (slicer tozalangan, kerakli vizuallar ochiq). Add. Nom: “Reset” yoki “Umumiy holat.” Data va Display belgilari: filtrni saqlash, obyekt ko‘rinishini saqlash. Noto‘g‘ri belgi — “reset” filtrni tashlamaydi yoki vizualni yashiradi. Sinab ko‘ring.</p>

<p>Insert → Buttons. Tugma matni: “Filtrlarni tozalash.” Action → Bookmark → Reset. Tooltip: “Boshlang‘ich holat.” Foydalanuvchi tushunsin. Sahifalar orasida: Page navigation tugmasi — “Filiallar”, “Orqaga.” Bu hisobotni “ilova” qiladi, yorliq qidirishdan ko‘ra oson.</p>

<p><strong>Drillthrough.</strong> Umumiy bar da “Oziq-ovqat” ni o‘ng tugma → Drill through → detal sahifa. Detal sahifada Drillthrough filtri (kategoriya maydoni). Kontekst o‘tadi: faqat o‘sha kategoriya. Sahifa nomini “Mahsulot detali” qiling, “orqaga” tugmasi qo‘ying. Bu bookmark emas, lekin navigatsiya oilasidan.</p>

<p>Selection pane. Vizualni yashirish/ko‘rsatish bookmark bilan: “KPI rejim” vs “Jadval rejim.” Ortiqcha bo‘lmasin — 15 ta bookmarkni hech kim boshqarmaydi. 2–4 ta: reset, asosiy ko‘rinish, ixtiyoriy drill.</p>

<p>Mobile layout. View → Mobile layout. Telefon uchun alohida joylashuv: card lar ustma-ust, asosiy grafik, slicer. Desktop dagi yonma-yon 6 ta chart telefonni sindiradi. Bookmark mobilida ham ishlashi mumkin, lekin avval oddiy layout.</p>

<p>Xato: bookmark ni har filtr o‘zgarishida yangilab yuborish — foydalanuvchi holati uchib ketadi. Xato: drillthrough sahifasini oddiy menyuda qoldirish, filtrsiz — bo‘sh yoki chalkash. Yashirin qilib, faqat drill orqali kirsın. Sinov: o‘zingiz slicer ni buzing, Reset bosing. Qaytdimi? Qaytmasa, bookmark sozlamasi. Shu 10 daqiqa qo‘llab-quvvatlash xatlarini kamaytiradi.</p>
""",
    "pbi-slicer": """
<p>Filtrning uch joyi bor. Shu yerda chalkashlik boshlanadi. Slicer — foydalanuvchi ko‘radigan, bosadigan filtr. Filter pane — muharrir (va ba’zan foydalanuvchi) uchun, vizual / sahifa / hisobot darajasida. Ikkalasi birga ishlaydi. Qaysi daraja — savolga qarab.</p>

<table>
  <tr><th>Daraja</th><th>Qayerga ta’sir</th><th>Misol</th></tr>
  <tr><td>Visual</td><td>Faqat bitta grafik</td><td>Bitta card da faqat 2024</td></tr>
  <tr><td>Page</td><td>Shu sahifa</td><td>“Filiallar” sahifasida faqat Toshkent</td></tr>
  <tr><td>Report</td><td>Barcha sahifalar</td><td>Faqat Status = Faol</td></tr>
</table>
<p>Toshkentni faqat bitta sahifada qotirmoqchi, boshqalar butun mamlakatni ko‘rsatsin — Page filter, Report emas. Butun hisobotda test filialar chiqmasin — Report level, kerak bo‘lsa qulflang (lock) va yashiring: foydalanuvchi olib tashlay olmasin.</p>

<p>Slicer turlari: ro‘yxat, dropdown, between (sana, summa). Ko‘p qiymat: Ctrl yoki “Select all.” Select all ni o‘ylab qo‘ying — ba’zan “hammasi tanlangan” va “hech narsa” farqi chalg‘itadi. Sana slicer — Relative date (oxirgi 30 kun) qulay, lekin CFO “mart oyi” desa, calendar aniqroq.</p>

<p>Nechta slicer? 3–5 ta asosiy: yil/oy, shahar yoki mintaqa, kategoriya. 12 ta slicer — foydalanuvchi qo‘rqadi va noto‘g‘ri kombinatsiya qiladi. Qolganini Filter pane da yoki boshqa sahifada.</p>

<p>Slicer ham vizual: joyi, “All” yozuvi, qidiruv (ko‘p filial). Sync ni keyingi dars. Hozir: Report filter ni muharrir sifatida qo‘ying, foydalanuvchiga esa 2–3 slicer. Card dagi “doim Toshkent” ni slicer emas, CALCULATE bilan qilgan edik — aralashtirmang. Slicer — odam tanlaydi. CALCULATE — siz qotirasiz. Visual filter — “shu grafik o‘zgacha.” Uchala vosita, uchala maqsad.</p>

<p>Xato: bir xil maydonni ham slicer, ham page filter qilib, keyin “nima uchun bo‘sh?” Qoida: bir maydon — bir asosiy boshqaruv. Tekshiruv: Faol mijozlarni report level qulflang, Toshkentni slicer qiling. Ikkinchi sahifa ochilsa, Faol saqlanadimi? Saqlansa — report filter. Toshkent saqlanmasa — slicer sahifaga bog‘liq, sync kerak bo‘lishi mumkin.</p>
""",
    "pbi-interactions": """
<p>Default: bir ustunni bossangiz, boshqa vizuallar ham o‘zgaradi. Ko‘pincha yaxshi: filialni tanladingiz, trend shu filial. Ba’zan yomon: Card “tarmoq jami” bo‘lishi kerak, bar esa detal. Bar ni bosganda Card ham kichrayadi — CFO “jami qayerga ketdi?” deydi. Bu DAX xatosi emas. Bu <strong>Edit interactions</strong>.</p>

<p>Vizualni tanlang (ta’sir qiluvchi, masalan bar). Format lenta → <strong>Edit interactions</strong>. Boshqa vizuallar ustida kichik ikonkalar: Filter, Highlight, None. Card ustida <strong>None</strong> — bar bosilsa, Card qimirlamaydi. Trendda Filter — qatorlar kesiladi, faqat o‘sha filial. Highlight — hammasi ko‘rinadi, tanlangan qismi yorqin, qolgani xira (ulush). Auditoriyaga qarab: “qancha qoldi” uchun Filter, “ulushi qanday” uchun Highlight.</p>

<p>Qanday tanlash. KPI “umumiy qolsin” — None. Jadval detal bo‘lsin — Filter. Pie (agar ishlatilsa) bosilganda bar highlight — ko‘rish oson. Har juftlikni o‘ylab chiqing, 10 vizualda 90 juftlik — charchoq. Shuning uchun kam vizual yaxshi.</p>

<p>Ikki tomon. A B ni filtrlaydi, B A ni ham. Ba’zan sikl: ikkalasini bosib, tushunarsiz holat. Keraksiz yo‘nalishni None qiling. Slicer odatda hammani filtrlaydi — slicer ni None qilmang, aks holda u o‘yinchoq bo‘lib qoladi. Exception: “taqqoslash” slicer alohida measure uchun — murakkab, boshlang‘ichda kerak emas.</p>

<p>Tekshiruv. Bar da Samarqand, Card o‘zgarmasin, Line o‘zgarsin. Edit interactions: Card None, Line Filter. Reset bookmark bor bo‘lsa, bosish holatini ham tozalashini tekshiring.</p>

<p>Xato: hech narsani sozlamasdan “DAX yozib Card ni qotiraman” — mumkin (ALL), lekin oddiy None aniqroq. Xato: hamma joyda Highlight, foydalanuvchi “nima uchun son o‘zgarmadi, faqat rang?” deb adashadi. Qisqa: ta’sir — hikoyaning bir qismi. Qaysi son qotishi, qaysi grafik tinglashi kerak — yozib qo‘ying, keyin ikonalarni bosing.</p>
""",
    "pbi-sync": """
<p>Ikki sahifa. Overview da mintaqa slicer: Toshkent. Details ochdingiz — slicer yo‘q yoki “hamma.” Menejer: “Men Toshkentni tanlagan edim.” Siz: “boshqa sahifa.” U: “nima farqi?” <strong>Sync slicers</strong> shu tushunmovchilikni yechadi.</p>

<p>View → Sync slicers. Jadval: qatorlar — slicer lar, ustunlar — sahifalar. Ikki belgi: ko‘rinsin (ko‘z), sinxron bo‘lsin (belgi). Ba’zan slicer faqat Overview da ko‘rinadi, lekin Details ga ham ta’sir qiladi — ko‘z o‘chiq, sync yoqilgan. Details toza qoladi, filtr yuradi. Ba’zan ikkala sahifada ham ko‘rinsin — foydalanuvchi qayerda ekanini unutmasin.</p>

<p>Qachon sync qilmaslik. “Filiallar” sahifasida Toshkent page filter qotgan, Overview butun mamlakat. Shu slicer ni sync qilsangiz, Overview ham Toshkentga yopiladi — hikoya buziladi. Har slicer uchun alohida qaror.</p>

<p>Nusxa. Slicerni Ctrl+C / sahifaga qo‘yish — yangi obyekt, sync avtomatik emas. Sync panelda bir xil maydonni bog‘laysiz. Nomlar chalkashmasin: ikkala “Slicer 1” — o‘zingiz adashasiz. Selection pane da “Mintaqa slicer” deb nomlang.</p>

<p>Bookmark bilan. Reset bookmark sync holatini ham saqlashi mumkin — ehtiyot. Avval sync ni sozlang, keyin Reset ni qayta yozing. Aks holda bookmark eski mustaqil slicerlarni eslaydi.</p>

<p>Xato: 8 sahifa, har birida 5 slicer, hammasi sync — sekin va “nima nima ta’sir qiladi” noma’lum. 2–3 ta global (yil, mintaqa), qolgani mahalliy. Sinov: Overview da Farg‘ona, Details ga o‘ting. Fact shu viloyatmi? Yo‘q bo‘lsa, sync yo‘q yoki boshqa maydon (shahar vs viloyat). Maydon bir xil bo‘lsin. Shu darsning amaliy yadrosi: foydalanuvchi sahifa almashtirganda hikoya uzilmasin.</p>
""",
    "pbi-publish": """
<p>Desktop da tayyor. Lekin 40 ta menejer noutbukingizni ochmaydi, .pbix ni email qilish ham yechim emas (versiya, parol, hajm). Nashr: Home → <strong>Publish</strong>. Hisobga kirgan bo‘lasiz, <strong>workspace</strong> tanlaysiz. Natija: Service da <strong>dataset</strong> (model, ma’lumot, measure) va <strong>report</strong> (sahifalar). Ikkalasi bog‘liq. Keyin ixtiyoriy Dashboard — pin qilingan plitkalar, bir ekran.</p>

<p>Workspace nima? Jamoa papkasi, bulutda. Rollar: Admin (sozlama, o‘chirish), Member, Contributor (yozish, nashr), Viewer (faqat ko‘rish). <strong>My workspace</strong> — shaxsiy qumloq. Production savdo hisobotini u yerga qo‘ymang: kasal bo‘lib qolsangiz, hech kim boshqarmaydi; 3 tahlilchi to‘qnashadi. Shared workspace: “Savdo-Analitika”, rollar aniq. IT dan so‘rang.</p>

<p>Report vs Dashboard. Report — siz yasagan sahifalar, slicer, bookmark, boy interaktivlik. Dashboard — Service da tile lar: card, skrinshot, ba’zan qisqa. Rahbariyat “bir ekranli bosh sahifa” desa — Dashboard + chuqur tahlil Report da. Farq yo‘q deb o‘ylash — chalkashlik. Ko‘p tahlilchilar asosan Report ulashadi, Dashboard ixtiyoriy.</p>

<p>Qayta nashr. .pbix ni o‘zgartirdingiz, yana Publish, o‘sha workspace, o‘sha nom — ustidan yoziladi. Odamlardagi havola o‘sha. Nomni o‘zgartirib yangi nusxa — ikki haqiqat. Aniq yashash: bitta dataset, yangilash shu.</p>

<p>Litsenziya. Bepul / Pro / Premium — kim ko‘rishi, refresh soni. Viewer ga Pro kerak bo‘lishi mumkin (tarqatish modeliga qarab). Bu IT savoli, lekin “hamma ocholadi” deb o‘ylamang. Xato: My workspace ga publish qilib, 40 kishiga share — boshqaruv yo‘q. Xato: dataset ni o‘chirib, report ni qoldirish. Xato: test va prod bir workspace da, “nima uchun CFO test raqamini ko‘rdi.”</p>

<p>Qadamlar: saqlash, Publish, workspace tanlash, brauzerda ochib slicer ni sinash. Hali refresh va app yo‘q — keyingi darslar. Bugun tushuncha: Desktop yaratadi, Service ko‘rsatadi va jamoa joyi beradi. .pbix — manba fayl, uni ham git yoki papkada saqlang. Service yagona nusxa emas, agar o‘chib ketsa.</p>
""",
    "pbi-refresh": """
<p>Kecha nashr qildingiz. Bugun ertalab CFO kechagi savdoni ko‘rmayapti. Sabab: Import — surat. Surat yangilanmasa, eski. <strong>Scheduled refresh</strong> — Service da dataset sozlamalari: kuniga necha marta (litsenziyaga bog‘liq), soat, vaqt mintaqasi. Toshkent 08:00 — kechasi 02:00 da SQL dan olib, ertalab tayyor. DirectQuery da “jadval” boshqacha: so‘rov vaqtida manba; lekin on-prem bo‘lsa, gateway baribir.</p>

<p>Gateway. Ichki SQL, ofisdagi Excel papkasi — Power BI buluti to‘g‘ridan-to‘g‘ri kira olmaydi (xavfsizlik). Kompyuter yoki serverda <strong>on-premises data gateway</strong>. Standard (korxona, bir nechta odam) vs Personal (faqat siz, kompyuter o‘chiq bo‘lsa refresh o‘ladi). Personal bilan prod qilmang. Gateway o‘chiq, parol eskirgan, server nomi o‘zgargan — refresh failed.</p>

<p>Muvaffaqiyatsiz refresh. Email keladi yoki Service da qizil. Tekshiruv tartibi: 1) credentials — parol, Windows hisobi; 2) gateway onlaynmi; 3) manba ochiladimi (VPN, DBA o‘zgartirganmi); 4) Power Query xatosi — yangi ustun, yo‘qolgan fayl, tip; 5) hajm/timeout. Desktop da Refresh ishlashi Service ni bildiradi, lekin yo‘l boshqacha: Desktop sizning kompyuteringiz, Service — gateway. Fayl yo‘li <code>C:\\Users\\Siz\\Desktop\\savdo.xlsx</code> Service da yo‘q. Papkani tarmoq yo‘liga yoki SharePoint ga ko‘chiring.</p>

<p>Import vs DirectQuery eslatma. Import — aniq vaqtli surat, tez vizual, kechikish bor (oxirgi refresh gacha). DirectQuery — yangiroq, sekin, manba yuki. Hybrid, incremental refresh — katta fact da keyinroq; boshlang‘ichda to‘liq Import + tungi jadval yetarli.</p>

<p>Kim javobgar? Dataset egasi. Ta’tilda bo‘lsangiz, workspace da ikkinchi admin. Refresh vaqtini Description ga yozing: “Har kuni 06:00, kechagi savdo.” CFO “jonli” deb o‘ylamasin.</p>

<p>Xato: Desktop da qo‘lda Refresh, Service ni unutish — sizda yangi, odamlarda eski. Xato: 15 daqiqada refresh, manba og‘ir, litsenziya cheklov. Xato: gateway ni noutbukka o‘rnatib, kechasi yopish. Sinov: kichik dataset, scheduled 1 marta, ertasi kuni timestamp ni Data view yoki measure <code>TODAY()</code> emas, balki manba “maksimal sana” card da ko‘rsating. Yangilanganmi — shu card aytadi.</p>
""",
    "pbi-share-apps": """
<p>Ulashishning ikki yo‘li: tez va tartibli. Tez: report da Share, email. 5 kishi, test — yaxshi. 200 filial menejeri — kecha kimdir huquqini yo‘qotdi, kimdir eski havola, kimdir dataset ga ham kirdi, keraksiz. Tartibli yo‘l: <strong>Power BI App</strong>.</p>

<p>Workspace da hisobotlar, dataset tayyor. Create app. Nom, tashkilot, qaysi reportlar kiritiladi, navigatsiya. Auditoriyaga nashr: guruh, ro‘yxat. Foydalanuvchi Power BI da <strong>Apps</strong> bo‘limidan ochadi, workspace ichida adashmaydi. Siz yangilaysiz, app yangilanadi (nashr qilishni unutmang — ba’zan “Update app”). Bitta joydan boshqaruv.</p>

<p>Huquq. Viewer — ko‘rish, filtr, odatda yuklab olish cheklanishi mumkin. Contributor — o‘zgartirish. Har kimga Admin — falokat: o‘chirish, RLS ni aylanib o‘tish. Dataset huquqi report dan kengroq bo‘lishi mumkin — Build huquqi: boshqa hisobot yozish. Kerak bo‘lmasa bermang. RLS keyingi dars: bir app, turli qatorlar.</p>

<p>Endorsement. Dataset ni Promoted yoki Certified qilish — “shu ishonchli savdo.” 50 ta o‘xshash dataset orasida odam shuni tanlaydi. Sensitivity label — korporativ siyosat, moliyaviy maxfiylik. IT yoqadi.</p>

<p>Qachon oddiy share? Bir odam, bir haftalik savol. Qachon app? Doimiy CFO dashboard, ko‘p foydalanuvchi, versiya nazorati. Qachon .pbix email? Deyarli hech qachon, agar maxfiy savdo bo‘lsa.</p>

<p>Xato: 200 marta individual share. Xato: app yaratmasdan workspace ga 200 Viewer qo‘shish — ular ishlanayotgan test sahifalarini ko‘radi. App — “tozalangan vitrina”, workspace — oshxona. Xato: Update app ni unutib, “nima uchun odamlarda eski?” Sinov (huquq bo‘lsa): test workspace, ikkita hisob, app, ikkinchi hisobda Apps dan ochish. Ko‘rinmasa — litsenziya yoki auditoriya. Ko‘rinsa — yo‘l to‘g‘ri. Keyin RLS: vitrina bir, ko‘z turlicha.</p>
""",
    "pbi-rls": """
<p>Toshkent filiali menejeri Farg‘ona savdosini ko‘rmasligi kerak. Yechim “har filialga alohida .pbix” emas — 12 nusxa, 12 marta tuzatish. Yechim: bitta dataset, <strong>Row-Level Security</strong>. Qatorlar filtrlanadi. Measure yashirilmaydi: u qolgan qatorlar ustida ishlaydi. Toshkent roli — faqat Toshkent qatorlari, jami ham shu.</p>

<p>Desktop: Modeling → Manage roles. Rol nomi: <code>Toshkent</code> yoki <code>FilialMenejer</code>. Jadvalga filtr:</p>
<pre>DimFilial[shahar] = "Toshkent"</pre>
<p>Yoki fact da, lekin dimension da yozish osonroq — yulduz filtrni fact ga olib tushadi. Dinamik: har foydalanuvchi o‘z filiali. Jadvalda email va filial. G‘oya:</p>
<pre>DimFilial[MenejerEmail] = USERPRINCIPALNAME()</pre>
<p><code>USERPRINCIPALNAME()</code> — Service dagi login (odatda email). Mapping jadvali toza bo‘lsin. Statik rol o‘rganish uchun yetarli; prod da ko‘pincha dinamik.</p>

<p>Tekshiruv Desktop da: Modeling → <strong>View as</strong> → rol. Sahifa Toshkentmi? Farg‘ona yo‘qolganmi? Jami kichrayganmi? Service ga chiqmasdan oldin shu. Service da workspace access yetarli emas: Role assignment — foydalanuvchini rolga qo‘shasiz. Qo‘shmasangiz, RLS yo‘qdek hammasi (yoki hech narsa — sozlamaga qarab). Sinang.</p>

<p>Muhim tuzoq. Workspace Admin/Member ko‘pincha RLS ni aylanib o‘tadi — “butun model.” Menejerni Viewer qiling, App orqali. O‘zingizni Admin qilib “RLS ishlamayapti” deb o‘ylamang: View as yoki test hisob.</p>

<p>Both relationship, noaniq yo‘l — RLS filtri kutilgan joyga tushmasligi mumkin. Oddiy star, Single filter — RLS tinchroq. “Hide measure” RLS emas. Sahifa yashirish ham emas. Faqat qator.</p>

<p>Xato: Toshkent ni slicer da yashirish — foydalanuvchi Filter pane dan ochishi mumkin. RLS — server tomonda, aylanib bo‘lmaydi (Viewer uchun). Xato: rolni SQL dagi boshqa mantiq bilan ikki marta, mos kelmasligi. Bitta haqiqat. CFO hammasi kerak — alohida rol <code>Rahbariyat</code> filtrsiz, yoki umuman RLS assignment yo‘q (va huquq yuqori — ehtiyot). Yozib qo‘ying: kim qaysi rol. Shu darsning amaliy yadrosi: bitta .pbix, ko‘p ko‘z, qatorlar bo‘yicha.</p>
""",
    "pbi-perf": """
<p>Hisobot 20 soniyada ochiladi. Rahbar kutmaydi, Mobile da umuman yo‘q. “Kompyuter sekin” emas. Model shishgan, vizual ko‘p, DAX og‘ir, Both hamma joyda. Tuzatish — sehr emas, ro‘yxat. Avval o‘lchash: View → <strong>Performance analyzer</strong> → Start recording, sahifani yangilang. Qaysi vizual uzoq: DAX? vizual chizish? Shu yerdan boshlang.</p>

<p>Ma’lumot. Keraksiz ustun va jadval — Power Query da olib tashlash, Hide yetarli emas (Import da ustun baribir xotirada). Matn kalit o‘rniga butun son. To‘g‘ri tip. Fact da takroriy matn — star ga qayting. Incremental refresh, aggregations — millionlab qator bo‘lsa, keyingi bosqich; avval axlatni tashlang.</p>

<p>Model. Single filter, keraksiz Both yo‘q. Many-to-many yo‘q. Keraksiz calculated column (har qator, og‘ir formula). Measure — yaxshi; 200 ta murakkab CALCULATE + iterator har card da — yomon. SUMX ni fact ning har qatorida og‘ir ifoda bilan — ehtiyot.</p>

<p>Hisobot. 40 vizual — 40 so‘rov. 8 ga tushiring. Custom visual og‘ir. Map, high-density scatter. Sahifa bo‘ling. Slicer da “Select all” million qiymat — qidiruvli dropdown yoki boshqa maydon (mintaqa, shahar emas har mijoz).</p>

<p>DirectQuery sahifasi: har slicer — SQL. 200 foydalanuvchi — manba ingillaydi. Import + tungi refresh ko‘pincha tezroq “yetarli yangi.”</p>

<p>Tekshiruv tartibi: analyzer → eng sekin vizualni olib tashlab farqni ko‘ring → ustunlarni qisqartiring → Both ni soddalashtiring → DAX ni soddalashtiring (odatda ALL ni kichikroq jadvalga). “Yana calculated column” deyarli yechim emas. “Yana custom visual” ham.</p>

<p>Xato: muammoni theme da qidirish. Xato: har qatorga “optimallashtirish” column. Xato: Performance analyzer ni ochmasdan DAX ni qayta yozish. 80 ta matn ustuni + 40 vizual + Both — birinchi kun: ustun va vizual soni. Tezlik 20 soniyadan 4 ga tushsa, CFO baxtli, siz DAX ni keyin chiroyli qilasiz. Tezlik ham tahlil sifati.</p>
""",
    "pbi-governance": """
<p>Tashkilotda 50 ta o‘xshash dataset. “Savdo”, “Savdo_final”, “Savdo_CFO_nusxa.” Foydalanuvchi qaysi haqiqat? Sizning hisobingiz to‘g‘ri bo‘lsa ham, boshqasi eski Excelga ulangan. <strong>Governance</strong> — qoida va odat: nom, egasi, ishonch belgisi, hujjat. DAX emas, lekin yo‘qligi DAX ni behuda qiladi.</p>

<p>Endorsement. Dataset ni <strong>Promoted</strong> (jamoa tavsiyasi) yoki <strong>Certified</strong> (rasmiy, odatda markaziy tahlil/IT). Foydalanuvchi qidiruvda shuni ko‘radi. Certified ni har test fayliga qo‘ymang — ishonch devalvatsiyasi. Bitta “Savdo — rasmiy” dataset, app shundan.</p>

<p>Nomlash. Fact/Dim prefiksi, measure “Jami savdo” (fe’l emas, qisqartma emas). Til: aralash Uzb/Eng — lug‘at qiling, bir xil yozing: <code>shahar</code> va <code>City</code> ikkalasi emas. Workspace: “Prod-Savdo”, “Test-Savdo.” My workspace da prod yo‘q.</p>

<p>Hujjat. Dataset Description: manba (SQL view, papka), refresh vaqti, egasi, RLS qoidalari (“filial menejeri o‘z shahri”). Measure Description — Fields da ko‘rinadi. “Ortacha chek = jami / chek soni, qaytarishsiz.” Kelajakdagi siz va hamkasb. Excel “qanday hisoblangan” ni unutish — Power BI da yozib qo‘yish mumkin.</p>

<p>Huquq va maxfiylik. RLS, sensitivity, kim Build oladi. Test ma’lumotida shaxsiy telefon raqami — prod app ga chiqmasin. Gateway kim boshqaradi, parol qachon yangilanadi — kalendar.</p>

<p>Kurs yakuni, yangi sehr yo‘q. Siz noldan: Desktop nima, Get data, Query da tozalash, yulduz model, column vs measure, CALCULATE odmi tilda, vizual tanlash, sahifa hikoyasi, slicer va sync, Publish, refresh, app, RLS, sekinlik. Qolgani — bitta haqiqiy savdo fayli: Connect → Transform → Model → 3 measure → Overview sahifa → (imkon bo‘lsa) Service. Har qadamda “CFO ishonadimi?” deb so‘rang. Ishonmasa, rang emas, kalit va yig‘indi. Ishonsa, ulashing. Keyingi ish — real loyiha, shu ovozda: avval savol, keyin bosish.</p>
""",
}
