"""
English for IT — pre-intermediate–intermediate (A2–B1/B2) ESP track.

Learning English stays in English (vocabulary, dialogues, reading).
UI instructions use Uzbek so |loc can translate the “second side”.
IT terms follow standard international English usage.
"""

COURSE_DESCRIPTION = (
    "IT uchun ingliz tili — workplace, intervyu va akademik darslar (17 modul). "
    "Hardware, software/OS, networking, programming, databases, web, cloud/DevOps, "
    "cybersecurity, QA, Agile, tech support, documentation, team communication, email/career. "
    "Grammatika, so‘z boyligi, dialoglar, puzzle va bilim testlari bilan."
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
        "editorial": editorial or "To‘g‘ri javob darsdagi IT terminiga mos keladi.",
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
        "title": 'IT asoslari (IT workplace basics)',
        "slug": 'eit-it-basics',
        "description": 'IT workplace, rollar, ofis va remote ish uchun asosiy so‘zlar.',
        "lectures": [
            _lec(
                'Welcome to IT English',
                'eit-welcome-it',
                """
<h2>Lesson goal</h2>
  <p>At the end of this lesson you can introduce yourself in an IT team, name common workplace tools, and describe a simple workday in clear A2–B1 English.</p>

<figure class="lang-fig">
  <img src="/static/course_media/english-it/welcome-workplace.png" alt="IT workplace first day" loading="lazy">
  <figcaption>First day in an IT team: tickets, meetings, laptop, and colleagues.</figcaption>
</figure>


  <h2>Warm-up</h2>
  <p>Think in English: Where do developers, analysts, and support staff work together? — in an <strong>office</strong>, from <strong>home</strong>, or in a <strong>hybrid</strong> model.</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>IT department</strong></td><td>team that builds and supports technology</td><td>I work in the IT department.</td></tr>
<tr><td><strong>workplace</strong></td><td>place where you do your job</td><td>Our workplace is open-plan.</td></tr>
<tr><td><strong>colleague / teammate</strong></td><td>person you work with</td><td>My colleague reviews my code.</td></tr>
<tr><td><strong>laptop</strong></td><td>portable computer</td><td>Please bring your laptop to the meeting.</td></tr>
<tr><td><strong>meeting</strong></td><td>planned discussion</td><td>We have a team meeting at 10.</td></tr>
<tr><td><strong>ticket</strong></td><td>recorded work request or issue</td><td>I closed three tickets today.</td></tr>
<tr><td><strong>deadline</strong></td><td>time when work must be finished</td><td>The deadline is Friday.</td></tr>
<tr><td><strong>hybrid work</strong></td><td>mix of office and remote days</td><td>Our company uses hybrid work.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Good morning. I’m Dilshod. I work as a junior developer.</li>
<li>Nice to meet you. Which team are you on?</li>
<li>Could you show me how to join the standup?</li>
<li>I’ll send you the link in Slack.</li>
<li>Thank you for your help today.</li>
  </ul>

  <h2>Dialogue — first day</h2>
  <p><strong>HR:</strong> Welcome to SoftNova. How can I help you today?<br><strong>New hire:</strong> Good morning. I’m starting in the IT team. Where should I go?<br><strong>HR:</strong> Please take a seat. Your manager will meet you in five minutes.<br><strong>New hire:</strong> Thank you. Do I need my laptop?<br><strong>HR:</strong> Yes. You’ll get your accounts and a quick tour of the tools.</p>

  <h2>Grammar focus — Present simple (routines)</h2>
  <p>Use present simple for daily IT work:</p><ul><li>We <strong>start</strong> standup at 9:30.</li><li>She <strong>works</strong> remotely on Fridays.</li><li>The office <strong>doesn’t open</strong> on Sundays.</li></ul><p><strong>Questions:</strong> <em>What time do you start? Does your team use Slack?</em></p>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ I am work in IT. → ✅ I work in IT. / I am working in IT this week.</li>
<li>❌ Give me password! → ✅ Could you help me reset my password, please?</li>
<li>❌ My colleague he is late. → ✅ My colleague is late.</li>
  </ul>

  <h2>Reading — A morning in IT</h2>
  <p>Malika is a support specialist. She starts work at nine. First, she checks new tickets in the helpdesk system. Then she joins a short team meeting online. After that she answers emails and resets passwords for users. At lunch she walks outside for ten minutes. In the afternoon she updates a knowledge-base article. At five she writes a short summary of closed tickets for her manager.</p><p><strong>Check:</strong> What does Malika do first? Why does she update an article?</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Introduce yourself and your IT role (3 sentences).</li>
<li>Describe your typical work morning (4–5 sentences).</li>
<li>Role-play Dialogue — first day with a partner. Switch roles.</li>
  </ol>

  <div class="esp-visual">
  <p class="esp-visual-label">Visual map · A morning in IT</p>
  <ol class="esp-timeline">
    <li><span class="esp-time">09:00</span><span class="esp-step"><strong>Tickets</strong> — check new requests</span></li>
    <li><span class="esp-time">09:30</span><span class="esp-step"><strong>Meeting</strong> — short standup</span></li>
    <li><span class="esp-time">10:00</span><span class="esp-step"><strong>Work</strong> — emails, fixes, passwords</span></li>
    <li><span class="esp-time">17:00</span><span class="esp-step"><strong>Summary</strong> — closed tickets for the manager</span></li>
  </ol>
</div>
<div class="esp-try">
  <p class="esp-try-label">Try it now</p>
  <ul class="esp-checklist">
    <li>Say your name + role in one sentence.</li>
    <li>Name two tools you use every day.</li>
    <li>Ask a polite question with <em>Could you…?</em></li>
  </ul>
</div>

  <h2>Quick review</h2>
  <p>IT department · colleague · ticket · deadline · hybrid work · How can I help you? · I work as…</p>
""",
            ),
            _lec(
                'IT roles and teams',
                'eit-it-roles',
                """
<h2>Lesson goal</h2>
  <p>Name common IT roles and say what each person does in simple, accurate English.</p>

<figure class="lang-fig">
  <img src="/static/course_media/english-it/it-roles-map.png" alt="IT roles map" loading="lazy">
  <figcaption>Who does what? Developer, QA, Sysadmin, DevOps, Product Owner, Tech Lead.</figcaption>
</figure>


  <h2>Warm-up</h2>
  <p>Quick think: Who writes code? Who tests it? Who helps users when something breaks?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>software developer / engineer</strong></td><td>person who writes and maintains code</td><td>Our developer fixed the bug.</td></tr>
<tr><td><strong>QA / tester</strong></td><td>person who checks quality and finds defects</td><td>QA found a login issue.</td></tr>
<tr><td><strong>sysadmin</strong></td><td>person who manages servers and systems</td><td>The sysadmin restarted the service.</td></tr>
<tr><td><strong>network engineer</strong></td><td>person who designs and supports networks</td><td>A network engineer checked the Wi-Fi.</td></tr>
<tr><td><strong>DevOps engineer</strong></td><td>person who connects development and operations</td><td>DevOps set up the pipeline.</td></tr>
<tr><td><strong>product owner</strong></td><td>person who prioritises product work</td><td>The product owner wrote the story.</td></tr>
<tr><td><strong>tech lead</strong></td><td>senior engineer who guides the team</td><td>Ask the tech lead for a design review.</td></tr>
<tr><td><strong>intern</strong></td><td>trainee gaining workplace experience</td><td>Our intern shadows the support team.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>I work as a junior developer on the payments team.</li>
<li>I’m responsible for writing unit tests.</li>
<li>Who should I escalate this ticket to?</li>
<li>Could you introduce me to the QA lead?</li>
<li>Our team owns the mobile app.</li>
  </ul>

  <h2>Dialogue — Who should I ask?</h2>
  <p><strong>Intern:</strong> The website is slow for some users. Who should I call?<br><strong>Mentor:</strong> Start with support. If it’s a network issue, involve the network engineer.<br><strong>Intern:</strong> And if the problem is in the code?<br><strong>Mentor:</strong> Create a ticket for the developers and copy the tech lead.<br><strong>Intern:</strong> Got it. Thanks!</p>

  <h2>Grammar focus — Present simple + 3rd person -s</h2>
  <ul><li>She <strong>tests</strong> new builds. He <strong>manages</strong> servers.</li><li>The team <strong>reviews</strong> pull requests every day.</li><li>Negative: He <strong>doesn’t deploy</strong> on Fridays.</li><li>Question: <em>Where does she work? Does QA test every release?</em></li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ He develop softwares. → ✅ He develops software.</li>
<li>❌ I responsible for bugs. → ✅ I’m responsible for fixing bugs.</li>
<li>❌ Who I should ask? → ✅ Who should I ask?</li>
  </ul>

  <h2>Reading — Meet the IT teams</h2>
  <p>At CloudBridge, developers write features in two-week sprints. QA checks each build before release. Sysadmins keep the servers healthy. DevOps engineers automate deployments. When a big outage happens, support opens a ticket, the tech lead coordinates, and everyone communicates in one channel. Clear roles make problems faster to solve.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Say what three IT roles do (one sentence each).</li>
<li>Introduce yourself: “I work as … I’m responsible for …”</li>
<li>Explain who to call for a Wi-Fi problem vs a code bug.</li>
  </ol>

  <div class="esp-visual">
  <p class="esp-visual-label">Role cards · who to call</p>
  <div class="esp-cards">
    <div class="esp-card"><strong>Developer</strong><span>writes &amp; fixes code</span></div>
    <div class="esp-card"><strong>QA</strong><span>finds defects before release</span></div>
    <div class="esp-card"><strong>Sysadmin</strong><span>keeps servers healthy</span></div>
    <div class="esp-card"><strong>DevOps</strong><span>automates deploy pipeline</span></div>
    <div class="esp-card"><strong>Product owner</strong><span>sets priorities</span></div>
    <div class="esp-card"><strong>Tech lead</strong><span>guides technical decisions</span></div>
  </div>
</div>
<div class="esp-scenario">
  <p class="esp-try-label">Scenario lab</p>
  <p>Wi‑Fi is down → <strong>network engineer / support</strong>. Login bug in code → <strong>developer + tech lead</strong>.</p>
</div>

  <h2>Quick review</h2>
  <p>developer · QA · sysadmin · DevOps · product owner · tech lead · responsible for</p>
""",
            ),
            _lec(
                'Office and remote work',
                'eit-office-remote',
                """
<h2>Lesson goal</h2>
  <p>Talk about office, remote, and hybrid setups; ask for help with tools politely.</p>

<figure class="lang-fig">
  <img src="/static/course_media/english-it/office-remote-modes.png" alt="Office remote hybrid" loading="lazy">
  <figcaption>Office · Remote · Hybrid — pick the words that match your week.</figcaption>
</figure>


  <h2>Warm-up</h2>
  <p>Do you prefer a quiet home desk or a busy office? Why?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>remote work</strong></td><td>working from outside the office</td><td>I work remotely on Mondays.</td></tr>
<tr><td><strong>on-site / in the office</strong></td><td>working at the company location</td><td>Please come on-site tomorrow.</td></tr>
<tr><td><strong>VPN</strong></td><td>secure connection to the company network</td><td>Connect to the VPN before opening the database.</td></tr>
<tr><td><strong>headset</strong></td><td>headphones with a microphone</td><td>Use a headset for video calls.</td></tr>
<tr><td><strong>shared calendar</strong></td><td>calendar everyone can see</td><td>Put the demo in the shared calendar.</td></tr>
<tr><td><strong>status update</strong></td><td>short report of progress</td><td>Post a status update by 5 p.m.</td></tr>
<tr><td><strong>timezone</strong></td><td>local time region</td><td>Our client is in another timezone.</td></tr>
<tr><td><strong>async</strong></td><td>not happening at the same moment</td><td>We prefer async updates in chat.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>I’ll join the call from home today.</li>
<li>Could you share your screen, please?</li>
<li>I’m afraid my connection is unstable.</li>
<li>Can we move the meeting to 3 p.m. your time?</li>
<li>I’ll follow up in writing after the call.</li>
  </ul>

  <h2>Dialogue A — remote standup</h2>
  <p><strong>Lead:</strong> Good morning, everyone. Kamola, can you hear us?<br><strong>Kamola:</strong> Yes — sorry, I had to reconnect to the VPN.<br><strong>Lead:</strong> No problem. What’s your update?<br><strong>Kamola:</strong> I finished the login fix. Today I’ll write tests.<br><strong>Lead:</strong> Great. Ping QA when the PR is ready.</p>

  <h2>Grammar focus — Can / Could / I’m afraid</h2>
  <ul><li><strong>Can you…?</strong> = ability or informal request</li><li><strong>Could you…?</strong> = more polite request</li><li><strong>I’m afraid…</strong> = soft bad news</li></ul><p><em>Could you share the agenda? I’m afraid I’m running five minutes late.</em></p>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ I work from home always yesterday. → ✅ I usually work from home. / I worked from home yesterday.</li>
<li>❌ Share screen! → ✅ Could you share your screen, please?</li>
<li>❌ My internet is bad, I leave. → ✅ I’m afraid my connection is unstable. I’ll reconnect.</li>
  </ul>

  <h2>Reading — Hybrid week</h2>
  <p>Jasur’s team works hybrid. On Tuesday and Thursday they come to the office for workshops. On other days they work remotely. Everyone must use the VPN for internal tools. Meetings start with a quick check: camera optional, mic muted when not speaking. Jasur writes async notes so teammates in other timezones can catch up later.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain your ideal hybrid week (4 sentences).</li>
<li>Ask a colleague politely to share a screen and a document link.</li>
<li>Role-play a bad connection and a polite reconnection.</li>
  </ol>

  <div class="esp-visual">
  <p class="esp-visual-label">Work modes · choose &amp; speak</p>
  <div class="esp-cards esp-cards-3">
    <div class="esp-card"><strong>Office</strong><span>on-site · workshops · whiteboard</span></div>
    <div class="esp-card"><strong>Remote</strong><span>VPN · headset · home desk</span></div>
    <div class="esp-card"><strong>Hybrid</strong><span>2 days office · async notes</span></div>
  </div>
</div>
<div class="esp-try">
  <p class="esp-try-label">Polite toolkit</p>
  <ul class="esp-checklist">
    <li>Could you share your screen, please?</li>
    <li>I’m afraid my connection is unstable.</li>
    <li>Can we move the meeting to 3 p.m. your time?</li>
  </ul>
</div>

  <h2>Quick review</h2>
  <p>remote · on-site · VPN · headset · async · Could you…? · I’m afraid…</p>
""",
            ),
        ],
        "practice": {
            'eit-welcome-it': _quiz(
                'eit-q-ticket',
                'So‘z: ticket',
                'IT workplace.',
                'In IT support, a ticket is…',
                [
                    'A) a recorded work request or issue',
                    'B) a train pass only',
                    'C) a type of virus',
                    'D) a hardware fan',
                ],
                'A',
            ),
            'eit-it-roles': _quiz(
                'eit-q-qa-role',
                'Rol: QA',
                'IT rollar.',
                'A QA specialist mainly…',
                [
                    'A) designs office furniture',
                    'B) checks quality and finds defects',
                    'C) prints salary slips',
                    'D) sells laptops in a shop',
                ],
                'B',
            ),
            'eit-office-remote': _quiz(
                'eit-q-vpn',
                'So‘z: VPN',
                'Remote ish.',
                'A VPN helps you…',
                [
                    'A) connect securely to the company network',
                    'B) cook lunch faster',
                    'C) delete all emails forever',
                    'D) change your job title automatically',
                ],
                'A',
            ),
        },
        "exercises": [
            _quiz(
                'eit-m1-colleague',
                'So‘z: colleague',
                'Workplace.',
                'A colleague is…',
                [
                    'A) a person you work with',
                    'B) only the company CEO',
                    'C) a broken cable',
                    'D) a database password',
                ],
                'A',
            ),
            _quiz(
                'eit-m1-help',
                'Gapirish: yordam',
                'Salomlashish.',
                'Best first line in a team chat:',
                [
                    'A) What do you want?',
                    'B) How can I help you?',
                    'C) Password now!',
                    'D) You again?',
                ],
                'B',
            ),
        ],
        "homework": _hw(
            "English for IT — Module 1 homework\n"
            "1) Write 8 sentences about your IT workday (present simple).\n"
            "2) Record or rehearse a 45-second self-introduction (name, role, team).\n"
            "3) Mini glossary: ticket, deadline, colleague, VPN, hybrid, QA, developer, sysadmin — English definition + one example each.\n"
            "4) Rewrite 5 rude messages into polite IT English."
        ),
    },
    {
        "order": 2,
        "title": 'Qurilmalar (Hardware & devices)',
        "slug": 'eit-hardware',
        "description": 'Kompyuter qismlari, periferiya va texnik xususiyatlar.',
        "lectures": [
            _lec(
                'Computer parts',
                'eit-computer-parts',
                """
<h2>Lesson goal</h2>
  <p>Name main internal computer parts and say what each one does in clear English.</p>

  <h2>Warm-up</h2>
  <p>If a PC is slow, which part do people blame first — CPU, RAM, or the hard disk?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>CPU / processor</strong></td><td>the ‘brain’ that runs instructions</td><td>A faster CPU helps with heavy apps.</td></tr>
<tr><td><strong>RAM</strong></td><td>short-term memory for running programs</td><td>This laptop has 16 GB of RAM.</td></tr>
<tr><td><strong>storage / SSD / HDD</strong></td><td>place where files are saved</td><td>An SSD is usually faster than an HDD.</td></tr>
<tr><td><strong>motherboard</strong></td><td>main board that connects components</td><td>The CPU sits on the motherboard.</td></tr>
<tr><td><strong>GPU / graphics card</strong></td><td>handles graphics and display work</td><td>Video editing needs a strong GPU.</td></tr>
<tr><td><strong>power supply (PSU)</strong></td><td>provides electricity to components</td><td>A weak PSU can cause restarts.</td></tr>
<tr><td><strong>cooling fan</strong></td><td>keeps parts from overheating</td><td>Clean the cooling fan regularly.</td></tr>
<tr><td><strong>port</strong></td><td>socket for cables and devices</td><td>Use the HDMI port for the monitor.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Could you check the RAM usage, please?</li>
<li>The disk is almost full.</li>
<li>We need to upgrade the SSD.</li>
<li>Is the power supply working correctly?</li>
<li>The laptop overheats under load.</li>
  </ul>

  <h2>Dialogue — diagnosing a slow PC</h2>
  <p><strong>User:</strong> My computer is very slow today.<br><strong>Tech:</strong> Let’s check a few things. How much free storage do you have?<br><strong>User:</strong> Only 2 GB on the C drive.<br><strong>Tech:</strong> That’s low. We should free space or upgrade the SSD. Also, open Task Manager and check RAM usage.<br><strong>User:</strong> RAM is at 95%.<br><strong>Tech:</strong> Close unused apps first. If it continues, we may add more RAM.</p>

  <h2>Grammar focus — How much / how many</h2>
  <ul><li><strong>How much RAM</strong> do you have?</li><li><strong>How many ports</strong> does this laptop have?</li><li>We need <strong>more storage</strong> / <strong>another SSD</strong>.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ I have many RAM. → ✅ I have a lot of RAM. / I have 16 GB of RAM.</li>
<li>❌ Memory and storage same. → ✅ RAM is short-term; storage keeps files.</li>
<li>❌ CPU is full of files. → ✅ The disk/storage is full — not the CPU.</li>
  </ul>

  <h2>Reading — Inside a laptop</h2>
  <p>A modern laptop packs a CPU, RAM, and an SSD into a thin case. The motherboard connects everything. A small cooling fan moves heat away from the processor. When dust blocks the fan, the laptop becomes hot and slow. Users often say “I need more memory,” but they may mean storage space, not RAM. Clear vocabulary helps support teams fix the real problem.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain CPU, RAM, and storage in one sentence each.</li>
<li>Role-play helping a user with a full disk.</li>
<li>Describe your own device specs for 30 seconds.</li>
  </ol>

  <h2>Quick review</h2>
  <p>CPU · RAM · SSD · motherboard · GPU · PSU · port · upgrade</p>
""",
            ),
            _lec(
                'Peripherals and devices',
                'eit-peripherals',
                """
<h2>Lesson goal</h2>
  <p>Talk about monitors, keyboards, printers, and other peripherals; request replacements politely.</p>

  <h2>Warm-up</h2>
  <p>List five devices on your desk without looking.</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>peripheral</strong></td><td>external device connected to a computer</td><td>A mouse is a peripheral.</td></tr>
<tr><td><strong>monitor / display</strong></td><td>screen you look at</td><td>I need a second monitor.</td></tr>
<tr><td><strong>keyboard</strong></td><td>device for typing</td><td>My keyboard has sticky keys.</td></tr>
<tr><td><strong>mouse / trackpad</strong></td><td>pointer control device</td><td>The trackpad stopped responding.</td></tr>
<tr><td><strong>printer / scanner</strong></td><td>prints or digitises paper</td><td>The printer is out of paper.</td></tr>
<tr><td><strong>webcam</strong></td><td>camera for video calls</td><td>Please turn on your webcam.</td></tr>
<tr><td><strong>USB cable / dock</strong></td><td>connection tools for devices</td><td>Use the dock for two screens.</td></tr>
<tr><td><strong>headset</strong></td><td>audio device for calls</td><td>The headset mic is muted.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>My monitor flickers. Could someone check it?</li>
<li>I’d like to request a replacement keyboard.</li>
<li>Is the printer connected to the network?</li>
<li>Please plug the HDMI cable into the dock.</li>
<li>The webcam isn’t detected.</li>
  </ul>

  <h2>Dialogue — printer problem</h2>
  <p><strong>Employee:</strong> The office printer won’t print my PDF.<br><strong>Support:</strong> Are you connected to the correct printer queue?<br><strong>Employee:</strong> I think so. It says ‘offline’.<br><strong>Support:</strong> Please check the USB or network cable, then restart the printer.<br><strong>Employee:</strong> Done — it’s online now. Thanks!</p>

  <h2>Grammar focus — Imperatives for instructions</h2>
  <p>Use clear steps:</p><ul><li><strong>Plug in</strong> the cable. <strong>Restart</strong> the device.</li><li><strong>Don’t unplug</strong> the server without approval.</li><li>Polite: <em>Could you restart the printer, please?</em></li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Monitor is broke. → ✅ The monitor is broken.</li>
<li>❌ Make print. → ✅ Print the document.</li>
<li>❌ Mouse not working always yesterday. → ✅ The mouse wasn’t working yesterday.</li>
  </ul>

  <h2>Reading — Dual monitors</h2>
  <p>Many developers use two monitors: code on one screen, documentation on the other. A docking station connects laptop, monitors, and a wired keyboard with one cable. When a webcam fails during a client call, a quick checklist helps: check permissions, test another app, try a different USB port. Good peripheral English saves time in tickets.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Give 4 imperative steps to connect a second monitor.</li>
<li>Request a new headset politely.</li>
<li>Explain why a dock is useful (3 sentences).</li>
  </ol>

  <h2>Quick review</h2>
  <p>peripheral · monitor · printer · webcam · dock · Plug in… · Could you…?</p>
""",
            ),
            _lec(
                'Specs and comparisons',
                'eit-specs-compare',
                """
<h2>Lesson goal</h2>
  <p>Compare device specifications using comparatives and clear numbers.</p>

  <h2>Warm-up</h2>
  <p>Which matters more for your work: battery life, screen size, or CPU speed?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>specifications (specs)</strong></td><td>technical details of a device</td><td>Please send the laptop specs.</td></tr>
<tr><td><strong>performance</strong></td><td>how fast/well something works</td><td>Performance dropped after the update.</td></tr>
<tr><td><strong>battery life</strong></td><td>how long a device runs on battery</td><td>Battery life is about 8 hours.</td></tr>
<tr><td><strong>resolution</strong></td><td>screen detail (e.g. 1920×1080)</td><td>This monitor has 4K resolution.</td></tr>
<tr><td><strong>weight</strong></td><td>how heavy a device is</td><td>The ultrabook is light — only 1.2 kg.</td></tr>
<tr><td><strong>upgrade</strong></td><td>improve by adding better parts</td><td>We upgraded the RAM to 32 GB.</td></tr>
<tr><td><strong>compatible</strong></td><td>able to work together</td><td>Is this charger compatible?</td></tr>
<tr><td><strong>warranty</strong></td><td>repair/replace promise for a period</td><td>The warranty ends next month.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>This model is faster than the old one.</li>
<li>It has more RAM, but a smaller screen.</li>
<li>Which laptop is better for development?</li>
<li>The new SSD is much quieter.</li>
<li>It’s compatible with USB-C docks.</li>
  </ul>

  <h2>Dialogue — choosing a laptop</h2>
  <p><strong>Buyer:</strong> I need a laptop for coding and video calls.<br><strong>Advisor:</strong> Then look for at least 16 GB of RAM and a bright screen.<br><strong>Buyer:</strong> Is Model A better than Model B?<br><strong>Advisor:</strong> Model A is lighter and has longer battery life. Model B has a stronger GPU.<br><strong>Buyer:</strong> I’ll take Model A — I travel a lot.</p>

  <h2>Grammar focus — Comparatives and superlatives</h2>
  <ul><li>faster / slower · lighter / heavier · better / worse</li><li>more RAM · less storage · the most powerful GPU</li><li>This SSD is <strong>faster than</strong> that HDD.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ This laptop more better. → ✅ This laptop is better.</li>
<li>❌ It have 16 GB. → ✅ It has 16 GB.</li>
<li>❌ The most fast CPU. → ✅ The fastest CPU.</li>
  </ul>

  <h2>Reading — Spec sheet sense</h2>
  <p>A good buyer reads specs carefully. More GHz does not always mean a better experience if RAM is low. A high resolution looks sharp, but may use more battery. Weight matters for travel. Support teams should ask: “What do you use the device for?” before recommending an upgrade.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Compare two imaginary laptops using comparatives (6 sentences).</li>
<li>Ask three questions about specs in a shop role-play.</li>
<li>Explain warranty in simple English.</li>
  </ol>

  <h2>Quick review</h2>
  <p>specs · performance · battery life · compatible · faster than · better for</p>
""",
            ),
        ],
        "practice": {
            'eit-computer-parts': _quiz(
                'eit-q-ram',
                'So‘z: RAM',
                'Hardware.',
                'RAM is mainly…',
                [
                    'A) short-term memory for running programs',
                    'B) a printer type',
                    'C) an email folder',
                    'D) a Wi-Fi password',
                ],
                'A',
            ),
            'eit-peripherals': _quiz(
                'eit-q-peripheral',
                'So‘z: peripheral',
                'Devices.',
                'A peripheral is…',
                [
                    'A) an external device connected to a computer',
                    'B) the CPU only',
                    'C) a cloud region',
                    'D) a programming language',
                ],
                'A',
            ),
            'eit-specs-compare': _quiz(
                'eit-q-faster',
                'Grammar: comparative',
                'Specs.',
                'Correct sentence:',
                [
                    'A) This SSD is faster than that HDD.',
                    'B) This SSD more faster that HDD.',
                    'C) This SSD fastest as HDD.',
                    'D) SSD is more better.',
                ],
                'A',
            ),
        },
        "exercises": [
            _quiz(
                'eit-m2-ssd',
                'So‘z: SSD',
                'Storage.',
                'An SSD usually…',
                [
                    'A) stores files and is often faster than an HDD',
                    'B) prints documents',
                    'C) replaces the keyboard',
                    'D) is a type of phishing',
                ],
                'A',
            ),
            _quiz(
                'eit-m2-upgrade',
                'So‘z: upgrade',
                'Hardware.',
                'To upgrade RAM means…',
                [
                    'A) add or install more memory',
                    'B) delete the operating system',
                    'C) throw away the monitor',
                    'D) change the company name',
                ],
                'A',
                difficulty='medium',
            ),
        ],
        "homework": _hw(
            "English for IT — Module 2 homework\n"
            "1) Label a PC diagram in English (CPU, RAM, SSD, GPU, ports).\n"
            "2) Write 10 comparative sentences about two devices.\n"
            "3) Record a 60-second explanation of why a PC is slow (disk/RAM).\n"
            "4) Make a mini glossary of 10 hardware words with examples."
        ),
    },
    {
        "order": 3,
        "title": 'Dasturiy ta’minot va OS (Software & OS)',
        "slug": 'eit-software-os',
        "description": 'Operatsion tizim, ilovalar, litsenziya, o‘rnatish va yangilash.',
        "lectures": [
            _lec(
                'Operating system basics',
                'eit-os-basics',
                """
<h2>Lesson goal</h2>
  <p>Describe what an OS does and compare common systems in simple English.</p>

  <h2>Warm-up</h2>
  <p>Which OS do you use every day — Windows, macOS, or Linux? Why?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>operating system (OS)</strong></td><td>software that manages hardware and apps</td><td>Windows is a popular OS.</td></tr>
<tr><td><strong>desktop / laptop OS</strong></td><td>system for personal computers</td><td>macOS runs on Apple laptops.</td></tr>
<tr><td><strong>mobile OS</strong></td><td>system for phones/tablets</td><td>Android is a mobile OS.</td></tr>
<tr><td><strong>file / folder</strong></td><td>data item / container for files</td><td>Save the file in the Documents folder.</td></tr>
<tr><td><strong>process / task</strong></td><td>a running program</td><td>Close unused processes to free RAM.</td></tr>
<tr><td><strong>driver</strong></td><td>software that talks to a device</td><td>Update the printer driver.</td></tr>
<tr><td><strong>user account</strong></td><td>login identity on a system</td><td>Create a new user account.</td></tr>
<tr><td><strong>admin rights</strong></td><td>permission to change system settings</td><td>You need admin rights to install this.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Which operating system are you running?</li>
<li>I need admin rights to install this.</li>
<li>Please restart and try again.</li>
<li>The OS crashed after the update.</li>
<li>Let’s check the Task Manager / Activity Monitor.</li>
  </ul>

  <h2>Dialogue — choosing an OS</h2>
  <p><strong>Student:</strong> Should I learn Linux for IT work?<br><strong>Mentor:</strong> Yes, many servers run Linux. Start with basic commands.<br><strong>Student:</strong> Do companies still use Windows?<br><strong>Mentor:</strong> Absolutely. Offices often use Windows desktops and Linux servers together.</p>

  <h2>Grammar focus — Present continuous vs present simple</h2>
  <ul><li>I <strong>use</strong> Windows at work. (habit)</li><li>The system <strong>is updating</strong> now. (right now)</li><li>Don’t restart while it <strong>is installing</strong>.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ OS is a hardware. → ✅ An OS is software.</li>
<li>❌ I am use Linux. → ✅ I use Linux. / I am using Linux today.</li>
<li>❌ Open the folder of Documents. → ✅ Open the Documents folder.</li>
  </ul>

  <h2>Reading — Why the OS matters</h2>
  <p>The operating system is the bridge between hardware and applications. It manages memory, files, and user accounts. If a driver is missing, a device may not work. Support staff often ask: “Which OS version are you on?” because solutions differ between Windows 11, macOS, and Linux distributions.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain what an OS does in 4 sentences.</li>
<li>Compare Windows and Linux for servers vs offices.</li>
<li>Give polite steps to restart after an update.</li>
  </ol>

  <h2>Quick review</h2>
  <p>OS · driver · user account · admin rights · file · folder · is updating</p>
""",
            ),
            _lec(
                'Apps and licenses',
                'eit-apps-licenses',
                """
<h2>Lesson goal</h2>
  <p>Talk about applications, free vs paid software, and licence rules politely.</p>

  <h2>Warm-up</h2>
  <p>Is all software free to copy? Why or why not?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>application / app</strong></td><td>program that does a task</td><td>Slack is a communication app.</td></tr>
<tr><td><strong>licence / license</strong></td><td>legal permission to use software</td><td>Check the licence before installing.</td></tr>
<tr><td><strong>open source</strong></td><td>code that can be studied and shared under rules</td><td>Linux is open source.</td></tr>
<tr><td><strong>proprietary</strong></td><td>owned by a company; limited rights</td><td>That tool is proprietary software.</td></tr>
<tr><td><strong>subscription</strong></td><td>pay regularly to use software</td><td>We pay a monthly subscription.</td></tr>
<tr><td><strong>trial version</strong></td><td>time-limited test copy</td><td>Download the 30-day trial.</td></tr>
<tr><td><strong>malware</strong></td><td>harmful software</td><td>Don’t install apps from unknown sites — risk of malware.</td></tr>
<tr><td><strong>uninstall</strong></td><td>remove a program</td><td>Uninstall the old antivirus first.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Is this software licensed for commercial use?</li>
<li>We need a subscription for the whole team.</li>
<li>Please don’t install pirated software.</li>
<li>The trial expires tomorrow.</li>
<li>I’ll request a licence from IT.</li>
  </ul>

  <h2>Dialogue — licence request</h2>
  <p><strong>Developer:</strong> I need a design tool for mockups.<br><strong>IT:</strong> We have a company subscription. I’ll add you to the team licence.<br><strong>Developer:</strong> Can I install a free random app from the internet?<br><strong>IT:</strong> Only from the approved list. Unknown installers can bring malware.</p>

  <h2>Grammar focus — Need to / have to / mustn’t</h2>
  <ul><li>You <strong>need to</strong> request a licence.</li><li>We <strong>have to</strong> follow company policy.</li><li>You <strong>mustn’t</strong> share licence keys in public chat.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Softwares are many. → ✅ Software is uncountable: a lot of software / many apps.</li>
<li>❌ Licence key send me. → ✅ Could you send me the licence key, please?</li>
<li>❌ Open source means no rules. → ✅ Open source still has licence rules.</li>
  </ul>

  <h2>Reading — Approved apps only</h2>
  <p>Many companies keep an approved application list. Staff can install tools from that list without special permission. New tools need a security review. Licences matter: using one personal key for twenty people can break the contract. Clear English in tickets — “Please add me to the Figma licence” — speeds up IT responses.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain open source vs proprietary in simple English.</li>
<li>Role-play requesting a team subscription.</li>
<li>Warn a colleague about pirated software politely.</li>
  </ol>

  <h2>Quick review</h2>
  <p>app · licence · open source · subscription · trial · malware · mustn’t</p>
""",
            ),
            _lec(
                'Install and update',
                'eit-install-update',
                """
<h2>Lesson goal</h2>
  <p>Give and follow clear steps for installing, updating, and rolling back software.</p>

  <h2>Warm-up</h2>
  <p>Have you ever had an update break something? What did you do?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>install</strong></td><td>set up software on a device</td><td>Install the latest browser.</td></tr>
<tr><td><strong>update / patch</strong></td><td>improve or fix existing software</td><td>Install security patches this week.</td></tr>
<tr><td><strong>download</strong></td><td>copy a file from the internet</td><td>Download the installer from the official site.</td></tr>
<tr><td><strong>reboot / restart</strong></td><td>turn the system off and on</td><td>Reboot after the update.</td></tr>
<tr><td><strong>rollback</strong></td><td>return to a previous version</td><td>We rolled back the failed release.</td></tr>
<tr><td><strong>release notes</strong></td><td>summary of what changed</td><td>Read the release notes first.</td></tr>
<tr><td><strong>compatibility</strong></td><td>works with your system/version</td><td>Check compatibility with Windows 11.</td></tr>
<tr><td><strong>dependency</strong></td><td>other software required</td><td>The app needs a library dependency.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Download the installer from the official website only.</li>
<li>Close all apps before updating.</li>
<li>The update requires a reboot.</li>
<li>If it fails, we can roll back.</li>
<li>Please read the release notes.</li>
  </ul>

  <h2>Dialogue — failed update</h2>
  <p><strong>User:</strong> After the update, the app won’t open.<br><strong>Support:</strong> Thanks for reporting it. Which version did you install?<br><strong>User:</strong> 4.2.0 from this morning.<br><strong>Support:</strong> We’re seeing that bug. Please roll back to 4.1.8 and wait for the patch.</p>

  <h2>Grammar focus — Sequencing: first / then / after that / finally</h2>
  <ul><li><strong>First</strong>, download the installer.</li><li><strong>Then</strong>, run it as administrator.</li><li><strong>After that</strong>, restart.</li><li><strong>Finally</strong>, verify the version number.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Update the software yesterday I. → ✅ I updated the software yesterday.</li>
<li>❌ Make download. → ✅ Download the file.</li>
<li>❌ Reboot always without save. → ✅ Save your work before you reboot.</li>
  </ul>

  <h2>Reading — Patch Tuesday mindset</h2>
  <p>Security patches fix known weaknesses. Waiting too long increases risk. Still, wise teams test updates on a small group first. If something breaks, rollback plans save the day. Good communication — “Update starts at 18:00; expect 10 minutes of downtime” — reduces user stress.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Give a 5-step install instruction aloud.</li>
<li>Explain rollback to a non-technical user.</li>
<li>Role-play reporting a failed update.</li>
  </ol>

  <h2>Quick review</h2>
  <p>install · update · patch · reboot · rollback · release notes · First… Then…</p>
""",
            ),
        ],
        "practice": {
            'eit-os-basics': _quiz(
                'eit-q-os',
                'So‘z: OS',
                'Software.',
                'An operating system is…',
                [
                    'A) software that manages hardware and apps',
                    'B) only a mouse cable',
                    'C) a type of phishing email',
                    'D) a meeting room',
                ],
                'A',
            ),
            'eit-apps-licenses': _quiz(
                'eit-q-licence',
                'So‘z: licence',
                'Apps.',
                'A software licence is…',
                [
                    'A) legal permission to use software',
                    'B) a hardware fan',
                    'C) a Wi-Fi channel',
                    'D) a bug report template',
                ],
                'A',
            ),
            'eit-install-update': _quiz(
                'eit-q-rollback',
                'So‘z: rollback',
                'Updates.',
                'To roll back means…',
                [
                    'A) return to a previous version',
                    'B) buy a new monitor',
                    'C) delete the company',
                    'D) invent a password',
                ],
                'A',
            ),
        },
        "exercises": [
            _quiz(
                'eit-m3-admin',
                'So‘z: admin rights',
                'OS.',
                'Admin rights allow you to…',
                [
                    'A) change system settings and install software',
                    'B) cook lunch in the cafeteria',
                    'C) rename the internet',
                    'D) skip all passwords forever',
                ],
                'A',
            ),
            _quiz(
                'eit-m3-mustnt',
                'Grammar: mustn’t',
                'Licences.',
                'Correct policy sentence:',
                [
                    'A) You mustn’t share licence keys in public chat.',
                    'B) You mustn’t to share keys.',
                    'C) You no must share.',
                    'D) Mustn’t you sharing keys always.',
                ],
                'A',
                difficulty='medium',
            ),
        ],
        "homework": _hw(
            "English for IT — Module 3 homework\n"
            "1) Write steps to install a browser (First/Then/Finally).\n"
            "2) Glossary: OS, driver, licence, patch, rollback, malware, subscription, admin rights.\n"
            "3) Record a 45-second warning about unofficial installers.\n"
            "4) Compare two OS options in 8 sentences."
        ),
    },
    {
        "order": 4,
        "title": 'Tarmoq va Internet (Networking)',
        "slug": 'eit-networking',
        "description": 'Tarmoq asoslari, protokollar va Wi-Fi muammolarini hal qilish.',
        "lectures": [
            _lec(
                'Network basics',
                'eit-network-basics',
                """
<h2>Lesson goal</h2>
  <p>Explain LAN/WAN, router, switch, and IP address in clear pre-intermediate English.</p>

  <h2>Warm-up</h2>
  <p>How does your phone get internet at home — cable, Wi-Fi, or mobile data?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>network</strong></td><td>connected devices that share data</td><td>Our office network is private.</td></tr>
<tr><td><strong>LAN</strong></td><td>local area network (same building)</td><td>Printers are on the LAN.</td></tr>
<tr><td><strong>WAN</strong></td><td>wide area network across locations</td><td>Branch offices connect over a WAN.</td></tr>
<tr><td><strong>router</strong></td><td>device that directs traffic between networks</td><td>Restart the router if the net is down.</td></tr>
<tr><td><strong>switch</strong></td><td>connects devices inside a LAN</td><td>Plug the cable into the switch.</td></tr>
<tr><td><strong>IP address</strong></td><td>number that identifies a device on a network</td><td>What’s your IP address?</td></tr>
<tr><td><strong>bandwidth</strong></td><td>capacity for data transfer</td><td>Video calls need enough bandwidth.</td></tr>
<tr><td><strong>latency</strong></td><td>delay in network response</td><td>High latency makes games lag.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>The network is down.</li>
<li>Please check the router lights.</li>
<li>Can you ping the server?</li>
<li>We have high latency today.</li>
<li>Is this device on the LAN?</li>
  </ul>

  <h2>Dialogue — network down</h2>
  <p><strong>User:</strong> I can’t open any website.<br><strong>Support:</strong> Are other people affected too?<br><strong>User:</strong> Yes, the whole floor.<br><strong>Support:</strong> Thanks. We’ll check the router and switch. Please wait five minutes.</p>

  <h2>Grammar focus — There is / There are + network problems</h2>
  <ul><li><strong>There is</strong> a problem with the router.</li><li><strong>There are</strong> too many devices on this Wi-Fi.</li><li><strong>There isn’t</strong> enough bandwidth for the meeting.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Network is break. → ✅ The network is down / broken.</li>
<li>❌ IP address what is you? → ✅ What is your IP address?</li>
<li>❌ Router and switch same always. → ✅ They have different roles.</li>
  </ul>

  <h2>Reading — Office LAN</h2>
  <p>In a typical office, computers connect to a switch. The switch links to a router that reaches the internet. Each device has an IP address. If bandwidth is low, video meetings freeze. Support teams measure latency and check cables before blaming the ISP.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain LAN vs WAN in 3 sentences.</li>
<li>Role-play reporting a network outage.</li>
<li>Describe router vs switch simply.</li>
  </ol>

  <h2>Quick review</h2>
  <p>network · LAN · WAN · router · switch · IP · bandwidth · latency</p>
""",
            ),
            _lec(
                'Internet and protocols',
                'eit-internet-protocols',
                """
<h2>Lesson goal</h2>
  <p>Use everyday protocol words: HTTP/HTTPS, DNS, TCP/IP without deep theory overload.</p>

  <h2>Warm-up</h2>
  <p>Why do some website addresses start with https?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>protocol</strong></td><td>set of rules for communication</td><td>HTTPS is a secure protocol.</td></tr>
<tr><td><strong>HTTP / HTTPS</strong></td><td>web transfer protocols; S = secure</td><td>Always prefer HTTPS.</td></tr>
<tr><td><strong>DNS</strong></td><td>system that maps names to IP addresses</td><td>DNS can’t resolve the domain.</td></tr>
<tr><td><strong>TCP/IP</strong></td><td>core internet communication suite</td><td>TCP/IP moves packets across networks.</td></tr>
<tr><td><strong>URL / domain</strong></td><td>web address / site name</td><td>Check the domain carefully.</td></tr>
<tr><td><strong>packet</strong></td><td>small unit of network data</td><td>Packets travel across the internet.</td></tr>
<tr><td><strong>firewall</strong></td><td>filter that allows/blocks traffic</td><td>The firewall blocked the port.</td></tr>
<tr><td><strong>port (network)</strong></td><td>number for a service on a host</td><td>Port 443 is used for HTTPS.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>The DNS lookup failed.</li>
<li>Please try HTTPS instead of HTTP.</li>
<li>The firewall is blocking this port.</li>
<li>What’s the exact URL?</li>
<li>Clear the DNS cache and try again.</li>
  </ul>

  <h2>Dialogue — site won’t open</h2>
  <p><strong>User:</strong> The company portal won’t load.<br><strong>Support:</strong> Do you see an HTTPS padlock or an error?<br><strong>User:</strong> It says DNS_PROBE_FINISHED_NXDOMAIN.<br><strong>Support:</strong> The domain may be wrong, or DNS is failing. I’ll verify the URL and DNS settings.</p>

  <h2>Grammar focus — because / so / if</h2>
  <ul><li>Use HTTPS <strong>because</strong> it encrypts traffic.</li><li>DNS failed, <strong>so</strong> the site didn’t open.</li><li><strong>If</strong> the firewall blocks the port, the app can’t connect.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ HTTP is more safe than HTTPS. → ✅ HTTPS is more secure than HTTP.</li>
<li>❌ DNS is a cable. → ✅ DNS maps names to IP addresses.</li>
<li>❌ Firewall is virus. → ✅ A firewall filters traffic; antivirus finds malware.</li>
  </ul>

  <h2>Reading — Name to number</h2>
  <p>When you type a domain, DNS finds the matching IP address. Browsers then use HTTPS to talk to the server securely. Firewalls may block unknown ports. You don’t need to memorise every RFC — but you do need clear words to describe errors to colleagues.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain HTTPS to a beginner in 4 sentences.</li>
<li>Describe a DNS failure simply.</li>
<li>Ask three clarifying questions about a ‘site down’ ticket.</li>
  </ol>

  <h2>Quick review</h2>
  <p>protocol · HTTPS · DNS · firewall · port · URL · because / so / if</p>
""",
            ),
            _lec(
                'Wi-Fi troubleshooting',
                'eit-wifi-troubleshoot',
                """
<h2>Lesson goal</h2>
  <p>Follow and give a calm Wi-Fi troubleshooting checklist in English.</p>

  <h2>Warm-up</h2>
  <p>What is your first step when Wi-Fi disconnects?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>Wi-Fi / wireless</strong></td><td>network without cables</td><td>Connect to the office Wi-Fi.</td></tr>
<tr><td><strong>signal strength</strong></td><td>how strong the wireless signal is</td><td>Signal strength is weak near the lift.</td></tr>
<tr><td><strong>SSID</strong></td><td>network name</td><td>Choose the correct SSID.</td></tr>
<tr><td><strong>password / passphrase</strong></td><td>secret to join the network</td><td>The Wi-Fi password changed today.</td></tr>
<tr><td><strong>interference</strong></td><td>noise that weakens Wi-Fi</td><td>Microwaves can cause interference.</td></tr>
<tr><td><strong>reconnect</strong></td><td>connect again</td><td>Forget the network and reconnect.</td></tr>
<tr><td><strong>airplane mode</strong></td><td>radio off setting on devices</td><td>Toggle airplane mode on and off.</td></tr>
<tr><td><strong>hotspot</strong></td><td>phone sharing internet</td><td>Use a mobile hotspot temporarily.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Forget the network, then reconnect.</li>
<li>Is airplane mode off?</li>
<li>The signal is weak in this room.</li>
<li>Try moving closer to the access point.</li>
<li>I’ll share a temporary hotspot.</li>
  </ul>

  <h2>Dialogue — weak signal</h2>
  <p><strong>Employee:</strong> My Wi-Fi keeps dropping in the meeting room.<br><strong>Support:</strong> Let’s check signal strength. Are you far from the access point?<br><strong>Employee:</strong> Yes, I’m near the window.<br><strong>Support:</strong> Move closer or use the wired dock. I’ll also check for interference after lunch.</p>

  <h2>Grammar focus — Imperatives + sequencing for troubleshooting</h2>
  <ul><li><strong>First</strong>, toggle airplane mode.</li><li><strong>Next</strong>, forget the SSID and reconnect.</li><li><strong>If that fails</strong>, restart the router.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Wi-Fi is broke always internet. → ✅ The Wi-Fi connection is unstable.</li>
<li>❌ Password forget me. → ✅ Forget the network / I forgot the password.</li>
<li>❌ Signal is many low. → ✅ The signal is very weak.</li>
  </ul>

  <h2>Reading — Calm checklist</h2>
  <p>Good troubleshooters stay calm. They ask: Is it one device or many? Is the SSID correct? Is the password updated? They try reconnect, then reboot, then escalate. Speaking clearly — “Signal is weak; wired connection works” — helps network engineers act faster.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Give a 5-step Wi-Fi fix checklist aloud.</li>
<li>Role-play a weak-signal complaint.</li>
<li>Explain when to escalate to a network engineer.</li>
  </ol>

  <h2>Quick review</h2>
  <p>Wi-Fi · SSID · signal · reconnect · hotspot · First… Next… If that fails…</p>
""",
            ),
        ],
        "practice": {
            'eit-network-basics': _quiz(
                'eit-q-router',
                'So‘z: router',
                'Network.',
                'A router mainly…',
                [
                    'A) directs traffic between networks',
                    'B) prints documents',
                    'C) writes unit tests',
                    'D) designs logos',
                ],
                'A',
            ),
            'eit-internet-protocols': _quiz(
                'eit-q-https',
                'So‘z: HTTPS',
                'Protocols.',
                'HTTPS is preferred because…',
                [
                    'A) it encrypts web traffic',
                    'B) it is slower by law',
                    'C) it deletes DNS',
                    'D) it replaces all cables',
                ],
                'A',
            ),
            'eit-wifi-troubleshoot': _quiz(
                'eit-q-ssid',
                'So‘z: SSID',
                'Wi-Fi.',
                'An SSID is…',
                [
                    'A) the Wi-Fi network name',
                    'B) a CPU model',
                    'C) a database table',
                    'D) a Scrum ceremony',
                ],
                'A',
            ),
        },
        "exercises": [
            _quiz(
                'eit-m4-latency',
                'So‘z: latency',
                'Network.',
                'Latency means…',
                [
                    'A) delay in network response',
                    'B) free lunch',
                    'C) a type of monitor',
                    'D) a licence key',
                ],
                'A',
            ),
            _quiz(
                'eit-m4-dns',
                'So‘z: DNS',
                'Internet.',
                'DNS maps…',
                [
                    'A) domain names to IP addresses',
                    'B) passwords to printers',
                    'C) bugs to coffee',
                    'D) RAM to GPUs',
                ],
                'A',
                difficulty='medium',
            ),
        ],
        "homework": _hw(
            "English for IT — Module 4 homework\n"
            "1) Draw and label LAN devices in English.\n"
            "2) Write a 6-step Wi-Fi troubleshooting script.\n"
            "3) Glossary: router, switch, IP, DNS, HTTPS, firewall, latency, SSID.\n"
            "4) Record a 60-second explanation of why HTTPS matters."
        ),
    },
    {
        "order": 5,
        "title": 'Dasturlash inglizchasi (Programming English)',
        "slug": 'eit-programming',
        "description": 'Kod so‘z boyligi, algoritmlar haqida gapirish va Git asoslari.',
        "lectures": [
            _lec(
                'Coding vocabulary',
                'eit-code-vocab',
                """
<h2>Lesson goal</h2>
  <p>Use core coding words: bug, function, variable, compile/run in natural English.</p>

  <h2>Warm-up</h2>
  <p>What English words do you already see in code editors every day?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>code / source code</strong></td><td>instructions written by programmers</td><td>Please review my source code.</td></tr>
<tr><td><strong>bug / defect</strong></td><td>error in software</td><td>We found a critical bug.</td></tr>
<tr><td><strong>function / method</strong></td><td>reusable block of code</td><td>This function validates email.</td></tr>
<tr><td><strong>variable</strong></td><td>named storage for a value</td><td>Store the total in a variable.</td></tr>
<tr><td><strong>syntax</strong></td><td>rules for writing code correctly</td><td>There’s a syntax error on line 12.</td></tr>
<tr><td><strong>compile / runtime</strong></td><td>build time / while the program runs</td><td>It fails at runtime.</td></tr>
<tr><td><strong>library / framework</strong></td><td>ready-made code to build on</td><td>We use a UI framework.</td></tr>
<tr><td><strong>refactor</strong></td><td>improve code without changing behaviour</td><td>Let’s refactor this module.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>There’s a bug in the login flow.</li>
<li>Can you review my pull request?</li>
<li>It throws an exception at runtime.</li>
<li>I’ll add a unit test.</li>
<li>Let’s refactor before we add features.</li>
  </ul>

  <h2>Dialogue — code review</h2>
  <p><strong>Dev A:</strong> Can you review my PR?<br><strong>Dev B:</strong> Sure. There’s a naming issue in this function.<br><strong>Dev A:</strong> Good catch. I’ll rename the variable and add a test.<br><strong>Dev B:</strong> After that, it looks ready to merge.</p>

  <h2>Grammar focus — Going to / will for plans</h2>
  <ul><li>I’m <strong>going to</strong> fix the bug this afternoon.</li><li>I <strong>will</strong> add tests after lunch.</li><li>We <strong>won’t</strong> merge without a review.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Softwares has bug. → ✅ The software has a bug. / There are bugs.</li>
<li>❌ Function not working yesterday I write. → ✅ I wrote a function that didn’t work yesterday.</li>
<li>❌ Refactor means add bugs. → ✅ Refactor means improve structure.</li>
  </ul>

  <h2>Reading — Words that unblock teams</h2>
  <p>Clear coding English saves hours. Saying “null pointer on line 40 after submit” is better than “it doesn’t work.” Teams talk about functions, variables, and tests every day. Junior developers who learn these words join reviews faster and ask better questions.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Describe a bug you know using 5 vocabulary words.</li>
<li>Role-play a short code review.</li>
<li>Say your plan for today with going to / will.</li>
  </ol>

  <h2>Quick review</h2>
  <p>bug · function · variable · syntax · runtime · refactor · I’m going to…</p>
""",
            ),
            _lec(
                'Talking about algorithms',
                'eit-algorithms-talk',
                """
<h2>Lesson goal</h2>
  <p>Describe steps, complexity, and trade-offs in simple algorithmic English.</p>

  <h2>Warm-up</h2>
  <p>How do you explain a recipe? Algorithms are recipes for computers.</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>algorithm</strong></td><td>step-by-step method to solve a problem</td><td>Explain your sorting algorithm.</td></tr>
<tr><td><strong>input / output</strong></td><td>data in / result out</td><td>What is the expected output?</td></tr>
<tr><td><strong>loop</strong></td><td>repeat a set of steps</td><td>The loop runs through each item.</td></tr>
<tr><td><strong>condition</strong></td><td>yes/no check that changes the path</td><td>Add a condition for empty lists.</td></tr>
<tr><td><strong>efficiency / performance</strong></td><td>how well it uses time/memory</td><td>This approach is more efficient.</td></tr>
<tr><td><strong>edge case</strong></td><td>unusual input that may break code</td><td>Did you test edge cases?</td></tr>
<tr><td><strong>pseudocode</strong></td><td>plain-language draft of logic</td><td>Write pseudocode first.</td></tr>
<tr><td><strong>complexity (big O)</strong></td><td>rough measure of growth</td><td>This is O(n) time complexity — say it simply.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>First we take the input, then we…</li>
<li>What’s the edge case here?</li>
<li>This solution is slower but easier to read.</li>
<li>Let’s write pseudocode on the board.</li>
<li>Can we optimise this loop?</li>
  </ul>

  <h2>Dialogue — whiteboard talk</h2>
  <p><strong>Interviewer:</strong> How would you find duplicates in a list?<br><strong>Candidate:</strong> First I’d clarify the input size. Then I could use a set to track seen items.<br><strong>Interviewer:</strong> What about edge cases?<br><strong>Candidate:</strong> Empty list and all-identical values.</p>

  <h2>Grammar focus — Sequencing and passives for process</h2>
  <ul><li>The list <strong>is sorted</strong>, then duplicates <strong>are removed</strong>.</li><li><strong>After</strong> we validate input, we run the loop.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Algorithm is a hardware. → ✅ An algorithm is a method/process.</li>
<li>❌ Edge case not important. → ✅ Edge cases often cause bugs.</li>
<li>❌ Loop forever is fine. → ✅ An infinite loop is usually a bug.</li>
  </ul>

  <h2>Reading — Explain before you code</h2>
  <p>Strong engineers explain algorithms before typing. Pseudocode helps the team agree on steps. Talking about edge cases early prevents production surprises. You don’t need perfect academic language — you need clear order: input, steps, output, risks.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain a simple search in 6 sequenced sentences.</li>
<li>Name three edge cases for a login form.</li>
<li>Compare a slow clear solution vs a fast complex one.</li>
  </ol>

  <h2>Quick review</h2>
  <p>algorithm · input · loop · edge case · pseudocode · First… Then…</p>
""",
            ),
            _lec(
                'Git basics in English',
                'eit-git-basics',
                """
<h2>Lesson goal</h2>
  <p>Talk about commit, branch, merge, and pull request in workplace English.</p>

  <h2>Warm-up</h2>
  <p>Have you ever been afraid to run a Git command? You’re not alone.</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>repository (repo)</strong></td><td>project storage with history</td><td>Clone the repo first.</td></tr>
<tr><td><strong>commit</strong></td><td>saved snapshot of changes</td><td>Write a clear commit message.</td></tr>
<tr><td><strong>branch</strong></td><td>parallel line of development</td><td>Create a feature branch.</td></tr>
<tr><td><strong>merge</strong></td><td>combine changes into another branch</td><td>Merge into main after review.</td></tr>
<tr><td><strong>pull request (PR) / merge request</strong></td><td>request to review and merge</td><td>Open a PR when ready.</td></tr>
<tr><td><strong>clone</strong></td><td>copy a repo to your machine</td><td>Clone via SSH.</td></tr>
<tr><td><strong>conflict</strong></td><td>competing changes to resolve</td><td>There’s a merge conflict in app.js.</td></tr>
<tr><td><strong>push / pull</strong></td><td>send / fetch commits</td><td>Pull before you push.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>I’ll create a feature branch.</li>
<li>Please review my pull request.</li>
<li>There is a merge conflict.</li>
<li>Don’t push secrets to the repo.</li>
<li>I’ll rebase onto main — if that’s our team practice.</li>
  </ul>

  <h2>Dialogue — PR review</h2>
  <p><strong>Dev:</strong> I opened a PR for the payment fix.<br><strong>Lead:</strong> Thanks. Please resolve the conflict with main first.<br><strong>Dev:</strong> On it. Should I squash the commits?<br><strong>Lead:</strong> Yes — one clean commit message is enough.</p>

  <h2>Grammar focus — Present perfect for recent work</h2>
  <ul><li>I <strong>have pushed</strong> the fix.</li><li>She <strong>hasn’t merged</strong> the PR yet.</li><li><strong>Have you pulled</strong> the latest changes?</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ I make commit yesterday. → ✅ I committed / I made a commit yesterday.</li>
<li>❌ Push the password file. → ✅ Never commit secrets.</li>
<li>❌ Branch is a tree outside. → ✅ In Git, a branch is a line of work.</li>
  </ul>

  <h2>Reading — Small commits, clear messages</h2>
  <p>Teams move faster with small commits and clear messages: “Fix null check on login.” Pull requests invite discussion. Conflicts are normal when two people edit the same file. The goal is not to fear Git — it is to communicate what changed and why.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain clone → branch → commit → PR in order.</li>
<li>Role-play asking for a PR review.</li>
<li>Say three present-perfect sentences about your Git day.</li>
  </ol>

  <h2>Quick review</h2>
  <p>repo · commit · branch · merge · PR · conflict · I have pushed…</p>
""",
            ),
        ],
        "practice": {
            'eit-code-vocab': _quiz(
                'eit-q-bug',
                'So‘z: bug',
                'Coding.',
                'A bug is…',
                [
                    'A) an error in software',
                    'B) a type of monitor',
                    'C) a Wi-Fi password',
                    'D) a meeting room',
                ],
                'A',
            ),
            'eit-algorithms-talk': _quiz(
                'eit-q-edge',
                'So‘z: edge case',
                'Algorithms.',
                'An edge case is…',
                [
                    'A) unusual input that may break code',
                    'B) the office edge of a desk',
                    'C) a GPU brand',
                    'D) a Scrum snack',
                ],
                'A',
            ),
            'eit-git-basics': _quiz(
                'eit-q-pr',
                'So‘z: pull request',
                'Git.',
                'A pull request is…',
                [
                    'A) a request to review and merge changes',
                    'B) a hardware upgrade',
                    'C) a phishing email',
                    'D) a database backup only',
                ],
                'A',
            ),
        },
        "exercises": [
            _quiz(
                'eit-m5-refactor',
                'So‘z: refactor',
                'Code.',
                'To refactor means…',
                [
                    'A) improve code without changing behaviour',
                    'B) delete the repository forever',
                    'C) buy a new laptop',
                    'D) turn off the firewall',
                ],
                'A',
            ),
            _quiz(
                'eit-m5-present-perfect',
                'Grammar: present perfect',
                'Git.',
                'Correct sentence:',
                [
                    'A) I have pushed the fix.',
                    'B) I have push the fix.',
                    'C) I pushing have fix.',
                    'D) Push I have yesterdayed.',
                ],
                'A',
                difficulty='medium',
            ),
        ],
        "homework": _hw(
            "English for IT — Module 5 homework\n"
            "1) Write 10 sentences using bug, function, branch, commit, PR.\n"
            "2) Explain a simple algorithm in pseudocode English.\n"
            "3) Record a 45-second PR description.\n"
            "4) Glossary of 12 programming/Git terms."
        ),
    },
    {
        "order": 6,
        "title": 'Ma’lumotlar bazasi (Databases)',
        "slug": 'eit-databases',
        "description": 'DB tushunchalari, SQL haqida gapirish va ma’lumot maxfiyligi.',
        "lectures": [
            _lec(
                'Database concepts',
                'eit-db-concepts',
                """
<h2>Lesson goal</h2>
  <p>Explain database, table, row, primary key, and relational basics in English.</p>

  <h2>Warm-up</h2>
  <p>Where does a website store users and orders — in files only, or in a database?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>database (DB)</strong></td><td>organised collection of data</td><td>Customer data is in the database.</td></tr>
<tr><td><strong>table</strong></td><td>grid of related records</td><td>The users table has emails.</td></tr>
<tr><td><strong>row / record</strong></td><td>one item in a table</td><td>Insert a new row for each order.</td></tr>
<tr><td><strong>column / field</strong></td><td>one attribute in a table</td><td>The email column must be unique.</td></tr>
<tr><td><strong>primary key</strong></td><td>unique ID for a row</td><td>id is the primary key.</td></tr>
<tr><td><strong>foreign key</strong></td><td>reference to another table’s key</td><td>user_id is a foreign key.</td></tr>
<tr><td><strong>query</strong></td><td>request for data</td><td>Run a query to find inactive users.</td></tr>
<tr><td><strong>index</strong></td><td>structure that speeds up lookups</td><td>Add an index on email.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Which table stores orders?</li>
<li>We need a unique primary key.</li>
<li>Don’t delete production rows without a backup.</li>
<li>The query is too slow.</li>
<li>Is there a foreign key relationship?</li>
  </ul>

  <h2>Dialogue — modelling users</h2>
  <p><strong>Analyst:</strong> Should email be the primary key?<br><strong>DBA:</strong> Better use a numeric id. Email can be unique, but people change emails.<br><strong>Analyst:</strong> And orders?<br><strong>DBA:</strong> orders.user_id will be a foreign key to users.id.</p>

  <h2>Grammar focus — Articles a/an/the with tech nouns</h2>
  <ul><li>We need <strong>a</strong> primary key.</li><li><strong>The</strong> users table is large.</li><li>Add <strong>an</strong> index on email.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Datas are many. → ✅ Data is often uncountable: a lot of data / many records.</li>
<li>❌ Primary key is password. → ✅ A primary key uniquely identifies a row.</li>
<li>❌ Delete table for fun. → ✅ Never drop production tables casually.</li>
  </ul>

  <h2>Reading — Why keys matter</h2>
  <p>Relational databases organise data into tables linked by keys. A clear primary key prevents duplicates. Foreign keys keep relationships consistent. When teams say “the query is slow,” they may need an index — or a simpler question. Good English helps developers and analysts design together.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain table, row, and primary key in one minute.</li>
<li>Role-play designing users and orders.</li>
<li>Warn a junior about deleting production data.</li>
  </ol>

  <h2>Quick review</h2>
  <p>database · table · row · primary key · foreign key · query · index</p>
""",
            ),
            _lec(
                'Talking about SQL',
                'eit-sql-talk',
                """
<h2>Lesson goal</h2>
  <p>Describe SELECT, INSERT, UPDATE, DELETE and joins in workplace conversation.</p>

  <h2>Warm-up</h2>
  <p>Have you seen SQL keywords in ALL CAPS? Why do people write them that way?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>SELECT</strong></td><td>read data from tables</td><td>SELECT name FROM users;</td></tr>
<tr><td><strong>INSERT</strong></td><td>add new rows</td><td>INSERT a new customer record.</td></tr>
<tr><td><strong>UPDATE</strong></td><td>change existing rows</td><td>UPDATE the status to closed.</td></tr>
<tr><td><strong>DELETE</strong></td><td>remove rows</td><td>DELETE only with a WHERE clause.</td></tr>
<tr><td><strong>JOIN</strong></td><td>combine rows from related tables</td><td>JOIN orders and users on user_id.</td></tr>
<tr><td><strong>WHERE clause</strong></td><td>filter for rows</td><td>Filter inactive accounts in the WHERE clause.</td></tr>
<tr><td><strong>backup</strong></td><td>copy of data for recovery</td><td>Take a backup before migration.</td></tr>
<tr><td><strong>migration</strong></td><td>structured change to the schema/data</td><td>We run migrations in CI.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Can you write a SELECT for active users?</li>
<li>Never run DELETE without WHERE in production.</li>
<li>We’ll JOIN these two tables.</li>
<li>Please take a backup first.</li>
<li>The migration failed on staging.</li>
  </ul>

  <h2>Dialogue — dangerous delete</h2>
  <p><strong>Junior:</strong> I’ll delete old rows to clean the table.<br><strong>Senior:</strong> Stop — do you have a WHERE clause and a backup?<br><strong>Junior:</strong> Not yet.<br><strong>Senior:</strong> Good catch to ask. Let’s filter by date and test on staging first.</p>

  <h2>Grammar focus — Imperatives and warnings</h2>
  <ul><li><strong>Always</strong> filter deletes.</li><li><strong>Don’t</strong> run untested SQL on production.</li><li><strong>Make sure</strong> you have a backup.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Select all then think. → ✅ Know your filters before you run heavy queries.</li>
<li>❌ Join is only coffee. → ✅ In SQL, JOIN combines related tables.</li>
<li>❌ Update yesterday I the table. → ✅ I updated the table yesterday.</li>
  </ul>

  <h2>Reading — Read before you write</h2>
  <p>In production, reading data is common; writing data needs care. Teams practise SELECT skills daily. Migrations change structure safely when tested. The English you use in chat — “Can someone review this UPDATE?” — is part of database safety culture.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain SELECT vs UPDATE in simple English.</li>
<li>Give three safety rules for DELETE.</li>
<li>Describe a JOIN between users and orders.</li>
  </ol>

  <h2>Quick review</h2>
  <p>SELECT · INSERT · UPDATE · DELETE · JOIN · WHERE · backup · Don’t…</p>
""",
            ),
            _lec(
                'Data privacy basics',
                'eit-data-privacy',
                """
<h2>Lesson goal</h2>
  <p>Talk about personal data, consent, and safe handling in IT English.</p>

  <h2>Warm-up</h2>
  <p>Should anyone in the company be able to download all customer emails? Why not?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>personal data</strong></td><td>information about an identifiable person</td><td>Email can be personal data.</td></tr>
<tr><td><strong>privacy</strong></td><td>control over personal information</td><td>We respect user privacy.</td></tr>
<tr><td><strong>consent</strong></td><td>permission to use data</td><td>We need consent for marketing emails.</td></tr>
<tr><td><strong>encrypt</strong></td><td>encode data to protect it</td><td>Encrypt passwords and sensitive fields.</td></tr>
<tr><td><strong>anonymise / anonymize</strong></td><td>remove identifying details</td><td>Anonymise data used for demos.</td></tr>
<tr><td><strong>access control</strong></td><td>rules for who can see data</td><td>Tighten access control on HR tables.</td></tr>
<tr><td><strong>breach</strong></td><td>unauthorised access or leak</td><td>Report a suspected breach immediately.</td></tr>
<tr><td><strong>GDPR / data protection rules</strong></td><td>common legal frameworks (awareness)</td><td>Follow our data protection policy.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>This field contains personal data.</li>
<li>Please don’t share exports in public chat.</li>
<li>We should encrypt sensitive columns.</li>
<li>Report a breach to security now.</li>
<li>Do we have consent to use this list?</li>
  </ul>

  <h2>Dialogue — export request</h2>
  <p><strong>Marketer:</strong> Can you send me the full customer database?<br><strong>Engineer:</strong> I can’t send everything. We need a filtered export and approval.<br><strong>Marketer:</strong> I only need emails of users who opted in.<br><strong>Engineer:</strong> Perfect — that’s consent-based. I’ll prepare an anonymised report where possible.</p>

  <h2>Grammar focus — Should / shouldn’t for advice</h2>
  <ul><li>You <strong>should</strong> encrypt personal data.</li><li>You <strong>shouldn’t</strong> email password lists.</li><li>We <strong>should</strong> limit access to need-to-know.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Privacy is only for lawyers. → ✅ Engineers handle personal data every day.</li>
<li>❌ Encrypt means delete. → ✅ Encrypt means protect by encoding.</li>
<li>❌ Breach ignore until Monday. → ✅ Report breaches immediately.</li>
  </ul>

  <h2>Reading — Need to know</h2>
  <p>Modern IT work includes privacy. Personal data needs access control, encryption, and clear purpose. A breach can hurt users and the company. Speaking up — “This export looks too wide” — is professional, not rude.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain personal data with two examples.</li>
<li>Role-play refusing an unsafe full-database export.</li>
<li>Give four should/shouldn’t privacy tips.</li>
  </ol>

  <h2>Quick review</h2>
  <p>personal data · privacy · consent · encrypt · breach · should / shouldn’t</p>
""",
            ),
        ],
        "practice": {
            'eit-db-concepts': _quiz(
                'eit-q-pk',
                'So‘z: primary key',
                'DB.',
                'A primary key…',
                [
                    'A) uniquely identifies a row',
                    'B) prints invoices',
                    'C) is a Wi-Fi password',
                    'D) deletes DNS',
                ],
                'A',
            ),
            'eit-sql-talk': _quiz(
                'eit-q-where',
                'SQL safety',
                'SQL.',
                'Best advice for DELETE:',
                [
                    'A) Use a WHERE clause and prefer backups/tests',
                    'B) Delete everything in production first',
                    'C) Never use WHERE',
                    'D) Only delete on Fridays for luck',
                ],
                'A',
            ),
            'eit-data-privacy': _quiz(
                'eit-q-encrypt',
                'So‘z: encrypt',
                'Privacy.',
                'To encrypt data means…',
                [
                    'A) encode it to protect confidentiality',
                    'B) print it on posters',
                    'C) share it on social media',
                    'D) translate it to Latin',
                ],
                'A',
            ),
        },
        "exercises": [
            _quiz(
                'eit-m6-join',
                'So‘z: JOIN',
                'SQL.',
                'A JOIN is used to…',
                [
                    'A) combine rows from related tables',
                    'B) restart the router',
                    'C) design a logo',
                    'D) create a Slack channel',
                ],
                'A',
            ),
            _quiz(
                'eit-m6-breach',
                'So‘z: breach',
                'Privacy.',
                'A data breach is…',
                [
                    'A) unauthorised access or a data leak',
                    'B) a successful backup',
                    'C) a type of SSD',
                    'D) a friendly merge',
                ],
                'A',
                difficulty='medium',
            ),
        ],
        "homework": _hw(
            "English for IT — Module 6 homework\n"
            "1) Draw users/orders tables and label keys in English.\n"
            "2) Write 8 should/shouldn’t privacy sentences.\n"
            "3) Record a 60-second warning about DELETE without WHERE.\n"
            "4) Glossary: table, primary key, JOIN, backup, encrypt, consent, breach, query."
        ),
    },
    {
        "order": 7,
        "title": 'Veb dasturlash (Web development)',
        "slug": 'eit-web',
        "description": 'Frontend/backend, API/HTTP va veb deploy haqida inglizcha.',
        "lectures": [
            _lec(
                'Frontend and backend',
                'eit-frontend-backend',
                """
<h2>Lesson goal</h2>
  <p>Contrast frontend and backend roles and technologies in clear English.</p>

  <h2>Warm-up</h2>
  <p>When you click a button on a website, where does the work happen?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>frontend</strong></td><td>user-facing part of an app</td><td>She works on the frontend UI.</td></tr>
<tr><td><strong>backend</strong></td><td>server-side logic and data</td><td>Backend handles payments.</td></tr>
<tr><td><strong>UI / UX</strong></td><td>user interface / user experience</td><td>Improve the UI for mobile.</td></tr>
<tr><td><strong>HTML / CSS / JavaScript</strong></td><td>common frontend building blocks</td><td>HTML structures the page.</td></tr>
<tr><td><strong>server</strong></td><td>computer that responds to requests</td><td>The server returned an error.</td></tr>
<tr><td><strong>client</strong></td><td>browser or app that requests</td><td>The client sends a request.</td></tr>
<tr><td><strong>full-stack</strong></td><td>works across frontend and backend</td><td>We’re hiring a full-stack developer.</td></tr>
<tr><td><strong>responsive</strong></td><td>layout adapts to screen size</td><td>Make the page responsive.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>I’m a frontend developer.</li>
<li>The bug is on the backend.</li>
<li>Is this a UI issue or an API issue?</li>
<li>The page isn’t responsive on mobile.</li>
<li>Let’s reproduce it in the browser first.</li>
  </ul>

  <h2>Dialogue — who owns the bug?</h2>
  <p><strong>PM:</strong> The total looks wrong on the screen.<br><strong>Frontend:</strong> The UI shows what the API returns.<br><strong>Backend:</strong> I’ll check the calculation in the service.<br><strong>PM:</strong> Great — please update the ticket with findings.</p>

  <h2>Grammar focus — Present simple for roles + present continuous for current work</h2>
  <ul><li>I <strong>build</strong> UI components. (role/habit)</li><li>I <strong>am fixing</strong> the mobile layout today. (current)</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Frontend is only colours. → ✅ Frontend includes structure, behaviour, and accessibility.</li>
<li>❌ Backend is the keyboard. → ✅ Backend is server-side logic/data.</li>
<li>❌ Client always means customer person. → ✅ In web talk, client often means browser/app.</li>
  </ul>

  <h2>Reading — One product, two sides</h2>
  <p>Modern web products split work: frontend shapes what users see; backend stores data and enforces rules. Full-stack engineers bridge both. Clear tickets say whether the issue is UI display or server logic — that single sentence can save a day of confusion.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain frontend vs backend with examples.</li>
<li>Describe your preferred side and why (4 sentences).</li>
<li>Role-play assigning a bug to the right team.</li>
  </ol>

  <h2>Quick review</h2>
  <p>frontend · backend · UI · server · client · responsive · full-stack</p>
""",
            ),
            _lec(
                'APIs and HTTP',
                'eit-apis-http',
                """
<h2>Lesson goal</h2>
  <p>Talk about APIs, endpoints, status codes, and JSON in everyday team English.</p>

  <h2>Warm-up</h2>
  <p>What happens when an app says “500 Internal Server Error”?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>API</strong></td><td>interface for software to talk to software</td><td>We call the payments API.</td></tr>
<tr><td><strong>endpoint</strong></td><td>specific API URL/route</td><td>POST /api/login is an endpoint.</td></tr>
<tr><td><strong>request / response</strong></td><td>what you send / what you get</td><td>Check the response body.</td></tr>
<tr><td><strong>HTTP method</strong></td><td>GET, POST, PUT, DELETE, etc.</td><td>Use GET to read data.</td></tr>
<tr><td><strong>status code</strong></td><td>number showing result (200, 404, 500…)</td><td>We got a 404 status code.</td></tr>
<tr><td><strong>JSON</strong></td><td>common data format for APIs</td><td>The API returns JSON.</td></tr>
<tr><td><strong>authentication</strong></td><td>proving who you are</td><td>Add a token for authentication.</td></tr>
<tr><td><strong>rate limit</strong></td><td>max calls allowed in a time window</td><td>We hit the rate limit.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>The endpoint returns 500.</li>
<li>Please share the request payload.</li>
<li>We need an auth token.</li>
<li>Is this GET or POST?</li>
<li>The JSON field is missing.</li>
  </ul>

  <h2>Dialogue — debugging an API call</h2>
  <p><strong>Mobile dev:</strong> Login fails with 401.<br><strong>Backend:</strong> 401 means unauthorised — is the token expired?<br><strong>Mobile dev:</strong> Possibly. I’ll refresh the token and retry.<br><strong>Backend:</strong> If it still fails, send me the request headers (without secrets).</p>

  <h2>Grammar focus — Zero / first conditional for debugging</h2>
  <ul><li>If the token is missing, the API <strong>returns</strong> 401.</li><li>If we hit the rate limit, we <strong>will wait</strong> and retry.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ 404 means server exploded. → ✅ 404 often means not found.</li>
<li>❌ API is a type of keyboard. → ✅ API is a software interface.</li>
<li>❌ JSON is a person. → ✅ JSON is a data format.</li>
  </ul>

  <h2>Reading — Status codes tell a story</h2>
  <p>HTTP status codes communicate outcomes quickly: 200 OK, 400 bad request, 401 unauthorised, 404 not found, 500 server error. Teams paste statuses into tickets because they shrink investigation time. Learning to say them confidently is practical English for web work.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain API and endpoint in simple words.</li>
<li>Say what 401, 404, and 500 usually mean.</li>
<li>Role-play debugging a failed login call.</li>
  </ol>

  <h2>Quick review</h2>
  <p>API · endpoint · GET/POST · status code · JSON · token · If…</p>
""",
            ),
            _lec(
                'Deploying web apps',
                'eit-deploy-web',
                """
<h2>Lesson goal</h2>
  <p>Describe environments, deploy, rollback, and downtime in calm release English.</p>

  <h2>Warm-up</h2>
  <p>Would you deploy untested code on Friday evening? Why or why not?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>deploy</strong></td><td>release software to an environment</td><td>We deploy to production tonight.</td></tr>
<tr><td><strong>environment</strong></td><td>dev / staging / production setup</td><td>Test on staging first.</td></tr>
<tr><td><strong>production (prod)</strong></td><td>live system used by real users</td><td>Be careful in production.</td></tr>
<tr><td><strong>staging</strong></td><td>pre-prod testing environment</td><td>Reproduce the bug on staging.</td></tr>
<tr><td><strong>release</strong></td><td>version shipped to users</td><td>Release notes are ready.</td></tr>
<tr><td><strong>downtime</strong></td><td>period when service is unavailable</td><td>Expect five minutes of downtime.</td></tr>
<tr><td><strong>rollback</strong></td><td>return to previous release</td><td>Rollback if error rates rise.</td></tr>
<tr><td><strong>CI/CD</strong></td><td>automated integrate/deploy pipelines</td><td>CI/CD runs tests on every commit.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Don’t deploy directly to production.</li>
<li>Staging looks good — ready to release?</li>
<li>We’ll announce downtime in Slack.</li>
<li>Rollback now — error rate is high.</li>
<li>CI failed on the build.</li>
  </ul>

  <h2>Dialogue — release decision</h2>
  <p><strong>DevOps:</strong> Staging tests passed. Deploy to prod?<br><strong>Lead:</strong> Yes, but start with a small canary if we can.<br><strong>DevOps:</strong> Understood. I’ll watch the dashboards for 15 minutes.<br><strong>Lead:</strong> If latency spikes, roll back immediately.</p>

  <h2>Grammar focus — will / going to for release plans</h2>
  <ul><li>We <strong>are going to</strong> deploy at 20:00.</li><li>We <strong>will</strong> roll back if errors increase.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Production is a movie. → ✅ Production is the live environment.</li>
<li>❌ Deploy means delete servers. → ✅ Deploy means release/ship software.</li>
<li>❌ Downtime always secret. → ✅ Announce planned downtime early.</li>
  </ul>

  <h2>Reading — Staging is a safety net</h2>
  <p>Professional teams rarely jump from laptop to production. Staging catches surprises. CI/CD automates checks. Rollback plans turn panic into process. The English of releases — clear time, risk, owner — is as important as the scripts.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain dev vs staging vs production.</li>
<li>Announce a 10-minute downtime politely.</li>
<li>Role-play a rollback decision.</li>
  </ol>

  <h2>Quick review</h2>
  <p>deploy · staging · production · downtime · rollback · CI/CD · We will…</p>
""",
            ),
        ],
        "practice": {
            'eit-frontend-backend': _quiz(
                'eit-q-frontend',
                'So‘z: frontend',
                'Web.',
                'Frontend mainly means…',
                [
                    'A) the user-facing part of an app',
                    'B) only the database cables',
                    'C) a type of phishing',
                    'D) the office kitchen',
                ],
                'A',
            ),
            'eit-apis-http': _quiz(
                'eit-q-404',
                'Status code',
                'HTTP.',
                'A 404 status usually means…',
                [
                    'A) not found',
                    'B) success always',
                    'C) printer offline only',
                    'D) battery empty',
                ],
                'A',
            ),
            'eit-deploy-web': _quiz(
                'eit-q-staging',
                'So‘z: staging',
                'Deploy.',
                'Staging is…',
                [
                    'A) a pre-production testing environment',
                    'B) a theatre hobby only',
                    'C) a GPU brand',
                    'D) a Wi-Fi SSID',
                ],
                'A',
            ),
        },
        "exercises": [
            _quiz(
                'eit-m7-api',
                'So‘z: API',
                'Web.',
                'An API lets software…',
                [
                    'A) communicate with other software',
                    'B) cook lunch',
                    'C) replace the monitor',
                    'D) invent passwords for fun',
                ],
                'A',
            ),
            _quiz(
                'eit-m7-rollback',
                'Deploy',
                'Release.',
                'If production errors spike, teams often…',
                [
                    'A) roll back to a previous release',
                    'B) delete the company domain',
                    'C) ignore dashboards forever',
                    'D) turn off all backups',
                ],
                'A',
                difficulty='medium',
            ),
        ],
        "homework": _hw(
            "English for IT — Module 7 homework\n"
            "1) Write a short frontend vs backend comparison (10 sentences).\n"
            "2) Glossary: API, endpoint, JSON, status code, deploy, staging, production, rollback.\n"
            "3) Record a 45-second release announcement.\n"
            "4) Explain 401/404/500 with examples."
        ),
    },
    {
        "order": 8,
        "title": 'Cloud va DevOps',
        "slug": 'eit-cloud-devops',
        "description": 'Cloud asoslari, konteynerlar/CI va monitoring.',
        "lectures": [
            _lec(
                'Cloud basics',
                'eit-cloud-basics',
                """
<h2>Lesson goal</h2>
  <p>Explain cloud computing, regions, and IaaS/PaaS/SaaS ideas in simple English.</p>

  <h2>Warm-up</h2>
  <p>Is “the cloud” a real place in the sky? What is it really?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>cloud computing</strong></td><td>using remote servers over the internet</td><td>We host the app in the cloud.</td></tr>
<tr><td><strong>provider (AWS/Azure/GCP…)</strong></td><td>company offering cloud services</td><td>Which cloud provider do you use?</td></tr>
<tr><td><strong>region / availability zone</strong></td><td>geographic cloud location units</td><td>Deploy closer to users’ region.</td></tr>
<tr><td><strong>scalability</strong></td><td>ability to grow with demand</td><td>Cloud helps with scalability.</td></tr>
<tr><td><strong>IaaS / PaaS / SaaS</strong></td><td>infrastructure / platform / software as a service</td><td>Gmail is a SaaS example.</td></tr>
<tr><td><strong>instance / VM</strong></td><td>virtual server</td><td>Start a new VM instance.</td></tr>
<tr><td><strong>storage bucket</strong></td><td>object storage container</td><td>Upload images to a storage bucket.</td></tr>
<tr><td><strong>cost / billing</strong></td><td>money charged for usage</td><td>Watch cloud billing this month.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>We deployed to the Frankfurt region.</li>
<li>Please don’t leave idle instances running.</li>
<li>Is this IaaS or PaaS?</li>
<li>We need better scalability for Black Friday.</li>
<li>Check the billing dashboard.</li>
  </ul>

  <h2>Dialogue — choosing a region</h2>
  <p><strong>Dev:</strong> Users in Asia see high latency.<br><strong>Cloud eng:</strong> Let’s deploy closer to their region.<br><strong>Dev:</strong> Will that increase cost?<br><strong>Cloud eng:</strong> A bit — but performance should improve. We’ll monitor both.</p>

  <h2>Grammar focus — Comparatives for cloud choices</h2>
  <ul><li>This region is <strong>closer</strong> and <strong>faster</strong> for local users.</li><li>Managed PaaS can be <strong>easier</strong> than raw VMs.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Cloud is only weather. → ✅ In IT, cloud means remote computing services.</li>
<li>❌ Scalability means delete users. → ✅ Scalability means handling growth.</li>
<li>❌ Leave VMs on forever free. → ✅ Idle resources still cost money.</li>
  </ul>

  <h2>Reading — Pay for what you use</h2>
  <p>Cloud services rent computing power and storage. Teams choose regions for speed and compliance. Scalability helps during traffic spikes. Billing surprises happen when unused instances stay on. Clear English in tickets — “Please stop idle VMs in staging” — protects the budget.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain cloud computing without saying ‘magic’.</li>
<li>Give one example each of SaaS and IaaS.</li>
<li>Discuss region choice for latency.</li>
  </ol>

  <h2>Quick review</h2>
  <p>cloud · region · scalability · IaaS/PaaS/SaaS · VM · billing</p>
""",
            ),
            _lec(
                'Containers and CI',
                'eit-containers-ci',
                """
<h2>Lesson goal</h2>
  <p>Talk about containers, Docker images, and continuous integration pipelines.</p>

  <h2>Warm-up</h2>
  <p>Why do developers say “it works on my machine”? How can containers help?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>container</strong></td><td>packaged app with dependencies</td><td>Run the service in a container.</td></tr>
<tr><td><strong>Docker image</strong></td><td>template used to create containers</td><td>Build a new Docker image.</td></tr>
<tr><td><strong>CI (continuous integration)</strong></td><td>auto-build/test on each change</td><td>CI failed on unit tests.</td></tr>
<tr><td><strong>pipeline</strong></td><td>automated sequence of CI/CD steps</td><td>Fix the pipeline yaml.</td></tr>
<tr><td><strong>build</strong></td><td>compile/package process</td><td>The build is green.</td></tr>
<tr><td><strong>artifact</strong></td><td>output of a build</td><td>Upload the artifact to the registry.</td></tr>
<tr><td><strong>registry</strong></td><td>storage for images/packages</td><td>Push the image to the registry.</td></tr>
<tr><td><strong>orchestration (e.g. Kubernetes)</strong></td><td>managing many containers</td><td>Orchestration schedules containers.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>The CI pipeline is red.</li>
<li>Please rebuild the image.</li>
<li>Don’t commit secrets into Dockerfiles.</li>
<li>Tests must pass before merge.</li>
<li>Push the image to the registry.</li>
  </ul>

  <h2>Dialogue — red pipeline</h2>
  <p><strong>Dev:</strong> Why is CI red?<br><strong>Teammate:</strong> Unit tests failed after your last commit.<br><strong>Dev:</strong> I’ll fix them and push again.<br><strong>Teammate:</strong> Thanks — green builds keep deploys safe.</p>

  <h2>Grammar focus — Must / have to for pipeline rules</h2>
  <ul><li>Tests <strong>must</strong> pass before merge.</li><li>We <strong>have to</strong> keep secrets out of images.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Container is only a box for food. → ✅ In DevOps, a container packages software.</li>
<li>❌ CI means see you. → ✅ CI means continuous integration.</li>
<li>❌ Pipeline is only oil. → ✅ Here, pipeline means automated build/deploy steps.</li>
  </ul>

  <h2>Reading — Same everywhere</h2>
  <p>Containers reduce “works on my machine” problems by packaging dependencies. CI runs the same checks for every change. Pipelines fail loudly so humans can fix issues early. Learning to describe a red build clearly is everyday DevOps English.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain container vs VM in simple terms.</li>
<li>Describe what CI does in 4 sentences.</li>
<li>Role-play reporting a failed pipeline.</li>
  </ol>

  <h2>Quick review</h2>
  <p>container · image · CI · pipeline · build · registry · must pass</p>
""",
            ),
            _lec(
                'Monitoring and alerts',
                'eit-monitoring',
                """
<h2>Lesson goal</h2>
  <p>Discuss logs, metrics, alerts, and on-call communication calmly.</p>

  <h2>Warm-up</h2>
  <p>If a service is slow at 2 a.m., who should know first — and how?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>monitoring</strong></td><td>watching system health</td><td>We improved monitoring last sprint.</td></tr>
<tr><td><strong>logs</strong></td><td>recorded events from systems</td><td>Check the error logs.</td></tr>
<tr><td><strong>metrics</strong></td><td>numeric measurements over time</td><td>CPU metrics look high.</td></tr>
<tr><td><strong>alert</strong></td><td>notification about a problem</td><td>I got a PagerDuty alert.</td></tr>
<tr><td><strong>dashboard</strong></td><td>visual overview of metrics</td><td>Open the latency dashboard.</td></tr>
<tr><td><strong>uptime / downtime</strong></td><td>time available / unavailable</td><td>Uptime was 99.9% this month.</td></tr>
<tr><td><strong>incident</strong></td><td>serious service disruption</td><td>We’re in an incident call.</td></tr>
<tr><td><strong>on-call</strong></td><td>person available to respond</td><td>I’m on-call this week.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Check the logs for stack traces.</li>
<li>Latency metrics spiked at 14:02.</li>
<li>Acknowledge the alert, please.</li>
<li>Declare an incident if users are blocked.</li>
<li>I’ll take the on-call handover.</li>
  </ul>

  <h2>Dialogue — alert triage</h2>
  <p><strong>On-call:</strong> Alert: API error rate above 5%.<br><strong>Teammate:</strong> Are users impacted?<br><strong>On-call:</strong> Yes — checkout fails. I’m declaring an incident.<br><strong>Teammate:</strong> I’ll join the bridge and watch the dashboard.</p>

  <h2>Grammar focus — Past simple for incident timelines</h2>
  <ul><li>Errors <strong>started</strong> at 14:02.</li><li>We <strong>rolled back</strong> at 14:20.</li><li>Service <strong>recovered</strong> at 14:25.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Ignore alerts until morning. → ✅ Acknowledge and triage important alerts.</li>
<li>❌ Logs are only wood. → ✅ In IT, logs are system event records.</li>
<li>❌ Incident means birthday. → ✅ An incident is a serious disruption.</li>
  </ul>

  <h2>Reading — See problems early</h2>
  <p>Monitoring turns invisible failures into visible signals. Metrics show trends; logs show detail; alerts call humans. Clear timelines in English help postmortems: what happened, when, and what fixed it. Calm words beat panic in the middle of the night.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain logs vs metrics.</li>
<li>Role-play an on-call alert conversation.</li>
<li>Narrate a short incident timeline in past simple.</li>
  </ol>

  <h2>Quick review</h2>
  <p>monitoring · logs · metrics · alert · incident · on-call · started / recovered</p>
""",
            ),
        ],
        "practice": {
            'eit-cloud-basics': _quiz(
                'eit-q-cloud',
                'So‘z: cloud',
                'Cloud.',
                'Cloud computing means…',
                [
                    'A) using remote servers over the internet',
                    'B) only weather forecasting',
                    'C) printing on paper clouds',
                    'D) deleting all networks',
                ],
                'A',
            ),
            'eit-containers-ci': _quiz(
                'eit-q-ci',
                'So‘z: CI',
                'DevOps.',
                'Continuous integration (CI) mainly…',
                [
                    'A) automatically builds/tests changes',
                    'B) cooks continuous meals',
                    'C) replaces keyboards',
                    'D) turns off monitoring',
                ],
                'A',
            ),
            'eit-monitoring': _quiz(
                'eit-q-alert',
                'So‘z: alert',
                'Ops.',
                'An alert is…',
                [
                    'A) a notification about a possible problem',
                    'B) a type of SSD',
                    'C) a Scrum snack',
                    'D) a CSS colour',
                ],
                'A',
            ),
        },
        "exercises": [
            _quiz(
                'eit-m8-saas',
                'So‘z: SaaS',
                'Cloud.',
                'SaaS examples are usually…',
                [
                    'A) ready software used over the internet',
                    'B) raw metal servers you rack yourself always',
                    'C) HDMI cables',
                    'D) mechanical keyboards only',
                ],
                'A',
            ),
            _quiz(
                'eit-m8-incident',
                'So‘z: incident',
                'Monitoring.',
                'An incident is…',
                [
                    'A) a serious service disruption',
                    'B) a successful unit test',
                    'C) a new emoji',
                    'D) a holiday calendar',
                ],
                'A',
                difficulty='medium',
            ),
        ],
        "homework": _hw(
            "English for IT — Module 8 homework\n"
            "1) Explain IaaS vs SaaS with examples (8 sentences).\n"
            "2) Write a red-CI report template in English.\n"
            "3) Glossary: region, container, pipeline, metrics, alert, incident, on-call, rollback.\n"
            "4) Record a 60-second on-call handover."
        ),
    },
]


def build_english_it_modules():
    from apps.core.english_it_academic import ACADEMIC_MODULE, enrich_modules
    from apps.core.english_it_interview import INTERVIEW_MODULE
    from apps.core.english_it_modules_extra import EXTRA_MODULES

    head = [m for m in MODULES if m["order"] <= 8]
    return enrich_modules(head + list(EXTRA_MODULES) + [ACADEMIC_MODULE, INTERVIEW_MODULE])
