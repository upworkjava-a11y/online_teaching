"""Module 1 — Python noldan (absolute beginners). Merged in build_python_modules()."""

from apps.core.python_content import _hw, _lec, _quiz

BEGINNER_MODULE = {
    "order": 1,
    "title": "Python noldan",
    "slug": "py-noldan",
    "description": "O‘rnatish, birinchi qator kod, xatolarni o‘qish — hech narsa bilmasdan boshlash.",
    "lectures": [
        _lec(
            "Python va birinchi qator",
            "py-noldan-start",
            """
<h2>Dars maqsadi</h2>
<p>Python nima ekanini tushunasiz, REPL yoki Notebook da birinchi <code>print</code> ni yozasiz.</p>

<h2>Kim uchun?</h2>
<p>Dasturchi bo‘lish shart emas. Excel, bank yoki savdo bilan ishlaysiz — Python keyinroq takroriy ishlarni avtomatlashtiradi. Bugun faqat: “kod yozdim → ekranda ko‘rdim”.</p>

<h2>Birinchi qator</h2>
<pre>print("Salom, tahlil!")</pre>
<p><code>print</code> — natijani ekranga chiqaradi. Qavs ichidagi matn — qo‘shtirnoqda.</p>

<h2>Qayerda yozamiz?</h2>
<ul>
  <li><strong>python.org</strong> yoki Microsoft Store — Python o‘rnatish</li>
  <li><strong>VS Code</strong> + Python kengaytmasi — oddiy <code>.py</code> fayl</li>
  <li><strong>Jupyter</strong> — keyinroq; hozir REPL yoki bitta fayl yetarli</li>
</ul>

<h2>Odat</h2>
<p>Har yangi g‘oyani 3 qator kod bilan sinab ko‘ring. Katta fayl emas — kichik parcha.</p>
""",
            examples=['print("Men Python o‘rganyapman")\nprint(2 + 2)'],
        ),
        _lec(
            "Skript fayl va izoh",
            "py-noldan-run",
            """
<h2>Dars maqsadi</h2>
<p><code>.py</code> fayl yaratib, terminaldan ishga tushirasiz; izoh (<code>#</code>) bilan kodni tushuntirasiz.</p>

<h2>Fayl vs REPL</h2>
<p>REPL — bir qator sinov. Skript — saqlangan retsept: har dushanba bir xil ishga tushirasiz.</p>

<h2>Izoh</h2>
<pre># Bu izoh — Python buni o‘qimaydi
revenue = 1000000  # tushum, so‘m (1 mln)</pre>

<h2>Ishga tushirish</h2>
<p>Terminal: <code>python my_report.py</code> (Windows da ba’zan <code>py my_report.py</code>).</p>

<h2>Xato</h2>
<p>Fayl nomini xato yozsangiz yoki papkada emassiz — “file not found”. Avval <code>cd</code> bilan to‘g‘ri papkaga o‘ting.</p>
""",
            examples=[
                "# mini hisobot\nregion = \"Toshkent\"\nprint(f\"Filial: {region}\")",
            ],
        ),
        _lec(
            "Xatolarni o‘qish",
            "py-noldan-errors",
            """
<h2>Dars maqsadi</h2>
<p>Qizil xabar (traceback) dan qaysi qator va qanday xato ekanini topasiz — qo‘rqmasdan.</p>

<h2>SyntaxError</h2>
<p>Qavs yopilmagan, qo‘shtirnoq unutilgan. Xabar odatda qator raqamini ko‘rsatadi.</p>

<h2>NameError</h2>
<p>O‘zgaruvchi nomi xato yoki hali yaratilmagan: <code>revnue</code> o‘rniga <code>revenue</code>.</p>

<h2>ZeroDivisionError</h2>
<p>0 ga bo‘lish. AOV da <code>orders == 0</code> ni tekshiring.</p>

<h2>Strategiya</h2>
<ol>
  <li>Xabarning <strong>oxirgi qatorini</strong> o‘qing (xato turi).</li>
  <li><strong>Qator raqamiga</strong> qarang.</li>
  <li>Bitta o‘zgarish qiling, qayta ishga tushiring.</li>
</ol>
""",
            examples=[
                "# SyntaxError misoli (izohda):\n# print(\"hello\"   # qavs yopilmagan",
            ],
        ),
    ],
    "practice": {
        "py-noldan-start": _quiz(
            "py-noldan-q-print",
            "print",
            "Birinchi dars.",
            "print('OK') nima qiladi?",
            [
                "A) Faylni o‘chiradi",
                "B) OK matnini ekranga chiqaradi",
                "C) Internetga ulanadi",
                "D) Excel ochadi",
            ],
            "B",
        ),
        "py-noldan-run": _quiz(
            "py-noldan-q-comment",
            "Izoh",
            "Skript.",
            "# revenue = 100  qatori nima qiladi?",
            [
                "A) revenue ni 100 qiladi",
                "B) Hech narsa — bu izoh, Python o‘tkazib yuboradi",
                "C) Xato beradi doim",
                "D) Faylni yopadi",
            ],
            "B",
        ),
        "py-noldan-errors": _quiz(
            "py-noldan-q-trace",
            "Traceback",
            "Xato.",
            "Traceback da eng avvalo nimaga qarasiz?",
            [
                "A) Kompyuterni o‘chirib yoqish",
                "B) Xato turi va qator raqami",
                "C) Faqat fayl nomi",
                "D) Hech narsa",
            ],
            "B",
        ),
    },
    "exercises": [],
    "homework": _hw(
        "1) Python o‘rnating (yoki mavjud versiyani tekshiring: python --version).\n"
        "2) hello.py yarating: 2 ta print va 1 ta izoh.\n"
        "3) Ataylab kichik xato qiling, traceback ni o‘qing, tuzating.\n"
        "Skrinshot yoki kodni yuklang."
    ),
}
