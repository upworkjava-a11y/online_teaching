"""
Русский язык для IT — pre-intermediate–intermediate (A2–B1/B2) ESP track.

Learning Russian stays in Russian (vocabulary, dialogues, reading).
UI instructions use Uzbek so |loc can translate the “second side”.
IT terms follow common international / Russian professional usage.
"""

COURSE_DESCRIPTION = (
    "IT uchun rus tili — workplace, intervyu va akademik darslar (17 modul). "
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
        "hints": hints or ["Darsdagi ruscha so‘zlarni eslang.", "Noto‘g‘ri variantlarni chiqarib tashlang."],
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
    "title": 'IT asoslari (Основы IT)',
    "slug": 'rit-it-basics',
    "description": 'IT workplace, rollar, ofis va remote ish uchun asosiy ruscha so‘zlar.',
    "lectures": [
            _lec(
                'Добро пожаловать в IT-русский',
                'rit-welcome-it',
                """
<h2>Lesson goal</h2>
    <p>К концу урока вы сможете представиться в IT-команде, назвать рабочие инструменты и описать простой рабочий день на русском (A2–B1).</p>

<figure class="lang-fig">
  <img src="/static/course_media/russian-it/welcome-workplace.png" alt="Первый день в IT" loading="lazy">
  <figcaption>Первый день в IT: тикеты, митинги, ноутбук и коллеги.</figcaption>
</figure>


    <h2>Warm-up</h2>
    <p>Где работают разработчики и поддержка — в <strong>офисе</strong>, из <strong>дома</strong> или в <strong>гибридном</strong> режиме?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>IT-отдел</strong></td><td>команда, которая создаёт и поддерживает технологии</td><td>Я работаю в IT-отделе.</td></tr>
<tr><td><strong>рабочее место</strong></td><td>место, где вы выполняете работу</td><td>Наше рабочее место — open space.</td></tr>
<tr><td><strong>коллега</strong></td><td>человек, с которым вы работаете</td><td>Коллега проверяет мой код.</td></tr>
<tr><td><strong>ноутбук</strong></td><td>портативный компьютер</td><td>Возьмите ноутбук на встречу.</td></tr>
<tr><td><strong>митинг / встреча</strong></td><td>запланированное обсуждение</td><td>У нас митинг в 10:00.</td></tr>
<tr><td><strong>тикет</strong></td><td>зарегистрированная заявка или проблема</td><td>Я закрыл три тикета.</td></tr>
<tr><td><strong>дедлайн</strong></td><td>срок сдачи работы</td><td>Дедлайн — в пятницу.</td></tr>
<tr><td><strong>гибридная работа</strong></td><td>офис + удалёнка</td><td>У нас гибридный график.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Доброе утро. Меня зовут Дильшод. Я младший разработчик.</li>
  <li>Приятно познакомиться. В какой вы команде?</li>
  <li>Подскажите, как подключиться к стендапу?</li>
  <li>Я пришлю ссылку в Slack.</li>
  <li>Спасибо за помощь сегодня.</li>
    </ul>

    <h2>Dialogue — первый день</h2>
    <p><strong>HR:</strong> Добро пожаловать в SoftNova. Чем могу помочь?<br><strong>Новичок:</strong> Я выхожу в IT-команду. Куда пройти?<br><strong>HR:</strong> Присаживайтесь. Руководитель встретит вас через пять минут.<br><strong>Новичок:</strong> Нужен ноутбук?<br><strong>HR:</strong> Да. Выдадим доступы и покажем инструменты.</p>

    <h2>Grammar focus — Настоящее время (привычки)</h2>
    <p>Для ежедневной работы:</p><ul><li>Мы <strong>начинаем</strong> стендап в 9:30.</li><li>Она <strong>работает</strong> удалённо по пятницам.</li><li>Офис <strong>не работает</strong> по воскресеньям.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Я есть работаю в IT. → ✅ Я работаю в IT.</li>
  <li>❌ Дай пароль! → ✅ Не могли бы вы помочь сбросить пароль?</li>
  <li>❌ Мой коллега он опаздывает. → ✅ Мой коллега опаздывает.</li>
    </ul>

    <h2>Reading — Утро в IT</h2>
    <p>Малика — специалист поддержки. В девять она проверяет новые тикеты, затем идёт на короткий митинг, отвечает на письма и сбрасывает пароли. Днём обновляет статью в базе знаний. Вечером пишет отчёт о закрытых тикетах.<br><strong>Проверка:</strong> Что она делает сначала?</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Представьтесь и назовите роль (3 предложения).</li>
  <li>Опишите типичное утро (4–5 предложений).</li>
  <li>Разыграйте диалог «первый день».</li>
    </ol>

    <div class="esp-visual">
  <p class="esp-visual-label">Визуальная карта · Утро в IT</p>
  <ol class="esp-timeline">
    <li><span class="esp-time">09:00</span><span class="esp-step"><strong>Тикеты</strong> — новые заявки</span></li>
    <li><span class="esp-time">09:30</span><span class="esp-step"><strong>Митинг</strong> — короткий стендап</span></li>
    <li><span class="esp-time">10:00</span><span class="esp-step"><strong>Работа</strong> — письма, фиксы, пароли</span></li>
    <li><span class="esp-time">17:00</span><span class="esp-step"><strong>Итог</strong> — отчёт руководителю</span></li>
  </ol>
</div>
<div class="esp-try">
  <p class="esp-try-label">Попробуйте сейчас</p>
  <ul class="esp-checklist">
    <li>Назовите имя и роль одним предложением.</li>
    <li>Назовите два рабочих инструмента.</li>
    <li>Скажите вежливую просьбу: <em>Не могли бы вы…?</em></li>
  </ul>
</div>

  <h2>Quick review</h2>
    <p>IT-отдел · коллега · тикет · дедлайн · гибрид · Чем могу помочь?</p>
""",
            ),
            _lec(
                'Роли и команды в IT',
                'rit-it-roles',
                """
<h2>Lesson goal</h2>
    <p>Называть IT-роли и коротко объяснять обязанности каждого специалиста.</p>

<figure class="lang-fig">
  <img src="/static/course_media/russian-it/it-roles-map.png" alt="Карта IT-ролей" loading="lazy">
  <figcaption>Кто за что отвечает? Разработчик, QA, сисадмин, DevOps, PO, техлид.</figcaption>
</figure>


    <h2>Warm-up</h2>
    <p>Кто пишет код? Кто тестирует? Кто помогает пользователям?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>разработчик</strong></td><td>пишет и поддерживает код</td><td>Разработчик исправил баг.</td></tr>
<tr><td><strong>QA / тестировщик</strong></td><td>проверяет качество</td><td>QA нашёл ошибку входа.</td></tr>
<tr><td><strong>сисадмин</strong></td><td>управляет серверами</td><td>Сисадмин перезапустил сервис.</td></tr>
<tr><td><strong>сетевой инженер</strong></td><td>поддерживает сети</td><td>Сетевой инженер проверил Wi‑Fi.</td></tr>
<tr><td><strong>DevOps-инженер</strong></td><td>связывает разработку и эксплуатацию</td><td>DevOps настроил пайплайн.</td></tr>
<tr><td><strong>продакт-оунер</strong></td><td>приоритизирует продуктовую работу</td><td>PO написал историю.</td></tr>
<tr><td><strong>техлид</strong></td><td>ведёт техническую команду</td><td>Спросите техлида.</td></tr>
<tr><td><strong>стажёр</strong></td><td>практикант</td><td>Стажёр работает с поддержкой.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Я работаю младшим разработчиком в команде платежей.</li>
  <li>Я отвечаю за unit-тесты.</li>
  <li>Кому эскалировать этот тикет?</li>
  <li>Познакомьте меня с лидом QA.</li>
  <li>Наша команда отвечает за мобильное приложение.</li>
    </ul>

    <h2>Dialogue — К кому обратиться?</h2>
    <p><strong>Стажёр:</strong> Сайт тормозит. Кому звонить?<br><strong>Ментор:</strong> Сначала поддержка. Если сеть — сетевой инженер.<br><strong>Стажёр:</strong> А если баг в коде?<br><strong>Ментор:</strong> Тикет разработчикам и копия техлиду.</p>

    <h2>Grammar focus — 3-е лицо настоящего времени</h2>
    <ul><li>Она <strong>тестирует</strong> сборки.</li><li>Он <strong>управляет</strong> серверами.</li><li>Он <strong>не деплоит</strong> по пятницам.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Он разрабатывает софтвары. → ✅ Он разрабатывает ПО.</li>
  <li>❌ Я ответственный за баги. → ✅ Я отвечаю за исправление багов.</li>
  <li>❌ Кому я должен спросить? → ✅ У кого спросить?</li>
    </ul>

    <h2>Reading — IT-команды</h2>
    <p>В CloudBridge разработчики работают спринтами, QA проверяет сборки, сисадмины следят за серверами, DevOps автоматизирует деплои. При сбое поддержка открывает тикет, техлид координирует.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Опишите три роли.</li>
  <li>Скажите: «Я работаю как… Я отвечаю за…»</li>
  <li>К кому идти с Wi‑Fi и с багом в коде?</li>
    </ol>

    <div class="esp-visual">
  <p class="esp-visual-label">Карточки ролей · к кому идти</p>
  <div class="esp-cards">
    <div class="esp-card"><strong>Разработчик</strong><span>пишет и чинит код</span></div>
    <div class="esp-card"><strong>QA</strong><span>ищет дефекты до релиза</span></div>
    <div class="esp-card"><strong>Сисадмин</strong><span>следит за серверами</span></div>
    <div class="esp-card"><strong>DevOps</strong><span>автоматизирует деплой</span></div>
    <div class="esp-card"><strong>Продакт-оунер</strong><span>ставит приоритеты</span></div>
    <div class="esp-card"><strong>Техлид</strong><span>ведёт техрешения</span></div>
  </div>
</div>
<div class="esp-scenario">
  <p class="esp-try-label">Лаборатория сценариев</p>
  <p>Упал Wi‑Fi → <strong>сетевой инженер / поддержка</strong>. Баг в коде → <strong>разработчик + техлид</strong>.</p>
</div>

  <h2>Quick review</h2>
    <p>разработчик · QA · сисадмин · DevOps · техлид · отвечать за</p>
""",
            ),
            _lec(
                'Офис и удалённая работа',
                'rit-office-remote',
                """
<h2>Lesson goal</h2>
    <p>Говорить об офисе, удалёнке и гибриде; вежливо просить помощь.</p>

<figure class="lang-fig">
  <img src="/static/course_media/russian-it/office-remote-modes.png" alt="Офис / удалёнка / гибрид" loading="lazy">
  <figcaption>Офис · Удалёнка · Гибрид — выберите слова для своей недели.</figcaption>
</figure>


    <h2>Warm-up</h2>
    <p>Вам комфортнее дома или в офисе? Почему?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>удалённая работа</strong></td><td>работа вне офиса</td><td>По понедельникам я на удалёнке.</td></tr>
<tr><td><strong>в офисе</strong></td><td>на территории компании</td><td>Завтра нужно в офис.</td></tr>
<tr><td><strong>VPN</strong></td><td>защищённое подключение</td><td>Подключите VPN перед БД.</td></tr>
<tr><td><strong>гарнитура</strong></td><td>наушники с микрофоном</td><td>Для звонков нужна гарнитура.</td></tr>
<tr><td><strong>общий календарь</strong></td><td>календарь команды</td><td>Добавьте демо в календарь.</td></tr>
<tr><td><strong>статус-апдейт</strong></td><td>короткий отчёт</td><td>Напишите апдейт до 17:00.</td></tr>
<tr><td><strong>часовой пояс</strong></td><td>временная зона</td><td>Клиент в другом поясе.</td></tr>
<tr><td><strong>асинхронно</strong></td><td>не одновременно</td><td>Мы пишем async-апдейты.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Сегодня подключусь из дома.</li>
  <li>Можете показать экран?</li>
  <li>К сожалению, соединение нестабильное.</li>
  <li>Можем перенести на 15:00 по вашему времени?</li>
  <li>После звонка пришлю follow-up.</li>
    </ul>

    <h2>Dialogue — удалённый стендап</h2>
    <p><strong>Лид:</strong> Камола, вы нас слышите?<br><strong>Камола:</strong> Да, переподключала VPN.<br><strong>Лид:</strong> Какой апдейт?<br><strong>Камола:</strong> Фикс логина готов, сегодня тесты.<br><strong>Лид:</strong> Напишите QA, когда PR готов.</p>

    <h2>Grammar focus — Вежливые просьбы</h2>
    <p><strong>Не могли бы вы…?</strong> / <strong>Можно…?</strong> / <strong>Подскажите, пожалуйста…</strong></p>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Ты экран покажи. → ✅ Можете, пожалуйста, показать экран?</li>
  <li>❌ Интернет плохой всё. → ✅ К сожалению, соединение нестабильное.</li>
  <li>❌ Я опаздываю потому VPN. → ✅ Я опаздываю, потому что VPN не подключался.</li>
    </ul>

    <h2>Reading — Гибридный день</h2>
    <p>Утром — онлайн-стендап, днём — глубокая работа, вечером — короткий статус в чате. Важно договориться о часовых поясах, VPN и правилах async-общения.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Опишите свой режим работы.</li>
  <li>Попросите показать экран.</li>
  <li>Разыграйте удалённый стендап.</li>
    </ol>

    <div class="esp-visual">
  <p class="esp-visual-label">Режимы работы · выберите и скажите</p>
  <div class="esp-cards esp-cards-3">
    <div class="esp-card"><strong>Офис</strong><span>на месте · воркшопы</span></div>
    <div class="esp-card"><strong>Удалёнка</strong><span>VPN · гарнитура</span></div>
    <div class="esp-card"><strong>Гибрид</strong><span>2 дня в офисе · async</span></div>
  </div>
</div>
<div class="esp-try">
  <p class="esp-try-label">Вежливый набор</p>
  <ul class="esp-checklist">
    <li>Можете, пожалуйста, показать экран?</li>
    <li>К сожалению, соединение нестабильное.</li>
    <li>Можем перенести на 15:00 по вашему времени?</li>
  </ul>
</div>

  <h2>Quick review</h2>
    <p>удалёнка · офис · VPN · гарнитура · async · Не могли бы вы…?</p>
""",
            ),
            ],
            "practice": {
            'rit-welcome-it': _quiz(
                    'rit-q-ticket',
                    'Слово: тикет',
                    'IT workplace.',
                    'В IT-поддержке тикет — это…',
                    [
                        'A) зарегистрированная заявка или проблема',
                        'B) только билет на поезд',
                        'C) вид вируса',
                        'D) вентилятор',
                    ],
                    'A',
                ),
            'rit-it-roles': _quiz(
                    'rit-q-qa-role',
                    'Роль: QA',
                    'IT-роли.',
                    'Специалист QA в основном…',
                    [
                        'A) проектирует мебель',
                        'B) проверяет качество и находит дефекты',
                        'C) печатает зарплату',
                        'D) продаёт ноутбуки',
                    ],
                    'B',
                ),
            'rit-office-remote': _quiz(
                    'rit-q-vpn',
                    'Слово: VPN',
                    'Удалёнка.',
                    'VPN помогает…',
                    [
                        'A) безопасно подключиться к сети компании',
                        'B) быстрее готовить обед',
                        'C) удалить все письма',
                        'D) сменить должность',
                    ],
                    'A',
                ),
            },
            "exercises": [
            _quiz(
                'rit-m1-colleague',
                'Слово: коллега',
                'Workplace.',
                'Коллега — это…',
                [
                    'A) человек, с которым вы работаете',
                    'B) только CEO',
                    'C) сломанный кабель',
                    'D) пароль БД',
                ],
                'A',
            ),
            _quiz(
                'rit-m1-help',
                'Речь: помощь',
                'Приветствие.',
                'Лучшая первая фраза в чате:',
                [
                    'A) Чего тебе надо?',
                    'B) Чем могу помочь?',
                    'C) Пароль сейчас!',
                    'D) Опять ты?',
                ],
                'B',
            ),
            ],
            "homework": _hw(
                'Русский язык для IT — Модуль 1\n1) 8 предложений о рабочем дне.\n2) Самопрезентация 45 сек.\n3) Глоссарий: IT-отдел, коллега, тикет, дедлайн, гибрид, VPN.\n4) Диалог «первый день».'
            ),
        },
{
    "order": 2,
    "title": 'Qurilmalar (Оборудование)',
    "slug": 'rit-hardware',
    "description": 'Компьютер қисмлари, периферия ва техник хусусиятлар — русча.',
    "lectures": [
            _lec(
                'Части компьютера',
                'rit-computer-parts',
                """
<h2>Lesson goal</h2>
    <p>Называть компоненты ПК и объяснять их назначение.</p>

    <h2>Warm-up</h2>
    <p>Что важнее: CPU, RAM или SSD?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>процессор / CPU</strong></td><td>выполняет инструкции</td><td>CPU быстрее старого.</td></tr>
<tr><td><strong>RAM</strong></td><td>оперативная память</td><td>Нужно больше RAM.</td></tr>
<tr><td><strong>SSD / HDD</strong></td><td>накопители</td><td>SSD быстрее HDD.</td></tr>
<tr><td><strong>материнская плата</strong></td><td>соединяет компоненты</td><td>Материнка поддерживает CPU.</td></tr>
<tr><td><strong>БП</strong></td><td>блок питания</td><td>Проверьте блок питания.</td></tr>
<tr><td><strong>GPU</strong></td><td>видеокарта</td><td>Для ML нужна GPU.</td></tr>
<tr><td><strong>охлаждение</strong></td><td>снижение температуры</td><td>Кулер шумит.</td></tr>
<tr><td><strong>порт</strong></td><td>разъём</td><td>Мало USB-портов.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>CPU выполняет инструкции.</li>
  <li>RAM хранит данные активных программ.</li>
  <li>SSD обычно быстрее HDD.</li>
  <li>Проверьте совместимость памяти.</li>
  <li>Нужен ли адаптер для порта?</li>
    </ul>

    <h2>Dialogue — диагностика</h2>
    <p><strong>Юзер:</strong> Ноутбук тормозит.<br><strong>Техник:</strong> Сколько RAM?<br><strong>Юзер:</strong> 8 ГБ.<br><strong>Техник:</strong> Лучше 16 ГБ. Проверим и SSD.</p>

    <h2>Grammar focus — Сравнения</h2>
    <ul><li>SSD <strong>быстрее</strong> HDD.</li><li>У модели <strong>больше</strong> памяти.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Более быстрее. → ✅ Быстрее.</li>
  <li>❌ RAM = жёсткий диск. → ✅ RAM — оперативка.</li>
  <li>❌ CPU хранит все файлы. → ✅ Файлы на диске.</li>
    </ul>

    <h2>Reading — Что внутри</h2>
    <p>CPU считает, RAM держит активные данные, диск хранит файлы. Тормоза вкладок — часто мало RAM; долгие открытия файлов — диск.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Разница RAM и SSD.</li>
  <li>Опишите свой ПК.</li>
  <li>Диалог про апгрейд.</li>
    </ol>

    <h2>Quick review</h2>
    <p>CPU · RAM · SSD · GPU · порт</p>
""",
            ),
            _lec(
                'Периферия и устройства',
                'rit-peripherals',
                """
<h2>Lesson goal</h2>
    <p>Называть периферию и решать проблемы подключения.</p>

    <h2>Warm-up</h2>
    <p>Что вы подключаете к ноутбуку каждый день?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>периферия</strong></td><td>внешнее устройство</td><td>Мышь — периферия.</td></tr>
<tr><td><strong>монитор</strong></td><td>экран</td><td>Второй монитор.</td></tr>
<tr><td><strong>клавиатура / мышь</strong></td><td>ввод</td><td>Клавиатура не отвечает.</td></tr>
<tr><td><strong>док-станция</strong></td><td>база портов</td><td>Док удобен в офисе.</td></tr>
<tr><td><strong>кабель / адаптер</strong></td><td>провод / переходник</td><td>Нужен HDMI-адаптер.</td></tr>
<tr><td><strong>драйвер</strong></td><td>ПО устройства</td><td>Обновите драйвер.</td></tr>
<tr><td><strong>беспроводной</strong></td><td>без провода</td><td>Мышь разрядилась.</td></tr>
<tr><td><strong>совместимый</strong></td><td>работает вместе</td><td>Наушники совместимы.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Устройство не определяется.</li>
  <li>Попробуйте другой порт.</li>
  <li>Переустановите драйвер.</li>
  <li>Проверьте заряд.</li>
  <li>Адаптер совместим с USB‑C.</li>
    </ul>

    <h2>Dialogue — принтер</h2>
    <p><strong>Сотрудник:</strong> Принтер не печатает.<br><strong>IT:</strong> Виден в устройствах?<br><strong>Сотрудник:</strong> Нет.<br><strong>IT:</strong> Кабель, драйвер, перезапуск спулера.</p>

    <h2>Grammar focus — Императив</h2>
    <ul><li><strong>Подключите</strong> кабель.</li><li><strong>Перезагрузите</strong> устройство.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Драйвер = водитель. → ✅ Программа для устройства.</li>
  <li>❌ Периферия внутри корпуса. → ✅ Обычно снаружи.</li>
    </ul>

    <h2>Reading — Чек-лист</h2>
    <p>Питание → кабель → порт → драйвер → перезагрузка. Часто «сломан ПК» = плохой кабель.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>6 устройств.</li>
  <li>5 шагов: мышь не работает.</li>
  <li>Зачем драйвер?</li>
    </ol>

    <h2>Quick review</h2>
    <p>периферия · драйвер · док · совместимый</p>
""",
            ),
            _lec(
                'Характеристики и сравнение',
                'rit-specs-compare',
                """
<h2>Lesson goal</h2>
    <p>Сравнивать specs и рекомендовать апгрейд.</p>

    <h2>Warm-up</h2>
    <p>Как выбираете ноутбук: цена, вес, скорость?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>характеристики</strong></td><td>техпараметры</td><td>Пришлите specs.</td></tr>
<tr><td><strong>производительность</strong></td><td>скорость системы</td><td>Производительность упала.</td></tr>
<tr><td><strong>объём</strong></td><td>ёмкость</td><td>Диск 512 ГБ.</td></tr>
<tr><td><strong>апгрейд</strong></td><td>улучшение</td><td>Апгрейд RAM.</td></tr>
<tr><td><strong>узкое место</strong></td><td>ограничивающий фактор</td><td>Узкое место — диск.</td></tr>
<tr><td><strong>гарантия</strong></td><td>срок обслуживания</td><td>Гарантия действует.</td></tr>
<tr><td><strong>бюджет</strong></td><td>деньги</td><td>В бюджете эта модель.</td></tr>
<tr><td><strong>рекомендовать</strong></td><td>советовать</td><td>Рекомендую с SSD.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Модель мощнее, но тяжелее.</li>
  <li>Для разработки — 16 ГБ RAM.</li>
  <li>Узкое место — диск.</li>
  <li>Апгрейд в гарантии.</li>
  <li>По цене/качеству лучше этот.</li>
    </ul>

    <h2>Dialogue — выбор</h2>
    <p><strong>Менеджер:</strong> Какой ноутбук стажёру?<br><strong>IT:</strong> SSD, 16 ГБ, хороший экран.<br><strong>Менеджер:</strong> Бюджет мал?<br><strong>IT:</strong> Средний класс + апгрейд позже.</p>

    <h2>Grammar focus — Сравнение</h2>
    <ul><li>A <strong>лучше</strong> B для кода.</li><li><strong>Чем больше</strong> RAM, <strong>тем стабильнее</strong>.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Самый хороший более. → ✅ Лучше / самый подходящий.</li>
  <li>❌ Апгрейд = удалить Windows. → ✅ Улучшить комплектующие.</li>
    </ul>

    <h2>Reading — Сравнение по задачам</h2>
    <p>Смотрите CPU, RAM, диск, порты, вес, гарантию под ваши задачи.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Сравните 2 ноутбука.</li>
  <li>Рекомендуйте апгрейд.</li>
  <li>Объясните «узкое место».</li>
    </ol>

    <h2>Quick review</h2>
    <p>specs · апгрейд · бюджет · чем… тем…</p>
""",
            ),
            ],
            "practice": {
            'rit-computer-parts': _quiz(
                    'rit-q-ram',
                    'RAM',
                    'Hardware.',
                    'RAM в основном…',
                    [
                        'A) кратковременная память для программ',
                        'B) тип принтера',
                        'C) папка почты',
                        'D) пароль Wi‑Fi',
                    ],
                    'A',
                ),
            'rit-peripherals': _quiz(
                    'rit-q-peripheral',
                    'Периферия',
                    'Devices.',
                    'Периферия — это…',
                    [
                        'A) внешнее устройство ПК',
                        'B) только CPU',
                        'C) облачный регион',
                        'D) язык программирования',
                    ],
                    'A',
                ),
            'rit-specs-compare': _quiz(
                    'rit-q-upgrade',
                    'Апгрейд',
                    'Specs.',
                    'Апгрейд RAM значит…',
                    [
                        'A) добавить больше памяти',
                        'B) удалить ОС',
                        'C) выбросить монитор',
                        'D) сменить название фирмы',
                    ],
                    'A',
                ),
            },
            "exercises": [
            _quiz(
                'rit-m2-ssd',
                'SSD',
                'Storage.',
                'SSD обычно…',
                [
                    'A) хранит файлы и часто быстрее HDD',
                    'B) печатает',
                    'C) заменяет клавиатуру',
                    'D) фишинг',
                ],
                'A',
            ),
            _quiz(
                'rit-m2-compare',
                'Сравнение',
                'Grammar.',
                'Правильно:',
                [
                    'A) Этот SSD быстрее, чем HDD.',
                    'B) Более быстрее HDD.',
                    'C) Самый быстрее как HDD.',
                    'D) Более лучше.',
                ],
                'A',
                difficulty='medium',
            ),
            ],
            "homework": _hw(
                'Русский язык для IT — Модуль 2\n1) Опишите комплектацию ПК.\n2) Рекомендация апгрейда.\n3) Глоссарий: CPU, RAM, SSD, GPU, драйвер, порт.\n4) Сравнение устройств 60 сек.'
            ),
        },
{
    "order": 3,
    "title": 'ПО и ОС (Программное обеспечение и ОС)',
    "slug": 'rit-software-os',
    "description": 'Operatsion tizim, ilovalar, litsenziya, o‘rnatish va yangilash — ruscha.',
    "lectures": [
            _lec(
                'Основы операционной системы',
                'rit-os-basics',
                """
<h2>Lesson goal</h2>
    <p>Объяснять, что делает ОС, и называть базовые действия пользователя.</p>

    <h2>Warm-up</h2>
    <p>Какая ОС у вас на работе: Windows, macOS или Linux?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>операционная система</strong></td><td>управляет железом и программами</td><td>ОС управляет ресурсами.</td></tr>
<tr><td><strong>процесс</strong></td><td>запущенная программа</td><td>Процесс завис.</td></tr>
<tr><td><strong>файл / папка</strong></td><td>данные / каталог</td><td>Сохраните файл в папку.</td></tr>
<tr><td><strong>права доступа</strong></td><td>что разрешено пользователю</td><td>Нет прав администратора.</td></tr>
<tr><td><strong>рабочий стол</strong></td><td>основной экран</td><td>Ярлык на рабочем столе.</td></tr>
<tr><td><strong>панель задач</strong></td><td>панель запущенных приложений</td><td>Откройте панель задач.</td></tr>
<tr><td><strong>перезагрузка</strong></td><td>перезапуск системы</td><td>Перезагрузите ПК.</td></tr>
<tr><td><strong>драйвер</strong></td><td>ПО для устройства</td><td>Нужен драйвер видеокарты.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>ОС управляет памятью и процессами.</li>
  <li>У меня нет прав администратора.</li>
  <li>Перезагрузите систему после установки.</li>
  <li>Файл заблокирован другим процессом.</li>
  <li>Проверьте журнал событий.</li>
    </ul>

    <h2>Dialogue — зависшее приложение</h2>
    <p><strong>Юзер:</strong> Программа не отвечает.<br><strong>IT:</strong> Откройте диспетчер задач и завершите процесс.<br><strong>Юзер:</strong> Готово.<br><strong>IT:</strong> Если повторится — переустановим.</p>

    <h2>Grammar focus — Глаголы инструкций</h2>
    <ul><li><strong>Откройте</strong>…</li><li><strong>Сохраните</strong>…</li><li><strong>Не удаляйте</strong> системные файлы.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ ОС это только антивирус. → ✅ ОС управляет компьютером.</li>
  <li>❌ Права = зарплата. → ✅ Здесь — разрешения.</li>
    </ul>

    <h2>Reading — Зачем ОС</h2>
    <p>ОС — мост между железом и приложениями. Без неё программы не получают память, диск и сеть.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Что делает ОС?</li>
  <li>Инструкция: завершить процесс.</li>
  <li>Сравните Windows и Linux (3 фразы).</li>
    </ol>

    <h2>Quick review</h2>
    <p>ОС · процесс · права · перезагрузка</p>
""",
            ),
            _lec(
                'Приложения и лицензии',
                'rit-apps-licenses',
                """
<h2>Lesson goal</h2>
    <p>Говорить о типах ПО и лицензиях.</p>

    <h2>Warm-up</h2>
    <p>Чем отличаются бесплатное, open source и корпоративное ПО?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>приложение / софт</strong></td><td>программа</td><td>Установите приложение.</td></tr>
<tr><td><strong>лицензия</strong></td><td>право на использование</td><td>Лицензия истекает.</td></tr>
<tr><td><strong>open source</strong></td><td>открытый исходный код</td><td>Мы используем open source.</td></tr>
<tr><td><strong>проприетарный</strong></td><td>закрытый код</td><td>Это проприетарный продукт.</td></tr>
<tr><td><strong>подписка</strong></td><td>оплата по периоду</td><td>Подписка на год.</td></tr>
<tr><td><strong>активация</strong></td><td>включение лицензии</td><td>Нужна активация.</td></tr>
<tr><td><strong>ключ лицензии</strong></td><td>секрет для активации</td><td>Не публикуйте ключ.</td></tr>
<tr><td><strong>соответствие / compliance</strong></td><td>соблюдение правил</td><td>Проверьте compliance.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Не делитесь ключами в чате.</li>
  <li>Нужна корпоративная лицензия.</li>
  <li>ПО open source, но лицензию читайте.</li>
  <li>Подписка заканчивается в марте.</li>
  <li>Мы обязаны соблюдать compliance.</li>
    </ul>

    <h2>Dialogue — ключ в Slack</h2>
    <p><strong>Джун:</strong> Кину ключ в канал?<br><strong>Лид:</strong> Нет. Ключи только в секрет-хранилище.<br><strong>Джун:</strong> Понял.</p>

    <h2>Grammar focus — must / нельзя</h2>
    <ul><li>Вы <strong>должны</strong> активировать легально.</li><li><strong>Нельзя</strong> публиковать ключи.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Open source = можно всё без правил. → ✅ Есть лицензионные условия.</li>
  <li>❌ Лицензия = только бумага. → ✅ Это право использования.</li>
    </ul>

    <h2>Reading — Лицензии на работе</h2>
    <p>IT следит, чтобы софт был легальным: меньше рисков аудита и блокировок.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Объясните лицензию.</li>
  <li>Почему нельзя кидать ключ в чат?</li>
  <li>Разница подписки и вечной лицензии.</li>
    </ol>

    <h2>Quick review</h2>
    <p>лицензия · open source · ключ · compliance</p>
""",
            ),
            _lec(
                'Установка и обновление',
                'rit-install-update',
                """
<h2>Lesson goal</h2>
    <p>Описывать установку, обновление, откат и патчи.</p>

    <h2>Warm-up</h2>
    <p>Вы ставите обновления сразу или ждёте?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>установка</strong></td><td>инсталляция</td><td>Установка займёт 10 минут.</td></tr>
<tr><td><strong>обновление / патч</strong></td><td>исправление/улучшение</td><td>Поставьте патч.</td></tr>
<tr><td><strong>откат / rollback</strong></td><td>возврат к версии</td><td>Сделаем откат.</td></tr>
<tr><td><strong>зависимости</strong></td><td>нужные компоненты</td><td>Не хватает зависимости.</td></tr>
<tr><td><strong>права админа</strong></td><td>расширенные права</td><td>Нужны права админа.</td></tr>
<tr><td><strong>тихая установка</strong></td><td>без диалогов</td><td>Деплоим silently.</td></tr>
<tr><td><strong>релиз-ноты</strong></td><td>описание изменений</td><td>Читайте release notes.</td></tr>
<tr><td><strong>совместимость</strong></td><td>работа с окружением</td><td>Проверьте совместимость.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Сначала сделайте резервную копию.</li>
  <li>Обновление требует прав админа.</li>
  <li>После патча проверьте сервис.</li>
  <li>Если сломалось — откат.</li>
  <li>Читайте release notes.</li>
    </ul>

    <h2>Dialogue — сломанный апдейт</h2>
    <p><strong>Ops:</strong> После обновления сервис падает.<br><strong>Dev:</strong> Давайте rollback на прошлую версию.<br><strong>Ops:</strong> Откат сделан, пишем постмортем.</p>

    <h2>Grammar focus — Последовательность</h2>
    <p>Сначала… Затем… После этого… Наконец…</p>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Rollback = удалить компанию. → ✅ Вернуться к предыдущей версии.</li>
  <li>❌ Патч всегда новый продукт. → ✅ Исправление существующего.</li>
    </ul>

    <h2>Reading — Порядок обновлений</h2>
    <p>Бэкап → тест → обновление → проверка → при проблеме откат.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Опишите установку приложения.</li>
  <li>Когда нужен rollback?</li>
  <li>Что такое release notes?</li>
    </ol>

    <h2>Quick review</h2>
    <p>установка · патч · rollback · админ · зависимости</p>
""",
            ),
            ],
            "practice": {
            'rit-os-basics': _quiz(
                    'rit-q-os',
                    'ОС',
                    'Software.',
                    'Операционная система — это…',
                    [
                        'A) ПО, управляющее железом и приложениями',
                        'B) только кабель мыши',
                        'C) фишинг',
                        'D) переговорка',
                    ],
                    'A',
                ),
            'rit-apps-licenses': _quiz(
                    'rit-q-licence',
                    'Лицензия',
                    'Apps.',
                    'Лицензия на ПО — это…',
                    [
                        'A) законное разрешение использовать софт',
                        'B) вентилятор',
                        'C) канал Wi‑Fi',
                        'D) шаблон бага',
                    ],
                    'A',
                ),
            'rit-install-update': _quiz(
                    'rit-q-rollback',
                    'Откат',
                    'Update.',
                    'Откат (rollback) значит…',
                    [
                        'A) вернуться к предыдущей версии',
                        'B) купить монитор',
                        'C) удалить компанию',
                        'D) придумать пароль',
                    ],
                    'A',
                ),
            },
            "exercises": [
            _quiz(
                'rit-m3-admin',
                'Права админа',
                'OS.',
                'Права администратора позволяют…',
                [
                    'A) менять системные настройки и ставить ПО',
                    'B) готовить обед',
                    'C) переименовать интернет',
                    'D) жить без паролей',
                ],
                'A',
            ),
            _quiz(
                'rit-m3-patch',
                'Патч',
                'Update.',
                'Патч обычно…',
                [
                    'A) исправляет или улучшает ПО',
                    'B) печатает листовки',
                    'C) меняет клавиатуру',
                    'D) создаёт фишинг',
                ],
                'A',
                difficulty='medium',
            ),
            ],
            "homework": _hw(
                'Русский язык для IT — Модуль 3\n1) Объясните, что делает ОС.\n2) Политика лицензий (5 правил).\n3) Глоссарий: ОС, лицензия, патч, rollback, админ.\n4) Чек-лист обновления.'
            ),
        },
{
    "order": 4,
    "title": 'Сети (Networking)',
    "slug": 'rit-networking',
    "description": 'Tarmoq asoslari, protokollar va Wi‑Fi muammolari — ruscha.',
    "lectures": [
            _lec(
                'Основы сетей',
                'rit-network-basics',
                """
<h2>Lesson goal</h2>
    <p>Объяснять LAN/WAN, роутер, IP на простом русском.</p>

    <h2>Warm-up</h2>
    <p>Чем домашняя сеть отличается от офисной?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>сеть</strong></td><td>связанные устройства</td><td>Сеть недоступна.</td></tr>
<tr><td><strong>LAN</strong></td><td>локальная сеть</td><td>LAN в одном здании.</td></tr>
<tr><td><strong>роутер</strong></td><td>маршрутизирует трафик</td><td>Перезагрузите роутер.</td></tr>
<tr><td><strong>коммутатор / switch</strong></td><td>соединяет устройства в LAN</td><td>Кабель в switch.</td></tr>
<tr><td><strong>IP-адрес</strong></td><td>адрес устройства в сети</td><td>Какой у вас IP?</td></tr>
<tr><td><strong>маска подсети</strong></td><td>граница сети</td><td>Проверьте маску.</td></tr>
<tr><td><strong>шлюз</strong></td><td>выход во внешнюю сеть</td><td>Шлюз по умолчанию.</td></tr>
<tr><td><strong>трафик</strong></td><td>поток данных</td><td>Трафик вырос.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Проверьте кабель и индикаторы.</li>
  <li>Роутер раздаёт адреса по DHCP.</li>
  <li>Устройство не получает IP.</li>
  <li>Это проблема локальной сети.</li>
  <li>Перезапустите сетевой адаптер.</li>
    </ul>

    <h2>Dialogue — нет сети</h2>
    <p><strong>Юзер:</strong> Нет интернета.<br><strong>IT:</strong> Есть линк на кабеле?<br><strong>Юзер:</strong> Нет.<br><strong>IT:</strong> Проверьте порт на switch и другой кабель.</p>

    <h2>Grammar focus — Есть / нет</h2>
    <ul><li>Интернета <strong>нет</strong>.</li><li><strong>Есть</strong> линк, но <strong>нет</strong> IP.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Роутер печатает. → ✅ Роутер маршрутизирует.</li>
  <li>❌ LAN = весь интернет. → ✅ LAN — локально.</li>
    </ul>

    <h2>Reading — Слои простыми словами</h2>
    <p>Кабель/Wi‑Fi → адрес (IP) → маршрутизация → сервисы. Начинайте диагностику снизу.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>LAN vs WAN.</li>
  <li>Что делает роутер?</li>
  <li>Диалог про «нет сети».</li>
    </ol>

    <h2>Quick review</h2>
    <p>LAN · роутер · IP · шлюз · трафик</p>
""",
            ),
            _lec(
                'Интернет и протоколы',
                'rit-internet-protocols',
                """
<h2>Lesson goal</h2>
    <p>Говорить о DNS, HTTP/HTTPS, latency и bandwidth.</p>

    <h2>Warm-up</h2>
    <p>Почему сайт открывается по имени, а не по цифрам IP?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>DNS</strong></td><td>имя → IP</td><td>Проблема в DNS.</td></tr>
<tr><td><strong>HTTP / HTTPS</strong></td><td>протоколы веба</td><td>Используйте HTTPS.</td></tr>
<tr><td><strong>latency</strong></td><td>задержка</td><td>Высокая latency.</td></tr>
<tr><td><strong>bandwidth</strong></td><td>пропускная способность</td><td>Мало bandwidth.</td></tr>
<tr><td><strong>пакет</strong></td><td>единица данных</td><td>Пакеты теряются.</td></tr>
<tr><td><strong>firewall</strong></td><td>фильтр трафика</td><td>Firewall блокирует.</td></tr>
<tr><td><strong>порт (сетевой)</strong></td><td>номер сервиса</td><td>Откройте порт 443.</td></tr>
<tr><td><strong>прокси</strong></td><td>посредник</td><td>Нужен корпоративный прокси.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Сайт не резолвится через DNS.</li>
  <li>HTTPS шифрует трафик.</li>
  <li>Latency высокая до Европы.</li>
  <li>Firewall режет порт.</li>
  <li>Проверьте прокси-настройки.</li>
    </ul>

    <h2>Dialogue — медленный сайт</h2>
    <p><strong>Dev:</strong> API тормозит.<br><strong>Net:</strong> Latency 200 мс, потери пакетов.<br><strong>Dev:</strong> Значит сеть, не код?<br><strong>Net:</strong> Сначала проверим канал.</p>

    <h2>Grammar focus — Причина → следствие</h2>
    <p>Из‑за… / Поэтому… / Если… то…</p>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ HTTPS медленнее по закону. → ✅ HTTPS шифрует.</li>
  <li>❌ Bandwidth = ширина клавиатуры. → ✅ Ёмкость канала.</li>
    </ul>

    <h2>Reading — Протоколы в жизни</h2>
    <p>DNS находит адрес, HTTPS защищает страницу, firewall решает, что пускать.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>DNS своими словами.</li>
  <li>HTTPS vs HTTP.</li>
  <li>Объясните latency.</li>
    </ol>

    <h2>Quick review</h2>
    <p>DNS · HTTPS · latency · firewall · bandwidth</p>
""",
            ),
            _lec(
                'Диагностика Wi‑Fi',
                'rit-wifi-troubleshoot',
                """
<h2>Lesson goal</h2>
    <p>Диагностировать Wi‑Fi: сигнал, SSID, аутентификация.</p>

    <h2>Warm-up</h2>
    <p>Что вы делаете первым, когда Wi‑Fi «пропал»?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>SSID</strong></td><td>имя Wi‑Fi сети</td><td>Выберите правильный SSID.</td></tr>
<tr><td><strong>сигнал</strong></td><td>сила радиосвязи</td><td>Слабый сигнал.</td></tr>
<tr><td><strong>аутентификация</strong></td><td>проверка доступа</td><td>Ошибка аутентификации.</td></tr>
<tr><td><strong>канал</strong></td><td>частотный канал</td><td>Канал перегружен.</td></tr>
<tr><td><strong>помехи</strong></td><td>внешние искажения</td><td>Помехи от микроволновки.</td></tr>
<tr><td><strong>гостевая сеть</strong></td><td>сеть для гостей</td><td>Подключите гостевую.</td></tr>
<tr><td><strong>забыть сеть</strong></td><td>сбросить профиль</td><td>Забудьте сеть и подключитесь снова.</td></tr>
<tr><td><strong>точка доступа</strong></td><td>AP</td><td>Точка доступа перегружена.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Забудьте сеть и подключитесь снова.</li>
  <li>Сигнал слабый — подойдите ближе.</li>
  <li>Проверьте пароль SSID.</li>
  <li>Переключитесь на 5 ГГц.</li>
  <li>Перезагрузите точку доступа.</li>
    </ul>

    <h2>Dialogue — не подключается</h2>
    <p><strong>Юзер:</strong> Пароль верный, но не коннектится.<br><strong>IT:</strong> Забудьте сеть. Какой SSID?<br><strong>Юзер:</strong> Office-Guest.<br><strong>IT:</strong> Для работы нужен Office-Corp + сертификат.</p>

    <h2>Grammar focus — Пошаговый чек-лист</h2>
    <ol><li>SSID</li><li>пароль/сертификат</li><li>сигнал</li><li>перезагрузка</li></ol>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ SSID = модель CPU. → ✅ Имя Wi‑Fi.</li>
  <li>❌ Забыть сеть = удалить интернет. → ✅ Сбросить профиль Wi‑Fi.</li>
    </ul>

    <h2>Reading — Типичные причины</h2>
    <p>Неверный SSID, старый профиль, слабый сигнал, перегруженная точка доступа.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Чек-лист из 5 шагов.</li>
  <li>Разница гостевой и корп. сети.</li>
  <li>Объясните помехи.</li>
    </ol>

    <h2>Quick review</h2>
    <p>SSID · сигнал · аутентификация · точка доступа</p>
""",
            ),
            ],
            "practice": {
            'rit-network-basics': _quiz(
                    'rit-q-router',
                    'Роутер',
                    'Net.',
                    'Роутер в основном…',
                    [
                        'A) направляет трафик между сетями',
                        'B) печатает',
                        'C) пишет unit-тесты',
                        'D) рисует логотипы',
                    ],
                    'A',
                ),
            'rit-internet-protocols': _quiz(
                    'rit-q-https',
                    'HTTPS',
                    'Protocols.',
                    'HTTPS предпочтителен, потому что…',
                    [
                        'A) шифрует веб-трафик',
                        'B) медленнее по закону',
                        'C) удаляет DNS',
                        'D) заменяет кабели',
                    ],
                    'A',
                ),
            'rit-wifi-troubleshoot': _quiz(
                    'rit-q-ssid',
                    'SSID',
                    'Wi‑Fi.',
                    'SSID — это…',
                    [
                        'A) имя Wi‑Fi сети',
                        'B) модель CPU',
                        'C) таблица БД',
                        'D) Scrum-событие',
                    ],
                    'A',
                ),
            },
            "exercises": [
            _quiz(
                'rit-m4-latency',
                'Latency',
                'Net.',
                'Latency значит…',
                [
                    'A) задержка ответа сети',
                    'B) бесплатный обед',
                    'C) тип монитора',
                    'D) ключ лицензии',
                ],
                'A',
            ),
            _quiz(
                'rit-m4-dns',
                'DNS',
                'Protocols.',
                'DNS сопоставляет…',
                [
                    'A) доменные имена с IP',
                    'B) пароли с принтерами',
                    'C) баги с кофе',
                    'D) RAM с GPU',
                ],
                'A',
                difficulty='medium',
            ),
            ],
            "homework": _hw(
                'Русский язык для IT — Модуль 4\n1) Объясните LAN/роутер/IP.\n2) Почему HTTPS.\n3) Чек-лист Wi‑Fi.\n4) Глоссарий: DNS, latency, firewall, SSID.'
            ),
        },
{
    "order": 5,
    "title": 'Язык программиста (Programming)',
    "slug": 'rit-programming',
    "description": 'Kod so‘z boyligi, algoritmlar va Git asoslari — ruscha.',
    "lectures": [
            _lec(
                'Словарь кода',
                'rit-code-vocab',
                """
<h2>Lesson goal</h2>
    <p>Использовать базовый словарь разработки на русском.</p>

    <h2>Warm-up</h2>
    <p>Что такое баг простыми словами?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>баг / дефект</strong></td><td>ошибка в ПО</td><td>Нашли критический баг.</td></tr>
<tr><td><strong>функция / метод</strong></td><td>блок кода</td><td>Вызовите функцию.</td></tr>
<tr><td><strong>переменная</strong></td><td>именованное значение</td><td>Обновите переменную.</td></tr>
<tr><td><strong>репозиторий</strong></td><td>хранилище кода</td><td>Клонируйте репозиторий.</td></tr>
<tr><td><strong>коммит</strong></td><td>сохранённое изменение</td><td>Сделайте коммит.</td></tr>
<tr><td><strong>рефакторинг</strong></td><td>улучшение без смены поведения</td><td>Нужен рефакторинг.</td></tr>
<tr><td><strong>edge case</strong></td><td>редкий/граничный случай</td><td>Учтите edge case.</td></tr>
<tr><td><strong>лог</strong></td><td>журнал событий</td><td>Смотрите логи.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Я воспроизвёл баг.</li>
  <li>Нужен рефакторинг этого модуля.</li>
  <li>Добавьте обработку edge case.</li>
  <li>Закоммитьте с понятным сообщением.</li>
  <li>Логи показывают NPE.</li>
    </ul>

    <h2>Dialogue — code review</h2>
    <p><strong>Ревьюер:</strong> Имя переменной неясное.<br><strong>Автор:</strong> Переименую.<br><strong>Ревьюер:</strong> И покройте edge case пустой строки.</p>

    <h2>Grammar focus — Прошедшее время для багов</h2>
    <ul><li>Я <strong>нашёл</strong> баг.</li><li>Мы <strong>исправили</strong> регрессию.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Баг = насекомое на работе. → ✅ Ошибка ПО.</li>
  <li>❌ Рефакторинг = удалить репо. → ✅ Улучшить структуру.</li>
    </ul>

    <h2>Reading — Ясный язык кода</h2>
    <p>Говорите: симптом → шаги → ожидаемое/фактическое → логи. Так быстрее помогают.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Определите баг/рефакторинг/edge case.</li>
  <li>Опишите баг 4 предложениями.</li>
  <li>Диалог code review.</li>
    </ol>

    <h2>Quick review</h2>
    <p>баг · переменная · коммит · рефакторинг · edge case</p>
""",
            ),
            _lec(
                'Об алгоритмах',
                'rit-algorithms-talk',
                """
<h2>Lesson goal</h2>
    <p>Кратко объяснять алгоритм, сложность и компромиссы.</p>

    <h2>Warm-up</h2>
    <p>Как объяснить решение коллеге за 1 минуту?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>алгоритм</strong></td><td>последовательность шагов</td><td>Опишите алгоритм.</td></tr>
<tr><td><strong>сложность</strong></td><td>оценка затрат</td><td>Сложность O(n).</td></tr>
<tr><td><strong>компромисс / trade-off</strong></td><td>выбор плюсов/минусов</td><td>Есть trade-off по памяти.</td></tr>
<tr><td><strong>оптимизация</strong></td><td>улучшение производительности</td><td>Нужна оптимизация.</td></tr>
<tr><td><strong>кэш</strong></td><td>быстрое временное хранение</td><td>Добавим кэш.</td></tr>
<tr><td><strong>бутылочное горлышко</strong></td><td>узкое место</td><td>БД — bottleneck.</td></tr>
<tr><td><strong>псевдокод</strong></td><td>схема без синтаксиса</td><td>Напишите псевдокод.</td></tr>
<tr><td><strong>корректность</strong></td><td>правильность результата</td><td>Сначала корректность.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Сначала корректность, потом скорость.</li>
  <li>Компромисс: память vs время.</li>
  <li>Bottleneck в запросе к БД.</li>
  <li>Давайте псевдокод на доске.</li>
  <li>Кэш снизит latency.</li>
    </ul>

    <h2>Dialogue — разбор задачи</h2>
    <p><strong>Интервьюер:</strong> Как будете сортировать?<br><strong>Кандидат:</strong> Сначала уточню ограничения.<br><strong>Интервьюер:</strong> n до миллиона.<br><strong>Кандидат:</strong> Тогда O(n log n), обсудим память.</p>

    <h2>Grammar focus — Сначала / затем / поэтому</h2>
    <p>Сначала уточняем ввод. Затем предлагаем подход. Поэтому выбираем структуру данных.</p>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Trade-off = бесплатный обед. → ✅ Выбор между вариантами.</li>
  <li>❌ Оптимизация до понимания задачи. → ✅ Сначала ясность.</li>
    </ul>

    <h2>Reading — Объяснять просто</h2>
    <p>Цель → вход/выход → шаги → сложность → риски. Так звучит уверенно на русском и на собеседовании.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Объясните алгоритм поиска.</li>
  <li>Назовите один trade-off.</li>
  <li>Скажите псевдокод вслух.</li>
    </ol>

    <h2>Quick review</h2>
    <p>алгоритм · trade-off · кэш · сложность · псевдокод</p>
""",
            ),
            _lec(
                'Git на русском',
                'rit-git-basics',
                """
<h2>Lesson goal</h2>
    <p>Говорить о branch, PR, merge и конфликтах.</p>

    <h2>Warm-up</h2>
    <p>Зачем ветки, если можно всё в main?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>ветка / branch</strong></td><td>параллельная линия разработки</td><td>Создайте ветку.</td></tr>
<tr><td><strong>pull request / MR</strong></td><td>запрос на влитие</td><td>Откройте PR.</td></tr>
<tr><td><strong>merge</strong></td><td>слияние изменений</td><td>Замерджили в main.</td></tr>
<tr><td><strong>конфликт</strong></td><td>несовместимые правки</td><td>Есть merge conflict.</td></tr>
<tr><td><strong>rebase</strong></td><td>перенос коммитов</td><td>Сделайте rebase аккуратно.</td></tr>
<tr><td><strong>main / master</strong></td><td>основная ветка</td><td>Не пушьте напрямую в main.</td></tr>
<tr><td><strong>review</strong></td><td>проверка кода</td><td>Ждём review.</td></tr>
<tr><td><strong>CI красный</strong></td><td>пайплайн упал</td><td>CI красный — смотрите тесты.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Я открыл PR.</li>
  <li>Конфликт в файле config.</li>
  <li>Дождитесь зелёного CI.</li>
  <li>Не пушьте в main без review.</li>
  <li>Сделаю rebase на latest main.</li>
    </ul>

    <h2>Dialogue — конфликт</h2>
    <p><strong>Dev A:</strong> Конфликт в utils.py.<br><strong>Dev B:</strong> Давайте созвонимся и разрешим вместе.<br><strong>Dev A:</strong> Ок, после — прогоним тесты.</p>

    <h2>Grammar focus — Перфект для опыта</h2>
    <ul><li>Я <strong>уже делал</strong> rebase.</li><li>Мы <strong>не мержили</strong> без CI.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Branch = дерево во дворе. → ✅ Линия разработки.</li>
  <li>❌ Conflict = ссора только. → ✅ Ещё и конфликт правок в Git.</li>
    </ul>

    <h2>Reading — Гигиена Git</h2>
    <p>Маленькие коммиты, понятные PR, зелёный CI, аккуратное разрешение конфликтов.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Что такое PR?</li>
  <li>Как объяснить conflict?</li>
  <li>Правила работы с main.</li>
    </ol>

    <h2>Quick review</h2>
    <p>branch · PR · merge · conflict · CI</p>
""",
            ),
            ],
            "practice": {
            'rit-code-vocab': _quiz(
                    'rit-q-bug',
                    'Баг',
                    'Code.',
                    'Баг — это…',
                    [
                        'A) ошибка в ПО',
                        'B) тип монитора',
                        'C) пароль Wi‑Fi',
                        'D) переговорка',
                    ],
                    'A',
                ),
            'rit-algorithms-talk': _quiz(
                    'rit-q-edge',
                    'Edge case',
                    'Algo.',
                    'Edge case — это…',
                    [
                        'A) необычный ввод, который может сломать код',
                        'B) край стола',
                        'C) бренд GPU',
                        'D) Scrum-перекус',
                    ],
                    'A',
                ),
            'rit-git-basics': _quiz(
                    'rit-q-pr',
                    'PR',
                    'Git.',
                    'Pull request — это…',
                    [
                        'A) запрос на ревью и слияние изменений',
                        'B) апгрейд железа',
                        'C) фишинг',
                        'D) только бэкап БД',
                    ],
                    'A',
                ),
            },
            "exercises": [
            _quiz(
                'rit-m5-refactor',
                'Рефакторинг',
                'Code.',
                'Рефакторинг значит…',
                [
                    'A) улучшить код без смены поведения',
                    'B) удалить репозиторий',
                    'C) купить ноутбук',
                    'D) выключить firewall',
                ],
                'A',
            ),
            _quiz(
                'rit-m5-conflict',
                'Конфликт',
                'Git.',
                'Merge conflict значит…',
                [
                    'A) нужно разрешить конфликтующие правки',
                    'B) закончился кофе',
                    'C) DNS идеален',
                    'D) MFA навсегда опционален',
                ],
                'A',
                difficulty='medium',
            ),
            ],
            "homework": _hw(
                'Русский язык для IT — Модуль 5\n1) Опишите баг по шаблону.\n2) Объясните алгоритм за 60 сек.\n3) Мини-глоссарий Git.\n4) Правила PR команды.'
            ),
        },
{
    "order": 6,
    "title": 'Базы данных (Databases)',
    "slug": 'rit-databases',
    "description": 'DB tushunchalari, SQL haqida gapirish va maxfiylik — ruscha.',
    "lectures": [
            _lec(
                'Понятия БД',
                'rit-db-concepts',
                """
<h2>Lesson goal</h2>
    <p>Объяснять таблицу, ключи, индекс и транзакцию.</p>

    <h2>Warm-up</h2>
    <p>Чем таблица Excel отличается от таблицы в БД?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>база данных</strong></td><td>организованное хранилище данных</td><td>Данные в БД.</td></tr>
<tr><td><strong>таблица / строка / столбец</strong></td><td>структура реляционной БД</td><td>Добавьте столбец.</td></tr>
<tr><td><strong>первичный ключ</strong></td><td>уникальный идентификатор строки</td><td>id — primary key.</td></tr>
<tr><td><strong>внешний ключ</strong></td><td>ссылка на другую таблицу</td><td>user_id — FK.</td></tr>
<tr><td><strong>индекс</strong></td><td>ускоряет поиск</td><td>Нужен индекс.</td></tr>
<tr><td><strong>транзакция</strong></td><td>атомарная операция</td><td>Транзакция откатилась.</td></tr>
<tr><td><strong>бэкап</strong></td><td>резервная копия</td><td>Ежедневный бэкап.</td></tr>
<tr><td><strong>репликация</strong></td><td>копии для надёжности/чтения</td><td>Настроена репликация.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Primary key уникален.</li>
  <li>Без WHERE удалять опасно.</li>
  <li>Индекс ускорит SELECT.</li>
  <li>Сделайте бэкап перед миграцией.</li>
  <li>Транзакция должна быть атомарной.</li>
    </ul>

    <h2>Dialogue — медленный запрос</h2>
    <p><strong>Dev:</strong> Отчёт тормозит.<br><strong>DBA:</strong> Нет индекса по date.<br><strong>Dev:</strong> Добавим и проверим план запроса.</p>

    <h2>Grammar focus — Нельзя / нужно / осторожно</h2>
    <ul><li><strong>Нельзя</strong> DELETE без WHERE.</li><li><strong>Нужно</strong> бэкапить.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Primary key = пароль Wi‑Fi. → ✅ Уникальный id строки.</li>
  <li>❌ Индекс = содержание книги только. → ✅ В БД ускоряет поиск.</li>
    </ul>

    <h2>Reading — Данные — актив</h2>
    <p>Структура, ключи и бэкапы важнее «просто сохранить файл».</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>PK vs FK.</li>
  <li>Зачем индекс?</li>
  <li>Почему бэкап перед миграцией?</li>
    </ol>

    <h2>Quick review</h2>
    <p>таблица · PK · FK · индекс · транзакция · бэкап</p>
""",
            ),
            _lec(
                'Говорим о SQL',
                'rit-sql-talk',
                """
<h2>Lesson goal</h2>
    <p>Описывать SELECT/JOIN/UPDATE словами, не только кодом.</p>

    <h2>Warm-up</h2>
    <p>Как объяснить JOIN менеджеру?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>запрос / query</strong></td><td>запрос к данным</td><td>Напишите query.</td></tr>
<tr><td><strong>SELECT</strong></td><td>чтение строк</td><td>SELECT только нужные поля.</td></tr>
<tr><td><strong>JOIN</strong></td><td>объединение таблиц</td><td>JOIN users и orders.</td></tr>
<tr><td><strong>WHERE</strong></td><td>фильтр</td><td>Добавьте WHERE.</td></tr>
<tr><td><strong>миграция</strong></td><td>изменение схемы</td><td>Миграция на staging.</td></tr>
<tr><td><strong>план запроса</strong></td><td>как БД выполняет запрос</td><td>Смотрите plan.</td></tr>
<tr><td><strong>NULL</strong></td><td>пустое значение</td><td>Учтите NULL.</td></tr>
<tr><td><strong>производительность запроса</strong></td><td>скорость SQL</td><td>Оптимизируем query.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>JOIN по user_id.</li>
  <li>Фильтруйте в WHERE, не в приложении.</li>
  <li>Миграцию сначала на staging.</li>
  <li>NULL ≠ 0.</li>
  <li>Запрос сканирует всю таблицу.</li>
    </ul>

    <h2>Dialogue — код-ревью SQL</h2>
    <p><strong>Ревьюер:</strong> Здесь SELECT *.<br><strong>Автор:</strong> Заменю на нужные поля.<br><strong>Ревьюер:</strong> И проверьте индекс.</p>

    <h2>Grammar focus — Пассив для процедур</h2>
    <ul><li>Миграция <strong>была применена</strong> на staging.</li><li>Индекс <strong>был добавлен</strong>.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ JOIN = перезапуск роутера. → ✅ Связка таблиц.</li>
  <li>❌ DELETE без WHERE норма. → ✅ Опасно.</li>
    </ul>

    <h2>Reading — SQL как язык команды</h2>
    <p>Говорите целью: «нужны заказы клиента за март» — затем пишите SQL.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Объясните JOIN.</li>
  <li>Что проверить перед DELETE?</li>
  <li>Зачем staging для миграций?</li>
    </ol>

    <h2>Quick review</h2>
    <p>query · JOIN · WHERE · миграция · NULL</p>
""",
            ),
            _lec(
                'Конфиденциальность данных',
                'rit-data-privacy',
                """
<h2>Lesson goal</h2>
    <p>Говорить о персональных данных, согласии и утечках.</p>

    <h2>Warm-up</h2>
    <p>Какие данные нельзя светить в логах?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>персональные данные</strong></td><td>данные о человеке</td><td>Не логируйте ПДн.</td></tr>
<tr><td><strong>согласие</strong></td><td>разрешение на использование</td><td>Нужно согласие пользователя.</td></tr>
<tr><td><strong>шифрование</strong></td><td>защита кодированием</td><td>Данные зашифрованы.</td></tr>
<tr><td><strong>маскирование</strong></td><td>скрытие части данных</td><td>Замаскируйте номер карты.</td></tr>
<tr><td><strong>утечка / breach</strong></td><td>несанкционированный доступ</td><td>Был data breach.</td></tr>
<tr><td><strong>доступ по роли</strong></td><td>минимальные права</td><td>Least privilege.</td></tr>
<tr><td><strong>аудит</strong></td><td>проверка действий</td><td>Включите аудит.</td></tr>
<tr><td><strong>политика хранения</strong></td><td>сколько хранить</td><td>Срок хранения — 1 год.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Не храните пароли в открытом виде.</li>
  <li>Замаскируйте ПДн в логах.</li>
  <li>Сообщите о подозрении на утечку.</li>
  <li>Доступ только по роли.</li>
  <li>Проверьте срок хранения.</li>
    </ul>

    <h2>Dialogue — логи с ПДн</h2>
    <p><strong>Sec:</strong> В логах видны телефоны.<br><strong>Dev:</strong> Уберём и замаскируем.<br><strong>Sec:</strong> Сделайте срочно, до релиза.</p>

    <h2>Grammar focus — Должен / запрещено</h2>
    <ul><li>Вы <strong>должны</strong> шифровать секреты.</li><li><strong>Запрещено</strong> отправлять ПДн в личный чат.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Breach = успешный бэкап. → ✅ Утечка/взлом.</li>
  <li>❌ Согласие не нужно, если удобно. → ✅ Нужно основание/согласие.</li>
    </ul>

    <h2>Reading — Приватность = доверие</h2>
    <p>Команды, которые аккуратно говорят о данных, меньше рискуют штрафами и репутацией.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Что такое ПДн?</li>
  <li>3 правила логов.</li>
  <li>Что делать при подозрении на breach?</li>
    </ol>

    <h2>Quick review</h2>
    <p>ПДн · согласие · шифрование · breach · least privilege</p>
""",
            ),
            ],
            "practice": {
            'rit-db-concepts': _quiz(
                    'rit-q-pk',
                    'PK',
                    'DB.',
                    'Первичный ключ…',
                    [
                        'A) уникально идентифицирует строку',
                        'B) печатает счета',
                        'C) пароль Wi‑Fi',
                        'D) удаляет DNS',
                    ],
                    'A',
                ),
            'rit-sql-talk': _quiz(
                    'rit-q-join',
                    'JOIN',
                    'SQL.',
                    'JOIN используют, чтобы…',
                    [
                        'A) объединить строки связанных таблиц',
                        'B) перезапустить роутер',
                        'C) нарисовать логотип',
                        'D) создать Slack-канал',
                    ],
                    'A',
                ),
            'rit-data-privacy': _quiz(
                    'rit-q-encrypt',
                    'Шифрование',
                    'Privacy.',
                    'Зашифровать данные значит…',
                    [
                        'A) закодировать для защиты конфиденциальности',
                        'B) напечатать на плакатах',
                        'C) выложить в соцсети',
                        'D) перевести на латынь',
                    ],
                    'A',
                ),
            },
            "exercises": [
            _quiz(
                'rit-m6-delete',
                'DELETE',
                'SQL.',
                'Лучший совет для DELETE:',
                [
                    'A) Используйте WHERE и бэкапы/тесты',
                    'B) Сначала удалите всё в prod',
                    'C) Никогда не используйте WHERE',
                    'D) Только по пятницам',
                ],
                'A',
            ),
            _quiz(
                'rit-m6-consent',
                'Согласие',
                'Privacy.',
                'Согласие в privacy значит…',
                [
                    'A) разрешение использовать данные для цели',
                    'B) вечный бесплатный cloud',
                    'C) удаление бэкапов',
                    'D) публичный OTP',
                ],
                'A',
                difficulty='medium',
            ),
            ],
            "homework": _hw(
                'Русский язык для IT — Модуль 6\n1) Объясните PK/FK/индекс.\n2) Опишите опасный DELETE и как сделать безопасно.\n3) 6 правил ПДн.\n4) Глоссарий SQL.'
            ),
        },
{
    "order": 7,
    "title": 'Веб (Web)',
    "slug": 'rit-web',
    "description": 'Frontend/backend, API/HTTP va deploy — ruscha.',
    "lectures": [
            _lec(
                'Frontend и backend',
                'rit-frontend-backend',
                """
<h2>Lesson goal</h2>
    <p>Объяснять слои веб-приложения.</p>

    <h2>Warm-up</h2>
    <p>Что видит пользователь — frontend или backend?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>frontend</strong></td><td>клиентская часть</td><td>Баг на frontend.</td></tr>
<tr><td><strong>backend</strong></td><td>серверная логика</td><td>Backend отдал 500.</td></tr>
<tr><td><strong>fullstack</strong></td><td>и то и другое</td><td>Fullstack-разработчик.</td></tr>
<tr><td><strong>UI / UX</strong></td><td>интерфейс / опыт</td><td>Улучшим UX.</td></tr>
<tr><td><strong>адаптивная вёрстка</strong></td><td>под разные экраны</td><td>Нужна адаптивность.</td></tr>
<tr><td><strong>состояние</strong></td><td>state приложения</td><td>Состояние формы.</td></tr>
<tr><td><strong>рендеринг</strong></td><td>отрисовка</td><td>Проблема рендеринга.</td></tr>
<tr><td><strong>эндпоинт</strong></td><td>точка API</td><td>Вызовите эндпоинт.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Это UI-баг на frontend.</li>
  <li>Backend валидирует данные.</li>
  <li>Нужен адаптивный layout.</li>
  <li>Эндпоинт вернул ошибку.</li>
  <li>Давайте разделим ответственность слоёв.</li>
    </ul>

    <h2>Dialogue — где баг?</h2>
    <p><strong>QA:</strong> Кнопка не работает.<br><strong>FE:</strong> Запрос уходит.<br><strong>BE:</strong> Вижу 401 — проблема токена.</p>

    <h2>Grammar focus — Это / то</h2>
    <p><strong>Это</strong> проблема UI. <strong>То</strong> — ошибка API.</p>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Frontend = только кабели БД. → ✅ То, что видит пользователь.</li>
  <li>❌ Backend = только CSS. → ✅ Серверная логика.</li>
    </ul>

    <h2>Reading — Разделение слоёв</h2>
    <p>Чёткий язык «FE/BE/API» ускоряет поиск причины.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>FE vs BE.</li>
  <li>Что такое эндпоинт?</li>
  <li>Диалог про 401.</li>
    </ol>

    <h2>Quick review</h2>
    <p>frontend · backend · UI · эндпоинт</p>
""",
            ),
            _lec(
                'API и HTTP',
                'rit-apis-http',
                """
<h2>Lesson goal</h2>
    <p>Говорить о REST, статусах и JSON.</p>

    <h2>Warm-up</h2>
    <p>Что значит ошибка 404?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>API</strong></td><td>интерфейс между системами</td><td>Публичный API.</td></tr>
<tr><td><strong>HTTP-метод</strong></td><td>GET/POST/PUT/DELETE</td><td>Используйте POST.</td></tr>
<tr><td><strong>статус-код</strong></td><td>код ответа</td><td>Получили 500.</td></tr>
<tr><td><strong>JSON</strong></td><td>формат данных</td><td>Тело в JSON.</td></tr>
<tr><td><strong>авторизация</strong></td><td>проверка прав</td><td>Нет авторизации.</td></tr>
<tr><td><strong>токен</strong></td><td>ключ доступа</td><td>Токен истёк.</td></tr>
<tr><td><strong>rate limit</strong></td><td>лимит запросов</td><td>Упёрлись в rate limit.</td></tr>
<tr><td><strong>документация API</strong></td><td>описание методов</td><td>Смотрите API docs.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>GET безопасен для чтения.</li>
  <li>404 — не найдено.</li>
  <li>401 — не авторизован.</li>
  <li>Пришлите пример JSON.</li>
  <li>Токен нужно обновить.</li>
    </ul>

    <h2>Dialogue — интеграция</h2>
    <p><strong>Dev:</strong> Интеграция падает.<br><strong>Партнёр:</strong> Какой статус?<br><strong>Dev:</strong> 429.<br><strong>Партнёр:</strong> Это rate limit — снизьте частоту.</p>

    <h2>Grammar focus — Числа как факты</h2>
    <ul><li>Статус <strong>404</strong> значит «не найдено».</li><li><strong>200</strong> — успех.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ API готовит обед. → ✅ Интерфейс ПО.</li>
  <li>❌ 401 = успех. → ✅ Не авторизован.</li>
    </ul>

    <h2>Reading — Статусы экономят время</h2>
    <p>Называйте код и короткое значение: 404 not found, 500 server error.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Что такое API?</li>
  <li>401 vs 403.</li>
  <li>Зачем JSON?</li>
    </ol>

    <h2>Quick review</h2>
    <p>API · JSON · 404 · токен · rate limit</p>
""",
            ),
            _lec(
                'Деплой веб-приложений',
                'rit-deploy-web',
                """
<h2>Lesson goal</h2>
    <p>Обсуждать staging, prod, rollback релиза.</p>

    <h2>Warm-up</h2>
    <p>Почему нельзя деплоить сразу в production без проверки?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>деплой</strong></td><td>выкладка версии</td><td>Деплой в 18:00.</td></tr>
<tr><td><strong>staging</strong></td><td>предпрод</td><td>Сначала staging.</td></tr>
<tr><td><strong>production</strong></td><td>боевая среда</td><td>Ошибка в production.</td></tr>
<tr><td><strong>релиз</strong></td><td>выпуск версии</td><td>Релиз задержан.</td></tr>
<tr><td><strong>rollback</strong></td><td>откат релиза</td><td>Срочный rollback.</td></tr>
<tr><td><strong>feature flag</strong></td><td>флаг функции</td><td>Выключим флагом.</td></tr>
<tr><td><strong>простой / downtime</strong></td><td>недоступность</td><td>Минимизируем downtime.</td></tr>
<tr><td><strong>мониторинг после релиза</strong></td><td>наблюдение</td><td>Смотрим метрики 30 минут.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Выкатили на staging.</li>
  <li>В prod выросла ошибка 500.</li>
  <li>Делаем rollback.</li>
  <li>Включим feature flag постепенно.</li>
  <li>После релиза дежурим в канале.</li>
    </ul>

    <h2>Dialogue — инцидент после релиза</h2>
    <p><strong>On-call:</strong> Ошибки выросли после деплоя.<br><strong>Lead:</strong> Rollback сейчас.<br><strong>On-call:</strong> Откатили, пишем постмортем.</p>

    <h2>Grammar focus — План B</h2>
    <p>Если… то rollback / feature flag / hotfix.</p>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Staging = театр. → ✅ Предпрод среда.</li>
  <li>❌ Rollback стыдно. → ✅ Rollback — ответственная практика.</li>
    </ul>

    <h2>Reading — Безопасный релиз</h2>
    <p>Staging → проверка → prod → мониторинг → rollback при спайке ошибок.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Staging vs prod.</li>
  <li>Когда rollback?</li>
  <li>Что такое feature flag?</li>
    </ol>

    <h2>Quick review</h2>
    <p>деплой · staging · production · rollback · downtime</p>
""",
            ),
            ],
            "practice": {
            'rit-frontend-backend': _quiz(
                    'rit-q-frontend',
                    'Frontend',
                    'Web.',
                    'Frontend — это…',
                    [
                        'A) пользовательская часть приложения',
                        'B) только кабели БД',
                        'C) фишинг',
                        'D) кухня офиса',
                    ],
                    'A',
                ),
            'rit-apis-http': _quiz(
                    'rit-q-404',
                    '404',
                    'HTTP.',
                    '404 обычно значит…',
                    [
                        'A) не найдено',
                        'B) всегда успех',
                        'C) принтер офлайн',
                        'D) батарея села',
                    ],
                    'A',
                ),
            'rit-deploy-web': _quiz(
                    'rit-q-staging',
                    'Staging',
                    'Deploy.',
                    'Staging — это…',
                    [
                        'A) среда перед production',
                        'B) только хобби театра',
                        'C) бренд GPU',
                        'D) SSID',
                    ],
                    'A',
                ),
            },
            "exercises": [
            _quiz(
                'rit-m7-api',
                'API',
                'Web.',
                'API позволяет ПО…',
                [
                    'A) взаимодействовать с другим ПО',
                    'B) готовить обед',
                    'C) заменить монитор',
                    'D) придумывать пароли',
                ],
                'A',
            ),
            _quiz(
                'rit-m7-401',
                '401',
                'HTTP.',
                'HTTP 401 часто значит…',
                [
                    'A) не авторизован',
                    'B) успех',
                    'C) замятие бумаги',
                    'D) батарея полная',
                ],
                'A',
                difficulty='medium',
            ),
            ],
            "homework": _hw(
                'Русский язык для IT — Модуль 7\n1) FE/BE своими словами.\n2) Таблица статус-кодов (5 шт).\n3) Чек-лист релиза.\n4) Глоссарий API.'
            ),
        },
{
    "order": 8,
    "title": 'Cloud и DevOps',
    "slug": 'rit-cloud-devops',
    "description": 'Cloud asoslari, konteynerlar/CI va monitoring — ruscha.',
    "lectures": [
            _lec(
                'Основы облака',
                'rit-cloud-basics',
                """
<h2>Lesson goal</h2>
    <p>Объяснять IaaS/PaaS/SaaS и регионы.</p>

    <h2>Warm-up</h2>
    <p>Чем облако отличается от сервера в кабинете?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>облако / cloud</strong></td><td>удалённые ресурсы по сети</td><td>Сервис в облаке.</td></tr>
<tr><td><strong>IaaS / PaaS / SaaS</strong></td><td>модели сервиса</td><td>Gmail — пример SaaS.</td></tr>
<tr><td><strong>регион</strong></td><td>географическая зона</td><td>Выберите регион.</td></tr>
<tr><td><strong>масштабирование</strong></td><td>увеличение мощности</td><td>Нужен scale-out.</td></tr>
<tr><td><strong>инстанс</strong></td><td>виртуальный сервер</td><td>Поднимите инстанс.</td></tr>
<tr><td><strong>стоимость / billing</strong></td><td>счёт за ресурсы</td><td>Billing вырос.</td></tr>
<tr><td><strong>доступность</strong></td><td>uptime</td><td>SLA по доступности.</td></tr>
<tr><td><strong>провайдер</strong></td><td>AWS/GCP/Azure и др.</td><td>Смена провайдера.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Поднимем инстанс в регионе EU.</li>
  <li>SaaS не требует своей установки.</li>
  <li>Масштабируем при пике.</li>
  <li>Проверьте billing alerts.</li>
  <li>Выберите регион ближе к пользователям.</li>
    </ul>

    <h2>Dialogue — выбор модели</h2>
    <p><strong>PM:</strong> Нам свой сервер?<br><strong>DevOps:</strong> Для MVP хватит PaaS/SaaS.<br><strong>PM:</strong> Дешевле?<br><strong>DevOps:</strong> На старте да, следим за billing.</p>

    <h2>Grammar focus — Сравнение моделей</h2>
    <ul><li>IaaS — контроль инфраструктуры.</li><li>SaaS — готовое ПО.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Cloud = только погода. → ✅ Удалённые IT-ресурсы.</li>
  <li>❌ SaaS = всегда свои серверы. → ✅ Готовое ПО по сети.</li>
    </ul>

    <h2>Reading — Облако гибкое, но не бесплатное</h2>
    <p>Платите за использование: выключайте тест-инстансы.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>IaaS vs SaaS.</li>
  <li>Зачем регион?</li>
  <li>Что такое billing alert?</li>
    </ol>

    <h2>Quick review</h2>
    <p>cloud · SaaS · регион · масштабирование · billing</p>
""",
            ),
            _lec(
                'Контейнеры и CI',
                'rit-containers-ci',
                """
<h2>Lesson goal</h2>
    <p>Говорить о Docker, пайплайнах и зелёном CI.</p>

    <h2>Warm-up</h2>
    <p>Что делает CI, когда вы пушите код?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>контейнер</strong></td><td>упаковка приложения с зависимостями</td><td>Соберите контейнер.</td></tr>
<tr><td><strong>образ</strong></td><td>шаблон контейнера</td><td>Образ устарел.</td></tr>
<tr><td><strong>Docker</strong></td><td>платформа контейнеров</td><td>Docker на локали.</td></tr>
<tr><td><strong>CI</strong></td><td>непрерывная интеграция</td><td>CI упал.</td></tr>
<tr><td><strong>пайплайн</strong></td><td>цепочка шагов сборки</td><td>Пайплайн долгий.</td></tr>
<tr><td><strong>артефакт</strong></td><td>результат сборки</td><td>Сохраните артефакт.</td></tr>
<tr><td><strong>зелёный / красный CI</strong></td><td>успех / падение</td><td>Дождитесь зелёного CI.</td></tr>
<tr><td><strong>окружение</strong></td><td>env</td><td>Переменные окружения.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>CI должен быть зелёным до мержа.</li>
  <li>Образ соберём в пайплайне.</li>
  <li>Контейнер одинаково бежит везде.</li>
  <li>Секрет — в env, не в коде.</li>
  <li>Пайплайн кэширует зависимости.</li>
    </ul>

    <h2>Dialogue — красный CI</h2>
    <p><strong>Dev:</strong> Почему CI красный?<br><strong>Коллега:</strong> Упал unit-тест на auth.<br><strong>Dev:</strong> Исправлю и перезапущу пайплайн.</p>

    <h2>Grammar focus — Условные конструкции</h2>
    <ul><li>Если CI красный, <strong>не мержим</strong>.</li><li>Когда тесты зелёные, открываем PR.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Контейнер = коробка для обеда. → ✅ Упаковка приложения.</li>
  <li>❌ CI готовит еду. → ✅ Автосборка/тесты.</li>
    </ul>

    <h2>Reading — Одинаковая среда</h2>
    <p>Контейнеры уменьшают «у меня работает». CI ловит регрессии рано.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Что в контейнере?</li>
  <li>Зачем CI?</li>
  <li>Правило про красный CI.</li>
    </ol>

    <h2>Quick review</h2>
    <p>контейнер · Docker · CI · пайплайн · артефакт</p>
""",
            ),
            _lec(
                'Мониторинг и алерты',
                'rit-monitoring',
                """
<h2>Lesson goal</h2>
    <p>Описывать метрики, алерты, инциденты и on-call.</p>

    <h2>Warm-up</h2>
    <p>Что важнее: красивый дашборд или понятный алерт?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>мониторинг</strong></td><td>наблюдение за системой</td><td>Настроим мониторинг.</td></tr>
<tr><td><strong>метрика</strong></td><td>измеряемый показатель</td><td>Метрика latency.</td></tr>
<tr><td><strong>алерт</strong></td><td>уведомление о проблеме</td><td>Пришёл алерт.</td></tr>
<tr><td><strong>инцидент</strong></td><td>серьёзный сбой</td><td>Открыли инцидент.</td></tr>
<tr><td><strong>on-call</strong></td><td>дежурство</td><td>Сегодня я on-call.</td></tr>
<tr><td><strong>дашборд</strong></td><td>панель метрик</td><td>Смотрите дашборд.</td></tr>
<tr><td><strong>SLO / SLA</strong></td><td>цели надёжности / договор</td><td>Нарушили SLO.</td></tr>
<tr><td><strong>постмортем</strong></td><td>разбор после инцидента</td><td>Пишем постмортем.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Алерт: высокий error rate.</li>
  <li>Я on-call до 22:00.</li>
  <li>Инцидент P1 — собираем war room.</li>
  <li>Сначала стабилизация, потом разбор.</li>
  <li>Постмортем без обвинений.</li>
    </ul>

    <h2>Dialogue — ночной алерт</h2>
    <p><strong>Alert:</strong> 5xx > 5%.<br><strong>On-call:</strong> Подтверждаю деградацию API.<br><strong>Lead:</strong> Откатываем релиз и обновляем статус-страницу.</p>

    <h2>Grammar focus — Приоритеты</h2>
    <ul><li>Сначала влияние на пользователей.</li><li>Потом корневая причина.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Инцидент = успешный тест. → ✅ Серьёзный сбой.</li>
  <li>❌ On-call = отпуск. → ✅ Дежурство по инцидентам.</li>
    </ul>

    <h2>Reading — Спокойный on-call</h2>
    <p>Ясный язык: симптом, влияние, действие, ETA.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Метрика vs алерт.</li>
  <li>Что писать в статус инцидента?</li>
  <li>Зачем постмортем?</li>
    </ol>

    <h2>Quick review</h2>
    <p>мониторинг · алерт · инцидент · on-call · постмортем</p>
""",
            ),
            ],
            "practice": {
            'rit-cloud-basics': _quiz(
                    'rit-q-cloud',
                    'Cloud',
                    'Cloud.',
                    'Облачные вычисления — это…',
                    [
                        'A) использование удалённых серверов по интернету',
                        'B) только прогноз погоды',
                        'C) печать на бумажных облаках',
                        'D) удаление сетей',
                    ],
                    'A',
                ),
            'rit-containers-ci': _quiz(
                    'rit-q-ci',
                    'CI',
                    'DevOps.',
                    'CI в основном…',
                    [
                        'A) автоматически собирает/тестирует изменения',
                        'B) готовит обеды',
                        'C) меняет клавиатуры',
                        'D) выключает мониторинг',
                    ],
                    'A',
                ),
            'rit-monitoring': _quiz(
                    'rit-q-alert',
                    'Алерт',
                    'Ops.',
                    'Алерт — это…',
                    [
                        'A) уведомление о возможной проблеме',
                        'B) тип SSD',
                        'C) Scrum-перекус',
                        'D) цвет CSS',
                    ],
                    'A',
                ),
            },
            "exercises": [
            _quiz(
                'rit-m8-saas',
                'SaaS',
                'Cloud.',
                'Примеры SaaS обычно…',
                [
                    'A) готовое ПО через интернет',
                    'B) всегда свои стойки серверов',
                    'C) HDMI-кабели',
                    'D) только механические клавиатуры',
                ],
                'A',
            ),
            _quiz(
                'rit-m8-incident',
                'Инцидент',
                'Monitoring.',
                'Инцидент — это…',
                [
                    'A) серьёзный сбой сервиса',
                    'B) успешный unit-тест',
                    'C) новый эмодзи',
                    'D) календарь праздников',
                ],
                'A',
                difficulty='medium',
            ),
            ],
            "homework": _hw(
                'Русский язык для IT — Модуль 8\n1) IaaS vs SaaS с примерами.\n2) Шаблон отчёта о красном CI.\n3) Глоссарий DevOps.\n4) Handover on-call 60 сек.'
            ),
        }
]


def build_russian_it_modules():
    from apps.core.russian_it_academic import ACADEMIC_MODULE, INTERVIEW_MODULE, enrich_modules
    from apps.core.russian_it_modules_extra import EXTRA_MODULES

    head = [m for m in MODULES if m["order"] <= 8]
    return enrich_modules(head + list(EXTRA_MODULES) + [ACADEMIC_MODULE, INTERVIEW_MODULE])
