"""
Python darslari — yangi boshlovchi uchun aniq, qadam-baqadam.
Har dars: oddiy tilda → nima uchun → qadamlar → kod → natija → chalkashlik → mashq.
"""

LECTURES = {
    "py-noldan-start": """
<h2>Oddiy tilda</h2>
<p>Tasavvur qiling: Excelda katakga <code>=2+2</code> yozasiz — javob chiqadi. Python ham shunga o‘xshaydi, faqat buyruqni katak emas, <strong>qatorga</strong> yozasiz. Bugun bitta narsani o‘rganamiz: <code>print</code> — “ekranga ko‘rsat”. Dasturchi bo‘lish shart emas. Bank, savdo yoki Excel bilan ishlasangiz ham — shu yeridan boshlaysiz. Xato chiqsa qo‘rqmang: bu “siz yomonsiz” degani emas, “shu qatorda tuzatish kerak” degani.</p>

<h2>Nima uchun kerak?</h2>
<p>Nima uchun umuman Python? Chunki har dushanba bir xil hisobotni qo‘lda yig‘ish charchatadi va xato keltiradi. Python shu ishni keyinroq avtomatlashtirishga yo‘l ochadi. Lekin avval eng oddiy narsa: kod yozdim → ekranda ko‘rdim. Shu his bo‘lmasa, keyingi darslar tushunarsiz tuyuladi.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Python o‘rnating: python.org yoki Windows da Microsoft Store. “Install” tugmasini bosing.</li>
  <li>Tekshirish: terminal (cmd) ochib <code>python --version</code> yozing. Raqam chiqsa — tayyor. Ba’zan <code>py --version</code> ishlaydi.</li>
  <li>Quyidagi 2 qatorni yozing (yoki platformadagi kod oynasida ishga tushiring).</li>
  <li>Natijani o‘qing: matn va son chiqishi kerak. Chiqmasa — qo‘shtirnoq yoki yozuvni tekshiring.</li>
  <li>Odat: har yangi g‘oyani avval 2–3 qator bilan sinang. Katta loyiha emas.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>print("Salom, tahlil!")
print(2 + 2)</pre>
<p><strong>Natija:</strong> Birinchi qator ekranga <code>Salom, tahlil!</code> yozadi. Ikkinchi qator <code>4</code> ni chiqaradi. <code>print(...)</code> — buyruq. Qavs ichidagi narsa — ko‘rsatiladigan narsa. Matn doim qo‘shtirnoq ichida: <code>"..."</code> yoki <code>'...'</code>. Sonni qo‘shtirnoqsiz yozasiz: <code>2 + 2</code>.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Qo‘shtirnoq ochilib yopilmasa — qizil xato. Har ochilgan qo‘shtirnoq yopilsin.</li>
  <li><code>Print</code> (katta P) ko‘pincha ishlamaydi. Yozing: <code>print</code> (kichik harf).</li>
  <li>Ortiqcha vergul, noto‘g‘ri qavs — xato. Avval namunani aynan ko‘chiring, keyin o‘zgartiring.</li>
  <li>Bugun 20 qatorlik dastur yozmang. 2 qator — yetarli g‘alaba.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>1) O‘z ismingizni print qiling. 2) <code>print(10 * 5)</code> ni ishga tushiring. 3) Natijani o‘qing: matn va 50 chiqishi kerak. Chiqmasa — qo‘shtirnoqni tekshiring.</p>
""",
    "py-noldan-run": """
<h2>Oddiy tilda</h2>
<p>Oldingi darsda bitta qatorni sinadingiz. Endi shu buyruqlarni <strong>faylga</strong> saqlaymiz. Fayl — retsept: ertaga ham bir xil ishlaydi. REPL — taomni tatib ko‘rish; fayl — retseptni daftarga yozish.</p>

<h2>Nima uchun kerak?</h2>
<p>Haftalik hisobot har dushanba bir xil. Uni har safar qayta yozmaslik uchun <code>.py</code> fayl kerak. Izoh (<code>#</code>) — kelajakdagi sizga eslatma.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Yangi fayl yarating: masalan <code>hello.py</code>.</li>
  <li>Ichiga kod va izoh yozing (pastdagi namunadek).</li>
  <li>Fayl turgan papkada terminal oching.</li>
  <li><code>python hello.py</code> deb yozing (Windows da ba’zan <code>py hello.py</code>).</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre># Bu izoh — Python o‘qimaydi
region = "Toshkent"
print(f"Filial: {region}")</pre>
<p><strong>Natija:</strong> <code>Filial: Toshkent</code> chiqadi. <code>region = ...</code> — qutiga nom berib, ichiga matn qo‘ydik. <code>f"...{region}..."</code> — matn ichiga o‘zgaruvchini joylash.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>“File not found” — noto‘g‘ri papkadasiz yoki fayl nomi xato.</li>
  <li>Faylni Word da saqlamang — oddiy matn (<code>.py</code>).</li>
  <li>Izohni kod deb yozmang: <code>#</code> bo‘lmasa, Python uni buyruq sanaydi.</li>
</ul>

<h2>Bugungi mashq</h2>
<p><code>my_report.py</code> yarating: 1 izoh, 1 o‘zgaruvchi, 1 <code>print</code>. Ishga tushiring.</p>
""",
    "py-noldan-errors": """
<h2>Oddiy tilda</h2>
<p>Xato — dushman emas. Qizil xabar (traceback) — “qayerda adashdingiz” xaritasi. Yangi boshlovchi qo‘rqadi; tajribali odam oxirgi qatorni o‘qiydi.</p>

<h2>Nima uchun kerak?</h2>
<p>Tahlilda 0 ga bo‘lish, noto‘g‘ri nom, yopilmagan qavs — kundalik. Xabarni o‘qiy olmasangiz, soatlab “nima bo‘ldi?” deb qolasiz.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Xabarning eng pastki qatoriga qarang — xato turi.</li>
  <li>Qator raqamiga boring — odatda shu yerda muammo.</li>
  <li>Bitta narsani o‘zgartiring, qayta ishga tushiring.</li>
  <li>Bir vaqtda 10 joyini o‘zgartirmang.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>revenue = 1000000
orders = 0
if orders == 0:
    aov = None
else:
    aov = revenue / orders
print(aov)</pre>
<p><strong>Natija:</strong> <code>None</code> chiqadi — “buyurtma yo‘q, AOV hisoblanmadi.” Dastur yiqilmaydi. Shartsiz <code>revenue / orders</code> yozsangiz — ZeroDivisionError.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li><strong>SyntaxError</strong> — yozuv buzilgan (qavs/qo‘shtirnoq).</li>
  <li><strong>NameError</strong> — nom topilmadi (<code>revnue</code> o‘rniga <code>revenue</code>).</li>
  <li><strong>ZeroDivisionError</strong> — 0 ga bo‘lish. Avval tekshiring.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>Ataylab bitta qo‘shtirnoqni ochiq qoldiring (SyntaxError), keyin tuzating. Keyin NameError ni ko‘ring.</p>
""",
    "py-nima": """
<h2>Oddiy tilda</h2>
<p>Bu kurs dasturchi emas, <strong>tahlilchi</strong> uchun. Siz Excel, savdo yoki bank bilan ishlaysiz. Python — takroriy tozalash va hisobni avtomatlashtirish vositasi. Har dushanba 12 ta CSV ni qo‘lda ochish o‘rniga — bitta skript.</p>

<h2>Nima uchun kerak?</h2>
<p>Excel tezkor filtr uchun ajoyib. Lekin 100 ming qator, 12 ta oylik fayl, bir nechta jadvalni ulash — Excel sekinlashadi va xato ko‘payadi. Python charchamaydi, lekin siz aniq yozishingiz kerak.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Qachon Excel: 5 daqiqalik filtr, kichik jadval, bitta pivot.</li>
  <li>Qachon Python: har oy ko‘p fayl, katta hajm, qayta-qayta bir xil ish.</li>
  <li>Ish muhiti: Notebook — tadqiqot; <code>.py</code> — barqaror pipeline.</li>
  <li>Odat: xom faylni o‘zgartirmang (<code>raw/</code>), har qadamga izoh yozing.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>print("Savdo tahlili boshlandi")
region = "Toshkent"
print(region)</pre>
<p><strong>Natija:</strong> Ekranda ikki qator: xabar va <code>Toshkent</code>. <code>region</code> — o‘zgaruvchi (Excel katakchasi nomi kabi, lekin xotirada).</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Python “sehrli dashboard” emas — siz yozganini bajaradi.</li>
  <li>Birinchi kundan katta loyiha yozmang: avval print, keyin fayl, keyin jadval.</li>
  <li>Excelni “yomon” demang — vositani vazifaga mos tanlang.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>3 ta print yozing: bugungi vazifa, shahar, va oddiy hisob (masalan 10*12). Har birini izohlab qo‘ying.</p>
""",
    "py-turlar": """
<h2>Oddiy tilda</h2>
<p>Excelda katakda 1200 ko‘rinsa, bu “son”. Python da esa ba’zan shu 1200 aslida <strong>matn</strong> bo‘ladi (qo‘shtirnoq ichida yoki CSV dan shunday kelgan). O‘zgaruvchi — quti nomi (<code>revenue</code>). Ichida nima yotishi — <strong>tur</strong> (sonmi, matnmi). Turini bilmasangiz, keyin “nima uchun ko‘paytirish ishlamadi?” deb qiynalasiz.</p>

<h2>Nima uchun kerak?</h2>
<p>CSV da amount ko‘pincha matn: <code>"1 200"</code>. Uni tozalamasdan QQS qo‘shsangiz — xato yoki g‘alati natija. Tahlilchilar vaqtining katta qismi shu: ko‘rinishdagi sonni haqiqiy songa aylantirish.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li><code>int</code> — butun son: 250 buyurtma.</li>
  <li><code>float</code> — o‘nli: narx, AOV, foiz.</li>
  <li><code>str</code> — matn: "Toshkent", telefon, SKU.</li>
  <li><code>bool</code> — True yoki False: VIP-mi?</li>
  <li><code>None</code> — qiymat yo‘q. Diqqat: bu 0 emas, bo‘sh satr ham emas.</li>
  <li>Har doim so‘rang: <code>type(x)</code> — “men nima ushlab turibman?”</li>
  <li>Matndan songa: avval tozalang (bo‘shliq/vergul), keyin <code>float(...)</code>.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>revenue = 12500000
orders = 250
aov = revenue / orders
print(type(aov), round(aov, 2))

s = "1 200"
n = float(s.replace(" ", "").replace(",", "."))
print(n)
print(type(n))</pre>
<p><strong>Natija:</strong> Birinchi blok: AOV float (masalan 50000.0) — bo‘lish Python da odatda o‘nli beradi. Ikkinchi blok: <code>1200.0</code> va uning turi <code>float</code>. Avval bo‘shliqni olib tashladik, keyin songa o‘girdik. Agar tozalamasdan <code>float("1 200")</code> desangiz — xato chiqadi.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li><code>amount = "150000"</code> bo‘lsa, <code>amount * 2</code> → <code>150000150000</code> (matn ikki marta), 300000 emas.</li>
  <li>Qo‘shtirnoq bormi-yo‘qmi — shunga qarang. Qo‘shtirnoq bo‘lsa, bu matn.</li>
  <li><code>True + 1</code> Python da 2. Hisobotda flag ni pulga qo‘shmang.</li>
  <li>Locale: ba’zi faylda nuqta ming ajratgich, boshqasida o‘nli. Avval 5 qatorni ko‘z bilan ko‘ring.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>1) <code>x = 10</code>, <code>y = "10"</code> yarating. Ikkala <code>type</code> ni chop eting. 2) <code>y</code> ni songa o‘girib, 2 ga ko‘paytiring. 3) <code>"3 500"</code> matnini 3500.0 qilib ko‘ring.</p>
""",
    "py-ifodalar": """
<h2>Oddiy tilda</h2>
<p>Son chiqardi. Endi uni odam o‘qiydigan qilamiz. Rahbar “50000” emas, “AOV: 50,000 so‘m (−10.7%)” ni xohlaydi. Bu dars — hisob + format.</p>

<h2>Nima uchun kerak?</h2>
<p>Foiz o‘zgarish formulasi chalkashadi. Qavsni unutsangiz — boshqa javob. Format esa hisobotning yarmi: to‘g‘ri son noto‘g‘ri yozilsa, ishonchsiz ko‘rinadi.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Arifmetika: <code>+</code> <code>-</code> <code>*</code> <code>/</code>, qavs Exceldagi kabi.</li>
  <li>Foiz o‘zgarish: <code>(yangi - eski) / eski</code>.</li>
  <li>f-string: matn ichiga o‘zgaruvchi.</li>
  <li>Taqqoslash: <code>==</code> tengmi; bitta <code>=</code> — “qo‘y”.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>aov = 50000
prev = 56000
change = (aov - prev) / prev
print(f"AOV o‘zgarishi: {change:.1%}")
print(f"AOV: {aov:,.0f} so‘m")</pre>
<p><strong>Natija:</strong> Taxminan <code>AOV o‘zgarishi: -10.7%</code> va <code>AOV: 50,000 so‘m</code>. <code>:.1%</code> — foiz ko‘rinishi; <code>:,.0f</code> — ming ajratgich.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Qavssiz formula — boshqa tartib, boshqa javob.</li>
  <li><code>"Toshkent" == "toshkent"</code> odatda False — harf katta-kichikligi muhim.</li>
  <li>Avval sonni print qiling, keyin chiroyli matn — xato sonni yashirmasin.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>O‘tgan oy 80, bu oy 92. Foiz o‘zgarishni hisoblab, f-string bilan chiroyli chiqaring.</p>
""",
    "py-if": """
<h2>Oddiy tilda</h2>
<p>Rahbar: “VIP larni ajrating.” Excelda IF. Python da ham shart: agar rost bo‘lsa — bir yo‘l, aks holda — boshqa. Odamdek o‘qiladi.</p>

<h2>Nima uchun kerak?</h2>
<p>Segmentatsiya, flag, ogohlantirish — hammasi shart. Noto‘g‘ri tartibda yozsangiz, VIP ham Regular bo‘lib qoladi.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Avval eng katta chegarani tekshiring (VIP).</li>
  <li>Keyin o‘rta (Regular).</li>
  <li>Qolganlar — New.</li>
  <li><code>and</code> — hammasi rost; <code>or</code> — bittasi yetadi.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>def segment(revenue):
    if revenue &gt;= 10000000:
        return "VIP"
    if revenue &gt;= 2000000:
        return "Regular"
    return "New"

print(segment(3500000))
print(segment(15000000))</pre>
<p><strong>Natija:</strong> <code>Regular</code> va <code>VIP</code>. 3.5 mln — Regular; 15 mln — VIP. <code>return</code> — “javob shu, to‘xta.”</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li><code>if amount = 0</code> — xato. Taqqoslash: <code>==</code>.</li>
  <li>Chegara tartibini teskari yozmang.</li>
  <li><code>if amount:</code> — 0 ni False deb yutadi; aniq <code>amount &gt; 0</code> yozing.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>O‘z qoidangizni yozing (masalan 5 mln VIP). 4 ta son bilan sinab ko‘ring.</p>
""",
    "py-loop": """
<h2>Oddiy tilda</h2>
<p>Uchta to‘lov: 120, 45, 80 ming. “50 mingdan kattalarini qo‘sh.” 3 katak — oson. 8 ming qator bo‘lsa? Tsikl: bir xil ishni har element uchun.</p>

<h2>Nima uchun kerak?</h2>
<p><code>for</code> — ro‘yxatdagi har biri. Kichik mantiqni o‘rganish uchun. Million qatorni sof Python for da yig‘ish sekin — keyinroq Pandas. Lekin g‘oya shu.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Ro‘yxat yarating.</li>
  <li>Yig‘indi uchun boshlang‘ich qiymat (0).</li>
  <li>Har element uchun shart tekshiring.</li>
  <li>Mos kelsa, yig‘indiga qo‘shing; oxirida print.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>amounts = [120000, 45000, 80000]
total = 0
for a in amounts:
    if a &gt;= 50000:
        total += a
print(total)</pre>
<p><strong>Natija:</strong> <code>200000</code> (120000 + 80000). 45000 tashlandi. <code>total += a</code> — “oldingi total ga a ni qo‘sh.”</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Tsikl ichida millionta print — noutbuk qiynaladi. Print oxirida.</li>
  <li><code>while</code> hisoblagich o‘zgarmasa — cheksiz tsikl. Tahlilda asosan <code>for</code>.</li>
  <li>Katta jadval — keyinroq <code>df["amount"].sum()</code>.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>5 ta summa ro‘yxati yarating. 100000 dan kattalarini qo‘shib chiqaring.</p>
""",
    "py-func": """
<h2>Oddiy tilda</h2>
<p>AOV ni 12 joyga nusxa qildingiz — birini unutdingiz. Funksiya: hisob <strong>bitta joyda</strong>. Nom berasiz, kerakli narsani olasiz, javob qaytarasiz.</p>

<h2>Nima uchun kerak?</h2>
<p>Qoida o‘zgarsa, 12 joyni emas, bitta funksiyani tuzatasiz. Test qilish oson: kichik sonlar bilan tekshirib, keyin katta fayl.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li><code>def</code> — yangi buyruq e’lon qilish.</li>
  <li>Qavs ichida kirish (parametrlar).</li>
  <li><code>return</code> — javob.</li>
  <li>0 ga bo‘lishni ichida tekshiring.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>def aov(revenue, orders):
    if orders == 0:
        return None
    return revenue / orders

print(aov(1200000, 40))
print(aov(500000, 0))</pre>
<p><strong>Natija:</strong> 30000.0 va <code>None</code>. Ikkinchi chaqiriqda dastur yiqilmaydi.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Nom: <code>aov</code>, <code>clean_amount</code> — tushunarli. <code>f1</code> — yo‘q.</li>
  <li>Funksiya ichida faqat hisob; faylga yozish tashqarida.</li>
  <li>0 ni sekin 1 ga almashtirmang — AOV ni yolg‘on qilasiz.</li>
</ul>

<h2>Bugungi mashq</h2>
<p><code>margin(revenue, cost)</code> funksiyasini yozing. cost=0 holatini ham o‘ylab ko‘ring.</p>
""",
    "py-collections": """
<h2>Oddiy tilda</h2>
<p>Ma’lumotni qayerga solish — muhim. Ro‘yxatmi? Unique to‘plammi? Kalit-qiymatmi? Noto‘g‘ri idish — keyin chalkash xato.</p>

<h2>Nima uchun kerak?</h2>
<p>Unique mijoz — set. Filial bo‘yicha tushum — dict. Kunlik cheklar — list. “Nima saqlayapman?” deb so‘rang, keyin tanlang.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li><code>list</code> — tartib bor, o‘zgaradi.</li>
  <li><code>tuple</code> — o‘zgarmas juftlik.</li>
  <li><code>set</code> — unique.</li>
  <li><code>dict</code> — kalit → qiymat.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>cities = ["Toshkent", "Samarqand", "Toshkent"]
print(set(cities))
revenue = {"Toshkent": 12500000}
print(revenue.get("Buxoro", 0))</pre>
<p><strong>Natija:</strong> Set da Toshkent bir marta. <code>Buxoro</code> yo‘q — 0 qaytadi (xato emas). <code>revenue["Buxoro"]</code> desangiz — KeyError.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li><code>ids * 2</code> — unique emas, ikki marta takror.</li>
  <li>CustomerID takrorlanishi normal (ko‘p xarid). Order_id takrori — odatda muammo.</li>
  <li>Dict kaliti list bo‘lmaydi.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>3 shaharli list yarating (bittasi takror). Unique qiling. Dict da 2 filial tushumini saqlang.</p>
""",
    "py-file": """
<h2>Oddiy tilda</h2>
<p>CSV — oddiy matn jadvali. Lekin “Exceldan saqlash” ba’zan o‘zbekcha harflarni buzadi yoki vergul o‘rniga nuqtali vergul qo‘yadi. Bu Python aybi emas — fayl qanday yozilgani.</p>

<h2>Nima uchun kerak?</h2>
<p>Noto‘g‘ri encoding/sep — butun jadval bitta ustun bo‘lib ketadi yoki “krakozyabra”. Avval 1–2 qatorni ko‘z bilan ko‘ring.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Faylni Notepad da ochib, ajratuvchini ko‘ring (<code>,</code> yoki <code>;</code>).</li>
  <li>Encoding: ko‘pincha <code>utf-8-sig</code> (Excel CSV).</li>
  <li>Xom faylni o‘zgartirmang — tozalanganini boshqa joyga yozing.</li>
  <li>Kichik misolda satrlarni bo‘lib ko‘ring, keyin Pandas.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>lines = ["city;amount", "Toshkent;120000", "Samarqand;80000"]
rows = [line.split(";") for line in lines]
print(rows)

import pandas as pd
df = pd.DataFrame({"city": ["Toshkent", "Samarqand"], "amount": [120000, 80000]})
print(df.head())</pre>
<p><strong>Natija:</strong> Avval ro‘yxatlar ro‘yxati; keyin kichik jadval. Haqiqiy ishda: <code>pd.read_csv(..., encoding="utf-8-sig", sep=";")</code>.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Separatorni taxmin qilmang.</li>
  <li>Xom CSV ni to‘g‘ridan tahrirlab saqlamang.</li>
  <li><code>with open(...)</code> — faylni yopishni unutmang.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>O‘zingiz 3 qatorli mini-CSV matnini list qilib yozing va <code>split</code> bilan ustunlarga bo‘ling.</p>
""",
    "py-except": """
<h2>Oddiy tilda</h2>
<p>Dastur yiqildi — yaxshi xabar: “shu yerda muammo.” Yomon narsa — xatoni yutib, jim noto‘g‘ri hisobot chiqarish.</p>

<h2>Nima uchun kerak?</h2>
<p>CSV da <code>12a</code> bo‘lsa, <code>int</code> xato beradi. Butun pipeline o‘chmasin, shu qatorni belgilang va jurnalga yozing.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Kutilgan xato atrofini <code>try</code> ga oling.</li>
  <li>Aniq tur: <code>except ValueError</code> (yalang <code>except:</code> emas).</li>
  <li>Fallback qo‘ying (None) va xabar chiqaring.</li>
  <li>Keyin nechtasi None ekanini sanang.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>try:
    orders = int("12a")
except ValueError:
    orders = None
    print("orders ustuni tozalanmadi")
print(orders)</pre>
<p><strong>Natija:</strong> Xabar chiqadi, <code>orders</code> — <code>None</code>. Dastur davom etadi.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Yalang <code>except:</code> hammasi yutadi — disk to‘la ham “jim”.</li>
  <li>Kutilmagan xato (sizning kodingiz) — yiqilsin, tuzating.</li>
  <li>Modullar: <code>import pandas as pd</code>; o‘z funksiyalaringizni alohida faylda saqlang.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>3 ta qiymatli list: "10", "abc", "7". Har birini int qilib ko‘ring; yomonlarini None qiling.</p>
""",
    "np-ndarray": """
<h2>Oddiy tilda</h2>
<p>Python list qulay, lekin millionta sonni birma-bir qo‘shish sekin. NumPy massivi — bir xil turdagi sonlar uchun tezkor hisob. Pandas ham ko‘pincha shu ustida turadi.</p>

<h2>Nima uchun kerak?</h2>
<p>O‘rtacha, og‘ish, filtr — tsiklsiz. Keyinroq DataFrame tushunarliroq bo‘lishi uchun avval massiv g‘oyasini biling.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li><code>import numpy as np</code>.</li>
  <li>Massiv yarating.</li>
  <li><code>mean</code>, <code>std</code> ni ko‘ring.</li>
  <li>Tur bir xil ekanini biling (dtype).</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>import numpy as np
x = np.array([10, 20, 30, 40], dtype=float)
print(x.mean())
print(x.std(ddof=1))</pre>
<p><strong>Natija:</strong> O‘rtacha 25.0; std — tanlama og‘ishi (Excel STDEV.S ga yaqin). <code>ddof=0</code> boshqacha — hisobotda qaysi ekanini yozing.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Matn aralashsa, massiv “buzuq” bo‘lishi mumkin.</li>
  <li>NumPy internet ochmaydi, SQL o‘rnini bosmaydi — faqat hisob.</li>
  <li>Kichik misolda o‘rganing, keyin katta ustunga o‘ting.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>5 ta narx massivi yarating. mean va max ni chop eting.</p>
""",
    "np-index": """
<h2>Oddiy tilda</h2>
<p>Uchta narx, hammaga 12% chegirma. Excelda formulani pastga tortasiz. NumPy da: massiv <code>* 0.88</code>. Tsikl yo‘q. Shartga moslarini kesish — mask.</p>

<h2>Nima uchun kerak?</h2>
<p>“100 mingdan katta to‘lovlar” — SQL WHERE ga o‘xshash, lekin bitta ustun (massiv) uchun.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Massiv yarating.</li>
  <li>Shart yozing: <code>price &gt;= 100</code> → True/False massivi.</li>
  <li>Shu niqob bilan kesing: <code>price[price &gt;= 100]</code>.</li>
  <li>Skalyar ko‘paytirishni sinang.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>import numpy as np
price = np.array([100, 250, 80])
print(price[price &gt;= 100])
print(price * 0.88)</pre>
<p><strong>Natija:</strong> Birinchi: 100 va 250. Ikkinchi: har narx * 0.88.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Ba’zi kesmalar view — asl massivga bog‘liq. Kerak bo‘lsa <code>.copy()</code>.</li>
  <li>Indeks 0 dan boshlanadi.</li>
  <li>Bu matn qidiruv yoki join emas — shartga mos elementlar.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>Massivda 4 ta summa. 50000 dan kattalarini chiqaring va hammaga +10% qo‘llang.</p>
""",
    "np-nan": """
<h2>Oddiy tilda</h2>
<p>O‘rtacha hisobladiz — javob <code>nan</code>. Bu “buzilish” emas: massivda teshik bor (noma’lum qiymat). Bitta NaN oddiy mean ni “zaharlaydi”.</p>

<h2>Nima uchun kerak?</h2>
<p>0 — “savdo yo‘q” (fakt). NaN — “bilmaymiz”. Aralashtirsangiz, KPI yolg‘on gapiradi.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>NaN bor-yo‘qligini biling.</li>
  <li>Oddiy mean va nanmean farqini ko‘ring.</li>
  <li>Avval nechta NaN ekanini sanang.</li>
  <li>Keyin siyosat: tashlash / to‘ldirish / so‘rash.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>import numpy as np
x = np.array([10, np.nan, 30])
print(np.mean(x))
print(np.nanmean(x))</pre>
<p><strong>Natija:</strong> Birinchi — nan. Ikkinchi — 20.0 (teshikni o‘tkazib yuboradi).</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Darhol hammaga 0 qo‘ymang — yashirish.</li>
  <li>40% NaN bo‘lsa — avval manbani so‘rang.</li>
  <li>Keyingi modulda Pandas da flag qo‘yamiz.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>4 elementli massivda 1 ta NaN qiling. mean va nanmean ni solishtiring.</p>
""",
    "pd-df": """
<h2>Oddiy tilda</h2>
<p>Excelda Table, SQL da natija jadvali. Pandas da bu — <strong>DataFrame</strong>: nomlangan ustunlar + qatorlar. Bitta ustun — Series.</p>

<h2>Nima uchun kerak?</h2>
<p>Tahlilchining asosiy idishi. Filtr, groupby, merge — hammasi DataFrame ustida. Avval jadvalni “ko‘rish” odatini o‘rganing.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>DataFrame yarating (lug‘atdan).</li>
  <li><code>head()</code> — birinchi qatorlar.</li>
  <li><code>dtypes</code> — har ustun turi.</li>
  <li><code>shape</code> — (qator, ustun).</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>import pandas as pd
df = pd.DataFrame({
    "city": ["Toshkent", "Samarqand"],
    "amount": [120000, 80000],
})
print(df.head())
print(df.dtypes)
print(df.shape)</pre>
<p><strong>Natija:</strong> 2×2 jadval ko‘rinadi; amount — int; shape (2, 2). Yangi CSV da tartib: head → dtypes → shape → keyin isna.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Darhol grafik/model — yo‘q. Avval ko‘z bilan o‘qing.</li>
  <li><code>df["city"]</code> — Series; <code>df[["city","amount"]]</code> — kichik DataFrame.</li>
  <li>Ustun nomlarini keyinroq tozalaymiz (snake_case).</li>
</ul>

<h2>Bugungi mashq</h2>
<p>3 shaharli kichik DataFrame yozing. head, dtypes, shape ni chop eting.</p>
""",
    "pd-filter": """
<h2>Oddiy tilda</h2>
<p>SQL WHERE ning ukasi. “Faqat Toshkent” yoki “amount katta.” Avval har qator uchun True/False niqob, keyin shu niqob bilan kesasiz.</p>

<h2>Nima uchun kerak?</h2>
<p>Katta jadvaldan kerakli qatorlarni ajratmasangiz, KPI chalkashadi. Filtr — tahlilning asosiy pichoqi.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Shart yozing: <code>df["city"] == "Toshkent"</code>.</li>
  <li>Bir nechta shart: <code>&amp;</code> (va), <code>|</code> (yoki) — har biri qavsda.</li>
  <li>Python <code>and</code>/<code>or</code> bu yerda ishlamaydi.</li>
  <li>Kerakli ustunlarni ham kesing.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>import pandas as pd
df = pd.DataFrame({"city": ["Toshkent", "Buxoro"], "amount": [5, 12]})
print(df[(df["city"] == "Toshkent") | (df["amount"] &gt; 10)])</pre>
<p><strong>Natija:</strong> Toshkent qatori ham, amount=12 qatori ham chiqadi.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Qavssiz <code>&amp;</code> — xato yoki noto‘g‘ri niqob.</li>
  <li>Matnda yashirin bo‘shliq bo‘lsa, filtr “topmaydi” — trim keyinroq.</li>
  <li><code>df.city</code> qisqa, lekin <code>df["city"]</code> xavfsizroq.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>3 qatorli df yarating. Faqat amount &gt; 100000 qatorlarni chiqaring.</p>
""",
    "pd-assign": """
<h2>Oddiy tilda</h2>
<p>Amount bor, QQS yo‘q. Yangi ustun — hisoblangan maydon. Xom CSV ni emas, xotiradagi jadvalni kengaytirasiz.</p>

<h2>Nima uchun kerak?</h2>
<p>Har yangi ko‘rsatkich (QQS, chegirma, flag) — yangi ustun. Nomini rost yozing: 12% bo‘lsa, 15% ni ham vat demang.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Oddiy usul: <code>df["vat"] = df["amount"] * 0.12</code>.</li>
  <li>Yoki <code>assign</code> — zanjir uchun qulay.</li>
  <li>Filtrlangan bo‘lakka yozishda ehtiyot (SettingWithCopy).</li>
  <li>Xavfsiz: <code>loc</code> bilan yozing yoki <code>.copy()</code> oling.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>import pandas as pd
df = pd.DataFrame({"amount": [100, 200]})
df = df.assign(vat=lambda x: x["amount"] * 0.12)
print(df)</pre>
<p><strong>Natija:</strong> amount va vat ustunlari: 12.0 va 24.0.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Filtrlab olingan bo‘lakka jim yozmang — natija g‘alati bo‘lishi mumkin.</li>
  <li>Uzun mantiqni lambda ichiga tiqmang — alohida funksiya.</li>
  <li>Yangi ustun — yangi haqiqat; nom yolg‘on bo‘lmasin.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>amount ustuniga 5% chegirma ustunini qo‘shing va chop eting.</p>
""",
    "pd-na": """
<h2>Oddiy tilda</h2>
<p>Bo‘sh katak. Pandas da ko‘pincha NaN — “noma’lum”. Bu 0 emas. 0 — do‘kon yopiq (fakt). NaN — fayl kelmagan / kiritilmagan.</p>

<h2>Nima uchun kerak?</h2>
<p>NaN ni ko‘r-ko‘rona 0 qilsangiz, o‘rtacha va konversiya yolg‘on chiqadi. Avval ulushini o‘lchang, keyin siyosat yozing.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li><code>isna()</code> bilan teshiklarni toping.</li>
  <li>Ulush: <code>isna().mean()</code>.</li>
  <li>Flag ustuni qo‘ying (keyinroq ajratib ko‘rish uchun).</li>
  <li>To‘ldirish yoki tashlash — biznes qoidasi bilan.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>import pandas as pd
df = pd.DataFrame({"amount": [10, None, 30]})
print(df["amount"].isna().mean())
df["amount_missing"] = df["amount"].isna()
df["amount"] = df["amount"].fillna(df["amount"].median())
print(df)</pre>
<p><strong>Natija:</strong> Ulush 1/3. Flag True/False. Median bilan to‘ldirilgan qiymat — siyosat misoli, avtomatik haqiqat emas.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Hamma NaN → 0 — eng yomon odatlardan.</li>
  <li>Kalit maydon (order_id) bo‘sh — odatda tashlash + jurnal.</li>
  <li>Siyosatni yozib qo‘ying — ikki kishi boshqacha tozalamasin.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>4 qatorli df da 1 NaN qiling. Ulushini chop eting va flag qo‘ying.</p>
""",
    "pd-dup": """
<h2>Oddiy tilda</h2>
<p>Bir order_id ikki marta. Ba’zan eksport takrori, ba’zan join xatosi. Customer_id takrori esa normal (ko‘p xarid).</p>

<h2>Nima uchun kerak?</h2>
<p>Noto‘g‘ri subset bilan drop_duplicates — butun savdoni o‘chirib yuborishingiz mumkin.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Qaysi ustun unique bo‘lishi kerakligini aniqlang.</li>
  <li><code>duplicated(...).sum()</code> — nechta ortiqcha.</li>
  <li>Keyin drop (keep first/last — qoida bilan).</li>
  <li>Nechta qator ketdi — jurnalga.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>import pandas as pd
df = pd.DataFrame({"order_id": [1, 1, 2], "amount": [10, 10, 5]})
print(df.duplicated(subset=["order_id"]).sum())
print(df.drop_duplicates("order_id"))</pre>
<p><strong>Natija:</strong> 1 ta dublikat belgi; keyin 2 qator qoladi.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Customer_id ni unique qilmang — revenue erib ketadi.</li>
  <li>Bir xil id, turli amount — konflikt; odam so‘rang.</li>
  <li>Avval sanang, keyin o‘chiring.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>5 qatorli df da 2 xil order_id takrorini yasang. duplicated sum va drop ni ko‘ring.</p>
""",
    "pd-cast": """
<h2>Oddiy tilda</h2>
<p>Yana “1 200” matni — endi butun ustun. Qo‘lda float() 50 ming marta emas: tozalash + <code>to_numeric</code>. Yomon katak — NaN bo‘lsin, dastur yiqilmasin.</p>

<h2>Nima uchun kerak?</h2>
<p>Tur belgilanmasa, sum/groupby ishlamasligi yoki matnni “qo‘shishi” mumkin.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Bo‘shliq/vergulni tozalang.</li>
  <li><code>to_numeric(..., errors="coerce")</code>.</li>
  <li>Nechta NaN chiqdi — sanang.</li>
  <li>Keyin siyosat (tashlash/to‘ldirish).</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>import pandas as pd
s = pd.Series([" 1 200 ", "abc", "3,5"])
clean = s.str.replace(" ", "", regex=False).str.replace(",", ".", regex=False)
print(pd.to_numeric(clean, errors="coerce"))</pre>
<p><strong>Natija:</strong> 1200.0, NaN, 3.5. <code>abc</code> 0 ga aylanmadi — yaxshi.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Darhol <code>astype(int)</code> — bitta “abc” da yiqiladi.</li>
  <li>Avval coerce, keyin qaror.</li>
  <li>Ustun nomlarini ham tozalang (strip, snake_case).</li>
</ul>

<h2>Bugungi mashq</h2>
<p>Series: "10", "2 000", "x". to_numeric coerce qiling va NaN sonini chop eting.</p>
""",
    "pd-groupby": """
<h2>Oddiy tilda</h2>
<p>SQL GROUP BY: har shahar uchun yig‘indi. Pandas da xuddi shu: uyum-uyum qilib, har uyumda sum/count.</p>

<h2>Nima uchun kerak?</h2>
<p>Region, kanal, oy bo‘yicha KPI — hisobotning yuragi. count vs nunique farqini biling.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Guruh kalitini tanlang (region).</li>
  <li><code>agg</code> bilan o‘lchovlar yozing.</li>
  <li>Buyurtma soni uchun odatda <code>nunique(order_id)</code>.</li>
  <li>Natijani o‘qing: qaysi guruh katta/kichik.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>import pandas as pd
df = pd.DataFrame({
    "region": ["Toshkent", "Toshkent", "Buxoro"],
    "amount": [10, 20, 5],
    "oid": [1, 2, 3],
})
print(df.groupby("region").agg(revenue=("amount", "sum"), n=("oid", "nunique")))</pre>
<p><strong>Natija:</strong> Toshkent: revenue 30, n 2. Buxoro: 5, 1.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>count qatorlarni sanaydi; dublikat bo‘lsa shishadi.</li>
  <li>WHERE oldin, groupby keyin.</li>
  <li>Natija ustuniga tushunarli nom bering.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>4 qatorli df da 2 region. region bo‘yicha sum va count chiqaring.</p>
""",
    "pd-merge": """
<h2>Oddiy tilda</h2>
<p>Ism customers da, to‘lov orders da. Excel VLOOKUP / SQL JOIN. Pandas: <code>merge</code>. Qanday ulash — savolga bog‘liq (left/inner).</p>

<h2>Nima uchun kerak?</h2>
<p>Noto‘g‘ri join — qatorlar ko‘payib (fan-out), revenue 3 marta bo‘lishi mumkin.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Kalit ustunni aniqlang.</li>
  <li>Chap jadvalni tanlang (odatda fakt: orders).</li>
  <li><code>how="left"</code> — chapdagi hech kimni yo‘qotma.</li>
  <li>Merge oldin/keyin <code>len</code> ni solishtiring.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>import pandas as pd
orders = pd.DataFrame({"cid": [1, 2], "amount": [10, 20]})
cust = pd.DataFrame({"cid": [1, 3], "name": ["Ali", "Nodira"]})
print(orders.merge(cust, on="cid", how="left"))</pre>
<p><strong>Natija:</strong> Ali ulanadi; cid=2 uchun name NaN; Nodira bu natijada yo‘q (buyurtmasi yo‘q).</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>O‘ng jadvalda kalit dublikat — fan-out.</li>
  <li>1 va "1" mos kelmasligi mumkin — tur bir xil bo‘lsin.</li>
  <li>validate="many_to_one" — himoya.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>Kichik orders/customers yarating. left merge qiling va len ni tekshiring.</p>
""",
    "pd-dt": """
<h2>Oddiy tilda</h2>
<p>Sana ko‘pincha matn. Matnni oy bo‘yicha to‘g‘ri guruhlab bo‘lmaydi. Avval haqiqiy sana: <code>to_datetime</code>.</p>

<h2>Nima uchun kerak?</h2>
<p>Trend, oylik KPI, recency — hammasi to‘g‘ri sanaga bog‘liq. Noto‘g‘ri dayfirst — butun oy siljiydi.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Ustunni datetime qiling.</li>
  <li>Oy kesimi: <code>.dt.to_period("M")</code>.</li>
  <li>groupby bilan yig‘ing.</li>
  <li>Yomon sanalar — NaT; sanang.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>import pandas as pd
df = pd.DataFrame({
    "dt": ["2024-01-31", "2024-02-01"],
    "amount": [10, 20],
})
df["dt"] = pd.to_datetime(df["dt"])
print(df.groupby(df["dt"].dt.to_period("M"))["amount"].sum())</pre>
<p><strong>Natija:</strong> Yanvar 10, fevral 20.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>03/04/2024 — martmi apreldami? ISO YYYY-MM-DD tinchroq.</li>
  <li>dayfirst ni faqat bilganingizda qo‘ying.</li>
  <li>Avval datetime, keyin period — str[:7] ga ishonmang.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>3 sana + amount. Oylik summani chiqaring.</p>
""",
    "pd-eda": """
<h2>Oddiy tilda</h2>
<p>Yangi dataset. Qo‘l qichishadi: darhol pie. To‘xtang. EDA — savol berish: hajm, tur, missing, taqsimot, anomaliya. Dashboard dan oldin.</p>

<h2>Nima uchun kerak?</h2>
<p>Chiroyli yolg‘on chizmaslik uchun. EDA insight urug‘ini beradi: “o‘rtacha shishgan — bitta katta chek.”</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>shape, dtypes, isna.</li>
  <li>describe — sonli taqsimot.</li>
  <li>value_counts — kategoriyalar.</li>
  <li>Kesimlar (groupby) va qisqa xulosa (5 jumla).</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>import pandas as pd
df = pd.DataFrame({"amount": [1, 2, 3, 1000], "city": ["A", "A", "B", "B"]})
print(df.describe())
print(df["city"].value_counts(normalize=True))</pre>
<p><strong>Natija:</strong> describe da 1000 dum ko‘rinadi; value_counts ulushni ko‘rsatadi.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Darhol dropna/model/pie — yo‘q.</li>
  <li>1000 xatomi yoki ulkan buyurtmami — EDA savolni ochadi, hukm emas.</li>
  <li>Har EDA oxirida 5 aniq jumla yozing.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>Kichik df da describe + value_counts qiling va 3 jumlalik xulosa yozing.</p>
""",
    "py-mpl": """
<h2>Oddiy tilda</h2>
<p>Grafik rahbar uchun. Maqsad — trendni 3 soniyada tushunish. 3D pie va 20 rang — ishonchni o‘ldiradi.</p>

<h2>Nima uchun kerak?</h2>
<p>Oylik savdo — chiziq. Region taqqoslash — ustun. Taqsimot — hist. Bir grafik — bir savol.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Ma’lumotni tayyorlang (ro‘yxat yoki df).</li>
  <li>Mos turdagi chart tanlang.</li>
  <li>Title va o‘q nomlarini yozing.</li>
  <li>Notebookda show; skriptda savefig.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
months = ["Yan", "Fev", "Mar"]
revenue = [12500000, 11800000, 13100000]
plt.plot(months, revenue)
plt.title("Oylik savdo")
plt.ylabel("so‘m")
plt.tight_layout()
print("grafik tayyor")</pre>
<p><strong>Natija:</strong> Chiziqli grafik yig‘iladi (Agg rejimida faylga saqlash mumkin). Muhimi — title/ylabel.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Pie ni deyarli ishlatmang.</li>
  <li>Shkala yolg‘on aytmasin.</li>
  <li>12 chiziq birga — hech kim o‘qimaydi.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>3 oylik revenue bilan chiziq chizing, title qo‘ying.</p>
""",
    "py-sns": """
<h2>Oddiy tilda</h2>
<p>Seaborn — statistik grafiklar uchun qulay qatlam (boxplot, heatmap). Ichida matplotlib, lekin defaultlari tahlilchiga yaqin.</p>

<h2>Nima uchun kerak?</h2>
<p>Dum/outlier ni ko‘rish — pie dan ko‘ra muhimroq. Korrelyatsiya — savol generator, sabab-oqibat emas.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>DataFrame tayyorlang.</li>
  <li>boxplot: kategoriya × son.</li>
  <li>corr + heatmap — ehtiyot bilan.</li>
  <li>Grafik ostiga 1 jumla insight yozing.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>import matplotlib
matplotlib.use("Agg")
import pandas as pd
import seaborn as sns
df = pd.DataFrame({"region": ["Toshkent", "Toshkent", "Buxoro", "Buxoro"], "amount": [80, 1200, 40, 55]})
ax = sns.boxplot(data=df, x="region", y="amount")
print(type(ax).__name__)</pre>
<p><strong>Natija:</strong> Boxplot obyekti yaratiladi. Toshkentda 1200 — dum/outlier sifatida ko‘zga tashlanadi.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Korrelyatsiya sabab emas.</li>
  <li>Chiroy baholanmaydi — insight jumlasi baholanadi.</li>
  <li>Stakeholderga kerak bo‘lmasa, murakkab CI ni majburan qo‘ymang.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>2 regionli df da boxplot qiling va 1 jumla yozing: qayerda dum bor?</p>
""",
    "py-kpi": """
<h2>Oddiy tilda</h2>
<p>KPI — qisqartma emas, <strong>kelishilgan ta’rif</strong>. Ikki kishi AOV ni boshqacha hisoblasa, ikkalasi ham “to‘g‘ri” deb urishadi.</p>

<h2>Nima uchun kerak?</h2>
<p>Koddan oldin qog‘oz: nima kiradi, nima chiqmaydi. Keyin funksiya — bitta joyda ta’rif.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Ta’rifni yozing (masalan AOV = revenue / unique orders).</li>
  <li>Funksiya qaytarsin (print qilmasin).</li>
  <li>0 bo‘linmani xavfsiz qiling.</li>
  <li>Kichik df da qo‘lda tekshiring.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>import pandas as pd
df = pd.DataFrame({"order_id": [1, 2], "amount": [100000, 200000]})
def kpi_summary(df):
    orders = df["order_id"].nunique()
    revenue = df["amount"].sum()
    return {"orders": orders, "revenue": revenue, "aov": revenue / orders if orders else None}
print(kpi_summary(df))</pre>
<p><strong>Natija:</strong> orders 2, revenue 300000, aov 150000.0.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Bekor cheklar kiritiladimi — ta’rifda yozing.</li>
  <li>“Faol mijoz” ni hujjatlashtiring.</li>
  <li>Ta’rif o‘zgarsa, bitta funksiyani yangilang.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>O‘z kpi_summary ni yozing va 3 qatorli df da tekshiring.</p>
""",
    "py-rfm": """
<h2>Oddiy tilda</h2>
<p>Mijoz 120 kundan beri xarid qilmagan — bu “jimlik”. Recency: so‘nggi xariddan beri necha kun. RFM ning R qismi.</p>

<h2>Nima uchun kerak?</h2>
<p>Qayta faollashtirish ro‘yxati uchun. Chegara (90 kun) — biznes parametri, sehrli son emas.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Hisobot sanasini (as_of) belgilang.</li>
  <li>Har mijozning oxirgi sanasini oling (max).</li>
  <li>Kun farqini hisoblang.</li>
  <li>Chegaradan katta/jimlarni sanang.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>import pandas as pd
df = pd.DataFrame({
    "customer_id": [1, 1, 2, 3],
    "order_date": pd.to_datetime(["2024-05-01", "2024-06-01", "2024-03-01", "2024-01-15"]),
})
as_of = pd.Timestamp("2024-08-01")
last = df.groupby("customer_id")["order_date"].max()
recency = (as_of - last).dt.days
print(recency)
print((recency &gt;= 90).sum())</pre>
<p><strong>Natija:</strong> Har mijoz uchun recency kunlari; 90+ nechta ekani chiqadi.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>Bekor buyurtmani “oxirgi xarid” deb olma — status filtri.</li>
  <li>customer_id bo‘sh mehmon cheklari — alohida.</li>
  <li>“Churn albatta” deb yozmang — “90 kun jim, qoidaga ko‘ra aloqa”.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>Kichik df da recency hisoblang. 60 kun chegarasi bilan nechta jim?</p>
""",
    "py-final": """
<h2>Oddiy tilda</h2>
<p>Oxirgi dars — yangi sehr yo‘q. Bitta savdo CSV: tozalash, KPI, kesim, 2 grafik, 5 tavsiya. “Yaxshilash kerak” tavsiya emas — aniq songa tayaning.</p>

<h2>Nima uchun kerak?</h2>
<p>Ishda shu ketma-ketlik: turlar → NaN siyosati → kalit dublikat → KPI → grafik → gap. Darhol model yoki hamma ustunga dropna — yo‘q.</p>

<h2>Qadam-baqadam</h2>
<ol>
  <li>Tozalash jurnali yozing (nechta bor edi / nima ketdi).</li>
  <li>Oylik revenue, AOV, unique mijoz — ta’rif bilan.</li>
  <li>Region × kanal kesimi.</li>
  <li>2 grafik + 5 aniq tavsiya.</li>
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>import pandas as pd
df = pd.DataFrame({
    "order_id": [1, 2, 3, 4],
    "customer_id": [10, 10, 11, 12],
    "amount": [100000, 200000, 150000, 80000],
    "order_date": pd.to_datetime(["2024-01-05", "2024-01-20", "2024-02-03", "2024-02-18"]),
})
monthly = (
    df.groupby(df["order_date"].dt.to_period("M"))
      .agg(revenue=("amount", "sum"), orders=("order_id", "nunique"), customers=("customer_id", "nunique"))
)
monthly["aov"] = monthly["revenue"] / monthly["orders"]
print(monthly)</pre>
<p><strong>Natija:</strong> Oy kesimida revenue/orders/customers/aov — hisobot umurtqasi.</p>

<h2>Chalkashmaslik</h2>
<ul>
  <li>20 ta 3D chart — loyiha emas.</li>
  <li>Faqat print(df) — yetarli emas.</li>
  <li>Har tavsiya: kimga, nima qilsin, qaysi songa tayanadi.</li>
</ul>

<h2>Bugungi mashq</h2>
<p>Shu namunaviy df dan oylik jadvalni o‘zingiz yig‘ing va 2 jumlalik insight yozing.</p>
""",
}
