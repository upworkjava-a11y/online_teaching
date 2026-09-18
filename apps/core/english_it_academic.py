"""
Academic English for IT / Computer Science — EAP module + lesson enrichments.

Inspired by university EAP/ESP courses for CS (abstracts, papers, presentations,
citations, lecture note-taking) — original classroom wording.
"""

from __future__ import annotations

from apps.core.english_it_content import _hw, _lec, _quiz

# Appended to every workplace lesson (once) during build.
_LESSON_ENRICHMENT = """
<h2>Collocations & useful chunks</h2>
<ul>
  <li><strong>raise a ticket</strong> / <strong>resolve an issue</strong> / <strong>share an update</strong></li>
  <li><strong>meet the deadline</strong> / <strong>block the release</strong> / <strong>review the pull request</strong></li>
  <li><strong>in production</strong> / <strong>on staging</strong> / <strong>behind schedule</strong></li>
</ul>

<h2>Academic / study tip</h2>
<p>When you study this topic for university or certification, practise <strong>paraphrasing</strong>:
read one paragraph, close the page, then write the idea in your own English words.
Keep technical terms (API, sprint, latency) but change the sentence structure.
Never copy a paper sentence without a citation.</p>

<h2>Mini writing task</h2>
<p>Write 4–6 sentences that summarise today’s lesson for a classmate who missed class.
Use present simple for facts and <em>we / you</em> for advice.</p>
""".strip()


def enrich_lecture_html(html: str) -> str:
    """Add collocations, academic tip, and mini writing if not already present."""
    text = (html or "").strip()
    if not text:
        return text
    if "Academic / study tip" in text or "Collocations & useful chunks" in text:
        return text
    # Insert enrichment before Quick review when possible
    marker = "<h2>Quick review</h2>"
    if marker in text:
        return text.replace(marker, _LESSON_ENRICHMENT + "\n\n" + marker, 1)
    return text + "\n\n" + _LESSON_ENRICHMENT


def enrich_modules(modules: list[dict]) -> list[dict]:
    """Return a deep-enough copy with enriched lecture HTML."""
    out = []
    for mod in modules:
        lectures = []
        for lec in mod.get("lectures") or []:
            lectures.append(
                {
                    **lec,
                    "content": enrich_lecture_html(lec.get("content") or ""),
                }
            )
        out.append({**mod, "lectures": lectures})
    return out


