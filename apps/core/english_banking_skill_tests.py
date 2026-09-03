"""
English for Banking — skill tests per module (quiz, 4 options).
English vocabulary/options stay in English; titles/descriptions can be Uzbek for UI.
"""


def _q(num: int, title: str, task: str, options: list[str], answer: str, editorial: str, difficulty: str = "easy"):
    assert answer in "ABCD"
    assert len(options) == 4
    return {
        "num": num,
        "title": title,
        "description": "Modul bilim testi. To‘g‘ri inglizcha javobni tanlang.",
        "task": task,
        "kind": "quiz",
        "difficulty": difficulty,
        "is_skill_test": True,
        "quiz_options": options,
        "hints": [
            "Darsdagi bank so‘zlarini eslang.",
            "Noto‘g‘ri variantlarni chiqarib tashlang.",
        ],
        "editorial": editorial,
        "columns": ["javob"],
        "rows": [[answer]],
    }


MODULE_SKILL_TESTS: dict[str, list[dict]] = {
    "eb-bank-basics": [
        _q(1, "Branch", "A branch is…", [
            "A) a local bank office", "B) a credit card chip", "C) an interest formula", "D) a passport type",
        ], "A", "Branch = local office."),
        _q(2, "Teller", "A teller usually…", [
            "A) serves customers at the counter", "B) writes national law", "C) prints money at home", "D) sets FX policy alone",
        ], "A", "Teller = counter service."),
        _q(3, "HR", "HR mainly…", [
            "A) hires and supports staff", "B) approves every mortgage alone", "C) builds ATMs", "D) deletes KYC forever",
        ], "A", "HR = people."),
        _q(4, "Greeting", "Best customer greeting:", [
            "A) How can I help you?", "B) Give money!", "C) You again?", "D) Password now!",
        ], "A", "Offer help politely."),
        _q(5, "Polite request", "Polite request:", [
            "A) Could you show me your ID, please?", "B) ID! Fast!", "C) No talk.", "D) Leave documents anywhere.",
        ], "A", "Could you… please?"),
        _q(6, "Compliance", "Compliance focuses on…", [
            "A) following laws and bank rules", "B) painting walls", "C) lunch menus", "D) card colours only",
        ], "A", "Compliance = rules."),
        _q(7, "Present simple", "Correct routine sentence:", [
            "A) The bank opens at 9 a.m.", "B) The bank opening at 9.", "C) Bank open yesterday always.", "D) Opens the bank never clock.",
        ], "A", "Present simple for routines."),
        _q(8, "Customer", "A customer is…", [
            "A) a person who uses bank services", "B) only the CEO", "C) an ATM cable", "D) a loan formula",
        ], "A", "Customer = client."),
    ],
    "eb-accounts": [
        _q(1, "Savings", "A savings account is for…", [
            "A) keeping money and earning interest", "B) printing cards only", "C) HR interviews", "D) closing branches",
        ], "A", "Savings = store + interest."),
        _q(2, "Withdraw", "To withdraw means…", [
            "A) take money out", "B) put money in", "C) hire staff", "D) raise the policy rate",
        ], "A", "Withdraw = take out."),
        _q(3, "Deposit", "To deposit money means…", [
            "A) put money into an account", "B) delete an account", "C) lose a card", "D) refuse KYC",
        ], "A", "Deposit = put in."),
        _q(4, "Balance", "Balance means…", [
            "A) money available in the account", "B) the manager’s age", "C) ATM colour", "D) email signature",
        ], "A", "Balance = available funds."),
        _q(5, "I’d like to", "Best polite wish:", [
            "A) I’d like to open an account, please.", "B) Account open now!", "C) Give savings!", "D) Balance me immediately forever.",
        ], "A", "I’d like to…"),
        _q(6, "Statement", "A statement lists…", [
            "A) transactions on the account", "B) staff birthdays only", "C) building floors", "D) PIN secrets",
        ], "A", "Statement = transaction list."),
        _q(7, "Current account", "A current/checking account is mainly for…", [
            "A) everyday payments", "B) buying the bank building", "C) writing poems", "D) hiding ID",
        ], "A", "Everyday use."),
        _q(8, "Past simple", "Correct past sentence:", [
            "A) She deposited money yesterday.", "B) She deposit money yesterday.", "C) She depositing yesterday money.", "D) Yesterday deposit she.",
        ], "A", "Past simple -ed.", "medium"),
    ],
    "eb-cards-payments": [
        _q(1, "Debit", "A debit card uses…", [
            "A) money in your account", "B) unlimited free loans forever", "C) HR budgets only", "D) gold from the vault for fun",
        ], "A", "Debit = your money."),
        _q(2, "Credit card", "A credit card…", [
            "A) borrows from the bank up to a limit", "B) never needs repayment", "C) is only for HR", "D) deletes interest",
        ], "A", "Credit = borrow now."),
        _q(3, "Beneficiary", "Beneficiary means…", [
            "A) person who receives the money", "B) the ATM screen", "C) the fee percentage song", "D) a branch plant",
        ], "A", "Receiver of funds."),
        _q(4, "PIN", "Correct PIN advice:", [
            "A) Keep it secret and cover the keypad", "B) Share with friends", "C) Write it on the card", "D) Post it online",
        ], "A", "PIN safety."),
        _q(5, "Fee", "A transfer fee is…", [
            "A) a charge for the service", "B) free lunch", "C) a type of passport", "D) an HR bonus always",
        ], "A", "Fee = charge."),
        _q(6, "Lost card", "If a card is lost, you should…", [
            "A) report it to the bank immediately", "B) wait one year", "C) share the PIN", "D) ignore SMS alerts forever",
        ], "A", "Report immediately."),
        _q(7, "Credit limit", "Credit limit is…", [
            "A) the maximum you can borrow on the card", "B) the branch opening hour", "C) a savings gift", "D) KYC ink colour",
        ], "A", "Max borrow amount."),
        _q(8, "Imperative", "Correct safety instruction:", [
            "A) Don’t share your PIN.", "B) Don’t sharing your PIN.", "C) Not share you PIN never do.", "D) PIN sharing always good.",
        ], "A", "Imperative don’t + verb.", "medium"),
    ],
    "eb-loans-credit": [
        _q(1, "Borrow", "Correct sentence:", [
            "A) I want to borrow money from the bank.", "B) I want to lend money from the bank.", "C) The loan borrows me.", "D) Interest borrows the house.",
        ], "A", "Client borrows."),
        _q(2, "Lender", "The lender is…", [
            "A) the bank that gives the loan", "B) only the ATM", "C) the customer’s neighbour", "D) a debit PIN",
        ], "A", "Bank lends."),
        _q(3, "Interest rate", "Interest rate is…", [
            "A) the % charged for borrowing", "B) the customer’s nickname", "C) the card colour", "D) lunch time",
        ], "A", "% for credit."),
        _q(4, "Mortgage", "A mortgage is…", [
            "A) a loan to buy property", "B) a type of email", "C) an HR form only", "D) a free gift card",
        ], "A", "Property loan."),
        _q(5, "Collateral", "Collateral is…", [
            "A) an asset given as guarantee", "B) a greeting", "C) a debit sticker", "D) a meeting snack",
        ], "A", "Security for loan."),
        _q(6, "Overdue", "Overdue means…", [
            "A) late", "B) early", "C) free", "D) imaginary",
        ], "A", "Late payment."),
        _q(7, "Installment", "An installment is…", [
            "A) a regular repayment amount", "B) a branch plant", "C) a passport photo", "D) a PIN joke",
        ], "A", "Scheduled repayment."),
        _q(8, "First conditional", "Correct sentence:", [
            "A) If you pay today, you will avoid a late fee.", "B) If you will pay today, you avoid a late fee.", "C) If pay you, fee avoid.", "D) If you paying, fee gone maybe never.",
        ], "A", "If + present, will + verb.", "medium"),
    ],
    "eb-hr-banking": [
        _q(1, "Credit analyst", "A credit analyst…", [
            "A) reviews loan applications", "B) paints ATMs", "C) sells lunch", "D) invents PINs for fun",
        ], "A", "Analyses credit."),
        _q(2, "Present perfect", "Correct experience sentence:", [
            "A) I have worked in a bank for one year.", "B) I work in a bank since one year ago yesterday.", "C) I am work bank year.", "D) Working I bank have.",
        ], "A", "Have + past participle."),
        _q(3, "Responsible", "Correct phrase:", [
            "A) I’m responsible for checking documents.", "B) I’m responsible to checking forever bad.", "C) I responsible documents.", "D) Documents responsible me.",
        ], "A", "Responsible for + -ing/noun."),
        _q(4, "Strengths", "Professional strength answer:", [
            "A) I’m organised and polite with customers.", "B) I hate teamwork.", "C) I sleep in meetings.", "D) I lose documents often.",
        ], "A", "Positive workplace trait."),
        _q(5, "Intern", "An intern is usually…", [
            "A) a trainee gaining experience", "B) the Central Bank governor always", "C) an ATM model", "D) a credit limit",
        ], "A", "Trainee."),
        _q(6, "Why banking", "Good interview idea:", [
            "A) I’m interested in finance and helping customers.", "B) I want free unlimited cash.", "C) I dislike people.", "D) I refuse all rules.",
        ], "A", "Motivation."),
        _q(7, "Risk officer", "A risk officer helps…", [
            "A) identify and control risks", "B) cook for staff", "C) design logos only", "D) hide overdue loans",
        ], "A", "Risk control."),
        _q(8, "Team player", "A team player…", [
            "A) works well with colleagues", "B) never shares information when needed", "C) insults clients", "D) ignores deadlines always",
        ], "A", "Cooperation.", "medium"),
    ],
    "eb-customer-service": [
        _q(1, "Apology", "Best complaint start:", [
            "A) I’m sorry for the inconvenience.", "B) That’s your problem.", "C) We are never wrong.", "D) Call later never.",
        ], "A", "Empathy first."),
        _q(2, "On hold", "On hold means…", [
            "A) please wait on the line", "B) close the account", "C) raise rates now", "D) visit HR for lunch",
        ], "A", "Short wait."),
        _q(3, "Escalate", "Escalate means…", [
            "A) pass to a higher level", "B) delete the ticket", "C) shout at the client", "D) change the PIN randomly",
        ], "A", "Higher level."),
        _q(4, "Double charge", "Charged twice means…", [
            "A) the amount was taken two times", "B) the card is gold", "C) KYC is finished", "D) interest is zero forever",
        ], "A", "Two charges."),
        _q(5, "Verify", "Verify details means…", [
            "A) check that information is correct", "B) invent new data", "C) ignore security", "D) share secrets publicly",
        ], "A", "Check accuracy."),
        _q(6, "Concern", "I understand your concern means…", [
            "A) I see why you are worried", "B) I refuse to listen", "C) Please leave forever", "D) No help today",
        ], "A", "Empathy."),
        _q(7, "Hotline", "A bank hotline is…", [
            "A) a phone service for customers", "B) a type of mortgage poem", "C) an HR cake", "D) a debit sticker",
        ], "A", "Phone support."),
        _q(8, "Next step", "Good complaint structure ends with…", [
            "A) a clear next step", "B) silence forever", "C) insults", "D) random PINs",
        ], "A", "Offer action.", "medium"),
    ],
    "eb-compliance-kyc": [
        _q(1, "KYC", "KYC means…", [
            "A) Know Your Customer", "B) Keep Your Cash", "C) Key Yellow Card", "D) Kill Your Credit",
        ], "A", "Know Your Customer."),
        _q(2, "AML", "AML is about…", [
            "A) anti-money laundering", "B) art marketing logos", "C) apple menu lists", "D) automatic music lunch",
        ], "A", "Anti-Money Laundering."),
        _q(3, "Proof of address", "Proof of address shows…", [
            "A) where the client lives", "B) the PIN", "C) the lunch menu", "D) card design",
        ], "A", "Address evidence."),
        _q(4, "Suspicious", "Suspicious transaction should be…", [
            "A) flagged/escalated to Compliance", "B) ignored always", "C) posted online", "D) celebrated",
        ], "A", "Escalate unusual activity."),
        _q(5, "ID", "An identity document is often…", [
            "A) a passport or national ID", "B) a shopping receipt for bread only", "C) a meme", "D) a random photo of a cat",
        ], "A", "Official ID."),
        _q(6, "Polite KYC", "Polite KYC request:", [
            "A) Could you provide your passport, please?", "B) Papers! Now!", "C) No documents needed ever.", "D) Hide your name.",
        ], "A", "Polite could you…"),
        _q(7, "Beneficial owner", "Beneficial owner is…", [
            "A) the person who ultimately owns/controls a company", "B) the ATM cleaner only", "C) a debit sticker", "D) lunch manager",
        ], "A", "Ultimate owner.", "medium"),
        _q(8, "Why KYC", "Banks need KYC mainly to…", [
            "A) verify clients and reduce illegal risk", "B) decorate offices", "C) choose card colours", "D) avoid helping customers",
        ], "A", "Identity + risk."),
    ],
    "eb-emails-meetings": [
        _q(1, "Email purpose", "A good email should…", [
            "A) state the purpose clearly", "B) hide the request", "C) insult the reader", "D) use only emojis",
        ], "A", "Clear purpose."),
        _q(2, "Closing", "Professional closing:", [
            "A) Kind regards,", "B) Bye loser,", "C) Give money,", "D) PIN forever,",
        ], "A", "Kind regards."),
        _q(3, "Summarise", "Let’s summarise next steps is for…", [
            "A) ending with clear actions", "B) deleting the agenda", "C) closing accounts randomly", "D) changing PINs",
        ], "A", "Action summary."),
        _q(4, "Opinion", "Natural meeting phrase:", [
            "A) In my opinion, we should verify income.", "B) Opinion my scream verify.", "C) I opinioning.", "D) Verify shout now.",
        ], "A", "In my opinion…"),
        _q(5, "Product pitch", "A short pitch should include…", [
            "A) who it is for and the main benefit", "B) only jokes", "C) private PINs", "D) no benefit at all",
        ], "A", "Audience + benefit."),
        _q(6, "Repeat", "Could you repeat that, please? is used when…", [
            "A) you didn’t catch the words", "B) you want to close the bank", "C) you refuse KYC", "D) you change interest alone",
        ], "A", "Clarification."),
        _q(7, "Shall we start", "Shall we start? is used to…", [
            "A) begin a meeting politely", "B) end employment", "C) delete emails", "D) freeze cards forever",
        ], "A", "Start meeting."),
        _q(8, "Call to action", "Visit our branch to open it today is a…", [
            "A) call to action", "B) KYC crime", "C) PIN leak", "D) random insult",
        ], "A", "CTA.", "medium"),
    ],
    "eb-fx-remittance": [
        _q(1, "Exchange rate", "An exchange rate is…", [
            "A) the price of one currency in another", "B) a type of debit PIN", "C) an HR form", "D) a lunch voucher",
        ], "A", "FX price."),
        _q(2, "Spread", "The FX spread is…", [
            "A) the difference between buy and sell rates", "B) a mortgage room", "C) a branch plant", "D) a free gift",
        ], "A", "Buy/sell difference."),
        _q(3, "Remittance", "A remittance is usually…", [
            "A) money sent across borders, often to family", "B) a savings stamp", "C) a card colour", "D) a teller chair",
        ], "A", "Cross-border support money."),
        _q(4, "SWIFT", "SWIFT is mainly…", [
            "A) a messaging network for banks", "B) a plastic card brand only", "C) a type of collateral", "D) a phishing app",
        ], "A", "Bank messaging network."),
        _q(5, "Sell rate", "If you buy USD from the bank, you usually use the bank’s…", [
            "A) sell rate for USD", "B) HR calendar", "C) ATM temperature", "D) poetry book",
        ], "A", "Customer buys → bank sells."),
        _q(6, "Cut-off", "Cut-off time means…", [
            "A) deadline for same-working-day processing", "B) lunch break forever", "C) PIN expiry only", "D) branch decoration hour",
        ], "A", "Same-day deadline."),
        _q(7, "BIC", "A BIC/SWIFT code identifies…", [
            "A) a bank in international transfers", "B) a customer’s favourite colour", "C) an OTP snack", "D) a local bus stop",
        ], "A", "Bank identifier."),
        _q(8, "Value date", "Value date is roughly…", [
            "A) when funds are available", "B) the teller’s birthday", "C) a phishing link", "D) card plastic thickness",
        ], "A", "Availability date.", "medium"),
    ],
    "eb-trade-sme": [
        _q(1, "SME", "SME means…", [
            "A) small and medium-sized enterprise", "B) super monthly exchange", "C) safe metal elevator", "D) salary magic event",
        ], "A", "Small/medium business."),
        _q(2, "Working capital", "Working capital is for…", [
            "A) day-to-day business needs", "B) buying the moon", "C) PIN art", "D) only holidays",
        ], "A", "Operating money."),
        _q(3, "LC", "A letter of credit is…", [
            "A) a bank payment undertaking if documents comply", "B) a birthday card", "C) an ATM sticker", "D) a free lunch",
        ], "A", "Documentary credit idea."),
        _q(4, "Applicant", "In a typical import LC, the applicant is usually…", [
            "A) the buyer", "B) the ATM", "C) the cafeteria", "D) the debit chip",
        ], "A", "Buyer requests LC."),
        _q(5, "Beneficiary LC", "The LC beneficiary is usually…", [
            "A) the seller", "B) the parking guard", "C) the PIN printer", "D) the coffee machine",
        ], "A", "Seller side."),
        _q(6, "Guarantee", "A bank guarantee often…", [
            "A) supports a contract obligation if the client fails", "B) deletes KYC", "C) paints the branch", "D) creates OTPs for fun",
        ], "A", "Security for obligation."),
        _q(7, "Performance guarantee", "A performance guarantee mainly supports…", [
            "A) completing a contract", "B) choosing emojis", "C) hiding fees forever", "D) skipping onboarding",
        ], "A", "Contract performance."),
        _q(8, "Cash flow", "Cash flow means…", [
            "A) money moving in and out of the business", "B) only paper cash in a museum", "C) a type of phishing", "D) a card design",
        ], "A", "In/out money.", "medium"),
    ],
    "eb-digital-fraud": [
        _q(1, "OTP", "An OTP is…", [
            "A) a one-time password/code", "B) a mortgage type", "C) an LC stamp", "D) a teller hat",
        ], "A", "One-time code."),
        _q(2, "Phishing", "Phishing is…", [
            "A) fake messages/sites to steal data", "B) a savings bonus", "C) a trade guarantee", "D) branch music",
        ], "A", "Data-stealing scam."),
        _q(3, "2FA", "Two-factor authentication means…", [
            "A) password plus a second factor", "B) two free loans", "C) two PINs on the card", "D) two lunches",
        ], "A", "Extra security factor."),
        _q(4, "Vishing", "Vishing is fraud by…", [
            "A) voice call", "B) only paper from 1800", "C) ATM painting", "D) printing cash",
        ], "A", "Voice phishing."),
        _q(5, "Safe account", "‘Transfer to a safe account now’ is usually…", [
            "A) a common scam pattern — stop and verify", "B) official always", "C) required by SWIFT law for coffee", "D) an HR rule",
        ], "A", "Scam urgency."),
        _q(6, "App advice", "Best advice for OTP:", [
            "A) never share OTP with anyone on a call", "B) read OTP aloud to strangers", "C) write OTP on the card", "D) post OTP online",
        ], "A", "OTP secrecy."),
        _q(7, "Card controls", "Card controls in an app can…", [
            "A) freeze the card or set limits", "B) change national law", "C) delete Compliance", "D) invent interest alone",
        ], "A", "In-app card safety."),
        _q(8, "Smishing", "Smishing is phishing by…", [
            "A) SMS", "B) only orchestra music", "C) paper planes", "D) branch flowers",
        ], "A", "SMS phishing.", "medium"),
    ],
}


def skill_tests_for_module(module_slug: str) -> list[dict]:
    items = MODULE_SKILL_TESTS.get(module_slug, [])
    result = []
    for item in items:
        data = dict(item)
        num = data.pop("num")
        data["slug"] = f"bt-{module_slug}-{num:02d}"
        result.append(data)
    return result
