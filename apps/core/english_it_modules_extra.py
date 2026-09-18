"""
Extra English-for-IT modules (9–15) — cybersecurity through career English.
Merged in english_it_content.build_english_it_modules().
"""

from apps.core.english_it_content import _hw, _lec, _quiz

EXTRA_MODULES = [
    {
        "order": 9,
        "title": 'Kiberxavfsizlik (Cybersecurity)',
        "slug": 'eit-cybersecurity',
        "description": 'Xavfsizlik asoslari, parol/MFA va phishingdan himoya.',
        "lectures": [
            _lec(
                'Security basics',
                'eit-security-basics',
                """
<h2>Lesson goal</h2>
  <p>Explain threats, vulnerabilities, and basic security hygiene in clear English.</p>

  <h2>Warm-up</h2>
  <p>What is more dangerous: a weak password or an unpatched server? Why?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>cybersecurity</strong></td><td>protecting systems and data from attacks</td><td>Cybersecurity is everyone’s job.</td></tr>
<tr><td><strong>threat</strong></td><td>possible danger</td><td>Phishing is a common threat.</td></tr>
<tr><td><strong>vulnerability</strong></td><td>weakness that can be exploited</td><td>Unpatched software is a vulnerability.</td></tr>
<tr><td><strong>attack / breach</strong></td><td>malicious action / successful intrusion</td><td>The attack caused a breach.</td></tr>
<tr><td><strong>malware</strong></td><td>harmful software</td><td>Don’t open files that may contain malware.</td></tr>
<tr><td><strong>firewall</strong></td><td>traffic filter for protection</td><td>The firewall blocked the scan.</td></tr>
<tr><td><strong>patch</strong></td><td>fix for a security weakness</td><td>Apply security patches weekly.</td></tr>
<tr><td><strong>risk</strong></td><td>chance of harm and impact</td><td>We must reduce the risk.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Report suspicious activity immediately.</li>
<li>This system looks vulnerable.</li>
<li>Apply the security patch today.</li>
<li>Don’t disable the firewall.</li>
<li>What’s the risk if we wait?</li>
  </ul>

  <h2>Dialogue — unpatched server</h2>
  <p><strong>Sec:</strong> This server is missing critical patches.<br><strong>Ops:</strong> Can we schedule downtime tonight?<br><strong>Sec:</strong> Yes — the vulnerability is actively exploited elsewhere.<br><strong>Ops:</strong> Understood. I’ll announce maintenance.</p>

  <h2>Grammar focus — Modals for safety: must / shouldn’t / might</h2>
  <ul><li>You <strong>must</strong> report breaches.</li><li>You <strong>shouldn’t</strong> ignore alerts.</li><li>The attachment <strong>might</strong> be malware.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Security is only IT police job. → ✅ Everyone shares security responsibility.</li>
<li>❌ Vulnerability means sad feeling only. → ✅ In IT, it means a weakness.</li>
<li>❌ Patch means cloth always. → ✅ Here, patch means a software fix.</li>
  </ul>

  <h2>Reading — Small habits, big protection</h2>
  <p>Most incidents start with simple gaps: old software, weak access, rushed clicks. Security English helps teams act: name the threat, estimate the risk, apply the patch. You don’t need fear — you need clear, calm action words.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Define threat vs vulnerability.</li>
<li>Give five must/shouldn’t security rules.</li>
<li>Role-play scheduling emergency patching.</li>
  </ol>

  <h2>Quick review</h2>
  <p>cybersecurity · threat · vulnerability · malware · patch · must / might</p>
""",
            ),
            _lec(
                'Passwords and MFA',
                'eit-passwords-mfa',
                """
<h2>Lesson goal</h2>
  <p>Talk about strong passwords, password managers, and multi-factor authentication.</p>

  <h2>Warm-up</h2>
  <p>Is ‘123456’ a good password? What makes a password strong?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>password</strong></td><td>secret string for access</td><td>Don’t reuse passwords.</td></tr>
<tr><td><strong>passphrase</strong></td><td>longer memorable secret phrase</td><td>A passphrase can be stronger.</td></tr>
<tr><td><strong>password manager</strong></td><td>tool that stores secrets safely</td><td>Use a password manager.</td></tr>
<tr><td><strong>MFA / 2FA</strong></td><td>extra verification factor(s)</td><td>Enable MFA on email and VPN.</td></tr>
<tr><td><strong>OTP</strong></td><td>one-time password/code</td><td>Never share OTP codes on calls.</td></tr>
<tr><td><strong>credentials</strong></td><td>username + secret used to log in</td><td>Stolen credentials are dangerous.</td></tr>
<tr><td><strong>lockout</strong></td><td>temporary block after failed tries</td><td>Too many attempts cause lockout.</td></tr>
<tr><td><strong>reset</strong></td><td>set a new password</td><td>I’ll send a reset link.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Please enable MFA today.</li>
<li>Never share your OTP.</li>
<li>Reset your password if you suspect a leak.</li>
<li>Use a unique password per site.</li>
<li>I’ll unlock your account after verification.</li>
  </ul>

  <h2>Dialogue — enable MFA</h2>
  <p><strong>IT:</strong> Your account doesn’t have MFA yet.<br><strong>Employee:</strong> Is it difficult?<br><strong>IT:</strong> It takes two minutes. You’ll confirm with an authenticator app.<br><strong>Employee:</strong> OK — let’s do it now.</p>

  <h2>Grammar focus — Imperatives for security instructions</h2>
  <ul><li><strong>Enable</strong> MFA.</li><li><strong>Don’t reuse</strong> passwords.</li><li><strong>Never share</strong> OTP codes.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Share OTP with helpful caller. → ✅ Real IT rarely asks for OTP on a cold call.</li>
<li>❌ Same password everywhere easy. → ✅ Reuse increases risk.</li>
<li>❌ MFA is optional always. → ✅ Many companies require MFA.</li>
  </ul>

  <h2>Reading — One more step</h2>
  <p>Passwords alone are not enough. MFA adds a second factor — something you have or are. Password managers help create unique secrets. Support staff must verify identity before resets. Clear instructions in English reduce lockouts and tickets.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain MFA to a non-technical colleague.</li>
<li>Give password hygiene tips (6 imperatives).</li>
<li>Role-play a password reset with verification.</li>
  </ol>

  <h2>Quick review</h2>
  <p>password · MFA · OTP · credentials · reset · Don’t share…</p>
""",
            ),
            _lec(
                'Phishing and safe browsing',
                'eit-phishing-safe',
                """
<h2>Lesson goal</h2>
  <p>Recognise phishing patterns and respond safely in English.</p>

  <h2>Warm-up</h2>
  <p>Would you click a link that says ‘Urgent: confirm your salary now’ from an unknown sender?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>phishing</strong></td><td>fake messages to steal data</td><td>That email looks like phishing.</td></tr>
<tr><td><strong>smishing / vishing</strong></td><td>SMS / voice phishing</td><td>Vishing uses phone calls.</td></tr>
<tr><td><strong>spoofing</strong></td><td>faking identity/address</td><td>The address was spoofed.</td></tr>
<tr><td><strong>link / attachment</strong></td><td>URL / file in a message</td><td>Don’t open strange attachments.</td></tr>
<tr><td><strong>suspicious</strong></td><td>possibly dangerous</td><td>Mark it as suspicious.</td></tr>
<tr><td><strong>verify</strong></td><td>check if something is real</td><td>Verify via the official website.</td></tr>
<tr><td><strong>report</strong></td><td>tell security/IT about it</td><td>Report phishing to security.</td></tr>
<tr><td><strong>safe browsing</strong></td><td>careful habits online</td><td>Practice safe browsing.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>This looks like a phishing attempt.</li>
<li>Don’t click the link.</li>
<li>Verify through the official app/site.</li>
<li>I’ll report it to security.</li>
<li>The sender address looks spoofed.</li>
  </ul>

  <h2>Dialogue — urgent fake invoice</h2>
  <p><strong>Employee:</strong> I got an email: pay this invoice in one hour or legal action!<br><strong>IT:</strong> That urgency is a classic phishing pattern. Don’t pay or click.<br><strong>Employee:</strong> Should I reply?<br><strong>IT:</strong> No. Forward it to security and delete it from your inbox after reporting.</p>

  <h2>Grammar focus — First conditional for safety outcomes</h2>
  <ul><li>If you click the link, you <strong>might</strong> give away credentials.</li><li>If you report it, the team <strong>can</strong> protect others.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Click first, think later. → ✅ Verify first, click later (or never).</li>
<li>❌ Phishing is only fishing sport. → ✅ In IT, phishing steals data via fake messages.</li>
<li>❌ Official bank always asks password in email. → ✅ Be sceptical of such requests.</li>
  </ul>

  <h2>Reading — Urgency is a weapon</h2>
  <p>Attackers use fear and hurry. Real companies rarely demand secrets by email. Hover carefully, check domains, and report. Safe browsing is not paranoia — it is professional skill. Your calm English sentence “This looks like phishing” can stop an incident.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>List five phishing warning signs.</li>
<li>Role-play advising a colleague not to click.</li>
<li>Explain smishing vs vishing briefly.</li>
  </ol>

  <h2>Quick review</h2>
  <p>phishing · spoofing · suspicious · verify · report · If you click…</p>
""",
            ),
        ],
        "practice": {
            'eit-security-basics': _quiz(
                'eit-q-vuln',
                'So‘z: vulnerability',
                'Security.',
                'A vulnerability is…',
                [
                    'A) a weakness that can be exploited',
                    'B) a strong password',
                    'C) a green dashboard',
                    'D) a type of monitor',
                ],
                'A',
            ),
            'eit-passwords-mfa': _quiz(
                'eit-q-mfa',
                'So‘z: MFA',
                'Auth.',
                'MFA means…',
                [
                    'A) multi-factor authentication',
                    'B) many free accounts',
                    'C) main file archive',
                    'D) monthly fan activity',
                ],
                'A',
            ),
            'eit-phishing-safe': _quiz(
                'eit-q-phish',
                'So‘z: phishing',
                'Safety.',
                'Phishing is…',
                [
                    'A) fake messages used to steal data',
                    'B) a hardware upgrade',
                    'C) a database index',
                    'D) a Scrum event',
                ],
                'A',
            ),
        },
        "exercises": [
            _quiz(
                'eit-m9-otp',
                'So‘z: OTP',
                'Security.',
                'Best OTP advice:',
                [
                    'A) never share OTP codes on unexpected calls',
                    'B) read OTP aloud to strangers',
                    'C) post OTP in Slack publicly',
                    'D) write OTP on your laptop lid',
                ],
                'A',
            ),
            _quiz(
                'eit-m9-patch',
                'So‘z: patch',
                'Security.',
                'A security patch…',
                [
                    'A) fixes a known weakness',
                    'B) prints marketing flyers',
                    'C) deletes backups for fun',
                    'D) turns off all firewalls',
                ],
                'A',
                difficulty='medium',
            ),
        ],
        "homework": _hw(
            "English for IT — Module 9 homework\n"
            "1) Write a phishing warning poster in English (8 bullet points).\n"
            "2) Glossary: threat, vulnerability, MFA, OTP, phishing, spoofing, patch, breach.\n"
            "3) Record a 45-second MFA how-to.\n"
            "4) Rewrite 5 unsafe habits into safe imperatives."
        ),
    },
    {
        "order": 10,
        "title": 'QA va testlash (QA & testing)',
        "slug": 'eit-qa-testing',
        "description": 'QA rollari, bug report va test turlari.',
        "lectures": [
            _lec(
                'QA roles',
                'eit-qa-roles',
                """
<h2>Lesson goal</h2>
  <p>Describe what QA does and how testers work with developers.</p>

  <h2>Warm-up</h2>
  <p>Is QA only “clicking around,” or is it a skilled engineering practice?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>QA (quality assurance)</strong></td><td>work that improves product quality</td><td>QA protects users from defects.</td></tr>
<tr><td><strong>tester / QA engineer</strong></td><td>person who designs and runs tests</td><td>Our QA engineer found a crash.</td></tr>
<tr><td><strong>test case</strong></td><td>documented steps and expected result</td><td>Write a test case for login.</td></tr>
<tr><td><strong>test plan</strong></td><td>strategy for what/how to test</td><td>Share the test plan before release.</td></tr>
<tr><td><strong>regression</strong></td><td>old features breaking after changes</td><td>We found a regression in checkout.</td></tr>
<tr><td><strong>severity</strong></td><td>version for testing</td><td>Install the latest build.</td></tr>
<tr><td><strong>severity</strong></td><td>severity / severity of defects</td><td>Prioritise critical blockers.</td></tr>
<tr><td><strong>sign-off</strong></td><td>approval that quality is acceptable</td><td>QA sign-off is required.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>QA blocked the release.</li>
<li>Please add steps to reproduce.</li>
<li>This looks like a regression.</li>
<li>We need sign-off before prod.</li>
<li>I’ll write more test cases tonight.</li>
  </ul>

  <h2>Dialogue — release gate</h2>
  <p><strong>Dev:</strong> Can we ship today?<br><strong>QA:</strong> Not yet — there’s a critical login bug on mobile.<br><strong>Dev:</strong> I’ll fix it in an hour.<br><strong>QA:</strong> Great. Retest and then we can discuss sign-off.</p>

  <h2>Grammar focus — Need to / have to for release quality</h2>
  <ul><li>We <strong>need to</strong> retest after the fix.</li><li>We <strong>have to</strong> document steps to reproduce.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ QA is enemy of developers. → ✅ QA and developers share quality goals.</li>
<li>❌ Test case is a suitcase. → ✅ A test case documents steps and expected results.</li>
<li>❌ Sign-off means draw a picture. → ✅ Sign-off means formal approval.</li>
  </ul>

  <h2>Reading — Quality is a team sport</h2>
  <p>QA engineers design coverage, not just random clicks. They speak with developers about risk, priority, and regressions. Clear English in bug tickets turns frustration into fixes. When QA blocks a release, they are protecting users — and the company’s reputation.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain QA in 4 sentences.</li>
<li>Role-play a release gate conversation.</li>
<li>Describe what a test case includes.</li>
  </ol>

  <h2>Quick review</h2>
  <p>QA · test case · regression · build · priority · sign-off</p>
""",
            ),
            _lec(
                'Writing a bug report',
                'eit-bug-report',
                """
<h2>Lesson goal</h2>
  <p>Write clear bug reports: title, steps, expected vs actual, environment.</p>

  <h2>Warm-up</h2>
  <p>Which helps more: “It doesn’t work” or “Login fails on iOS 17 with error 500”?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>bug report</strong></td><td>document describing a defect</td><td>File a bug report in Jira.</td></tr>
<tr><td><strong>steps to reproduce</strong></td><td>exact actions to see the bug</td><td>Include steps to reproduce.</td></tr>
<tr><td><strong>expected result</strong></td><td>what should happen</td><td>Expected: user lands on home.</td></tr>
<tr><td><strong>actual result</strong></td><td>what really happens</td><td>Actual: spinner forever.</td></tr>
<tr><td><strong>severity / priority</strong></td><td>impact / urgency to fix</td><td>Severity is high; priority is P1.</td></tr>
<tr><td><strong>environment</strong></td><td>where it happens (OS, browser, build)</td><td>Environment: Chrome 120, staging.</td></tr>
<tr><td><strong>screenshot / logs</strong></td><td>visual / text evidence</td><td>Attach a screenshot and logs.</td></tr>
<tr><td><strong>workaround</strong></td><td>temporary way to avoid the issue</td><td>Is there a workaround?</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Steps to reproduce: 1) … 2) … 3) …</li>
<li>Expected vs actual don’t match.</li>
<li>I attached logs and a screenshot.</li>
<li>Severity: critical — users can’t pay.</li>
<li>Workaround: use the desktop site.</li>
  </ul>

  <h2>Dialogue — clarifying a bug</h2>
  <p><strong>Dev:</strong> I can’t reproduce your bug.<br><strong>QA:</strong> Did you use the staging build from today?<br><strong>Dev:</strong> No — I used yesterday’s.<br><strong>QA:</strong> Please retry with build 1.8.2 and follow the three steps in the ticket.</p>

  <h2>Grammar focus — Past simple for what happened</h2>
  <ul><li>I <strong>clicked</strong> Save and the app <strong>froze</strong>.</li><li>The server <strong>returned</strong> 500.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Bug: bad. → ✅ Give steps, expected, actual, environment.</li>
<li>❌ Expected and actual same always write. → ✅ Contrast them clearly.</li>
<li>❌ No need environment. → ✅ Environment often decides the fix.</li>
  </ul>

  <h2>Reading — Bugs love details</h2>
  <p>A strong bug report is a gift to developers. Titles should be specific. Steps must be ordered. Expected and actual results prevent guessing. Evidence shortens time-to-fix. Learning this English template makes you valuable on any IT team.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Write aloud a bug report for a broken search box.</li>
<li>Ask three clarifying questions about a vague bug.</li>
<li>Explain severity vs priority simply.</li>
  </ol>

  <h2>Quick review</h2>
  <p>bug report · steps · expected · actual · environment · screenshot</p>
""",
            ),
            _lec(
                'Types of testing',
                'eit-test-types',
                """
<h2>Lesson goal</h2>
  <p>Name common test types and say when each is useful.</p>

  <h2>Warm-up</h2>
  <p>Should every test be manual? When do automated tests help?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>unit test</strong></td><td>tests a small piece of code</td><td>Add unit tests for the calculator.</td></tr>
<tr><td><strong>integration test</strong></td><td>tests how parts work together</td><td>Integration tests cover API + DB.</td></tr>
<tr><td><strong>UI / end-to-end (E2E)</strong></td><td>tests full user flows</td><td>E2E tests cover checkout.</td></tr>
<tr><td><strong>manual testing</strong></td><td>human-executed tests</td><td>Exploratory testing is manual.</td></tr>
<tr><td><strong>automated testing</strong></td><td>scripts run tests</td><td>We automated smoke tests.</td></tr>
<tr><td><strong>smoke test</strong></td><td>quick check that build is basically OK</td><td>Run smoke tests after deploy.</td></tr>
<tr><td><strong>load / performance test</strong></td><td>checks behaviour under load</td><td>Load tests start at 6 p.m.</td></tr>
<tr><td><strong>acceptance test</strong></td><td>checks if requirements are met</td><td>Product runs acceptance tests.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Unit tests are green.</li>
<li>We still need manual exploratory testing.</li>
<li>Smoke tests passed on staging.</li>
<li>E2E coverage is still thin.</li>
<li>Performance testing found a bottleneck.</li>
  </ul>

  <h2>Dialogue — choosing coverage</h2>
  <p><strong>Dev:</strong> Do we need E2E for this tiny CSS change?<br><strong>QA:</strong> Probably smoke tests are enough. But if checkout CSS changed, run the E2E path.<br><strong>Dev:</strong> Fair point — I’ll run smoke + one checkout E2E.</p>

  <h2>Grammar focus — Gerunds after verbs: need / suggest / avoid</h2>
  <ul><li>We need <strong>testing</strong> before release.</li><li>I suggest <strong>automating</strong> smoke tests.</li><li>Avoid <strong>skipping</strong> regression checks.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Unit test means test the whole company. → ✅ Unit tests target small code units.</li>
<li>❌ Automation replaces all thinking. → ✅ Humans still explore and judge risk.</li>
<li>❌ Smoke test means test cigarettes. → ✅ Smoke tests are quick health checks.</li>
  </ul>

  <h2>Reading — The right test for the risk</h2>
  <p>Different risks need different tests. Unit tests are fast feedback. Integration tests catch contract issues. E2E tests are slower but closer to user reality. Good teams mix approaches and say why in plain English.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Compare unit vs E2E testing.</li>
<li>Recommend tests for a login change.</li>
<li>Explain smoke tests in 3 sentences.</li>
  </ol>

  <h2>Quick review</h2>
  <p>unit · integration · E2E · smoke · automated · load test</p>
""",
            ),
        ],
        "practice": {
            'eit-qa-roles': _quiz(
                'eit-q-regression',
                'So‘z: regression',
                'QA.',
                'A regression is…',
                [
                    'A) an old feature breaking after changes',
                    'B) a new office plant',
                    'C) a type of router',
                    'D) a salary bonus',
                ],
                'A',
            ),
            'eit-bug-report': _quiz(
                'eit-q-repro',
                'Bug report',
                'QA.',
                'Steps to reproduce are…',
                [
                    'A) exact actions to see the bug again',
                    'B) random emojis',
                    'C) server prices',
                    'D) Wi-Fi passwords',
                ],
                'A',
            ),
            'eit-test-types': _quiz(
                'eit-q-unit',
                'So‘z: unit test',
                'Testing.',
                'A unit test usually…',
                [
                    'A) tests a small piece of code',
                    'B) replaces the CEO',
                    'C) paints the office',
                    'D) buys cloud regions',
                ],
                'A',
            ),
        },
        "exercises": [
            _quiz(
                'eit-m10-expected',
                'Bug fields',
                'QA.',
                'Expected result means…',
                [
                    'A) what should happen',
                    'B) what the printer ate',
                    'C) the developer’s lunch order',
                    'D) a random crash always',
                ],
                'A',
            ),
            _quiz(
                'eit-m10-smoke',
                'So‘z: smoke test',
                'Testing.',
                'Smoke tests are…',
                [
                    'A) quick checks that a build is basically OK',
                    'B) tests of office fire alarms only',
                    'C) phishing emails',
                    'D) hardware warranties',
                ],
                'A',
                difficulty='medium',
            ),
        ],
        "homework": _hw(
            "English for IT — Module 10 homework\n"
            "1) Write two full bug reports in English.\n"
            "2) Glossary: test case, regression, severity, environment, unit test, E2E, smoke, sign-off.\n"
            "3) Record a 60-second QA release gate speech.\n"
            "4) Map test types to one example each."
        ),
    },
    {
        "order": 11,
        "title": 'Agile va Scrum',
        "slug": 'eit-agile',
        "description": 'Agile qiymatlari, Scrum voqealari va user story’lar.',
        "lectures": [
            _lec(
                'Agile values',
                'eit-agile-values',
                """
<h2>Lesson goal</h2>
  <p>Explain Agile ideas: collaboration, working software, responding to change — in simple English.</p>

  <h2>Warm-up</h2>
  <p>Is a huge 12-month plan always better than small frequent deliveries? Why or why not?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>Agile</strong></td><td>flexible, iterative way of working</td><td>Our team works in an Agile way.</td></tr>
<tr><td><strong>iteration / sprint</strong></td><td>short work cycle</td><td>This sprint is two weeks.</td></tr>
<tr><td><strong>backlog</strong></td><td>ordered list of work items</td><td>Groom the product backlog.</td></tr>
<tr><td><strong>increment</strong></td><td>usable piece of product</td><td>We shipped an increment today.</td></tr>
<tr><td><strong>collaboration</strong></td><td>working together closely</td><td>Agile values collaboration.</td></tr>
<tr><td><strong>feedback</strong></td><td>useful responses for improvement</td><td>We need user feedback.</td></tr>
<tr><td><strong>adapt</strong></td><td>change based on learning</td><td>We adapt the plan each sprint.</td></tr>
<tr><td><strong>continuous improvement</strong></td><td>always getting a bit better</td><td>Retros support continuous improvement.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Let’s keep the backlog visible.</li>
<li>We deliver value every sprint.</li>
<li>Customer feedback changed our priority.</li>
<li>Inspect and adapt.</li>
<li>Working software over perfect documents — but docs still matter.</li>
  </ul>

  <h2>Dialogue — changing priority</h2>
  <p><strong>PO:</strong> Users hate the new filter. Can we change priority?<br><strong>Dev:</strong> Yes — that’s Agile. We’ll adapt the sprint backlog.<br><strong>PO:</strong> Thanks. Collaboration beats sticking to a bad plan.</p>

  <h2>Grammar focus — Comparatives for values</h2>
  <ul><li>Frequent delivery is <strong>better than</strong> a big risky release.</li><li>Face-to-face talk can be <strong>clearer than</strong> long email chains.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Agile means no planning. → ✅ Agile plans in shorter cycles.</li>
<li>❌ Backlog is only a broken keyboard. → ✅ Backlog is the work list.</li>
<li>❌ Feedback is only criticism. → ✅ Feedback guides improvement.</li>
  </ul>

  <h2>Reading — Small steps, real learning</h2>
  <p>Agile teams deliver in short iterations, learn from feedback, and adapt. Documents still help, but working software proves value. English phrases like “Let’s inspect and adapt” keep ceremonies purposeful instead of robotic.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Explain Agile in 5 beginner sentences.</li>
<li>Give an example of adapting after feedback.</li>
<li>Compare a big-bang release vs incremental delivery.</li>
  </ol>

  <h2>Quick review</h2>
  <p>Agile · sprint · backlog · feedback · adapt · continuous improvement</p>
""",
            ),
            _lec(
                'Scrum events',
                'eit-scrum-events',
                """
<h2>Lesson goal</h2>
  <p>Name Scrum events and say the purpose of each in meeting English.</p>

  <h2>Warm-up</h2>
  <p>What is the difference between a planning meeting and a retrospective?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>Scrum</strong></td><td>popular Agile framework</td><td>We follow Scrum.</td></tr>
<tr><td><strong>sprint planning</strong></td><td>meeting to choose sprint work</td><td>Planning is Monday 10:00.</td></tr>
<tr><td><strong>daily scrum / standup</strong></td><td>short daily sync</td><td>Keep standup to 15 minutes.</td></tr>
<tr><td><strong>sprint review</strong></td><td>show what was built</td><td>Demo in the sprint review.</td></tr>
<tr><td><strong>retrospective (retro)</strong></td><td>improve how the team works</td><td>Be honest in the retro.</td></tr>
<tr><td><strong>scrum master</strong></td><td>helps Scrum process and blockers</td><td>The scrum master removes blockers.</td></tr>
<tr><td><strong>product owner (PO)</strong></td><td>owns backlog priorities</td><td>Ask the PO about priority.</td></tr>
<tr><td><strong>blocker / impediment</strong></td><td>something stopping progress</td><td>VPN issues are my blocker.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Yesterday I… Today I will… Blockers: …</li>
<li>Any impediments?</li>
<li>Let’s take that offline.</li>
<li>Please update the board before standup.</li>
<li>What went well? What should we improve?</li>
  </ul>

  <h2>Dialogue — standup</h2>
  <p><strong>Dev:</strong> Yesterday I finished the API fix. Today I’ll write tests. Blocker: staging is down.<br><strong>SM:</strong> Thanks. I’ll escalate staging with DevOps after standup.<br><strong>QA:</strong> I’ll retest as soon as staging is back.</p>

  <h2>Grammar focus — Past simple / present continuous / going to in standup</h2>
  <ul><li>Yesterday I <strong>fixed</strong> the bug.</li><li>Now I <strong>am writing</strong> tests.</li><li>I <strong>am going to</strong> demo after lunch.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Standup is a long status novel. → ✅ Keep it short and focused.</li>
<li>❌ Retro is for blaming people. → ✅ Retro improves the system/process.</li>
<li>❌ Blocker hide until Friday. → ✅ Raise blockers early.</li>
  </ul>

  <h2>Reading — Meetings with a purpose</h2>
  <p>Scrum events are not bureaucracy for fun. Planning chooses focus. Standup exposes blockers. Review shares outcomes. Retro improves teamwork. If you can explain each event’s purpose in English, you can participate professionally anywhere.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Deliver a 20-second standup update.</li>
<li>Explain sprint review vs retrospective.</li>
<li>Role-play raising a blocker politely.</li>
  </ol>

  <h2>Quick review</h2>
  <p>standup · planning · review · retro · blocker · Yesterday / Today / Blockers</p>
""",
            ),
            _lec(
                'User stories',
                'eit-user-stories',
                """
<h2>Lesson goal</h2>
  <p>Write and discuss user stories and acceptance criteria in English.</p>

  <h2>Warm-up</h2>
  <p>Why say “As a user, I want…” instead of “Build a button”?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>user story</strong></td><td>short need from a user’s view</td><td>Write a user story for search.</td></tr>
<tr><td><strong>persona / user role</strong></td><td>type of user</td><td>As a support agent, I want…</td></tr>
<tr><td><strong>acceptance criteria</strong></td><td>conditions for ‘done’</td><td>Add acceptance criteria.</td></tr>
<tr><td><strong>story points</strong></td><td>relative effort estimate</td><td>We estimated 5 story points.</td></tr>
<tr><td><strong>definition of done (DoD)</strong></td><td>team quality checklist</td><td>Does it meet the DoD?</td></tr>
<tr><td><strong>epic</strong></td><td>large theme split into stories</td><td>Split the epic into stories.</td></tr>
<tr><td><strong>priority</strong></td><td>order of importance</td><td>This story is high priority.</td></tr>
<tr><td><strong>INVEST (awareness)</strong></td><td>quality guide for stories</td><td>Is the story testable?</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>As a … I want … so that …</li>
<li>Acceptance criteria: Given… When… Then…</li>
<li>Is this story ready for development?</li>
<li>Let’s split this epic.</li>
<li>It doesn’t meet the definition of done.</li>
  </ul>

  <h2>Dialogue — refining a story</h2>
  <p><strong>PO:</strong> As a user, I want faster search so that I find products quickly.<br><strong>Dev:</strong> What are the acceptance criteria?<br><strong>PO:</strong> Results appear in under two seconds for common queries.<br><strong>QA:</strong> Please add mobile and empty-query cases too.</p>

  <h2>Grammar focus — want / so that / can</h2>
  <ul><li>I <strong>want</strong> filters <strong>so that</strong> I <strong>can</strong> narrow results.</li><li>Users <strong>need</strong> clear errors <strong>so that</strong> they <strong>can</strong> fix input.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Story = technical task only. → ✅ Lead with user value; tasks follow.</li>
<li>❌ Acceptance criteria optional fluff. → ✅ Criteria define done.</li>
<li>❌ Epic means movie only. → ✅ In Agile, an epic is a large work theme.</li>
  </ul>

  <h2>Reading — Stories that guide builds</h2>
  <p>Good user stories focus on people and outcomes. Acceptance criteria make quality visible. Teams estimate and split work to reduce risk. When English stories are clear, developers and QA waste less time guessing.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Write three user stories aloud.</li>
<li>Add acceptance criteria to a login story.</li>
<li>Explain definition of done in 4 sentences.</li>
  </ol>

  <h2>Quick review</h2>
  <p>user story · acceptance criteria · epic · DoD · As a… I want… so that…</p>
""",
            ),
        ],
        "practice": {
            'eit-agile-values': _quiz(
                'eit-q-backlog',
                'So‘z: backlog',
                'Agile.',
                'A backlog is…',
                [
                    'A) an ordered list of work items',
                    'B) a broken chair',
                    'C) a type of malware',
                    'D) a cloud invoice only',
                ],
                'A',
            ),
            'eit-scrum-events': _quiz(
                'eit-q-standup',
                'Standup',
                'Scrum.',
                'A daily scrum is mainly for…',
                [
                    'A) a short sync and surfacing blockers',
                    'B) rewriting the whole roadmap secretly',
                    'C) lunch orders only',
                    'D) deleting repositories',
                ],
                'A',
            ),
            'eit-user-stories': _quiz(
                'eit-q-ac',
                'Acceptance criteria',
                'Stories.',
                'Acceptance criteria define…',
                [
                    'A) conditions for considering work done',
                    'B) the office Wi-Fi password',
                    'C) CPU temperature',
                    'D) holiday dates only',
                ],
                'A',
            ),
        },
        "exercises": [
            _quiz(
                'eit-m11-retro',
                'So‘z: retrospective',
                'Scrum.',
                'A retrospective helps teams…',
                [
                    'A) improve how they work together',
                    'B) ignore all feedback',
                    'C) turn off monitoring',
                    'D) invent phishing emails',
                ],
                'A',
            ),
            _quiz(
                'eit-m11-story-form',
                'User story form',
                'Agile.',
                'Best story shape:',
                [
                    'A) As a user, I want… so that…',
                    'B) Button make now!',
                    'C) Code forever without goal.',
                    'D) Server delete please ASAP secretly.',
                ],
                'A',
                difficulty='medium',
            ),
        ],
        "homework": _hw(
            "English for IT — Module 11 homework\n"
            "1) Write 5 user stories with acceptance criteria.\n"
            "2) Record a full standup update (Y/T/B).\n"
            "3) Glossary: sprint, backlog, PO, scrum master, retro, epic, DoD, blocker.\n"
            "4) Explain Agile vs “no planning” myth in 8 sentences."
        ),
    },
    {
        "order": 12,
        "title": 'Texnik yordam (Tech support)',
        "slug": 'eit-tech-support',
        "description": 'Ticket tili, troubleshooting qadamlari va escalate qilish.',
        "lectures": [
            _lec(
                'Ticket language',
                'eit-ticket-intake',
                """
<h2>Lesson goal</h2>
  <p>Use professional helpdesk words: ticket, priority, SLA, resolve, reopen.</p>

  <h2>Warm-up</h2>
  <p>Why do companies track support work in tickets instead of only chat?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>ticket / case</strong></td><td>tracked support request</td><td>I’ll open a ticket for you.</td></tr>
<tr><td><strong>priority</strong></td><td>urgency level</td><td>This is priority high.</td></tr>
<tr><td><strong>SLA</strong></td><td>service level agreement / response targets</td><td>We must meet the SLA.</td></tr>
<tr><td><strong>assign</strong></td><td>give a ticket to someone</td><td>Assign it to network support.</td></tr>
<tr><td><strong>resolve / close</strong></td><td>finish the ticket</td><td>The ticket was resolved.</td></tr>
<tr><td><strong>reopen</strong></td><td>open again after close</td><td>Please reopen if it happens again.</td></tr>
<tr><td><strong>requester / end user</strong></td><td>person who asked for help</td><td>Ask the requester for logs.</td></tr>
<tr><td><strong>knowledge base (KB)</strong></td><td>help articles library</td><td>We updated the KB article.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>I’ve created ticket #1042.</li>
<li>What’s the business impact?</li>
<li>I’ll assign this to L2.</li>
<li>Resolved — please confirm.</li>
<li>Here’s a KB link while we investigate.</li>
  </ul>

  <h2>Dialogue — opening a ticket</h2>
  <p><strong>User:</strong> Email is down for our sales team.<br><strong>Support:</strong> Thanks — I’m opening a high-priority ticket. How many people are affected?<br><strong>User:</strong> About twenty.<br><strong>Support:</strong> Understood. I’ll assign it to messaging support and update you in 15 minutes.</p>

  <h2>Grammar focus — Present perfect for ticket status</h2>
  <ul><li>I <strong>have opened</strong> a ticket.</li><li>We <strong>haven’t resolved</strong> it yet.</li><li><strong>Has</strong> the issue <strong>happened</strong> before?</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Ticket is only train. → ✅ Here, ticket means a tracked request.</li>
<li>❌ SLA is salad. → ✅ SLA relates to service targets.</li>
<li>❌ Close ticket before confirm. → ✅ Confirm with the user when possible.</li>
  </ul>

  <h2>Reading — Tickets create memory</h2>
  <p>Tickets record problems, owners, and outcomes. Priority and SLA language set expectations. Knowledge-base links reduce repeat work. Support English is customer service plus technical clarity.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Open a ticket verbally for a VPN outage.</li>
<li>Explain priority using business impact.</li>
<li>Give a resolve message politely.</li>
  </ol>

  <h2>Quick review</h2>
  <p>ticket · priority · SLA · assign · resolve · reopen · I have opened…</p>
""",
            ),
            _lec(
                'Troubleshooting steps',
                'eit-troubleshoot-steps',
                """
<h2>Lesson goal</h2>
  <p>Guide users through calm, ordered troubleshooting in English.</p>

  <h2>Warm-up</h2>
  <p>What is your personal first step when an app freezes?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>troubleshoot</strong></td><td>find and fix a problem systematically</td><td>Let’s troubleshoot together.</td></tr>
<tr><td><strong>reproduce</strong></td><td>make the issue happen again</td><td>Can you reproduce it?</td></tr>
<tr><td><strong>isolate</strong></td><td>narrow down the cause</td><td>Isolate whether it’s Wi-Fi or the app.</td></tr>
<tr><td><strong>workaround</strong></td><td>temporary solution</td><td>Use this workaround for now.</td></tr>
<tr><td><strong>root cause</strong></td><td>fundamental reason</td><td>We haven’t found the root cause yet.</td></tr>
<tr><td><strong>symptom</strong></td><td>visible sign of a problem</td><td>The symptom is a white screen.</td></tr>
<tr><td><strong>checklist</strong></td><td>ordered list of checks</td><td>Follow the checklist.</td></tr>
<tr><td><strong>verify</strong></td><td>confirm the fix worked</td><td>Please verify after the restart.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>First, let’s reproduce the issue.</li>
<li>Does it happen on another device?</li>
<li>Try this workaround while we dig deeper.</li>
<li>I’ll isolate network vs application.</li>
<li>Please verify and reply to the ticket.</li>
  </ul>

  <h2>Dialogue — app won’t start</h2>
  <p><strong>Support:</strong> When did it start?<br><strong>User:</strong> After today’s update.<br><strong>Support:</strong> OK. First, reboot. Then open the app without other programs running.<br><strong>User:</strong> Still fails.<br><strong>Support:</strong> Thanks — that helps isolate it. I’ll check known issues for this build.</p>

  <h2>Grammar focus — Sequencing adverbs for support scripts</h2>
  <ul><li><strong>First</strong>… <strong>Then</strong>… <strong>After that</strong>… <strong>Finally</strong>…</li><li><strong>If that doesn’t work</strong>, tell me what you see.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Guess randomly forever. → ✅ Use ordered checks and evidence.</li>
<li>❌ Root cause is flower. → ✅ Root cause is the underlying reason.</li>
<li>❌ Workaround means ignore forever. → ✅ Workaround is temporary.</li>
  </ul>

  <h2>Reading — Calm beats chaos</h2>
  <p>Great support sounds calm. Agents reproduce, isolate, and verify. They separate symptoms from root causes. A clear checklist in English helps users who are stressed. Every confirmed step is progress — even when the bug is not fixed yet.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Give a 6-step troubleshooting script for no internet.</li>
<li>Explain symptom vs root cause.</li>
<li>Role-play verifying a fix with a user.</li>
  </ol>

  <h2>Quick review</h2>
  <p>troubleshoot · reproduce · isolate · workaround · root cause · First… Then…</p>
""",
            ),
            _lec(
                'Escalating issues',
                'eit-escalate',
                """
<h2>Lesson goal</h2>
  <p>Escalate politely with context: what you tried, impact, and urgency.</p>

  <h2>Warm-up</h2>
  <p>When should you stop trying alone and ask a higher level for help?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>escalate</strong></td><td>pass to a higher/more specialised level</td><td>I’ll escalate to L3.</td></tr>
<tr><td><strong>L1 / L2 / L3</strong></td><td>support levels</td><td>L1 gathers info; L2 deepens; L3 specialises.</td></tr>
<tr><td><strong>handover</strong></td><td>transfer of ownership with context</td><td>Do a clean handover.</td></tr>
<tr><td><strong>impact</strong></td><td>who/what is affected</td><td>Customer impact is high.</td></tr>
<tr><td><strong>urgency</strong></td><td>how soon action is needed</td><td>Urgency is critical.</td></tr>
<tr><td><strong>ownership</strong></td><td>who is responsible now</td><td>Confirm ownership in the ticket.</td></tr>
<tr><td><strong>update / ETA</strong></td><td>status news / estimated time</td><td>Any ETA for a fix?</td></tr>
<tr><td><strong>follow up</strong></td><td>check again later</td><td>I’ll follow up in 30 minutes.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>I’m escalating this with full notes.</li>
<li>Here’s what we already tried…</li>
<li>Business impact: the whole sales floor is blocked.</li>
<li>Please confirm ownership.</li>
<li>I’ll follow up with the requester.</li>
  </ul>

  <h2>Dialogue — clean escalation</h2>
  <p><strong>L1:</strong> Escalating ticket #2201 to L2. VPN fails for 40 users after the cert update. Reboot and reinstall didn’t help. Logs attached.<br><strong>L2:</strong> Thanks — clear handover. I’ll take ownership and send an ETA in 20 minutes.<br><strong>L1:</strong> I’ll update the requester now.</p>

  <h2>Grammar focus — Reported information: said / reported / according to</h2>
  <ul><li>The user <strong>reported</strong> that VPN fails after login.</li><li><strong>According to</strong> the logs, the certificate expired.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Escalate without notes. → ✅ Include steps tried and evidence.</li>
<li>❌ ETA means eat. → ✅ ETA means estimated time of arrival/fix.</li>
<li>❌ Ownership unclear OK. → ✅ Always confirm who owns the ticket.</li>
  </ul>

  <h2>Reading — Escalation is teamwork</h2>
  <p>Escalation is not failure — it is using the right skills at the right time. Clean handovers save senior engineers hours. Impact and urgency language helps prioritise. Follow-ups keep users informed and calm.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Escalate a payment outage with a 30-second brief.</li>
<li>Practice a polite ETA request.</li>
<li>Explain L1 vs L2 responsibilities.</li>
  </ol>

  <h2>Quick review</h2>
  <p>escalate · L1/L2 · handover · impact · ETA · follow up · according to</p>
""",
            ),
        ],
        "practice": {
            'eit-ticket-intake': _quiz(
                'eit-q-sla',
                'So‘z: SLA',
                'Support.',
                'An SLA relates to…',
                [
                    'A) service targets such as response times',
                    'B) a type of GPU',
                    'C) a Scrum snack',
                    'D) a CSS framework',
                ],
                'A',
            ),
            'eit-troubleshoot-steps': _quiz(
                'eit-q-root',
                'So‘z: root cause',
                'Support.',
                'Root cause means…',
                [
                    'A) the fundamental reason for a problem',
                    'B) a tree in the office garden',
                    'C) a random reboot',
                    'D) a new emoji',
                ],
                'A',
            ),
            'eit-escalate': _quiz(
                'eit-q-escalate',
                'So‘z: escalate',
                'Support.',
                'To escalate means…',
                [
                    'A) pass an issue to a higher/specialised level',
                    'B) delete the ticket forever',
                    'C) ignore the user',
                    'D) turn off monitoring',
                ],
                'A',
            ),
        },
        "exercises": [
            _quiz(
                'eit-m12-workaround',
                'So‘z: workaround',
                'Support.',
                'A workaround is…',
                [
                    'A) a temporary way to reduce impact',
                    'B) the final root-cause deletion of Earth',
                    'C) a type of phishing',
                    'D) a cloud region name',
                ],
                'A',
            ),
            _quiz(
                'eit-m12-handover',
                'Handover',
                'Escalate.',
                'A clean handover should include…',
                [
                    'A) impact, steps tried, and evidence',
                    'B) only the word HELP',
                    'C) lunch menus',
                    'D) unrelated memes',
                ],
                'A',
                difficulty='medium',
            ),
        ],
        "homework": _hw(
            "English for IT — Module 12 homework\n"
            "1) Write two sample tickets (high/low priority).\n"
            "2) Create a troubleshooting checklist for “can’t print”.\n"
            "3) Record a 45-second escalation brief.\n"
            "4) Glossary: SLA, resolve, reproduce, isolate, escalate, ETA, KB, impact."
        ),
    },
    {
        "order": 13,
        "title": 'Hujjatlar (Documentation)',
        "slug": 'eit-documentation',
        "description": 'README/spec, user guide va change log yozish inglizchasi.',
        "lectures": [
            _lec(
                'README and specs',
                'eit-readme-spec',
                """
<h2>Lesson goal</h2>
  <p>Describe what belongs in a README and a simple technical spec.</p>

  <h2>Warm-up</h2>
  <p>If a new developer joins tomorrow, what must your README answer in five minutes?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>documentation</strong></td><td>written information about a system</td><td>Good documentation saves time.</td></tr>
<tr><td><strong>README</strong></td><td>first doc in a repo</td><td>Update the README with setup steps.</td></tr>
<tr><td><strong>specification (spec)</strong></td><td>detailed requirements/design</td><td>Read the API spec.</td></tr>
<tr><td><strong>setup / install</strong></td><td>how to prepare the project</td><td>Setup takes about ten minutes.</td></tr>
<tr><td><strong>prerequisite</strong></td><td>what you need before starting</td><td>Docker is a prerequisite.</td></tr>
<tr><td><strong>configuration</strong></td><td>settings for an environment</td><td>Check configuration in .env.example.</td></tr>
<tr><td><strong>example</strong></td><td>sample usage</td><td>Include a curl example.</td></tr>
<tr><td><strong>contribute</strong></td><td>how others can help</td><td>See CONTRIBUTING.md to contribute.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Clone the repo and follow the README.</li>
<li>Prerequisites: Node 20 and Docker.</li>
<li>See the spec for edge cases.</li>
<li>I’ll add a configuration example.</li>
<li>Documentation is part of done.</li>
  </ul>

  <h2>Dialogue — missing README steps</h2>
  <p><strong>New hire:</strong> The app won’t start.<br><strong>Teammate:</strong> Did you copy .env.example?<br><strong>New hire:</strong> That step isn’t in the README.<br><strong>Teammate:</strong> Good catch — I’ll document it now.</p>

  <h2>Grammar focus — Imperatives in docs</h2>
  <ul><li><strong>Install</strong> dependencies.</li><li><strong>Run</strong> the tests.</li><li><strong>Don’t commit</strong> secrets.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ README is optional poem. → ✅ README should enable setup quickly.</li>
<li>❌ Spec is only glasses. → ✅ Spec means specification.</li>
<li>❌ Docs later forever. → ✅ Update docs with the change.</li>
  </ul>

  <h2>Reading — Docs are user interface for developers</h2>
  <p>A README is onboarding UI. Specs reduce ambiguity before coding. Examples beat abstract paragraphs. Teams that treat documentation as “done” ship with less chaos. Clear imperative English is a kindness to future you.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Outline a README structure aloud.</li>
<li>Explain prerequisites for a sample project.</li>
<li>Role-play improving a weak README.</li>
  </ol>

  <h2>Quick review</h2>
  <p>README · spec · prerequisite · configuration · example · Install… Run…</p>
""",
            ),
            _lec(
                'User guides',
                'eit-user-guide',
                """
<h2>Lesson goal</h2>
  <p>Write user-facing help: goals, steps, screenshots notes, and troubleshooting tips.</p>

  <h2>Warm-up</h2>
  <p>Have you ever read a guide that assumed too much? How did it feel?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>user guide</strong></td><td>help for end users</td><td>The user guide explains exports.</td></tr>
<tr><td><strong>instruction</strong></td><td>step telling what to do</td><td>Follow each instruction carefully.</td></tr>
<tr><td><strong>screenshot</strong></td><td>picture of the screen</td><td>Add a screenshot of the menu.</td></tr>
<tr><td><strong>tip / note</strong></td><td>extra helpful comment</td><td>Tip: save before exporting.</td></tr>
<tr><td><strong>warning</strong></td><td>alert about risk</td><td>Warning: this deletes data.</td></tr>
<tr><td><strong>faq</strong></td><td>frequently asked questions</td><td>Add this to the FAQ.</td></tr>
<tr><td><strong>audience</strong></td><td>who the doc is for</td><td>Know your audience.</td></tr>
<tr><td><strong>plain language</strong></td><td>clear simple wording</td><td>Use plain language for users.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>To export a report, click…</li>
<li>Note: you need manager access.</li>
<li>Warning: this cannot be undone.</li>
<li>If you see an error, try…</li>
<li>For more help, contact support.</li>
  </ul>

  <h2>Dialogue — reviewing a guide</h2>
  <p><strong>Writer:</strong> Is step 3 clear?<br><strong>User:</strong> Not really — where is the Export button?<br><strong>Writer:</strong> I’ll add a screenshot and a tip about permissions.<br><strong>User:</strong> Perfect — that would have saved me ten minutes.</p>

  <h2>Grammar focus — Softening with please / make sure</h2>
  <ul><li><strong>Please</strong> save your work first.</li><li><strong>Make sure</strong> you are online.</li><li><strong>If</strong> the button is grey, check permissions.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Use jargon for everyone. → ✅ Match language to audience.</li>
<li>❌ Warning same as tip. → ✅ Warnings highlight risk.</li>
<li>❌ Screenshot without alt context. → ✅ Say what the image shows.</li>
  </ul>

  <h2>Reading — Help that respects time</h2>
  <p>User guides succeed when busy people can scan them. Short steps, plain language, and visible warnings reduce support tickets. Writers who test instructions on a real user learn faster than writers who guess.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Write 5 steps to reset a password for end users.</li>
<li>Add one tip and one warning to a delete action.</li>
<li>Explain FAQ value in 3 sentences.</li>
  </ol>

  <h2>Quick review</h2>
  <p>user guide · instruction · screenshot · tip · warning · plain language</p>
""",
            ),
            _lec(
                'Changelogs',
                'eit-change-log',
                """
<h2>Lesson goal</h2>
  <p>Summarise releases: added, fixed, changed, breaking — in changelog English.</p>

  <h2>Warm-up</h2>
  <p>Why do users care about what changed in version 2.1.0?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>changelog</strong></td><td>list of changes by version</td><td>Read the changelog before upgrading.</td></tr>
<tr><td><strong>release notes</strong></td><td>human summary of a release</td><td>Publish release notes today.</td></tr>
<tr><td><strong>added / fixed / changed</strong></td><td>common changelog verbs</td><td>Fixed: login timeout bug.</td></tr>
<tr><td><strong>breaking change</strong></td><td>change that can break old usage</td><td>Warning: breaking API change.</td></tr>
<tr><td><strong>version</strong></td><td>release identifier</td><td>Upgrade to version 3.2.</td></tr>
<tr><td><strong>deprecate</strong></td><td>mark as outdated for later removal</td><td>We deprecated the old endpoint.</td></tr>
<tr><td><strong>migrate</strong></td><td>move to a new way/version</td><td>Migrate before next quarter.</td></tr>
<tr><td><strong>highlight</strong></td><td>most important change</td><td>Highlight the new dashboard.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Added dark mode support.</li>
<li>Fixed crash on export.</li>
<li>Changed default timeout to 30s.</li>
<li>Breaking: /v1/login removed.</li>
<li>Please migrate to /v2/login.</li>
  </ul>

  <h2>Dialogue — before upgrading</h2>
  <p><strong>Client:</strong> Can we upgrade today?<br><strong>Engineer:</strong> Check the changelog — there’s a breaking auth change.<br><strong>Client:</strong> Do you have migration steps?<br><strong>Engineer:</strong> Yes, in the release notes. I’ll walk you through them.</p>

  <h2>Grammar focus — Passive for release notes</h2>
  <ul><li>The timeout <strong>was changed</strong> to 30 seconds.</li><li>Two critical bugs <strong>were fixed</strong>.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Changelog = secret diary. → ✅ Make it readable for humans.</li>
<li>❌ Hide breaking changes. → ✅ Highlight breaking changes clearly.</li>
<li>❌ Fixed stuff. → ✅ Be specific about what was fixed.</li>
  </ul>

  <h2>Reading — Trust through transparency</h2>
  <p>Changelogs build trust. Users and other teams plan upgrades when notes are honest. Verbs like Added/Fixed/Changed create a familiar pattern. Calling out breaking changes early prevents angry surprises.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Write a mini changelog for three imaginary fixes.</li>
<li>Explain a breaking change politely.</li>
<li>Summarise release notes in 30 seconds.</li>
  </ol>

  <h2>Quick review</h2>
  <p>changelog · release notes · added/fixed · breaking · deprecate · migrate</p>
""",
            ),
        ],
        "practice": {
            'eit-readme-spec': _quiz(
                'eit-q-readme',
                'So‘z: README',
                'Docs.',
                'A README should mainly help people…',
                [
                    'A) set up and understand a project quickly',
                    'B) cook pasta',
                    'C) design office plants',
                    'D) delete production blindly',
                ],
                'A',
            ),
            'eit-user-guide': _quiz(
                'eit-q-plain',
                'Plain language',
                'Docs.',
                'Plain language means…',
                [
                    'A) clear simple wording for the audience',
                    'B) only using Latin poetry',
                    'C) hiding warnings',
                    'D) removing all screenshots forever',
                ],
                'A',
            ),
            'eit-change-log': _quiz(
                'eit-q-breaking',
                'Breaking change',
                'Docs.',
                'A breaking change…',
                [
                    'A) can break existing integrations/usage',
                    'B) always fixes nothing',
                    'C) is a lunch break',
                    'D) is a type of monitor',
                ],
                'A',
            ),
        },
        "exercises": [
            _quiz(
                'eit-m13-deprecate',
                'So‘z: deprecate',
                'Docs.',
                'To deprecate means…',
                [
                    'A) mark something as outdated for later removal',
                    'B) make it permanent forever secretly',
                    'C) encrypt lunch menus',
                    'D) reboot the building',
                ],
                'A',
            ),
            _quiz(
                'eit-m13-warning',
                'User guide',
                'Docs.',
                'A warning in a guide should…',
                [
                    'A) highlight risk clearly',
                    'B) tell jokes only',
                    'C) hide delete buttons',
                    'D) replace the FAQ with silence',
                ],
                'A',
                difficulty='medium',
            ),
        ],
        "homework": _hw(
            "English for IT — Module 13 homework\n"
            "1) Write a README outline for a sample app.\n"
            "2) Create a one-page user guide (8 steps).\n"
            "3) Write a changelog with Added/Fixed/Breaking.\n"
            "4) Glossary: spec, prerequisite, FAQ, deprecate, migrate, release notes, audience, plain language."
        ),
    },
    {
        "order": 14,
        "title": 'Jamoa aloqasi (Team communication)',
        "slug": 'eit-team-comms',
        "description": 'Standup inglizchasi, Slack/Teams va muloyim feedback.',
        "lectures": [
            _lec(
                'Standup English',
                'eit-standup-english',
                """
<h2>Lesson goal</h2>
  <p>Give crisp standup updates and ask clarifying questions politely.</p>

  <h2>Warm-up</h2>
  <p>How long should one person’s standup update be — 20 seconds or 20 minutes?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>update</strong></td><td>short progress report</td><td>Here’s my update.</td></tr>
<tr><td><strong>progress</strong></td><td>forward movement on work</td><td>Good progress on the API.</td></tr>
<tr><td><strong>blocker</strong></td><td>something stopping you</td><td>My blocker is missing access.</td></tr>
<tr><td><strong>offline / take offline</strong></td><td>discuss later outside the meeting</td><td>Let’s take that offline.</td></tr>
<tr><td><strong>board</strong></td><td>visual task board</td><td>Move the card on the board.</td></tr>
<tr><td><strong>owner</strong></td><td>person responsible</td><td>Who is the owner of this task?</td></tr>
<tr><td><strong>ETA</strong></td><td>estimated completion time</td><td>ETA is end of day.</td></tr>
<tr><td><strong>sync</strong></td><td>short alignment conversation</td><td>Quick sync after standup?</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Yesterday I finished…</li>
<li>Today I’m working on…</li>
<li>Blockers: none / I need…</li>
<li>I’ll post details in the channel.</li>
<li>Can we take the design debate offline?</li>
  </ul>

  <h2>Dialogue — standup</h2>
  <p><strong>A:</strong> Yesterday I fixed the export bug. Today I’ll add tests. No blockers.<br><strong>B:</strong> Yesterday I reviewed PRs. Today I’m starting the dashboard. Blocker: need Figma access.<br><strong>SM:</strong> Thanks — I’ll sort access after standup.</p>

  <h2>Grammar focus — Concise past / present / future in updates</h2>
  <ul><li>I <strong>finished</strong> X. I <strong>am doing</strong> Y. I <strong>will start</strong> Z.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Tell your life story in standup. → ✅ Keep it short and work-focused.</li>
<li>❌ Hide blockers. → ✅ Say blockers early.</li>
<li>❌ Argue design for 15 minutes live. → ✅ Take long topics offline.</li>
  </ul>

  <h2>Reading — Respect the clock</h2>
  <p>Standup English rewards brevity. Teams sync on progress and blockers, then continue deep work. Moving long debates offline is professional, not rude. Clear updates reduce status meetings elsewhere.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Give three different 20-second updates.</li>
<li>Raise a blocker politely.</li>
<li>Practice saying ‘take it offline’ kindly.</li>
  </ol>

  <h2>Quick review</h2>
  <p>update · blocker · offline · ETA · Yesterday / Today / Blockers</p>
""",
            ),
            _lec(
                'Slack and Teams chat',
                'eit-slack-teams',
                """
<h2>Lesson goal</h2>
  <p>Write clear chat messages: channels, threads, mentions, and async updates.</p>

  <h2>Warm-up</h2>
  <p>Is it OK to @channel for a tiny question? When is urgency real?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>channel</strong></td><td>topic space in chat tools</td><td>Post in #engineering.</td></tr>
<tr><td><strong>thread</strong></td><td>replies under one message</td><td>Please reply in the thread.</td></tr>
<tr><td><strong>mention (@)</strong></td><td>notify a person/group</td><td>Don’t @channel unless urgent.</td></tr>
<tr><td><strong>DM (direct message)</strong></td><td>private chat</td><td>I’ll DM you the link.</td></tr>
<tr><td><strong>async</strong></td><td>not real-time</td><td>Prefer async updates when possible.</td></tr>
<tr><td><strong>status / presence</strong></td><td>available/busy indicators</td><td>Set your status to ‘in a meeting’.</td></tr>
<tr><td><strong>pin / bookmark</strong></td><td>keep important info handy</td><td>Pin the runbook link.</td></tr>
<tr><td><strong>noise</strong></td><td>too many low-value messages</td><td>Reduce channel noise.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Quick question in-thread:</li>
<li>FYI — staging will restart at 18:00.</li>
<li>Can someone from QA take a look?</li>
<li>Summarising decisions here: …</li>
<li>Moving this to a ticket for tracking.</li>
  </ul>

  <h2>Dialogue — noisy channel</h2>
  <p><strong>Lead:</strong> Please keep long debugging in a thread.<br><strong>Dev:</strong> Sorry — I’ll move my messages there.<br><strong>Lead:</strong> Thanks. Also use tickets for anything that needs an owner and deadline.</p>

  <h2>Grammar focus — Soft requests in chat</h2>
  <ul><li><strong>Could you</strong> review this PR?</li><li><strong>When you have a moment</strong>, can you check staging?</li><li><strong>No rush</strong> if you’re in deep work.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ @channel for everything. → ✅ Reserve for true urgency.</li>
<li>❌ Hide decisions across 40 messages. → ✅ Summarise decisions.</li>
<li>❌ Paste secrets in public channels. → ✅ Use secure paths.</li>
  </ul>

  <h2>Reading — Chat with purpose</h2>
  <p>Chat tools are powerful and distracting. Threads keep topics readable. Mentions should be intentional. Async updates respect focus time. Professionals write messages that future teammates can search and understand.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Rewrite a rude ping into a polite async ask.</li>
<li>Summarise a decision in 3 chat lines.</li>
<li>Explain when to use channel vs DM vs ticket.</li>
  </ol>

  <h2>Quick review</h2>
  <p>channel · thread · mention · async · FYI · Could you…?</p>
""",
            ),
            _lec(
                'Polite feedback',
                'eit-feedback-polite',
                """
<h2>Lesson goal</h2>
  <p>Give and receive code/work feedback without blame.</p>

  <h2>Warm-up</h2>
  <p>Which lands better: “This is stupid” or “Could we clarify this edge case?”?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>feedback</strong></td><td>comments for improvement</td><td>Thanks for the feedback.</td></tr>
<tr><td><strong>suggestion</strong></td><td>optional improvement idea</td><td>One suggestion: rename this.</td></tr>
<tr><td><strong>nitpick (nit)</strong></td><td>tiny optional comment</td><td>Nit: trailing space.</td></tr>
<tr><td><strong>blocking</strong></td><td>must fix before merge</td><td>This comment is blocking.</td></tr>
<tr><td><strong>appreciate</strong></td><td>show thanks</td><td>I appreciate the review.</td></tr>
<tr><td><strong>clarify</strong></td><td>make clearer</td><td>Could you clarify the expected behaviour?</td></tr>
<tr><td><strong>agree / disagree</strong></td><td>align or not</td><td>I respectfully disagree because…</td></tr>
<tr><td><strong>action item</strong></td><td>task after discussion</td><td>Action item: add a test.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Thanks for reviewing.</li>
<li>Could we consider…?</li>
<li>I’m not sure I follow — could you clarify?</li>
<li>Good point; I’ll change it.</li>
<li>This is a nit, non-blocking.</li>
  </ul>

  <h2>Dialogue — PR feedback</h2>
  <p><strong>Reviewer:</strong> Could we extract this function for readability?<br><strong>Author:</strong> Good suggestion — I’ll do that. Is it blocking?<br><strong>Reviewer:</strong> Non-blocking nit, but I’d appreciate it before merge if you have time.<br><strong>Author:</strong> On it. Thanks for the review.</p>

  <h2>Grammar focus — Softeners: could we / might / a bit</h2>
  <ul><li><strong>Could we</strong> rename this variable?</li><li>This <strong>might</strong> be clearer as…</li><li>This is <strong>a bit</strong> hard to test — can we simplify?</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ You always write garbage. → ✅ Comment on the code, not the person.</li>
<li>❌ Ignore all feedback. → ✅ Respond and decide transparently.</li>
<li>❌ Everything is blocking forever. → ✅ Label severity of comments.</li>
  </ul>

  <h2>Reading — Feedback builds trust</h2>
  <p>Polite feedback is a career skill. Softeners keep discussions technical. Saying thanks closes the loop. Teams that separate nits from blockers move faster with less drama.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Turn three harsh comments into polite ones.</li>
<li>Role-play receiving critical feedback calmly.</li>
<li>Label comments as blocking vs nit.</li>
  </ol>

  <h2>Quick review</h2>
  <p>feedback · suggestion · nit · blocking · could we… · I appreciate…</p>
""",
            ),
        ],
        "practice": {
            'eit-standup-english': _quiz(
                'eit-q-blocker-chat',
                'So‘z: blocker',
                'Comms.',
                'In standup, a blocker is…',
                [
                    'A) something stopping your progress',
                    'B) a type of headphone',
                    'C) a cloud discount',
                    'D) a changelog verb',
                ],
                'A',
            ),
            'eit-slack-teams': _quiz(
                'eit-q-thread',
                'So‘z: thread',
                'Chat.',
                'Using a thread helps…',
                [
                    'A) keep replies organised under one topic',
                    'B) delete the channel',
                    'C) hide all decisions forever',
                    'D) bypass security',
                ],
                'A',
            ),
            'eit-feedback-polite': _quiz(
                'eit-q-nit',
                'So‘z: nit',
                'Feedback.',
                'A nit usually means…',
                [
                    'A) a small optional comment',
                    'B) a critical outage',
                    'C) a firewall rule',
                    'D) a sprint cancelled',
                ],
                'A',
            ),
        },
        "exercises": [
            _quiz(
                'eit-m14-offline',
                'Phrase',
                'Comms.',
                '“Let’s take it offline” means…',
                [
                    'A) discuss later outside the current meeting',
                    'B) turn off the internet forever',
                    'C) delete Slack',
                    'D) ignore the problem',
                ],
                'A',
            ),
            _quiz(
                'eit-m14-softener',
                'Polite English',
                'Feedback.',
                'Most polite request:',
                [
                    'A) Could we rename this function?',
                    'B) Rename now idiot.',
                    'C) Your code trash.',
                    'D) Fix or leave.',
                ],
                'A',
                difficulty='medium',
            ),
        ],
        "homework": _hw(
            "English for IT — Module 14 homework\n"
            "1) Write 5 standup updates for different days.\n"
            "2) Rewrite 8 chat messages to be clearer/politer.\n"
            "3) Practice 6 feedback softeners.\n"
            "4) Glossary: blocker, thread, mention, async, nit, blocking, ETA, action item."
        ),
    },
    {
        "order": 15,
        "title": 'Email va karyera (Emails & career)',
        "slug": 'eit-career-email',
        "description": 'Email shablonlari, IT intervyu va LinkedIn/CV inglizchasi.',
        "lectures": [
            _lec(
                'Email templates',
                'eit-email-templates',
                """
<h2>Lesson goal</h2>
  <p>Write professional IT emails: request, follow-up, and incident updates.</p>

  <h2>Warm-up</h2>
  <p>What makes an email subject line useful for busy people?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>subject line</strong></td><td>email title</td><td>Use a clear subject line.</td></tr>
<tr><td><strong>greeting / closing</strong></td><td>hello / goodbye phrases</td><td>Best regards is a common closing.</td></tr>
<tr><td><strong>request</strong></td><td>polite ask</td><td>I’m writing to request access.</td></tr>
<tr><td><strong>follow-up</strong></td><td>second message about earlier topic</td><td>Just following up on my request.</td></tr>
<tr><td><strong>cc / bcc</strong></td><td>copy / blind copy</td><td>I’ll cc your manager.</td></tr>
<tr><td><strong>attachment</strong></td><td>file added to email</td><td>Please see the attachment.</td></tr>
<tr><td><strong>summary</strong></td><td>short overview</td><td>Summary: staging is restored.</td></tr>
<tr><td><strong>action required</strong></td><td>reader must do something</td><td>Action required: approve access.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>I’m writing to request…</li>
<li>Could you please… by Friday?</li>
<li>Just following up on…</li>
<li>Please find attached…</li>
<li>Let me know if you have questions.</li>
  </ul>

  <h2>Dialogue — clarifying an email</h2>
  <p><strong>Junior:</strong> Should I write a long story in the email?<br><strong>Mentor:</strong> No — start with the ask, then give short context, then action required.<br><strong>Junior:</strong> And the subject?<br><strong>Mentor:</strong> “Request: VPN access for new hire Dilshod — needed by Friday.”</p>

  <h2>Grammar focus — Formal requests: Could you / Would you mind</h2>
  <ul><li><strong>Could you</strong> approve this request?</li><li><strong>Would you mind</strong> reviewing the attached logs?</li><li>I <strong>would appreciate</strong> a response by Thursday.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Subject: Hi. → ✅ Subject states topic and urgency.</li>
<li>❌ ALL CAPS NOW!!! → ✅ Stay calm and specific.</li>
<li>❌ Hide the ask at the end. → ✅ Put the request near the top.</li>
  </ul>

  <h2>Reading — Busy inbox skills</h2>
  <p>IT email is practical writing. Clear subjects get opened. Short paragraphs get answered. Polite urgency beats panic. Templates help, but customise details so the reader can act without a meeting.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Dictate a request-for-access email.</li>
<li>Give a 4-line incident update email.</li>
<li>Practice a polite follow-up.</li>
  </ol>

  <h2>Quick review</h2>
  <p>subject · request · follow-up · attachment · Could you… · Action required</p>
""",
            ),
            _lec(
                'IT interview English',
                'eit-interview-it',
                """
<h2>Lesson goal</h2>
  <p>Answer common IT interview questions with structure and examples.</p>

  <h2>Warm-up</h2>
  <p>How would you introduce yourself in 45 seconds for a junior developer role?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>interview</strong></td><td>formal job conversation</td><td>I have an interview tomorrow.</td></tr>
<tr><td><strong>strength / weakness</strong></td><td>strong point / area to improve</td><td>One strength is debugging.</td></tr>
<tr><td><strong>experience</strong></td><td>what you have done</td><td>I have internship experience.</td></tr>
<tr><td><strong>project</strong></td><td>piece of work you can discuss</td><td>Tell me about a project.</td></tr>
<tr><td><strong>challenge</strong></td><td>difficult situation</td><td>Describe a technical challenge.</td></tr>
<tr><td><strong>teamwork</strong></td><td>working with others</td><td>Teamwork mattered on that release.</td></tr>
<tr><td><strong>STAR method</strong></td><td>Situation Task Action Result</td><td>Answer with STAR.</td></tr>
<tr><td><strong>follow-up question</strong></td><td>extra question after an answer</td><td>Any follow-up questions?</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>I’m a junior developer with experience in…</li>
<li>In that situation, I…</li>
<li>The result was…</li>
<li>I improved by…</li>
<li>I’d love to learn more about your stack.</li>
  </ul>

  <h2>Dialogue — interview excerpt</h2>
  <p><strong>Interviewer:</strong> Tell me about a bug you fixed.<br><strong>Candidate:</strong> Situation: checkout failed for some users. I reproduced it on staging, found a null value, wrote a test, and patched it. Result: error rate dropped and we released the same day.<br><strong>Interviewer:</strong> Nice — clear STAR structure.</p>

  <h2>Grammar focus — Present perfect vs past simple for experience</h2>
  <ul><li>I <strong>have worked</strong> with Git for two years. (experience up to now)</li><li>I <strong>fixed</strong> a login bug last month. (finished time)</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ I am knowing Java. → ✅ I know Java. / I have used Java.</li>
<li>❌ Weakness: I am perfect. → ✅ Share a real improvement area + actions.</li>
<li>❌ Answer for 10 minutes without structure. → ✅ Use STAR and check time.</li>
  </ul>

  <h2>Reading — Stories beat buzzwords</h2>
  <p>Interviewers remember concrete stories. STAR keeps answers organised. Honest learning edges beat fake perfection. Asking thoughtful questions about the team shows interest and communication skill — both critical in IT.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Deliver a 45-second self-intro.</li>
<li>Answer a bug-fix question with STAR.</li>
<li>Ask two smart questions about the team.</li>
  </ol>

  <h2>Quick review</h2>
  <p>interview · STAR · strength · project · I have worked… · I fixed…</p>
""",
            ),
            _lec(
                'LinkedIn and CV English',
                'eit-linkedin-cv',
                """
<h2>Lesson goal</h2>
  <p>Write CV bullets and LinkedIn summaries with strong action verbs.</p>

  <h2>Warm-up</h2>
  <p>Which is stronger: “Responsible for stuff” or “Reduced API errors by 30%”?</p>

  <h2>Key vocabulary</h2>
  <table>
    <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><strong>CV / resume</strong></td><td>document of experience</td><td>Update your CV before applying.</td></tr>
<tr><td><strong>LinkedIn profile</strong></td><td>professional online presence</td><td>Keep your LinkedIn profile current.</td></tr>
<tr><td><strong>headline</strong></td><td>short role line under your name</td><td>Write a clear headline.</td></tr>
<tr><td><strong>summary</strong></td><td>short profile text</td><td>Your summary should show value.</td></tr>
<tr><td><strong>bullet point</strong></td><td>short achievement line</td><td>Use strong bullet points.</td></tr>
<tr><td><strong>action verb</strong></td><td>built, improved, fixed, led…</td><td>Start bullets with action verbs.</td></tr>
<tr><td><strong>achievement</strong></td><td>measurable result</td><td>Quantify achievements when possible.</td></tr>
<tr><td><strong>skills section</strong></td><td>list of abilities</td><td>Keep the skills section honest.</td></tr>
  </table>

  <h2>Useful phrases (memorise)</h2>
  <ul>
    <li>Built a REST API for…</li>
<li>Improved page load time by…</li>
<li>Collaborated with QA to…</li>
<li>Open to junior developer roles.</li>
<li>Passionate about clean code and learning.</li>
  </ul>

  <h2>Dialogue — CV review</h2>
  <p><strong>Mentor:</strong> This bullet is weak: “Worked on website.”<br><strong>Student:</strong> How can I improve it?<br><strong>Mentor:</strong> Try: “Built responsive product pages used by 5,000 monthly users.”<br><strong>Student:</strong> Much clearer — thanks!</p>

  <h2>Grammar focus — Past simple action verbs for bullets</h2>
  <ul><li><strong>Built</strong>… <strong>Fixed</strong>… <strong>Automated</strong>… <strong>Documented</strong>…</li><li>Prefer past simple for completed roles; present simple for current role.</li></ul>

  <h2>Common mistakes</h2>
  <ul>
    <li>❌ Responsible for many things. → ✅ Name tools + outcomes.</li>
<li>❌ Lie about skills. → ✅ Be honest; show learning speed.</li>
<li>❌ One-page wall of text. → ✅ Scan-friendly bullets.</li>
  </ul>

  <h2>Reading — Make value visible</h2>
  <p>Recruiters scan fast. Action verbs and numbers help. LinkedIn headlines should match the roles you want. A clean CV in English opens doors even when you are still junior — clarity beats buzzword fog.</p>

  <h2>Speaking practice</h2>
  <ol>
    <li>Rewrite three weak CV bullets.</li>
<li>Say your LinkedIn headline and summary aloud.</li>
<li>List eight strong IT action verbs.</li>
  </ol>

  <h2>Quick review</h2>
  <p>CV · headline · bullet · action verb · achievement · Built / Improved / Fixed</p>
""",
            ),
        ],
        "practice": {
            'eit-email-templates': _quiz(
                'eit-q-subject',
                'Email subject',
                'Career.',
                'A good subject line should…',
                [
                    'A) state the topic clearly (and urgency if needed)',
                    'B) say only Hi',
                    'C) be empty',
                    'D) use only emojis',
                ],
                'A',
            ),
            'eit-interview-it': _quiz(
                'eit-q-star',
                'STAR',
                'Interview.',
                'STAR stands for…',
                [
                    'A) Situation, Task, Action, Result',
                    'B) Server, Token, API, Router',
                    'C) Scrum, Test, Alert, Rollback',
                    'D) Soft, Tall, Angry, Random',
                ],
                'A',
            ),
            'eit-linkedin-cv': _quiz(
                'eit-q-verb',
                'CV verbs',
                'Career.',
                'Best CV bullet start:',
                [
                    'A) Built a REST API for order tracking',
                    'B) Responsible for things',
                    'C) Stuff happened',
                    'D) I am very very good forever',
                ],
                'A',
            ),
        },
        "exercises": [
            _quiz(
                'eit-m15-followup',
                'Email',
                'Career.',
                'A follow-up email is…',
                [
                    'A) a polite second message about an earlier request',
                    'B) a type of malware',
                    'C) a hardware fan',
                    'D) a sprint cancelled',
                ],
                'A',
            ),
            _quiz(
                'eit-m15-present-perfect',
                'Grammar',
                'Interview.',
                'Correct experience sentence:',
                [
                    'A) I have worked with Git for two years.',
                    'B) I am work with Git for two years.',
                    'C) I working Git since two years yesterday.',
                    'D) Work I Git have.',
                ],
                'A',
                difficulty='medium',
            ),
        ],
        "homework": _hw(
            "English for IT — Module 15 homework\n"
            "1) Write 3 professional emails (request, incident update, follow-up).\n"
            "2) Prepare STAR answers for bug, teamwork, and learning.\n"
            "3) Rewrite your CV summary + 6 bullets in English.\n"
            "4) Glossary: subject line, follow-up, STAR, headline, achievement, action verb, cc, attachment."
        ),
    },
]
