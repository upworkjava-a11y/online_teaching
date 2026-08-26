"""
Statistika Data Analyst uchun — interpretatsiya va qaror, og‘ir formula emas.
"""

COURSE_DESCRIPTION = (
    "Statistika — formula yodlash emas: o‘rtacha yolg‘on gapirganda nima qilish, "
    "A/B ni rahbarga qanday aytish, p-value ni qo‘rqitmasdan tushunish. "
    "Do‘kon, bank va landing misollari bilan, o‘zbekcha."
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


MODULES = [
    {
        "order": 1,
        "title": "Ma’lumot va tanlanma",
        "slug": "st-kirish",
        "description": "Turlar, populyatsiya vs namuna, tahlilchi savoli.",
        "lectures": [
            _lec(
                "Statistika tahlilchiga nima beradi?",
                "st-nima",
                """
<h2>Dars maqsadi</h2>
<p>Statistika — “o‘rtacha chiqarish” emas. Bu <strong>noaniqlik ostida qaror</strong>: farq tasodifmi yoki haqiqiy signal?</p>
<h2>Biznes</h2>
<p>Landing sahifa konversiyasi 2.1% dan 2.4% ga chiqdi. Marketing “yutdik” deydi. Siz: namuna hajmi, vaqt oralig‘i, tashqi omil (bayram) bormi — deb so‘raysiz.</p>
<h2>Uch savol</h2>
<ol>
  <li>Bu son nimani o‘lchaydi (ta’rif)?</li>
  <li>Qanchalik barqaror (tarqalish, namuna)?</li>
  <li>Qanday harakat (to‘xtatish, kengaytirish, yana kutish)?</li>
</ol>
""",
            ),
            _lec(
                "Ma’lumot turlari",
                "st-turlar",
                """
<h2>Dars maqsadi</h2>
<p>Nominal, ordinal, interval, nisbat (ratio) — qaysi grafik va qaysi o‘rtacha mos.</p>
<ul>
  <li><strong>Nominal</strong> — viloyat, kanal (tartib yo‘q) → mode, count</li>
  <li><strong>Ordinal</strong> — qoniqish 1–5 → median ehtiyot bilan</li>
  <li><strong>Miqdoriy</strong> — summa, narx → mean/median, hist</li>
</ul>
<h2>Xato</h2>
<p>Viloyat kodining “o‘rtachasi” ma’nosiz. Likert 1–5 ni o‘rtacha qilish bahsli — avval taqsimotni ko‘ring.</p>
""",
            ),
            _lec(
                "Populyatsiya va namuna",
                "st-namuna",
                """
<h2>Dars maqsadi</h2>
<p>Populyatsiya — qiziqishdagi to‘liq to‘plam. Namuna — ko‘rgan qism. Ko‘p dashboardlar namuna (oxirgi 30 kun, bitta kanal).</p>
<h2>Bias</h2>
<p>Faqat ilova foydalanuvchilarini so‘rash — butun mijoz bazasini ifodalamaydi. Convenience sample xulosani cheklang.</p>
<h2>Tahlilchi tili</h2>
<p>“Barcha mijozlar” o‘rniga: “2024-yil mart, online kanal, to‘langan buyurtmalar.” Chegarani yozing.</p>
""",
            ),
        ],
        "practice": {
            "st-nima": _quiz(
                "st-q-lift",
                "Kichik o‘sish",
                "Konversiya 2.1% → 2.4%, n=80 tashrif.",
                "To‘g‘ri munosabat?",
                [
                    "A) Aniq g‘alaba, kampaniyani 10x",
                    "B) Farq kichik namuna tufayli shovqin bo‘lishi mumkin — hajm va barqarorlikni tekshirish",
                    "C) Statistika kerak emas",
                    "D) O‘rtacha viloyat",
                ],
                "B",
            ),
            "st-turlar": _quiz(
                "st-q-nominal",
                "Kanal ustuni",
                "Online / Offline / Marketplace.",
                "Qaysi tur?",
                ["A) Ratio", "B) Nominal kategoriya", "C) Interval temperatura", "D) Time series majburiy"],
                "B",
            ),
            "st-namuna": _quiz(
                "st-q-bias",
                "So‘rovnoma",
                "Faqat VIP mijozlar javob bergan.",
                "Xavf?",
                ["A) Yo‘q", "B) Selection bias — umumiy bazaga o‘tkazib bo‘lmaydi", "C) p doim 0", "D) GPU"],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "O‘z ish/o‘qish datasetidan 1 ta ko‘rsatkich tanlang.\n"
            "Yozing: populyatsiya ta’rifi, namuna chegarasi, ma’lumot turi, 1 ta mumkin bo‘lgan bias.\n"
            "1 sahifadan oshmasin."
        ),
    },
    {
        "order": 2,
        "title": "Markaziy tendentsiya",
        "slug": "st-markaz",
        "description": "Mean, median, mode — qachon qaysi biri.",
        "lectures": [
            _lec(
                "O‘rtacha (mean)",
                "st-mean",
                """
<h2>Dars maqsadi</h2>
<p>Mean — yig‘indi / n. Hammaga tanish, lekin dumli taqsimotda aldashi mumkin.</p>
<h2>Biznes</h2>
<p>O‘rtacha chek 180 ming, lekin 3 ta ulkan B2B shartnoma mean ni ko‘taradi. Oddiy chakana boshqacha ko‘rinadi.</p>
<h2>Qachon?</h2>
<p>Simmetrik, outlier kam. KPI sifatida mean ni median bilan juftlab bering.</p>
""",
                examples=["mean = sum(x) / len(x)  # outlier bo‘lsa median ni ham hisoblang"],
            ),
            _lec(
                "Median va mode",
                "st-median",
                """
<h2>Dars maqsadi</h2>
<p>Median — o‘rtadagi qiymat (50-percentile). Mode — eng ko‘p uchraydigan.</p>
<h2>Qachon median?</h2>
<p>Daromad, uy narxi, chek summasi — o‘ngga qiyshaygan. Median “oddiy mijoz”ga yaqinroq.</p>
<h2>Mode</h2>
<p>Eng mashhur SKU, eng ko‘p tanlangan to‘lov usuli. Miqdoriy uzluksizda mode kam foydali (bin qilmasangiz).</p>
""",
            ),
            _lec(
                "Qaysi markazni hisobotga?",
                "st-markaz-tanlash",
                """
<h2>Qoida</h2>
<table>
  <tr><th>Holat</th><th>Ko‘rsatkich</th></tr>
  <tr><td>Jami pul (kompaniya)</td><td>Yig‘indi + mean ehtiyot</td></tr>
  <tr><td>Tipik mijoz</td><td>Median</td></tr>
  <tr><td>Eng keng tarqalgan kategoriya</td><td>Mode</td></tr>
</table>
<p>Bitta son yetmasa — mean va median yonma-yon. Farq katta bo‘lsa — dum/outlier bor deb yozing.</p>
""",
            ),
        ],
        "practice": {
            "st-mean": _quiz(
                "st-q-outlier-mean",
                "Mean aldashi",
                "99 ta chek 50 ming, 1 ta 50 mln.",
                "Mean haqida?",
                ["A) Tipik chekni yaxshi ifodalaydi", "B) Kattaroq tomonga tortiladi — median ham kerak", "C) Mode yetarli", "D) p-value"],
                "B",
            ),
            "st-median": _quiz(
                "st-q-when-med",
                "Median",
                "Ish haqi taqsimoti qiyshaygan.",
                "Tipik xodim uchun?",
                ["A) Faqat max", "B) Median (va IQR)", "C) Faqat mode SKU", "D) Random"],
                "B",
            ),
            "st-markaz-tanlash": _quiz(
                "st-q-pair",
                "Hisobot",
                "Mean 12 mln, median 3 mln.",
                "Xulosa?",
                ["A) Xato hisob", "B) Dum/katta shartnomalar — ikkalasini ham ko‘rsatish", "C) Median o‘chirilsin", "D) A/B shart"],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "10–20 ta amount oling (yoki o‘ylab yozing, 1–2 outlier qo‘shing).\n"
            "Mean, median, mode (agar bor) ni hisoblang.\n"
            "Qaysi birini rahbarga aytasiz va nima uchun — 5–7 jumla."
        ),
    },
    {
        "order": 3,
        "title": "Tarqalish",
        "slug": "st-tarqalish",
        "description": "Range, variansiya, std, percentile, kvartil.",
        "lectures": [
            _lec(
                "Nima uchun o‘rtacha yetmaydi?",
                "st-spread",
                """
<h2>Dars maqsadi</h2>
<p>Ikki filialning o‘rtacha savdosi teng, lekin birida kunlik tebranish katta — ombor va kassa xavfi boshqacha.</p>
<p>Tarqalish: range, IQR, variansiya, standart og‘ish (std).</p>
""",
            ),
            _lec(
                "Variansiya va standart og‘ish",
                "st-std",
                """
<h2>Dars maqsadi</h2>
<p>Std — o‘rtachadan o‘rtacha og‘ishning “o‘lchami” (birlik asl o‘zgaruvchi bilan bir xil).</p>
<h2>ddof</h2>
<p>Namuna std odatda n−1 (ddof=1). Populyatsiya ma’lum bo‘lsa n. Hisobotda qaysi ekanini yozing.</p>
<h2>Interpretatsiya</h2>
<p>Std ni mean ga nisbatan (CV = std/mean) — turli o‘lchamdagi mahsulotlarni solishtirish.</p>
""",
                examples=["cv = std / mean  # nisbiy tarqalish"],
            ),
            _lec(
                "Percentile, kvartil, IQR",
                "st-percentile",
                """
<h2>Dars maqsadi</h2>
<p>p90 — 90% qiymat shu sondan kichik. Q1, Q2 (median), Q3. IQR = Q3−Q1 — o‘rta 50% kengligi.</p>
<h2>Biznes</h2>
<p>Yetkazib berish vaqti: median 2 kun, p95 = 8 kun — SLA ni p95 ga qarab qo‘ying, o‘rtachaga emas.</p>
<h2>Outlier qoidasi (qo‘pol)</h2>
<p>Q1−1.5·IQR dan tashqari — tekshirish uchun flag, avtomatik o‘chirish emas.</p>
""",
            ),
        ],
        "practice": {
            "st-spread": _quiz(
                "st-q-same-mean",
                "Bir xil mean",
                "A va B filial mean teng, B da std katta.",
                "Nima deysiz?",
                ["A) Bir xil biznes", "B) B barqaror emas — reja/ombor xavfi yuqori", "C) B yomon mean", "D) Mode"],
                "B",
            ),
            "st-std": _quiz(
                "st-q-cv",
                "CV",
                "Turli narxdagi tovarlar tarqalishi.",
                "Solishtirish?",
                ["A) Faqat range so‘mda", "B) CV (std/mean) yoki boshqa nisbiy o‘lchov", "C) Faqat n", "D) pie"],
                "B",
            ),
            "st-percentile": _quiz(
                "st-q-sla",
                "SLA",
                "Yetkazib berish.",
                "Mijoz tajribasi uchun qaysi?",
                ["A) Faqat min", "B) Median + p95 (dum)", "C) Faqat mean", "D) Mode kanal"],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "Bir o‘lchov (yetkazib berish kuni yoki amount) uchun min, max, std, Q1, median, Q3, p90 ni toping.\n"
            "SLA yoki “tipik vs dum” haqida 2 tavsiya yozing."
        ),
    },
    {
        "order": 4,
        "title": "Taqsimot, qiyshayish, outlier",
        "slug": "st-dist",
        "description": "Histogram, normal g‘oya, skewness, outlier siyosati.",
        "lectures": [
            _lec(
                "Taqsimotni o‘qish",
                "st-hist",
                """
<h2>Dars maqsadi</h2>
<p>Histogram / density — qayerda massa, qancha cho‘qqi, dum bormi.</p>
<h2>Shakllar</h2>
<ul>
  <li>Simmetrik</li>
  <li>O‘ng dum (savdo, daromad)</li>
  <li>Ikki cho‘qqi (ikki segment aralashgan — B2B+B2C)</li>
</ul>
<p>Ikki cho‘qqi ko‘rsangiz — o‘rtacha yolg‘on. Segmentlab qayta hisoblang.</p>
""",
            ),
            _lec(
                "Normal taqsimot — qachon taxmin?",
                "st-normal",
                """
<h2>Dars maqsadi</h2>
<p>Normal qo‘ng‘iroq shakli — ko‘p testlar shu taxminga tayanadi. Savdo summalari ko‘pincha normal emas.</p>
<h2>Tahlilchi</h2>
<p>n katta bo‘lsa mean ning tanlanma taqsimoti normalga yaqinlashadi (markaziy limit g‘oyasi) — lekin alohida chek hali ham qiyshaygan bo‘lishi mumkin.</p>
<p>Qoida: avval grafik, keyin test. “Normal deb faraz qildik” ni yozing.</p>
""",
            ),
            _lec(
                "Skewness va outlier",
                "st-skew",
                """
<h2>Dars maqsadi</h2>
<p>O‘ng qiyshayish: mean &gt; median. Outlier — xato (vergul) yoki haqiqiy ulkan buyurtma.</p>
<h2>Siyosat</h2>
<ol>
  <li>Aniqlash (IQR, z-score — qo‘pol)</li>
  <li>Manbani tekshirish</li>
  <li>Hisobotda alohida qator (“top 1%”) yoki winsorize (ehtiyot)</li>
  <li>Hech qachon sukut bilan o‘chirmaslik</li>
</ol>
""",
            ),
        ],
        "practice": {
            "st-hist": _quiz(
                "st-q-bimodal",
                "Ikki cho‘qqi",
                "Amount histogramida 2 cho‘qqi.",
                "Nima qilasiz?",
                ["A) Mean yetarli", "B) Segment aralashgan bo‘lishi mumkin — ajratib qayta tahlil", "C) dropna", "D) pie"],
                "B",
            ),
            "st-normal": _quiz(
                "st-q-sales-norm",
                "Savdo normalmi?",
                "Kunlik chek summasi.",
                "Odatda?",
                ["A) Doim aniq normal", "B) Ko‘pincha o‘ng dum — avval taqsimotni ko‘rish", "C) Faqat integer", "D) p=0"],
                "B",
            ),
            "st-skew": _quiz(
                "st-q-out-policy",
                "Outlier",
                "1 ta 10x katta buyurtma.",
                "To‘g‘ri?",
                ["A) Darhol o‘chirish", "B) Tekshirish + hisobotda alohida ko‘rsatish", "C) Mean ni 2 ga bo‘lish", "D) Ignore forever"],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "Histogram (yoki Excel bin) chizing.\n"
            "Shaklni tasvirlang (simmetrik/qiyshaygan/ikki cho‘qqi).\n"
            "1 ta outlier siyosatini yozing (o‘chirish/saqlash/ajratish)."
        ),
    },
    {
        "order": 5,
        "title": "Ehtimollik, tanlanma, ishonch oralig‘i",
        "slug": "st-prob",
        "description": "Asosiy ehtimollik, sampling, CI interpretatsiyasi.",
        "lectures": [
            _lec(
                "Ehtimollik tahlilchiga",
                "st-prob-intro",
                """
<h2>Dars maqsadi</h2>
<p>Ehtimollik — “qanchalik ishonamiz”. Mustaqil hodisalar, shartli ehtimollik (filtrlangan segment).</p>
<h2>Biznes</h2>
<p>Qaytarish ehtimoli kategoriya A da 8%, B da 2%. Aralash o‘rtacha 5% — ombor rejasida segment kerak.</p>
<p>Bayes tilida o‘ylash foydali: oldingi bilim + yangi ma’lumot. Formula yodlash shart emas, mantiq shart.</p>
""",
            ),
            _lec(
                "Tanlanma xatosi",
                "st-sampling",
                """
<h2>Dars maqsadi</h2>
<p>Har namuna boshqacha mean beradi. Kichik n — katta tebranish.</p>
<h2>Qoida</h2>
<p>Konversiya kabi ulushlar uchun n yetarlimi? 10 tashrifdan 1 xarid = 10% — ishonchsiz. 10 000 dan 1 000 = 10% — ancha barqaror.</p>
""",
            ),
            _lec(
                "Ishonch oralig‘i (CI)",
                "st-ci",
                """
<h2>Dars maqsadi</h2>
<p>95% CI — “shu usulni ko‘p takrorlasak, intervallarning ~95% haqiqiy parametrni qoplaydi.” Bitta interval “95% ehtimol ichida” deb soddalashtiriladi, lekin aniq ta’rif shu.</p>
<h2>Hisobot</h2>
<p>Konversiya 2.4% (95% CI: 1.9–2.9). Agar maqsad 3% bo‘lsa — hali yetishmayapti, deb ayting. Nuqta bahoni yolg‘iz bermang.</p>
""",
            ),
        ],
        "practice": {
            "st-prob-intro": _quiz(
                "st-q-mix",
                "Aralash ulush",
                "A 8%, B 2%, teng hajm.",
                "Umumiy qaytarish?",
                ["A) 8%", "B) taxminan 5% — segmentni yashirmang", "C) 2%", "D) 10%"],
                "B",
            ),
            "st-sampling": _quiz(
                "st-q-n10",
                "n=10",
                "10 tashrif, 3 xarid.",
                "30% konversiya?",
                ["A) Aniq haqiqat", "B) Juda shovqinli — CI keng, qarorni kechiktirish/yig‘ish", "C) A/B yutdi", "D) Median 30"],
                "B",
            ),
            "st-ci": _quiz(
                "st-q-ci-use",
                "CI",
                "2.4% (1.9–2.9), maqsad 3%.",
                "Xulosa?",
                ["A) Maqsad bajarildi", "B) Nuqta 2.4, interval 3% ni qo‘shmaydi — ehtiyot xulosa", "C) p=1", "D) std=0"],
                "B",
                difficulty="medium",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "Bir ulush (masalan, 40/2000 = 2%).\n"
            "Python yoki onlayn kalkulyator bilan 95% CI ni toping (yoki formula g‘oyasini yozing).\n"
            "Rahbarga 3 jumlada tushuntiring."
        ),
    },
    {
        "order": 6,
        "title": "Korrelyatsiya va kovariatsiya",
        "slug": "st-corr",
        "description": "Bog‘liqlik ≠ sabab; heatmap ehtiyoti.",
        "lectures": [
            _lec(
                "Kovariatsiya va korrelyatsiya",
                "st-corr-intro",
                """
<h2>Dars maqsadi</h2>
<p>Korrelyatsiya (Pearson) −1…1: chiziqli bog‘liqlik. Birlikdan mustaqil. Kovariatsiya birlikka bog‘liq — taqqoslash qiyin.</p>
<h2>Spearman</h2>
<p>Monoton, lekin chiziqli bo‘lmagan bog‘liqlik / outlier da barqarorroq.</p>
""",
            ),
            _lec(
                "Sabab emas",
                "st-causation",
                """
<h2>Klassik xato</h2>
<p>Muzqaymoq savdosi va cho‘kish — yoz sabab. Marketing spend va revenue o‘sishi — mavsum yoki narx ham o‘zgargan bo‘lishi mumkin.</p>
<p>Tahlilchi tili: “birga harakat qiladi”, “sabab bo‘ldi” emas — tajriba yoki yaxshi dizayn bo‘lmasa.</p>
""",
            ),
            _lec(
                "Amaliy tekshiruv",
                "st-corr-check",
                """
<h2>Qadamlar</h2>
<ol>
  <li>Scatter chizing — outlier bormi?</li>
  <li>Pearson + Spearman</li>
  <li>Segment (region) bo‘yicha alohida</li>
  <li>Vaqt kechikishi (lag) — kampaniya keyin savdo</li>
</ol>
<p>r=0.9 lekin n=8 — ishonmang. n ni yozing.</p>
""",
            ),
        ],
        "practice": {
            "st-corr-intro": _quiz(
                "st-q-pearson",
                "Pearson",
                "r = 0.05, n=5000.",
                "Chiziqli bog‘liqlik?",
                ["A) Juda kuchli", "B) Deyarli yo‘q (lekin n katta — p kichik bo‘lishi mumkin, amaliy ahamiyat yo‘q)", "C) Sabab aniq", "D) Mode"],
                "B",
                difficulty="medium",
            ),
            "st-causation": _quiz(
                "st-q-ice",
                "Sabab",
                "Ikkita seriya birga o‘sadi.",
                "Darhol?",
                ["A) A B ni keltirib chiqardi", "B) Bog‘liqlik; sabab uchun dizayn/mantiq kerak", "C) r=1", "D) drop column"],
                "B",
            ),
            "st-corr-check": _quiz(
                "st-q-n8",
                "Kichik n",
                "r=0.92, n=8.",
                "Ishonch?",
                ["A) Ideal model", "B) Juda nozik — scatter va ko‘proq nuqta kerak", "C) A/B done", "D) CI=0"],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "Ikki o‘lchov (reklama, savdo yoki harorat, savdo — ixtiyoriy).\n"
            "Scatter + korrelyatsiya.\n"
            "“Sabab emas, chunki …” jumlasini yozing."
        ),
    },
    {
        "order": 7,
        "title": "Gipoteza, p-value, A/B test",
        "slug": "st-ab",
        "description": "H0/H1, p-value noto‘g‘ri tushunchalari, A/B amaliyoti.",
        "lectures": [
            _lec(
                "Gipotezani tekshirish g‘oyasi",
                "st-h0",
                """
<h2>Dars maqsadi</h2>
<p>H0 — “farq yo‘q / effekt yo‘q”. Ma’lumot H0 ni qanchalik “ajablantiradi”.</p>
<p>p-value — H0 rost bo‘lsa, shunchalik yoki undan ham ekstremal natija ko‘rish ehtimoli. Bu “H0 rost ehtimoli” emas, “biznes muvaffaqiyat ehtimoli” ham emas.</p>
""",
            ),
            _lec(
                "p-value ni qanday aytish",
                "st-pvalue",
                """
<h2>Noto‘g‘ri</h2>
<ul>
  <li>“p=0.04 demak 96% ishonch bilan yutdik”</li>
  <li>“p=0.06 hech narsa yo‘q, to‘xtatamiz”</li>
</ul>
<h2>To‘g‘riroq</h2>
<p>Effekt o‘lchami + CI + p. p=0.049 va p=0.051 deyarli bir xil. α=0.05 — kelishuv, sehrli chegara emas.</p>
<p>Ko‘p test (20 ta KPI) — yolg‘on ijobiy ko‘payadi. Oldindan asosiy metrikani belgilang.</p>
""",
            ),
            _lec(
                "A/B test tahlilchi nazarida",
                "st-abtest",
                """
<h2>Dizayn</h2>
<ol>
  <li>Bitta asosiy metrika</li>
  <li>Minimal aniqlamoqchi effekt (MDE) va n</li>
  <li>Randomizatsiya, peeking (erta to‘xtatish) xavfi</li>
  <li>Segment (qurilma) oldindan, p-hacking emas</li>
</ol>
<h2>Natija</h2>
<p>“Yutgan variant +0.3 pp (CI …). Amaliy ahamiyat: qo‘shimcha 12 mln/oy. Texnik qarz: sahifa sekinlashdi — trade-off.”</p>
""",
            ),
        ],
        "practice": {
            "st-h0": _quiz(
                "st-q-pdef",
                "p-value",
                "Ta’rif.",
                "p nima?",
                [
                    "A) H0 rost ehtimoli",
                    "B) H0 ostida shunday/ekstremal natija ehtimoli",
                    "C) Effekt kattaligi",
                    "D) Accuracy",
                ],
                "B",
                difficulty="medium",
            ),
            "st-pvalue": _quiz(
                "st-q-peek",
                "Ko‘p KPI",
                "20 ta metrika, biri p<0.05.",
                "Xavf?",
                ["A) Yo‘q", "B) Yolg‘on ijobiy / p-hacking — asosiy metrika oldindan", "C) Normal taqsimot buzildi", "D) Median"],
                "B",
            ),
            "st-abtest": _quiz(
                "st-q-mde",
                "A/B",
                "n kichik, kutilgan effekt 0.1%.",
                "Muammo?",
                ["A) Doim yetarli", "B) Power past — farqni ko‘rmaslik mumkin", "C) CI yo‘qoladi", "D) SQL kerak emas"],
                "B",
            ),
        },
        "exercises": [],
        "homework": _hw(
            "Fiktiv A/B: A 120/5000, B 150/5000.\n"
            "Ulushlar, taxminiy farq, p-value ni hisoblang (kalkulyator yoki Python).\n"
            "Rahbarga: yutdimi, shubhaliman, nima qilaman — 3 bullet."
        ),
    },
    {
        "order": 8,
        "title": "Regressiya asoslari va interpretatsiya",
        "slug": "st-reg",
        "description": "Chiziqli g‘oya, koeffitsiyent, ehtiyotkor xulosa.",
        "lectures": [
            _lec(
                "Oddiy chiziqli regressiya",
                "st-linreg",
                """
<h2>Dars maqsadi</h2>
<p>y ≈ a + b·x. b — x 1 birlik o‘zgaganda y ning o‘rtacha o‘zgarishi (boshqa narsa doimiy, deb model aytadi — hayotda emas).</p>
<h2>Biznes</h2>
<p>Reklama so‘miga savdo. b musbat — bog‘liqlik; sabab emas. Residual (qoldiq) ni ko‘ring.</p>
""",
            ),
            _lec(
                "R² va haddan oshirish",
                "st-rsq",
                """
<h2>R²</h2>
<p>Model qancha variansni “tushuntiradi”. Yuqori R² yomon modelni yashirmaydi (o‘ta moslash, o‘zgaruvchi oqishi).</p>
<p>Tahlilchi: grafik + biznes mantiq + oddiy baseline (o‘tgan oy o‘rtachasi) bilan solishtirish.</p>
""",
            ),
            _lec(
                "Yakun: qaror tilida yozish",
                "st-interpret",
                """
<h2>Shablon</h2>
<ol>
  <li>Savol va populyatsiya</li>
  <li>Ko‘rsatkich ta’rifi</li>
  <li>Son + noaniqlik (CI / tarqalish)</li>
  <li>Cheklov (namuna, bias)</li>
  <li>Tavsiya (1 ta aniq harakat)</li>
</ol>
<p>Bu kurs yopilishi: siz “p kichik” emas, “shu chegara ichida shunday qilishni maslahat beraman” deysiz.</p>
""",
            ),
        ],
        "practice": {
            "st-linreg": _quiz(
                "st-q-slope",
                "Slope",
                "b = 0.3, x=reklama mln, y=savdo mln.",
                "Ehtiyotkor o‘qish?",
                [
                    "A) 1 mln reklama aniq +0.3 mln savdo sabab",
                    "B) Model bo‘yicha o‘rtacha bog‘liqlik; sabab va boshqa omillar ochiq",
                    "C) R²=1",
                    "D) p yo‘qoladi",
                ],
                "B",
            ),
            "st-rsq": _quiz(
                "st-q-r2",
                "R² yuqori",
                "R²=0.95, 3 nuqta.",
                "?",
                ["A) Mukammal bashorat", "B) n kichik / haddan moslashish xavfi", "C) A/B", "D) Mode=0.95"],
                "B",
            ),
            "st-interpret": _quiz(
                "st-q-tmpl",
                "Hisobot",
                "Yaxshi xulosa tarkibi?",
                "Nimalar?",
                [
                    "A) Faqat p-value",
                    "B) Savol, ta’rif, son+noaniqlik, cheklov, harakat",
                    "C) Faqat pie",
                    "D) 20 ta jargon",
                ],
                "B",
            ),
        },
        "exercises": [
            _quiz(
                "st-cap",
                "Kurs yakuni",
                "Konversiya +0.2 pp, CI noldan o‘tadi, p=0.11, n katta emas.",
                "Eng to‘g‘ri?",
                [
                    "A) Aniq yutqazdik, to‘xtatamiz",
                    "B) Aniq yutdik",
                    "C) Noaniq/kuchsiz dalil — effekt kichik, ko‘proq ma’lumot yoki sifat tahlili",
                    "D) Mean=median",
                ],
                "C",
                difficulty="hard",
            ),
        ],
        "homework": _hw(
            "Bitta biznes savolni shablon bo‘yicha yozing (5 band).\n"
            "Ixtiyoriy: o‘qish/Python da oddiy regressiya yoki A/B sonlari.\n"
            "Jargonni minimallashtiring — rahbar o‘qishi kerak."
        ),
    },
]


def build_statistics_modules():
    from apps.core.statistics_teacher_lessons import LECTURES

    for module in MODULES:
        for lecture in module["lectures"]:
            html = LECTURES.get(lecture["slug"])
            if html:
                lecture["content"] = html.strip()
    return MODULES
