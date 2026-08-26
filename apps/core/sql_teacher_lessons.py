"""
SQL darslari — o‘qituvchi ovozida, noldan.
Har dars talaba bilan gaplashgandek yozilgan; bir xil qolip takrorlanmaydi.
"""

LECTURES = {
    "select-nima": """
<p>Salom. Agar siz hech qachon SQL yozmagan bo‘lsangiz — yaxshi. Shu darsdan boshlaymiz, hech narsa oldindan bilishingiz shart emas.</p>

<p>Ishda ma’lumot odatda Exceldagi kabi <strong>jadval</strong>da yotadi: qatorlar va ustunlar. Farqi shunda — bazada millionlab qator bo‘lishi mumkin, uni sichqoncha bilan filtrlash qiyin. Shuning uchun biz kompyuterga <em>oddiy tilda buyruq</em> beramiz: “Shu jadvaldan mana shu ustunlarni olib kel.”</p>

<p>O‘sha buyruq tili — <strong>SQL</strong>. To‘liq nomi Structured Query Language, ya’ni “tuzilgan so‘rov tili”. Qo‘rqitadigan nom, lekin amalda 2–3 ta so‘z bilan ish boshlanadi.</p>

<p>Bizning mashg‘ulotda bank misoli bor. Mijozlar <code>customers</code> jadvalida. Qarang, u qanday ko‘rinadi:</p>
<table>
  <tr><th>id</th><th>name</th><th>city</th></tr>
  <tr><td>1</td><td>Ali Valiyev</td><td>Toshkent</td></tr>
  <tr><td>2</td><td>Malika Karimova</td><td>Samarqand</td></tr>
  <tr><td>3</td><td>Javohir Saidov</td><td>Buxoro</td></tr>
</table>
<p>Gorizontal chiziq — <strong>qator</strong>: bitta odam. Vertikal — <strong>ustun</strong>: id, ism, shahar. Exceldagi “satr” va “ustun” bilan bir xil mantiq.</p>

<p>Endi eng muhim buyruq. “Menga ismlarni olib kel” deyish uchun yozamiz:</p>
<pre>SELECT name FROM customers;</pre>
<p>Buni o‘qish oson: <code>SELECT</code> — “tanla / olib kel”, <code>name</code> — qaysi ustun, <code>FROM customers</code> — qayerdan. Oxiridagi nuqtali vergul ko‘p joyda ixtiyoriy, lekin odatda qo‘yiladi.</p>
<p>Natija: Ali Valiyev, Malika Karimova, Javohir Saidov. Boshqa ustunlar chiqmaydi — chunki so‘ramadik.</p>

<p>Hamma narsani ko‘rmoqchi bo‘lsangiz, yulduzcha:</p>
<pre>SELECT * FROM customers;</pre>
<p><code>*</code> “barcha ustunlar” demak. O‘rganishda foydali. Keyinroq ishda aniq ustun yozishni o‘rganamiz — nima uchunligini keyingi darsda aytaman.</p>

<p>Yana bir narsa: SQL ni “o‘zgartirish tili” deb o‘ylamang. Bugungi <code>SELECT</code> faqat <strong>o‘qiydi</strong>. Jadvaldagi ma’lumot o‘chmaydi, buzilmaydi. Xotirjam mashq qiling.</p>

<p>Quyida shu so‘rovlarni ko‘rasiz. Keyin mashqda o‘zingiz yozasiz: jadvaldan faqat bitta ustunni oling. Birinchi muvaffaqiyat shu.</p>
""",
    "ustunlarni-tanlash": """
<p>Oldingi darsda <code>SELECT *</code> bilan butun jadvalni oldik. Bu “hamma narsani stolga to‘kish”. Hisobotda esa odatda 2–3 ta ustun kerak bo‘ladi.</p>

<p>Tasavvur qiling, rahbar so‘raydi: “Mijozlar qayerda yashaydi?” Unga <code>id</code> ham, ro‘yxatdan o‘tgan sana ham kerak emas. Keraklisi — ism va shahar.</p>
<pre>SELECT name, city FROM customers;</pre>
<p>Ustunlar <strong>vergul</strong> bilan yoziladi. Tartib ham siznik: avval <code>name</code> desangiz, natijada birinchi ustun ism bo‘ladi.</p>
<table>
  <tr><th>name</th><th>city</th></tr>
  <tr><td>Ali Valiyev</td><td>Toshkent</td></tr>
  <tr><td>Malika Karimova</td><td>Samarqand</td></tr>
</table>

<p>Nima uchun yulduzchani har doim ishlatmaslik kerak? Uchta sabab, oddiy tilda:</p>
<ul>
  <li>Keraksiz ustunlar ko‘zni chalg‘itadi va katta jadvalda so‘rovni sekinlatadi.</li>
  <li>Ertaga bazaga “ichki izoh” ustuni qo‘shilsa, <code>*</code> uni ham chiqarib yuboradi — ba’zan maxfiy narsa.</li>
  <li>Siz nima so‘raganingizni o‘qigan odam tushunishi kerak. Aniq ustun — aniq savol.</li>
</ul>

<p>Ba’zan ustun nomi inglizcha, hisobot o‘zbekcha bo‘lishi kerak. Shunda <code>AS</code> yordam beradi — bu “taxallus”, faqat shu so‘rov uchun yangi sarlavha:</p>
<pre>SELECT name AS mijoz, city AS shahar
FROM customers;</pre>
<p>Ma’lumot o‘zgarmaydi. Faqat natijada ustun “mijoz” va “shahar” deb yoziladi. Mashqlarda tizim shu nomni kutishi mumkin — shuning uchun <code>AS total</code> kabi narsalarni e’tiborsiz qoldirmang.</p>

<p>Kichik maslahat: avval savolni o‘zbekcha yozing (“ism va shahar kerak”), keyin SQL ga o‘giring. Teskari qilmang.</p>
""",
    "natijani-oqish": """
<p>So‘rov yozdingiz, tugma bosildi. Ekranda jadval chiqdi. Uni qanday o‘qishni ham o‘rganish kerak — aks holda “ishladi” deb o‘ylab, noto‘g‘ri xulosa chiqarasiz.</p>

<p><strong>Har bir qator — bitta fakt.</strong> Mijozlar jadvalida bir qator = bir odam. To‘lovlar jadvalida bir qator = bir operatsiya. Agar 0 qator chiqsa, dastur buzilgani emas: shartga mos yozuv yo‘q. Tahlilda “hech kim” ham javob.</p>

<p>Endi takrorlash. Agar yozsangiz:</p>
<pre>SELECT city FROM customers;</pre>
<p>Toshkent ikki marta chiqishi mumkin — chunki ikki mijoz Toshkentda. Bu xato emas. Lekin savol boshqacha bo‘lishi mumkin: “Umuman qaysi shaharlar bor?” Takror kerak emas. Shunda:</p>
<pre>SELECT DISTINCT city FROM customers;</pre>
<p><code>DISTINCT</code> — “takrorsiz”. Har shahar bir marta. Nechta unikal shahar bor, deb so‘rasangiz:</p>
<pre>SELECT COUNT(DISTINCT city) AS shahar_soni FROM customers;</pre>
<p>Buni hozir yoddan yozishingiz shart emas. G‘oya muhim: takror va unikal — ikki xil savol.</p>

<p>Yana bir tushuncha: <strong>NULL</strong>. Bu “noma’lum”. Shahar kiritilmagan bo‘lsa, katak bo‘sh emas, balki NULL. 0 ham emas, bo‘sh matn ham emas. Keyinroq <code>IS NULL</code> ni o‘rganamiz. Hozir shuni biling: NULL ni <code>= 'Toshkent'</code> bilan solishtirsangiz, odatda u qator chiqmaydi.</p>

<p>Katta jadvalni ko‘zdan kechirish uchun ba’zan faqat 5 qator kerak:</p>
<pre>SELECT * FROM customers LIMIT 5;</pre>
<p>Bu “birinchi 5 ta”. Tartib bermasangiz, qaysi 5 tasi ekani aniq bo‘lmasligi mumkin. Tartibni keyingi modulda o‘rganamiz.</p>

<p>Xulosa qilib: natija — oddiy jadval. Uni o‘qing. Takror bormi? Bo‘shmi? NULL bormi? Shu uch savol sizni “robot so‘rovchi”dan tahlilchiga aylantiradi.</p>
""",
    "where-operatori": """
<p>Hozirgacha butun jadvalni oldik. Amalda esa: “Faqat Toshkent”, “Faqat katta to‘lov”. Qatorlarni tanlash — <code>WHERE</code>. Inglizcha “qayerda / qaysi shart bilan”.</p>

<p>O‘qish tartibini eslab qoling, go‘yo gap gapirayotgandek:</p>
<p><em>customers jadvalidan, shahari Toshkent bo‘lganlarning, ismi va shahrini olib kel.</em></p>
<pre>SELECT name, city
FROM customers
WHERE city = 'Toshkent';</pre>
<p>Ali chiqadi. Malika (Samarqand) chiqmaydi. Filtr ishladi.</p>

<p>Ikki qoida, shu yerdan ko‘p xato chiqadi:</p>
<p><strong>Matn</strong> — yakka qo‘shtirnoq ichida. <code>'Toshkent'</code>, <code>'debit'</code>. Qo‘shtirnoqsiz yozsangiz, SQL buni ustun nomi deb o‘ylashi mumkin.</p>
<p><strong>Son</strong> — qo‘shtirnoqsiz. <code>amount &gt; 100000</code>. Ming ajratgich, so‘m belgisi qo‘yilmaydi.</p>
<pre>SELECT id, amount FROM transactions WHERE amount &gt; 100000;</pre>

<p>Taqqoslash belgilarini kundalik tilda:</p>
<ul>
  <li><code>=</code> teng</li>
  <li><code>&lt;&gt;</code> yoki <code>!=</code> teng emas</li>
  <li><code>&gt;</code> katta, <code>&gt;=</code> katta yoki teng</li>
  <li><code>&lt;</code> kichik, <code>&lt;=</code> kichik yoki teng</li>
</ul>
<p>Ikki shart birga kerak bo‘lsa — <code>AND</code>:</p>
<pre>SELECT name, city FROM customers
WHERE city = 'Toshkent' AND name = 'Ali Valiyev';</pre>
<p>Ikkalasi ham to‘g‘ri bo‘lishi shart. Keyingi darsda <code>OR</code>, <code>LIKE</code>, <code>IN</code> ni kengaytiramiz. Bugun: <code>=</code>, <code>&gt;</code>, <code>AND</code>.</p>

<p>Matn uzunligi — <code>LENGTH</code>. Masalan, juda uzun izohlar:</p>
<pre>SELECT id FROM transactions
WHERE LENGTH(note) &gt; 15;</pre>
<p><code>LENGTH(ustun)</code> — belgilar soni. <code>&gt; 15</code> — qat’iy katta (15 emas, 16 va undan yuqori).</p>

<p>Hisob-kitob ham WHERE da bo‘lishi mumkin. Masalan, zichlik = aholi / maydon. Butun sonni butun songa bo‘lsangiz, kasr yo‘qolishi mumkin — shuning uchun birini kasrga aylantiring:</p>
<pre>SELECT name,
       ROUND(population * 1.0 / area, 2) AS density
FROM World
WHERE population * 1.0 / area &gt; 90
  AND gdp &gt;= 10000000000;</pre>
<p><code>ROUND(..., 2)</code> — 2 ta kasr. <code>AS density</code> — natija ustuni nomi. Mashqda shu nomni kutishadi.</p>

<p>Moliya “faqat debitni ko‘rsat” desa:</p>
<pre>SELECT id, transaction_type
FROM transactions
WHERE transaction_type = 'debit';</pre>
<p>Agar <code>debit</code> ni qo‘shtirnoqsiz yozsangiz — ishlamasligi mumkin. Shu xatoni bir marta qiling, keyin unutmaysiz.</p>

<p>Esda tuting: <code>WHERE</code> qatorni tashlaydi yoki qoldiradi. Ustun tanlash hali ham <code>SELECT</code> da. Avval “qaysi odamlar”, keyin “ulardan qaysi maydonlar”.</p>
""",
    "order-by": """
<p>Filtrlab oldik. Lekin natija “qanday tushsa shunday” chiqishi mumkin. Rahbar esa “eng katta to‘lovdan boshla” deydi. Bu — saralash: <code>ORDER BY</code>.</p>

<p>Sukut bo‘yicha SQL o‘sish tartibida qo‘yadi: kichikdan kattaga, A dan Z gacha. Bunga <code>ASC</code> deyiladi, yozmasangiz ham shu. Teskarisi — <code>DESC</code> (descending, pastga / kamayish).</p>
<pre>SELECT id, amount
FROM transactions
ORDER BY amount DESC;</pre>
<p>Birinchi qator — eng katta summa. “Top” degan hisobotlarning deyarli hammasi <code>DESC</code>.</p>

<p>Arzonidan qimmatiga kerak bo‘lsa, <code>DESC</code> ni olib tashlang yoki <code>ASC</code> yozing:</p>
<pre>ORDER BY amount ASC</pre>

<p>Ba’zan ikkita mezon bo‘ladi: avval shahar, bir shaharda esa ism.</p>
<pre>SELECT name, city
FROM customers
ORDER BY city, name;</pre>
<p>SQL avval <code>city</code> bo‘yicha qo‘yadi. Shahar bir xil bo‘lsa, <code>name</code> ga qarab. Turli yo‘nalish ham bo‘ladi: <code>ORDER BY city ASC, amount DESC</code>.</p>

<p>“Eng katta 3 ta” desa, avval tartib, keyin chegara:</p>
<pre>SELECT id, amount
FROM transactions
ORDER BY amount DESC
LIMIT 3;</pre>
<p>Agar <code>LIMIT 3</code> ni tartibsiz qo‘ysangiz, tasodifiy 3 qator chiqishi mumkin. Avval kim birinchi, keyin nechta.</p>

<p>Ko‘pincha filtrlash + takrorsiz + tartib birga keladi. Oldingi darslardagi <code>WHERE</code>, <code>DISTINCT</code>, <code>AS</code> ni eslang:</p>
<pre>SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;</pre>
<p>Avval shart, keyin takrorlarni olib tashlash, keyin o‘sish tartibi. Ustun nomi <code>id</code> bo‘lishi uchun <code>AS id</code>.</p>

<p>Mashqda “qator tartibi tekshiriladi” desam — <code>ORDER BY</code> ni unutmang. To‘g‘ri ustunlar, noto‘g‘ri tartib — xato hisoblanadi.</p>
""",
    "bir-nechta-shart": """
<p>Hayotda bir shart kamdan-kam yetadi. “Toshkent <em>va</em> ismi A bilan”, “Toshkent <em>yoki</em> Samarqand”. Bu yerda <code>AND</code> va <code>OR</code> kiradi.</p>

<p><code>AND</code> — qizg‘in ota-ona: <strong>hammasi</strong> to‘g‘ri bo‘lishi kerak.</p>
<pre>SELECT * FROM customers
WHERE city = 'Toshkent' AND name LIKE 'A%';</pre>
<p>Toshkentda yashamaydigan Ali chiqmaydi. A bilan boshlanmaydigan toshkentlik ham chiqmaydi.</p>

<p><code>OR</code> — yumshoqroq: <strong>bittasi</strong> to‘g‘ri bo‘lsa yetadi.</p>
<pre>SELECT * FROM customers
WHERE city = 'Toshkent' OR city = 'Samarqand';</pre>
<p>Qisqa yo‘l: <code>city IN ('Toshkent', 'Samarqand')</code>. Ro‘yxatni o‘qish osonroq.</p>

<p>Endi tuzoq. Qavs qo‘ymasangiz, SQL o‘zicha “kim birinchi” deb hisoblaydi va siz kutmagan odamlarni olib kelishi mumkin.</p>
<pre>WHERE city = 'Toshkent' AND (name LIKE 'A%' OR name LIKE 'M%')</pre>
<p>Bu: Toshkentdagi A yoki M. Qavssiz yozsangiz, “Toshkent va A” <em>yoki</em> “ismi M — istalgan shahar” chiqishi mumkin. Ovoz chiqarib o‘qing, keyin qavs qo‘ying.</p>

<p><code>LIKE</code> — matn qidiruv. Ikki belgi:</p>
<ul>
  <li><code>%</code> — nima bo‘lsa bo‘ladi, hatto hech narsa: <code>'A%'</code> A bilan boshlanadi, <code>'%ov'</code> ov bilan tugaydi, <code>'%ali%'</code> ichida ali bor</li>
  <li><code>_</code> — aniq bitta belgi: <code>'_oshkent'</code> Toshkentga mos kelishi mumkin</li>
</ul>
<p>Kodlar bo‘shliq bilan ajratilgan bo‘lsa (masalan <code>ACNE DIAB100</code>), kod qator <em>boshida</em> yoki <em>bo‘shliqdan keyin</em> turishi mumkin. Ikkalasini qamrab olish:</p>
<pre>WHERE conditions LIKE 'DIAB1%'
   OR conditions LIKE '% DIAB1%'</pre>
<p>E’tibor: <code>'% DIAB1%'</code> da <code>%</code> dan keyin <strong>bo‘shliq</strong> bor. Shunda <code>XDIAB1</code> kabi yolg‘on mos kelmaydi. <code>DIAB100</code> mos (<code>DIAB1</code> bilan boshlanadi), <code>DIAB201</code> emas.</p>

<p>Katta-kichik harf ba’zi bazalarda farq qiladi. Bizning mashqlarda namunani aniq yozing.</p>

<p>Oraliq pul:</p>
<pre>WHERE amount BETWEEN 10000 AND 50000</pre>
<p>10000 ham, 50000 ham kiritiladi. “Dan … gacha, chekkalari bilan.”</p>

<p>Maslahat: avval bitta shartni ishlatib ko‘ring, ishlasa ikkinchisini qo‘shing. Darhol uch qatorlik WHERE yozib, keyin “nima uchun bo‘sh?” deb o‘tirmang.</p>
""",
    "count": """
<p>Tahlilchining birinchi savoli ko‘pincha “nechta?”. Ro‘yxat emas, <strong>son</strong>. Buning uchun <code>COUNT</code>.</p>

<p>Eng sodda:</p>
<pre>SELECT COUNT(*) AS total FROM customers;</pre>
<p>Jadvalda nechta qator bor — shu. <code>AS total</code> natijaga nom beradi. Nom bermasangiz, ustun “nomsiz” chiqadi; mashqda esa <code>total</code> yoki <code>cnt</code> kutulishi mumkin.</p>

<p>Faqat Toshkentliklar soni — avval filtr, keyin sanash:</p>
<pre>SELECT COUNT(*) AS total
FROM customers
WHERE city = 'Toshkent';</pre>
<p>Bu yerda <code>GROUP BY</code> yo‘q. Bitta savol, bitta son.</p>

<p>Uch xil COUNT ni farqlang, aks holda NULL sizni aldaydi:</p>
<ul>
  <li><code>COUNT(*)</code> — qatorlar, NULL bo‘lsa ham qator bor deb sanaydi</li>
  <li><code>COUNT(city)</code> — faqat shahar yozilganlari (NULL emas)</li>
  <li><code>COUNT(DISTINCT city)</code> — nechta <em>xil</em> shahar</li>
</ul>
<p>5 mijoz, 2 tasi Toshkent, 2 tasi Samarqand, 1 tasida shahar bo‘sh. <code>COUNT(*)</code> = 5. <code>COUNT(city)</code> = 4. <code>COUNT(DISTINCT city)</code> = 2.</p>

<p>Hozir “har bir shahar uchun alohida son” ni to‘liq qilmaymiz — bu keyingi dars, <code>GROUP BY</code>. Bugun: bitta savol → bitta COUNT.</p>
""",
    "sum-va-avg": """
<p>“Nechta?” dan keyin “qancha pul?” keladi. Qatorlarni qo‘lda qo‘shmaymiz. <code>SUM</code> yig‘adi, <code>AVG</code> o‘rtachasini oladi. <code>MIN</code> va <code>MAX</code> chekkalarni ko‘rsatadi.</p>
<pre>SELECT SUM(amount) AS total FROM transactions;</pre>
<p>Barcha to‘lovlar yig‘indisi. Debitni alohida so‘rasa, <code>WHERE</code> qo‘shamiz — avval kerakli qatorlar, keyin yig‘indi:</p>
<pre>SELECT SUM(amount) AS total
FROM transactions
WHERE transaction_type = 'debit';</pre>

<p>O‘rtacha chek:</p>
<pre>SELECT AVG(amount) AS avg_amount FROM transactions;</pre>
<p>O‘rtacha haqida ochiq gap: bitta ulkan to‘lov o‘rtachani osmondan oshiradi. Hisobotda ba’zan “tipik chek” uchun median ham kerak bo‘ladi — bu statistika. SQL da avval SUM/AVG ni ishonchli qiling.</p>

<p>NULL bu yerda ham muhim: odatda SUM va AVG NULL kataklarni tashlab yuboradi, 0 deb hisoblamaydi. “Noma’lum” va “nol so‘m” — turli narsa.</p>
<pre>SELECT MIN(amount) AS eng_kichik, MAX(amount) AS eng_katta
FROM transactions;</pre>
<p>Bir so‘rovda ikkita agregat — ruxsat. Hammasini bitta qator qilib qaytaradi.</p>

<p>Ba’zan yig‘indi ustun emas, <em>ifoda</em> bo‘ladi. Masalan, sessiya daqiqasi = chiqish − kirish:</p>
<pre>SELECT SUM(out_time - in_time) AS total_time
FROM EmployeeAttendance;</pre>
<p><code>SUM</code> ichida <code>out_time - in_time</code> — har qator uchun farq, keyin yig‘indi. Hozircha <code>GROUP BY</code> yo‘q: butun jadval → bitta son. “Har xodim / har kun” keyingi darsda.</p>

<p>Mashqda so‘ralgan ustun nomini <code>AS</code> bilan qo‘ying. To‘g‘ri son, noto‘g‘ri nom — tizim qabul qilmasligi mumkin. Injiq, lekin hisobotda ham sarlavha muhim.</p>
""",
    "group-by-asoslari": """
<p>Shu paytgacha bitta savolga bitta son oldik: jami nechta, jami qancha. Endi savol o‘zgaradi: <em>har bir mijoz uchun</em> nechta to‘lov? <em>Har bir shahar uchun</em> nechta odam?</p>
<p>Bu — guruhlash. <code>GROUP BY</code>. Tasavvur qiling, qatorlarni stolda “shu mijoz”, “o‘sha mijoz” deb uyum-uyum qilib qo‘ydik. Keyin har uyumda sanaymiz yoki qo‘shamiz.</p>
<pre>SELECT customer_id, COUNT(*) AS cnt
FROM transactions
GROUP BY customer_id;</pre>
<p>Natijada har bir <code>customer_id</code> bitta qator. Yonida o‘sha odamning to‘lovlari soni. Yig‘indi kerak bo‘lsa, <code>COUNT</code> o‘rniga <code>SUM(amount) AS total</code>.</p>

<p>Obunachilar soni kabi savol: har <code>user_id</code> uchun nechta qator, keyin tartib:</p>
<pre>SELECT user_id, COUNT(*) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;</pre>
<p><code>ORDER BY</code> guruhlashdan keyin ham ishlaydi — natija qatorlarini saralaydi.</p>

<p>Takroriy qiymatni bir marta sanash kerak bo‘lsa — <code>COUNT(DISTINCT ...)</code>:</p>
<pre>SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;</pre>
<p>Bir fan ikki kafedraga yozilgan bo‘lsa, oddiy <code>COUNT(*)</code> ikki marta sanaydi; <code>COUNT(DISTINCT subject_id)</code> — bitta fan.</p>

<p>Oltin qoida, shu yerda ko‘p kishi yiqiladi: <code>SELECT</code> da yozgan oddiy ustun (COUNT/SUM bo‘lmagan) <code>GROUP BY</code> da ham bo‘lishi kerak. Aks holda SQL so‘raydi: “Qaysi amount? Uyumda 6 xil amount bor-ku?”</p>
<p>Xato g‘oya: <code>SELECT customer_id, amount, COUNT(*)</code> — amount guruhlanmagan. To‘g‘ri: guruh kaliti + hisob.</p>

<p>Yana ikkita so‘z. <code>WHERE</code> uyum qilishdan <em>oldin</em> qatorlarni tashlaydi: masalan, avval faqat debit. <code>HAVING</code> esa uyum qilingandan <em>keyin</em> “bu uyum juda kichik, tashla” deydi.</p>
<pre>SELECT customer_id, COUNT(*) AS cnt
FROM transactions
GROUP BY customer_id
HAVING COUNT(*) &gt; 5;</pre>
<p>Faqat 5 tadan ko‘p to‘lovi borlar. <code>WHERE COUNT(*) &gt; 5</code> odatda ishlamaydi — hisob hali yo‘q, qator darajasida COUNT yo‘q.</p>
<p>HAVING ni keyingi modulda sekinroq qayta ko‘ramiz. Bugun: GROUP BY = “har biri uchun”. SELECT da kalit va COUNT/SUM. Nomini <code>AS</code> bilan qo‘ying.</p>
""",
}


