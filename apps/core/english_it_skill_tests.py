"""
English for IT — skill tests per module (quiz, 4 options).
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
            "Darsdagi IT so‘zlarini eslang.",
            "Noto‘g‘ri variantlarni chiqarib tashlang.",
        ],
        "editorial": editorial,
        "columns": ["javob"],
        "rows": [[answer]],
    }


MODULE_SKILL_TESTS: dict[str, list[dict]] = {
    "eit-it-basics": [
        _q(1, 'Ticket', 'In IT support, a ticket is…', ['A) a recorded work request or issue', 'B) a train pass only', 'C) a type of virus', 'D) a hardware fan'], 'A', 'Ticket = tracked request.'),
        _q(2, 'Colleague', 'A colleague is…', ['A) a person you work with', 'B) only the company CEO', 'C) a broken cable', 'D) a database password'], 'A', 'Colleague = teammate.'),
        _q(3, 'QA role', 'A QA specialist mainly…', ['A) checks quality and finds defects', 'B) designs office furniture', 'C) prints salary slips', 'D) sells laptops'], 'A', 'QA = quality testing.'),
        _q(4, 'VPN', 'A VPN helps you…', ['A) connect securely to the company network', 'B) cook lunch faster', 'C) delete emails forever', 'D) change job titles automatically'], 'A', 'VPN = secure remote access.'),
        _q(5, 'Deadline', 'A deadline is…', ['A) the time when work must be finished', 'B) a type of monitor', 'C) a Wi-Fi password', 'D) a Scrum snack'], 'A', 'Deadline = due time.'),
        _q(6, 'Greeting', 'Best first line in a team chat:', ['A) How can I help you?', 'B) What do you want?', 'C) Password now!', 'D) You again?'], 'A', 'Offer help politely.'),
        _q(7, 'Present simple', 'Correct routine sentence:', ['A) We start standup at 9:30.', 'B) We starting standup at 9:30.', 'C) Start we standup always clock.', 'D) Standup starting we yesterday always.'], 'A', 'Present simple for routines.'),
        _q(8, 'Hybrid', 'Hybrid work means…', ['A) a mix of office and remote days', 'B) only working underwater', 'C) never using a laptop', 'D) deleting the backlog'], 'A', 'Hybrid = office + remote.', 'medium'),
    ],
    "eit-hardware": [
        _q(1, 'RAM', 'RAM is mainly…', ['A) short-term memory for running programs', 'B) a printer type', 'C) an email folder', 'D) a Wi-Fi password'], 'A', 'RAM = working memory.'),
        _q(2, 'SSD', 'An SSD usually…', ['A) stores files and is often faster than an HDD', 'B) prints documents', 'C) replaces the keyboard', 'D) is phishing'], 'A', 'SSD = fast storage.'),
        _q(3, 'Peripheral', 'A peripheral is…', ['A) an external device connected to a computer', 'B) the CPU only', 'C) a cloud region', 'D) a programming language'], 'A', 'Peripheral = external device.'),
        _q(4, 'CPU', 'The CPU is often called…', ['A) the ‘brain’ that runs instructions', 'B) a mouse cable', 'C) a meeting room', 'D) a changelog'], 'A', 'CPU = processor.'),
        _q(5, 'Comparative', 'Correct sentence:', ['A) This SSD is faster than that HDD.', 'B) This SSD more faster that HDD.', 'C) This SSD fastest as HDD.', 'D) SSD is more better.'], 'A', 'Comparative: faster than.'),
        _q(6, 'Upgrade', 'To upgrade RAM means…', ['A) add or install more memory', 'B) delete the OS', 'C) throw away the monitor', 'D) change the company name'], 'A', 'Upgrade = improve parts.'),
        _q(7, 'Compatible', 'Compatible means…', ['A) able to work together', 'B) broken forever', 'C) illegal software', 'D) a type of phishing'], 'A', 'Compatible = works together.'),
        _q(8, 'Port', 'A port on a laptop is…', ['A) a socket for cables and devices', 'B) a Scrum event', 'C) a database table', 'D) an email signature'], 'A', 'Port = connection socket.', 'medium'),
    ],
    "eit-software-os": [
        _q(1, 'OS', 'An operating system is…', ['A) software that manages hardware and apps', 'B) only a mouse cable', 'C) a phishing email', 'D) a meeting room'], 'A', 'OS manages the computer.'),
        _q(2, 'Licence', 'A software licence is…', ['A) legal permission to use software', 'B) a hardware fan', 'C) a Wi-Fi channel', 'D) a bug template'], 'A', 'Licence = legal permission.'),
        _q(3, 'Rollback', 'To roll back means…', ['A) return to a previous version', 'B) buy a new monitor', 'C) delete the company', 'D) invent a password'], 'A', 'Rollback = previous version.'),
        _q(4, 'Admin rights', 'Admin rights allow you to…', ['A) change system settings and install software', 'B) cook lunch', 'C) rename the internet', 'D) skip all passwords forever'], 'A', 'Admin = elevated permission.'),
        _q(5, 'Patch', 'A software patch usually…', ['A) fixes or improves existing software', 'B) prints flyers', 'C) replaces the keyboard', 'D) creates phishing'], 'A', 'Patch = fix/update.'),
        _q(6, 'Mustn’t', 'Correct policy sentence:', ['A) You mustn’t share licence keys in public chat.', 'B) You mustn’t to share keys.', 'C) You no must share.', 'D) Mustn’t you sharing keys always.'], 'A', 'mustn’t + base verb.'),
        _q(7, 'Open source', 'Open source software…', ['A) can be studied/shared under licence rules', 'B) has no rules ever', 'C) is only hardware', 'D) means free malware'], 'A', 'Open source still has licences.'),
        _q(8, 'Driver', 'A driver is…', ['A) software that talks to a device', 'B) a bus ticket', 'C) a sprint backlog', 'D) a cloud invoice'], 'A', 'Driver = device software.', 'medium'),
    ],
    "eit-networking": [
        _q(1, 'Router', 'A router mainly…', ['A) directs traffic between networks', 'B) prints documents', 'C) writes unit tests', 'D) designs logos'], 'A', 'Router routes traffic.'),
        _q(2, 'HTTPS', 'HTTPS is preferred because…', ['A) it encrypts web traffic', 'B) it is slower by law', 'C) it deletes DNS', 'D) it replaces cables'], 'A', 'HTTPS = secure HTTP.'),
        _q(3, 'SSID', 'An SSID is…', ['A) the Wi-Fi network name', 'B) a CPU model', 'C) a database table', 'D) a Scrum ceremony'], 'A', 'SSID = network name.'),
        _q(4, 'Latency', 'Latency means…', ['A) delay in network response', 'B) free lunch', 'C) a type of monitor', 'D) a licence key'], 'A', 'Latency = delay.'),
        _q(5, 'DNS', 'DNS maps…', ['A) domain names to IP addresses', 'B) passwords to printers', 'C) bugs to coffee', 'D) RAM to GPUs'], 'A', 'DNS = name to IP.'),
        _q(6, 'LAN', 'A LAN is typically…', ['A) a local network in one building/area', 'B) a worldwide ocean cable only', 'C) a type of phishing', 'D) a changelog'], 'A', 'LAN = local network.'),
        _q(7, 'Firewall', 'A firewall…', ['A) filters network traffic', 'B) prints invoices', 'C) writes user stories', 'D) charges batteries'], 'A', 'Firewall filters traffic.'),
        _q(8, 'Bandwidth', 'Bandwidth refers to…', ['A) capacity for data transfer', 'B) keyboard width only', 'C) a sprint length', 'D) a CV bullet'], 'A', 'Bandwidth = capacity.', 'medium'),
    ],
    "eit-programming": [
        _q(1, 'Bug', 'A bug is…', ['A) an error in software', 'B) a type of monitor', 'C) a Wi-Fi password', 'D) a meeting room'], 'A', 'Bug = defect.'),
        _q(2, 'Edge case', 'An edge case is…', ['A) unusual input that may break code', 'B) the office edge of a desk', 'C) a GPU brand', 'D) a Scrum snack'], 'A', 'Edge case = unusual input.'),
        _q(3, 'Pull request', 'A pull request is…', ['A) a request to review and merge changes', 'B) a hardware upgrade', 'C) a phishing email', 'D) a DB backup only'], 'A', 'PR = review/merge request.'),
        _q(4, 'Refactor', 'To refactor means…', ['A) improve code without changing behaviour', 'B) delete the repository forever', 'C) buy a new laptop', 'D) turn off the firewall'], 'A', 'Refactor = improve structure.'),
        _q(5, 'Present perfect', 'Correct sentence:', ['A) I have pushed the fix.', 'B) I have push the fix.', 'C) I pushing have fix.', 'D) Push I have yesterdayed.'], 'A', 'have + past participle.'),
        _q(6, 'Branch', 'In Git, a branch is…', ['A) a parallel line of development', 'B) a tree outside only', 'C) a printer queue', 'D) a cloud bill'], 'A', 'Branch = line of work.'),
        _q(7, 'Variable', 'A variable is…', ['A) named storage for a value', 'B) a type of mouse', 'C) a meeting agenda', 'D) a Wi-Fi SSID'], 'A', 'Variable stores values.'),
        _q(8, 'Conflict', 'A merge conflict means…', ['A) competing changes must be resolved', 'B) the office ran out of coffee', 'C) DNS is perfect', 'D) MFA is optional forever'], 'A', 'Conflict = competing edits.', 'medium'),
    ],
    "eit-databases": [
        _q(1, 'Primary key', 'A primary key…', ['A) uniquely identifies a row', 'B) prints invoices', 'C) is a Wi-Fi password', 'D) deletes DNS'], 'A', 'PK uniquely identifies.'),
        _q(2, 'DELETE safety', 'Best advice for DELETE:', ['A) Use a WHERE clause and prefer backups/tests', 'B) Delete everything in production first', 'C) Never use WHERE', 'D) Only delete on Fridays for luck'], 'A', 'Filter deletes safely.'),
        _q(3, 'Encrypt', 'To encrypt data means…', ['A) encode it to protect confidentiality', 'B) print it on posters', 'C) share it on social media', 'D) translate it to Latin'], 'A', 'Encrypt = protect by encoding.'),
        _q(4, 'JOIN', 'A JOIN is used to…', ['A) combine rows from related tables', 'B) restart the router', 'C) design a logo', 'D) create a Slack channel'], 'A', 'JOIN combines related rows.'),
        _q(5, 'Breach', 'A data breach is…', ['A) unauthorised access or a data leak', 'B) a successful backup', 'C) a type of SSD', 'D) a friendly merge'], 'A', 'Breach = leak/intrusion.'),
        _q(6, 'Query', 'A query is…', ['A) a request for data', 'B) a keyboard key only', 'C) a standup snack', 'D) a phishing link'], 'A', 'Query requests data.'),
        _q(7, 'Foreign key', 'A foreign key…', ['A) references another table’s key', 'B) is a passport stamp', 'C) turns off Wi-Fi', 'D) writes CSS'], 'A', 'FK links tables.'),
        _q(8, 'Consent', 'Consent in privacy means…', ['A) permission to use data for a purpose', 'B) free cloud forever', 'C) deleting backups', 'D) sharing OTPs publicly'], 'A', 'Consent = permission.', 'medium'),
    ],
    "eit-web": [
        _q(1, 'Frontend', 'Frontend mainly means…', ['A) the user-facing part of an app', 'B) only the database cables', 'C) a type of phishing', 'D) the office kitchen'], 'A', 'Frontend = UI side.'),
        _q(2, '404', 'A 404 status usually means…', ['A) not found', 'B) success always', 'C) printer offline only', 'D) battery empty'], 'A', '404 = not found.'),
        _q(3, 'Staging', 'Staging is…', ['A) a pre-production testing environment', 'B) a theatre hobby only', 'C) a GPU brand', 'D) a Wi-Fi SSID'], 'A', 'Staging before prod.'),
        _q(4, 'API', 'An API lets software…', ['A) communicate with other software', 'B) cook lunch', 'C) replace the monitor', 'D) invent passwords for fun'], 'A', 'API = software interface.'),
        _q(5, 'Rollback release', 'If production errors spike, teams often…', ['A) roll back to a previous release', 'B) delete the company domain', 'C) ignore dashboards forever', 'D) turn off all backups'], 'A', 'Rollback reduces damage.'),
        _q(6, 'JSON', 'JSON is commonly…', ['A) a data format for APIs', 'B) a type of keyboard', 'C) a Scrum master title', 'D) a phishing kit'], 'A', 'JSON = data format.'),
        _q(7, 'Backend', 'Backend typically handles…', ['A) server-side logic and data', 'B) only CSS colours', 'C) office plants', 'D) lunch menus'], 'A', 'Backend = server side.'),
        _q(8, '401', 'HTTP 401 often means…', ['A) unauthorised', 'B) success', 'C) printer jam', 'D) battery full'], 'A', '401 = unauthorised.', 'medium'),
    ],
    "eit-cloud-devops": [
        _q(1, 'Cloud', 'Cloud computing means…', ['A) using remote servers over the internet', 'B) only weather forecasting', 'C) printing on paper clouds', 'D) deleting all networks'], 'A', 'Cloud = remote computing.'),
        _q(2, 'CI', 'Continuous integration (CI) mainly…', ['A) automatically builds/tests changes', 'B) cooks continuous meals', 'C) replaces keyboards', 'D) turns off monitoring'], 'A', 'CI auto-builds/tests.'),
        _q(3, 'Alert', 'An alert is…', ['A) a notification about a possible problem', 'B) a type of SSD', 'C) a Scrum snack', 'D) a CSS colour'], 'A', 'Alert notifies problems.'),
        _q(4, 'SaaS', 'SaaS examples are usually…', ['A) ready software used over the internet', 'B) raw metal servers you rack yourself always', 'C) HDMI cables', 'D) mechanical keyboards only'], 'A', 'SaaS = software as a service.'),
        _q(5, 'Incident', 'An incident is…', ['A) a serious service disruption', 'B) a successful unit test', 'C) a new emoji', 'D) a holiday calendar'], 'A', 'Incident = serious disruption.'),
        _q(6, 'Container', 'A container packages…', ['A) an app with its dependencies', 'B) office lunches only', 'C) phishing kits', 'D) wooden boxes for plants'], 'A', 'Container packages software.'),
        _q(7, 'On-call', 'On-call means…', ['A) available to respond to incidents', 'B) on vacation forever', 'C) offline without phone', 'D) writing poetry only'], 'A', 'On-call = incident duty.'),
        _q(8, 'Region', 'A cloud region is…', ['A) a geographic location for cloud resources', 'B) a type of mouse', 'C) a CV section', 'D) a password manager'], 'A', 'Region = geo location.', 'medium'),
    ],
    "eit-cybersecurity": [
        _q(1, 'Vulnerability', 'A vulnerability is…', ['A) a weakness that can be exploited', 'B) a strong password', 'C) a green dashboard', 'D) a type of monitor'], 'A', 'Vulnerability = weakness.'),
        _q(2, 'MFA', 'MFA means…', ['A) multi-factor authentication', 'B) many free accounts', 'C) main file archive', 'D) monthly fan activity'], 'A', 'MFA = multi-factor auth.'),
        _q(3, 'Phishing', 'Phishing is…', ['A) fake messages used to steal data', 'B) a hardware upgrade', 'C) a database index', 'D) a Scrum event'], 'A', 'Phishing steals via fake messages.'),
        _q(4, 'OTP', 'Best OTP advice:', ['A) never share OTP codes on unexpected calls', 'B) read OTP aloud to strangers', 'C) post OTP in Slack publicly', 'D) write OTP on your laptop lid'], 'A', 'Keep OTP secret.'),
        _q(5, 'Patch', 'A security patch…', ['A) fixes a known weakness', 'B) prints marketing flyers', 'C) deletes backups for fun', 'D) turns off all firewalls'], 'A', 'Patch fixes weakness.'),
        _q(6, 'Malware', 'Malware is…', ['A) harmful software', 'B) a healthy backup', 'C) a standup update', 'D) a CSS framework'], 'A', 'Malware = harmful software.'),
        _q(7, 'Spoofing', 'Spoofing often means…', ['A) faking identity or address', 'B) cooking lunch', 'C) upgrading RAM', 'D) writing unit tests'], 'A', 'Spoofing fakes identity.'),
        _q(8, 'Credentials', 'Credentials usually include…', ['A) username and secret used to log in', 'B) office plant names', 'C) monitor colours', 'D) lunch menus'], 'A', 'Credentials = login secrets.', 'medium'),
    ],
    "eit-qa-testing": [
        _q(1, 'Regression', 'A regression is…', ['A) an old feature breaking after changes', 'B) a new office plant', 'C) a type of router', 'D) a salary bonus'], 'A', 'Regression = old thing breaks.'),
        _q(2, 'Reproduce', 'Steps to reproduce are…', ['A) exact actions to see the bug again', 'B) random emojis', 'C) server prices', 'D) Wi-Fi passwords'], 'A', 'Repro steps recreate the bug.'),
        _q(3, 'Unit test', 'A unit test usually…', ['A) tests a small piece of code', 'B) replaces the CEO', 'C) paints the office', 'D) buys cloud regions'], 'A', 'Unit = small code test.'),
        _q(4, 'Expected', 'Expected result means…', ['A) what should happen', 'B) what the printer ate', 'C) the developer’s lunch order', 'D) a random crash always'], 'A', 'Expected = should happen.'),
        _q(5, 'Smoke test', 'Smoke tests are…', ['A) quick checks that a build is basically OK', 'B) tests of office fire alarms only', 'C) phishing emails', 'D) hardware warranties'], 'A', 'Smoke = quick health check.'),
        _q(6, 'Severity', 'Severity in a bug report describes…', ['A) how serious the impact is', 'B) the office temperature', 'C) keyboard colour', 'D) lunch time'], 'A', 'Severity = impact seriousness.'),
        _q(7, 'Sign-off', 'QA sign-off means…', ['A) approval that quality is acceptable', 'B) drawing a cartoon', 'C) deleting tests', 'D) turning off CI'], 'A', 'Sign-off = quality approval.'),
        _q(8, 'E2E', 'End-to-end tests mainly…', ['A) check full user flows', 'B) test one variable only always', 'C) replace documentation forever', 'D) reboot routers randomly'], 'A', 'E2E = full flows.', 'medium'),
    ],
    "eit-agile": [
        _q(1, 'Backlog', 'A backlog is…', ['A) an ordered list of work items', 'B) a broken chair', 'C) a type of malware', 'D) a cloud invoice only'], 'A', 'Backlog = work list.'),
        _q(2, 'Standup', 'A daily scrum is mainly for…', ['A) a short sync and surfacing blockers', 'B) rewriting the whole roadmap secretly', 'C) lunch orders only', 'D) deleting repositories'], 'A', 'Standup = short sync.'),
        _q(3, 'Acceptance criteria', 'Acceptance criteria define…', ['A) conditions for considering work done', 'B) the office Wi-Fi password', 'C) CPU temperature', 'D) holiday dates only'], 'A', 'AC = done conditions.'),
        _q(4, 'Retro', 'A retrospective helps teams…', ['A) improve how they work together', 'B) ignore all feedback', 'C) turn off monitoring', 'D) invent phishing emails'], 'A', 'Retro improves process.'),
        _q(5, 'Story form', 'Best story shape:', ['A) As a user, I want… so that…', 'B) Button make now!', 'C) Code forever without goal.', 'D) Server delete please ASAP secretly.'], 'A', 'Classic user-story form.'),
        _q(6, 'Sprint', 'A sprint is…', ['A) a short work cycle', 'B) a type of keyboard', 'C) a phishing kit', 'D) a cloud discount code'], 'A', 'Sprint = short cycle.'),
        _q(7, 'Blocker', 'A blocker is…', ['A) something stopping progress', 'B) a free lunch', 'C) a CSS colour', 'D) a CV template'], 'A', 'Blocker stops progress.'),
        _q(8, 'DoD', 'Definition of done is…', ['A) the team’s quality checklist for finished work', 'B) a password hint', 'C) a monitor brand', 'D) a lunch menu'], 'A', 'DoD = done checklist.', 'medium'),
    ],
    "eit-tech-support": [
        _q(1, 'SLA', 'An SLA relates to…', ['A) service targets such as response times', 'B) a type of GPU', 'C) a Scrum snack', 'D) a CSS framework'], 'A', 'SLA = service targets.'),
        _q(2, 'Root cause', 'Root cause means…', ['A) the fundamental reason for a problem', 'B) a tree in the office garden', 'C) a random reboot', 'D) a new emoji'], 'A', 'Root cause = underlying reason.'),
        _q(3, 'Escalate', 'To escalate means…', ['A) pass an issue to a higher/specialised level', 'B) delete the ticket forever', 'C) ignore the user', 'D) turn off monitoring'], 'A', 'Escalate = higher level.'),
        _q(4, 'Workaround', 'A workaround is…', ['A) a temporary way to reduce impact', 'B) the final root-cause deletion of Earth', 'C) a type of phishing', 'D) a cloud region name'], 'A', 'Workaround = temporary help.'),
        _q(5, 'Handover', 'A clean handover should include…', ['A) impact, steps tried, and evidence', 'B) only the word HELP', 'C) lunch menus', 'D) unrelated memes'], 'A', 'Handover needs context.'),
        _q(6, 'Resolve', 'To resolve a ticket means…', ['A) finish/fix the request', 'B) hide it forever', 'C) print it on paper only', 'D) assign it randomly without notes'], 'A', 'Resolve = finish the case.'),
        _q(7, 'Reproduce', 'To reproduce an issue means…', ['A) make it happen again on purpose', 'B) delete logs', 'C) buy new hardware always', 'D) ignore the user'], 'A', 'Reproduce = make it happen again.'),
        _q(8, 'ETA', 'ETA usually means…', ['A) estimated time of arrival/fix', 'B) eat the apples', 'C) empty the archive', 'D) extra test always'], 'A', 'ETA = estimated time.', 'medium'),
    ],
    "eit-documentation": [
        _q(1, 'README', 'A README should mainly help people…', ['A) set up and understand a project quickly', 'B) cook pasta', 'C) design office plants', 'D) delete production blindly'], 'A', 'README enables setup.'),
        _q(2, 'Plain language', 'Plain language means…', ['A) clear simple wording for the audience', 'B) only using Latin poetry', 'C) hiding warnings', 'D) removing all screenshots forever'], 'A', 'Plain = clear wording.'),
        _q(3, 'Breaking', 'A breaking change…', ['A) can break existing integrations/usage', 'B) always fixes nothing', 'C) is a lunch break', 'D) is a type of monitor'], 'A', 'Breaking can break clients.'),
        _q(4, 'Deprecate', 'To deprecate means…', ['A) mark something as outdated for later removal', 'B) make it permanent forever secretly', 'C) encrypt lunch menus', 'D) reboot the building'], 'A', 'Deprecate = mark outdated.'),
        _q(5, 'Warning', 'A warning in a guide should…', ['A) highlight risk clearly', 'B) tell jokes only', 'C) hide delete buttons', 'D) replace the FAQ with silence'], 'A', 'Warnings highlight risk.'),
        _q(6, 'Changelog', 'A changelog lists…', ['A) changes by version', 'B) lunch orders', 'C) Wi-Fi passwords', 'D) office plants'], 'A', 'Changelog = version changes.'),
        _q(7, 'Spec', 'A specification (spec) is…', ['A) detailed requirements or design', 'B) a pair of glasses only', 'C) a phishing kit', 'D) a standup joke'], 'A', 'Spec = detailed requirements.'),
        _q(8, 'Prerequisite', 'A prerequisite is…', ['A) something required before starting', 'B) a random optional meme', 'C) a broken cable always', 'D) a cloud discount'], 'A', 'Prerequisite = required before.', 'medium'),
    ],
    "eit-team-comms": [
        _q(1, 'Blocker', 'In standup, a blocker is…', ['A) something stopping your progress', 'B) a type of headphone', 'C) a cloud discount', 'D) a changelog verb'], 'A', 'Blocker stops progress.'),
        _q(2, 'Thread', 'Using a thread helps…', ['A) keep replies organised under one topic', 'B) delete the channel', 'C) hide all decisions forever', 'D) bypass security'], 'A', 'Threads organise replies.'),
        _q(3, 'Nit', 'A nit usually means…', ['A) a small optional comment', 'B) a critical outage', 'C) a firewall rule', 'D) a sprint cancelled'], 'A', 'Nit = tiny optional note.'),
        _q(4, 'Offline', '“Let’s take it offline” means…', ['A) discuss later outside the current meeting', 'B) turn off the internet forever', 'C) delete Slack', 'D) ignore the problem'], 'A', 'Offline = discuss later.'),
        _q(5, 'Softener', 'Most polite request:', ['A) Could we rename this function?', 'B) Rename now idiot.', 'C) Your code trash.', 'D) Fix or leave.'], 'A', 'Could we… is polite.'),
        _q(6, 'Async', 'Async communication means…', ['A) not requiring everyone at the same moment', 'B) shouting in the hallway only', 'C) always @channel', 'D) deleting threads'], 'A', 'Async = not real-time.'),
        _q(7, 'Blocking comment', 'A blocking review comment…', ['A) must be fixed before merge', 'B) is always a joke', 'C) deletes the repo', 'D) turns off CI forever'], 'A', 'Blocking = must fix.'),
        _q(8, 'FYI', 'FYI in chat usually means…', ['A) for your information', 'B) fix your internet', 'C) find your intern', 'D) free yellow ink'], 'A', 'FYI = for your information.', 'medium'),
    ],
    "eit-career-email": [
        _q(1, 'Subject', 'A good subject line should…', ['A) state the topic clearly (and urgency if needed)', 'B) say only Hi', 'C) be empty', 'D) use only emojis'], 'A', 'Clear subjects help.'),
        _q(2, 'STAR', 'STAR stands for…', ['A) Situation, Task, Action, Result', 'B) Server, Token, API, Router', 'C) Scrum, Test, Alert, Rollback', 'D) Soft, Tall, Angry, Random'], 'A', 'STAR interview structure.'),
        _q(3, 'CV verb', 'Best CV bullet start:', ['A) Built a REST API for order tracking', 'B) Responsible for things', 'C) Stuff happened', 'D) I am very very good forever'], 'A', 'Action verb + outcome.'),
        _q(4, 'Follow-up', 'A follow-up email is…', ['A) a polite second message about an earlier request', 'B) a type of malware', 'C) a hardware fan', 'D) a sprint cancelled'], 'A', 'Follow-up continues a thread.'),
        _q(5, 'Present perfect', 'Correct experience sentence:', ['A) I have worked with Git for two years.', 'B) I am work with Git for two years.', 'C) I working Git since two years yesterday.', 'D) Work I Git have.'], 'A', 'have + past participle.'),
        _q(6, 'Attachment', 'Please find attached means…', ['A) a file is included with the email', 'B) the server is on fire', 'C) delete the ticket', 'D) ignore the request'], 'A', 'Attachment = included file.'),
        _q(7, 'Headline', 'A LinkedIn headline should…', ['A) clearly show your role/value', 'B) be empty always', 'C) list only emojis', 'D) hide your skills'], 'A', 'Headline shows role/value.'),
        _q(8, 'Could you', 'Most formal request:', ['A) Could you approve this access request by Friday?', 'B) Approve now!!!!', 'C) Give access or else.', 'D) Access me immediately forever.'], 'A', 'Could you… by date.', 'medium'),
    ],

    "eit-interview": [
        _q(1, 'STAR', 'STAR stands for…', ['A) Situation, Task, Action, Result', 'B) Server, Token, API, Router', 'C) Soft, Tall, Angry, Random', 'D) SQL, Test, Alert, Rollback'], 'A', 'STAR = story structure.'),
        _q(2, 'Clarify', 'Best first step in a tech interview problem:', ['A) clarify the requirements / restate the problem', 'B) insult the interviewer', 'C) stay silent for 20 minutes', 'D) guess randomly without thinking'], 'A', 'Clarify before coding.'),
        _q(3, 'Trade-off', 'A trade-off means…', ['A) choosing between options with different pros/cons', 'B) a type of keyboard', 'C) a free lunch', 'D) deleting production for fun'], 'A', 'Trade-off = option choice.'),
        _q(4, 'Ownership', 'Best interview habit:', ['A) describe your actions and measurable results', 'B) only blame others', 'C) refuse all examples', 'D) read the phone the whole time'], 'A', 'Own actions + results.'),
        _q(5, 'Follow-up', 'A thank-you note should usually be sent…', ['A) within about 24 hours', 'B) never', 'C) after one year', 'D) only by fax in 1990'], 'A', 'Follow up the same day if possible.'),
        _q(6, 'Bottleneck', 'A bottleneck is…', ['A) a limiting factor in a system', 'B) a type of headphone', 'C) a Slack emoji', 'D) a lunch menu'], 'A', 'Bottleneck limits throughput.'),
        _q(7, 'Notice period', 'A notice period is…', ['A) time before leaving your current job', 'B) a Wi-Fi password', 'C) a monitor type', 'D) a Scrum snack'], 'A', 'Notice = time before leave.'),
        _q(8, 'Salary range', 'When discussing salary, it is best to…', ['A) share a range and ask about total package', 'B) demand a random number and leave', 'C) refuse to discuss ever', 'D) only talk about lunch'], 'A', 'Range + total package.', 'medium'),
    ],
    "eit-academic": [
        _q(1, "Abstract", "An abstract is…", [
            "A) a short summary of a paper’s aim, method, and results",
            "B) a password list", "C) a hardware fan", "D) a Slack emoji",
        ], "A", "Abstract = paper summary."),
        _q(2, "Cite", "To cite means…", [
            "A) give credit to the original author", "B) delete references", "C) hide datasets", "D) skip peer review",
        ], "A", "Cite = credit the source."),
        _q(3, "Plagiarism", "Plagiarism is…", [
            "A) using someone’s work without proper credit", "B) formatting slides", "C) renaming variables", "D) closing tickets",
        ], "A", "Always paraphrase and cite."),
        _q(4, "Hypothesis", "A hypothesis is…", [
            "A) an idea you test with evidence", "B) a type of monitor", "C) a Wi-Fi cable", "D) a vacation policy",
        ], "A", "Hypothesis = testable idea."),
        _q(5, "Signpost", "Best presentation signpost:", [
            "A) Next, I’ll explain the method.", "B) Stuff now.", "C) Password!", "D) You again?",
        ], "A", "Guide the audience."),
        _q(6, "Passive", "Best methods sentence:", [
            "A) The model was trained on 10,000 samples.", "B) Model we train cool yesterday.", "C) Train is very very.", "D) Password training forever.",
        ], "A", "Passive common in methods."),
        _q(7, "Limitation", "A limitation is…", [
            "A) a weak point of the study or project", "B) always a compliment", "C) a keyboard type", "D) a merge conflict emoji",
        ], "A", "Limitation = weakness/boundary."),
        _q(8, "Reporting verb", "Best academic summary:", [
            "A) The authors conclude that caching reduces latency.", "B) Authors say cool stuff forever.", "C) Paper is about about.", "D) Result good password.",
        ], "A", "Use reporting verbs.", "medium"),
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
