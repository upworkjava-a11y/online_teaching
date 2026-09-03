"""
English for Banking — pre-intermediate (A2–B1) track.

Learning English stays in English (vocabulary, dialogues, reading).
UI instructions use Uzbek so |loc can translate the “second side”.
Banking terms follow standard international English usage.
"""

COURSE_DESCRIPTION = (
    "Bank sohasi uchun pre-intermediate ingliz tili (11 modul): asoslar, hisoblar, kartalar, "
    "kredit, FX/remittance, SME/trade finance, raqamli banking va firibgarlik, HR, mijoz xizmati, "
    "KYC/compliance, email va uchrashuvlar. Grammatika, so‘z boyligi, o‘qish va gapirish — "
    "puzzle va bilim testlari bilan."
)


def _lec(title, slug, html, examples=None):
    return {"title": title, "slug": slug, "content": html.strip(), "sql_examples": examples or []}


def _quiz(slug, title, description, task, options, answer, hints=None, difficulty="easy", editorial=""):
    return {
        "slug": slug,
        "title": title,
        "description": description.strip(),
        "task": task,
        "hints": hints or ["Darsdagi inglizcha so‘zlarni eslang.", "Noto‘g‘ri variantlarni chiqarib tashlang."],
        "editorial": editorial or "To‘g‘ri javob darsdagi bank terminiga mos keladi.",
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
        "title": "Bank asoslari (Bank basics)",
        "slug": "eb-bank-basics",
        "description": "Bankda ishlash, rollar, salomlashish va asosiy so‘zlar.",
        "lectures": [
            _lec(
                "Welcome to the bank",
                "eb-welcome",
                """
<h2>Lesson goal</h2>
<p>At the end of this lesson you can greet a customer, name main bank roles, and describe a simple branch routine in English (pre-intermediate / A2–B1).</p>

<h2>Warm-up</h2>
<p>Think in English: Where do people go to open an account, get cash, or ask about a loan? — to a <strong>bank branch</strong> or through the <strong>mobile app</strong>.</p>

<h2>Key vocabulary</h2>
<table>
  <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
  <tr><td><strong>branch</strong></td><td>a local bank office</td><td>Our branch is on Navoi Street.</td></tr>
  <tr><td><strong>head office</strong></td><td>main central office</td><td>Head office sets the rules.</td></tr>
  <tr><td><strong>teller / cashier</strong></td><td>serves customers at the counter</td><td>The teller counts the cash.</td></tr>
  <tr><td><strong>customer / client</strong></td><td>person who uses bank services</td><td>Every customer needs an ID.</td></tr>
  <tr><td><strong>manager</strong></td><td>leads a team or branch</td><td>I’ll call the manager.</td></tr>
  <tr><td><strong>ATM</strong></td><td>cash machine</td><td>There is an ATM outside.</td></tr>
  <tr><td><strong>counter / desk</strong></td><td>place where staff serve clients</td><td>Please come to desk number 3.</td></tr>
  <tr><td><strong>queue / line</strong></td><td>people waiting</td><td>There is a long queue today.</td></tr>
</table>

<h2>Useful phrases (memorise)</h2>
<ul>
  <li>Good morning. Welcome to Orient Bank. How can I help you?</li>
  <li>I’d like to open an account, please.</li>
  <li>Certainly. One moment, please.</li>
  <li>I’m afraid the manager is in a meeting. Can you wait five minutes?</li>
  <li>Thank you for coming in today.</li>
</ul>

<h2>Dialogue A — at the entrance</h2>
<p><strong>Security:</strong> Good morning. How can I help you?<br>
<strong>Customer:</strong> Good morning. I’d like to speak to someone about a new account.<br>
<strong>Security:</strong> Please take a ticket and wait in the retail banking queue.<br>
<strong>Customer:</strong> Thank you.</p>

<h2>Dialogue B — at the counter</h2>
<p><strong>Teller:</strong> Next, please. How can I help you?<br>
<strong>Customer:</strong> I’d like to open a savings account.<br>
<strong>Teller:</strong> Of course. May I see your passport?<br>
<strong>Customer:</strong> Here you are.<br>
<strong>Teller:</strong> Thank you. Please take a seat. I’ll prepare the forms.</p>

<h2>Grammar focus — Present simple (routines)</h2>
<p>Use present simple for bank opening hours and daily work:</p>
<ul>
  <li>We <strong>open</strong> at 9 a.m. and <strong>close</strong> at 6 p.m.</li>
  <li>The branch <strong>doesn’t open</strong> on Sundays.</li>
  <li>She <strong>works</strong> as a teller. He <strong>helps</strong> customers every day.</li>
</ul>
<p><strong>Question forms:</strong> <em>What time do you open? Does this branch have an ATM?</em></p>

<h2>Common mistakes</h2>
<ul>
  <li>❌ I want account. → ✅ I’d like to open an account.</li>
  <li>❌ Give me manager! → ✅ Could I speak to the manager, please?</li>
  <li>❌ Client is angry always shout. → ✅ If a customer is unhappy, stay calm and polite.</li>
</ul>

<h2>Reading — A day at the branch</h2>
<p>Aziza is a teller at a busy city branch. The bank opens at nine. First, she checks her cash drawer. Then she serves customers: deposits, withdrawals, and simple questions about cards. At lunchtime the queue is long, so she works quickly but carefully. In the afternoon a client asks for a loan. Aziza cannot decide alone, so she calls the credit department. At six o’clock the branch closes. Aziza counts the cash again and writes a short report for the manager.</p>
<p><strong>Check:</strong> What does Aziza do first? Why does she call another department?</p>

<h2>Speaking practice</h2>
<ol>
  <li>Greet a customer and offer help (2 sentences).</li>
  <li>Explain your branch opening hours (3 sentences).</li>
  <li>Role-play Dialogue B with a partner. Switch roles.</li>
</ol>

<h2>Quick review</h2>
<p>branch · teller · customer · manager · ATM · How can I help you? · I’d like to…</p>
""",
            ),
            _lec(
                "Departments in a bank",
                "eb-departments",
                """
<h2>Lesson goal</h2>
<p>Name the main bank departments and say what each one does in clear, simple English.</p>

<h2>Big picture</h2>
<p>A bank is like a company with many teams. Retail staff meet people. Credit staff study loans. Compliance checks rules. HR finds people for jobs. Operations moves money every day.</p>

<h2>Key vocabulary</h2>
<table>
  <tr><th>Department</th><th>What they do</th></tr>
  <tr><td><strong>Retail banking</strong></td><td>products for individuals (accounts, cards, small loans)</td></tr>
  <tr><td><strong>Corporate banking</strong></td><td>services for companies and businesses</td></tr>
  <tr><td><strong>Credit / Lending</strong></td><td>reviews and decides on loans</td></tr>
  <tr><td><strong>HR (Human Resources)</strong></td><td>hiring, contracts, training, staff support</td></tr>
  <tr><td><strong>Compliance</strong></td><td>follows laws and internal bank rules</td></tr>
  <tr><td><strong>Operations / Back office</strong></td><td>processes payments and account changes</td></tr>
  <tr><td><strong>Risk</strong></td><td>identifies and controls financial risks</td></tr>
  <tr><td><strong>IT / Digital</strong></td><td>apps, systems, online banking</td></tr>
  <tr><td><strong>Call centre / Contact centre</strong></td><td>helps clients by phone or chat</td></tr>
</table>

<h2>Collocations (word partners)</h2>
<ul>
  <li>work <strong>in</strong> HR / Credit / Compliance</li>
  <li>process a payment · review a file · approve a loan · interview a candidate</li>
  <li>retail clients · corporate clients · high-risk transactions</li>
</ul>

<h2>Example sentences</h2>
<ul>
  <li>HR interviews new candidates and organises training.</li>
  <li>The credit department checks the client’s income and documents.</li>
  <li>Compliance reviews unusual or high-risk transactions.</li>
  <li>Operations processes salary transfers every morning.</li>
  <li>Corporate banking serves factories, shops, and large companies.</li>
</ul>

<h2>Dialogue — Who should I ask?</h2>
<p><strong>Intern:</strong> A company wants a large business loan. Who should I call?<br>
<strong>Mentor:</strong> That’s corporate banking and credit. Send the file to the credit analyst.<br>
<strong>Intern:</strong> And if the client’s passport looks strange?<br>
<strong>Mentor:</strong> Stop and escalate to Compliance. Don’t open the account yet.<br>
<strong>Intern:</strong> Understood. Thanks!</p>

<h2>Grammar focus — Present simple + 3rd person -s</h2>
<ul>
  <li>She <strong>works</strong> in HR. He <strong>checks</strong> documents.</li>
  <li>It <strong>processes</strong> payments. The team <strong>reviews</strong> files.</li>
  <li>Negative: He <strong>doesn’t approve</strong> every loan.</li>
  <li>Question: <em>Where does she work? Does Compliance check every transfer?</em></li>
</ul>

<h2>Reading — Meet the teams</h2>
<p>Orient Bank has several departments under one roof. On the ground floor, retail bankers open accounts and sell cards. Upstairs, credit analysts read salary statements and decide if a loan is safe. In another room, compliance officers study KYC documents. HR posts job ads and plans interviews. At the end of the day, operations confirms that salaries and transfers went through without errors. When teams communicate clearly, customers get faster and safer service.</p>

<h2>Speaking &amp; writing</h2>
<ol>
  <li>Say what three departments do (one sentence each).</li>
  <li>Introduce yourself: “I work in … I … every day.”</li>
  <li>Write 5 sentences: <em>The credit department …</em></li>
</ol>

<h2>Quick review</h2>
<p>retail · corporate · credit · HR · compliance · operations · risk · escalate</p>
""",
            ),
            _lec(
                "Polite customer talk",
                "eb-polite-talk",
                """
<h2>Lesson goal</h2>
<p>Ask for documents, offer choices, and say “no” politely without sounding rude.</p>

<h2>Why politeness matters</h2>
<p>In banking, tone is part of the product. Soft language builds trust. Hard orders create conflict — even when the rule is correct.</p>

<h2>Softening toolkit</h2>
<table>
  <tr><th>Direct (too hard)</th><th>Polite (better)</th></tr>
  <tr><td>Give ID!</td><td>Could you show me your ID, please?</td></tr>
  <tr><td>Wait!</td><td>Could you wait a moment, please?</td></tr>
  <tr><td>You can’t.</td><td>I’m afraid we can’t do that today.</td></tr>
  <tr><td>Wrong number!</td><td>I think there may be a mistake in the account number.</td></tr>
  <tr><td>Sit.</td><td>Please take a seat.</td></tr>
</table>

<h2>Key phrases</h2>
<ul>
  <li>Could you show me your ID, please?</li>
  <li>Would you like a debit card or a credit card?</li>
  <li>I’m afraid we need more documents.</li>
  <li>Thank you for waiting.</li>
  <li>I’ll be happy to help you with that.</li>
  <li>Is there anything else I can do for you?</li>
</ul>

<h2>Offers and choices</h2>
<ul>
  <li>Would you like me to print your statement?</li>
  <li>You can come tomorrow, or we can finish online.</li>
  <li>Shall I explain the fees first?</li>
</ul>

<h2>Dialogue — Missing document</h2>
<p><strong>Officer:</strong> Thank you for your application. I’m afraid we still need proof of address.<br>
<strong>Customer:</strong> I don’t have it with me today.<br>
<strong>Officer:</strong> No problem. Could you bring a utility bill or a rental contract tomorrow?<br>
<strong>Customer:</strong> Yes, I can.<br>
<strong>Officer:</strong> Great. I’ll keep your file ready. Thank you for understanding.</p>

<h2>Grammar focus — Could / Would / I’m afraid</h2>
<ul>
  <li><strong>Could you…?</strong> = polite request</li>
  <li><strong>Would you like…?</strong> = polite offer/choice</li>
  <li><strong>I’m afraid…</strong> = soft bad news</li>
</ul>
<p>Practice: <em>Could you spell your name? Would you like a receipt? I’m afraid the system is slow today.</em></p>

<h2>Reading — Soft skills at the desk</h2>
<p>Javlon serves a customer who wants a large cash withdrawal without booking. The rule says the branch needs notice for big amounts. Javlon does not say “Impossible!” He smiles and explains: “I’m afraid we need one day for this amount. Would you like to book it for tomorrow morning?” The customer agrees. Clear rules + polite language = professional banking.</p>

<h2>Speaking practice</h2>
<ol>
  <li>Ask for a passport politely.</li>
  <li>Explain a short wait (system is busy).</li>
  <li>Refuse an incomplete application softly and offer a next step.</li>
</ol>

<h2>Quick review</h2>
<p>Could you…? · Would you like…? · I’m afraid… · Please take a seat · Thank you for waiting</p>
""",
            ),
        ],
        "practice": {
            "eb-welcome": _quiz(
                "eb-q-branch",
                "So‘z: branch",
                "Bank sohasidagi asosiy so‘z.",
                "What is a branch?",
                [
                    "A) A local bank office",
                    "B) A type of credit card",
                    "C) A loan interest rate",
                    "D) A password",
                ],
                "A",
            ),
            "eb-departments": _quiz(
                "eb-q-hr",
                "So‘z: HR",
                "Bo‘limlar.",
                "What does HR mainly do?",
                [
                    "A) Print money",
                    "B) Hire and support staff",
                    "C) Set the Central Bank rate",
                    "D) Approve every loan alone",
                ],
                "B",
            ),
            "eb-polite-talk": _quiz(
                "eb-q-polite-id",
                "Muloyim so‘rov",
                "Mijoz bilan gaplashish.",
                "Which sentence is polite?",
                [
                    "A) Give me passport now!",
                    "B) Could you show me your ID, please?",
                    "C) You must speak faster.",
                    "D) No documents, go away.",
                ],
                "B",
            ),
        },
        "exercises": [
            _quiz(
                "eb-m1-teller",
                "Rol: teller",
                "Ish o‘rinlari.",
                "A teller usually…",
                [
                    "A) designs the bank building",
                    "B) serves customers at the counter",
                    "C) writes national laws",
                    "D) sets FX rates for the country",
                ],
                "B",
                difficulty="medium",
            ),
            _quiz(
                "eb-m1-speaking-help",
                "Gapirish: yordam",
                "Salomlashish.",
                "Best first line to a customer:",
                [
                    "A) What do you want?",
                    "B) How can I help you?",
                    "C) Are you rich?",
                    "D) Password, quick!",
                ],
                "B",
            ),
        ],
        "homework": _hw(
            "English for Banking — Module 1 homework\n"
            "1) Write 8 sentences about branch routines (present simple).\n"
            "2) Record or rehearse a 45-second greeting + offer of help.\n"
            "3) Make a mini glossary: branch, teller, customer, manager, ATM, queue, retail, compliance — English definition + one example each.\n"
            "4) Rewrite 5 rude sentences into polite bank English."
        ),
    },
    {
        "order": 2,
        "title": "Hisoblar va depozitlar (Accounts)",
        "slug": "eb-accounts",
        "description": "Account types, deposit, withdraw, balance.",
        "lectures": [
            _lec(
                "Types of accounts",
                "eb-account-types",
                """
<h2>Lesson goal</h2>
<p>Compare common account types and help a customer choose in simple English.</p>

<h2>Key vocabulary</h2>
<table>
  <tr><th>Term</th><th>Meaning</th></tr>
  <tr><td><strong>current / checking account</strong></td><td>for everyday payments and card spending</td></tr>
  <tr><td><strong>savings account</strong></td><td>to keep money and earn some interest</td></tr>
  <tr><td><strong>joint account</strong></td><td>shared by two (or more) people</td></tr>
  <tr><td><strong>deposit</strong></td><td>put money into an account</td></tr>
  <tr><td><strong>withdrawal</strong></td><td>take money out</td></tr>
  <tr><td><strong>balance</strong></td><td>money available now</td></tr>
  <tr><td><strong>statement</strong></td><td>list of transactions for a period</td></tr>
  <tr><td><strong>interest</strong></td><td>money earned on savings (or paid on loans)</td></tr>
  <tr><td><strong>minimum balance</strong></td><td>lowest amount the bank may require</td></tr>
</table>

<h2>Compare quickly</h2>
<ul>
  <li><strong>Current account:</strong> easy payments, often little/no interest.</li>
  <li><strong>Savings account:</strong> better for keeping money; may have limits on withdrawals.</li>
  <li>Many people use <em>both</em>: salary to current, extras to savings.</li>
</ul>

<h2>Dialogue — Choosing an account</h2>
<p><strong>Customer:</strong> I’d like to open an account. I’m not sure which type.<br>
<strong>Officer:</strong> Do you need it for daily payments or mainly to save?<br>
<strong>Customer:</strong> Mostly to save, but I also want a card.<br>
<strong>Officer:</strong> Then a savings account plus a debit card can work. Would you like me to explain the interest rate and fees?<br>
<strong>Customer:</strong> Yes, please.</p>

<h2>Grammar — I’d like to / May I…?</h2>
<ul>
  <li>I’d like to open a savings account.</li>
  <li>I’d like to check my balance.</li>
  <li>May I see your ID and proof of address?</li>
</ul>

<h2>Reading — Nilufar’s choice</h2>
<p>Nilufar receives her salary every month. She opens a current account for rent, food, and transport. She also opens a savings account for travel. Each payday she transfers 10% of her salary to savings. After six months she has a useful emergency fund. Her banker says: “Paying yourself first is a simple habit.”</p>
<p><strong>Questions:</strong> Why two accounts? What habit helps her save?</p>

<h2>Speaking</h2>
<ol>
  <li>Explain current vs savings in 4 sentences.</li>
  <li>Help a student choose an account (role-play, 1 minute).</li>
</ol>

<h2>Quick review</h2>
<p>current · savings · joint · balance · statement · interest · I’d like to…</p>
""",
            ),
            _lec(
                "Deposits and withdrawals",
                "eb-deposit-withdraw",
                """
<h2>Lesson goal</h2>
<p>Use the correct verbs for putting money in, taking money out, and moving money between accounts.</p>

<h2>Core verbs</h2>
<table>
  <tr><th>Verb</th><th>Noun</th><th>Example</th></tr>
  <tr><td>deposit</td><td>a deposit</td><td>She deposited 2,000,000 UZS.</td></tr>
  <tr><td>withdraw</td><td>a withdrawal</td><td>He withdrew cash from the ATM.</td></tr>
  <tr><td>transfer</td><td>a transfer</td><td>I transferred money to my sister.</td></tr>
  <tr><td>check</td><td>—</td><td>Please check the balance.</td></tr>
</table>

<h2>Spelling &amp; usage warnings</h2>
<ul>
  <li>✅ deposit / ❌ deposite</li>
  <li>✅ withdraw → withdrawal (noun)</li>
  <li>✅ transfer money <strong>to</strong> an account</li>
  <li>Cash in / cash out (informal) ≈ deposit / withdraw</li>
</ul>

<h2>Useful phrases</h2>
<ul>
  <li>I’d like to make a deposit, please.</li>
  <li>I’d like to withdraw 500,000 UZS.</li>
  <li>Can I transfer money from my current account to my savings account?</li>
  <li>Is there a daily withdrawal limit?</li>
</ul>

<h2>Dialogue — At the teller</h2>
<p><strong>Customer:</strong> I’d like to deposit this cash into my savings account.<br>
<strong>Teller:</strong> Certainly. Please fill in the deposit slip and sign here.<br>
<strong>Customer:</strong> Done. Can I also withdraw 300,000 for the weekend?<br>
<strong>Teller:</strong> Yes. May I see your ID? … Thank you. Here is your cash and receipt.<br>
<strong>Customer:</strong> Could you tell me my new balance?<br>
<strong>Teller:</strong> Of course. Your available balance is 4,250,000 UZS.</p>

<h2>Grammar — Past simple for completed actions</h2>
<ul>
  <li>Yesterday she <strong>deposited</strong> her bonus.</li>
  <li>He <strong>withdrew</strong> money and <strong>paid</strong> the rent.</li>
  <li>We <strong>transferred</strong> the fee on Monday.</li>
</ul>

<h2>Reading — A short money story</h2>
<p>Yesterday Ms Karimova deposited 2,000,000 UZS into her savings account. Today she withdrew 200,000 UZS from the ATM to buy gifts. She also transferred 150,000 UZS to her brother’s current account. Her balance is lower than yesterday, but she still has enough for the month. She keeps every receipt in a folder for her records.</p>

<h2>Practice prompts</h2>
<ol>
  <li>Tell a 5-sentence story using deposit, withdraw, transfer, balance.</li>
  <li>Ask three questions a teller might ask during a cash deposit.</li>
</ol>
""",
            ),
            _lec(
                "Reading a bank statement",
                "eb-statement",
                """
<h2>Lesson goal</h2>
<p>Read statement lines and explain date, description, amount, and running balance.</p>

<h2>Statement words</h2>
<ul>
  <li><strong>transaction</strong> — one money movement</li>
  <li><strong>credit</strong> — money in (+)</li>
  <li><strong>debit</strong> — money out (−)</li>
  <li><strong>running balance</strong> — balance after each line</li>
  <li><strong>opening / closing balance</strong> — start and end of the period</li>
</ul>

<h2>Sample statement</h2>
<table>
  <tr><th>Date</th><th>Description</th><th>Amount</th><th>Balance</th></tr>
  <tr><td>12 Mar</td><td>Salary credit</td><td>+8,500,000</td><td>9,200,000</td></tr>
  <tr><td>13 Mar</td><td>Card payment (supermarket)</td><td>−185,000</td><td>9,015,000</td></tr>
  <tr><td>14 Mar</td><td>ATM withdrawal</td><td>−400,000</td><td>8,615,000</td></tr>
  <tr><td>15 Mar</td><td>Transfer to savings</td><td>−850,000</td><td>7,765,000</td></tr>
  <tr><td>16 Mar</td><td>Refund (shop)</td><td>+85,000</td><td>7,850,000</td></tr>
</table>

<h2>How to talk about a line</h2>
<ul>
  <li>On 13 March there was a card payment of 185,000 UZS.</li>
  <li>The salary credit increased the balance.</li>
  <li>After the ATM withdrawal, the balance was 8,615,000.</li>
</ul>

<h2>Dialogue — Explaining a line</h2>
<p><strong>Customer:</strong> What is this minus 400,000?<br>
<strong>Officer:</strong> That is an ATM withdrawal on 14 March.<br>
<strong>Customer:</strong> And the plus 85,000?<br>
<strong>Officer:</strong> That’s a refund from a shop. The money came back to your account.</p>

<h2>Grammar — Past simple + time phrases</h2>
<p><em>On Monday… / Yesterday… / Last week… / Two days ago…</em><br>
She paid by card. He withdrew cash. The bank credited the salary.</p>

<h2>Comprehension</h2>
<ol>
  <li>What was the largest credit?</li>
  <li>Did the balance rise or fall after the supermarket payment?</li>
  <li>Explain the 15 March line in one sentence.</li>
</ol>

<h2>Speaking</h2>
<p>Describe the whole sample statement in 60–90 seconds using the words credit, debit, balance, transfer, refund.</p>
""",
            ),
        ],
        "practice": {
            "eb-account-types": _quiz(
                "eb-q-savings",
                "Savings account",
                "Hisob turlari.",
                "A savings account is mainly for…",
                [
                    "A) keeping money and earning interest",
                    "B) printing banknotes",
                    "C) hiring staff",
                    "D) closing the branch",
                ],
                "A",
            ),
            "eb-deposit-withdraw": _quiz(
                "eb-q-withdraw",
                "Withdraw",
                "Fe’llar.",
                "To withdraw money means…",
                [
                    "A) to put money in",
                    "B) to take money out",
                    "C) to open HR files",
                    "D) to raise the interest rate",
                ],
                "B",
            ),
            "eb-statement": _quiz(
                "eb-q-balance",
                "Balance",
                "Statement.",
                "The balance is…",
                [
                    "A) the interest rate only",
                    "B) the money available in the account",
                    "C) the bank manager’s name",
                    "D) a type of loan",
                ],
                "B",
            ),
        },
        "exercises": [
            _quiz(
                "eb-m2-id-like",
                "I’d like to…",
                "Muloyim tilak.",
                "Choose the best sentence:",
                [
                    "A) I want account open now!",
                    "B) I’d like to open a current account, please.",
                    "C) Give savings!",
                    "D) Balance me.",
                ],
                "B",
                difficulty="medium",
            ),
        ],
        "homework": _hw(
            "Module 2 homework\n"
            "1) Write a 7-line mini statement with dates and a running balance.\n"
            "2) Use deposit / withdraw / transfer / balance / refund in 6 sentences.\n"
            "3) Speaking: explain how to open a savings account (10–12 lines).\n"
            "4) Compare current vs savings in a short paragraph (80–100 words)."
        ),
    },
    {
        "order": 3,
        "title": "Kartalar va to‘lovlar (Cards & payments)",
        "slug": "eb-cards-payments",
        "description": "Debit/credit cards, transfers, ATM, online payments.",
        "lectures": [
            _lec(
                "Debit and credit cards",
                "eb-cards",
                """
<h2>Lesson goal</h2>
<p>Explain debit vs credit clearly and answer basic customer questions about limits and PINs.</p>

<h2>Key vocabulary</h2>
<table>
  <tr><th>Term</th><th>Meaning</th></tr>
  <tr><td><strong>debit card</strong></td><td>pays with your own money in the account</td></tr>
  <tr><td><strong>credit card</strong></td><td>borrows from the bank up to a limit</td></tr>
  <tr><td><strong>credit limit</strong></td><td>maximum you can borrow on the card</td></tr>
  <tr><td><strong>PIN</strong></td><td>secret personal code</td></tr>
  <tr><td><strong>expiry date</strong></td><td>when the card stops working</td></tr>
  <tr><td><strong>CVV / security code</strong></td><td>code for online payments</td></tr>
  <tr><td><strong>contactless</strong></td><td>pay by tapping the card</td></tr>
  <tr><td><strong>available credit</strong></td><td>credit limit minus what you already used</td></tr>
</table>

<h2>Clear difference</h2>
<p><strong>Debit</strong> = your money now.<br>
<strong>Credit</strong> = bank’s money now → you repay later (often with interest if not paid in full).</p>

<h2>Dialogue — Which card?</h2>
<p><strong>Customer:</strong> What’s the difference between debit and credit?<br>
<strong>Officer:</strong> With a debit card, the money comes from your account immediately. With a credit card, you borrow up to your credit limit and repay later.<br>
<strong>Customer:</strong> Is credit free?<br>
<strong>Officer:</strong> Not always. If you don’t repay on time, you may pay interest and fees. Would you like me to show an example?</p>

<h2>Grammar — Zero / first ideas with if</h2>
<ul>
  <li>If you use a debit card, the money leaves your account.</li>
  <li>If you miss a credit card payment, you may pay a fee.</li>
</ul>

<h2>Reading — Choosing carefully</h2>
<p>Sardor wants a card for supermarket shopping and online tickets. He already budgets well, so the banker recommends a debit card linked to his current account. Later, when Sardor has a stable salary history, he can apply for a small credit card for emergencies. The banker reminds him: “A credit card is a tool, not free money.”</p>

<h2>Speaking</h2>
<ol>
  <li>Explain debit vs credit in 5 sentences.</li>
  <li>Warn a friend about sharing a PIN (3 tips).</li>
</ol>
""",
            ),
            _lec(
                "Transfers and payments",
                "eb-transfers",
                """
<h2>Lesson goal</h2>
<p>Talk about local transfers, fees, and careful checking of account details.</p>

<h2>Key vocabulary</h2>
<ul>
  <li><strong>transfer</strong> — send money from one account to another</li>
  <li><strong>beneficiary</strong> — person/company who receives the money</li>
  <li><strong>account number / IBAN</strong> — account identifier</li>
  <li><strong>fee / charge / commission</strong> — money the bank takes for a service</li>
  <li><strong>online banking / mobile app</strong> — banking on internet/phone</li>
  <li><strong>payment reference</strong> — note that explains the payment</li>
  <li><strong>same-day / instant transfer</strong> — arrives quickly (if available)</li>
</ul>

<h2>Safety checklist (say this to clients)</h2>
<ol>
  <li>Check the beneficiary name.</li>
  <li>Check the account number carefully.</li>
  <li>Check the amount and currency.</li>
  <li>Ask about the fee before you confirm.</li>
</ol>

<h2>Useful phrases</h2>
<ul>
  <li>I’d like to make a transfer to another bank.</li>
  <li>Please check the account number carefully.</li>
  <li>Is there a fee for this transfer?</li>
  <li>The money should arrive today / on the next working day.</li>
</ul>

<h2>Dialogue — Transfer desk</h2>
<p><strong>Customer:</strong> I’d like to transfer 1,500,000 UZS to my supplier.<br>
<strong>Officer:</strong> Certainly. What’s the beneficiary’s account number?<br>
<strong>Customer:</strong> Here it is.<br>
<strong>Officer:</strong> Thank you. Please double-check the last four digits with me: 7-7-2-1.<br>
<strong>Customer:</strong> Yes, that’s correct. Is there a fee?<br>
<strong>Officer:</strong> Yes, a small transfer fee. Shall I continue?</p>

<h2>Reading — A costly typo</h2>
<p>A client typed one wrong digit and sent rent to the wrong account. The bank tried to help, but recovery took time and stress. After that, the client always reads numbers aloud with the officer. One careful minute can save a week of problems.</p>

<h2>Speaking</h2>
<p>Role-play a transfer: ask for beneficiary details, confirm digits, explain the fee, and give a timing estimate.</p>
""",
            ),
            _lec(
                "ATM and card safety",
                "eb-atm-safety",
                """
<h2>Lesson goal</h2>
<p>Give clear safety advice for ATMs, lost cards, and online card use.</p>

<h2>Do / Don’t</h2>
<table>
  <tr><th>Do</th><th>Don’t</th></tr>
  <tr><td>Cover the keypad when you enter your PIN</td><td>Share your PIN with anyone</td></tr>
  <tr><td>Report a lost card immediately</td><td>Write your PIN on the card</td></tr>
  <tr><td>Use official bank apps and websites</td><td>Click unknown payment links</td></tr>
  <tr><td>Check SMS alerts for every payment</td><td>Ignore strange transactions</td></tr>
</table>

<h2>Emergency phrases</h2>
<ul>
  <li>I’ve lost my card. Please block it immediately.</li>
  <li>I don’t recognise this transaction.</li>
  <li>Someone asked for my PIN by phone — I refused.</li>
</ul>

<h2>Dialogue — Lost card</h2>
<p><strong>Customer:</strong> Hello, I’ve lost my debit card.<br>
<strong>Hotline:</strong> I’m sorry to hear that. I can block it now. May I verify your full name and date of birth?<br>
<strong>Customer:</strong> Yes…<br>
<strong>Hotline:</strong> Done. Your card is blocked. Would you like to order a replacement?</p>

<h2>Grammar — Imperatives for instructions</h2>
<ul>
  <li>Keep your PIN secret.</li>
  <li>Call the bank now.</li>
  <li>Don’t share codes from SMS.</li>
</ul>

<h2>Reading — Skimming risk</h2>
<p>Before using an ATM, look at the card slot and keypad. If something looks loose or strange, use another machine and tell the bank. Good habits are part of financial safety — like locking your front door.</p>

<h2>Speaking</h2>
<ol>
  <li>Give five safety tips using imperatives.</li>
  <li>Act out the lost-card phone call (both roles).</li>
</ol>
""",
            ),
        ],
        "practice": {
            "eb-cards": _quiz(
                "eb-q-debit",
                "Debit card",
                "Kartalar.",
                "A debit card uses…",
                [
                    "A) only the bank manager’s money",
                    "B) money already in your account",
                    "C) unlimited free loans forever",
                    "D) HR documents",
                ],
                "B",
            ),
            "eb-transfers": _quiz(
                "eb-q-beneficiary",
                "Beneficiary",
                "O‘tkazmalar.",
                "The beneficiary is…",
                [
                    "A) the person who receives the money",
                    "B) the ATM machine",
                    "C) the interest rate",
                    "D) the branch building",
                ],
                "A",
            ),
            "eb-atm-safety": _quiz(
                "eb-q-pin",
                "PIN xavfsizligi",
                "Xavfsizlik.",
                "Which advice is correct?",
                [
                    "A) Share your PIN with friends",
                    "B) Write the PIN on the card",
                    "C) Cover the keypad and keep the PIN secret",
                    "D) Never report a lost card",
                ],
                "C",
            ),
        },
        "exercises": [
            _quiz(
                "eb-m3-credit-limit",
                "Credit limit",
                "Kredit karta.",
                "A credit limit is…",
                [
                    "A) the maximum you can borrow on the card",
                    "B) the bank’s lunch time",
                    "C) a type of savings account",
                    "D) an HR interview score",
                ],
                "A",
                difficulty="medium",
            ),
        ],
        "homework": _hw(
            "Module 3 homework\n"
            "1) Write 8 card/ATM safety tips (imperatives).\n"
            "2) Dialogue (12 lines): customer wants a transfer; officer confirms details + fee.\n"
            "3) Explain debit vs credit in a short paragraph (90–120 words).\n"
            "4) Write an SMS-style alert explanation for a client in 4 sentences."
        ),
    },
    {
        "order": 4,
        "title": "Kredit va qarzlar (Loans & credit)",
        "slug": "eb-loans-credit",
        "description": "Loan types, interest, collateral, overdue payments.",
        "lectures": [
            _lec(
                "Loan basics",
                "eb-loan-basics",
                """
<h2>Lesson goal</h2>
<p>Use accurate loan vocabulary and avoid the classic borrow/lend mistake.</p>

<h2>Key vocabulary</h2>
<table>
  <tr><th>Term</th><th>Meaning</th></tr>
  <tr><td><strong>loan / credit</strong></td><td>borrowed money you must repay</td></tr>
  <tr><td><strong>borrower</strong></td><td>person who takes the loan</td></tr>
  <tr><td><strong>lender</strong></td><td>bank that gives the loan</td></tr>
  <tr><td><strong>interest rate</strong></td><td>% charged for borrowing</td></tr>
  <tr><td><strong>principal</strong></td><td>the original amount borrowed</td></tr>
  <tr><td><strong>repayment / installment</strong></td><td>regular payment to return the loan</td></tr>
  <tr><td><strong>maturity</strong></td><td>end date of the loan</td></tr>
  <tr><td><strong>application</strong></td><td>formal request for a loan</td></tr>
</table>

<h2>Borrow vs lend (critical)</h2>
<ul>
  <li>The <strong>client borrows</strong> money <strong>from</strong> the bank.</li>
  <li>The <strong>bank lends</strong> money <strong>to</strong> the client.</li>
  <li>❌ I want to lend money from the bank.</li>
  <li>✅ I want to borrow money from the bank.</li>
</ul>

<h2>Dialogue — First loan questions</h2>
<p><strong>Customer:</strong> I’d like to apply for a consumer loan.<br>
<strong>Officer:</strong> Certainly. How much would you like to borrow, and for how many months?<br>
<strong>Customer:</strong> About 30 million UZS for 24 months.<br>
<strong>Officer:</strong> We’ll check your income, employment, and credit history. The interest rate depends on your profile.</p>

<h2>Grammar — want to / would like to / need to</h2>
<ul>
  <li>I’d like to borrow money for home repairs.</li>
  <li>You need to provide salary statements.</li>
  <li>We have to check your documents before approval.</li>
</ul>

<h2>Reading — Not free money</h2>
<p>A loan can help with a real plan: education, repairs, or a car. But every loan has a cost — the interest rate — and a timetable for installments. Good officers explain both the monthly payment and the total cost. Responsible borrowing starts with clear numbers, not hope alone.</p>

<h2>Speaking</h2>
<ol>
  <li>Define borrower, lender, interest rate, installment.</li>
  <li>Correct three wrong sentences with lend/borrow.</li>
</ol>
""",
            ),
            _lec(
                "Mortgage and collateral",
                "eb-mortgage",
                """
<h2>Lesson goal</h2>
<p>Describe secured lending with mortgage and collateral in accurate English.</p>

<h2>Key vocabulary</h2>
<ul>
  <li><strong>mortgage</strong> — loan to buy property (house/apartment)</li>
  <li><strong>collateral / security</strong> — asset given as guarantee</li>
  <li><strong>secured loan</strong> — protected by collateral</li>
  <li><strong>unsecured loan</strong> — no collateral (often higher rate)</li>
  <li><strong>consumer loan</strong> — personal needs</li>
  <li><strong>overdraft</strong> — short negative balance allowed by arrangement</li>
  <li><strong>down payment / deposit</strong> — first part the buyer pays</li>
  <li><strong>valuation</strong> — estimate of property value</li>
</ul>

<h2>Simple explanation</h2>
<p>If the borrower cannot repay a mortgage, the bank may use the property (collateral) according to law and contract. That is why documents and valuation matter.</p>

<h2>Dialogue</h2>
<p><strong>Customer:</strong> We want a mortgage for an apartment.<br>
<strong>Officer:</strong> Congratulations on the plan. The apartment will usually be the collateral. We’ll need income documents and a valuation.<br>
<strong>Customer:</strong> How long does approval take?<br>
<strong>Officer:</strong> It depends on the file. I’ll give you a checklist today.</p>

<h2>Reading — Checklist thinking</h2>
<p>Before a mortgage meeting, prepare: ID, income proof, property details, and questions about rate, term, early repayment, and fees. Clear questions save time. “What is the monthly installment?” and “What happens if I repay early?” are smart, normal questions.</p>

<h2>Speaking</h2>
<p>Explain collateral to a friend who is not a banker — 6 simple sentences, no jargon overload.</p>
""",
            ),
            _lec(
                "Late payments",
                "eb-overdue",
                """
<h2>Lesson goal</h2>
<p>Explain overdue payments politely and use first conditional for consequences.</p>

<h2>Key vocabulary</h2>
<ul>
  <li><strong>due date</strong> — when payment must be made</li>
  <li><strong>overdue / late payment</strong> — after the due date</li>
  <li><strong>penalty / late fee</strong> — extra charge for being late</li>
  <li><strong>reminder</strong> — message that payment is due/overdue</li>
  <li><strong>default</strong> — serious failure to repay</li>
  <li><strong>restructuring</strong> — changing the repayment plan (if allowed)</li>
</ul>

<h2>Polite but clear phrases</h2>
<ul>
  <li>I’m afraid your installment is overdue.</li>
  <li>Please pay as soon as possible to avoid a penalty.</li>
  <li>If you pay today, you will avoid an extra fee.</li>
  <li>Would you like to discuss a payment plan with an officer?</li>
</ul>

<h2>Grammar — First conditional</h2>
<p>Form: <strong>If + present simple, will + verb</strong></p>
<ul>
  <li>If you pay today, you will avoid a late fee.</li>
  <li>If the payment stays overdue, the bank will send another reminder.</li>
  <li>If you have a problem, call us early — don’t wait in silence.</li>
</ul>

<h2>Dialogue — Overdue call</h2>
<p><strong>Officer:</strong> Good afternoon. I’m calling about your loan installment. I’m afraid it is overdue by five days.<br>
<strong>Customer:</strong> Oh — I had a delay with my salary.<br>
<strong>Officer:</strong> I understand. If you pay tomorrow morning, you will reduce further penalties. Shall I SMS the exact amount due?</p>

<h2>Reading — Early communication</h2>
<p>Clients sometimes hide from calls when money is tight. That usually makes things worse. Banks prefer early contact: maybe a short plan is possible. Silence helps nobody. Polite honesty is professional on both sides.</p>

<h2>Speaking</h2>
<ol>
  <li>Deliver overdue news politely (30 seconds).</li>
  <li>Make 5 first-conditional sentences about payments.</li>
</ol>
""",
            ),
        ],
        "practice": {
            "eb-loan-basics": _quiz(
                "eb-q-borrow",
                "Borrow vs lend",
                "Terminologiya.",
                "Correct sentence:",
                [
                    "A) I want to lend money from the bank.",
                    "B) I want to borrow money from the bank.",
                    "C) The client lends a mortgage to himself.",
                    "D) Interest rate borrows the client.",
                ],
                "B",
            ),
            "eb-mortgage": _quiz(
                "eb-q-mortgage",
                "Mortgage",
                "Kredit turlari.",
                "A mortgage is usually…",
                [
                    "A) a loan to buy property",
                    "B) a type of debit PIN",
                    "C) an HR holiday",
                    "D) a savings gift",
                ],
                "A",
            ),
            "eb-overdue": _quiz(
                "eb-q-overdue",
                "Overdue",
                "Kechikish.",
                "If a payment is overdue, it is…",
                [
                    "A) early",
                    "B) late",
                    "C) free forever",
                    "D) not a real word",
                ],
                "B",
            ),
        },
        "exercises": [
            _quiz(
                "eb-m4-conditional",
                "First conditional",
                "Grammatika.",
                "Choose the correct sentence:",
                [
                    "A) If you pay today, you will avoid a late fee.",
                    "B) If you pay today, you avoid will a late fee.",
                    "C) If you will pay today, you avoid a late fee.",
                    "D) If pay you today, fee late avoid.",
                ],
                "A",
                difficulty="medium",
            ),
        ],
        "homework": _hw(
            "Module 4 homework\n"
            "1) Write 8 sentences with borrow / lend / loan / interest rate / installment.\n"
            "2) Dialogue: officer explains an overdue installment (12–14 lines).\n"
            "3) Explain collateral in 5 simple English sentences.\n"
            "4) Write 6 first-conditional sentences about loan payments."
        ),
    },
    {
        "order": 8,
        "title": "Bankda HR (HR in banking)",
        "slug": "eb-hr-banking",
        "description": "Jobs, CV, interviews, and workplace English in a bank.",
        "lectures": [
            _lec(
                "Bank job titles",
                "eb-job-titles",
                """
<h2>Lesson goal</h2>
<p>Name common bank jobs and introduce your role in one clear sentence.</p>

<h2>Job map</h2>
<table>
  <tr><th>Title</th><th>Focus</th></tr>
  <tr><td>relationship manager</td><td>long-term client relationships</td></tr>
  <tr><td>credit analyst</td><td>loan files and risk of default</td></tr>
  <tr><td>risk officer</td><td>identify and control risks</td></tr>
  <tr><td>compliance officer</td><td>rules, KYC, monitoring</td></tr>
  <tr><td>customer service specialist</td><td>help desk / branch support</td></tr>
  <tr><td>operations specialist</td><td>processing and back office</td></tr>
  <tr><td>intern / trainee</td><td>learning role with supervision</td></tr>
</table>

<h2>Self-introduction templates</h2>
<ul>
  <li>I’m a credit analyst. I review loan applications and client documents.</li>
  <li>I work in customer service. I help clients with cards and transfers.</li>
  <li>I’m an intern in retail banking. I’m learning account opening procedures.</li>
</ul>

<h2>Dialogue — Networking</h2>
<p><strong>A:</strong> Hi, what do you do here?<br>
<strong>B:</strong> I’m a compliance officer. I review KYC files and unusual transactions.<br>
<strong>A:</strong> That sounds important.<br>
<strong>B:</strong> It is. And you?<br>
<strong>A:</strong> I’m a relationship manager for SME clients.</p>

<h2>Reading — More than one path</h2>
<p>Banking careers are not only “cashier forever.” Some people start at the counter, then move to sales, credit, or operations. English helps when products, emails, and training materials use international terms. Clear speech also helps in interviews and team meetings.</p>

<h2>Speaking</h2>
<ol>
  <li>Introduce three imaginary colleagues and their jobs.</li>
  <li>30-second self-introduction for your target bank role.</li>
</ol>
""",
            ),
            _lec(
                "CV and interview phrases",
                "eb-cv-interview",
                """
<h2>Lesson goal</h2>
<p>Build pre-intermediate CV lines and interview answers with present perfect for experience.</p>

<h2>High-value phrases</h2>
<ul>
  <li>I have two years of experience in customer service.</li>
  <li>I’m responsible for checking client documents.</li>
  <li>I improved my English to work with international clients.</li>
  <li>I’m a team player and I’m careful with numbers.</li>
  <li>I deal with customers politely under pressure.</li>
  <li>I learned bank products quickly during my internship.</li>
</ul>

<h2>Grammar — Present perfect for experience</h2>
<ul>
  <li>I <strong>have worked</strong> in a bank branch for one year.</li>
  <li>I <strong>have handled</strong> cash and card issues.</li>
  <li>I <strong>haven’t worked</strong> in credit yet, but I am learning.</li>
</ul>
<p>Compare: <em>I worked there in 2023</em> (finished time) vs <em>I have worked there for a year</em> (experience / unfinished period).</p>

<h2>Dialogue — Short interview</h2>
<p><strong>HR:</strong> Tell me about yourself.<br>
<strong>Candidate:</strong> I’m Dilshod. I have one year of experience in retail customer service. I’m responsible for helping clients with accounts and cards. I’d like to grow in banking.<br>
<strong>HR:</strong> What are your strengths?<br>
<strong>Candidate:</strong> I’m organised, polite, and careful with details.</p>

<h2>Reading — Honest and specific</h2>
<p>Good answers are specific. “I am perfect at everything” sounds weak. “I reduced queue mistakes by double-checking ID numbers” sounds real. Prepare 3 stories: a problem, your action, the result — in simple English.</p>

<h2>Writing task</h2>
<p>Write 8 CV-style bullet lines starting with verbs: assisted, checked, prepared, explained, processed, supported…</p>
""",
            ),
            _lec(
                "Speaking: interview mini-dialogue",
                "eb-interview-speak",
                """
<h2>Lesson goal</h2>
<p>Answer common bank interview questions in 20–40 seconds with clear structure.</p>

<h2>Answer formula (STAR-light)</h2>
<ol>
  <li><strong>Situation</strong> — one line</li>
  <li><strong>Action</strong> — what you did</li>
  <li><strong>Result</strong> — simple outcome</li>
</ol>

<h2>Sample Q&amp;A bank</h2>
<p><strong>Q:</strong> Why do you want to work in banking?<br>
<strong>A:</strong> I’m interested in finance and I like helping people with money matters. Banking combines service and responsibility.</p>
<p><strong>Q:</strong> What are your strengths?<br>
<strong>A:</strong> I’m organised, polite, and I learn new products quickly. In my last role I explained fees clearly to customers.</p>
<p><strong>Q:</strong> What is your weakness?<br>
<strong>A:</strong> Sometimes I need more time for complex Excel files, so I practise every week and ask colleagues when needed.</p>
<p><strong>Q:</strong> How do you handle an angry customer?<br>
<strong>A:</strong> I stay calm, listen, apologise for the inconvenience, and offer a clear next step. If needed, I escalate to a supervisor.</p>

<h2>Useful linking words</h2>
<p>First… / Then… / For example… / As a result… / That’s why…</p>

<h2>Practice cycle</h2>
<ol>
  <li>Read one answer aloud slowly.</li>
  <li>Close the page and say it from memory.</li>
  <li>Record yourself and fix grammar only (not accent perfection).</li>
</ol>

<h2>Pair work</h2>
<p>Partner A = HR (asks 4 questions). Partner B answers. Then switch. Give one positive comment each.</p>
""",
            ),
        ],
        "practice": {
            "eb-job-titles": _quiz(
                "eb-q-analyst",
                "Credit analyst",
                "Lavozimlar.",
                "A credit analyst mainly…",
                [
                    "A) reviews loan applications",
                    "B) cooks in the canteen",
                    "C) prints passports",
                    "D) sets national holidays",
                ],
                "A",
            ),
            "eb-cv-interview": _quiz(
                "eb-q-present-perfect",
                "Present perfect",
                "Grammatika.",
                "Correct sentence about experience:",
                [
                    "A) I work in a bank since 2024.",
                    "B) I have worked in a bank for one year.",
                    "C) I am work in bank one year.",
                    "D) I working bank yesterday year.",
                ],
                "B",
            ),
            "eb-interview-speak": _quiz(
                "eb-q-strength",
                "Interview answer",
                "Gapirish.",
                "Best professional answer to “What are your strengths?”",
                [
                    "A) I sleep a lot.",
                    "B) I’m organised and polite with customers.",
                    "C) I hate numbers.",
                    "D) I don’t like teamwork.",
                ],
                "B",
            ),
        },
        "exercises": [
            _quiz(
                "eb-m5-responsible",
                "I’m responsible for…",
                "Ish tavsifi.",
                "Complete the idea correctly:",
                [
                    "A) I’m responsible for checking client documents.",
                    "B) I’m responsible to check forever documents bad.",
                    "C) I responsible checking.",
                    "D) Documents responsible me.",
                ],
                "A",
                difficulty="medium",
            ),
        ],
        "homework": _hw(
            "Module 5 homework\n"
            "1) Write a 10-line self-introduction for a bank job.\n"
            "2) Answer in writing: Why banking? Strengths? Weakness? Angry customer?\n"
            "3) Speaking: record or rehearse a 60-second introduction.\n"
            "4) Create 8 CV bullets with present perfect or past simple."
        ),
    },
    {
        "order": 9,
        "title": "Mijozlarga xizmat (Customer service)",
        "slug": "eb-customer-service",
        "description": "Complaints, phone English, problem solving.",
        "lectures": [
            _lec(
                "Handling complaints",
                "eb-complaints",
                """
<h2>Lesson goal</h2>
<p>Respond to complaints with empathy, clarity, and a next step.</p>

<h2>3-step service model</h2>
<ol>
  <li><strong>Empathy</strong> — show you care</li>
  <li><strong>Clarify</strong> — confirm the problem</li>
  <li><strong>Action</strong> — offer a next step / timeline</li>
</ol>

<h2>Useful phrases</h2>
<ul>
  <li>I’m sorry for the inconvenience.</li>
  <li>I understand your concern.</li>
  <li>Let me check this for you.</li>
  <li>Thank you for telling us.</li>
  <li>I’ll escalate this to my manager.</li>
  <li>I’ll call you back within one hour.</li>
</ul>

<h2>Dialogue — Fee surprise</h2>
<p><strong>Customer:</strong> Why did you take this fee? Nobody told me!<br>
<strong>Officer:</strong> I’m sorry for the inconvenience. Let me check your tariff and the transaction date… You’re right — we should have explained this fee more clearly. I’ll print the details and explain your options.</p>

<h2>Reading — Tone changes outcomes</h2>
<p>Two officers can say the same rule. One sounds cold: “It’s in the contract.” The other sounds professional: “I’m sorry this was unclear. Here’s where the fee is listed, and here is what we can do next.” Same fact, better trust.</p>

<h2>Speaking</h2>
<p>Practise empathy → clarify → action on three problems: double charge, long queue, blocked card.</p>
""",
            ),
            _lec(
                "Phone banking English",
                "eb-phone",
                """
<h2>Lesson goal</h2>
<p>Use clear, secure phone phrases for identification and hold time.</p>

<h2>Call flow</h2>
<ol>
  <li>Greeting + name</li>
  <li>Offer help</li>
  <li>Verify identity</li>
  <li>Solve / escalate</li>
  <li>Confirm next step + closing</li>
</ol>

<h2>Key phrases</h2>
<ul>
  <li>Bank hotline, Anna speaking. How can I help you?</li>
  <li>Could you spell your full name, please?</li>
  <li>For security, I need to verify a few details.</li>
  <li>Can I put you on hold for a moment?</li>
  <li>Thanks for holding.</li>
  <li>Is there anything else I can help you with today?</li>
</ul>

<h2>Security note (say it)</h2>
<p>We will never ask for your full PIN or full password. If someone asks, hang up and call the official number.</p>

<h2>Dialogue</h2>
<p><strong>Agent:</strong> Orient Bank hotline, Jasur speaking. How can I help you?<br>
<strong>Caller:</strong> My card isn’t working online.<br>
<strong>Agent:</strong> I’m sorry about that. For security, could you confirm your full name and date of birth?<br>
<strong>Caller:</strong> …<br>
<strong>Agent:</strong> Thank you. Can I put you on hold for a moment while I check?<br>
<strong>Caller:</strong> Yes.<br>
<strong>Agent:</strong> Thanks for holding. I can see a temporary block for online payments. I can remove it after one more check…</p>

<h2>Speaking drills</h2>
<ol>
  <li>Open 5 calls with different names.</li>
  <li>Ask to spell names: Karimova, Oxunjonov, Schweitzer (practice clarity).</li>
  <li>Put someone on hold and return politely.</li>
</ol>
""",
            ),
            _lec(
                "Reading: complaint email",
                "eb-complaint-email",
                """
<h2>Lesson goal</h2>
<p>Read a complaint email and write a professional short reply.</p>

<h2>Customer email</h2>
<p>Dear Sir/Madam,<br>
I paid by card yesterday at Green Market, but the amount was charged twice (2 × 186,000 UZS). My account ending 4412 shows both payments. Please refund the extra payment and confirm by email.<br>
Best regards,<br>
A. Rahimov<br>
Phone: 90 000 00 00</p>

<h2>What to notice</h2>
<ul>
  <li>Problem: double charge</li>
  <li>Evidence: amount, merchant, account ending</li>
  <li>Ask: refund + confirmation</li>
</ul>

<h2>Model reply</h2>
<p>Dear Mr Rahimov,<br>
Thank you for your message. I’m sorry for the inconvenience. We are checking the two card payments of 186,000 UZS at Green Market. We will update you within one business day. If a duplicate is confirmed, we will refund the extra amount.<br>
Kind regards,<br>
Malika Yusupova<br>
Customer Service, Orient Bank</p>

<h2>Useful reply chunks</h2>
<ul>
  <li>Thank you for contacting us.</li>
  <li>I’m sorry for the inconvenience.</li>
  <li>We are looking into this now.</li>
  <li>We will get back to you by…</li>
</ul>

<h2>Writing task</h2>
<p>Rewrite the model reply in your own words (don’t copy every sentence). Keep it polite and specific.</p>

<h2>Speaking</h2>
<p>Summarise the email problem in 20 seconds, then summarise your reply plan in 20 seconds.</p>
""",
            ),
        ],
        "practice": {
            "eb-complaints": _quiz(
                "eb-q-inconvenience",
                "Inconvenience",
                "Shikoyat.",
                "Best first response to a complaint:",
                [
                    "A) That’s your problem.",
                    "B) I’m sorry for the inconvenience.",
                    "C) Call someone else forever.",
                    "D) We never make mistakes.",
                ],
                "B",
            ),
            "eb-phone": _quiz(
                "eb-q-on-hold",
                "On hold",
                "Telefon.",
                "“Can I put you on hold?” means…",
                [
                    "A) please wait a short time on the line",
                    "B) close your account now",
                    "C) increase your interest rate",
                    "D) visit HR today",
                ],
                "A",
            ),
            "eb-complaint-email": _quiz(
                "eb-q-double-charge",
                "Double charge",
                "O‘qish.",
                "In the email, the problem is…",
                [
                    "A) the card was charged twice",
                    "B) the customer wants a mortgage poem",
                    "C) HR closed the branch",
                    "D) the PIN is a colour",
                ],
                "A",
            ),
        },
        "exercises": [
            _quiz(
                "eb-m6-escalate",
                "Escalate",
                "Jarayon.",
                "To escalate a case means…",
                [
                    "A) pass it to a higher level / manager",
                    "B) delete the customer",
                    "C) print more cash",
                    "D) ignore the call",
                ],
                "A",
                difficulty="medium",
            ),
        ],
        "homework": _hw(
            "Module 6 homework\n"
            "1) Write a polite reply email to the double-charge complaint (10–12 lines).\n"
            "2) Phone role-play script (12–14 lines) with verification + hold.\n"
            "3) Speaking: empathy + next step in 25 seconds for three scenarios.\n"
            "4) Make a personal phrasebook: 12 service sentences under Empathy / Clarify / Action."
        ),
    },
    {
        "order": 10,
        "title": "KYC va compliance",
        "slug": "eb-compliance-kyc",
        "description": "Identity checks, KYC/AML basics in clear English.",
        "lectures": [
            _lec(
                "What is KYC?",
                "eb-kyc",
                """
<h2>Lesson goal</h2>
<p>Explain KYC accurately in simple English and ask for documents politely.</p>

<h2>Key vocabulary</h2>
<table>
  <tr><th>Term</th><th>Meaning</th></tr>
  <tr><td><strong>KYC (Know Your Customer)</strong></td><td>identifying and verifying the client</td></tr>
  <tr><td><strong>ID / identity document</strong></td><td>passport or national ID</td></tr>
  <tr><td><strong>proof of address</strong></td><td>shows where the client lives</td></tr>
  <tr><td><strong>verification</strong></td><td>checking that information is true</td></tr>
  <tr><td><strong>beneficial owner</strong></td><td>person who ultimately owns/controls a company</td></tr>
  <tr><td><strong>onboarding</strong></td><td>process of accepting a new client</td></tr>
</table>

<h2>Why banks do KYC</h2>
<p>Banks must know who the customer is. This reduces fraud and helps stop illegal money flows. KYC is not “extra bureaucracy for fun” — it is core banking safety.</p>

<h2>Dialogue</h2>
<p><strong>Officer:</strong> For compliance reasons, I need to see your passport and proof of address.<br>
<strong>Customer:</strong> Why so many documents?<br>
<strong>Officer:</strong> It’s part of Know Your Customer rules. We verify identity before we open an account. It protects you and the bank.</p>

<h2>Reading — Incomplete file</h2>
<p>An officer almost opened an account with only a passport photo copy that was unclear. A colleague stopped the process: “We can’t finish onboarding without clear ID and address proof.” Good compliance culture means colleagues can challenge each other politely.</p>

<h2>Speaking</h2>
<p>Explain KYC to a non-banker in 5 sentences. Then ask for passport + proof of address politely.</p>
""",
            ),
            _lec(
                "AML in simple words",
                "eb-aml",
                """
<h2>Lesson goal</h2>
<p>Understand AML at pre-intermediate level and know when to escalate.</p>

<h2>Key vocabulary</h2>
<ul>
  <li><strong>AML (Anti-Money Laundering)</strong> — rules against cleaning illegal money</li>
  <li><strong>suspicious transaction</strong> — unusual activity that needs review</li>
  <li><strong>flag / report</strong> — mark something for compliance review</li>
  <li><strong>monitoring</strong> — watching transactions for unusual patterns</li>
  <li><strong>source of funds</strong> — where the money comes from</li>
</ul>

<h2>Important limit of this lesson</h2>
<p>You are learning workplace English, not giving legal advice. If something looks unusual, escalate to Compliance — don’t accuse the customer loudly on the floor.</p>

<h2>Useful phrases</h2>
<ul>
  <li>I need to escalate this transaction to Compliance because it looks unusual.</li>
  <li>Could you tell us more about the source of these funds?</li>
  <li>Please wait while we complete an additional check.</li>
</ul>

<h2>Dialogue — Escalate calmly</h2>
<p><strong>Teller:</strong> This cash deposit is much larger than usual for this account.<br>
<strong>Supervisor:</strong> Thank you for noticing. Don’t process it yet. Escalate to Compliance and keep the client informed politely.<br>
<strong>Teller:</strong> Should I say “suspicious”?<br>
<strong>Supervisor:</strong> Better: “We need an additional compliance check.” Stay calm and factual.</p>

<h2>Reading — Patterns, not panic</h2>
<p>Unusual does not always mean criminal. A client may sell a car and deposit cash. Still, banks ask questions and document answers. Good staff are curious, polite, and exact — not dramatic.</p>

<h2>Speaking</h2>
<ol>
  <li>Define AML in two sentences.</li>
  <li>Role-play escalating without alarming language.</li>
</ol>
""",
            ),
            _lec(
                "Speaking: asking for documents",
                "eb-ask-docs",
                """
<h2>Lesson goal</h2>
<p>Ask for KYC documents firmly, politely, and completely.</p>

<h2>Document request bank</h2>
<ul>
  <li>For compliance reasons, I need to see your passport.</li>
  <li>Could you provide proof of address, please?</li>
  <li>We also need a recent utility bill or rental contract.</li>
  <li>We cannot open the account without complete KYC documents.</li>
  <li>Please bring the originals, not only photos, if possible.</li>
</ul>

<h2>Full mini-script</h2>
<p>Good morning. To open your account we complete KYC — Know Your Customer. Could you show me your passport, please? Thank you. We also need proof of address, for example a utility bill. I’m afraid we can’t finish today without it, but I can prepare the form now so tomorrow will be quick.</p>

<h2>Grammar — need to / have to / can’t</h2>
<ul>
  <li>We need to verify your identity.</li>
  <li>You have to provide proof of address.</li>
  <li>We can’t open the account yet.</li>
</ul>

<h2>Practice situations</h2>
<ol>
  <li>Customer forgot proof of address.</li>
  <li>Passport is expired.</li>
  <li>Corporate client must declare beneficial owner (simple explanation).</li>
</ol>

<h2>Speaking challenge</h2>
<p>Give a 45-second explanation: what KYC is, which two documents you need, and what happens next.</p>
""",
            ),
        ],
        "practice": {
            "eb-kyc": _quiz(
                "eb-q-kyc",
                "KYC ma’nosi",
                "Compliance.",
                "KYC means…",
                [
                    "A) Know Your Customer",
                    "B) Keep Your Cash",
                    "C) Key Yellow Card",
                    "D) Kill Your Credit",
                ],
                "A",
            ),
            "eb-aml": _quiz(
                "eb-q-aml",
                "AML",
                "Compliance.",
                "AML is mainly about…",
                [
                    "A) decorating the branch",
                    "B) preventing money laundering",
                    "C) choosing card colours",
                    "D) writing poems",
                ],
                "B",
            ),
            "eb-ask-docs": _quiz(
                "eb-q-proof-address",
                "Proof of address",
                "Hujjatlar.",
                "Proof of address shows…",
                [
                    "A) where the client lives",
                    "B) the bank’s lunch menu",
                    "C) the ATM PIN",
                    "D) the credit limit song",
                ],
                "A",
            ),
        },
        "exercises": [
            _quiz(
                "eb-m7-suspicious",
                "Suspicious transaction",
                "Risk.",
                "If a transaction looks unusual, a clerk should…",
                [
                    "A) ignore it always",
                    "B) flag/escalate it to Compliance",
                    "C) delete the bank database",
                    "D) share the PIN online",
                ],
                "B",
                difficulty="medium",
            ),
        ],
        "homework": _hw(
            "Module 7 homework\n"
            "1) Define KYC and AML in your own simple English (6–8 sentences total).\n"
            "2) Dialogue: ask for passport + proof of address; client objects; you explain calmly.\n"
            "3) Speaking: 40-second KYC explanation.\n"
            "4) Write 8 polite compliance phrases for the branch floor."
        ),
    },
    {
        "order": 11,
        "title": "Email va uchrashuvlar (Emails & meetings)",
        "slug": "eb-emails-meetings",
        "description": "Workplace emails, meetings, and short presentations.",
        "lectures": [
            _lec(
                "Writing a clear bank email",
                "eb-email-write",
                """
<h2>Lesson goal</h2>
<p>Write short, polite, purpose-first banking emails.</p>

<h2>Email structure</h2>
<ol>
  <li>Greeting</li>
  <li>Purpose (one clear sentence)</li>
  <li>Details / deadline / next step</li>
  <li>Closing + name + department</li>
</ol>

<h2>Useful openers &amp; closers</h2>
<ul>
  <li>Dear Mr Aliyev, / Dear Ms Karimova,</li>
  <li>I hope you are well.</li>
  <li>I am writing to ask for… / confirm… / inform you…</li>
  <li>Please find the details below.</li>
  <li>Kind regards, / Best regards,</li>
</ul>

<h2>Sample email</h2>
<p>Dear Mr Aliyev,<br>
Thank you for your loan application. We need one more document: your latest salary statement.
Please send it by Friday so we can continue the review.<br>
Kind regards,<br>
Dilnoza Rakhimova<br>
Credit Department, Orient Bank</p>

<h2>Tone tips</h2>
<ul>
  <li>One email = one main purpose.</li>
  <li>Use short sentences.</li>
  <li>Avoid ALL CAPS and blame language.</li>
  <li>Give a date when you need a reply.</li>
</ul>

<h2>Bad → better</h2>
<ul>
  <li>❌ Send docs!!! → ✅ Please send the salary statement by Friday.</li>
  <li>❌ Why you ignore? → ✅ Just a gentle reminder about the missing document.</li>
</ul>

<h2>Writing practice</h2>
<ol>
  <li>Request a meeting with a corporate client.</li>
  <li>Confirm a card replacement is ready.</li>
  <li>Remind about an overdue installment politely.</li>
</ol>
""",
            ),
            _lec(
                "Meeting phrases",
                "eb-meetings",
                """
<h2>Lesson goal</h2>
<p>Join short internal meetings with phrases for starting, agreeing, clarifying, and closing.</p>

<h2>Phrase bank</h2>
<table>
  <tr><th>Moment</th><th>Say</th></tr>
  <tr><td>Start</td><td>Shall we start? / Thanks for coming.</td></tr>
  <tr><td>Opinion</td><td>In my opinion… / I think we should…</td></tr>
  <tr><td>Agree</td><td>I agree. / That makes sense.</td></tr>
  <tr><td>Soft disagree</td><td>I’m not sure about that. / I see your point, but…</td></tr>
  <tr><td>Clarify</td><td>Could you repeat that, please? / What do you mean by…?</td></tr>
  <tr><td>Close</td><td>Let’s summarise the next steps.</td></tr>
</table>

<h2>Mini meeting script</h2>
<p><strong>Chair:</strong> Shall we start? Today we need to decide on the client’s extra documents.<br>
<strong>Analyst:</strong> In my opinion, we should verify the income again.<br>
<strong>RM:</strong> I agree. The numbers look incomplete.<br>
<strong>Chair:</strong> Okay. Next step: request the salary statement by Wednesday. Let’s summarise…</p>

<h2>Grammar — softening opinions</h2>
<ul>
  <li>I think… / Perhaps we could… / It might be better to…</li>
  <li>Avoid: “You are wrong.” Prefer: “I see it differently because…”</li>
</ul>

<h2>Speaking game</h2>
<p>3 people, 4 minutes: agenda = “approve / delay a small loan.” Use at least 8 meeting phrases from the table.</p>
""",
            ),
            _lec(
                "Mini presentation: a bank product",
                "eb-present-product",
                """
<h2>Lesson goal</h2>
<p>Present a simple bank product in about 60–90 seconds.</p>

<h2>5-part template</h2>
<ol>
  <li>Name the product</li>
  <li>Who it is for</li>
  <li>Main benefit</li>
  <li>One condition / fee / limit</li>
  <li>Call to action</li>
</ol>

<h2>Model pitch</h2>
<p>Our Basic Savings Account is for individuals who want to keep money safely and earn interest.
You can deposit money anytime in branch or via the app.
The minimum opening amount is 100,000 UZS.
Visit our branch or open it in the mobile app today — I can help you with the form.</p>

<h2>Upgrade language</h2>
<ul>
  <li>This product is designed for…</li>
  <li>The main benefit is…</li>
  <li>Please note that…</li>
  <li>If you have questions, I’m happy to help.</li>
</ul>

<h2>Second model — debit card</h2>
<p>The Everyday Debit Card is for current-account clients.
It helps you pay in shops and online without carrying too much cash.
There is a daily ATM limit for safety.
Would you like me to activate card controls in the app with you now?</p>

<h2>Delivery tips</h2>
<ul>
  <li>Smile with your voice; don’t rush numbers.</li>
  <li>One idea per sentence.</li>
  <li>Stop and ask: “Does this sound useful for you?”</li>
</ul>

<h2>Practice</h2>
<ol>
  <li>Write two pitches (savings + card) using the template.</li>
  <li>Say each pitch aloud three times.</li>
  <li>Partner asks two objections; you answer politely.</li>
</ol>

<h2>Course wrap tip</h2>
<p>You now have banking English for service, products, credit, HR, compliance, and workplace communication. Keep a personal phrase notebook and revise 10 lines every day.</p>
""",
            ),
        ],
        "practice": {
            "eb-email-write": _quiz(
                "eb-q-email-purpose",
                "Email purpose",
                "Yozish.",
                "A good bank email should…",
                [
                    "A) state the purpose clearly and politely",
                    "B) use only emojis",
                    "C) hide the next step",
                    "D) insult the client",
                ],
                "A",
            ),
            "eb-meetings": _quiz(
                "eb-q-summarise",
                "Summarise",
                "Uchrashuv.",
                "“Let’s summarise the next steps” is used to…",
                [
                    "A) end with clear actions",
                    "B) delete the agenda",
                    "C) close all accounts",
                    "D) change the PIN randomly",
                ],
                "A",
            ),
            "eb-present-product": _quiz(
                "eb-q-product-template",
                "Product pitch",
                "Taqdimot.",
                "A short product presentation should include…",
                [
                    "A) who it is for and the main benefit",
                    "B) only jokes",
                    "C) the manager’s private PIN",
                    "D) no call to action ever",
                ],
                "A",
            ),
        },
        "exercises": [
            _quiz(
                "eb-m8-kind-regards",
                "Email closing",
                "Yozishma.",
                "A professional closing is…",
                [
                    "A) Kind regards,",
                    "B) Bye loser,",
                    "C) Give money,",
                    "D) PIN forever,",
                ],
                "A",
            ),
            _quiz(
                "eb-m8-opinion",
                "In my opinion",
                "Uchrashuv.",
                "Choose the natural meeting phrase:",
                [
                    "A) In my opinion, we should verify the income.",
                    "B) Opinion my, income verify must scream.",
                    "C) I opinioning strong.",
                    "D) Verify you now shout.",
                ],
                "A",
                difficulty="medium",
            ),
        ],
        "homework": _hw(
            "Module 8 homework\n"
            "1) Write a full email asking for a salary statement (10–12 lines).\n"
            "2) Prepare two 60–90 second product pitches (write + speak).\n"
            "3) List 12 meeting phrases; use 6 in a short dialogue.\n"
            "4) Final reflection (8 sentences): which banking English skills improved most?"
        ),
    },
]


def build_english_banking_modules():
    from apps.core.english_banking_modules_extra import EXTRA_MODULES

    # Modules 1–4, then FX / trade / digital (5–7), then HR→comms (8–11).
    head = [m for m in MODULES if m["order"] <= 4]
    tail = [m for m in MODULES if m["order"] >= 8]
    return head + list(EXTRA_MODULES) + tail
