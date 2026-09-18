"""
English for IT — interview preparation module (order 17).
"""

from __future__ import annotations

from apps.core.english_it_content import _hw, _lec, _quiz

INTERVIEW_MODULE = {
    "order": 17,
    "title": "IT intervyu (Interview prep)",
    "slug": "eit-interview",
    "description": "IT suhbatiga tayyorgarlik: STAR, texnik savollar, salary va follow-up.",
    "lectures": [
        _lec(
            "Behavioral interview (STAR)",
            "eit-interview-star",
            """
<h2>Lesson goal</h2>
<p>You can answer behavioural interview questions with a clear STAR story (Situation, Task, Action, Result) in confident B1–B2 English.</p>

<h2>Warm-up</h2>
<p>Interviewers often ask: <em>Tell me about a time you…</em> They want structure, not a 10-minute novel.</p>

<h2>Key vocabulary</h2>
<table>
  <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
  <tr><td><strong>STAR</strong></td><td>Situation, Task, Action, Result</td><td>I answered with a STAR story.</td></tr>
  <tr><td><strong>behavioural question</strong></td><td>about past behaviour at work</td><td>Describe a conflict with a teammate.</td></tr>
  <tr><td><strong>strength / weakness</strong></td><td>what you do well / need to improve</td><td>One strength is clear communication.</td></tr>
  <tr><td><strong>ownership</strong></td><td>taking responsibility</td><td>I took ownership of the incident.</td></tr>
  <tr><td><strong>trade-off</strong></td><td>choosing between options</td><td>We discussed the performance trade-off.</td></tr>
  <tr><td><strong>follow-up</strong></td><td>message after the interview</td><td>I’ll send a short follow-up email.</td></tr>
  <tr><td><strong>culture fit</strong></td><td>match with team values</td><td>They asked about culture fit.</td></tr>
  <tr><td><strong>timeline</strong></td><td>when you can start</td><td>My timeline is two weeks’ notice.</td></tr>
</table>

<h2>Useful phrases (memorise)</h2>
<ul>
  <li>In my previous role at… / On my last project…</li>
  <li>My task was to… / I was responsible for…</li>
  <li>I decided to… / I coordinated with…</li>
  <li>As a result, we reduced… / we shipped on time.</li>
  <li>What I learned is…</li>
</ul>

<h2>Dialogue — interview snippet</h2>
<p><strong>Interviewer:</strong> Tell me about a time you fixed a production bug under pressure.<br>
<strong>Candidate:</strong> Situation: our checkout API started timing out on Friday evening.<br>
<strong>Candidate:</strong> Task: I needed to restore payments quickly and keep the team informed.<br>
<strong>Candidate:</strong> Action: I checked logs, rolled back the last deploy, and added a monitor.<br>
<strong>Candidate:</strong> Result: payments recovered in 25 minutes, and we wrote a short post-mortem.</p>

<h2>Grammar focus — Past simple for stories</h2>
<ul>
  <li>I <strong>joined</strong> the war room. We <strong>found</strong> the root cause.</li>
  <li>Present perfect for experience: <em>I have worked with Python for three years.</em></li>
</ul>

<h2>Common mistakes</h2>
<ul>
  <li>❌ I am hardworking always. → ✅ Here’s an example that shows my ownership…</li>
  <li>❌ Blame only teammates. → ✅ Focus on your actions and learning.</li>
  <li>❌ Speak for 8 minutes. → ✅ Keep STAR to about 90–120 seconds.</li>
</ul>

<h2>Reading — Top behavioural prompts</h2>
<p>Prepare 4–5 stories: conflict, deadline, mistake, leadership/initiative, learning something new.
Reuse the same stories for similar questions. Quantify results when possible (time, %, money, incidents).</p>

<h2>Speaking practice</h2>
<ol>
  <li>Answer “Tell me about yourself” in 60 seconds.</li>
  <li>STAR: a difficult bug or ticket.</li>
  <li>STAR: disagreement in a code review.</li>
</ol>

<h2>Academic / study tip</h2>
<p>Write STAR bullets on one page. Practise aloud with a timer. Record yourself once.</p>

<h2>Quick review</h2>
<ul>
  <li>STAR = Situation → Task → Action → Result (+ lesson).</li>
  <li>Past simple for the story; present perfect for experience.</li>
  <li>Own the action; measure the result.</li>
</ul>
""",
        ),
        _lec(
            "Technical interview English",
            "eit-interview-tech",
            """
<h2>Lesson goal</h2>
<p>You can explain systems, trade-offs, and debugging steps in clear interview English — even if you think in another language first.</p>

<h2>Warm-up</h2>
<p>Technical interviews test communication as much as knowledge. Say what you know, what you’d check next, and what you’re unsure about.</p>

<h2>Key vocabulary</h2>
<table>
  <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
  <tr><td><strong>clarify the requirements</strong></td><td>ask what exactly is needed</td><td>I’d like to clarify the requirements first.</td></tr>
  <tr><td><strong>edge case</strong></td><td>unusual input/situation</td><td>Null input is an edge case.</td></tr>
  <tr><td><strong>complexity</strong></td><td>time/space cost of an algorithm</td><td>This is O(n log n) time complexity.</td></tr>
  <tr><td><strong>bottleneck</strong></td><td>slowest part of a system</td><td>The database was the bottleneck.</td></tr>
  <tr><td><strong>scalability</strong></td><td>ability to grow with load</td><td>We designed for horizontal scalability.</td></tr>
  <tr><td><strong>idempotent</strong></td><td>safe to retry without side effects</td><td>The payment endpoint should be idempotent.</td></tr>
  <tr><td><strong>root cause</strong></td><td>the real underlying problem</td><td>The root cause was a missing index.</td></tr>
  <tr><td><strong>whiteboard</strong></td><td>draw/solve on a board</td><td>Let’s whiteboard the data model.</td></tr>
</table>

<h2>Useful phrases (memorise)</h2>
<ul>
  <li>Let me restate the problem to make sure I understand…</li>
  <li>One approach is… An alternative would be…</li>
  <li>The trade-off is simplicity versus performance.</li>
  <li>I’d start by reproducing the issue / checking the logs / writing a failing test.</li>
  <li>I’m not sure — I’d look it up / ask a senior / check the docs.</li>
</ul>

<h2>Dialogue — system design lite</h2>
<p><strong>Interviewer:</strong> How would you design a URL shortener?<br>
<strong>Candidate:</strong> First, I’ll clarify: expected QPS, custom aliases, and analytics needs?<br>
<strong>Interviewer:</strong> Assume medium traffic and unique short codes.<br>
<strong>Candidate:</strong> I’d use an API service, a key generator, and a datastore mapping code → URL, plus caching for hot links.</p>

<h2>Grammar focus — Conditionals for design</h2>
<ul>
  <li>If traffic <strong>grows</strong>, we <strong>can</strong> add read replicas.</li>
  <li>If I <strong>had</strong> more time, I <strong>would</strong> add rate limiting.</li>
</ul>

<h2>Common mistakes</h2>
<ul>
  <li>❌ Silent coding for 10 minutes. → ✅ Think aloud in short sentences.</li>
  <li>❌ Fake certainty. → ✅ Say assumptions and ask clarifying questions.</li>
  <li>❌ Only buzzwords. → ✅ Explain why a choice fits the problem.</li>
</ul>

<h2>Reading — Explain your stack</h2>
<p>Prepare a 90-second talk: languages, frameworks, databases, cloud, testing, and one proud project.
Mention ownership: “I built / maintained / improved…”</p>

<h2>Speaking practice</h2>
<ol>
  <li>Explain a project architecture in 90 seconds.</li>
  <li>Describe how you debug a 500 error.</li>
  <li>Compare SQL vs NoSQL for a simple use case.</li>
</ol>

<h2>Academic / study tip</h2>
<p>Keep a personal glossary: 30 phrases for algorithms, networking, databases, and DevOps. Review before interviews.</p>

<h2>Quick review</h2>
<ul>
  <li>Clarify → propose → discuss trade-offs → next steps.</li>
  <li>Think aloud; label assumptions.</li>
  <li>Honest “I’d verify…” beats fake expertise.</li>
</ul>
""",
        ),
        _lec(
            "Salary, offer, and follow-up",
            "eit-interview-offer",
            """
<h2>Lesson goal</h2>
<p>You can discuss salary range politely, ask smart process questions, and write a short thank-you / follow-up email after an interview.</p>

<h2>Warm-up</h2>
<p>Money talks are sensitive. Be prepared, be calm, and avoid inventing numbers you can’t defend.</p>

<h2>Key vocabulary</h2>
<table>
  <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
  <tr><td><strong>compensation / package</strong></td><td>salary + benefits</td><td>What’s the total compensation package?</td></tr>
  <tr><td><strong>base salary</strong></td><td>fixed pay</td><td>The base salary is competitive.</td></tr>
  <tr><td><strong>bonus / equity</strong></td><td>extra pay / company shares</td><td>Is there a bonus or equity?</td></tr>
  <tr><td><strong>notice period</strong></td><td>time before leaving current job</td><td>My notice period is two weeks.</td></tr>
  <tr><td><strong>offer letter</strong></td><td>written job offer</td><td>Please send the offer letter by email.</td></tr>
  <tr><td><strong>negotiate</strong></td><td>discuss better terms</td><td>I’d like to negotiate the start date.</td></tr>
  <tr><td><strong>counter-offer</strong></td><td>your alternative proposal</td><td>Here’s my polite counter-offer.</td></tr>
  <tr><td><strong>thank-you note</strong></td><td>short message after interview</td><td>I sent a thank-you note the same day.</td></tr>
</table>

<h2>Useful phrases (memorise)</h2>
<ul>
  <li>I’m targeting a range of … depending on responsibilities and total package.</li>
  <li>Could you share the budget range for this role?</li>
  <li>I’m flexible on start date if we align on the offer.</li>
  <li>Thank you for your time today. I enjoyed learning about the team.</li>
  <li>Please let me know the next steps and timeline.</li>
</ul>

<h2>Dialogue — salary question</h2>
<p><strong>Interviewer:</strong> What are your salary expectations?<br>
<strong>Candidate:</strong> Based on the role and market, I’m targeting X–Y total package. I’m open to discuss if the responsibilities are a strong match.<br>
<strong>Interviewer:</strong> We usually start near the middle of that range.<br>
<strong>Candidate:</strong> That sounds promising. Could you also share bonus, benefits, and the interview timeline?</p>

<h2>Grammar focus — Polite softener</h2>
<ul>
  <li><strong>I’d like to</strong> understand the full package.</li>
  <li><strong>Would it be possible to</strong> share the next steps?</li>
  <li><strong>I’m flexible on</strong> remote days / start date.</li>
</ul>

<h2>Common mistakes</h2>
<ul>
  <li>❌ First question: How much money? → ✅ Learn the role, then discuss compensation.</li>
  <li>❌ Accept instantly without reading. → ✅ Ask for the offer letter and review it.</li>
  <li>❌ No follow-up. → ✅ Send a short thank-you within 24 hours.</li>
</ul>

<h2>Reading — Follow-up email template</h2>
<p>Subject: Thank you — Backend Engineer interview<br>
Dear …,<br>
Thank you for speaking with me today about the … role. I enjoyed our discussion about … and I’m excited about the chance to contribute to …<br>
Please let me know if you need any extra information. I look forward to the next steps.<br>
Best regards,<br>Name</p>

<h2>Speaking practice</h2>
<ol>
  <li>Answer salary expectations in 3 sentences.</li>
  <li>Ask 3 smart questions about the team/process.</li>
  <li>Read your follow-up email aloud.</li>
</ol>

<h2>Academic / study tip</h2>
<p>Write your range on paper before the call. Practise saying it without laughing or apologising.</p>

<h2>Quick review</h2>
<ul>
  <li>Range + flexibility + total package questions.</li>
  <li>Soft language: I’d like to / Would it be possible…</li>
  <li>Thank-you note within 24 hours.</li>
</ul>
""",
        ),
    ],
    "practice": {
        "eit-interview-star": _quiz(
            "eit-q-star",
            "STAR",
            "Interview.",
            "STAR stands for…",
            [
                "A) Situation, Task, Action, Result",
                "B) Server, Token, API, Router",
                "C) Soft, Tall, Angry, Random",
                "D) SQL, Test, Alert, Rollback",
            ],
            "A",
            editorial="STAR = story structure.",
        ),
        "eit-interview-tech": _quiz(
            "eit-q-clarify",
            "Clarify",
            "Tech interview.",
            "Best first step in a tech interview problem:",
            [
                "A) clarify the requirements / restate the problem",
                "B) insult the interviewer",
                "C) stay silent for 20 minutes",
                "D) guess randomly without thinking",
            ],
            "A",
            editorial="Clarify before coding.",
        ),
        "eit-interview-offer": _quiz(
            "eit-q-followup",
            "Follow-up",
            "After interview.",
            "A thank-you note should usually be sent…",
            [
                "A) within about 24 hours",
                "B) never",
                "C) after one year",
                "D) only by fax in 1990",
            ],
            "A",
            editorial="Follow up the same day if possible.",
        ),
    },
    "exercises": [
        _quiz(
            "eit-m17-ownership",
            "Ownership",
            "Behavioural.",
            "Best interview habit:",
            [
                "A) describe your actions and measurable results",
                "B) only blame others",
                "C) refuse all examples",
                "D) read the phone the whole time",
            ],
            "A",
        ),
        _quiz(
            "eit-m17-tradeoff",
            "Trade-off",
            "Tech talk.",
            "A trade-off means…",
            [
                "A) choosing between options with different pros/cons",
                "B) a type of keyboard",
                "C) a free lunch",
                "D) deleting production for fun",
            ],
            "A",
            difficulty="medium",
        ),
    ],
    "homework": _hw(
        "English for IT — Module 17 (Interview) homework\n"
        "1) Write 5 STAR stories (bug, conflict, deadline, learning, leadership).\n"
        "2) Prepare a 90-second project pitch + architecture overview.\n"
        "3) Write salary range script + thank-you email.\n"
        "4) Glossary: STAR, trade-off, bottleneck, edge case, notice period, offer letter."
    ),
}