ACADEMIC_MODULE = {
    "order": 16,
    "title": "Akademik ingliz tili (Academic English for IT)",
    "slug": "eit-academic",
    "description": "CS/IT talabalari uchun: abstract, paper o‘qish, iqtibos, hisobot va taqdimot.",
    "lectures": [
        _lec(
            "Reading papers and abstracts",
            "eit-academic-abstracts",
            """
<h2>Lesson goal</h2>
<p>At the end of this lesson you can skim a short CS abstract, find the research aim and method,
and explain the main result in clear B1–B2 English.</p>

<h2>Warm-up</h2>
<p>University IT students often read <strong>papers</strong>, <strong>abstracts</strong>, and <strong>survey articles</strong>.
Ask yourself: What problem does the paper study? What method do the authors use? What do they claim?</p>

<h2>Key vocabulary</h2>
<table>
  <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
  <tr><td><strong>abstract</strong></td><td>short summary at the start of a paper</td><td>Read the abstract before the full text.</td></tr>
  <tr><td><strong>hypothesis</strong></td><td>idea you test with evidence</td><td>Our hypothesis is that caching reduces latency.</td></tr>
  <tr><td><strong>methodology</strong></td><td>how the study was done</td><td>The methodology section describes the experiment.</td></tr>
  <tr><td><strong>dataset</strong></td><td>collection of data for analysis</td><td>They trained the model on a public dataset.</td></tr>
  <tr><td><strong>findings / results</strong></td><td>what the study discovered</td><td>The findings show a 12% improvement.</td></tr>
  <tr><td><strong>limitation</strong></td><td>weak point of the study</td><td>A limitation is the small sample size.</td></tr>
  <tr><td><strong>cite / citation</strong></td><td>give credit to another source</td><td>Always cite the original paper.</td></tr>
  <tr><td><strong>peer-reviewed</strong></td><td>checked by other experts before publishing</td><td>Prefer peer-reviewed journals.</td></tr>
</table>

<h2>Useful phrases (memorise)</h2>
<ul>
  <li>This paper investigates / proposes / evaluates…</li>
  <li>The authors argue that…</li>
  <li>According to the abstract, the main contribution is…</li>
  <li>The study is based on experiments / a survey / a case study.</li>
  <li>Further research is needed to…</li>
</ul>

<h2>Dialogue — study group</h2>
<p><strong>Student A:</strong> Did you understand the abstract?<br>
<strong>Student B:</strong> Mostly. They propose a new caching algorithm for mobile apps.<br>
<strong>Student A:</strong> What was their method?<br>
<strong>Student B:</strong> They compared three algorithms on the same dataset.<br>
<strong>Student A:</strong> And the result?<br>
<strong>Student B:</strong> Latency dropped by about twelve percent, but the sample was small.</p>

<h2>Grammar focus — Reporting verbs (academic)</h2>
<p>Use reporting verbs to summarise other writers:</p>
<ul>
  <li>Smith <strong>states</strong> that… / Lee <strong>suggests</strong> that…</li>
  <li>The authors <strong>claim</strong> / <strong>demonstrate</strong> / <strong>conclude</strong> that…</li>
  <li>Present simple is common for published facts: <em>The paper shows…</em></li>
</ul>

<h2>Common mistakes</h2>
<ul>
  <li>❌ This paper is about about AI. → ✅ This paper is about AI. / This paper investigates AI.</li>
  <li>❌ Authors say good result. → ✅ The authors report strong results.</li>
  <li>❌ I copy sentence from paper. → ✅ I paraphrase and cite the source.</li>
</ul>

<h2>Reading — Sample abstract (adapted style)</h2>
<p><em>Mobile apps often feel slow when users open them on weak networks. This paper proposes a lightweight caching strategy for API responses. We evaluated the method on three open datasets and compared it with two baseline algorithms. Results show an average latency reduction of 12%. A limitation is that we tested only Android devices. Future work will include iOS benchmarks.</em></p>
<p><strong>Check:</strong> What problem? What method? What result? What limitation?</p>

<h2>Speaking practice</h2>
<ol>
  <li>Explain what an abstract is (2 sentences).</li>
  <li>Summarise the sample abstract without looking (4–5 sentences).</li>
  <li>Ask a partner three academic questions about any IT topic.</li>
</ol>

<h2>Academic / study tip</h2>
<p>First read title → abstract → conclusion → figures. Then decide if the full paper is worth your time.</p>

<h2>Quick review</h2>
<ul>
  <li>Abstract = short summary of aim, method, results.</li>
  <li>Use reporting verbs: state, suggest, conclude.</li>
  <li>Always paraphrase + cite; never submit copied text.</li>
</ul>
""",
        ),
        _lec(
            "Writing reports and citing sources",
            "eit-academic-writing",
            """
<h2>Lesson goal</h2>
<p>You can structure a short technical/academic report, paraphrase safely, and write a simple reference list in English.</p>

<h2>Warm-up</h2>
<p>In university projects you write <strong>lab reports</strong>, <strong>coursework</strong>, and sometimes a <strong>bachelor thesis</strong>.
Clear structure helps teachers and future employers trust your work.</p>

<h2>Key vocabulary</h2>
<table>
  <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
  <tr><td><strong>introduction</strong></td><td>opening that states the topic and aim</td><td>The introduction explains the problem.</td></tr>
  <tr><td><strong>literature review</strong></td><td>summary of previous research</td><td>Our literature review covers five papers.</td></tr>
  <tr><td><strong>paraphrase</strong></td><td>rewrite an idea in new words</td><td>Paraphrase the definition; do not copy it.</td></tr>
  <tr><td><strong>plagiarism</strong></td><td>using someone’s work without credit</td><td>Plagiarism can fail your course.</td></tr>
  <tr><td><strong>reference / bibliography</strong></td><td>list of sources</td><td>Add references at the end.</td></tr>
  <tr><td><strong>figure / table</strong></td><td>visual data in a report</td><td>Figure 2 shows the CPU usage.</td></tr>
  <tr><td><strong>appendix</strong></td><td>extra material at the end</td><td>Source code is in the appendix.</td></tr>
  <tr><td><strong>objective tone</strong></td><td>formal, factual style</td><td>Prefer “The results show…” over “I think it’s cool.”</td></tr>
</table>

<h2>Useful phrases (memorise)</h2>
<ul>
  <li>The aim of this report is to…</li>
  <li>This section describes the experimental setup.</li>
  <li>As shown in Figure 1, …</li>
  <li>These results suggest that…</li>
  <li>In conclusion, we recommend…</li>
</ul>

<h2>Dialogue — teacher feedback</h2>
<p><strong>Lecturer:</strong> Your report has good data, but some sentences are copied from a blog.<br>
<strong>Student:</strong> I’m sorry. How should I fix it?<br>
<strong>Lecturer:</strong> Paraphrase the ideas and add citations. Also keep an objective tone.<br>
<strong>Student:</strong> Should I use “I” in the methods section?<br>
<strong>Lecturer:</strong> In many CS reports, “We implemented…” or passive voice is acceptable. Follow your department guide.</p>

<h2>Grammar focus — Passive voice (methods)</h2>
<p>Academic methods often use passive:</p>
<ul>
  <li>The model <strong>was trained</strong> on 10,000 samples.</li>
  <li>Latency <strong>was measured</strong> in milliseconds.</li>
  <li>Active is also fine: <em>We trained the model…</em> — be consistent.</li>
</ul>

<h2>Common mistakes</h2>
<ul>
  <li>❌ Copy-paste from Wikipedia. → ✅ Paraphrase and cite a reliable source.</li>
  <li>❌ In this report I will talk about cool stuff. → ✅ This report evaluates two sorting algorithms.</li>
  <li>❌ According to internet… → ✅ According to Tanenbaum (2014), …</li>
</ul>

<h2>Reading — Mini report outline</h2>
<p><strong>Title:</strong> Comparing two sorting algorithms for small datasets<br>
<strong>1 Introduction</strong> — problem and aim<br>
<strong>2 Background</strong> — short literature notes<br>
<strong>3 Method</strong> — datasets, metrics, environment<br>
<strong>4 Results</strong> — tables/figures<br>
<strong>5 Discussion</strong> — what the numbers mean + limitations<br>
<strong>6 Conclusion</strong> — recommendation<br>
<strong>References</strong></p>
<p><strong>Check:</strong> Where do limitations go? Why are references required?</p>

<h2>Speaking practice</h2>
<ol>
  <li>Explain plagiarism in simple English (3 sentences).</li>
  <li>Describe your last university/project report structure.</li>
  <li>Practise: “As shown in Figure 1…” with an imaginary chart.</li>
</ol>

<h2>Academic / study tip</h2>
<p>Write the methods and results first; write the introduction last. It becomes clearer after you know your findings.</p>

<h2>Quick review</h2>
<ul>
  <li>Report = clear sections + evidence + references.</li>
  <li>Paraphrase + cite = academic honesty.</li>
  <li>Passive/“we” for methods; objective tone overall.</li>
</ul>
""",
        ),
        _lec(
            "Presentations and seminar English",
            "eit-academic-presentations",
            """
<h2>Lesson goal</h2>
<p>You can open and structure a short academic IT presentation, handle questions politely, and use clear signposting language.</p>

<h2>Warm-up</h2>
<p>At university you give <strong>seminar talks</strong>, <strong>project demos</strong>, and sometimes <strong>conference posters</strong>.
Good slides are short; your spoken English carries the explanation.</p>

<h2>Key vocabulary</h2>
<table>
  <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
  <tr><td><strong>agenda / outline</strong></td><td>plan of the talk</td><td>First, here is today’s outline.</td></tr>
  <tr><td><strong>signposting</strong></td><td>language that guides listeners</td><td>“Next, I’ll explain the method.”</td></tr>
  <tr><td><strong>slide deck</strong></td><td>set of presentation slides</td><td>Please share the slide deck after class.</td></tr>
  <tr><td><strong>demo</strong></td><td>live show of software</td><td>I’ll give a two-minute demo.</td></tr>
  <tr><td><strong>Q&amp;A</strong></td><td>questions and answers</td><td>We’ll leave five minutes for Q&amp;A.</td></tr>
  <tr><td><strong>handout</strong></td><td>paper/PDF for the audience</td><td>The handout summarises the formulas.</td></tr>
  <tr><td><strong>poster session</strong></td><td>event where you explain a poster</td><td>Our poster session starts at 3 p.m.</td></tr>
  <tr><td><strong>clarify</strong></td><td>make something clearer</td><td>Let me clarify that point.</td></tr>
</table>

<h2>Useful phrases (memorise)</h2>
<ul>
  <li>Good morning. Today I’ll present our project on…</li>
  <li>I’ll start with the problem, then the method, and finally the results.</li>
  <li>As you can see on this slide…</li>
  <li>That’s a great question. In short…</li>
  <li>Thank you for your attention. I’m happy to take questions.</li>
</ul>

<h2>Dialogue — after a seminar talk</h2>
<p><strong>Student:</strong> Thank you for your attention. Any questions?<br>
<strong>Peer:</strong> Why did you choose Redis for caching?<br>
<strong>Student:</strong> Good question. We needed low latency for session data, and Redis fitted our stack.<br>
<strong>Peer:</strong> Did you compare it with Memcached?<br>
<strong>Student:</strong> Not in this sprint. That’s a limitation. We plan to benchmark both next month.</p>

<h2>Grammar focus — Future forms for plans</h2>
<ul>
  <li><strong>will</strong> for decisions/offers now: <em>I’ll answer that after the demo.</em></li>
  <li><strong>going to</strong> for planned steps: <em>We’re going to show the architecture next.</em></li>
  <li><strong>Present continuous</strong> for fixed schedule: <em>We’re presenting on Friday at 10.</em></li>
</ul>

<h2>Common mistakes</h2>
<ul>
  <li>❌ I will to present… → ✅ I will present… / I’m going to present…</li>
  <li>❌ Read every word on the slide. → ✅ Speak; keep slides short.</li>
  <li>❌ Any question? (abrupt) → ✅ Are there any questions?</li>
</ul>

<h2>Reading — 5-minute talk structure</h2>
<p>1) Hook + aim (30 sec) 2) Problem (1 min) 3) Approach (1.5 min) 4) Result/demo (1.5 min)
5) Limitations + next steps (30 sec) 6) Q&amp;A. Practise with a timer. Mark signposting phrases in your script.</p>
<p><strong>Check:</strong> Where do you put limitations? Why is Q&amp;A important?</p>

<h2>Speaking practice</h2>
<ol>
  <li>Give a 60-second intro to any IT project.</li>
  <li>Answer: “Why did you choose this technology?”</li>
  <li>Practise closing + inviting questions.</li>
</ol>

<h2>Academic / study tip</h2>
<p>Record yourself once. Check: Do you say filler words too often? Are numbers clear? Is the last slide a summary, not new ideas?</p>

<h2>Quick review</h2>
<ul>
  <li>Signpost: first / next / finally / as you can see.</li>
  <li>Welcome hard questions; admit limitations honestly.</li>
  <li>Short slides + clear speech &gt; walls of text.</li>
</ul>
""",
        ),
    ],
    "practice": {
        "eit-academic-abstracts": _quiz(
            "eit-q-abstract",
            "Abstract",
            "Academic reading.",
            "An abstract is mainly…",
            [
                "A) a short summary of a paper’s aim, method, and results",
                "B) a list of passwords",
                "C) a hardware cable",
                "D) a Scrum snack",
            ],
            "A",
            editorial="Abstract = paper summary.",
        ),
        "eit-academic-writing": _quiz(
            "eit-q-plagiarism",
            "Plagiarism",
            "Academic writing.",
            "Plagiarism means…",
            [
                "A) using someone’s work without proper credit",
                "B) formatting a slide deck",
                "C) renaming a variable",
                "D) closing a ticket",
            ],
            "A",
            editorial="Always paraphrase and cite.",
        ),
        "eit-academic-presentations": _quiz(
            "eit-q-signpost",
            "Signposting",
            "Presentations.",
            "Best signposting phrase:",
            [
                "A) Next, I’ll explain the method.",
                "B) Stuff now.",
                "C) Password!",
                "D) You again?",
            ],
            "A",
            editorial="Guide the audience clearly.",
        ),
    },
    "exercises": [
        _quiz(
            "eit-m16-cite",
            "Citation",
            "Academic honesty.",
            "To cite a source means…",
            [
                "A) give credit to the original author",
                "B) delete the reference list",
                "C) hide the dataset",
                "D) skip the abstract",
            ],
            "A",
        ),
        _quiz(
            "eit-m16-passive",
            "Methods grammar",
            "Report writing.",
            "Best methods sentence:",
            [
                "A) The model was trained on 10,000 samples.",
                "B) Model training we yesterday cool.",
                "C) Train model is very very.",
                "D) The model training forever password.",
            ],
            "A",
            difficulty="medium",
        ),
    ],
    "homework": _hw(
        "English for IT — Module 16 (Academic) homework\n"
        "1) Find any short IT abstract online (or use the lesson sample). Write a 6-sentence paraphrase.\n"
        "2) Outline a mini report (title + 6 section headings) for a project you know.\n"
        "3) Prepare a 90-second presentation script with signposting phrases.\n"
        "4) Glossary: abstract, hypothesis, paraphrase, plagiarism, citation, signposting, Q&A, limitation."
    ),
}
