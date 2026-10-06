# -*- coding: utf-8 -*-
"""Build clearer python_teacher_lessons.py for absolute beginners."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "apps" / "core" / "python_teacher_lessons.py"


def lesson(simple, why, steps, code, result, mistakes, practice) -> str:
    steps_html = "\n".join(f"  <li>{s}</li>" for s in steps)
    mist_html = "\n".join(f"  <li>{m}</li>" for m in mistakes)
    return f"""
<h2>Oddiy tilda</h2>
<p>{simple}</p>

<h2>Nima uchun kerak?</h2>
<p>{why}</p>

<h2>Qadam-baqadam</h2>
<ol>
{steps_html}
</ol>

<h2>Kod — birga o‘qiymiz</h2>
<pre>{code}</pre>
<p><strong>Natija:</strong> {result}</p>

<h2>Chalkashmaslik</h2>
<ul>
{mist_html}
</ul>

<h2>Bugungi mashq</h2>
<p>{practice}</p>
""".strip()


LECTURES: dict[str, str] = {}

LECTURES["py-noldan-start"] = lesson(
    "Tasavvur qiling: Excelda katakga <code>=2+2</code> yozasiz — javob chiqadi. "
    "Python ham shunga o‘xshaydi, faqat buyruqni katak emas, <strong>qatorga</strong> yozasiz. "
    "Bugun bitta narsani o‘rganamiz: <code>print</code> — “ekranga ko‘rsat”. "
    "Dasturchi bo‘lish shart emas. Bank, savdo yoki Excel bilan ishlasangiz ham — shu yeridan boshlaysiz. "
    "Xato chiqsa qo‘rqmang: bu “siz yomonsiz” degani emas, “shu qatorda tuzatish kerak” degani.",
    "Nima uchun umuman Python? Chunki har dushanba bir xil hisobotni qo‘lda yig‘ish charchatadi va xato keltiradi. "
    "Python shu ishni keyinroq avtomatlashtirishga yo‘l ochadi. Lekin avval eng oddiy narsa: "
    "kod yozdim → ekranda ko‘rdim. Shu his bo‘lmasa, keyingi darslar tushunarsiz tuyuladi.",
    [
        "Python o‘rnating: python.org yoki Windows da Microsoft Store. “Install” tugmasini bosing.",
        "Tekshirish: terminal (cmd) ochib <code>python --version</code> yozing. Raqam chiqsa — tayyor. "
        "Ba’zan <code>py --version</code> ishlaydi.",
        "Quyidagi 2 qatorni yozing (yoki platformadagi kod oynasida ishga tushiring).",
        "Natijani o‘qing: matn va son chiqishi kerak. Chiqmasa — qo‘shtirnoq yoki yozuvni tekshiring.",
        "Odat: har yangi g‘oyani avval 2–3 qator bilan sinang. Katta loyiha emas.",
    ],
    'print("Salom, tahlil!")\nprint(2 + 2)',
    "Birinchi qator ekranga <code>Salom, tahlil!</code> yozadi. Ikkinchi qator <code>4</code> ni chiqaradi. "
    "<code>print(...)</code> — buyruq. Qavs ichidagi narsa — ko‘rsatiladigan narsa. "
    "Matn doim qo‘shtirnoq ichida: <code>\"...\"</code> yoki <code>'...'</code>. "
    "Sonni qo‘shtirnoqsiz yozasiz: <code>2 + 2</code>.",
    [
        "Qo‘shtirnoq ochilib yopilmasa — qizil xato. Har ochilgan qo‘shtirnoq yopilsin.",
        "<code>Print</code> (katta P) ko‘pincha ishlamaydi. Yozing: <code>print</code> (kichik harf).",
        "Ortiqcha vergul, noto‘g‘ri qavs — xato. Avval namunani aynan ko‘chiring, keyin o‘zgartiring.",
        "Bugun 20 qatorlik dastur yozmang. 2 qator — yetarli g‘alaba.",
    ],
    "1) O‘z ismingizni print qiling. 2) <code>print(10 * 5)</code> ni ishga tushiring. "
    "3) Natijani o‘qing: matn va 50 chiqishi kerak. Chiqmasa — qo‘shtirnoqni tekshiring.",
)

LECTURES["py-noldan-run"] = lesson(
    "Oldingi darsda bitta qatorni sinadingiz. Endi shu buyruqlarni <strong>faylga</strong> saqlaymiz. "
    "Fayl — retsept: ertaga ham bir xil ishlaydi. REPL — taomni tatib ko‘rish; fayl — retseptni daftarga yozish.",
    "Haftalik hisobot har dushanba bir xil. Uni har safar qayta yozmaslik uchun <code>.py</code> fayl kerak. "
    "Izoh (<code>#</code>) — kelajakdagi sizga eslatma.",
    [
        "Yangi fayl yarating: masalan <code>hello.py</code>.",
        "Ichiga kod va izoh yozing (pastdagi namunadek).",
        "Fayl turgan papkada terminal oching.",
        "<code>python hello.py</code> deb yozing (Windows da ba’zan <code>py hello.py</code>).",
    ],
    '# Bu izoh — Python o‘qimaydi\nregion = "Toshkent"\nprint(f"Filial: {region}")',
    "<code>Filial: Toshkent</code> chiqadi. <code>region = ...</code> — qutiga nom berib, ichiga matn qo‘ydik. "
    "<code>f\"...{region}...\"</code> — matn ichiga o‘zgaruvchini joylash.",
    [
        "“File not found” — noto‘g‘ri papkadasiz yoki fayl nomi xato.",
        "Faylni Word da saqlamang — oddiy matn (<code>.py</code>).",
        "Izohni kod deb yozmang: <code>#</code> bo‘lmasa, Python uni buyruq sanaydi.",
    ],
    "<code>my_report.py</code> yarating: 1 izoh, 1 o‘zgaruvchi, 1 <code>print</code>. Ishga tushiring.",
)

LECTURES["py-noldan-errors"] = lesson(
    "Xato — dushman emas. Qizil xabar (traceback) — “qayerda adashdingiz” xaritasi. "
    "Yangi boshlovchi qo‘rqadi; tajribali odam oxirgi qatorni o‘qiydi.",
    "Tahlilda 0 ga bo‘lish, noto‘g‘ri nom, yopilmagan qavs — kundalik. "
    "Xabarni o‘qiy olmasangiz, soatlab “nima bo‘ldi?” deb qolasiz.",
    [
        "Xabarning eng pastki qatoriga qarang — xato turi.",
        "Qator raqamiga boring — odatda shu yerda muammo.",
        "Bitta narsani o‘zgartiring, qayta ishga tushiring.",
        "Bir vaqtda 10 joyini o‘zgartirmang.",
    ],
    "revenue = 1000000\norders = 0\nif orders == 0:\n    aov = None\nelse:\n    aov = revenue / orders\nprint(aov)",
    "<code>None</code> chiqadi — “buyurtma yo‘q, AOV hisoblanmadi.” Dastur yiqilmaydi. "
    "Shartsiz <code>revenue / orders</code> yozsangiz — ZeroDivisionError.",
    [
        "<strong>SyntaxError</strong> — yozuv buzilgan (qavs/qo‘shtirnoq).",
        "<strong>NameError</strong> — nom topilmadi (<code>revnue</code> o‘rniga <code>revenue</code>).",
        "<strong>ZeroDivisionError</strong> — 0 ga bo‘lish. Avval tekshiring.",
    ],
    "Ataylab bitta qo‘shtirnoqni ochiq qoldiring (SyntaxError), keyin tuzating. Keyin NameError ni ko‘ring.",
)

LECTURES["py-nima"] = lesson(
    "Bu kurs dasturchi emas, <strong>tahlilchi</strong> uchun. Siz Excel, savdo yoki bank bilan ishlaysiz. "
    "Python — takroriy tozalash va hisobni avtomatlashtirish vositasi. "
    "Har dushanba 12 ta CSV ni qo‘lda ochish o‘rniga — bitta skript.",
    "Excel tezkor filtr uchun ajoyib. Lekin 100 ming qator, 12 ta oylik fayl, bir nechta jadvalni ulash — "
    "Excel sekinlashadi va xato ko‘payadi. Python charchamaydi, lekin siz aniq yozishingiz kerak.",
    [
        "Qachon Excel: 5 daqiqalik filtr, kichik jadval, bitta pivot.",
        "Qachon Python: har oy ko‘p fayl, katta hajm, qayta-qayta bir xil ish.",
        "Ish muhiti: Notebook — tadqiqot; <code>.py</code> — barqaror pipeline.",
        "Odat: xom faylni o‘zgartirmang (<code>raw/</code>), har qadamga izoh yozing.",
    ],
    'print("Savdo tahlili boshlandi")\nregion = "Toshkent"\nprint(region)',
    "Ekranda ikki qator: xabar va <code>Toshkent</code>. "
    "<code>region</code> — o‘zgaruvchi (Excel katakchasi nomi kabi, lekin xotirada).",
    [
        "Python “sehrli dashboard” emas — siz yozganini bajaradi.",
        "Birinchi kundan katta loyiha yozmang: avval print, keyin fayl, keyin jadval.",
        "Excelni “yomon” demang — vositani vazifaga mos tanlang.",
    ],
    "3 ta print yozing: bugungi vazifa, shahar, va oddiy hisob (masalan 10*12). Har birini izohlab qo‘ying.",
)

LECTURES["py-turlar"] = lesson(
    "Excelda katakda 1200 ko‘rinsa, bu “son”. Python da esa ba’zan shu 1200 aslida <strong>matn</strong> bo‘ladi "
    "(qo‘shtirnoq ichida yoki CSV dan shunday kelgan). "
    "O‘zgaruvchi — quti nomi (<code>revenue</code>). Ichida nima yotishi — <strong>tur</strong> (sonmi, matnmi). "
    "Turini bilmasangiz, keyin “nima uchun ko‘paytirish ishlamadi?” deb qiynalasiz.",
    "CSV da amount ko‘pincha matn: <code>\"1 200\"</code>. Uni tozalamasdan QQS qo‘shsangiz — xato yoki g‘alati natija. "
    "Tahlilchilar vaqtining katta qismi shu: ko‘rinishdagi sonni haqiqiy songa aylantirish.",
    [
        "<code>int</code> — butun son: 250 buyurtma.",
        "<code>float</code> — o‘nli: narx, AOV, foiz.",
        "<code>str</code> — matn: \"Toshkent\", telefon, SKU.",
        "<code>bool</code> — True yoki False: VIP-mi?",
        "<code>None</code> — qiymat yo‘q. Diqqat: bu 0 emas, bo‘sh satr ham emas.",
        "Har doim so‘rang: <code>type(x)</code> — “men nima ushlab turibman?”",
        "Matndan songa: avval tozalang (bo‘shliq/vergul), keyin <code>float(...)</code>.",
    ],
    'revenue = 12500000\norders = 250\naov = revenue / orders\nprint(type(aov), round(aov, 2))\n\ns = "1 200"\nn = float(s.replace(" ", "").replace(",", "."))\nprint(n)\nprint(type(n))',
    "Birinchi blok: AOV float (masalan 50000.0) — bo‘lish Python da odatda o‘nli beradi. "
    "Ikkinchi blok: <code>1200.0</code> va uning turi <code>float</code>. "
    "Avval bo‘shliqni olib tashladik, keyin songa o‘girdik. "
    "Agar tozalamasdan <code>float(\"1 200\")</code> desangiz — xato chiqadi.",
    [
        '<code>amount = "150000"</code> bo‘lsa, <code>amount * 2</code> → <code>150000150000</code> (matn ikki marta), 300000 emas.',
        "Qo‘shtirnoq bormi-yo‘qmi — shunga qarang. Qo‘shtirnoq bo‘lsa, bu matn.",
        "<code>True + 1</code> Python da 2. Hisobotda flag ni pulga qo‘shmang.",
        "Locale: ba’zi faylda nuqta ming ajratgich, boshqasida o‘nli. Avval 5 qatorni ko‘z bilan ko‘ring.",
    ],
    "1) <code>x = 10</code>, <code>y = \"10\"</code> yarating. Ikkala <code>type</code> ni chop eting. "
    "2) <code>y</code> ni songa o‘girib, 2 ga ko‘paytiring. "
    "3) <code>\"3 500\"</code> matnini 3500.0 qilib ko‘ring.",
)

LECTURES["py-ifodalar"] = lesson(
    "Son chiqardi. Endi uni odam o‘qiydigan qilamiz. Rahbar “50000” emas, "
    "“AOV: 50,000 so‘m (−10.7%)” ni xohlaydi. Bu dars — hisob + format.",
    "Foiz o‘zgarish formulasi chalkashadi. Qavsni unutsangiz — boshqa javob. "
    "Format esa hisobotning yarmi: to‘g‘ri son noto‘g‘ri yozilsa, ishonchsiz ko‘rinadi.",
    [
        "Arifmetika: <code>+</code> <code>-</code> <code>*</code> <code>/</code>, qavs Exceldagi kabi.",
        "Foiz o‘zgarish: <code>(yangi - eski) / eski</code>.",
        "f-string: matn ichiga o‘zgaruvchi.",
        "Taqqoslash: <code>==</code> tengmi; bitta <code>=</code> — “qo‘y”.",
    ],
    "aov = 50000\nprev = 56000\nchange = (aov - prev) / prev\nprint(f\"AOV o‘zgarishi: {change:.1%}\")\nprint(f\"AOV: {aov:,.0f} so‘m\")",
    "Taxminan <code>AOV o‘zgarishi: -10.7%</code> va <code>AOV: 50,000 so‘m</code>. "
    "<code>:.1%</code> — foiz ko‘rinishi; <code>:,.0f</code> — ming ajratgich.",
    [
        "Qavssiz formula — boshqa tartib, boshqa javob.",
        '<code>"Toshkent" == "toshkent"</code> odatda False — harf katta-kichikligi muhim.',
        "Avval sonni print qiling, keyin chiroyli matn — xato sonni yashirmasin.",
    ],
    "O‘tgan oy 80, bu oy 92. Foiz o‘zgarishni hisoblab, f-string bilan chiroyli chiqaring.",
)

LECTURES["py-if"] = lesson(
    "Rahbar: “VIP larni ajrating.” Excelda IF. Python da ham shart: "
    "agar rost bo‘lsa — bir yo‘l, aks holda — boshqa. Odamdek o‘qiladi.",
    "Segmentatsiya, flag, ogohlantirish — hammasi shart. "
    "Noto‘g‘ri tartibda yozsangiz, VIP ham Regular bo‘lib qoladi.",
    [
        "Avval eng katta chegarani tekshiring (VIP).",
        "Keyin o‘rta (Regular).",
        "Qolganlar — New.",
        "<code>and</code> — hammasi rost; <code>or</code> — bittasi yetadi.",
    ],
    'def segment(revenue):\n    if revenue &gt;= 10000000:\n        return "VIP"\n    if revenue &gt;= 2000000:\n        return "Regular"\n    return "New"\n\nprint(segment(3500000))\nprint(segment(15000000))',
    "<code>Regular</code> va <code>VIP</code>. 3.5 mln — Regular; 15 mln — VIP. "
    "<code>return</code> — “javob shu, to‘xta.”",
    [
        "<code>if amount = 0</code> — xato. Taqqoslash: <code>==</code>.",
        "Chegara tartibini teskari yozmang.",
        "<code>if amount:</code> — 0 ni False deb yutadi; aniq <code>amount &gt; 0</code> yozing.",
    ],
    "O‘z qoidangizni yozing (masalan 5 mln VIP). 4 ta son bilan sinab ko‘ring.",
)

LECTURES["py-loop"] = lesson(
    "Uchta to‘lov: 120, 45, 80 ming. “50 mingdan kattalarini qo‘sh.” "
    "3 katak — oson. 8 ming qator bo‘lsa? Tsikl: bir xil ishni har element uchun.",
    "<code>for</code> — ro‘yxatdagi har biri. Kichik mantiqni o‘rganish uchun. "
    "Million qatorni sof Python for da yig‘ish sekin — keyinroq Pandas. "
    "Lekin g‘oya shu.",
    [
        "Ro‘yxat yarating.",
        "Yig‘indi uchun boshlang‘ich qiymat (0).",
        "Har element uchun shart tekshiring.",
        "Mos kelsa, yig‘indiga qo‘shing; oxirida print.",
    ],
    "amounts = [120000, 45000, 80000]\ntotal = 0\nfor a in amounts:\n    if a &gt;= 50000:\n        total += a\nprint(total)",
    "<code>200000</code> (120000 + 80000). 45000 tashlandi. "
    "<code>total += a</code> — “oldingi total ga a ni qo‘sh.”",
    [
        "Tsikl ichida millionta print — noutbuk qiynaladi. Print oxirida.",
        "<code>while</code> hisoblagich o‘zgarmasa — cheksiz tsikl. Tahlilda asosan <code>for</code>.",
        "Katta jadval — keyinroq <code>df[\"amount\"].sum()</code>.",
    ],
    "5 ta summa ro‘yxati yarating. 100000 dan kattalarini qo‘shib chiqaring.",
)

LECTURES["py-func"] = lesson(
    "AOV ni 12 joyga nusxa qildingiz — birini unutdingiz. Funksiya: hisob <strong>bitta joyda</strong>. "
    "Nom berasiz, kerakli narsani olasiz, javob qaytarasiz.",
    "Qoida o‘zgarsa, 12 joyni emas, bitta funksiyani tuzatasiz. "
    "Test qilish oson: kichik sonlar bilan tekshirib, keyin katta fayl.",
    [
        "<code>def</code> — yangi buyruq e’lon qilish.",
        "Qavs ichida kirish (parametrlar).",
        "<code>return</code> — javob.",
        "0 ga bo‘lishni ichida tekshiring.",
    ],
    "def aov(revenue, orders):\n    if orders == 0:\n        return None\n    return revenue / orders\n\nprint(aov(1200000, 40))\nprint(aov(500000, 0))",
    "30000.0 va <code>None</code>. Ikkinchi chaqiriqda dastur yiqilmaydi.",
    [
        "Nom: <code>aov</code>, <code>clean_amount</code> — tushunarli. <code>f1</code> — yo‘q.",
        "Funksiya ichida faqat hisob; faylga yozish tashqarida.",
        "0 ni sekin 1 ga almashtirmang — AOV ni yolg‘on qilasiz.",
    ],
    "<code>margin(revenue, cost)</code> funksiyasini yozing. cost=0 holatini ham o‘ylab ko‘ring.",
)

LECTURES["py-collections"] = lesson(
    "Ma’lumotni qayerga solish — muhim. Ro‘yxatmi? Unique to‘plammi? Kalit-qiymatmi? "
    "Noto‘g‘ri idish — keyin chalkash xato.",
    "Unique mijoz — set. Filial bo‘yicha tushum — dict. Kunlik cheklar — list. "
    "“Nima saqlayapman?” deb so‘rang, keyin tanlang.",
    [
        "<code>list</code> — tartib bor, o‘zgaradi.",
        "<code>tuple</code> — o‘zgarmas juftlik.",
        "<code>set</code> — unique.",
        "<code>dict</code> — kalit → qiymat.",
    ],
    'cities = ["Toshkent", "Samarqand", "Toshkent"]\nprint(set(cities))\nrevenue = {"Toshkent": 12500000}\nprint(revenue.get("Buxoro", 0))',
    "Set da Toshkent bir marta. <code>Buxoro</code> yo‘q — 0 qaytadi (xato emas). "
    "<code>revenue[\"Buxoro\"]</code> desangiz — KeyError.",
    [
        "<code>ids * 2</code> — unique emas, ikki marta takror.",
        "CustomerID takrorlanishi normal (ko‘p xarid). Order_id takrori — odatda muammo.",
        "Dict kaliti list bo‘lmaydi.",
    ],
    "3 shaharli list yarating (bittasi takror). Unique qiling. Dict da 2 filial tushumini saqlang.",
)

LECTURES["py-file"] = lesson(
    "CSV — oddiy matn jadvali. Lekin “Exceldan saqlash” ba’zan o‘zbekcha harflarni buzadi "
    "yoki vergul o‘rniga nuqtali vergul qo‘yadi. Bu Python aybi emas — fayl qanday yozilgani.",
    "Noto‘g‘ri encoding/sep — butun jadval bitta ustun bo‘lib ketadi yoki “krakozyabra”. "
    "Avval 1–2 qatorni ko‘z bilan ko‘ring.",
    [
        "Faylni Notepad da ochib, ajratuvchini ko‘ring (<code>,</code> yoki <code>;</code>).",
        "Encoding: ko‘pincha <code>utf-8-sig</code> (Excel CSV).",
        "Xom faylni o‘zgartirmang — tozalanganini boshqa joyga yozing.",
        "Kichik misolda satrlarni bo‘lib ko‘ring, keyin Pandas.",
    ],
    'lines = ["city;amount", "Toshkent;120000", "Samarqand;80000"]\nrows = [line.split(";") for line in lines]\nprint(rows)\n\nimport pandas as pd\ndf = pd.DataFrame({"city": ["Toshkent", "Samarqand"], "amount": [120000, 80000]})\nprint(df.head())',
    "Avval ro‘yxatlar ro‘yxati; keyin kichik jadval. Haqiqiy ishda: "
    "<code>pd.read_csv(..., encoding=\"utf-8-sig\", sep=\";\")</code>.",
    [
        "Separatorni taxmin qilmang.",
        "Xom CSV ni to‘g‘ridan tahrirlab saqlamang.",
        "<code>with open(...)</code> — faylni yopishni unutmang.",
    ],
    "O‘zingiz 3 qatorli mini-CSV matnini list qilib yozing va <code>split</code> bilan ustunlarga bo‘ling.",
)

LECTURES["py-except"] = lesson(
    "Dastur yiqildi — yaxshi xabar: “shu yerda muammo.” Yomon narsa — xatoni yutib, "
    "jim noto‘g‘ri hisobot chiqarish.",
    "CSV da <code>12a</code> bo‘lsa, <code>int</code> xato beradi. "
    "Butun pipeline o‘chmasin, shu qatorni belgilang va jurnalga yozing.",
    [
        "Kutilgan xato atrofini <code>try</code> ga oling.",
        "Aniq tur: <code>except ValueError</code> (yalang <code>except:</code> emas).",
        "Fallback qo‘ying (None) va xabar chiqaring.",
        "Keyin nechtasi None ekanini sanang.",
    ],
    'try:\n    orders = int("12a")\nexcept ValueError:\n    orders = None\n    print("orders ustuni tozalanmadi")\nprint(orders)',
    "Xabar chiqadi, <code>orders</code> — <code>None</code>. Dastur davom etadi.",
    [
        "Yalang <code>except:</code> hammasi yutadi — disk to‘la ham “jim”.",
        "Kutilmagan xato (sizning kodingiz) — yiqilsin, tuzating.",
        "Modullar: <code>import pandas as pd</code>; o‘z funksiyalaringizni alohida faylda saqlang.",
    ],
    "3 ta qiymatli list: \"10\", \"abc\", \"7\". Har birini int qilib ko‘ring; yomonlarini None qiling.",
)

LECTURES["np-ndarray"] = lesson(
    "Python list qulay, lekin millionta sonni birma-bir qo‘shish sekin. "
    "NumPy massivi — bir xil turdagi sonlar uchun tezkor hisob. "
    "Pandas ham ko‘pincha shu ustida turadi.",
    "O‘rtacha, og‘ish, filtr — tsiklsiz. Keyinroq DataFrame tushunarliroq bo‘lishi uchun "
    "avval massiv g‘oyasini biling.",
    [
        "<code>import numpy as np</code>.",
        "Massiv yarating.",
        "<code>mean</code>, <code>std</code> ni ko‘ring.",
        "Tur bir xil ekanini biling (dtype).",
    ],
    "import numpy as np\nx = np.array([10, 20, 30, 40], dtype=float)\nprint(x.mean())\nprint(x.std(ddof=1))",
    "O‘rtacha 25.0; std — tanlama og‘ishi (Excel STDEV.S ga yaqin). "
    "<code>ddof=0</code> boshqacha — hisobotda qaysi ekanini yozing.",
    [
        "Matn aralashsa, massiv “buzuq” bo‘lishi mumkin.",
        "NumPy internet ochmaydi, SQL o‘rnini bosmaydi — faqat hisob.",
        "Kichik misolda o‘rganing, keyin katta ustunga o‘ting.",
    ],
    "5 ta narx massivi yarating. mean va max ni chop eting.",
)

LECTURES["np-index"] = lesson(
    "Uchta narx, hammaga 12% chegirma. Excelda formulani pastga tortasiz. "
    "NumPy da: massiv <code>* 0.88</code>. Tsikl yo‘q. Shartga moslarini kesish — mask.",
    "“100 mingdan katta to‘lovlar” — SQL WHERE ga o‘xshash, lekin bitta ustun (massiv) uchun.",
    [
        "Massiv yarating.",
        "Shart yozing: <code>price &gt;= 100</code> → True/False massivi.",
        "Shu niqob bilan kesing: <code>price[price &gt;= 100]</code>.",
        "Skalyar ko‘paytirishni sinang.",
    ],
    "import numpy as np\nprice = np.array([100, 250, 80])\nprint(price[price &gt;= 100])\nprint(price * 0.88)",
    "Birinchi: 100 va 250. Ikkinchi: har narx * 0.88.",
    [
        "Ba’zi kesmalar view — asl massivga bog‘liq. Kerak bo‘lsa <code>.copy()</code>.",
        "Indeks 0 dan boshlanadi.",
        "Bu matn qidiruv yoki join emas — shartga mos elementlar.",
    ],
    "Massivda 4 ta summa. 50000 dan kattalarini chiqaring va hammaga +10% qo‘llang.",
)

LECTURES["np-nan"] = lesson(
    "O‘rtacha hisobladiz — javob <code>nan</code>. Bu “buzilish” emas: massivda teshik bor "
    "(noma’lum qiymat). Bitta NaN oddiy mean ni “zaharlaydi”.",
    "0 — “savdo yo‘q” (fakt). NaN — “bilmaymiz”. Aralashtirsangiz, KPI yolg‘on gapiradi.",
    [
        "NaN bor-yo‘qligini biling.",
        "Oddiy mean va nanmean farqini ko‘ring.",
        "Avval nechta NaN ekanini sanang.",
        "Keyin siyosat: tashlash / to‘ldirish / so‘rash.",
    ],
    "import numpy as np\nx = np.array([10, np.nan, 30])\nprint(np.mean(x))\nprint(np.nanmean(x))",
    "Birinchi — nan. Ikkinchi — 20.0 (teshikni o‘tkazib yuboradi).",
    [
        "Darhol hammaga 0 qo‘ymang — yashirish.",
        "40% NaN bo‘lsa — avval manbani so‘rang.",
        "Keyingi modulda Pandas da flag qo‘yamiz.",
    ],
    "4 elementli massivda 1 ta NaN qiling. mean va nanmean ni solishtiring.",
)

# --- Pandas & later ---
LECTURES["pd-df"] = lesson(
    "Excelda Table, SQL da natija jadvali. Pandas da bu — <strong>DataFrame</strong>: "
    "nomlangan ustunlar + qatorlar. Bitta ustun — Series.",
    "Tahlilchining asosiy idishi. Filtr, groupby, merge — hammasi DataFrame ustida. "
    "Avval jadvalni “ko‘rish” odatini o‘rganing.",
    [
        "DataFrame yarating (lug‘atdan).",
        "<code>head()</code> — birinchi qatorlar.",
        "<code>dtypes</code> — har ustun turi.",
        "<code>shape</code> — (qator, ustun).",
    ],
    'import pandas as pd\ndf = pd.DataFrame({\n    "city": ["Toshkent", "Samarqand"],\n    "amount": [120000, 80000],\n})\nprint(df.head())\nprint(df.dtypes)\nprint(df.shape)',
    "2×2 jadval ko‘rinadi; amount — int; shape (2, 2). "
    "Yangi CSV da tartib: head → dtypes → shape → keyin isna.",
    [
        "Darhol grafik/model — yo‘q. Avval ko‘z bilan o‘qing.",
        "<code>df[\"city\"]</code> — Series; <code>df[[\"city\",\"amount\"]]</code> — kichik DataFrame.",
        "Ustun nomlarini keyinroq tozalaymiz (snake_case).",
    ],
    "3 shaharli kichik DataFrame yozing. head, dtypes, shape ni chop eting.",
)

LECTURES["pd-filter"] = lesson(
    "SQL WHERE ning ukasi. “Faqat Toshkent” yoki “amount katta.” "
    "Avval har qator uchun True/False niqob, keyin shu niqob bilan kesasiz.",
    "Katta jadvaldan kerakli qatorlarni ajratmasangiz, KPI chalkashadi. "
    "Filtr — tahlilning asosiy pichoqi.",
    [
        "Shart yozing: <code>df[\"city\"] == \"Toshkent\"</code>.",
        "Bir nechta shart: <code>&amp;</code> (va), <code>|</code> (yoki) — har biri qavsda.",
        "Python <code>and</code>/<code>or</code> bu yerda ishlamaydi.",
        "Kerakli ustunlarni ham kesing.",
    ],
    'import pandas as pd\ndf = pd.DataFrame({"city": ["Toshkent", "Buxoro"], "amount": [5, 12]})\nprint(df[(df["city"] == "Toshkent") | (df["amount"] &gt; 10)])',
    "Toshkent qatori ham, amount=12 qatori ham chiqadi.",
    [
        "Qavssiz <code>&amp;</code> — xato yoki noto‘g‘ri niqob.",
        "Matnda yashirin bo‘shliq bo‘lsa, filtr “topmaydi” — trim keyinroq.",
        "<code>df.city</code> qisqa, lekin <code>df[\"city\"]</code> xavfsizroq.",
    ],
    "3 qatorli df yarating. Faqat amount &gt; 100000 qatorlarni chiqaring.",
)

LECTURES["pd-assign"] = lesson(
    "Amount bor, QQS yo‘q. Yangi ustun — hisoblangan maydon. "
    "Xom CSV ni emas, xotiradagi jadvalni kengaytirasiz.",
    "Har yangi ko‘rsatkich (QQS, chegirma, flag) — yangi ustun. "
    "Nomini rost yozing: 12% bo‘lsa, 15% ni ham vat demang.",
    [
        "Oddiy usul: <code>df[\"vat\"] = df[\"amount\"] * 0.12</code>.",
        "Yoki <code>assign</code> — zanjir uchun qulay.",
        "Filtrlangan bo‘lakka yozishda ehtiyot (SettingWithCopy).",
        "Xavfsiz: <code>loc</code> bilan yozing yoki <code>.copy()</code> oling.",
    ],
    'import pandas as pd\ndf = pd.DataFrame({"amount": [100, 200]})\ndf = df.assign(vat=lambda x: x["amount"] * 0.12)\nprint(df)',
    "amount va vat ustunlari: 12.0 va 24.0.",
    [
        "Filtrlab olingan bo‘lakka jim yozmang — natija g‘alati bo‘lishi mumkin.",
        "Uzun mantiqni lambda ichiga tiqmang — alohida funksiya.",
        "Yangi ustun — yangi haqiqat; nom yolg‘on bo‘lmasin.",
    ],
    "amount ustuniga 5% chegirma ustunini qo‘shing va chop eting.",
)

LECTURES["pd-na"] = lesson(
    "Bo‘sh katak. Pandas da ko‘pincha NaN — “noma’lum”. Bu 0 emas. "
    "0 — do‘kon yopiq (fakt). NaN — fayl kelmagan / kiritilmagan.",
    "NaN ni ko‘r-ko‘rona 0 qilsangiz, o‘rtacha va konversiya yolg‘on chiqadi. "
    "Avval ulushini o‘lchang, keyin siyosat yozing.",
    [
        "<code>isna()</code> bilan teshiklarni toping.",
        "Ulush: <code>isna().mean()</code>.",
        "Flag ustuni qo‘ying (keyinroq ajratib ko‘rish uchun).",
        "To‘ldirish yoki tashlash — biznes qoidasi bilan.",
    ],
    'import pandas as pd\ndf = pd.DataFrame({"amount": [10, None, 30]})\nprint(df["amount"].isna().mean())\ndf["amount_missing"] = df["amount"].isna()\ndf["amount"] = df["amount"].fillna(df["amount"].median())\nprint(df)',
    "Ulush 1/3. Flag True/False. Median bilan to‘ldirilgan qiymat — siyosat misoli, avtomatik haqiqat emas.",
    [
        "Hamma NaN → 0 — eng yomon odatlardan.",
        "Kalit maydon (order_id) bo‘sh — odatda tashlash + jurnal.",
        "Siyosatni yozib qo‘ying — ikki kishi boshqacha tozalamasin.",
    ],
    "4 qatorli df da 1 NaN qiling. Ulushini chop eting va flag qo‘ying.",
)

LECTURES["pd-dup"] = lesson(
    "Bir order_id ikki marta. Ba’zan eksport takrori, ba’zan join xatosi. "
    "Customer_id takrori esa normal (ko‘p xarid).",
    "Noto‘g‘ri subset bilan drop_duplicates — butun savdoni o‘chirib yuborishingiz mumkin.",
    [
        "Qaysi ustun unique bo‘lishi kerakligini aniqlang.",
        "<code>duplicated(...).sum()</code> — nechta ortiqcha.",
        "Keyin drop (keep first/last — qoida bilan).",
        "Nechta qator ketdi — jurnalga.",
    ],
    'import pandas as pd\ndf = pd.DataFrame({"order_id": [1, 1, 2], "amount": [10, 10, 5]})\nprint(df.duplicated(subset=["order_id"]).sum())\nprint(df.drop_duplicates("order_id"))',
    "1 ta dublikat belgi; keyin 2 qator qoladi.",
    [
        "Customer_id ni unique qilmang — revenue erib ketadi.",
        "Bir xil id, turli amount — konflikt; odam so‘rang.",
        "Avval sanang, keyin o‘chiring.",
    ],
    "5 qatorli df da 2 xil order_id takrorini yasang. duplicated sum va drop ni ko‘ring.",
)

LECTURES["pd-cast"] = lesson(
    "Yana “1 200” matni — endi butun ustun. Qo‘lda float() 50 ming marta emas: "
    "tozalash + <code>to_numeric</code>. Yomon katak — NaN bo‘lsin, dastur yiqilmasin.",
    "Tur belgilanmasa, sum/groupby ishlamasligi yoki matnni “qo‘shishi” mumkin.",
    [
        "Bo‘shliq/vergulni tozalang.",
        "<code>to_numeric(..., errors=\"coerce\")</code>.",
        "Nechta NaN chiqdi — sanang.",
        "Keyin siyosat (tashlash/to‘ldirish).",
    ],
    'import pandas as pd\ns = pd.Series([" 1 200 ", "abc", "3,5"])\nclean = s.str.replace(" ", "", regex=False).str.replace(",", ".", regex=False)\nprint(pd.to_numeric(clean, errors="coerce"))',
    "1200.0, NaN, 3.5. <code>abc</code> 0 ga aylanmadi — yaxshi.",
    [
        "Darhol <code>astype(int)</code> — bitta “abc” da yiqiladi.",
        "Avval coerce, keyin qaror.",
        "Ustun nomlarini ham tozalang (strip, snake_case).",
    ],
    "Series: \"10\", \"2 000\", \"x\". to_numeric coerce qiling va NaN sonini chop eting.",
)

LECTURES["pd-groupby"] = lesson(
    "SQL GROUP BY: har shahar uchun yig‘indi. Pandas da xuddi shu: "
    "uyum-uyum qilib, har uyumda sum/count.",
    "Region, kanal, oy bo‘yicha KPI — hisobotning yuragi. "
    "count vs nunique farqini biling.",
    [
        "Guruh kalitini tanlang (region).",
        "<code>agg</code> bilan o‘lchovlar yozing.",
        "Buyurtma soni uchun odatda <code>nunique(order_id)</code>.",
        "Natijani o‘qing: qaysi guruh katta/kichik.",
    ],
    'import pandas as pd\ndf = pd.DataFrame({\n    "region": ["Toshkent", "Toshkent", "Buxoro"],\n    "amount": [10, 20, 5],\n    "oid": [1, 2, 3],\n})\nprint(df.groupby("region").agg(revenue=("amount", "sum"), n=("oid", "nunique")))',
    "Toshkent: revenue 30, n 2. Buxoro: 5, 1.",
    [
        "count qatorlarni sanaydi; dublikat bo‘lsa shishadi.",
        "WHERE oldin, groupby keyin.",
        "Natija ustuniga tushunarli nom bering.",
    ],
    "4 qatorli df da 2 region. region bo‘yicha sum va count chiqaring.",
)

LECTURES["pd-merge"] = lesson(
    "Ism customers da, to‘lov orders da. Excel VLOOKUP / SQL JOIN. "
    "Pandas: <code>merge</code>. Qanday ulash — savolga bog‘liq (left/inner).",
    "Noto‘g‘ri join — qatorlar ko‘payib (fan-out), revenue 3 marta bo‘lishi mumkin.",
    [
        "Kalit ustunni aniqlang.",
        "Chap jadvalni tanlang (odatda fakt: orders).",
        "<code>how=\"left\"</code> — chapdagi hech kimni yo‘qotma.",
        "Merge oldin/keyin <code>len</code> ni solishtiring.",
    ],
    'import pandas as pd\norders = pd.DataFrame({"cid": [1, 2], "amount": [10, 20]})\ncust = pd.DataFrame({"cid": [1, 3], "name": ["Ali", "Nodira"]})\nprint(orders.merge(cust, on="cid", how="left"))',
    "Ali ulanadi; cid=2 uchun name NaN; Nodira bu natijada yo‘q (buyurtmasi yo‘q).",
    [
        "O‘ng jadvalda kalit dublikat — fan-out.",
        "1 va \"1\" mos kelmasligi mumkin — tur bir xil bo‘lsin.",
        "validate=\"many_to_one\" — himoya.",
    ],
    "Kichik orders/customers yarating. left merge qiling va len ni tekshiring.",
)

LECTURES["pd-dt"] = lesson(
    "Sana ko‘pincha matn. Matnni oy bo‘yicha to‘g‘ri guruhlab bo‘lmaydi. "
    "Avval haqiqiy sana: <code>to_datetime</code>.",
    "Trend, oylik KPI, recency — hammasi to‘g‘ri sanaga bog‘liq. "
    "Noto‘g‘ri dayfirst — butun oy siljiydi.",
    [
        "Ustunni datetime qiling.",
        "Oy kesimi: <code>.dt.to_period(\"M\")</code>.",
        "groupby bilan yig‘ing.",
        "Yomon sanalar — NaT; sanang.",
    ],
    'import pandas as pd\ndf = pd.DataFrame({\n    "dt": ["2024-01-31", "2024-02-01"],\n    "amount": [10, 20],\n})\ndf["dt"] = pd.to_datetime(df["dt"])\nprint(df.groupby(df["dt"].dt.to_period("M"))["amount"].sum())',
    "Yanvar 10, fevral 20.",
    [
        "03/04/2024 — martmi apreldami? ISO YYYY-MM-DD tinchroq.",
        "dayfirst ni faqat bilganingizda qo‘ying.",
        "Avval datetime, keyin period — str[:7] ga ishonmang.",
    ],
    "3 sana + amount. Oylik summani chiqaring.",
)

LECTURES["pd-eda"] = lesson(
    "Yangi dataset. Qo‘l qichishadi: darhol pie. To‘xtang. "
    "EDA — savol berish: hajm, tur, missing, taqsimot, anomaliya. Dashboard dan oldin.",
    "Chiroyli yolg‘on chizmaslik uchun. EDA insight urug‘ini beradi: "
    "“o‘rtacha shishgan — bitta katta chek.”",
    [
        "shape, dtypes, isna.",
        "describe — sonli taqsimot.",
        "value_counts — kategoriyalar.",
        "Kesimlar (groupby) va qisqa xulosa (5 jumla).",
    ],
    'import pandas as pd\ndf = pd.DataFrame({"amount": [1, 2, 3, 1000], "city": ["A", "A", "B", "B"]})\nprint(df.describe())\nprint(df["city"].value_counts(normalize=True))',
    "describe da 1000 dum ko‘rinadi; value_counts ulushni ko‘rsatadi.",
    [
        "Darhol dropna/model/pie — yo‘q.",
        "1000 xatomi yoki ulkan buyurtmami — EDA savolni ochadi, hukm emas.",
        "Har EDA oxirida 5 aniq jumla yozing.",
    ],
    "Kichik df da describe + value_counts qiling va 3 jumlalik xulosa yozing.",
)

LECTURES["py-mpl"] = lesson(
    "Grafik rahbar uchun. Maqsad — trendni 3 soniyada tushunish. "
    "3D pie va 20 rang — ishonchni o‘ldiradi.",
    "Oylik savdo — chiziq. Region taqqoslash — ustun. Taqsimot — hist. "
    "Bir grafik — bir savol.",
    [
        "Ma’lumotni tayyorlang (ro‘yxat yoki df).",
        "Mos turdagi chart tanlang.",
        "Title va o‘q nomlarini yozing.",
        "Notebookda show; skriptda savefig.",
    ],
    'import matplotlib\nmatplotlib.use("Agg")\nimport matplotlib.pyplot as plt\nmonths = ["Yan", "Fev", "Mar"]\nrevenue = [12500000, 11800000, 13100000]\nplt.plot(months, revenue)\nplt.title("Oylik savdo")\nplt.ylabel("so‘m")\nplt.tight_layout()\nprint("grafik tayyor")',
    "Chiziqli grafik yig‘iladi (Agg rejimida faylga saqlash mumkin). Muhimi — title/ylabel.",
    [
        "Pie ni deyarli ishlatmang.",
        "Shkala yolg‘on aytmasin.",
        "12 chiziq birga — hech kim o‘qimaydi.",
    ],
    "3 oylik revenue bilan chiziq chizing, title qo‘ying.",
)

LECTURES["py-sns"] = lesson(
    "Seaborn — statistik grafiklar uchun qulay qatlam (boxplot, heatmap). "
    "Ichida matplotlib, lekin defaultlari tahlilchiga yaqin.",
    "Dum/outlier ni ko‘rish — pie dan ko‘ra muhimroq. "
    "Korrelyatsiya — savol generator, sabab-oqibat emas.",
    [
        "DataFrame tayyorlang.",
        "boxplot: kategoriya × son.",
        "corr + heatmap — ehtiyot bilan.",
        "Grafik ostiga 1 jumla insight yozing.",
    ],
    'import matplotlib\nmatplotlib.use("Agg")\nimport pandas as pd\nimport seaborn as sns\ndf = pd.DataFrame({"region": ["Toshkent", "Toshkent", "Buxoro", "Buxoro"], "amount": [80, 1200, 40, 55]})\nax = sns.boxplot(data=df, x="region", y="amount")\nprint(type(ax).__name__)',
    "Boxplot obyekti yaratiladi. Toshkentda 1200 — dum/outlier sifatida ko‘zga tashlanadi.",
    [
        "Korrelyatsiya sabab emas.",
        "Chiroy baholanmaydi — insight jumlasi baholanadi.",
        "Stakeholderga kerak bo‘lmasa, murakkab CI ni majburan qo‘ymang.",
    ],
    "2 regionli df da boxplot qiling va 1 jumla yozing: qayerda dum bor?",
)

LECTURES["py-kpi"] = lesson(
    "KPI — qisqartma emas, <strong>kelishilgan ta’rif</strong>. "
    "Ikki kishi AOV ni boshqacha hisoblasa, ikkalasi ham “to‘g‘ri” deb urishadi.",
    "Koddan oldin qog‘oz: nima kiradi, nima chiqmaydi. "
    "Keyin funksiya — bitta joyda ta’rif.",
    [
        "Ta’rifni yozing (masalan AOV = revenue / unique orders).",
        "Funksiya qaytarsin (print qilmasin).",
        "0 bo‘linmani xavfsiz qiling.",
        "Kichik df da qo‘lda tekshiring.",
    ],
    'import pandas as pd\ndf = pd.DataFrame({"order_id": [1, 2], "amount": [100000, 200000]})\ndef kpi_summary(df):\n    orders = df["order_id"].nunique()\n    revenue = df["amount"].sum()\n    return {"orders": orders, "revenue": revenue, "aov": revenue / orders if orders else None}\nprint(kpi_summary(df))',
    "orders 2, revenue 300000, aov 150000.0.",
    [
        "Bekor cheklar kiritiladimi — ta’rifda yozing.",
        "“Faol mijoz” ni hujjatlashtiring.",
        "Ta’rif o‘zgarsa, bitta funksiyani yangilang.",
    ],
    "O‘z kpi_summary ni yozing va 3 qatorli df da tekshiring.",
)

LECTURES["py-rfm"] = lesson(
    "Mijoz 120 kundan beri xarid qilmagan — bu “jimlik”. "
    "Recency: so‘nggi xariddan beri necha kun. RFM ning R qismi.",
    "Qayta faollashtirish ro‘yxati uchun. Chegara (90 kun) — biznes parametri, sehrli son emas.",
    [
        "Hisobot sanasini (as_of) belgilang.",
        "Har mijozning oxirgi sanasini oling (max).",
        "Kun farqini hisoblang.",
        "Chegaradan katta/jimlarni sanang.",
    ],
    'import pandas as pd\ndf = pd.DataFrame({\n    "customer_id": [1, 1, 2, 3],\n    "order_date": pd.to_datetime(["2024-05-01", "2024-06-01", "2024-03-01", "2024-01-15"]),\n})\nas_of = pd.Timestamp("2024-08-01")\nlast = df.groupby("customer_id")["order_date"].max()\nrecency = (as_of - last).dt.days\nprint(recency)\nprint((recency &gt;= 90).sum())',
    "Har mijoz uchun recency kunlari; 90+ nechta ekani chiqadi.",
    [
        "Bekor buyurtmani “oxirgi xarid” deb olma — status filtri.",
        "customer_id bo‘sh mehmon cheklari — alohida.",
        "“Churn albatta” deb yozmang — “90 kun jim, qoidaga ko‘ra aloqa”.",
    ],
    "Kichik df da recency hisoblang. 60 kun chegarasi bilan nechta jim?",
)

LECTURES["py-final"] = lesson(
    "Oxirgi dars — yangi sehr yo‘q. Bitta savdo CSV: tozalash, KPI, kesim, 2 grafik, 5 tavsiya. "
    "“Yaxshilash kerak” tavsiya emas — aniq songa tayaning.",
    "Ishda shu ketma-ketlik: turlar → NaN siyosati → kalit dublikat → KPI → grafik → gap. "
    "Darhol model yoki hamma ustunga dropna — yo‘q.",
    [
        "Tozalash jurnali yozing (nechta bor edi / nima ketdi).",
        "Oylik revenue, AOV, unique mijoz — ta’rif bilan.",
        "Region × kanal kesimi.",
        "2 grafik + 5 aniq tavsiya.",
    ],
    'import pandas as pd\ndf = pd.DataFrame({\n    "order_id": [1, 2, 3, 4],\n    "customer_id": [10, 10, 11, 12],\n    "amount": [100000, 200000, 150000, 80000],\n    "order_date": pd.to_datetime(["2024-01-05", "2024-01-20", "2024-02-03", "2024-02-18"]),\n})\nmonthly = (\n    df.groupby(df["order_date"].dt.to_period("M"))\n      .agg(revenue=("amount", "sum"), orders=("order_id", "nunique"), customers=("customer_id", "nunique"))\n)\nmonthly["aov"] = monthly["revenue"] / monthly["orders"]\nprint(monthly)',
    "Oy kesimida revenue/orders/customers/aov — hisobot umurtqasi.",
    [
        "20 ta 3D chart — loyiha emas.",
        "Faqat print(df) — yetarli emas.",
        "Har tavsiya: kimga, nima qilsin, qaysi songa tayanadi.",
    ],
    "Shu namunaviy df dan oylik jadvalni o‘zingiz yig‘ing va 2 jumlalik insight yozing.",
)


def main() -> None:
    assert len(LECTURES) == 30, len(LECTURES)
    chunks = [
        '"""',
        "Python darslari — yangi boshlovchi uchun aniq, qadam-baqadam.",
        "Har dars: oddiy tilda → nima uchun → qadamlar → kod → natija → chalkashlik → mashq.",
        '"""',
        "",
        "LECTURES = {",
    ]
    for key, html in LECTURES.items():
        chunks.append(f'    "{key}": """')
        chunks.append(html)
        chunks.append('""",')
    chunks.append("}")
    chunks.append("")
    OUT.write_text("\n".join(chunks), encoding="utf-8")
    # sanity
    ns: dict = {}
    exec(OUT.read_text(encoding="utf-8"), ns)
    assert len(ns["LECTURES"]) == 30
    words = {k: len(v.split()) for k, v in ns["LECTURES"].items()}
    print("wrote", OUT)
    print("lessons", len(words))
    print("min/avg/max words", min(words.values()), round(sum(words.values()) / 30), max(words.values()))
    print("sample py-noldan-start", words["py-noldan-start"], "py-turlar", words["py-turlar"])


if __name__ == "__main__":
    main()
