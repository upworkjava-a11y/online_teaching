"""
Python darslari — o‘qituvchi ovozida, noldan.
Har dars talaba bilan gaplashgandek yozilgan; bir xil qolip takrorlanmaydi.
"""

LECTURES = {
    "py-nima": """
<p>Salom. Agar siz hech qachon Python yozmagan bo‘lsangiz — yaxshi. Bu kurs dasturchi tayyorlamaydi. Siz tahlilchisiz: savdo, bank, CSV. Excelni bilasiz deb hisoblayman. Python shu ishni <em>takrorlab, xatosiz</em> qilish uchun.</p>

<p>Haftalik savdo hisobotini tasavvur qiling. Har dushanba 12 ta filial faylini ochasiz, vergulni nuqtaga almashtirasiz, Toshkentni filtrlaysiz, AOV yozasiz. Bir marta unutsangiz — rahbar boshqa raqam ko‘radi. Python skripti esa: ochadi, tozalaydi, hisoblaydi. Bir marta yozasiz, har hafta ishga tushirasiz.</p>

<p>Qachon Excel yetarli? Tezkor 5 daqiqalik filtr, 200 qator, bitta pivot. Qachon Python? Har oy 24 ta CSV, 100 ming qator, bir nechta jadvalni ulash, “o‘tgan oy bilan solishtir” ni avtomatlashtirish. Excel charchaydi va sekinlashadi. Python charchamaydi — lekin siz aniq yozishingiz kerak.</p>
<table>
  <tr><th>Vazifa</th><th>Excel</th><th>Python</th></tr>
  <tr><td>Tezkor filtr</td><td>Qulay</td><td>Ortiqcha</td></tr>
  <tr><td>12 ta oylik faylni birlashtirish</td><td>Charchatadi</td><td>Ideal</td></tr>
  <tr><td>100 ming+ qator, join</td><td>Sekin / xato</td><td>Pandas</td></tr>
</table>

<p>Ish muhiti ikkita. <strong>Jupyter Notebook</strong> — tadqiqot: “shu ustunni ko‘ray”, grafik, izoh. <strong>.py skript</strong> — ishlab chiqarish: har dushanba bir xil pipeline. Ikkisini ham biling. Avval notebookda tushunasiz, keyin barqaror qismni skriptga ko‘chirasiz.</p>

<p>Birinchi qator. Qo‘rqitadigan narsa yo‘q — shunchaki yozasiz, ekranga chiqadi:</p>
<pre>print("Savdo tahlili boshlandi")
region = "Toshkent"
print(region)</pre>
<p><code>print</code> — “ko‘rsat”. <code>region = "Toshkent"</code> — qutiga nom berib, ichiga matn qo‘ydik. Bu — <strong>o‘zgaruvchi</strong>. Exceldagi katakcha nomi kabi, lekin xotirada yotadi.</p>

<p>Uchta odat, shu kundan. Xom faylni o‘zgartirmang — <code>raw/</code> papkada saqlang, tozalanganini boshqa joyga yozing. Har qadamga izoh: nima va nima uchun. Natijani qayta ishlatish mumkin qiling — keyinroq funksiya o‘rganamiz. Hozir: print ishlasa, siz yo‘ldasiz.</p>
""",
    "py-turlar": """
<p>Dushanba. <code>sales.csv</code> ni ochdingiz. Amount ustunida <code>1 200</code> yozilgan. Ko‘z “ming ikki yuz so‘m” deydi. Python esa: bu <strong>matn</strong>. Unga <code>* 1.12</code> (QQS) qilsangiz — ko‘paytirish emas, g‘alati narsa yoki xato. Tahlil vaqtining katta qismi shu: ko‘rinishdagi son aslida son emas.</p>

<p>O‘zgaruvchi — nom. Ichida nima yotishi — <strong>tur</strong>. Beshta asosiysi yetarli:</p>
<ul>
  <li><code>int</code> — butun son: buyurtma soni, 250</li>
  <li><code>float</code> — o‘nli: narx, AOV, foiz</li>
  <li><code>str</code> — matn: "Toshkent", SKU, telefon</li>
  <li><code>bool</code> — True yoki False: VIP-mi?</li>
  <li><code>None</code> — qiymat yo‘q. SQL dagi NULL ga yaqin. 0 emas, bo‘sh satr ham emas</li>
</ul>

<p>Bank misoli. Toshkent filiali tushumi va buyurtmalar. AOV — o‘rtacha chek: tushumni buyurtmaga bo‘lamiz.</p>
<pre>revenue = 12_500_000
orders = 250
aov = revenue / orders
print(type(aov), round(aov, 2))</pre>
<p><code>12_500_000</code> dagi pastki chiziq — o‘qish uchun, Python uni e’tiborsiz qiladi. Bo‘lish <code>/</code> har doim <code>float</code> beradi. <code>type(aov)</code> ni yozish odat bo‘lsin: “men nima ushlab turibman?”</p>

<p>Matndan songa. CSV da bo‘shliq, vergul, “so‘m” yozuvi bo‘lishi mumkin. Avval tozalaysiz, keyin o‘girasiz:</p>
<pre>s = "1 200"
n = float(s.replace(" ", "").replace(",", "."))
print(n)</pre>
<p>Locale ni unutmang: ba’zi faylda <code>1.200</code> ming, boshqasida o‘nli. Avval 5 qatorni ko‘z bilan ko‘ring, keyin ommaviy konvertatsiya.</p>

<p>Tuzoq, yodda qolsin: <code>True + 1</code> Python da 2. Boolean ichida 1/0 yotadi. Hisobotda flag ni tushumga qo‘shmang. Yana: <code>amount = "150000"</code> bo‘lsa, <code>amount * 2</code> sonni ikkilamaydi — matnni ikki marta yozadi: <code>150000150000</code>. Qo‘shtirnoq bor-yo‘qligiga qarang.</p>
""",
    "py-ifodalar": """
<p>Son chiqardi. Endi uni odam o‘qiydigan qilish kerak. Rahbar “50000” emas, “AOV: 50,000 so‘m” ni xohlaydi. Tahlilchi esa o‘zgarishni foizda ko‘rsatadi. Bu dars — hisob va <em>format</em>.</p>

<p>Arifmetika odatiy: <code>+</code> <code>-</code> <code>*</code> <code>/</code>. Qavs ishlatamiz, Exceldagi kabi. Foiz o‘zgarish — eng ko‘p chalkashadigan formula. Yangi minus eski, keyin eskiga bo‘lish:</p>
<pre>aov = 50000
prev = 56000
change = (aov - prev) / prev
print(f"AOV o‘zgarishi: {change:.1%}")</pre>
<p>Natija taxminan −10.7%. Qavsni unutsangiz, avval bo‘lish, keyin ayirish — boshqa dunyo. <code>(yangi - eski) / eski</code> ni o‘zbekcha aytib yozing.</p>

<p><code>f"..."</code> — f-string. Qavs ichidagi o‘zgaruvchi matnga tushadi. <code>{change:.1%}</code> — bitta o‘nli, foiz ko‘rinishi. <code>{aov:,.0f}</code> — ming ajratgich, butun so‘m. Format — hisobotning yarmi.</p>

<p>Taqqoslash. <code>==</code> tengmi, <code>!=</code> teng emas, <code>&gt;</code> katta, <code>&lt;</code> kichik. Bitta tenglik <code>=</code> — “qo‘y”, ikkitasi — “tengmi?”. Matn sezgir: <code>"Toshkent" == "toshkent"</code> odatda False. Avval <code>.casefold()</code> yoki kelishilgan holda kichik harf.</p>

<p>Biznes ildizi, keyingi darsga: agar AOV o‘tgan oydan 10% past bo‘lsa — ogohlantirish. Bugun shu ifodani hisoblay olasiz. Ertaga <code>if</code> bilan gapga aylantiramiz.</p>

<p>Kichik odat: avval print qilib sonni ko‘ring, keyin chiroyli matn. Chiroyli matn noto‘g‘ri sonni yashirmasin.</p>
""",
    "py-if": """
<p>Rahbar: “VIP larni ajrating.” Excelda IF. Python da ham shart — lekin o‘qish osonroq, test qilish mumkin. G‘oya: agar shart rost bo‘lsa, shu yo‘l; aks holda boshqa.</p>

<p>Savdo qoidasi, Toshkent tarmog‘i:</p>
<pre>agar revenue &gt;= 10 mln → "VIP"
aks holda agar revenue &gt;= 2 mln → "Regular"
aks holda → "New"</pre>
<p>2 million aniq Regular. 10 milliondan kam, 2 milliondan kam — New. Tartib muhim: avval katta chegara. Teskarisini yozsangiz, VIP ham Regular ga tushib qoladi.</p>
<pre>def segment(revenue):
    if revenue &gt;= 10_000_000:
        return "VIP"
    if revenue &gt;= 2_000_000:
        return "Regular"
    return "New"

print(segment(3_500_000))</pre>
<p>3.5 million — Regular. <code>elif</code> ham yozish mumkin, mantiq bir xil. <code>return</code> — “javob shu, to‘xta.”</p>

<p>Bir nechta shart. <code>and</code> — hammasi rost. <code>or</code> — bittasi yetadi. <code>not</code> — teskarisi.</p>
<pre>if city == "Toshkent" and amount &gt; 0:
    print("Toshkent, musbat savdo")</pre>
<p>Bo‘sh satr <code>""</code> va <code>0</code> ni “bor” deb hisoblamang. Aniq solishtiring: <code>amount &gt; 0</code>, <code>city != ""</code>.</p>

<p>Eng ko‘p xato: <code>if amount = 0</code>. Bu tayinlash. Taqqoslash: <code>==</code>. Yana: <code>if amount:</code> — 0 ni False deb yutadi. Nol savdo va “ustun bo‘sh” ni aralashtirmang.</p>
""",
    "py-loop": """
<p>Oldingizda uchta to‘lov: 120 ming, 45 ming, 80 ming. “50 mingdan kattalarini qo‘sh.” Sichqoncha bilan uchta katak — oson. 8 ming qator bo‘lsa? Tsikl: bir xil ishni har element uchun.</p>

<p><code>for</code> — “ro‘yxatdagi har biri.” O‘qing: har <code>a</code> uchun, agar 50 mingdan katta bo‘lsa, yig‘indiga qo‘sh.</p>
<pre>amounts = [120000, 45000, 80000]
total = 0
for a in amounts:
    if a &gt;= 50000:
        total += a
print(total)</pre>
<p>120000 + 80000 = 200000. 45000 tashlandi. <code>total += a</code> — “oldingi total ga a ni qo‘sh.” Indeks kerak bo‘lsa <code>enumerate</code>, ikki ro‘yxatni juftlash — <code>zip</code>. Hozir oddiy for yetarli.</p>

<p><code>while</code> — shart rost ekan, takrorla. Hisoblagich o‘zgarmasa, shart hech qachon yolg‘on bo‘lmaydi — dastur osilib qoladi. Tahlilda while kam kerak. Fayl oxirigacha o‘qish, foydalanuvchi kiritishi — boshqa kasb. Sizga asosan for.</p>

<p>Muhim maslahat, ishda unutmang: million qatorni Python <code>for</code> da yig‘ish sekin. Mantiqni o‘rganish, 20 ta mijoz, kichik ro‘yxat — for. Katta savdo jadvali — keyinroq Pandas: <code>df["amount"].sum()</code> ichida tsikl yozmaysiz, lekin <em>nima qilayotganingiz</em> shu darsdagi kabi.</p>

<p>Xato: tsikl ichida har qatorni <code>print</code> qilish — 2 million qatorli faylda noutbuk yig‘laydi. Avval yig‘indi yoki hisoblagich, print oxirida.</p>
""",
    "py-func": """
<p>AOV ni 12 ta katakchaga qo‘lda yozdingiz. Birini unutdingiz — oylik hisobotda bitta filial “g‘alati.” Funksiya shuning uchun: hisob <strong>bitta joyda</strong>. Nom, kirish, chiqish.</p>

<p><code>def</code> — “mana yangi buyruq.” Qavs ichida nima kerak. <code>return</code> — javob. Docstring — qisqa izoh, kelajakdagi siz uchun.</p>
<pre>def aov(revenue, orders):
    # orders=0 bo‘lsa None (docstring o‘rniga izoh)
    if orders == 0:
        return None
    return revenue / orders

print(aov(1_200_000, 40))</pre>
<p>1.2 million / 40 = 30 000. Buyurtma yo‘q bo‘lsa 0 ga bo‘lish — dastur yiqiladi. Yaxshi xulq: tekshirib <code>None</code> yoki aniq xabar. 0 ni sekin 1 ga almashtirmang — AOV ni o‘ylab yolg‘on qilasiz.</p>

<p>Nom. Fe’l yoki aniq ot: <code>clean_amount</code>, <code>monthly_growth</code>, <code>segment</code>. <code>f1</code>, <code>calc</code> — bir haftadan keyin o‘zingiz tushunmaysiz. Argument kam bo‘lsin: nima kiradi, nima chiqadi — bir qarashda.</p>

<p>Ikkinchi qoida: hisob va yon effektni aralashtirmang. Funksiya AOV qaytarsin. Faylga yozish, print — tashqarida. Aks holda test qila olmaysiz: “son to‘g‘rimi?” ni “ekranga chiqdimi?” dan ajratolmaysiz.</p>

<p>Segment ham funksiya edi. 8 ta mijoz revenue ro‘yxatini for bilan aylanib, har biriga <code>segment(x)</code> deyish — takror yo‘q. Qoida o‘zgarsa, bitta joyni tuzatasiz.</p>
""",
    "py-collections": """
<p>Toshkent, Samarqand, Toshkent. Ro‘yxatda shahar takror. Savol: “qaysi shaharlar bor?” — takror kerak emas. “Har filial tushumi” — kalit va qiymat. Python da to‘rtta idish. Tahlilda shularni aralashtirmaslik — tinch uyqu.</p>

<p>Bankda ham shu. Unique mijoz — set. Filial bo‘yicha tushum — dict. Kunlik cheklar ketma-ket — list. “Nima saqlayapman?” deb so‘rang, keyin idishni tanlang. Noto‘g‘ri idish — keyin g‘alati xato.</p>

<ul>
  <li><strong>list</strong> — tartib bor, o‘zgartirish mumkin. Ustun qiymatlari, ketma-ket qatorlar</li>
  <li><strong>tuple</strong> — o‘zgarmas juftlik. Ba’zan lug‘at kaliti</li>
  <li><strong>set</strong> — unique, “bormi?” tez. Unique mijoz ID</li>
  <li><strong>dict</strong> — kalit → qiymat. Region: jami savdo</li>
</ul>

<pre>cities = ["Toshkent", "Samarqand", "Toshkent"]
print(set(cities))
revenue = {"Toshkent": 12_500_000}
print(revenue.get("Buxoro", 0))</pre>
<p><code>set(cities)</code> — Toshkent bir marta. <code>revenue["Buxoro"]</code> desangiz, kalit yo‘q — xato, dastur to‘xtaydi. <code>.get("Buxoro", 0)</code> — yo‘q bo‘lsa 0. Hisobotda “filial yo‘q = nol savdo” shu.</p>

<p>Kichik agregat dict da yotishi mumkin: <code>{"Toshkent": 12.5e6, "Samarqand": 4.1e6}</code>. 200 ming qatorni dict ga qo‘lda tiqmang — Pandas DataFrame. To‘plamlar — mantiq va kichik yordamchi hisoblar.</p>

<p>Xato: list ni unique qilaman deb <code>ids * 2</code> — bu ikki marta takror, unique emas. Unique kerak bo‘lsa <code>set(ids)</code>, tartib kerak bo‘lsa keyin <code>list(...)</code>. Yana: dict kaliti o‘zgarmas bo‘lishi kerak — list kalit bo‘lmaydi.</p>
""",
    "py-file": """
<p>Exceldan “CSV saqlash” bosdingiz. O‘zbekcha sarlavha buzilib chiqdi: krakozyabra. Bu Python “yomon”ligi emas. Fayl qanday <em>kodlangan</em> va qanday <em>ajratilgan</em> — shu ikkisi.</p>

<p>CSV — vergul (yoki nuqtali vergul) bilan ajratilgan matn. Excel O‘zbekiston/Rossiya locale da ko‘pincha <code>;</code> qo‘yadi. Siz <code>,</code> deb o‘qisangiz, butun qator bitta ustun bo‘lib ketadi. Avval faylni Notepad da ochib, birinchi qatorga qarang.</p>

<p>Encoding. Windows + Excel CSV: ko‘pincha <code>utf-8-sig</code> (boshida BOM). Oddiy <code>utf-8</code> ba’zan ishlaydi, ba’zan yo‘q. Kyrill yoki o‘zbek harflari kvadrat yoki “Рў” kabi bo‘lsa — birinchi gumon encoding.</p>
<pre>import pandas as pd
df = pd.read_csv("sales.csv", encoding="utf-8-sig", sep=";")
print(df.head())</pre>
<p>Kichik fayl uchun <code>csv</code> moduli ham bor. Tahlilchi ishining 90% — <code>pandas.read_csv</code>. Lekin xato chiqsa, aybdor Pandas emas: sep va encoding.</p>

<pre>import csv
with open("sales.csv", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.reader(f, delimiter=";"))
print(rows[:3])</pre>
<p><code>with open</code> — faylni och, ishlat, yop. Unutib yopsangiz, Windows da fayl “band”.</p>

<p>Xom faylni o‘zgartirmang. O‘qing, tozalang, <code>clean/sales.csv</code> ga yozing. Separatorni taxmin qilmang — birinchi 2 qatorni chop eting. Keyin butun yilni o‘qiysiz.</p>
""",
    "py-except": """
<p>Dastur yiqildi. Yaxshi. Yiqilish — “bu qator yomon” degan xabar. Yomon narsa — yiqilishni yutib, jim noto‘g‘ri hisobot chiqarish. <code>try/except</code> ni yostiq qilib, haqiqiy xatoni yashirmang.</p>

<p>CSV da buyurtma soni <code>12a</code>. <code>int("12a")</code> — <code>ValueError</code>. Butun dastur o‘chmasin, shu qatorni belgilaymiz:</p>
<pre>try:
    orders = int("12a")
except ValueError:
    orders = None
    print("orders ustuni tozalanmadi")</pre>
<p>Endi <code>orders</code> None. Keyin nechtasi None ekanini sanaysiz — tozalash jurnali. “O‘tdi” deb o‘ylamaslik.</p>

<p>Fayl yo‘q: <code>FileNotFoundError</code>. Noto‘g‘ri son: <code>ValueError</code>. Bo‘lish: <code>ZeroDivisionError</code>. Aniq nom yozing. Yalang <code>except:</code> yoki <code>except Exception:</code> hammasi — disk to‘la, kod xatosi, hammasini yutadi. Natija “ishlayapti”, raqam esa yolg‘on.</p>

<p>Modullar. <code>import pandas as pd</code> — tashqi paket, bir marta o‘rnatiladi. O‘zingizning <code>metrics.py</code> da <code>aov</code>, <code>segment</code> — jamoa standarti. Har notebookda nusxa ko‘chirmang. <code>from metrics import aov</code>.</p>

<p>Qoida: kutilgan xato (yomon katak) — except va jurnal. Kutilmagan xato (sizning kodingiz) — yiqilsin, tuzating. Tahlilchi “dastur o‘chmasin” deb emas, “noto‘g‘ri son ketmasin” deb o‘ylaydi.</p>
""",
    "np-ndarray": """
<p>Python list qulay. Lekin millionta sonni birma-bir qo‘shish — sekin, Python o‘zi sekin yuradi. NumPy massivi — bir xil turdagi sonlar, ichkarida tezkor hisob. Pandas jadvali ostida ham ko‘pincha shu yotadi. Shuning uchun “nima uchun NumPy?” — keyin DataFrame tushunarliroq bo‘ladi.</p>

<p>Yaratish:</p>
<pre>import numpy as np
x = np.array([10, 20, 30, 40], dtype=float)
print(x.mean(), x.std(ddof=1))</pre>
<p><code>mean</code> — o‘rtacha. <code>std(ddof=1)</code> — tanlama standart og‘ishi (Excel STDEV.S ga yaqin). <code>ddof=0</code> boshqacha formula. Hisobotda qaysi ekanini yozib qo‘ying.</p>

<p>List da har xil narsa aralashishi mumkin: son, matn, None. ndarray odatda <em>bir tur</em>. Matn aralashsa, hammasi matnga aylanib, o‘rtacha ishlamay qolishi mumkin. Turini <code>dtype</code> bilan belgilash — himoya.</p>

<p>Tahlilda nima beradi? Filtr, o‘rtacha, og‘ish, massiv minus massiv — tsiklsiz. Chegirma, zaxira, ball. Kichik o‘rganishda 4 ta son. Ishda — ustunning qiymatlari.</p>

<p>NumPy SQL ni almashtirmaydi, internet ham ochmaydi. U — tezkor hisob mashinasi. Chiroyli rang ham emas. Keyingi darsda shu massivdan “20 dan katta” ni kesib olamiz.</p>
""",
    "np-index": """
<p>Do‘kon: uchta narx, hammaga 12% chegirma. Excelda formulani pastga tortasiz. NumPy da: massiv <code>*</code> 0.88. Tsikl yo‘q. Buni broadcasting deyishadi — skalyar har elementga yuradi.</p>
<pre>import numpy as np
price = np.array([100, 250, 80])
print(price[price &gt;= 100])
print(price * 0.88)</pre>
<p>Birinchi print: 100 va 250. 80 tashlandi. <code>price &gt;= 100</code> — True/False massivi, <strong>boolean mask</strong>. Keyin shu niqob bilan kesamiz: faqat rost joylar.</p>

<p>Bank: “100 mingdan katta to‘lovlar.” <code>x[x &gt; 100000]</code>. Bu SQL WHERE ga o‘xshaydi, lekin hozircha bitta ustun — massiv.</p>

<p>Ehtiyot: ba’zi kesmalar <em>ko‘rinish</em> (view) — asl massivning oynasi. Oynaga yozsangiz, asl ham o‘zgaradi. Tasodifan xom ma’lumotni buzmaslik uchun kerak bo‘lsa <code>.copy()</code>. “Nima uchun narxlar o‘zgarib ketdi?” — ko‘pincha view.</p>

<p>Indeks son bilan ham: <code>price[0]</code> birinchi. Python da 0 dan. Oxirgi: <code>price[-1]</code>. Tahlilda ko‘proq mask ishlatasiz, chunki savol “qaysi indekslar” emas, “qaysi shart.”</p>

<p>Chalkashmaslik: <code>x[x &gt; 20]</code> matn qidiruv emas, join emas. Shartga mos elementlar. Shu jumlani mashqda tanlaysiz.</p>
""",
    "np-nan": """
<p>O‘rtacha hisobladiz — javob <code>nan</code>. Dastur “buzilgani” yo‘q. Massivda teshik bor: <code>np.nan</code>, “noma’lum.” Oddiy <code>mean</code> shu teshikni ko‘rib, butun o‘rtachani “zaharlaydi.” Bitta NaN — natija NaN.</p>
<pre>import numpy as np
x = np.array([10, np.nan, 30])
print(np.mean(x), np.nanmean(x))</pre>
<p><code>np.mean(x)</code> — nan. <code>np.nanmean(x)</code> — 20, teshikni o‘tkazib yuboradi. <code>nanstd</code> ham shu oila.</p>

<p>Avval sanang. Nechta NaN? Qancha foiz? Sensor ishlamagan, eksport teshigi, “hali kiritilmagan.” 2% bo‘lsa, o‘rtacha uchun nanmean yoki keyinroq Pandas da to‘ldirish. 40% bo‘lsa — avval manbani so‘rang, jim to‘ldirmang.</p>

<p>0 va NaN. Kassa yopiq kun — 0 so‘m savdo, bu fakt. Kassa fayli kelmagan — NaN. Ikkalasini bir xil qilsangiz, o‘rtacha va “necha kun ishladik” buziladi.</p>

<p>Qaror ketma-ketligi: sanash → biznesga aytish → to‘ldirish yoki tashlash. Darhol 0 qo‘yish — tahlil emas, yashirish. Keyingi modulda Pandas da flag qo‘yamiz: “bu katak teshik edi.”</p>
""",
    "pd-df": """
<p>SQL da so‘rov natijasi — jadval. Excelda Table. Pandas da bu — <strong>DataFrame</strong>: nomlangan ustunlar, qatorlar. Bitta ustun — <strong>Series</strong>. Tahlilchining asosiy idishi shu. NumPy — dvigatel; DataFrame — rul va panel.</p>

<pre>import pandas as pd
df = pd.DataFrame({
    "city": ["Toshkent", "Samarqand"],
    "amount": [120000, 80000],
})
print(df.head())
print(df.dtypes)
print(df.shape)</pre>
<p><code>head()</code> — birinchi qatorlar, ko‘z bilan. <code>dtypes</code> — har ustun turi: object (matn), int, float. <code>shape</code> — (qator, ustun). Yangi CSV ochilganda tartib: head, dtypes, shape, keyin <code>isna().sum()</code>. Darhol grafik yoki model — yo‘q.</p>

<p>Yaratish yo‘llari: lug‘atdan (yuqorida), <code>read_csv</code>, ba’zan SQL dan. Index — qator identifikatori. Ko‘pincha 0, 1, 2 qoldiriladi. Vaqt qatori bo‘lsa, sanani index qilish qulay — keyinroq.</p>

<p>Ustun nomi. Bo‘shliq, katta harf, “Amount (so‘m)” — ishlaydi, lekin charchatadi. Snake_case: <code>amount_sum</code>. Buni tozalash darsida qilamiz. Hozir: <code>df["city"]</code> — Series, <code>df[["city", "amount"]]</code> — kichik DataFrame. Ikki qavs — ikkita ustun.</p>

<p>Kichik odat: print qilib <em>o‘qing</em>. 2 qatorlimi, 2 millionlimi? Amount floatmi yoki object? Shu savollarsiz filtr “ishlamaydi” deb Pandas ni ayblaysiz.</p>
""",
    "pd-filter": """
<p>SQL dagi WHERE ning ukasi. “Faqat Toshkent”, “yoki amount 10 dan katta.” Pandas da avval <em>niqob</em> yasaysiz — har qator True/False — keyin shu niqob bilan kesasiz.</p>
<pre>import pandas as pd
df = pd.DataFrame({"city": ["Toshkent", "Buxoro"], "amount": [5, 12]})
print(df[(df["city"] == "Toshkent") | (df["amount"] &gt; 10)])</pre>
<p>Toshkent ham, 12 ham chiqadi. <code>|</code> — yoki. <code>&amp;</code> — va. Python dagi <code>and</code> / <code>or</code> bu yerda qator-qator ishlamaydi. Java dagi <code>&amp;&amp;</code> ham yo‘q.</p>

<p>Qavs. Operator tartibi tuzoq. Qavssiz:</p>
<pre>df.city == "Toshkent" &amp; df.amount &gt; 0</pre>
<p>Python avval <code>&amp;</code> ni boshqacha tushunishi mumkin — xato yoki noto‘g‘ri niqob. To‘g‘ri:</p>
<pre>df[(df["city"] == "Toshkent") &amp; (df["amount"] &gt; 0)]</pre>
<p>Ovoz chiqarib: “shahar Toshkent <em>va</em> summa musbat.” Har shart — o‘z qavsi.</p>

<p><code>loc</code> va <code>iloc</code>. <code>loc</code> — nom bilan: qator yorlig‘i, ustun nomi. <code>iloc</code> — raqam: 0-qator, 1-ustun. Filtrda ko‘pincha <code>df[mask]</code> yoki <code>df.loc[mask, ["city", "amount"]]</code>. Kerakli ustunlarni ham shu yerda kesing — SELECT kabi.</p>

<p>Nuqta bilan <code>df.city</code> qisqa, lekin ustun nomi <code>mean</code> yoki bo‘shliq bo‘lsa, ishlamasligi mumkin. Ishda <code>df["city"]</code> xavfsizroq. Matnni aniq yozing: <code>"Toshkent"</code>, ortda bo‘shliq bo‘lsa mos kelmaydi — trim keyingi modul.</p>
""",
    "pd-assign": """
<p>QQS 12%. Amount bor, <code>vat</code> yo‘q. Yangi ustun — hisoblangan maydon. Jadvalga ustun qo‘shasiz, xom CSV ni emas, xotiradagi df ni.</p>
<pre>import pandas as pd
df = pd.DataFrame({"amount": [100, 200]})
df = df.assign(vat=lambda x: x["amount"] * 0.12)
print(df)</pre>
<p><code>assign</code> yangi jadval qaytaradi (zanjir qulay). Yoki oddiy: <code>df["vat"] = df["amount"] * 0.12</code>. Ikkalasi ham ish. Zanjir: o‘qish, filtr, assign, groupby — bitta hikoya.</p>

<p>SettingWithCopy. Filtrladingiz, keyin bo‘lakka yozdingiz:</p>
<pre>tosh = df[df["city"] == "Toshkent"]
tosh["vat"] = 1</pre>
<p>Pandas ogohlantirishi mumkin: siz nusxaga yozayapsizmi, asliga mi? Natija g‘alati — ba’zan yoziladi, ba’zan yo‘q. Xavfsiz yo‘l:</p>
<pre>df.loc[df["city"] == "Toshkent", "vat"] = df["amount"] * 0.12</pre>
<p>Yoki filtrlanganini yangi df deb oling, assign qiling, asliga tegmang. “E’tiborsiz qoldirish” — keyin hisobotda Toshkent QQS i yo‘q.</p>

<p>lambda — qisqa funksiya, shu joyda. <code>x</code> — butun df. Uzoq mantiq bo‘lsa, alohida <code>def</code> yozing, o‘qiladi.</p>

<p>Yangi ustun — yangi haqiqat. Nomini yolg‘on qilmang: <code>vat</code> 12% bo‘lsa, 15% ni ham vat demang. Izoh yoki boshqa nom.</p>
""",
    "pd-na": """
<p>Bo‘sh katakcha. Pandas da ko‘pincha <code>NaN</code> (Not a Number) yoki <code>NA</code>. SQL dagi NULL. “Hali yo‘q” — 0 emas. Yetkazilmagan buyurtma amount i noma’lum. Uni 0 qilsangiz, o‘rtacha tushadi, konversiya o‘zgaradi, rahbar “arzonlashdik” deb o‘ylaydi.</p>
<pre>import pandas as pd
df = pd.DataFrame({"amount": [10, None, 30]})
print(df["amount"].isna().mean())
df["amount_missing"] = df["amount"].isna()
df["amount"] = df["amount"].fillna(df["amount"].median())</pre>
<p><code>isna().mean()</code> — teshik ulushi (bu yerda 1/3). Flag <code>amount_missing</code> — keyin “to‘ldirilganlar” ni alohida ko‘rasiz. Median bilan to‘ldirish — bitta siyosat, avtomatik haqiqat emas.</p>

<p>Qachon tashlash (<code>dropna</code>)? Kalit maydon: <code>order_id</code> bo‘sh — bu qator ishonchsiz, tashlang, jurnalga yozing. Amount ning 2% teshi — median yoki biznes qoidasi. 30% teshi — avval manba.</p>

<p>Hamma NaN ni 0 qilish — eng keng tarqalgan yomon odat. 0 — haqiqiy nol savdo (do‘kon yopiq). NaN — noma’lum. Aralashtirsangiz, AOV va “nechta buyurtma” yolg‘on gapiradi.</p>

<p>Siyosatni yozing: “order_id NaN — drop. amount NaN — flag + median. city NaN — ‘Noma’lum’.” Bir xil CSV ni ikki kishi boshqacha tozalasa, ikki hisobot. Shuning uchun jurnal.</p>
""",
    "pd-dup": """
<p>Bir <code>order_id</code> ikki marta. Eksport ikki marta yuborilgan, yoki join oldin qatorlarni ko‘paytirgan. Dublikat — ba’zan xato, ba’zan hayot. Kalitni aniqlamasdan <code>drop_duplicates()</code> bosish — butun buyurtmalarni yutib yuborish mumkin.</p>
<pre>import pandas as pd
df = pd.DataFrame({"order_id": [1, 1, 2], "amount": [10, 10, 5]})
print(df.duplicated(subset=["order_id"]).sum())
print(df.drop_duplicates("order_id"))</pre>
<p><code>duplicated</code> — takrorlar (birinchisini odatda False qoldiradi). <code>sum()</code> — nechta “ortiqcha.” <code>drop_duplicates("order_id")</code> — har buyurtma bir qator.</p>

<p>CustomerID takrorlanishi <strong>normal</strong>: bir odam 12 marta xarid qiladi. Agar unique qilsangiz, 11 ta chek yo‘qoladi, revenue erib ketadi. “Noto‘g‘ri subset” — mashqdagi tuzoq. Unique bo‘lishi kerak narsa: odatda order_id, chek raqami. Takrorlanishi kerak: customer_id, city.</p>

<p>Avval <code>duplicated(subset=["order_id"]).sum()</code> ni chop eting. Keyin drop. Nechta qator ketdi — tozalash jurnaliga. Amount farq qiladigan “bir xil id” — bu dublikat emas, konflikt: qaysi qator haqiqiy? Odam so‘rang.</p>

<p><code>keep="first"</code> / <code>"last"</code> — qaysi nusxa qoladi. Sana bo‘lsa, oxirgi yangilanish. Taxmin qilmang, qoidani yozing.</p>
""",
    "pd-cast": """
<p>Yana o‘sha <code>"1 200"</code>. Endi butun ustun. Qo‘lda <code>float()</code> 50 ming marta chaqirmaysiz. Pandas: matnni tozalash, keyin <code>to_numeric</code>. Noto‘g‘ri katak — dastur yiqilmasin, NaN bo‘lsin: <code>errors="coerce"</code>.</p>
<pre>import pandas as pd
s = pd.Series([" 1 200 ", "abc", "3,5"])
clean = (
    s.str.replace(" ", "", regex=False)
     .str.replace(",", ".", regex=False)
)
print(pd.to_numeric(clean, errors="coerce"))</pre>
<p>1200.0, NaN, 3.5. <code>abc</code> 0 ga aylanmadi — NaN. 0 qilsangiz, yolg‘on savdo. Keyin <code>isna().sum()</code> — nechta axlat bor.</p>

<p>Pipeline, odat tartibi:</p>
<ol>
  <li>Ustun nomlari: bo‘shliqni pastki chiziq, kichik harf (snake_case)</li>
  <li><code>str.strip()</code> — chetdagi bo‘shliq. “Toshkent ” filtrlarda yo‘qoladi</li>
  <li>Son — <code>to_numeric</code>, sana — <code>to_datetime</code></li>
  <li>Kutilmagan qiymatlar: unique, value_counts, jurnal</li>
</ol>

<p><code>regex=False</code> — oddiy almashtirish. Nuqta regex da maxsus; hozir oddiy matn deb o‘ylab yozamiz. Sana formatini keyingi darsda. Hozir: tur belgilanmasa, groupby va sum ishlamasligi yoki matnni “qo‘shishi” mumkin.</p>

<p>Xato: <code>astype(int)</code> darhol — bitta “abc” da yiqiladi. Avval coerce, keyin NaN siyosati, keyin int. Keskinlik — tozalashdan keyin.</p>
""",
    "pd-groupby": """
<p>SQL da GROUP BY: har bir shahar uchun nechta, har bir region uchun yig‘indi. Pandas da xuddi shu savol. Qatorlarni uyum-uyum, keyin har uyumda SUM, COUNT, nunique.</p>
<pre>import pandas as pd
df = pd.DataFrame({
    "region": ["Toshkent", "Toshkent", "Buxoro"],
    "amount": [10, 20, 5],
    "oid": [1, 2, 3],
})
print(
    df.groupby("region").agg(
        revenue=("amount", "sum"),
        n=("oid", "nunique"),
    )
)</pre>
<p>Toshkent: 30 so‘m, 2 ta unique buyurtma. Buxoro: 5, 1. <code>nunique</code> — “nechta xil.” Oddiy <code>count</code> qatorlarni sanaydi; bir buyurtma ikki qatorda bo‘lsa, count ikkita, nunique bitta. Buyurtmalar soni — odatda nunique(order_id).</p>

<p>Named aggregation: <code>revenue=("amount", "sum")</code> — natija ustuni chalkash <code>amount_sum</code> emas, siz aytgan nom. Hisobot va mashq shu nomni kutadi.</p>

<p><code>as_index=False</code> — region oddiy ustun bo‘lib qoladi, Excelga yozish oson. Kategoriya (category dtype) da <code>observed=True</code> — bo‘sh kategoriyalarni tortmaslik. Hozir asosiysi: guruh kaliti + agg.</p>

<p>WHERE oldin, guruh keyin — SQL kabi. Avval Toshkentni filtrlab, keyin kanal bo‘yicha yig‘ish. HAVING o‘rniga: groupby dan keyin <code>result[result["revenue"] &gt; 1000]</code>.</p>
""",
    "pd-merge": """
<p>Ism <code>customers</code> da, to‘lov <code>orders</code> da. Excel VLOOKUP. SQL JOIN. Pandas: <code>merge</code>. Kalit: <code>cid</code>. Qanday ulash — savolga bog‘liq.</p>
<pre>import pandas as pd
orders = pd.DataFrame({"cid": [1, 2], "amount": [10, 20]})
cust = pd.DataFrame({"cid": [1, 3], "name": ["Ali", "Nodira"]})
print(orders.merge(cust, on="cid", how="left"))</pre>
<p>Chap — orders. Ali ulanadi. cid=2 — mijoz yo‘q, name NaN. Nodira (3) bu so‘rovda yo‘q: u o‘ngda, chapda buyurtmasi yo‘q. <code>how="left"</code> — chapdagi hech kimni tashlama. <code>inner</code> — faqat mos kelganlar (2 yo‘qoladi). <code>outer</code> — ikkala tomon.</p>

<p>Fan-out. Merge dan keyin qatorlar kutilganidan ko‘p. Ehtimol: o‘ng jadvalda kalit dublikat, ko‘p-ko‘p. Har buyurtma 3 ta “mijoz qatori”ga yopishadi — revenue 3 marta. Merge <em>oldin</em> <code>cust["cid"].duplicated().sum()</code>. <code>validate="many_to_one"</code> — Pandas o‘zi baqiradi, agar o‘ng unique bo‘lmasa.</p>

<p>Kalit nomlari turlicha: <code>left_on="customer_id", right_on="id"</code>. Tur mosligi: 1 va "1" qo‘shilmasligi mumkin. Avval ikkala kalitni bir xil turga o‘giring.</p>

<p>Tekshiruv: merge oldin/keyin <code>len(df)</code>. Left bo‘lsa, chap qatorlardan kamaymasligi kerak (fan-out bo‘lmasa). Ko‘paygan bo‘lsa — to‘xta, dublikatni top.</p>
""",
    "pd-dt": """
<p>Sana ustuni ko‘pincha matn: <code>"2024-01-31"</code>. Matnni oy bo‘yicha guruhlab bo‘lmaydi — yoki g‘alati guruhlanadi. Avval haqiqiy sana: <code>to_datetime</code>.</p>
<pre>import pandas as pd
df = pd.DataFrame({
    "dt": ["2024-01-31", "2024-02-01"],
    "amount": [10, 20],
})
df["dt"] = pd.to_datetime(df["dt"])
print(df.groupby(df["dt"].dt.to_period("M"))["amount"].sum())</pre>
<p>Yanvar 10, fevral 20. <code>.dt.to_period("M")</code> — oy kesimi. Kunlikni oyga yig‘ish shu. <code>resample</code> index sana bo‘lsa qulay. Sliding 7 kunlik o‘rtacha — <code>rolling(7)</code>. Recency — so‘nggi xariddan beri kunlar, RFM darsida.</p>

<p>Tuzoq: kun/oy/yil aralash. <code>03/04/2024</code> — 3-aprel mi, 4-mart mi? <code>dayfirst=True</code> ni <em>faqat bilganingizda</em> qo‘ying. Noto‘g‘ri dayfirst — butun trend siljiydi. ISO <code>YYYY-MM-DD</code> eng tinch.</p>

<p><code>errors="coerce"</code> — yomon sana NaT (Not a Time). Sanang. 5% NaT — format aralashgan. <code>str[:7]</code> bilan “2024-01” kesish ba’zan ishlaydi, lekin 31/01/2024 da yiqiladi. Avval datetime, keyin period.</p>

<p>Vaqt zonasi, soat. Mashqlarda odatda kun. Ishda “31-kun 23:00” oyni adashtirmasligi uchun period yoki <code>dt.normalize()</code>. Avval savol: kunlikmi, oylikmi?</p>
""",
    "pd-eda": """
<p>Yangi dataset. Qo‘l qichishadi: darhol pie chart, darhol “model.” To‘xtang. EDA — Exploratory Data Analysis: savol berish, taqsimotni ko‘rish, anomaliyani topish. Dashboard va KPI dan <em>oldin</em>. Aks holda chiroyli yolg‘on chizasiz.</p>
<pre>import pandas as pd
df = pd.DataFrame({
    "amount": [1, 2, 3, 1000],
    "city": ["A", "A", "B", "B"],
})
print(df.describe())
print(df["city"].value_counts(normalize=True))</pre>
<p><code>describe</code> — sonli ustun: o‘rtacha, min, max, kvartillar. 1000 — dum, o‘rtachani tortadi. <code>value_counts(normalize=True)</code> — shaharlar ulushi. “Ko‘p qismi A” ni son bilan ayting, sezgi bilan emas.</p>

<p>Tartib, men shunday yuraman:</p>
<ol>
  <li>Hajm, turlar, yetishmovchilik: shape, dtypes, isna</li>
  <li>Tavsiflovchi statistika: describe</li>
  <li>Kategoriyalar: value_counts</li>
  <li>Taqsimot va outlier: hist, box (keyingi darslar)</li>
  <li>Kesimlar: region × kanal, groupby</li>
  <li>Qisqa xulosa: nima o‘zgardi, nima shubhali</li>
</ol>

<p>1000 so‘mlik “xato”mi yoki ulkan buyurtmami? EDA javob bermaydi — lekin savolni ko‘rsatadi. Neural net, pie, dropna hammasi — keyin. Avval hajm, tur, missing, describe, kesimlar.</p>

<p>Har EDA oxirida 5 jumla yozing. “Grafik chiqdi” emas: “Buxoroda AOV past, lekin bitta 12 mln chek o‘rtachani ko‘targan — flag.” Shu jumlalar hisobotning urug‘i.</p>
""",
    "py-mpl": """
<p>Grafik rahbar uchun. Siz uchun emas, “men matplotlib ni bilaman” uchun ham emas. 12 oylik savdo — ko‘z trendni tutsin. 3D pie, 20 rang, soya — ishonchni o‘ldiradi. Oddiy chiziq, aniq o‘q.</p>

<p>Qoida, deyarli qonun:</p>
<ul>
  <li>Vaqt oqimi — <strong>line</strong> (oylik savdo)</li>
  <li>Kategoriyani taqqoslash — <strong>bar</strong> (region revenue)</li>
  <li>Taqsimot — <strong>hist</strong> (amount)</li>
</ul>
<p>Pie ni deyarli ishlatmang, 3D pie ni umuman. Scatter — ikki sonning bog‘liqligi, 50 o‘lchov emas.</p>
<pre>import matplotlib.pyplot as plt

months = ["Yan", "Fev", "Mar"]
revenue = [12.5e6, 11.8e6, 13.1e6]
plt.plot(months, revenue)
plt.title("Oylik savdo, Toshkent tarmog‘i")
plt.ylabel("so‘m")
plt.tight_layout()
plt.savefig("revenue.png", dpi=120)</pre>
<p>Sarlavha — nima ekani. <code>ylabel</code> — birlik. Grid ixtiyoriy, lekin o‘qsi o‘qilishi shart. <code>tight_layout</code> — yozuv kesilmasin. PNG ni yuborasiz, ekrandagi oyna emas.</p>

<p>Chiroy ikkinchi. Birinchi: shkala yolg‘on aytmasin (nolsi o‘q ba’zan foizni dramaga aylantiradi). Ikkinchi: bitta grafik — bitta savol. 12 chiziq birga — hech kim o‘qimaydi.</p>

<p>Notebook da <code>plt.show()</code>. Skriptda savefig. Ikkala joyda ham title qo‘ying — fayl nomi “Figure 1” bo‘lib qolmasin.</p>
""",
    "py-sns": """
<p>Matplotlib — qalam. Seaborn — statistik qalam: “taqsimot qanday,” “o‘rtacha atrofida nima.” Bir qator bilan boxplot, heatmap. Ichida baribir matplotlib, lekin defaultlari tahlilchiga yaqin.</p>
<pre>import pandas as pd
import seaborn as sns
df = pd.DataFrame({
    "region": ["Toshkent", "Toshkent", "Buxoro", "Buxoro"],
    "amount": [80, 1200, 40, 55],
})
sns.boxplot(data=df, x="region", y="amount")</pre>
<p>Boxplot: quti — o‘rta 50%, chiziq — median, nuqtalar — dum. Qaysi viloyatda “dum” uzun? Katta chegirma, ulkan buyurtma, yoki xato chek. Toshkentda median oddiy, lekin 3 ta osmondagi nuqta — shu insight. Pie buni ko‘rsatmaydi. Violin — taqsimot shakli, box ga yaqin.</p>

<pre>sns.heatmap(df.select_dtypes("number").corr(), annot=True)</pre>
<p>Korrelyatsiya: sonli ustunlar qanchalik birga yuradi. 0.9 — deyarli bir xil hikoya (ehtimol siz ikkita o‘lchovni ikki marta hisoblagansiz). Sabab-oqibat emas: muzqaymoq va cho‘milish ham korrelyatsiya qiladi. Heatmap — savol generator, hukm emas.</p>

<p><code>barplot</code> o‘rtacha va (ixtiyoriy) ishonch oralig‘i. Stakeholderga CI kerak bo‘lmasa, oddiy bar + aniq yig‘indi (groupby) halolroq. “Chiroyli interval” noto‘g‘ri tanlovni yashirmasin.</p>

<p>Import: <code>seaborn as sns</code>. Dataset <code>df</code> da region, amount bor deb hisoblang. Grafik ostiga bir jumla: “Buxoroda dum yo‘q, Toshkentda 4 ta outlier — tekshirish ro‘yxati.” Chiroy baholanmaydi, shu jumla baholanadi.</p>
""",
    "py-kpi": """
<p>KPI — qisqartma emas, <em>kelishilgan ta’rif</em>. AOV ni ikki kishi boshqacha hisoblasa, yig‘ilishda urishadi, ikkalasi ham “Python to‘g‘ri.” Koddan oldin qog‘oz: nima kiradi, nima chiqmaydi.</p>
<pre>def kpi_summary(df):
    orders = df["order_id"].nunique()
    revenue = df["amount"].sum()
    return {
        "orders": orders,
        "revenue": revenue,
        "aov": revenue / orders if orders else None,
    }</pre>
<p>AOV shu yerda: tushum / unique buyurtmalar. Ba’zi firma “qatorlar soni” deb hisoblaydi — dublikat bo‘lsa AOV kichrayadi. Ta’rif: unique orders. 0 buyurtma — None, yiqilish emas.</p>

<p>Boshqa odatiy o‘lchovlar. Revenue — qaysi status? Bekor qilingan chek kiritiladimi? Conversion — agar traffic (tashrif) bo‘lsa, buyurtma / tashrif; tashrif yo‘q bo‘lsa, bu KPI ni uydirmang. Repeat rate — ikkinchi xarid qilgan mijozlar / birinchi marta xarid qilganlar; oynasi 30 kunmi, 90 mi?</p>

<p>“Faol mijoz” — 90 kun ichida xaridmi, yoki <code>status=active</code> ustunimi? Hujjatlashtiring. Aks holda marketing “12 ming faol”, moliya “8 ming” — ikkalasi ham o‘z faylidan.</p>

<p>Funksiya qaytarsin, print qilmasin. Test: kichik df da qo‘lda hisoblab, funksiya bilan solishtiring. Keyin 6 oylik CSV. Ta’rif o‘zgarsa, bitta funksiya, bitta izoh.</p>
""",
    "py-rfm": """
<p>Mijoz 120 kundan beri xarid qilmagan. Bu firibgarlik emas. Bu — jimlik. Marketing “qayta faollashtirish” deydi, siz esa avval <strong>recency</strong> ni kunlarda o‘lchaysiz. RFM to‘liq (Recency, Frequency, Monetary) — marketing kursi. Tahlilchi Recency ni hisoblashi shart: so‘nggi xarid qachon.</p>
<pre>last = df.groupby("customer_id")["order_date"].max()
recency = (as_of - last).dt.days
print(recency.head())
print((recency &gt;= 90).sum())</pre>
<p><code>as_of</code> — “bugun” yoki hisobot sanasi. Oxirgi xarid max. Ayirma — kun. 90+ — ro‘yxat (chegara biznes bilan: oziq-ovqat 30 kun, mebel 180). Chegarani kodga sehirli son qilib yashirmang — parametr.</p>

<p>Frequency — necha marta. Monetary — qancha pul. Uchlikni birga kesib, “VIP lekin jim” ni topasiz: katta tushum, recency 120. AOV oshgani recency emas. Join xatosi ham emas — agar sanalar to‘g‘ri bo‘lsa.</p>

<p>Tuzoq: bekor qilingan buyurtmani “so‘nggi xarid” deb olish. Status filtri avval. Yana: mijoz yo‘q, mehmon cheki — customer_id bo‘sh, recency hisoblanmaydi. Ularni alohida.</p>

<p>Ro‘yxatni CSV qilib berasiz: id, recency_days, last_order, revenue_6m. “Churn albatta” deb yozmang. “90 kun jim, qoidaga ko‘ra qayta aloqa” — halol gap.</p>
""",
    "py-final": """
<p>Oxirgi dars. Yangi sehr yo‘q. O‘rta do‘kon tarmog‘i 6 oylik savdo CSV beradi. Savol aniq: qaysi region va kanal o‘sadi, qayerda AOV tushgan, qaysi mijozlar jim. Siz — tozalash, KPI, kesim, ikkita grafik, beshta tavsiya. “Yaxshilash kerak” tavsiya emas.</p>

<p>Tasavvur: Toshkent, Samarqand, Buxoro; online va oflayn. Faylda order_id dublikat, amount ba’zan matn, 3% NaN, sanalar aralash. Ketma-ketlik: avval turlar, keyin NaN siyosati, keyin kalit dublikat, <em>keyin</em> KPI. Darhol model, darhol dropna hamma ustun — yo‘q.</p>

<p>Talab, shu ro‘yxat bo‘yicha topshirasiz:</p>
<ol>
  <li>Tozalash jurnali: nechta qator bor edi, nima tashlandi, nima to‘ldirildi</li>
  <li>Oylik revenue, AOV, unique mijoz — ta’rif yozilgan</li>
  <li>Region × kanal pivot (groupby yoki pivot_table)</li>
  <li>Ikita grafik: masalan oylik chiziq va region bar yoki boxplot</li>
  <li>Beshta aniq tavsiya: kimga, nima qilsin, qaysi songa tayangan</li>
</ol>

<p>Baholash. Kod ishlashi. Ta’riflar aniqligi. Insight: “Toshkent online AOV 12% tushgan, outlier yo‘q — narx yoki savat.” 20 ta 3D chart, parolni kodga yozish, faqat <code>print(df)</code> — bu loyiha emas.</p>
<pre>monthly = (
    df.groupby(df["order_date"].dt.to_period("M"))
      .agg(revenue=("amount", "sum"),
           orders=("order_id", "nunique"),
           customers=("customer_id", "nunique"))
)
monthly["aov"] = monthly["revenue"] / monthly["orders"]
print(monthly)</pre>
<p>Shu jadval — hikoyaning umurtqasi. Merge kerak bo‘lsa — mijoz va buyurtma. Recency — jimlar. EDA — 1000x chek.</p>

<p>Siz noldan: print, tur, if, for, funksiya, fayl, NumPy, DataFrame, tozalash, groupby, merge, sana, grafik, KPI. Endi bitta CSV ni o‘qituvchidek o‘qing: “Bu savol qaysi dars?” — keyin yozing. Omadingizni tilayman. Hisobotda son va gap yonma-yon bo‘lsin.</p>
""",
}
