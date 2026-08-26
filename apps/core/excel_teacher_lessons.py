"""Excel darslari — o‘qituvchi ovozida, noldan.
Har dars talaba bilan gaplashgandek yozilgan; bir xil qolip takrorlanmaydi.
"""

LECTURES = {
    "excel-nima": """
<p>Salom. Agar siz Excelni “chiroyli jadval chizadigan dastur” deb bilsangiz — tushunarli. Ko‘pchilik shunday boshlaydi. Shu kursda esa uni <strong>tahlil vositasi</strong> qilib o‘rganamiz: savol berasiz, kataklar javob qaytaradi.</p>

<p>Ishda ma’lumot odatda avval Excelga tushadi. Savdo eksporti, HR ro‘yxati, bank tranzaksiyalari, do‘konning kunlik kassasi. SQL va Power BI keyinroq keladi. Birinchi stolda siz o‘tirasiz — chalkash fayl oldingizda.</p>

<p>Qisqa lug‘at, qo‘rqitmasdan. <strong>Workbook</strong> — butun fayl, odatda <code>.xlsx</code>. Ichida varaqlar bor: <strong>Worksheet</strong>. Har varaq kataklardan iborat: <strong>Cell</strong>. Manzil oddiy: A1, B15. Bir nechta katak — <strong>Range</strong>, masalan <code>A1:D100</code>. Keyinroq <strong>Table</strong> ni o‘rganamiz: Ctrl+T bilan “oddiy diapazon” tuzilmali jadvalga aylanadi.</p>

<p>Tasavvur qiling, Toshkentdagi kichik do‘kon. Uch varaq: xom savdo, hisob-kitob, rahbarga chiqariladigan hisobot. Professional odat shu — qatlamlarni aralashtirmaslik:</p>
<table>
  <tr><th>Varaq</th><th>Nima yotadi</th><th>Tegish mumkinmi?</th></tr>
  <tr><td><code>raw_Sales</code></td><td>CSV dan kelgan asl qatorlar</td><td>Yo‘q — faqat saqlash</td></tr>
  <tr><td><code>calc_Sales</code></td><td>formulalar, flaglar, yig‘indilar</td><td>Ha — bu sizning ishingiz</td></tr>
  <tr><td><code>report_Sales</code></td><td>KPI, jadval, qisqa xulosa</td><td>Faqat ko‘rsatish</td></tr>
</table>
<p>Rang bilan “bezash” tahlil emas. Mantiq bilan tuzish — tahlil. Xom ma’lumotni o‘chirib tashlasangiz, ertaga auditda tushuntira olmaysiz.</p>

<p>Qachon Excel yetarli, qachon boshqa vosita? Tezkor tozalash, yuz minglab emas — o‘n-yuz ming qator, o‘zingiz tekshiradigan hisobot: Excel. Millionlab qator, 200 kishi bir manbadan o‘qiydi: SQL yoki ombor, ustiga Power BI. Interaktiv dashboard, rollar, telefon orqali ko‘rish: yana Power BI. Excel — tez laboratoriya stoli, ombor emas.</p>
<pre>=COUNTA(tbl_Sales[OrderID])
=SUM(tbl_Sales[Amount])</pre>
<p>Bu ikkisi hali “sehr” emas. Lekin odat shu: xom varaqqa tegmasdan, calc da sanash. Formula xom qatorni o‘zgartirmaydi — SQL dagi SELECT kabi o‘qiydi.</p>

<p>Quyida interfeysni ochib, bitta kichik savdo jadvalini ko‘rasiz. Keyingi darsda esa tuzoq: katak “son”ga o‘xshaydi, lekin Excel uni matn deb o‘qiydi. Shu yerdan SUM 0 qaytadi — va odamlar “Excel buzilgan” deyishadi. Buzilmagan. Turini tushunmagansiz.</p>
""",
    "excel-turlar": """
<p>Qarang. Bankdan tranzaksiya fayli keldi. Amount ustuni chapga tekislangan. Siz <code>SUM</code> qo‘ydingiz — natija 0. Formula to‘g‘ri. Ma’lumot “go‘yo son”. Aslida esa matn. Ishda shunday bo‘ladi, deyarli har hafta.</p>

<p>Excel katakda nafaqat qiymat, balki <strong>tur</strong> saqlaydi. Ko‘rinish — format. Mantiq — tur. Ming ajratgich va so‘m belgisi hisobot uchun. Hisoblash uchun esa haqiqiy son kerak.</p>

<p>Asosiy turlar, oddiy tilda:</p>
<ul>
  <li><strong>Number</strong> — qo‘shish, bo‘lish, o‘rtacha. O‘ngga tekislanadi.</li>
  <li><strong>Text</strong> — kodlar. <code>00123</code> ni songa aylantirsangiz, boshidagi nollar yo‘qoladi. SKU, INN, karta oxirgi 4 raqami — odatda matn.</li>
  <li><strong>Date/Time</strong> — aslida serial number. 1-yanvar 1900 dan boshlab kunlar. Shuning uchun sanalarni ayirish mumkin.</li>
  <li><strong>Boolean</strong> — TRUE/FALSE. IF ning javobi shu.</li>
  <li><strong>Error</strong> — <code>#N/A</code>, <code>#DIV/0!</code>, <code>#VALUE!</code>. Bu ham “tur”, yashirishdan oldin sababini biling.</li>
</ul>

<p><code>01.02.2024</code> matn bo‘lsa, sana filtrlari ishlamaydi: “fevral” deb so‘rasangiz, bo‘sh chiqadi. <code>1 200</code> ichida bo‘shliq bo‘lsa — yana matn, SUM 0. Auditlarda eng ko‘p uchraydigan muammo shu: ko‘z o‘qiydi, Excel o‘qimaydi.</p>

<table>
  <tr><th>Katakda nima</th><th>Ko‘rinishi</th><th>Haqiqiy tur</th><th>SUM nima qiladi</th></tr>
  <tr><td>150000</td><td>o‘ngga</td><td>son</td><td>qo‘shadi</td></tr>
  <tr><td>"150000"</td><td>chapga</td><td>matn</td><td>e’tiborsiz, 0</td></tr>
  <tr><td>01.02.2024 matn</td><td>chapga</td><td>matn</td><td>sana emas</td></tr>
  <tr><td>45323 (serial)</td><td>sana formatida</td><td>son/sana</td><td>filtrlash ishlaydi</td></tr>
</table>

<p>Tekshirish. <code>=ISTEXT(A2)</code> — matnmi? <code>=ISNUMBER(A2)</code> — sonmi? Excelda tayyor <code>ISDATE</code> yo‘q; sana uchun <code>=CELL("format";A2)</code> yoki Power Query da tur belgilash ishonchliroq. To‘g‘rilash: <code>VALUE</code>, <code>NUMBERVALUE</code>, yoki Query da <em>Change Type</em>.</p>
<pre>=VALUE(SUBSTITUTE(A2;" ";""))
=NUMBERVALUE(A2;",";".")
=ISTEXT(B2)
=ISNUMBER(B2)</pre>
<p>Hisobotda so‘m va bo‘shliq — format. Hisoblashda esa toza son. Ikkalasini aralashtirmang. Keyingi darsda shu toza sonlarni Table ichiga solamiz — formula o‘zi kengayadi.</p>
""",
    "excel-table": """
<p>Tasavvur qiling, har kuni yangi savdo qatori tushadi. Formula yozdingiz: <code>=C2*D2</code>, keyin pastga tortasiz. Ertaga 40 ta yangi qator. Formula yetmadi. Pivot eski diapazonni o‘qiydi. Hisobot yolg‘on. Ko‘p odam shu yerda adashadi: “Excel yangilamadi” — aslida manba qisqa qolgan.</p>

<p><strong>Excel Table</strong> shu dardni davolaydi. Ctrl+T. Oddiy diapazon tuzilmali jadvalga aylanadi: filtr, saralash, yangi qatorda formula avtomatik. Pivot va Power Query uchun barqaror manba.</p>

<p>Qoidalar, qattiq:</p>
<ol>
  <li>Birinchi qator — unique header. Ikki qatorli “chiroyli” sarlavha — Table dushmani.</li>
  <li>O‘rtada bo‘sh qator yoki bo‘sh ustun qo‘ymang. Table u yerni chegara deb o‘ylashi mumkin.</li>
  <li>Birlashtirilgan kataklar (merge) — unmerge qiling, keyin Table.</li>
  <li>Nom bering: <code>tbl_Sales</code>, <code>tbl_HR</code>. “Table1” bilan yashamang.</li>
</ol>

<p>Strukturali havola — Table ning tili. Qator ichida <code>[@Amount]</code> “shu qatordagi Amount”. Butun ustun: <code>Sales[Amount]</code>. A2, C2 deb yodlash shart emas.</p>
<pre>=[@Qty]*[@Price]
=SUM(tbl_Sales[Amount])
=COUNTA(tbl_Sales[OrderID])</pre>

<table>
  <tr><th>OrderID</th><th>Qty</th><th>Price</th><th>LineTotal (formula)</th></tr>
  <tr><td>1001</td><td>2</td><td>45000</td><td>=[@Qty]*[@Price] → 90000</td></tr>
  <tr><td>1002</td><td>1</td><td>120000</td><td>=[@Qty]*[@Price] → 120000</td></tr>
</table>
<p>A1:D1 header, pastda ma’lumot. Ctrl+T → “My table has headers” → OK. Yangi qator qo‘shsangiz, LineTotal o‘zi tushadi. Shu kichik sehr ishda soat tejaydi.</p>

<p>Merge qilingan sarlavha bilan Table yaratib bo‘lmaydi. Avval bitta header qatori. Chiroy hisobot varag‘ida, xom jadvalda emas. Keyingi darsda Table ichidagi ifloslikni tozalaymiz — TRIM, dublikat, aralash format.</p>
""",
    "excel-clean": """
<p>Ishda shunday bo‘ladi: CSV ochasiz, birinchi 10 qator chiroyli. Pivot qilasiz — “Toshkent” ikki marta: birida bo‘shliq bor. SUM ikki bo‘lak. Rahbar “nima bu?” deydi. Tahlildan oldin tozalash — shou emas, majburiyat.</p>

<p>Tipik iflosliklar, Toshkentdagi do‘kon yoki bank faylida:</p>
<ul>
  <li>Bo‘sh qatorlar; ism <code>" Ali "</code> — oldi-orqasida bo‘shliq</li>
  <li>Bir mijoz ikki marta, yoki bir OrderID ikki marta — bular turli savol</li>
  <li>Bir ustunda sana va matn aralash: <code>01.02.2024</code> va <code>noma’lum</code></li>
  <li>Bir katakda ikki qiymat: <code>Toshkent, Chilonzor</code></li>
  <li>Yashirin belgilar, non-breaking space (ko‘z ko‘rmaydi, TRIM ba’zan yengolmaydi)</li>
</ul>

<p>Asosiy qurollar. <code>TRIM</code> chetlarini kesadi. <code>CLEAN</code> chop etilmaydigan belgilarni. <code>SUBSTITUTE</code> aniq belgini almashtiradi. Find &amp; Replace — tez, lekin butun ustunni o‘ylab qiling. Text to Columns / Flash Fill — “ism familiya”ni ikki ustunga. Takroriy oylik tozalash uchun eng yaxshisi keyinroq: Power Query. Hozir qo‘l bilan tushunib oling.</p>
<pre>=TRIM(A2)
=CLEAN(A2)
=SUBSTITUTE(A2;CHAR(160);"")
=TRIM(CLEAN(SUBSTITUTE(A2;CHAR(160);" ")))</pre>

<p>Remove Duplicates — ehtiyot. Kalit nima? Buyurtmalar jadvalida <strong>OrderID</strong> unique bo‘lishi kerak. <strong>CustomerID</strong> takrorlanadi — bir odam o‘n marta xarid qiladi. CustomerID bo‘yicha dublikat o‘chirsangiz, savdo yo‘qoladi. Avval: bu haqiqiy nusxami yoki ikki voqea?</p>
<table>
  <tr><th>Kalit</th><th>Takror nima deydi</th><th>O‘chirish</th></tr>
  <tr><td>OrderID</td><td>Bir buyurtma ikki marta yozilgan</td><td>Ko‘pincha ha, tekshirib</td></tr>
  <tr><td>CustomerID</td><td>Bir mijozning bir necha buyurtmasi</td><td>Yo‘q — bu fakt</td></tr>
  <tr><td>Ism + telefon</td><td>Balki bir odam, balki homonim</td><td>Qo‘lda qaror</td></tr>
</table>

<p>Tozalashni raw varag‘ida emas, nusxada yoki calc qatlamida qiling. Asl fayl saqlansin. Keyin Sort/Filter — toza jadvalda ishlaydi, iflosida yolg‘on.</p>
""",
    "excel-sort-filter": """
<p>Rahbar so‘raydi: “Toshkent, summa milliondan katta, oxirgi 30 kun.” Ro‘yxat 12 ming qator. Ko‘z bilan izlamaysiz. Sort tartib beradi. Filter qatorlarni yashiradi — o‘chirmaydi, esda tuting.</p>

<p>Sort. Data → Sort. Avval Region, keyin Amount kamayishda. Ikkinchi mezon birinchisi teng bo‘lganda ishlaydi — SQL dagi <code>ORDER BY city, amount DESC</code> bilan bir xil mantiq. Oy tartibi A–Z bo‘lsa, “Aprel” “Dekabr”dan oldin chiqadi. Custom list (Yanvar, Fevral, …) shu yerda muhim.</p>

<p>Xato, klassika: faqat Amount ustunini belgilab Sort. Qatorlar “buziladi” — Ali ning shahari Malika ning summasiga yopishib qoladi. Butun jadvalni tanlang. Yoki Table ishlating: Table o‘zi qatorni butunlay siljitadi.</p>
<table>
  <tr><th>Noto‘g‘ri</th><th>To‘g‘ri</th></tr>
  <tr><td>Faqat C ustuni → Sort</td><td>Table yoki A1:F5000 tanlab Sort</td></tr>
  <tr><td>Birinchi 100 qatorni tartiblash</td><td>Header bilan butun manba</td></tr>
</table>

<p>Filter. Table tepasida o‘qcha. Text Filters: “Toshkent bilan boshlanadi”. Number Filters: kattaroq, oraliq, Top 10. Date Filters: oxirgi oy, shu hafta. Top 10 — tez ko‘zdan kechirish; bu yakuniy statistika emas.</p>
<pre>Filtr zanjiri (misol):
Region = Toshkent
Amount &gt; 1000000
OrderDate = oxirgi 30 kun</pre>
<p>Natijani hisobotga ko‘chirmoqchi bo‘lsangiz: Copy → Paste Values alohida varaqqa. Filtr o‘chsa, asl qatorlar qaytadi — yashirilgan edi, o‘chirilmagan.</p>

<p>Advanced Filter kamroq ishlatiladi, lekin “mezonlar jadvali” bilan murakkab shartni boshqa varaqqa ko‘chiradi. Kundalik ishda Table + Autofilter yetarli. Keyingi darsda filtrlashni rang bilan ko‘rsatamiz — Conditional Formatting. Lekin rang — yordamchi, filtr o‘rnini bosmaydi.</p>
""",
    "excel-cf": """
<p>Raqamlar to‘g‘ri. Lekin 800 qator Amount ichidan anomaliyani ko‘z topishi qiyin. Conditional Formatting (CF) katakni shartga qarab bo‘yaydi. Bu tahlil vositasi. Yakuniy PDF hisobotni “archagul” qilish vositasi emas.</p>

<p>Foydali turlari. Color scales — taqsimot: kim qizil zonada. Data bars — yonma-yon solishtirish, ustun diagrammasiz. Icon sets — status; ehtiyot: faqat rangga tayanmang, ko‘rish qiyinligi va qora-oq chop etish bor. Eng kuchlisi — formula qoidasi: “Target dan past bo‘lsa”.</p>
<pre>=$C2&lt;$E$2
=$D2="Toshkent"
=AND($C2&gt;1000000;$E2&lt;TODAY()-30)</pre>
<p><code>$C2</code> — ustun qotadi, qator yuradi. Qoida butun C2:C500 ga qo‘yiladi. Absolute/relative dollar belgisini xato qo‘ysangiz, bo‘yoq “siljiydi”.</p>

<table>
  <tr><th>Qoida</th><th>Qachon</th><th>Hisobotda</th></tr>
  <tr><td>Color scale</td><td>Taqsimotni tez ko‘rish</td><td>Kam, yoki umuman yo‘q</td></tr>
  <tr><td>Data bar</td><td>Bir ustun ichida solishtirish</td><td>Ixtiyoriy, ehtiyot</td></tr>
  <tr><td>Formula + och qizil</td><td>SLA buzilishi, minus qoldiq</td><td>Minimal, ma’noli</td></tr>
  <tr><td>Har katakda icon set</td><td>—</td><td>Stakeholder PDF da yo‘q</td></tr>
</table>

<p>Professional maslahat: CF — o‘zingiz va jamoa uchun. Rahbarga asosiy xabar son va bitta jumlada bo‘lsin. Qizil — xavf, yashil — maqsad; boshqa 12 rang kerak emas.</p>

<p>Samarqand filiali Target dan pastmi? Formula qoidasi $C da Amount, $E da Target. Ko‘rdingiz — keyin SUMIFS yoki Pivot bilan aniq son. Rang sezgi beradi, qaror son beradi. Keyingi modulda o‘sha sonni IF bilan flag qilamiz.</p>
""",
    "excel-if": """
<p>Exceldagi IF — odamning “agar shunday bo‘lsa, shuni yoz, aks holda boshqasini” gapiga o‘xshaydi. Segmentatsiya, flag, oddiy qoida — tahlilchining kundalik tili. Avval savolni o‘zbekcha ayting, keyin formulaga o‘giring.</p>

<p>Sintaksis uch qism: shart, rost bo‘lsa, yolg‘on bo‘lsa. O‘zbekiston Excelida argumentlar ko‘pincha nuqtali vergul bilan:</p>
<pre>=IF(A2&gt;=1000000;"VIP";"Oddiy")
=IF(AND(B2="Toshkent";C2&gt;0);"Lokal faol";"Boshqa")
=IF(OR(D2="debit";D2="credit");"Tranzaksiya";"Noma’lum")</pre>
<p><code>AND</code> — qizg‘in: hammasi rost. <code>OR</code> — yumshoq: bittasi yetadi. SQL dagi AND/OR bilan bir xil mantiq. Qavsni unutmang: <code>IF(AND(...); ...; ...)</code>.</p>

<p>Biznes. CRM: oxirgi xarid 90 kundan eski → "Churn risk", aks holda "Active". Oddiy, lekin foydali. Bank: Toshkent va musbat amount → "Focus". HR: sinov muddati tugagan va ball 4 dan past → "Suhbat".</p>
<table>
  <tr><th>City</th><th>Amount</th><th>Flag</th></tr>
  <tr><td>Toshkent</td><td>750000</td><td>Focus</td></tr>
  <tr><td>Toshkent</td><td>0</td><td>Other</td></tr>
  <tr><td>Samarqand</td><td>2000000</td><td>Other</td></tr>
</table>
<pre>=IF(AND([@City]="Toshkent";[@Amount]&gt;=500000);"Focus";"Other")</pre>

<p>Ichma-ich IF. 3–4 darajadan oshsa, o‘qilmaydi. Yechim: <code>IFS</code> (ketma-ket shartlar), yordamchi ustun, yoki kichik lookup jadvali (status kodlari). “Chiroyli bitta katak” uchun 12 ta IF — keyin siz ham, hamkasbingiz ham adashasiz.</p>
<pre>=IFS(A2&gt;=1000000;"VIP";A2&gt;=300000;"Oltin";TRUE;"Oddiy")</pre>
<p>Ko‘p odam shu yerda adashadi: matnni songa solishtirish. <code>"1000"&gt;500</code> kutilmagan natija berishi mumkin. Avval turini tozalang, keyin IF. Keyingi darsda shu flaglar ustida SUMIFS — “Focus lar jami qancha?”</p>
""",
    "excel-sumifs": """
<p>Har kuni bir savol: “Mart oyida online kanaldan Toshkent bo‘yicha to‘langan buyurtmalar — qancha so‘m?” Ro‘yxatni filtrlash — ko‘z. Formula — takrorlanadigan javob. Shu yerda SUMIFS, COUNTIFS, AVERAGEIFS.</p>

<p>Nima uchun SUMIF emas, SUMIFS? SUMIFS ko‘p shartni oladi. Argument tartibi barqaror: avval <em>nima qo‘shiladi</em> (sum_range), keyin juftliklar: mezoni qayerda, qiymati nima. SUMIF da tartib boshqacha edi; aralashtirsangiz, jim xato.</p>
<pre>=SUMIFS(Amount; Region; "Toshkent"; Month; 3)
=COUNTIFS(Status; "Paid"; Channel; "Online")
=AVERAGEIFS(Score; Team; "A"; Score; "&gt;0")</pre>
<p>COUNTIFS — nechta qator. AVERAGEIFS — o‘rtacha, lekin shartga moslar. AVERAGEIFS da 0 ballni tashlamoqchi bo‘lsangiz, <code>"&gt;0"</code> kabi mezon qo‘shing — aks holda nol o‘rtachani tortadi.</p>

<table>
  <tr><th>Region</th><th>Month</th><th>Channel</th><th>Status</th><th>Amount</th></tr>
  <tr><td>Toshkent</td><td>3</td><td>Online</td><td>Paid</td><td>1200000</td></tr>
  <tr><td>Toshkent</td><td>3</td><td>Do‘kon</td><td>Paid</td><td>400000</td></tr>
  <tr><td>Samarqand</td><td>3</td><td>Online</td><td>Paid</td><td>800000</td></tr>
</table>
<p>“Toshkent + mart + online + paid” — bitta qator, 1 200 000. Formula to‘rt shartni birga qo‘yadi. Table nomlari bilan:</p>
<pre>=SUMIFS(tbl_Sales[Amount]; tbl_Sales[Region]; "Toshkent"; tbl_Sales[Month]; 3; tbl_Sales[Channel]; "Online"; tbl_Sales[Status]; "Paid")</pre>

<p>Pivot vs SUMIFS. Tez ad-hoc, 2–3 kesim, katakda yashashi kerak bo‘lgan son — SUMIFS. Ko‘p o‘q, o‘yinchoq kabi aylantirish, foizlar — PivotTable. Ikkalasini biling. SUMIFS ni report_ varag‘iga yozib qo‘yasiz — manba Table bo‘lsa, yangi qator o‘zi kiradi.</p>

<p>Mezon matnini aniq yozing: <code>Toshkent</code> va <code>Toshkent </code> (oxirida bo‘shliq) — ikki xil. Tozalash darsi shu yerda qaytadi. Keyin xatolar: #N/A ni 0 deb yutib yubormang, avval nima buzilganini ko‘ring.</p>
""",
    "excel-errors": """
<p>Ko‘p odam shu yerda adashadi: hisobotda <code>#N/A</code> ko‘rinsa, rahbar “Excel buziq” deydi. Shuning uchun hamma narsani <code>IFERROR(...,0)</code> ga o‘raydi. Xato yo‘qoladi. Sabab ham yo‘qoladi. Debug paytida xatoni yashirmang.</p>

<p>Uchrashadigan yuzlar:</p>
<ul>
  <li><code>#N/A</code> — qidiruv topilmadi (XLOOKUP, VLOOKUP, MATCH)</li>
  <li><code>#DIV/0!</code> — nolgacha bo‘lish. AOV = Revenue / Orders, buyurtma 0 bo‘lsa</li>
  <li><code>#VALUE!</code> — tur aralash: matn + son, noto‘g‘ri argument</li>
  <li><code>#REF!</code> — o‘chirilgan katakga havola</li>
  <li><code>#NAME?</code> — funksiya nomi xato yoki til/qavs</li>
</ul>

<pre>=IFERROR(VLOOKUP(A2;tbl_Map;2;FALSE);0)
=IFNA(XLOOKUP(A2;tbl_Map[ID];tbl_Map[Name]);"Topilmadi")
=IF(C2=0;"—";B2/C2)</pre>
<p><code>IFNA</code> faqat #N/A ni tutadi. Boshqa xato oshkora qoladi — bu yaxshi. <code>IFERROR</code> hammasi yutadi, jumladan #DIV/0! va #VALUE!. Hisobotda ba’zan kerak, modelda kamroq.</p>

<table>
  <tr><th>Vaziyat</th><th>Yaxshi javob</th><th>Yomon odat</th></tr>
  <tr><td>Mahsulot ID yo‘q</td><td>"NO_MATCH" yoki status ustuni</td><td>Jim 0 — go‘yo narx bepul</td></tr>
  <tr><td>Bo‘lish, maxraj 0</td><td>"—" yoki bo‘sh, alohida izoh</td><td>IFERROR bilan 0, o‘rtacha buziladi</td></tr>
  <tr><td>Hali yozayotgan formula</td><td>Xato ko‘rinsin</td><td>Darhol IFERROR</td></tr>
</table>

<p>0 bilan #N/A ni aralashtirmang. “Topilmadi” va “narxi nol so‘m” — turli biznes. Flag ustuni: Found / Missing. Keyin SUMIFS faqat Found larni oladi.</p>

<p>Samarqand omborida narx ro‘yxatida yo‘q SKU. IFERROR 0 qilsangiz, chegirma emas — yolg‘on bepul. Avval Missing ni sanang, keyin biznesga qo‘ng‘iroq. Qidiruv moduliga o‘tamiz: avval XLOOKUP — zamonaviy standart.</p>
""",
    "excel-xlookup": """
<p>SQL da JOIN bor edi: kalit bo‘yicha ismni boshqa jadvaldan olib kelish. Excelda yillar davomida odamlar VLOOKUP yozishgan. Yangi standart — <strong>XLOOKUP</strong>. Chapga ham qaytaradi, “topilmasa nima” ni o‘zi so‘raydi, ustun raqamini sanamaysiz.</p>

<p>O‘qish tartibi: nima qidiramiz, qayerda qidiramiz, nima qaytaramiz. Ixtiyoriy: topilmasa, moslik turi, qidiruv yo‘nalishi.</p>
<pre>=XLOOKUP(lookup_value; lookup_array; return_array; [if_not_found]; [match_mode]; [search_mode])

=XLOOKUP(A2; tbl_Customers[CustomerID]; tbl_Customers[Name]; "Topilmadi")
=XLOOKUP([@ProductID]; tbl_Price[ProductID]; tbl_Price[Price]; "NO_MATCH")</pre>

<p>Biznes. Orders da OrderID va CustomerID bor, ism yo‘q. Customers da ID va Name. XLOOKUP — har buyurtma yoniga ism. Price list: ProductID → Price. HR: tabel raqami → lavozim.</p>
<table>
  <tr><th>OrderID</th><th>CustomerID</th><th>Name (XLOOKUP)</th></tr>
  <tr><td>501</td><td>12</td><td>Ali Valiyev</td></tr>
  <tr><td>502</td><td>99</td><td>Topilmadi</td></tr>
</table>
<p>99 yo‘q bo‘lsa, hisobotda ochiq yoziladi. IFERROR(0) qilsangiz, go‘yo “nomsiz nol” — tahlilchiga yomon.</p>

<p>Afzalliklar, qisqa: return_array chapda ham bo‘lishi mumkin (VLOOKUP buni yoqtirmasdi). Ustun qo‘shilsada col_index buzilmaydi — nom bilan ishlaysiz. <code>match_mode</code> 0 — aniq moslik, odatda shu. Taxminiy moslikni faqat tartiblangan sonlar/sanalar uchun, ongli ravishda.</p>

<p>Eski Excel (2016 va oldin) da XLOOKUP yo‘q. Shuning uchun keyingi dars: INDEX + MATCH. Intervyuda ham, meros fayllarda ham hali yashaydi. Yangi varaqda — XLOOKUP.</p>
""",
    "excel-index-match": """
<p>XLOOKUP yo‘q noutbuk ochdingiz, yoki ikki o‘qli qidiruv kerak: “shu mahsulot, shu oy — narx”. Ikki funksiya sherik: <strong>MATCH</strong> qator raqamini topadi, <strong>INDEX</strong> o‘sha joydagi qiymatni oladi.</p>

<p>MATCH: “Ali qayerda?” — 4-qator. INDEX: “Ismlar ro‘yxatining 4-si nima?”. Birga:</p>
<pre>=INDEX(return_range; MATCH(key; key_range; 0))

=INDEX(tbl_Customers[Name]; MATCH(A2; tbl_Customers[CustomerID]; 0))
=INDEX(C2:G10; MATCH(A2; B2:B10; 0); MATCH(B1; C1:G1; 0))</pre>
<p>Oxirgi qator — 2D: qator bo‘yicha mahsulot, ustun bo‘yicha oy. XLOOKUP odatda bitta o‘q; INDEX ikkita MATCH ni yutadi.</p>

<p>Uchinchi argument — <code>match_type</code>. Aniq qidiruv uchun <strong>0</strong>. 1 va -1 taxminiy, diapazon tartiblangan bo‘lishi shart. Tartibsiz ID larda 1 qo‘ysangiz, “deyarli o‘xshash” noto‘g‘ri odamni berishi mumkin. Ko‘p odam shu yerda adashadi.</p>
<table>
  <tr><th>match_type</th><th>Ma’no</th><th>Qachon</th></tr>
  <tr><td>0</td><td>Aniq tenglik</td><td>ID, kod, ism — deyarli doim</td></tr>
  <tr><td>1</td><td>Kichik yoki teng, taxminiy</td><td>Tartiblangan son, ongli</td></tr>
  <tr><td>-1</td><td>Katta yoki teng, taxminiy</td><td>Kam, tartib teskari</td></tr>
</table>

<p>Nima uchun hali kerak? Eski fayllar. Array senariylari. Ba’zi odamlar INDEX/MATCH ni “ustun siljisa ham yashaydi” deb VLOOKUP dan afzal ko‘rishgan — XLOOKUP chiqqach, yangi ishda XLOOKUP qisqaroq. Lekin MATCH 0 ni unutmang. Keyingi darsda VLOOKUP ning cheklovlarini ochiq aytamiz — o‘chirish uchun emas, tushunish uchun.</p>
""",
    "excel-vlookup": """
<p>Ofisda hali ham VLOOKUP yoziladi. Eski modelni buzmasdan ishlating. Yangi varaqda XLOOKUP. Lekin VLOOKUP ni tushunmasangiz, meros faylni tuzata olmaysiz. Cheklovlari esa xavfli — shuning uchun alohida dars.</p>

<p>G‘oya: chapdagi kalitni qidir, o‘ngdagi N-ustunni qaytar. <code>FALSE</code> (yoki 0) — aniq moslik. Buni yozmasangiz, default taxminiy — tartibsiz ID da tasodifiy juftlik.</p>
<pre>=VLOOKUP(A2; Table; 3; FALSE)
=VLOOKUP([@ProductID]; tbl_Price; 4; FALSE)</pre>
<p><code>3</code> — “jadvalning uchinchi ustuni”. Ertaga o‘rtaga yangi ustun qo‘shsangiz, 3 endi boshqa narsa. Hisobot jim buziladi. XLOOKUP da bunday indeks yo‘q.</p>

<table>
  <tr><th>Muammo</th><th>Nima bo‘ladi</th><th>Yechim yangi ishda</th></tr>
  <tr><td>Qidiruv ustuni chapda bo‘lishi shart</td><td>Ismdan ID olish qiyin</td><td>XLOOKUP / INDEX-MATCH</td></tr>
  <tr><td>col_index raqami</td><td>Ustun qo‘shilsa formula yolg‘on</td><td>Nomlangan ustun</td></tr>
  <tr><td>range_lookup default TRUE</td><td>Noto‘g‘ri yaqin ID</td><td>Doim FALSE, yoki XLOOKUP</td></tr>
</table>

<p>Toshkentdagi do‘kon: narxlar jadvali. Mahsulot kodi B ustunida, narx A da — VLOOKUP ishlamaydi, chunki “chapga qaramaydi”. Jadvallarni kesib-qo‘yish — yomon odat. Funksiyani almashtirish — to‘g‘ri.</p>

<p>Migratsiya: ishlayotgan dashboardni bir kechada qayta yozmang. Yangi calc varag‘ida XLOOKUP. Parallel tekshiruv: eski VLOOKUP va yangi — bir xilmi? Keyin almashtirasiz. Matn funksiyalariga o‘tamiz — kodlardan parcha olish, SKU ni bo‘laklash.</p>
""",
    "excel-text-fn": """
<p>SKU <code>UZ-TSH-041</code> — bitta katak. Ichida esa uch xil ma’lumot: mamlakat, kategoriya, model. Tahlilchi “futbolkalar savdosi” desa, butun SKU ni guruhlamaydi — o‘rtadagi qismni ajratadi. Matn funksiyalari shu ish.</p>

<p>LEFT — boshidan N belgi. RIGHT — oxiridan. MID — o‘rtadan: qayerdan, nechta. UPPER / LOWER / PROPER — bir xil yozuv: <code>toshkent</code> va <code>Toshkent</code> filtrlarda ikki shahar bo‘lib ketmasin.</p>
<pre>=LEFT(A2;2)
=RIGHT(A2;3)
=MID(A2;4;3)
=UPPER(B2)
=LOWER(B2)
=PROPER(B2)
=TEXTJOIN(", ";TRUE; C2:C5)
=LEN(A2)
=FIND("-";A2)</pre>
<p><code>TEXTJOIN</code> — bir nechta katakni vergul bilan, bo‘shlarini tashlab. Telefonlar, teglar, manzil qismlari.</p>

<table>
  <tr><th>SKU</th><th>LEFT 2</th><th>MID 4,3</th><th>RIGHT 3</th></tr>
  <tr><td>UZ-TSH-041</td><td>UZ</td><td>TSH</td><td>041</td></tr>
  <tr><td>UZ-SHS-210</td><td>UZ</td><td>SHS</td><td>210</td></tr>
</table>
<p>Chiziq joyi siljisa, FIND bilan dinamik: avval birinchi <code>-</code> ni topasiz, keyin MID. Qattiq 4,3 faqat format barqaror bo‘lsa. Flash Fill ba’zan yordam beradi, lekin yangi qatorda “sehr” ishlamasligi mumkin — formula ishonchliroq.</p>
<pre>=LEFT(A2;FIND("-";A2)-1)
=TRIM(PROPER(D2))</pre>

<p>Biznes: telefonni bir xillashtirish — bo‘shliq, qavs, <code>+998</code>. SUBSTITUTE zanjiri. HR da F.I.SH ni PROPER. Bankda dokument raqamining oxirgi 4 belgisini RIGHT. Tozalash darsidagi TRIM shu yerda ham birinchi qadam. Keyin sanalar — matn emas, serial.</p>
""",
    "excel-date-fn": """
<p>Sana Excelda rasm emas. Bu — serial number. 1-yanvar 1900 dan boshlab kunlar (Excelning o‘z qoidasi). Shuning uchun <code>TODAY()-OrderDate</code> “necha kun” beradi. Matn <code>01.02.2024</code> esa ayirishni bilmaydi — avval turga o‘tkazing.</p>

<p>Yil, oy, kun ajratish — hisobot o‘qi. EOMONTH — shu oyning oxirgi kuni (ish haqi, yopilish). EDATE — N oy oldinga/orqaga. NETWORKDAYS — dam olishlarsiz ish kunlari, SLA uchun. TODAY — bugun, har ochilganda yangilanadi.</p>
<pre>=YEAR(A2)
=MONTH(A2)
=DAY(A2)
=EOMONTH(A2;0)
=EDATE(A2;1)
=NETWORKDAYS(start; end)
=NETWORKDAYS(start; end; tbl_Holidays[Date])
=TODAY()
=DATEVALUE(A2)</pre>
<p>Bayramlar jadvali NETWORKDAYS ning uchinchi argumenti. Aks holda 8-martni ish kuni deb sanaydi.</p>

<table>
  <tr><th>Funksiya</th><th>Savol</th><th>Misol</th></tr>
  <tr><td>YEAR / MONTH</td><td>Qaysi oyda sotdik?</td><td>Pivot uchun oy ustuni</td></tr>
  <tr><td>EOMONTH</td><td>Oy yakuni qachon?</td><td>Byudjet yopilishi</td></tr>
  <tr><td>NETWORKDAYS</td><td>Necha ish kuni?</td><td>Yetkazib berish SLA</td></tr>
  <tr><td>TODAY</td><td>Hozir qancha kechikkan?</td><td>Aging, churn</td></tr>
</table>

<p>Matn sanani DATEVALUE yoki Power Query Change Type bilan konvert qiling. Kun/oy almashtirish (AQSH vs Yevropa) — Toshkent fayllarida ham uchraydi. 03/04/2026 martmi yoki aprelmi? Locale ni tekshiring, taxmin qilmang.</p>

<p>Rolling 30 kun: <code>=A2&gt;=TODAY()-30</code>. Ish kuni bilan oddiy kun farqini aralashtirmang: kuryer SLA odatda NETWORKDAYS, “necha kalendar kun o‘tdi” esa oddiy ayirma. Keyingi dars — shu ayirmadan aging bucket: 0–29, 30–59, 60+.</p>
""",
    "excel-order-age": """
<p>Keling, haqiqiy vazifa. Do‘konning buyurtmalari bor. Rahbar: “Qancha pul 60 kundan oshiq yotibdi?” Debitorlik, ombor zaxirasi, churn — aging tahlili klassikasi. Yangi sehr yo‘q: sana ayirmasi + IF/IFS.</p>

<p>Yosh kunlarda: bugun minus buyurtma sanasi. Table da:</p>
<pre>=TODAY()-[@OrderDate]</pre>
<p>Musbat son — o‘tgan kunlar. Manfiy chiqsa, kelajakdagi sana yoki noto‘g‘ri tur. Avval OrderDate haqiqiy sanami, tekshiring.</p>

<p>Bucket. Chegaralarni pastdan yuqoriga, ketma-ket. Avval 30 ni qo‘ymasangiz, 10 ham “60+” ga tushishi mumkin — IF tartibi muhim, SQL CASE kabi.</p>
<pre>=IFS([@AgeDays]&lt;30;"0-29";[@AgeDays]&lt;60;"30-59";TRUE;"60+")
=IF([@AgeDays]&lt;30;"0-29";IF([@AgeDays]&lt;60;"30-59";"60+"))</pre>

<table>
  <tr><th>OrderID</th><th>OrderDate</th><th>AgeDays</th><th>Bucket</th><th>Amount</th></tr>
  <tr><td>801</td><td>2026-08-01</td><td>18</td><td>0-29</td><td>350000</td></tr>
  <tr><td>802</td><td>2026-06-20</td><td>60</td><td>60+</td><td>2100000</td></tr>
  <tr><td>803</td><td>2026-07-15</td><td>35</td><td>30-59</td><td>900000</td></tr>
</table>
<p>Keyin COUNTIFS / SUMIFS: har bucket nechta, qancha so‘m. Yoki Pivot: Rows = AgingBucket, Values = SUM Amount. report_Aging varag‘iga shu jadval.</p>
<pre>=COUNTIFS(tbl_Orders[AgingBucket];"60+")
=SUMIFS(tbl_Orders[Amount]; tbl_Orders[AgingBucket];"60+"; tbl_Orders[Region];"Toshkent")</pre>

<p>Churn flag ham shu oiladan: <code>=IF([@LastOrder]&lt;TODAY()-90;1;0)</code>. 1 va 0 ni qo‘shish — nechta xavf ostida. TODAY har ochilganda siljiydi — faylni kecha yuborgan “yosh” bugun boshqacha bo‘lishi mumkin. Snapshot kerak bo‘lsa, sanani qiymat qilib qo‘ying. Pivotga o‘tamiz: bucketlarni sichqoncha bilan kesamiz.</p>
""",
    "excel-pivot-base": """
<p>SUMIFS yozib charchadingiz. Har yangi kesim — yangi formula. PivotTable boshqa yo‘l: qatorlarni sudrab, “har region, har oy — yig‘indi” ni soniyalarda olasiz. Katta jadvalni tez kesish — tahlilchining noni.</p>

<p>Maydonlar to‘rt quti. <strong>Rows</strong> / <strong>Columns</strong> — o‘qlar, guruh kalitlari. <strong>Values</strong> — SUM, COUNT, AVERAGE. <strong>Filters</strong> (yoki slicer) — sahifa filtri: faqat Online, faqat 2026. SQL dagi GROUP BY + aggregat, lekin sichqoncha bilan.</p>

<p>Qoida: manba — Excel Table. Merge katak, ikki qatorli sarlavha — Pivot kasal bo‘ladi. Ma’lumot yangilansa — Pivot ni Refresh. Calculated Field ehtiyot: murakkab mantiqni calc ustunida qiling, Pivotda emas.</p>
<table>
  <tr><th>Quti</th><th>Misol</th><th>Natija</th></tr>
  <tr><td>Rows</td><td>Region</td><td>Toshkent, Samarqand, …</td></tr>
  <tr><td>Columns</td><td>Month</td><td>Yan, Fev, Mart, …</td></tr>
  <tr><td>Values</td><td>Sum of Amount</td><td>har kesimda so‘m</td></tr>
  <tr><td>Values (2)</td><td>Count of OrderID</td><td>buyurtmalar soni</td></tr>
</table>
<p>Biznes: Region × Month bo‘yicha Revenue; yonida Count of Orders. AOV ni Pivotda to‘g‘ridan-to‘g‘ri “o‘rtacha amount” bilan almashtirmang — ba’zan Average of Amount chek o‘rtachasi, ba’zan esa keraklisi Revenue/Orders. Savolni aniqlang.</p>
<pre>Manba: tbl_Sales (Table)
Insert → PivotTable → New worksheet
Rows: Region
Columns: Month
Values: Sum of Amount, Count of OrderID</pre>

<p>OrderID ni Values ga tashlasangiz, odatda COUNT kerak, SUM emas. ID larni qo‘shish ma’nosiz. Keyingi darsda Values ni foizga, running totalga aylantiramiz — “ulush” savoli.</p>
""",
    "excel-pivot-values": """
<p>Pivotda SUM yetarli emas. Rahbar: “Toshkent umumiydan necha foiz?” “O‘tgan oyga nisbatan?” “Yil boshidan yig‘ilib boryaptimi?” Bular Value Field Settings ichida: Show Values As.</p>

<p>Foydali ko‘rinishlar. % of Grand Total — ulush. % of Row Total / Column Total — qator yoki ustun ichidagi ulush. Difference From / % Difference From — oldingi oy, oldingi yil. Running Total In — yil boshidan o‘sish. Bir metrikani ikki marta tashlashingiz mumkin: birinchisi so‘m, ikkinchisi foiz.</p>
<table>
  <tr><th>Ko‘rinish</th><th>Savol</th></tr>
  <tr><td>% of Grand Total</td><td>Regionning umumiy savdodagi ulushi</td></tr>
  <tr><td>% Difference From (previous Month)</td><td>O‘sish yoki tushish</td></tr>
  <tr><td>Running Total In Month</td><td>Yanvardan beri yig‘indi</td></tr>
  <tr><td>Count of OrderID</td><td>Nechta chek, pul emas</td></tr>
</table>

<p>Xato: Values ga OrderID qo‘yib SUM. Yoki City ni SUM. Matn va ID — COUNT yoki DISTINCT COUNT (Excel versiyasiga bog‘liq). Distinct Count Data Model / Add to data model orqali chiqishi mumkin. Oddiy Pivotda COUNT qatorlar soni — bir mijoz 5 buyurtma bo‘lsa 5.</p>
<pre>Value Field Settings → Summarize by: Sum / Count / Average
Show Values As → % of Grand Total
Show Values As → % Difference From → Month → (previous)</pre>

<p>Foizni yozganda asos nima ekanini ayting. “12%” — nimadan? Grand totalmi, Toshkent qatorimi? Hisobotda bitta qavs ichida yozing: <em>ulush, jami savdodan</em>.</p>

<p>Toshkent 40%, Samarqand 15% — bu yomonlik emas, hajm. O‘sish foizi boshqa savol: Samarqand o‘tgan oyga +30% bo‘lishi mumkin, Toshkent esa −2%. Ikkalasini bitta Pivotda yonma-yon qo‘ying. Slicer va grafik keyingi dars — foizni ko‘rsatish, lekin pie bilan 12 regionni tiqmaslik.</p>
""",
    "excel-pivot-slicer": """
<p>Rahbar sichqoncha bilan o‘ynashni yaxshi ko‘radi. “Faqat Online ko‘rsat. Endi Toshkent. Endi mart.” Har safar Pivot filtrini ochish — sekin. <strong>Slicer</strong> — katta tugmalar: Channel, Region. Bosildi, barcha bog‘langan Pivotlar birga filtrlanadi.</p>

<p>Insert → Slicer. Keyin Report Connections (yoki Pivot Connections): bir slicer ni ikki-uch Pivotga bog‘lang. Aks holda grafik yangilanadi, yonidagi jadval eski qoladi — ishonchsizlik. Timeline — sanalar uchun, oy/kvartal tugmasi.</p>
<table>
  <tr><th>Vosita</th><th>Nima qiladi</th></tr>
  <tr><td>Slicer</td><td>Diskret ro‘yxat: kanal, viloyat, brend</td></tr>
  <tr><td>Timeline</td><td>Vaqt o‘qi</td></tr>
  <tr><td>Report Connections</td><td>Bir filtr — ko‘p Pivot</td></tr>
  <tr><td>PivotChart</td><td>Shu Pivotning grafigi, filtrlar ulashgan</td></tr>
</table>

<p>Chart turini xabarga moslang. Ulush — ko‘pincha bar aniqroq; pie faqat 2–4 bo‘lak, nomlari qisqa. Trend — line. Taqqos — clustered column. 3D pie — yo‘q. Ranglar CF dagi qoida: ma’no, bezak emas.</p>
<pre>PivotChart: clustered column
O‘q: Month
Ustunlar: Sum of Amount
Slicer: Channel (Online / Do‘kon)
Ikkinchi Pivot: Rows = Region, Values = % of Grand Total
Ikkalasi bir Channel slicer ga bog‘langan</pre>

<p>Bir nechta Pivotni bir slicer ga bog‘lamasangiz, “hisobot yolg‘on gapiryapti” degan shikoyat chiqadi. Bosqich: avval bitta Pivotda slicer, ishlasa ikkinchisini ulash. Hammasini birga ulab, keyin “nima uchun bo‘sh?” deb o‘tirmang.</p>

<p>Dashboardga o‘tishdan oldin: slicer ishlayaptimi, Refresh qildingizmi, manba Table mi. Power Query — oylik CSV ni qo‘lda yopishtirishni to‘xtatadi. Avval “nima ekani”, keyin Merge.</p>
""",
    "excel-pq-intro": """
<p>Har oy bir xil CSV. Har safar qo‘lda TRIM, tur, ustun nomlari. Birinchi oy ishladi. Uchinchi oy kimdir “Amount” ni “Сумма” qilib yubordi — formulalar o‘ldi. Power Query shu takroriy tozalashni yozib qo‘yadi. Refresh — qadamlar qayta yuguradi.</p>

<p>Bu — UI. Orqada M tili turadi, hozir yodlash shart emas. Siz qadamlarni ko‘rasiz: o‘ng panel, Applied Steps. Birini o‘chirsangiz, zanjir orqaga qaytadi. SQL dagi CTE kabi: bosqichma-bosqich, nomlangan.</p>

<p>Oqim, oddiy:</p>
<ol>
  <li>Data → Get Data → fayl, papka, yoki boshqa workbook</li>
  <li>Transform: tur, split, filter, group, ustun nomlari</li>
  <li>Close &amp; Load — varaqqa jadval, yoki Connection Only (faqat keyin Merge uchun)</li>
</ol>
<pre>Get Data → From Text/CSV → sales_2026_03.csv
Applied Steps:
  Source
  Promoted Headers
  Changed Type
  Filtered Rows (bo‘sh OrderID yo‘q)
  Trimmed Text
Close &amp; Load → tbl_Fact</pre>

<table>
  <tr><th>Qo‘lda Excel</th><th>Power Query</th></tr>
  <tr><td>Har oy Copy-Paste</td><td>Bir marta sozlash, Refresh</td></tr>
  <tr><td>TRIM formulasi yuz ustunda</td><td>Transform → Format → Trim</td></tr>
  <tr><td>Xato qayerda — izla</td><td>Qadamni tekshir, keyingisini qo‘sh</td></tr>
</table>

<p>Load qilganda “raw ni bosib ketmang”. Query natijasi alohida varaq yoki data model. Xom CSV papkada qolsin.</p>

<p>Refresh ni o‘zingiz bosing, avtomatikga ishonib yubormang — manba yo‘li o‘zgargan bo‘lishi mumkin. Qadam xato bersa, oxirgisini o‘chiring, oldingisini tekshiring. Butun zanjirni boshidan yozish shart emas. Keyingi dars: 12 oy faylni vertikal yig‘ish (Append) va mijoz jadvali bilan kalit bo‘yicha (Merge) — JOIN/UNION g‘oyasi.</p>
""",
    "excel-pq-merge": """
<p>SQL dagi JOIN va UNION ni eslang. Power Query da ikki tugma: <strong>Append</strong> va <strong>Merge</strong>. Append — bir xil ustunli jadvallarni ostma-ost (oylik CSV lar). Merge — kalit bo‘yicha yonma-yon (Order + Customer).</p>

<p>Append. Yanvar va fevral, ustunlar bir xil: OrderID, Date, Amount. Natija — uzun fact. Ustun nomi farq qilsa, Query bo‘sh ustun yoki chalkashlik beradi. Avval nomlarni bir xillashtiring. 12 oy: papkadan Get Data → From Folder, keyin Combine — Append ning avtomati.</p>
<pre>Append Queries:
  tbl_Jan
  tbl_Feb
→ tbl_Sales_YTD

From Folder:
  C:\\data\\sales\\*.csv
  Combine &amp; Transform</pre>

<p>Merge. Left Outer — chapdagi barcha buyurtmalar, mijoz topilmasa Name NULL (Excelda null, bo‘sh). Inner — faqat mos kelganlar. Right, Full — kamroq, lekin bor. Kalit: CustomerID = CustomerID, turlar bir xil bo‘lsin (ikkala tomon matn yoki ikkala son).</p>
<table>
  <tr><th>Merge turi</th><th>SQL analogi</th><th>Qachon</th></tr>
  <tr><td>Left Outer</td><td>LEFT JOIN</td><td>Barcha orderlar, mijoz bo‘lsa ism</td></tr>
  <tr><td>Inner</td><td>INNER JOIN</td><td>Faqat to‘liq juftlik</td></tr>
  <tr><td>Anti (left)</td><td>LEFT … WHERE NULL</td><td>Mijozsiz buyurtmalar — sifat nazorati</td></tr>
</table>
<pre>Merge:
  Left: tbl_Orders
  Right: dim_Customer
  On: CustomerID
  Join Kind: Left Outer
  Expand: Name, City, Segment</pre>

<p>Biznes: 12 oy → Append → bitta fact. Keyin dim_Customer bilan Merge. Expand qilganda kerakli ustunlarni oling, butun o‘ng jadvalni emas — fayl shishadi.</p>

<p>Kalit turi farq qilsa (chapda matn <code>0012</code>, o‘ngda son 12) — Merge “topilmadi” deydi, go‘yo mijoz yo‘q. Avval ikkala tomonda Change Type. Keyingi dars aynan shu: locale va xato qatorlar.</p>
""",
    "excel-pq-types": """
<p>Power Query ishladi, lekin Amount bo‘sh yoki Error. Ko‘p odam shu yerda adashadi: Excel varag‘ida vergul, Query esa nuqta kutadi. O‘zbekiston CSV lari ko‘pincha <code>;</code> ajratgich, kasr vergul. Locale — bu “qaysi mamlakat qoidasi bilan o‘qi”.</p>

<p>Change Type. Avval to‘g‘ri locale: Uzbek (or Russian) vs English. <code>1 234,56</code> English locale da matn yoki error. Changed Type qadamini ochib, Using Locale ni tanlang. Separator ni Get Data dialogida ham belgilaysiz: semicolon.</p>
<pre>Changed Type (Using Locale):
  Amount → Decimal Number, locale: Uzbek / Russian
  OrderDate → Date, locale: ...
Replace Errors → null  yoki  0 (biznesga qarab)
Remove Errors → qator ketadi (ehtiyot: yo‘qolgan savdo)</pre>

<table>
  <tr><th>Belgi</th><th>Ko‘rinish</th><th>Nima qilish</th></tr>
  <tr><td>1.234,56</td><td>ming nuqta, kasr vergul</td><td>Locale Yevropa / RU / UZ</td></tr>
  <tr><td>1,234.56</td><td>ming vergul, kasr nuqta</td><td>Locale US / UK</td></tr>
  <tr><td>1234,56 va 1234.56 aralash</td><td>iflos fayl</td><td>Avval Replace, keyin tur</td></tr>
  <tr><td>Error katak</td><td>sariq / error</td><td>Replace Errors yoki manbani tuzatish</td></tr>
</table>

<p>Sana ham shu tuzoqda. <code>31.02.2024</code> yoki <code>noma’lum</code> aralashsa, Changed Type error beradi. Avval shartli ustun: “o‘qiladimi?”, keyin filter. Hammasini Date qilib umid qilmang.</p>

<p>Remove Errors qatorni butunlay olib tashlaydi. Katta Amount error bo‘lsa, savdo “yo‘qoladi”, Pivot xursand, moliya emas. Avval Replace Errors bilan flag yoki null, hisobotda “nechta qator o‘qilmadi” ni yozing.</p>

<p>Modelga chiqishdan oldin: Amount — decimal, Date — date, ID — matn (boshidagi 0 saqlansin). Shundan keyin dashboard. Chiroyli grafik iflos tur ustida — yolg‘on ishonch.</p>
""",
    "excel-dash-principles": """
<p>Dashboard bezak emas. Bitta ekran: hozir nima bo‘lyapti, nima uchun, keyin nima qilamiz. Rahbar 20 soniyada yo‘nalish olsin. 12 ta 3D pie — yo‘nalish emas, shovqin.</p>

<p>Tuzilma, ishda ishlaydigan:</p>
<ol>
  <li>Header: qaysi davr, qaysi filtr (slicer), yangilangan sana</li>
  <li>KPI qatori — 3–5 ta, ko‘pi emas</li>
  <li>Asosiy trend yoki taqqos (oylar, reja vs fakt)</li>
  <li>Detal: Pivot yoki top-10 jadval — “nima uchun KPI tushdi”</li>
</ol>
<p>Har bir vizual bitta savolga javob bersin. “Hamma narsa bitta grafikda” — hech narsa ko‘rinmaydi.</p>

<table>
  <tr><th>Qism</th><th>Savol</th><th>Vosita</th></tr>
  <tr><td>KPI</td><td>Bu oy qancha?</td><td>Katta son, oldingi oyga Δ</td></tr>
  <tr><td>Trend</td><td>Qayerga ketayapti?</td><td>Line / column</td></tr>
  <tr><td>Kesim</td><td>Kim aybdor / qahramon?</td><td>Bar, Pivot</td></tr>
  <tr><td>Filtr</td><td>Faqat Toshkent?</td><td>Slicer, bog‘langan</td></tr>
</table>
<pre>Layout (bitta sahifa):
[ Davr: 2026-YTD ] [ Channel slicer ] [ Region slicer ]
[ Revenue ] [ Orders ] [ AOV ] [ 60+ aging % ]
[ Oylik trend — column ]
[ Region ulushi — bar ]     [ Top mahsulotlar — jadval ]</pre>

<p>Rang — ma’no. Qizil = xavf yoki reja ostida. Yashil = maqsad. Kulrang = kontekst. Har kategoriya o‘z random rangi — yo‘q. CF darsini eslang: stakeholder sahifasida minimal.</p>

<p>Bir sahifa, chop etilsa ham o‘qiladigan. Scroll qilish kerak bo‘lsa — bu allaqachon ikkinchi hisobot. Bankdagi savdo rahbari telefonida ham tepadagi KPI ni ko‘rsin. Keyingi dars: qaysi KPI umuman kerak — vanity emas, qaror.</p>
""",
    "excel-kpi": """
<p>“Saytga 12 ming kirdi” — chiroyli. Qaror bormi? Ko‘pincha yo‘q. Vanity metric. Tahlilchi qaror metric tanlaydi: pul, marja, qaytish, xavf. Avval biznes savoli, keyin formula.</p>

<p>Savdo uchun uchlik: Revenue (qancha pul), Orders (nechta chek), AOV (o‘rtacha chek). AOV o‘ssa, odam qimmatroq oladi yoki savat katta. Orders o‘ssa, oqim bor. Faqat Revenue — aralash hikoya.</p>
<pre>AOV = Revenue / Orders
=IF(Orders=0;"—";Revenue/Orders)

Yo‘qolgan mijoz flag =
=IF([@LastOrder]&lt;TODAY()-90;1;0)

Churn_risk_soni = SUM(flag)
Retention ≈ qaytgan mijozlar / avvalgi davr faollari</pre>
<p>Margin — moliyaviy: (Revenue − Cost) / Revenue. Cost yo‘q bo‘lsa, “foyda” deb Revenue ni ko‘rsatmang. Conversion — agar qadamlar bo‘lsa (tashrif → savat → to‘lov). Yo‘q bo‘lsa, uydirma conversion yozmang.</p>

<table>
  <tr><th>KPI</th><th>Nima uchun</th><th>Tuzoq</th></tr>
  <tr><td>Revenue</td><td>Hajm</td><td>Chegirma, qaytarish kiritilmagan</td></tr>
  <tr><td>Orders</td><td>Faollik</td><td>Bekor qilingan status</td></tr>
  <tr><td>AOV</td><td>Chek sifati</td><td>0 ga bo‘lish; ulkan bitta chek</td></tr>
  <tr><td>Aging 60+ %</td><td>Pul yotishi</td><td>Bucket chegarasi o‘zgarsa taqqos buziladi</td></tr>
  <tr><td>Sahifa ko‘rishlari</td><td>Ko‘pincha vanity</td><td>Qarorga ulanmasa — KPI qatoriga qo‘ymang</td></tr>
</table>

<p>3–5 ta. Har birida: joriy son, oldingi davr, maqsad (bor bo‘lsa). Flag 1/0 ni SUM qilish — COUNTIFS o‘rniga ham ishlaydi.</p>

<p>HR misoli ham shu mantiq: “nechta odam ishlaydi” vanity bo‘lishi mumkin; “sinovdan o‘tganlar ulushi” yoki “bo‘sh o‘rin necha kun ochiq” — qaror. Savdo do‘konida: kassa tushumi, qaytarish foizi, 60+ debitor. Yakuniy darsda shu KPI larni zanjirga solamiz: raw dan insight gacha.</p>
""",
    "excel-final-case": """
<p>Kurs oxiri. Yangi sehr yo‘q. Ishdagi fayl odatda aralashma: tozalash, qidiruv, sana, Pivot, bir oz Query. Retail zanjir: savdo CSV + mijoz jadvali. Rahbariyat uch savol beradi — javob “men Pivot ochdim” emas, 5 jumla va tavsiya.</p>

<p>Savollar:</p>
<ol>
  <li>Qaysi region o‘syoqti?</li>
  <li>Qaysi kanal foydali (yoki hech bo‘lmaganda hajm vs AOV)?</li>
  <li>Qaysi mahsulotlar “og‘ir” zaxira / past aylanma — aging yoki sekin SKU?</li>
</ol>
<p>Toshkent o‘sishi mumkin, Samarqand AOV yuqori, do‘kon kanali marjasiz — uch xil xulosa, bitta fayl.</p>

<p>Sizning ish oqimingiz, ketma-ket. O‘tkazib yubormang:</p>
<pre>1) raw_  — CSV ni tegmasdan saqlash
2) Power Query — tur, TRIM, Append oylar, Merge mijoz
3) tbl_Fact — Table, toza turlar
4) calc_ — AgeDays, Bucket, Segment, XLOOKUP narx
5) Pivot + KPI + slicer — bitta sahifa
6) 5 jumla insight + 1–2 tavsiya (o‘zbekcha)</pre>
<table>
  <tr><th>Bosqich</th><th>Tekshiruv</th></tr>
  <tr><td>raw</td><td>Qatorlar soni manba bilan tengmi?</td></tr>
  <tr><td>PQ</td><td>Error qatorlar sanab yozildimi?</td></tr>
  <tr><td>Fact</td><td>SUM Amount “qo‘lda filtr” bilan bir xilmi?</td></tr>
  <tr><td>Dashboard</td><td>Har vizual bitta savolmi?</td></tr>
  <tr><td>Insight</td><td>Son + sabab + nima qilish?</td></tr>
</table>

<p>Yangi oy fayli keldi: darhol chart emas. raw → Query Refresh → model → KPI. Merge kataklar va VLOOKUP default TRUE — eskisi, qaytmang.</p>

<p>Keyingi qadam: shu modelni Power BI ga ko‘chirish. Excelda ishonchli fact jadvali bo‘lsa, migratsiya oson. Bo‘lmasa, BI ham axlatni chiroyli qiladi. Siz endi noldan: tur, Table, tozalash, IF, SUMIFS, qidiruv, matn/sana, aging, Pivot, Query, dashboard. Qolgani — haqiqiy CSV va aniq savol. Mashqda zanjirni o‘zingiz yurib chiqing.</p>
""",
}
