"""
Extra English-for-Banking modules (5–7) — deeper banking spheres.
Merged in english_banking_content.build_english_banking_modules().
"""

from apps.core.english_banking_content import _hw, _lec, _quiz

EXTRA_MODULES = [
    {
        "order": 5,
        "title": "Valyuta va pul o‘tkazmalari (FX & remittances)",
        "slug": "eb-fx-remittance",
        "description": "Exchange rates, buying/selling currency, remittances, and wire basics.",
        "lectures": [
            _lec(
                "Foreign exchange basics",
                "eb-fx-basics",
                """
<h2>Lesson goal</h2>
<p>Explain currency exchange in clear pre-intermediate English using accurate banking terms.</p>

<h2>Key vocabulary</h2>
<table>
  <tr><th>Term</th><th>Meaning</th><th>Example</th></tr>
  <tr><td><strong>foreign exchange (FX / forex)</strong></td><td>changing one currency into another</td><td>The FX desk sells US dollars.</td></tr>
  <tr><td><strong>currency pair</strong></td><td>two currencies quoted together</td><td>USD/UZS is a currency pair.</td></tr>
  <tr><td><strong>exchange rate</strong></td><td>price of one currency in another</td><td>What’s today’s exchange rate?</td></tr>
  <tr><td><strong>buy rate / sell rate</strong></td><td>bank’s rates for buying or selling currency</td><td>Our sell rate for USD is…</td></tr>
  <tr><td><strong>spread</strong></td><td>difference between buy and sell rates</td><td>The spread is the bank’s margin.</td></tr>
  <tr><td><strong>cash FX</strong></td><td>exchange of physical banknotes</td><td>Cash FX is available at the counter.</td></tr>
  <tr><td><strong>base currency / quote currency</strong></td><td>first and second currency in a pair</td><td>In USD/UZS, USD is the base.</td></tr>
</table>

<h2>Useful phrases</h2>
<ul>
  <li>I’d like to buy 500 US dollars, please.</li>
  <li>What’s your sell rate for euros today?</li>
  <li>The rate includes our standard margin.</li>
  <li>Please count the notes carefully at the counter.</li>
  <li>Do you need small denominations?</li>
</ul>

<h2>Dialogue — FX counter</h2>
<p><strong>Customer:</strong> Good morning. I’d like to exchange Uzbek sums for US dollars.<br>
<strong>Officer:</strong> Certainly. How much would you like to buy?<br>
<strong>Customer:</strong> 300 dollars.<br>
<strong>Officer:</strong> Our sell rate today is on the board. May I see your ID? For larger amounts we may need extra checks.<br>
<strong>Customer:</strong> Here you are. Are there any fees?<br>
<strong>Officer:</strong> The rate already includes our spread. Please sign here and count the cash.</p>

<h2>Grammar — Comparatives with rates</h2>
<ul>
  <li>Today’s rate is <strong>higher / lower</strong> than yesterday.</li>
  <li>Cash FX can be <strong>more expensive</strong> than card FX in some cases.</li>
  <li>Please choose the <strong>best</strong> option for your trip.</li>
</ul>

<h2>Reading — Why rates differ</h2>
<p>Banks publish buy and sell rates. They are not identical. The difference — the spread — helps cover operating costs and risk. Rates also change during the day when markets move. A good officer explains the rate clearly and never promises an impossible “special secret rate” by phone from an unknown person.</p>

<h2>Speaking</h2>
<ol>
  <li>Explain buy rate, sell rate, and spread in 5 sentences.</li>
  <li>Role-play buying 200 euros for a trip.</li>
</ol>

<h2>Quick review</h2>
<p>FX · exchange rate · buy/sell rate · spread · currency pair · denomination</p>
""",
            ),
            _lec(
                "Remittances and international transfers",
                "eb-remittance",
                """
<h2>Lesson goal</h2>
<p>Talk about sending money abroad: remittances, wires, fees, and timing.</p>

<h2>Key vocabulary</h2>
<table>
  <tr><th>Term</th><th>Meaning</th></tr>
  <tr><td><strong>remittance</strong></td><td>money sent, often to family across borders</td></tr>
  <tr><td><strong>wire transfer / telegraphic transfer (TT)</strong></td><td>bank-to-bank electronic transfer</td></tr>
  <tr><td><strong>SWIFT</strong></td><td>messaging network banks use for cross-border payments</td></tr>
  <tr><td><strong>BIC / SWIFT code</strong></td><td>bank identifier in international transfers</td></tr>
  <tr><td><strong>IBAN</strong></td><td>international bank account number (where used)</td></tr>
  <tr><td><strong>correspondent bank</strong></td><td>intermediary bank in some routes</td></tr>
  <tr><td><strong>value date</strong></td><td>date when funds are available</td></tr>
  <tr><td><strong>cut-off time</strong></td><td>deadline to send same-day</td></tr>
</table>

<h2>Careful terminology</h2>
<ul>
  <li><strong>Remittance</strong> is common for personal cross-border support.</li>
  <li><strong>Wire / TT</strong> is the bank transfer channel language.</li>
  <li>SWIFT is a <em>messaging</em> system — not “the money itself flying in the sky.”</li>
</ul>

<h2>Dialogue — Sending money home</h2>
<p><strong>Customer:</strong> I need to send money to my parents abroad.<br>
<strong>Officer:</strong> We can help with an international transfer. I’ll need the beneficiary’s full name, account details, and the bank’s SWIFT code.<br>
<strong>Customer:</strong> How long will it take?<br>
<strong>Officer:</strong> It usually takes one to three working days, depending on the corridor and cut-off time. There is a transfer fee, and the exchange rate applies if currencies differ.<br>
<strong>Customer:</strong> Can I track it?<br>
<strong>Officer:</strong> Yes. We’ll give you a reference number.</p>

<h2>Grammar — will / usually / depending on</h2>
<ul>
  <li>It will usually arrive in 1–3 working days.</li>
  <li>The fee depends on the amount and destination.</li>
  <li>If you miss the cut-off time, it will go on the next working day.</li>
</ul>

<h2>Reading — Check twice</h2>
<p>Most remittance problems come from wrong account numbers or incomplete beneficiary names. Officers should read digits back. Customers should keep the receipt and reference. If someone calls and asks you to “redirect the transfer urgently to a new account,” stop — that is a common fraud pattern. Call the bank using the official number.</p>

<h2>Speaking</h2>
<p>Explain to a customer: documents needed, fee, timing, and why the SWIFT code matters (60–90 seconds).</p>
""",
            ),
            _lec(
                "Talking about fees and timing",
                "eb-fx-fees",
                """
<h2>Lesson goal</h2>
<p>Explain transfer costs and timing without confusing the customer.</p>

<h2>Cost language</h2>
<ul>
  <li><strong>transfer fee / commission</strong> — fixed or %-based charge</li>
  <li><strong>FX margin / spread</strong> — built into the exchange rate</li>
  <li><strong>intermediary charges</strong> — possible fees from correspondent banks</li>
  <li><strong>OUR / SHA / BEN</strong> (advanced awareness) — who pays bank charges on some wires (explain only if your bank uses these codes; keep it simple for clients)</li>
</ul>

<h2>Clear explanation script</h2>
<p>“There are two cost parts to understand. First, our transfer fee. Second, the exchange rate if we convert currency. The final amount received can also depend on the receiving bank. I’ll show you an estimate before you confirm.”</p>

<h2>Dialogue — Transparent pricing</h2>
<p><strong>Customer:</strong> Will my family receive the full amount?<br>
<strong>Officer:</strong> I’ll give you an estimate. Our fee is charged here. The receiving bank may apply its own fee. Would you like a smaller amount first as a test transfer?</p>

<h2>Grammar — may / might / can</h2>
<ul>
  <li>The receiving bank <strong>may</strong> charge a fee.</li>
  <li>Arrival <strong>might</strong> take longer on holidays.</li>
  <li>You <strong>can</strong> send a small test amount first.</li>
</ul>

<h2>Speaking &amp; writing</h2>
<ol>
  <li>Write a 6-line SMS explanation of fee + timing.</li>
  <li>Role-play a client who is angry about a slow transfer — stay calm and factual.</li>
</ol>
""",
            ),
        ],
        "practice": {
            "eb-fx-basics": _quiz(
                "eb-q-spread",
                "Spread",
                "FX terminlari.",
                "In FX, the spread is…",
                [
                    "A) the difference between buy and sell rates",
                    "B) a type of mortgage",
                    "C) an HR interview score",
                    "D) a debit card PIN",
                ],
                "A",
            ),
            "eb-remittance": _quiz(
                "eb-q-swift",
                "SWIFT",
                "Xalqaro o‘tkazma.",
                "SWIFT is mainly…",
                [
                    "A) a messaging network used by banks for cross-border payments",
                    "B) a type of credit card plastic",
                    "C) a savings interest formula only",
                    "D) a lunch voucher",
                ],
                "A",
            ),
            "eb-fx-fees": _quiz(
                "eb-q-cutoff",
                "Cut-off time",
                "Muddat.",
                "A cut-off time is…",
                [
                    "A) the deadline to send a transfer the same working day",
                    "B) the bank’s closing party",
                    "C) a KYC stamp colour",
                    "D) a credit limit song",
                ],
                "A",
            ),
        },
        "exercises": [
            _quiz(
                "eb-m5-remittance-def",
                "Remittance",
                "Termin.",
                "A remittance is usually…",
                [
                    "A) money sent across borders, often to family",
                    "B) a type of branch furniture",
                    "C) an expired passport",
                    "D) a local parking fine only",
                ],
                "A",
                difficulty="medium",
            ),
            _quiz(
                "eb-m5-buy-sell",
                "Buy vs sell rate",
                "FX.",
                "If a customer wants to buy USD from the bank, they usually look at the bank’s…",
                [
                    "A) sell rate for USD",
                    "B) HR holiday calendar",
                    "C) ATM temperature",
                    "D) mortgage poem",
                ],
                "A",
            ),
        ],
        "homework": _hw(
            "Module 5 homework — FX & remittances\n"
            "1) Glossary (10 terms): FX, exchange rate, spread, remittance, SWIFT, BIC, IBAN, wire, value date, cut-off.\n"
            "2) Dialogue (14 lines): customer sends money abroad; officer explains fee + timing.\n"
            "3) Speaking: 60-second explanation of buy vs sell rate.\n"
            "4) Write a polite email confirming a transfer reference and expected value date."
        ),
    },
    {
        "order": 6,
        "title": "Biznes va trade finance (SME & trade)",
        "slug": "eb-trade-sme",
        "description": "SME banking, working capital, letters of credit and guarantees — simplified.",
        "lectures": [
            _lec(
                "SME and corporate banking basics",
                "eb-sme-basics",
                """
<h2>Lesson goal</h2>
<p>Describe how banks serve small businesses (SME) and larger companies in simple English.</p>

<h2>Key vocabulary</h2>
<table>
  <tr><th>Term</th><th>Meaning</th></tr>
  <tr><td><strong>SME</strong></td><td>small and medium-sized enterprise</td></tr>
  <tr><td><strong>corporate client</strong></td><td>company customer (often larger)</td></tr>
  <tr><td><strong>business account</strong></td><td>account for company operations</td></tr>
  <tr><td><strong>working capital</strong></td><td>money for day-to-day business needs</td></tr>
  <tr><td><strong>turnover / revenue</strong></td><td>sales over a period</td></tr>
  <tr><td><strong>cash flow</strong></td><td>money moving in and out of the business</td></tr>
  <tr><td><strong>relationship manager (RM)</strong></td><td>banker who manages company clients</td></tr>
  <tr><td><strong>merchant acquiring</strong></td><td>accepting card payments for shops</td></tr>
</table>

<h2>Retail vs business (quick contrast)</h2>
<ul>
  <li><strong>Retail:</strong> individuals — salary, cards, consumer loans.</li>
  <li><strong>SME / corporate:</strong> companies — payroll, suppliers, trade, larger credit lines.</li>
</ul>

<h2>Dialogue — First business meeting</h2>
<p><strong>RM:</strong> Thanks for visiting. Tell me about your business model in two minutes.<br>
<strong>Owner:</strong> We import spare parts and sell to local garages.<br>
<strong>RM:</strong> Understood. You may need a business current account, FX for suppliers, and possibly a working-capital facility. We’ll start with KYC for the company and beneficial owners.</p>

<h2>Grammar — may need / might help</h2>
<ul>
  <li>You may need a business account for supplier payments.</li>
  <li>A card acquiring service might help your shop.</li>
  <li>We should review your cash flow before a loan decision.</li>
</ul>

<h2>Reading — Listen first</h2>
<p>Good business bankers listen before selling. A bakery and an IT firm need different products. Turnover, seasonality, and supplier terms matter. English helps when contracts, invoices, and shipping documents use international words.</p>

<h2>Speaking</h2>
<ol>
  <li>Explain SME in one sentence, then give three typical bank products.</li>
  <li>Ask five discovery questions to a shop owner.</li>
</ol>
""",
            ),
            _lec(
                "Letters of credit — simple view",
                "eb-letter-of-credit",
                """
<h2>Lesson goal</h2>
<p>Explain a letter of credit (LC) at a basic level: who is who, and why traders use it.</p>

<h2>Key vocabulary</h2>
<ul>
  <li><strong>letter of credit (LC) / documentary credit</strong> — bank undertakes to pay if documents comply</li>
  <li><strong>applicant</strong> — usually the buyer who requests the LC</li>
  <li><strong>beneficiary</strong> — usually the seller who gets paid</li>
  <li><strong>issuing bank</strong> — opens the LC for the applicant</li>
  <li><strong>advising / confirming bank</strong> — banks in the seller’s country (roles vary)</li>
  <li><strong>shipping documents</strong> — papers that prove shipment terms</li>
  <li><strong>complying presentation</strong> — documents match LC terms</li>
</ul>

<h2>Simple story</h2>
<p>A buyer in Country A wants goods from a seller in Country B. They do not fully trust each other yet. The buyer’s bank issues an LC. If the seller presents the correct documents on time, the bank pays according to the LC. The focus is documents and terms — not casual promises.</p>

<h2>Useful phrases</h2>
<ul>
  <li>We can issue a letter of credit for your import contract.</li>
  <li>Payment depends on a complying presentation of documents.</li>
  <li>Please check the LC terms carefully before shipment.</li>
</ul>

<h2>Dialogue</h2>
<p><strong>Importer:</strong> Our supplier wants an LC, not open account.<br>
<strong>Trade officer:</strong> That’s common in new trade relationships. We’ll need the contract, company documents, and details of goods and shipment.<br>
<strong>Importer:</strong> Is an LC the same as a loan?<br>
<strong>Trade officer:</strong> It’s a payment undertaking with conditions. It can also tie up your credit line, so we’ll explain limits and fees clearly.</p>

<h2>Careful!</h2>
<p>This lesson is workplace English. Real LC work follows bank policy and international practice (e.g. ICC rules). Escalate details to trade specialists.</p>

<h2>Speaking</h2>
<p>Explain LC to a non-banker in 6 short sentences using applicant, beneficiary, issuing bank, documents.</p>
""",
            ),
            _lec(
                "Bank guarantees — simple view",
                "eb-guarantees",
                """
<h2>Lesson goal</h2>
<p>Describe a bank guarantee in plain English and contrast it lightly with an LC.</p>

<h2>Key vocabulary</h2>
<ul>
  <li><strong>bank guarantee</strong> — bank promise to pay if the customer fails a contract duty</li>
  <li><strong>bid bond</strong> — guarantee often used in tenders</li>
  <li><strong>performance guarantee</strong> — supports completing a contract</li>
  <li><strong>advance payment guarantee</strong> — protects a buyer’s advance payment</li>
  <li><strong>beneficiary (of a guarantee)</strong> — party protected by the guarantee</li>
</ul>

<h2>LC vs guarantee (very simple)</h2>
<table>
  <tr><th>Letter of credit</th><th>Bank guarantee</th></tr>
  <tr><td>Often used to pay for trade against documents</td><td>Often used as security if someone defaults on an obligation</td></tr>
  <tr><td>Payment process tied to document terms</td><td>Claim process tied to guarantee wording</td></tr>
</table>

<h2>Dialogue</h2>
<p><strong>Contractor:</strong> The project owner asks for a performance guarantee.<br>
<strong>Officer:</strong> We can review that. We’ll need the contract and your company limits. A guarantee is a serious contingent liability for the bank and for you.<br>
<strong>Contractor:</strong> Contingent?<br>
<strong>Officer:</strong> It becomes a real payment if a valid claim is made under the guarantee terms.</p>

<h2>Reading</h2>
<p>Guarantees help business trust. They are not “free paper.” Banks check the client’s capacity and collateral. Staff should never improvise legal wording — use approved templates and specialists.</p>

<h2>Speaking</h2>
<ol>
  <li>Define bank guarantee in 3 sentences.</li>
  <li>Give one example: performance guarantee for a construction contract.</li>
</ol>
""",
            ),
        ],
        "practice": {
            "eb-sme-basics": _quiz(
                "eb-q-sme",
                "SME",
                "Biznes banking.",
                "SME means…",
                [
                    "A) small and medium-sized enterprise",
                    "B) super magic exchange",
                    "C) salary monthly estimate only",
                    "D) safe metal elevator",
                ],
                "A",
            ),
            "eb-letter-of-credit": _quiz(
                "eb-q-lc-applicant",
                "LC applicant",
                "Trade finance.",
                "In a typical import LC, the applicant is usually…",
                [
                    "A) the buyer who asks the bank to issue the LC",
                    "B) the ATM technician",
                    "C) the lunch manager",
                    "D) the debit card plastic",
                ],
                "A",
            ),
            "eb-guarantees": _quiz(
                "eb-q-performance-guarantee",
                "Performance guarantee",
                "Guarantee.",
                "A performance guarantee mainly supports…",
                [
                    "A) completing a contract obligation",
                    "B) choosing card colours",
                    "C) writing poems in HR",
                    "D) deleting KYC files",
                ],
                "A",
            ),
        },
        "exercises": [
            _quiz(
                "eb-m6-working-capital",
                "Working capital",
                "SME.",
                "Working capital is money for…",
                [
                    "A) day-to-day business operations",
                    "B) buying the Central Bank building",
                    "C) personal holiday only always",
                    "D) PIN decoration",
                ],
                "A",
                difficulty="medium",
            ),
            _quiz(
                "eb-m6-lc-docs",
                "LC documents",
                "Trade.",
                "Under an LC, payment usually depends on…",
                [
                    "A) a complying presentation of required documents",
                    "B) a friendly SMS only",
                    "C) the teller’s favourite colour",
                    "D) deleting the contract",
                ],
                "A",
                difficulty="medium",
            ),
        ],
        "homework": _hw(
            "Module 6 homework — SME & trade\n"
            "1) Glossary: SME, working capital, cash flow, LC, applicant, beneficiary, issuing bank, bank guarantee, performance guarantee.\n"
            "2) Write a 120-word explanation of LC for a shop owner (simple English).\n"
            "3) Dialogue (12 lines): RM discovers needs of an importer.\n"
            "4) Speaking: contrast LC and guarantee in 45 seconds."
        ),
    },
    {
        "order": 7,
        "title": "Raqamli banking va firibgarlik (Digital & fraud)",
        "slug": "eb-digital-fraud",
        "description": "Mobile/internet banking, OTP, phishing, and fraud awareness English.",
        "lectures": [
            _lec(
                "Digital banking channels",
                "eb-digital-channels",
                """
<h2>Lesson goal</h2>
<p>Name digital channels and guide customers to safe self-service English phrases.</p>

<h2>Key vocabulary</h2>
<table>
  <tr><th>Term</th><th>Meaning</th></tr>
  <tr><td><strong>internet banking / online banking</strong></td><td>bank services via website</td></tr>
  <tr><td><strong>mobile banking app</strong></td><td>bank services via smartphone</td></tr>
  <tr><td><strong>OTP (one-time password)</strong></td><td>single-use code for confirmation</td></tr>
  <tr><td><strong>two-factor authentication (2FA)</strong></td><td>password + second factor</td></tr>
  <tr><td><strong>push notification</strong></td><td>alert on the phone</td></tr>
  <tr><td><strong>biometric login</strong></td><td>fingerprint / face ID</td></tr>
  <tr><td><strong>card controls</strong></td><td>limits, freeze, region settings in-app</td></tr>
  <tr><td><strong>e-wallet</strong></td><td>digital wallet for payments</td></tr>
</table>

<h2>Useful phrases</h2>
<ul>
  <li>You can reset your password in the mobile app.</li>
  <li>Never share your OTP with anyone — not even “bank staff” on the phone.</li>
  <li>Please update the app to the latest version.</li>
  <li>You can freeze the card in Card controls.</li>
</ul>

<h2>Dialogue — First app login</h2>
<p><strong>Customer:</strong> I can’t log in to the app.<br>
<strong>Officer:</strong> I’m sorry about that. Are you using the official app from the store? Let’s check your phone number for SMS OTP… For security, I won’t ask for the OTP itself. Enter it only in the app.</p>

<h2>Grammar — Imperatives for digital safety</h2>
<ul>
  <li>Download only the official app.</li>
  <li>Don’t share OTP codes.</li>
  <li>Enable 2FA if available.</li>
</ul>

<h2>Speaking</h2>
<p>Teach a parent how to freeze a card in the app — 5 clear steps in English.</p>
""",
            ),
            _lec(
                "Phishing and social engineering",
                "eb-phishing",
                """
<h2>Lesson goal</h2>
<p>Recognise common fraud stories and warn customers in calm, precise English.</p>

<h2>Key vocabulary</h2>
<ul>
  <li><strong>phishing</strong> — fake emails/sites to steal data</li>
  <li><strong>smishing</strong> — phishing by SMS</li>
  <li><strong>vishing</strong> — phishing by voice call</li>
  <li><strong>social engineering</strong> — manipulating people to give access/data</li>
  <li><strong>malware</strong> — harmful software</li>
  <li><strong>scam / fraud</strong> — criminal deception for money</li>
  <li><strong>impersonation</strong> — pretending to be the bank/police</li>
</ul>

<h2>Red-flag lines (teach customers)</h2>
<ul>
  <li>“Give me your OTP now or your account will close in 10 minutes.”</li>
  <li>“Install this remote-access app so I can help you.”</li>
  <li>“Transfer to a ‘safe account’ immediately.”</li>
</ul>
<p>Real banks do not ask for full passwords or OTPs on a cold call.</p>

<h2>Dialogue — Warning call</h2>
<p><strong>Customer:</strong> Someone called and said they’re from the bank. They want my OTP.<br>
<strong>Officer:</strong> Thank you for checking. Please hang up. We never ask for OTP on a call. I’ll help you review recent transactions and reset access if needed.</p>

<h2>Reading — Speed is the enemy</h2>
<p>Fraudsters create panic and urgency. Good staff slow the conversation down: verify via official channels, don’t click strange links, and report suspicious messages. English phrases should be short and memorable for customers.</p>

<h2>Speaking</h2>
<ol>
  <li>Give a 40-second anti-phishing briefing.</li>
  <li>Role-play calming a scared customer after a scam attempt.</li>
</ol>
""",
            ),
            _lec(
                "Fraud cases at the branch",
                "eb-fraud-cases",
                """
<h2>Lesson goal</h2>
<p>Describe common fraud case types and escalation language for branch staff.</p>

<h2>Case types (awareness level)</h2>
<ul>
  <li><strong>account takeover</strong> — criminal controls the customer’s access</li>
  <li><strong>identity theft</strong> — using stolen ID details</li>
  <li><strong>authorised push payment scam</strong> — customer is tricked into sending money</li>
  <li><strong>card-not-present fraud</strong> — online misuse of card data</li>
  <li><strong>internal fraud</strong> — misconduct by staff (zero tolerance; escalate)</li>
</ul>

<h2>What to say</h2>
<ul>
  <li>Please don’t transfer money to a ‘safe account’ on someone’s instructions.</li>
  <li>I’ll escalate this to our fraud team / secure channel.</li>
  <li>We’ll block the card and review the transactions.</li>
  <li>Can you tell me the exact time of the call/SMS?</li>
</ul>

<h2>Dialogue — Suspected scam in progress</h2>
<p><strong>Customer:</strong> I’m on the phone with a man. He says I must transfer now.<br>
<strong>Officer:</strong> Please pause the transfer. Ask the caller to hold — or hang up. We’ll call you back on the official process. If this is a scam, speed helps them, not you.</p>

<h2>Grammar — should / mustn’t / need to</h2>
<ul>
  <li>You should verify using official numbers.</li>
  <li>You mustn’t share OTP codes.</li>
  <li>We need to escalate unusual cases quickly.</li>
</ul>

<h2>Speaking &amp; writing</h2>
<ol>
  <li>Write a 8-line branch checklist for suspected phishing.</li>
  <li>Present one fraud case study in 60 seconds (problem → action → result).</li>
</ol>
""",
            ),
        ],
        "practice": {
            "eb-digital-channels": _quiz(
                "eb-q-otp",
                "OTP",
                "Digital banking.",
                "An OTP is…",
                [
                    "A) a one-time password/code for confirmation",
                    "B) a type of mortgage collateral",
                    "C) an HR holiday form",
                    "D) a branch coffee order",
                ],
                "A",
            ),
            "eb-phishing": _quiz(
                "eb-q-phishing",
                "Phishing",
                "Fraud.",
                "Phishing is…",
                [
                    "A) fake messages/sites used to steal data",
                    "B) a savings interest bonus",
                    "C) a trade LC template",
                    "D) a friendly ATM upgrade",
                ],
                "A",
            ),
            "eb-fraud-cases": _quiz(
                "eb-q-safe-account",
                "Safe account scam",
                "Fraud awareness.",
                "If someone tells a customer to transfer to a ‘safe account’, staff should…",
                [
                    "A) stop and verify via official channels — it is a common scam pattern",
                    "B) help transfer faster without checks",
                    "C) share the OTP for them",
                    "D) ignore the customer",
                ],
                "A",
            ),
        },
        "exercises": [
            _quiz(
                "eb-m7-2fa",
                "2FA",
                "Security.",
                "Two-factor authentication means…",
                [
                    "A) password plus a second factor (e.g. OTP/biometric)",
                    "B) two mortgages at once",
                    "C) two lunches per shift",
                    "D) two PINs written on the card",
                ],
                "A",
                difficulty="medium",
            ),
            _quiz(
                "eb-m7-vishing",
                "Vishing",
                "Fraud terms.",
                "Vishing is fraud by…",
                [
                    "A) voice call",
                    "B) only paper letters from 1890",
                    "C) decorating the branch",
                    "D) printing more cash",
                ],
                "A",
                difficulty="medium",
            ),
        ],
        "homework": _hw(
            "Module 7 homework — Digital & fraud\n"
            "1) Glossary: OTP, 2FA, phishing, smishing, vishing, malware, account takeover, card controls.\n"
            "2) Write a customer warning leaflet (120 words) in simple English.\n"
            "3) Dialogue: customer received a fake bank SMS — you guide next steps.\n"
            "4) Speaking: 60-second digital safety briefing for new interns."
        ),
    },
]


def build_extra_english_banking_modules():
    return EXTRA_MODULES