ADVANCED_LECTURES = {
    "having-nima": """
<p>Oldingi modulda guruhladik. Endi guruhning o‘zini tanlaymiz. Odamlar aralashmasin: qatorni tashlash — <code>WHERE</code>. “Bu guruh bizga kerakmi?” — <code>HAVING</code>.</p>

<p>Hayotiy savol: “Kamida N ta a’zosi bor guruhlar.” Avval guruh bo‘yicha sanaysiz, keyin kichiklarini tashlaysiz. Sanash guruhdan keyin bo‘lgani uchun HAVING. Mashqdagi jadval va chegara boshqacha bo‘ladi — g‘oya shu.</p>
<p>Bank misolida: kamida 2 mijozli shaharlar.</p>
<pre>SELECT city, COUNT(*) AS cnt
FROM customers
WHERE city &lt;&gt; 'Buxoro'
GROUP BY city
HAVING COUNT(*) &gt;= 2;</pre>
<p>Avval Buxoroni umuman hisobga olmaymiz (qator filtri), keyin qolgan shaharlarda “kamida 2 mijoz” (guruh filtri).</p>
<p>Yodlab qo‘ying, yozish tartibi: SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY. Og‘izda aytib yozing — chalkashmaydi.</p>
<p>Qoida: COUNT, SUM, AVG sharti — HAVING. Oddiy ustun sharti — WHERE.</p>
""",
    "group-by-kop-ustun": """
<p>Ba’zan guruh bitta ustun emas. “Har aktyor” emas, “aktyor va rejissyor juftligi”. Excelda ikkita ustunni birga pivot qilgandek.</p>
<pre>SELECT customer_id, transaction_type, COUNT(*) AS c
FROM transactions
GROUP BY customer_id, transaction_type;</pre>
<p>Har mijoz + tur juftligi — o‘z soni. <code>customer_id</code> ni guruhlab, <code>transaction_type</code> ni tashlab yozsangiz, SQL yana o‘sha savolni beradi: qaysi tur?</p>
<p>SELECT dagi har bir “oddiy” ustun GROUP BY da turishi kerak. COUNT esa hisob, guruh kaliti emas.</p>

<p>Faqat “kamida N marta” juftliklar kerak bo‘lsa — guruhlab sanang, keyin <code>HAVING</code>:</p>
<pre>SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) &gt;= 3;</pre>
<p>Ikki kalit GROUP BY da. Sanash juftlik ichida. Kichik juftliklar HAVING bilan tashlanadi.</p>

<p>Ishda: shahar + kanal, oy + mahsulot. Savolni “har bir X va Y uchun” deb ayting — ikkita kalit chiqadi.</p>
""",
    "agregat-filtr": """
<p>Ba’zan bir so‘rovga sig‘maydigan savol bo‘ladi. Masalan: “Faqat bir marta uchragan sonlar ichidan eng kattasi.” Avval sanaysiz, keyin filtr, keyin MAX.</p>
<p>Buni bosqichma-bosqich o‘ylang, darhol chiroyli kod yozmang.</p>
<ol>
  <li>Har qiymat necha marta? Guruhlab sanash</li>
  <li>Faqat bir marta uchraganlarni qoldirish</li>
  <li>Qolganlardan eng kattasi</li>
</ol>
<p>3-qadam tashqi so‘rov: ichkaridagi natija kichik jadval bo‘lib qoladi. Bankda: faqat bir marta uchragan summalar ichidan eng kattasi.</p>
<pre>SELECT MAX(amount) AS amount
FROM (
  SELECT amount FROM transactions
  GROUP BY amount
  HAVING COUNT(*) = 1
) AS t;</pre>
<p>Ichki qism — “yolg‘iz sonlar”. Tashqi — ularning eng kattasi. <code>AS t</code> — ichki jadvalga nom; ba’zi tizimlar nomsiz qabul qilmaydi.</p>
<p>Keyinroq shu narsani <code>WITH</code> (CTE) bilan yanada tushunarli yozamiz. Hozir g‘oya: katta savolni kichik savollarga bo‘ling.</p>
""",
    "inner-join": """
<p>Hozirgacha bitta jadval. Hayotda esa ism bir joyda, to‘lov boshqa joyda. Excelda VLOOKUP qilgan bo‘lar edingiz. SQL da bu — <code>JOIN</code>.</p>

<p>Nima bog‘laydi? Umumiy kalit. To‘lovda <code>customer_id = 1</code>, mijozlar jadvalida <code>id = 1</code> — shu Ali.</p>
<p><strong>INNER JOIN</strong> degani: faqat mos kelganlar. To‘lovi yo‘q mijoz — bu so‘rovda yo‘qoladi. To‘lov bor, lekin mijoz o‘chirilgan — u ham (odatda) chiqmaydi. Faqat kesishma.</p>
<pre>SELECT c.name, t.amount
FROM customers AS c
INNER JOIN transactions AS t
  ON c.id = t.customer_id;</pre>
<p><code>AS c</code> va <code>AS t</code> — qisqa laqab, charchamaslik uchun. <code>ON</code> — “qaysi ustunlar bir xil odamni bildiradi.”</p>
<p><code>INNER</code> so‘zini tashlab, faqat <code>JOIN</code> yozish ham ko‘p joyda shu ma’noni beradi.</p>
<p>Keyingi darsda so‘raymiz: to‘lovsiz mijozlar ham kerakmi? Unda INNER yetmaydi.</p>
""",
    "left-join": """
<p>Rahbar: “Barcha mijozlar. To‘lovi bo‘lsa yozing, bo‘lmasa ham ro‘yxatda qolsin.” Bu INNER emas. Bu — <code>LEFT JOIN</code>.</p>
<p>Chap jadval — asosiy, “hech kimni tashlama”. O‘ng jadval — qo‘shimcha. Mos kelmasa, o‘ng tomon <code>NULL</code> bo‘ladi, chapdagi ism saqlanadi.</p>
<pre>SELECT c.name, t.id
FROM customers AS c
LEFT JOIN transactions AS t
  ON c.id = t.customer_id;</pre>
<p>To‘lovi yo‘q odamning <code>t.id</code> si bo‘sh (NULL) chiqadi. Ichki JOIN da u umuman yo‘q edi.</p>

<p>Aynan shu NULL orqali “hech qachon to‘lamaganlar” ni topamiz:</p>
<pre>SELECT c.name
FROM customers AS c
LEFT JOIN transactions AS t ON c.id = t.customer_id
WHERE t.customer_id IS NULL;</pre>
<p>O‘ng kalit NULL — demak juftlik topilmadi. Bu klassik usul. Yodlab qo‘ying, intervyuda ham so‘rashadi.</p>
<p>Qaysi jadval chapda ekani muhim. Chapni almashtirsangiz, savol ham o‘zgaradi.</p>
""",
    "join-null": """
<p>LEFT JOIN qildingiz, endi “bonus 1000 dan kam yoki umuman bonus yo‘q” deb filtrlamoqchisiz. Shu yerda tuzoq bor.</p>
<p><code>WHERE bonus &lt; 1000</code> NULL qatorni odatda yutib yuboradi. Chunki “noma’lum 1000 dan kichikmi?” — SQL “ha” demaydi. Siz esa “bonus yo‘qlar ham kerak” degan edingiz.</p>
<p>Yechimlardan biri — NULL ni 0 deb o‘qish. Bank misoli: chapda barcha mijoz, o‘ngda to‘lov; “summa 20 000 dan kichik yoki to‘lov yo‘q”:</p>
<pre>SELECT c.name, t.amount
FROM customers AS c
LEFT JOIN transactions AS t ON c.id = t.customer_id
WHERE COALESCE(t.amount, 0) &lt; 20000;</pre>
<p><code>COALESCE</code> — “birinchi NULL bo‘lmaganini ol”. Bonus yo‘q bo‘lsa 0, 0 esa 1000 dan kichik — qator qoladi. Yoki ochiq yozing: <code>bonus &lt; 1000 OR bonus IS NULL</code>.</p>
<p>JOIN dan keyin WHERE yozsangiz, NULL haqida 5 soniya o‘ylab ko‘ring. Ko‘p “nima uchun odamlar yo‘qoldi?” shu yerdan chiqadi.</p>
""",
    "subquery-where": """
<p>Ba’zan javob boshqa so‘rovning ichida. “O‘rtachadan qimmat to‘lovlar” — avval o‘rtachani topasiz, keyin solishtirasiz. Ichki so‘rov qavs ichida turadi. Buni subquery deyishadi, qo‘rqmang: shunchaki so‘rov ichida so‘rov.</p>
<pre>SELECT id, amount
FROM transactions
WHERE amount &gt; (SELECT AVG(amount) FROM transactions);</pre>
<p>Ichki qism bitta son qaytaradi — o‘rtacha. Tashqi har qatorni shu songa solishtiradi.</p>
<p>Ro‘yxat ham bo‘lishi mumkin:</p>
<pre>SELECT name FROM customers
WHERE id NOT IN (SELECT customer_id FROM transactions);</pre>
<p>Ichki: buyurtma bergan ID lar. Tashqi: shu ro‘yxatda yo‘qlar. Eslatib qo‘yaman: ichki ro‘yxatda NULL bo‘lsa, <code>NOT IN</code> g‘alati bo‘sh natija berishi mumkin. Shunda LEFT JOIN … IS NULL yoki NOT EXISTS tinchroq.</p>
<p>Subquery ni “avval shu savolga javob ber, keyin uni ishlat” deb o‘qing.</p>
""",
    "subquery-from": """
<p>Ichki so‘rovni nafaqat WHERE da, balki FROM da ham qo‘yish mumkin. Ma’nosi: “Avval kichik jadval yasab ol, keyin undan SELECT qil.”</p>
<pre>SELECT MAX(amount) AS amount
FROM (
  SELECT amount FROM transactions
  GROUP BY amount
  HAVING COUNT(*) = 1
) AS singles;</pre>
<p>Qavs ichidagi narsa vaqtinchalik jadval. Unga albatta nom bering — <code>singles</code>. Tashqi SQL uni oddiy jadvaldek o‘qiydi.</p>
<p>Agar chigal bo‘lib ketsa, keyingi darsdagi <code>WITH</code> o‘sha narsani tepaga olib chiqadi, o‘qish osonlashadi. G‘oya bir xil: bosqichma-bosqich.</p>
""",
    "exists-in": """
<p>Ikki yaqin savol: “Bu qiymat ro‘yxatda bormi?” va “Bu mijozga bog‘liq birorta qator bormi?”</p>
<p><code>IN</code> — ro‘yxat. Qo‘lda ham, subquery dan ham:</p>
<pre>WHERE city IN ('Toshkent', 'Buxoro')
WHERE id IN (SELECT customer_id FROM transactions)</pre>
<p><code>EXISTS</code> — “ichki so‘rov hech bo‘lmaganda bitta qator qaytaryaptimi?” Ustun muhim emas, shuning uchun ko‘pincha <code>SELECT 1</code> yoziladi:</p>
<pre>SELECT c.name
FROM customers AS c
WHERE EXISTS (
  SELECT 1 FROM transactions AS t
  WHERE t.customer_id = c.id
);</pre>
<p>To‘lovi borlar. Teskarisi: <code>NOT EXISTS</code> — to‘lovi yo‘qlar.</p>
<p>Qachon qaysi? Qisqa ro‘yxat — IN. “Bog‘liq yozuv bormi?” — EXISTS. NULL dan qo‘rqsangiz, NOT IN o‘rniga NOT EXISTS yoki LEFT JOIN.</p>
""",
    "cte-asoslari": """
<p>So‘rov uzunlashsa, ichma-ich qavslar o‘qilmay qoladi. O‘qituvchi sifatida aytaman: tushunilmaydigan SQL — yomon SQL, hatto to‘g‘ri ishlasa ham.</p>
<p><code>WITH</code> yordamida bosqichga nom beramiz. Buni CTE deyishadi (Common Table Expression). Vaqtinchalik, faqat shu so‘rov uchun.</p>
<pre>WITH yolgiz AS (
  SELECT amount FROM transactions
  GROUP BY amount
  HAVING COUNT(*) = 1
)
SELECT MAX(amount) AS amount FROM yolgiz;</pre>
<p>Avval “yolg‘iz sonlar” ni <code>singles</code> deb atadik. Keyin oddiy SELECT. FROM ichidagi subquery bilan ish bir xil, lekin hikoya tepadan pastga o‘qiladi.</p>
<p>Ishda: avval tozalangan to‘lovlar, keyin guruh, keyin hisobot. Har bosqich — alohida WITH.</p>
""",
    "cte-bir-nechta": """
<p>Bitta WITH da bir nechta nom bo‘lishi mumkin. Vergul bilan. Ikkinchisi birinchidan foydalana oladi — zanjir.</p>
<pre>WITH a AS (
  SELECT city, COUNT(*) AS cnt FROM customers GROUP BY city
),
b AS (
  SELECT city FROM a WHERE cnt &gt;= 2
)
SELECT * FROM b;</pre>
<p>Avval sanadik, keyin filtrladik. HAVING ni ham shu yo‘l bilan “oddiy WHERE” ga aylirish mumkin — ba’zan o‘qish osonroq.</p>
<p><code>WITH</code> bir marta yoziladi. Oxirida albatta asosiy SELECT bo‘ladi. Unutmang: CTE lar bazaga saqlanmaydi, faqat shu yugurish.</p>
""",
    "cte-amal": """
<p>Keling, CTE ni “chiroy uchun” emas, ish uchun ishlatamiz. Guruhlash ichida, filtr tashqarida:</p>
<pre>WITH j AS (
  SELECT customer_id, COUNT(*) AS c
  FROM transactions
  GROUP BY customer_id
)
SELECT customer_id
FROM j
WHERE c &gt;= 3;</pre>
<p>Xato chiqsa, avval faqat <code>SELECT * FROM j</code> ni ishlatib ko‘ring. Bosqich ishlayaptimi? Keyin tashqi filtr. Shunday debug qilinadi — butun cho‘chqani bir tishda emas.</p>
<p>Tahlilchi odatda: 1) toza fact CTE, 2) KPI SELECT. Jamoa a’zosi o‘qiganda minnatdor bo‘ladi.</p>
""",
    "case-when": """
<p>Excelda IF bor edi: shart rost bo‘lsa bir narsa, aks holda boshqa. SQL da bu — <code>CASE</code>. Qator-qator yurib, birinchi to‘g‘ri shartni oladi, qolganini o‘qimaydi. Hech narsa to‘g‘ri kelmasa — <code>ELSE</code>, u ham yo‘q bo‘lsa NULL.</p>
<pre>SELECT id, amount,
  CASE
    WHEN amount &lt; 20000 THEN 'kichik'
    WHEN amount &lt; 50000 THEN 'orta'
    ELSE 'katta'
  END AS segment
FROM transactions;</pre>
<p>Tartib muhim. Avval “kichik” ni qo‘ymasangiz, 10 ming ham “orta”ga tushib qolishi mumkin. Chegaralarni yuqoridan yoki pastdan ketma-ket yozing.</p>
<p><code>END</code> ni unutmang — SQL shu yerda IF tugaydi. Nom <code>AS segment</code> bilan.</p>
<p>Uchburchak misoli ham shu IF: tomonlar tengsizligi rost bo‘lsa Yes, aks holda No. Mantiq bir xil.</p>
""",
    "case-select": """
<p>CASE ni yangi ustun qilib chiqaramiz: bonus, ha/yo‘q, flag. Jadval o‘zgarmaydi — faqat natija.</p>
<pre>SELECT id,
  CASE
    WHEN amount &gt;= 50000 THEN amount
    ELSE 0
  END AS katta_summa
FROM transactions;</pre>
<p>Shartga mos to‘lov o‘z summasini, qolganlar nol. Bu “hisobot maydoni”. Ertaga boshqa qoida bo‘lsa, CASE ni o‘zgartirasiz, xom ma’lumotga tegmaysiz.</p>
<p>Keyingi qadam: shu CASE ni SUM ichiga qo‘yib, nechtasini sanash. Avval bitta qatorlik mantiqni tushunib oling.</p>
""",
    "case-agregat": """
<p>Endi CASE ni hisobga aylantiramiz. Exceldagi COUNTIFS / SUMIF ga yaqin.</p>
<pre>SELECT transaction_type,
  SUM(CASE WHEN amount &gt;= 50000 THEN 1 ELSE 0 END) AS katta_soni,
  COUNT(*) AS jami
FROM transactions
GROUP BY transaction_type;</pre>
<p>Har tur uchun: nechtasi “katta”, nechtasi umuman. 1 va 0 ni qo‘shish — sanashning hiylasi.</p>
<p>Pul ham shunday:</p>
<pre>SUM(CASE WHEN transaction_type = 'debit' THEN amount ELSE 0 END) AS debit_sum</pre>
<p>Bitta so‘rovda debit yig‘indisi, yonida credit — pivotga o‘xshaydi. Guruh kaliti boshqa bo‘lishi mumkin (shahar, oy).</p>
<p>NULL chiqmasin desangiz, ELSE 0 qo‘ying. ELSE unutsangiz, mos kelmaganlar NULL, SUM ularni tashlashi mumkin — kutilgan 0 emas.</p>
""",
    "sana-filtr": """
<p>Sana — oddiy ustun, lekin format odamlarni chalg‘itadi. Xavfsiz odat: <code>'2024-03-01'</code> (yil-oy-kun). Kun/oy almashtirish xatolari shu formatda kamayadi.</p>
<pre>SELECT DISTINCT city
FROM customers
WHERE city = 'Toshkent';</pre>
<p>Aniq qiymat. Oraliq — mart oyi:</p>
<pre>WHERE transaction_date BETWEEN '2024-03-01' AND '2024-03-31'</pre>
<p>BETWEEN ikkala chekkani oladi. Agar ustunda soat ham bo‘lsa (12:00), “31-kun kechasi” tushib qolishi mumkin. Shunda: <code>&gt;= '2024-03-01' AND &lt; '2024-04-01'</code> aniqroq. Bizning mashqlarda odatda faqat kun.</p>
<p>Matn sanani solishtirish ISO tartibida ishlaydi. “Mart” deb o‘zbekcha yozilmaydi — raqam.</p>
""",
    "sana-group": """
<p>Kunlik faollik: har kun uchun nechta odam. Bu GROUP BY sana + unikal sanash.</p>
<pre>SELECT transaction_date AS day,
       COUNT(*) AS cnt
FROM transactions
GROUP BY transaction_date;</pre>
<p>Bir kishi bir kunda 10 marta kirsada, <code>COUNT(DISTINCT user_id)</code> uni bir marta sanaydi. Oddiy <code>COUNT(*)</code> esa har kirishni sanar edi — savol boshqacha.</p>
<p>Oy bo‘yicha savdo (SQLite, bizning muhit):</p>
<pre>SELECT strftime('%Y-%m', transaction_date) AS oy,
       SUM(amount) AS total
FROM transactions
GROUP BY oy;</pre>
<p>PostgreSQL da boshqacha funksiya bo‘ladi. Hisobotda qaysi tizim ekanini yozib qo‘ying. G‘oya baribir: vaqtni kesib, guruhlab, SUM/COUNT.</p>
""",
    "sana-farq": """
<p>Marketing: “Shu kun, shu brend — nechta unikal lead?” Takroriy ID larni bir marta sanash — yana DISTINCT.</p>
<pre>SELECT transaction_date, transaction_type,
       COUNT(*) AS cnt
FROM transactions
GROUP BY transaction_date, transaction_type;</pre>
<p>Guruh ikkita: kun va brend. Har katakcha — o‘z kesimi.</p>
<p>Yetkazib berish kechikdimi? Ikki sana ayirmasi. SQLite da <code>julianday(yetkazilgan) - julianday(va’da)</code> kun beradi. Musbat katta son — kech. Manfiy — erta. Formula tizimga bog‘liq, savol umumiy: SLA ni o‘rtacha bilan emas, kechikish dumini ham qarang.</p>
""",
    "window-asos": """
<p>GROUP BY qatorlarni “yig‘ib”, har guruhdan bitta qator qoldiradi. Ba’zan esa barcha qatorlar kerak, yonida tartib raqami yoki jami. Buni window (oyna) funksiyasi qiladi. Qator yo‘qolmaydi.</p>
<pre>SELECT id, amount,
       ROW_NUMBER() OVER (ORDER BY amount DESC) AS rn
FROM transactions;</pre>
<p><code>OVER (ORDER BY amount DESC)</code> — “shu tartibda 1, 2, 3…” Har to‘lov o‘z qatorida qoladi, yonida raqam.</p>
<p><code>PARTITION BY city</code> qo‘shsangiz, har shahar ichida 1 dan qayta boshlanadi. Excelda “guruh ichida tartib” degan narsa.</p>
<p>Hozircha bitta gap: OVER — oyna. ORDER BY — qanday sanash. PARTITION — qaysi ichki guruh (ixtiyoriy).</p>
""",
    "window-rank": """
<p>Ikki kishi bir xil ball olsa, o‘rin qanday bo‘ladi? Sportchilar tushunadi: ba’zan 1, 1, 3 (ikkkinchi yo‘q), ba’zan 1, 1, 2.</p>
<ul>
  <li><code>ROW_NUMBER()</code> — baribir 1, 2, 3. Teng bo‘lsa ham raqam farqli (ichki tartibga qarab)</li>
  <li><code>RANK()</code> — tenglar bir xil, keyingi teshik: 1, 1, 3</li>
  <li><code>DENSE_RANK()</code> — tenglar bir xil, teshik yo‘q: 1, 1, 2</li>
</ul>
<pre>SELECT id, amount,
       RANK() OVER (ORDER BY amount DESC) AS rnk
FROM transactions;</pre>
<p>Eng yuqori ball — 1. “Top-1 ni unique qilib olish” kerak bo‘lsa, ko‘pincha ROW_NUMBER qulay. Hisobotdagi o‘rin — RANK yoki DENSE_RANK. Savolni o‘zbekcha ayting, keyin funksiyani tanlang.</p>
""",
    "window-sum": """
<p>Har qatorda “umumiy nechta o‘rindiq” yoki “shu mijozning jami to‘lovi” kerak bo‘lsa, guruhlab yo‘qotish shart emas.</p>
<pre>SELECT id, amount,
       COUNT(*) OVER () AS jami
FROM transactions;</pre>
<p><code>OVER ()</code> — butun natija oynasi. Har qatorda bir xil jami.</p>
<p><code>SUM(amount) OVER (PARTITION BY customer_id)</code> — har to‘lov yonida o‘sha mijozning yig‘indisi. Running total (kun sayin o‘sib borish) uchun ORDER BY sana qo‘shiladi. Default ramka tizimga bog‘liq — mashqda kutilgan ustunni aniq yozing.</p>
<p>Qisqa farq: GROUP BY siqadi. Window yoniga yozadi.</p>
""",
    "null-coalesce": """
<p>NULL ni yana bir bor, sekin. Bu “bo‘sh katakcha” emas. “Bilmaymiz.” 10 + noma’lum = noma’lum. Shuning uchun <code>10 + NULL</code> odatda NULL.</p>
<p>Tekshirish: <code>city IS NULL</code> / <code>IS NOT NULL</code>. Hech qachon <code>city = NULL</code> — bu ishlamaydi, chunki noma’lum tengmi, noma’lum.</p>
<p>O‘rinbosar qiymat kerak bo‘lsa, standart yo‘l:</p>
<pre>COALESCE(amount, 0)
COALESCE(city, '—')</pre>
<p>Ro‘yxatdagi birinchi haqiqiy qiymat. MySQL da IFNULL, SQL Server da ISNULL degan o‘xshashlari bor. Kursda COALESCE yozing — ko‘proq joyda tushuniladi.</p>
<p>LEFT JOIN qilgan zahoti NULL chiqishi oddiy. Uni 0 yoki matn bilan almashtirish yoki alohida “yo‘q” deb qoldirish — biznes savoliga bog‘liq. Avtomatik 0 qilish har doim to‘g‘ri emas (masalan, “noma’lum maosh” ni 0 desangiz, o‘rtacha buziladi).</p>
""",
    "combine-tables": """
<p>Klassik vazifa: odamlar bir jadvalda, manzil boshqasida. Har kimda manzil bo‘lmasligi mumkin. INNER qilsangiz, manzilsizlar yo‘qoladi. Shuning uchun LEFT — odam chapda.</p>
<pre>SELECT c.name, t.amount
FROM customers AS c
LEFT JOIN transactions AS t ON c.id = t.customer_id;</pre>
<p>To‘lovi yo‘q mijozda amount NULL. Bu xato emas — savol shunday: “hamma odam, to‘lov bo‘lsa qo‘sh.”</p>
<p>Kalit nomlari bir xil bo‘lsa <code>USING (personId)</code> ham uchraydi. Tushunish uchun <code>ON</code> ochiqroq. Intervyudagi “Combine Two Tables” degani asosan shu.</p>
""",
    "advanced-review": """
<p>Oxirgi dars. Yangi sehr yo‘q. Ishdagi hisobot odatda aralashma: avval bog‘lash, keyin tozalash, keyin guruh, ba’zan CASE.</p>
<p>O‘zingizga aytib yozing:</p>
<ol>
  <li>Qaysi jadvallar? Kalit nima? INNER mi, LEFT mi?</li>
  <li>Qaysi qatorlar kerak? WHERE. NULL ni unutdingizmi?</li>
  <li>Har biri uchun hisob bormi? GROUP BY + COUNT/SUM</li>
  <li>Shartli sanash? SUM(CASE…)</li>
  <li>Ustun nomi mashqdagi bilan bir xilmi? AS</li>
  <li>Tartib muhimmi? ORDER BY</li>
</ol>
<pre>SELECT c.name, COUNT(*) AS cnt
FROM customers AS c
JOIN transactions AS t ON c.id = t.customer_id
GROUP BY c.name;</pre>
<p>Avval mahsulot nomini JOIN bilan oldik, keyin sanadik. Bir nafasda 20 qatorlik so‘rov yozmang. Kichik SELECT, keyin qo‘shib boring.</p>
<p>Siz endi noldan: jadval nima, SELECT, filtr, tartib, sanash, guruh, JOIN, ichki so‘rov, CTE, CASE, sana, oyna, NULL. Qolgani — mashq va savolni aniq aytish. Keyingi mashqni o‘qituvchidek o‘qing: “Bu savol qaysi darsga tegishli?” — keyin yozing.</p>
""",
}
