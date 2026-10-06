"""Beginner-friendly visual blocks for Python lectures (no extra assets required)."""

from __future__ import annotations

_BLOCKS: dict[str, str] = {
    "py-noldan-start": """
<div class="esp-visual">
  <p class="esp-visual-label">Birinchi 15 daqiqa</p>
  <ol class="esp-timeline">
    <li><span class="esp-time">1</span><span class="esp-step"><strong>O‘rnatish</strong> — python.org yoki VS Code</span></li>
    <li><span class="esp-time">2</span><span class="esp-step"><strong>print</strong> — bir qator kod</span></li>
    <li><span class="esp-time">3</span><span class="esp-step"><strong>Sinash</strong> — 2+2, matn chiqarish</span></li>
  </ol>
</div>
""".strip(),
    "py-noldan-errors": """
<div class="esp-try">
  <p class="esp-try-label">Xato xaritasi</p>
  <div class="esp-cards esp-cards-3">
    <div class="esp-card"><strong>SyntaxError</strong><span>yozuv xato — qavs, qo‘shtirnoq</span></div>
    <div class="esp-card"><strong>NameError</strong><span>noma topilmadi</span></div>
    <div class="esp-card"><strong>ZeroDivisionError</strong><span>0 ga bo‘lish</span></div>
  </div>
</div>
""".strip(),
    "py-nima": """
<div class="esp-visual">
  <p class="esp-visual-label">Excel vs Python</p>
  <div class="esp-cards esp-cards-3">
    <div class="esp-card"><strong>Excel</strong><span>tez, kichik hajm</span></div>
    <div class="esp-card"><strong>Python</strong><span>ko‘p fayl, takroriy qoida</span></div>
    <div class="esp-card"><strong>Pandas</strong><span>100 ming+ qator</span></div>
  </div>
</div>
""".strip(),
    "py-turlar": """
<div class="esp-try">
  <p class="esp-try-label">5 ta tur — yodda saqlang</p>
  <ul class="esp-checklist">
    <li><code>int</code> — butun son</li>
    <li><code>float</code> — o‘nli</li>
    <li><code>str</code> — matn (CSV dagi “son” ko‘pincha shu)</li>
    <li><code>bool</code> — True/False</li>
    <li><code>None</code> — qiymat yo‘q</li>
  </ul>
</div>
""".strip(),
    "py-if": """
<div class="esp-scenario">
  <p class="esp-try-label">Segment qoidasi</p>
  <p>≥10 mln → VIP · ≥2 mln → Regular · aks holda → New (chegaralarni yuqoridan pastga tekshiring)</p>
</div>
""".strip(),
    "pd-df": """
<div class="esp-visual">
  <p class="esp-visual-label">DataFrame = Excel jadval</p>
  <p class="muted" style="margin:0">Qatorlar — yozuvlar, ustunlar — maydonlar. <code>df.head()</code> bilan birinchi 5 qatorni ko‘ring.</p>
</div>
""".strip(),
    "py-loop": """
<div class="esp-try">
  <p class="esp-try-label">for vs katta data</p>
  <div class="esp-cards esp-cards-3">
    <div class="esp-card"><strong>Kichik list</strong><span>for — o‘rganish</span></div>
    <div class="esp-card"><strong>Katta CSV</strong><span>Pandas sum()</span></div>
    <div class="esp-card"><strong>Qoida</strong><span>print oxirida</span></div>
  </div>
</div>
""".strip(),
    "py-func": """
<div class="esp-scenario">
  <p class="esp-try-label">Funksiya qoidasi</p>
  <p>Hisob <strong>bitta joyda</strong>. <code>orders == 0</code> → <code>None</code>. Print — tashqarida.</p>
</div>
""".strip(),
    "py-collections": """
<div class="esp-try">
  <p class="esp-try-label">4 ta to‘plam</p>
  <ul class="esp-checklist">
    <li><code>list</code> — tartibli</li>
    <li><code>dict</code> — kalit→qiymat</li>
    <li><code>set</code> — unique</li>
    <li><code>tuple</code> — o‘zgarmas juft</li>
  </ul>
</div>
""".strip(),
    "pd-filter": """
<div class="esp-scenario">
  <p class="esp-try-label">Pandas filtr</p>
  <p><code>(mask1) &amp; (mask2)</code> — <code>and</code> emas. Qavslar majburiy.</p>
</div>
""".strip(),
    "pd-na": """
<div class="esp-visual">
  <p class="esp-visual-label">NaN ≠ 0</p>
  <div class="esp-cards esp-cards-3">
    <div class="esp-card"><strong>0</strong><span>haqiqiy nol savdo</span></div>
    <div class="esp-card"><strong>NaN</strong><span>noma’lum</span></div>
    <div class="esp-card"><strong>Flag</strong><span>amount_missing</span></div>
  </div>
</div>
""".strip(),
    "pd-groupby": """
<div class="esp-try">
  <p class="esp-try-label">groupby + agg</p>
  <p class="muted" style="margin:0">Region bo‘yicha: <code>sum(amount)</code>, <code>nunique(order_id)</code> → AOV.</p>
</div>
""".strip(),
    "pd-merge": """
<div class="esp-scenario">
  <p class="esp-try-label">Join xavfi</p>
  <p>O‘ng jadvalda dublikat kalit → <strong>fan-out</strong> (qatorlar sun’iy ko‘payadi). Avval tekshiring.</p>
</div>
""".strip(),
    "py-mpl": """
<div class="esp-visual">
  <p class="esp-visual-label">Grafik tanlash</p>
  <div class="esp-cards esp-cards-3">
    <div class="esp-card"><strong>Trend</strong><span>line</span></div>
    <div class="esp-card"><strong>Solishtirish</strong><span>bar</span></div>
    <div class="esp-card"><strong>Taqsimot</strong><span>hist / box</span></div>
  </div>
</div>
""".strip(),
    "py-kpi": """
<div class="esp-try">
  <p class="esp-try-label">KPI = ta’rif</p>
  <p class="muted" style="margin:0">AOV = revenue / unique orders. Ikki jamoa boshqacha hisoblasa — hujjatlashtiring.</p>
</div>
""".strip(),
    "py-final": """
<div class="esp-visual">
  <p class="esp-visual-label">Capstone tartib</p>
  <ol class="esp-timeline">
    <li><span class="esp-time">1</span><span class="esp-step"><strong>Tozalash</strong> + jurnal</span></li>
    <li><span class="esp-time">2</span><span class="esp-step"><strong>3 KPI</strong> (ta’rif bilan)</span></li>
    <li><span class="esp-time">3</span><span class="esp-step"><strong>Vizual + tavsiya</strong></span></li>
  </ol>
</div>
""".strip(),
}


def append_visuals(slug: str, html: str) -> str:
    block = _BLOCKS.get(slug)
    if not block or block in html:
        return html
    marker = "<h2>Dars maqsadi</h2>"
    if marker in html:
        return html.replace(marker, block + "\n\n" + marker, 1)
    return block + "\n\n" + html
