"""
Extra Russian-for-IT modules (9–15).
Merged in russian_it_content.build_russian_it_modules().
"""

from apps.core.russian_it_content import _hw, _lec, _quiz

EXTRA_MODULES = [
{
    "order": 9,
    "title": 'Kiberxavfsizlik (Кибербезопасность)',
    "slug": 'rit-cybersecurity',
    "description": 'Xavfsizlik asoslari, parol/MFA va phishing — ruscha.',
    "lectures": [
            _lec(
                'Основы безопасности',
                'rit-security-basics',
                """
<h2>Lesson goal</h2>
    <p>Объяснять угрозы, уязвимости и базовую гигиену безопасности.</p>

    <h2>Warm-up</h2>
    <p>Что опаснее: слабый пароль или незакрытый сервер?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>кибербезопасность</strong></td><td>защита систем и данных</td><td>Безопасность — задача всех.</td></tr>
<tr><td><strong>угроза</strong></td><td>возможная опасность</td><td>Фишинг — частая угроза.</td></tr>
<tr><td><strong>уязвимость</strong></td><td>слабость, которую используют</td><td>Непропатченное ПО — уязвимость.</td></tr>
<tr><td><strong>атака / breach</strong></td><td>вредоносное действие / проникновение</td><td>Атака привела к breach.</td></tr>
<tr><td><strong>вредонос / malware</strong></td><td>вредное ПО</td><td>Не открывайте malware.</td></tr>
<tr><td><strong>firewall</strong></td><td>фильтр трафика</td><td>Firewall заблокировал скан.</td></tr>
<tr><td><strong>патч</strong></td><td>исправление уязвимости</td><td>Поставьте патч.</td></tr>
<tr><td><strong>риск</strong></td><td>вероятность и ущерб</td><td>Снизим риск.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Сообщите о подозрительной активности.</li>
  <li>Система выглядит уязвимой.</li>
  <li>Поставьте патч сегодня.</li>
  <li>Не отключайте firewall.</li>
  <li>Какой риск, если подождём?</li>
    </ul>

    <h2>Dialogue — непропатченный сервер</h2>
    <p><strong>Sec:</strong> На сервере нет критических патчей.<br><strong>Ops:</strong> Можем сделать окно ночью?<br><strong>Sec:</strong> Да — уязвимость уже эксплуатируют.</p>

    <h2>Grammar focus — Модальности</h2>
    <ul><li>Вы <strong>должны</strong> сообщать о breach.</li><li><strong>Нельзя</strong> игнорировать алерты.</li><li>Вложение <strong>может быть</strong> malware.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Безопасность только у «полиции IT». → ✅ Ответственность общая.</li>
  <li>❌ Уязвимость = только эмоция. → ✅ Слабость системы.</li>
    </ul>

    <h2>Reading — Малые привычки</h2>
    <p>Старое ПО, слабый доступ, спешные клики. Ясный язык помогает действовать спокойно.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Угроза vs уязвимость.</li>
  <li>5 правил must/нельзя.</li>
  <li>Диалог про патч.</li>
    </ol>

    <h2>Quick review</h2>
    <p>угроза · уязвимость · malware · патч · риск</p>
""",
            ),
            _lec(
                'Пароли и MFA',
                'rit-passwords-mfa',
                """
<h2>Lesson goal</h2>
    <p>Говорить о сильных паролях, менеджерах и MFA.</p>

    <h2>Warm-up</h2>
    <p>Пароль 123456 — хороший? Почему нет?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>пароль</strong></td><td>секрет для входа</td><td>Не переиспользуйте пароли.</td></tr>
<tr><td><strong>пассфраза</strong></td><td>длинная фраза</td><td>Пассфраза надёжнее.</td></tr>
<tr><td><strong>менеджер паролей</strong></td><td>хранилище секретов</td><td>Используйте менеджер.</td></tr>
<tr><td><strong>MFA / 2FA</strong></td><td>доп. фактор</td><td>Включите MFA.</td></tr>
<tr><td><strong>OTP</strong></td><td>одноразовый код</td><td>Не сообщайте OTP.</td></tr>
<tr><td><strong>учётные данные</strong></td><td>логин + секрет</td><td>Украденные credentials опасны.</td></tr>
<tr><td><strong>блокировка</strong></td><td>lockout</td><td>Слишком много попыток — lockout.</td></tr>
<tr><td><strong>сброс</strong></td><td>новый пароль</td><td>Пришлю ссылку сброса.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Включите MFA сегодня.</li>
  <li>Никому не диктуйте OTP.</li>
  <li>Сбросим пароль по официальной ссылке.</li>
  <li>Не храните пароли в Excel.</li>
  <li>Используйте менеджер паролей.</li>
    </ul>

    <h2>Dialogue — звонок «из банка»</h2>
    <p><strong>Мошенник:</strong> Назовите код из SMS.<br><strong>Сотрудник:</strong> Я не сообщаю OTP. Перезвоню на официальный номер.</p>

    <h2>Grammar focus — Запреты</h2>
    <ul><li><strong>Нельзя</strong> сообщать OTP.</li><li><strong>Нужно</strong> включить MFA.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ OTP можно сказать «админу» по телефону. → ✅ Сверьте канал.</li>
  <li>❌ Один пароль везде удобно и безопасно. → ✅ Опасно.</li>
    </ul>

    <h2>Reading — MFA спасает</h2>
    <p>Даже при утечке пароля второй фактор часто останавливает вход.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Что такое MFA?</li>
  <li>Почему не делиться OTP?</li>
  <li>Зачем менеджер паролей?</li>
    </ol>

    <h2>Quick review</h2>
    <p>пароль · MFA · OTP · менеджер · credentials</p>
""",
            ),
            _lec(
                'Фишинг и безопасный браузинг',
                'rit-phishing-safe',
                """
<h2>Lesson goal</h2>
    <p>Распознавать фишинг и безопасно открывать ссылки.</p>

    <h2>Warm-up</h2>
    <p>Какие признаки подозрительного письма?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>фишинг</strong></td><td>обман для кражи данных</td><td>Это фишинг.</td></tr>
<tr><td><strong>спуфинг</strong></td><td>подделка адреса/личности</td><td>Поддельный отправитель.</td></tr>
<tr><td><strong>подозрительная ссылка</strong></td><td>опасный URL</td><td>Не кликайте.</td></tr>
<tr><td><strong>вложение</strong></td><td>файл в письме</td><td>Не открывайте странное вложение.</td></tr>
<tr><td><strong>https / замок</strong></td><td>признак шифрования сайта</td><td>Проверьте замок.</td></tr>
<tr><td><strong>сообщить / report</strong></td><td>отправить в Sec</td><td>Зарепортите письмо.</td></tr>
<tr><td><strong>срочность как давление</strong></td><td>манипуляция</td><td>Срочность — красный флаг.</td></tr>
<tr><td><strong>проверка отправителя</strong></td><td>сверка адреса</td><td>Проверьте домен.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Похоже на фишинг — не кликаю.</li>
  <li>Проверьте домен отправителя.</li>
  <li>Зарепортил в Security.</li>
  <li>Ссылка ведёт на другой домен.</li>
  <li>Не вводите пароль по письму.</li>
    </ul>

    <h2>Dialogue — срочное письмо</h2>
    <p><strong>Письмо:</strong> Пароль истечёт через час! Перейдите по ссылке.<br><strong>Сотрудник:</strong> Домен странный. Отправлю в Sec и зайду на сайт вручную.</p>

    <h2>Grammar focus — Если… то…</h2>
    <p>Если письмо требует срочно пароль — <strong>не кликайте</strong>, сообщите в Sec.</p>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Фишинг = апгрейд RAM. → ✅ Обманные сообщения.</li>
  <li>❌ Спуфинг = готовка обеда. → ✅ Подделка личности.</li>
    </ul>

    <h2>Reading — Стоп-кадр перед кликом</h2>
    <p>Домен, тон срочности, запрос секретов, странные вложения — стоп и report.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>3 признака фишинга.</li>
  <li>Что сказать коллеге.</li>
  <li>Куда репортить.</li>
    </ol>

    <h2>Quick review</h2>
    <p>фишинг · спуфинг · OTP · report · домен</p>
""",
            ),
            ],
            "practice": {
            'rit-security-basics': _quiz(
                    'rit-q-vuln',
                    'Уязвимость',
                    'Sec.',
                    'Уязвимость — это…',
                    [
                        'A) слабость, которую можно использовать',
                        'B) сильный пароль',
                        'C) зелёный дашборд',
                        'D) тип монитора',
                    ],
                    'A',
                ),
            'rit-passwords-mfa': _quiz(
                    'rit-q-mfa',
                    'MFA',
                    'Auth.',
                    'MFA значит…',
                    [
                        'A) многофакторная аутентификация',
                        'B) много бесплатных аккаунтов',
                        'C) главный архив файлов',
                        'D) месячная активность вентилятора',
                    ],
                    'A',
                ),
            'rit-phishing-safe': _quiz(
                    'rit-q-phish',
                    'Фишинг',
                    'Safe.',
                    'Фишинг — это…',
                    [
                        'A) поддельные сообщения для кражи данных',
                        'B) апгрейд железа',
                        'C) индекс БД',
                        'D) Scrum-событие',
                    ],
                    'A',
                ),
            },
            "exercises": [
            _quiz(
                'rit-m9-otp',
                'OTP',
                'Auth.',
                'Лучший совет по OTP:',
                [
                    'A) не сообщайте OTP на неожиданных звонках',
                    'B) читайте OTP незнакомцам',
                    'C) публикуйте в Slack',
                    'D) пишите на крышке ноутбука',
                ],
                'A',
            ),
            _quiz(
                'rit-m9-patch',
                'Патч',
                'Sec.',
                'Патч безопасности…',
                [
                    'A) закрывает известную слабость',
                    'B) печатает листовки',
                    'C) удаляет бэкапы ради шутки',
                    'D) отключает все firewall',
                ],
                'A',
                difficulty='medium',
            ),
            ],
            "homework": _hw(
                'Русский язык для IT — Модуль 9\n1) Угроза vs уязвимость.\n2) 8 правил паролей/MFA.\n3) Разбор фишингового письма.\n4) Глоссарий Sec.'
            ),
        },
{
    "order": 10,
    "title": 'QA ва тестлаш (QA и тестирование)',
    "slug": 'rit-qa-testing',
    "description": 'QA rollari, bug report va test turlari — ruscha.',
    "lectures": [
            _lec(
                'Роли QA',
                'rit-qa-roles',
                """
<h2>Lesson goal</h2>
    <p>Описывать задачи QA и взаимодействие с разработкой.</p>

    <h2>Warm-up</h2>
    <p>QA только «ломает» продукт или ещё помогает качеству?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>QA</strong></td><td>обеспечение качества</td><td>QA нашёл регрессию.</td></tr>
<tr><td><strong>тест-кейс</strong></td><td>сценарий проверки</td><td>Напишите тест-кейс.</td></tr>
<tr><td><strong>регрессия</strong></td><td>поломка старого после изменений</td><td>Есть регрессия.</td></tr>
<tr><td><strong>severity</strong></td><td>severity качества</td><td>Ждём sign-off QA.</td></tr>
<tr><td><strong>severityльность</strong></td><td>насколько серьёзно</td><td>Severity high.</td></tr>
<tr><td><strong>приоритет</strong></td><td>очередь исправления</td><td>Priority P1.</td></tr>
<tr><td><strong>smoke test</strong></td><td>быстрая проверка сборки</td><td>Сначала smoke.</td></tr>
<tr><td><strong>окружение теста</strong></td><td>test env</td><td>Баг только на test.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Нужен sign-off перед релизом.</li>
  <li>Это регрессия логина.</li>
  <li>Severity высокая, priority P1.</li>
  <li>Smoke прошёл.</li>
  <li>Воспроизводится на staging.</li>
    </ul>

    <h2>Dialogue — перед релизом</h2>
    <p><strong>PM:</strong> Можно релизить?<br><strong>QA:</strong> После фикса P1 и зелёного smoke — да.<br><strong>PM:</strong> Ок, ждём.</p>

    <h2>Grammar focus — Оценка</h2>
    <ul><li>Severity — влияние.</li><li>Priority — когда чинить.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Регрессия = новый бонус. → ✅ Старое сломалось.</li>
  <li>❌ Sign-off = рисунок. → ✅ Одобрение качества.</li>
    </ul>

    <h2>Reading — QA — партнёр</h2>
    <p>Хороший QA говорит фактами: шаги, ожидание, факт, окружение.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Что делает QA?</li>
  <li>Severity vs priority.</li>
  <li>Зачем smoke?</li>
    </ol>

    <h2>Quick review</h2>
    <p>QA · регрессия · smoke · sign-off · severity</p>
""",
            ),
            _lec(
                'Как писать баг-репорт',
                'rit-bug-report',
                """
<h2>Lesson goal</h2>
    <p>Составлять понятный баг-репорт на русском.</p>

    <h2>Warm-up</h2>
    <p>Какие поля обязательны в баг-репорте?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>заголовок</strong></td><td>краткая суть</td><td>Чёткий title.</td></tr>
<tr><td><strong>шаги воспроизведения</strong></td><td>как повторить</td><td>Steps to reproduce.</td></tr>
<tr><td><strong>ожидаемый результат</strong></td><td>что должно быть</td><td>Expected: …</td></tr>
<tr><td><strong>фактический результат</strong></td><td>что произошло</td><td>Actual: …</td></tr>
<tr><td><strong>окружение</strong></td><td>браузер/ОС/версия</td><td>Chrome, staging.</td></tr>
<tr><td><strong>вложения</strong></td><td>скрин/лог</td><td>Приложите скрин.</td></tr>
<tr><td><strong>воспроизводимость</strong></td><td>всегда/иногда</td><td>Always reproducible.</td></tr>
<tr><td><strong>обходной путь</strong></td><td>workaround</td><td>Есть workaround.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Шаги: 1)… 2)… 3)…</li>
  <li>Ожидали X, получили Y.</li>
  <li>Воспроизводится всегда на staging.</li>
  <li>Логи во вложении.</li>
  <li>Workaround: обновить страницу.</li>
    </ul>

    <h2>Dialogue — плохой vs хороший</h2>
    <p><strong>Плохо:</strong> Не работает.<br><strong>Хорошо:</strong> На staging кнопка «Оплатить» не активна после ввода карты; expected — активна; Chrome 120.</p>

    <h2>Grammar focus — Структура отчёта</h2>
    <ol><li>Title</li><li>Steps</li><li>Expected/Actual</li><li>Env</li></ol>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Баг: «всё плохо». → ✅ Конкретные шаги и факты.</li>
  <li>❌ Без окружения. → ✅ Укажите env.</li>
    </ul>

    <h2>Reading — Ясность = скорость фикса</h2>
    <p>Чем точнее репорт, тем быстрее разработчик попадёт в причину.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Напишите баг-репорт устно.</li>
  <li>Expected vs actual.</li>
  <li>Зачем скрин/лог?</li>
    </ol>

    <h2>Quick review</h2>
    <p>steps · expected · actual · env · workaround</p>
""",
            ),
            _lec(
                'Виды тестирования',
                'rit-test-types',
                """
<h2>Lesson goal</h2>
    <p>Различать unit, integration, e2e и ручное тестирование.</p>

    <h2>Warm-up</h2>
    <p>Можно ли заменить все тесты одним e2e?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>unit-тест</strong></td><td>тест маленькой части кода</td><td>Unit упал.</td></tr>
<tr><td><strong>интеграционный</strong></td><td>тест взаимодействия модулей</td><td>Integration failed.</td></tr>
<tr><td><strong>e2e</strong></td><td>сквозной пользовательский сценарий</td><td>E2E на логин.</td></tr>
<tr><td><strong>ручное тестирование</strong></td><td>проверка человеком</td><td>Нужен exploratory.</td></tr>
<tr><td><strong>автотест</strong></td><td>автоматическая проверка</td><td>Автотесты в CI.</td></tr>
<tr><td><strong>покрытие</strong></td><td>coverage</td><td>Покрытие низкое.</td></tr>
<tr><td><strong>флейки</strong></td><td>нестабильные тесты</td><td>Тест флакает.</td></tr>
<tr><td><strong>тест-данные</strong></td><td>данные для проверки</td><td>Подготовьте test data.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Unit быстрый, e2e медленнее.</li>
  <li>Почините флаки.</li>
  <li>E2E покрывает критический путь.</li>
  <li>Автотесты в CI обязательны.</li>
  <li>Нужны чистые test data.</li>
    </ul>

    <h2>Dialogue — пайрамида</h2>
    <p><strong>Lead:</strong> Почему релиз задержан?<br><strong>QA:</strong> E2E красный на оплате.<br><strong>Lead:</strong> Чиним критический путь, unit уже зелёные.</p>

    <h2>Grammar focus — Сравнение</h2>
    <ul><li>Unit — узко и быстро.</li><li>E2E — широко и дороже.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Unit заменяет CEO. → ✅ Тест куска кода.</li>
  <li>❌ E2E = только один переменный. → ✅ Полный пользовательский поток.</li>
    </ul>

    <h2>Reading — Баланс тестов</h2>
    <p>Много быстрых unit + ключевые e2e. Флаки чинить, не игнорировать.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Unit vs e2e.</li>
  <li>Что такое flaky?</li>
  <li>Зачем test data?</li>
    </ol>

    <h2>Quick review</h2>
    <p>unit · e2e · integration · coverage · flaky</p>
""",
            ),
            ],
            "practice": {
            'rit-qa-roles': _quiz(
                    'rit-q-regression',
                    'Регрессия',
                    'QA.',
                    'Регрессия — это…',
                    [
                        'A) поломка старой функции после изменений',
                        'B) новое растение в офисе',
                        'C) тип роутера',
                        'D) премия',
                    ],
                    'A',
                ),
            'rit-bug-report': _quiz(
                    'rit-q-repro',
                    'Воспроизведение',
                    'Bugs.',
                    'Шаги воспроизведения — это…',
                    [
                        'A) точные действия, чтобы снова увидеть баг',
                        'B) случайные эмодзи',
                        'C) цены серверов',
                        'D) пароли Wi‑Fi',
                    ],
                    'A',
                ),
            'rit-test-types': _quiz(
                    'rit-q-unit',
                    'Unit',
                    'Tests.',
                    'Unit-тест обычно…',
                    [
                        'A) проверяет небольшой фрагмент кода',
                        'B) заменяет CEO',
                        'C) красит офис',
                        'D) покупает регионы cloud',
                    ],
                    'A',
                ),
            },
            "exercises": [
            _quiz(
                'rit-m10-expected',
                'Expected',
                'Bugs.',
                'Ожидаемый результат — это…',
                [
                    'A) что должно произойти',
                    'B) что съел принтер',
                    'C) заказ обеда',
                    'D) всегда случайный краш',
                ],
                'A',
            ),
            _quiz(
                'rit-m10-e2e',
                'E2E',
                'Tests.',
                'E2E-тесты в основном…',
                [
                    'A) проверяют полные пользовательские сценарии',
                    'B) всегда одну переменную',
                    'C) заменяют документацию',
                    'D) случайно перезагружают роутеры',
                ],
                'A',
                difficulty='medium',
            ),
            ],
            "homework": _hw(
                'Русский язык для IT — Модуль 10\n1) Баг-репорт по шаблону.\n2) Severity/priority примеры.\n3) Пирамида тестов.\n4) Глоссарий QA.'
            ),
        },
{
    "order": 11,
    "title": 'Agile ва Scrum',
    "slug": 'rit-agile',
    "description": 'Agile qiymatlari, Scrum voqealari va user story — ruscha.',
    "lectures": [
            _lec(
                'Ценности Agile',
                'rit-agile-values',
                """
<h2>Lesson goal</h2>
    <p>Объяснять итерации, обратную связь и адаптацию.</p>

    <h2>Warm-up</h2>
    <p>Почему IT любит короткие циклы?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>Agile</strong></td><td>гибкий подход к разработке</td><td>Мы работаем по Agile.</td></tr>
<tr><td><strong>итерация</strong></td><td>короткий цикл</td><td>Итерация 2 недели.</td></tr>
<tr><td><strong>бэклог</strong></td><td>упорядоченный список работ</td><td>Бэклог приоритезирован.</td></tr>
<tr><td><strong>инкремент</strong></td><td>готовая добавка ценности</td><td>Инкремент готов.</td></tr>
<tr><td><strong>обратная связь</strong></td><td>feedback</td><td>Нужен feedback клиента.</td></tr>
<tr><td><strong>адаптация</strong></td><td>изменение плана</td><td>Адаптируем план.</td></tr>
<tr><td><strong>кросс-функциональная команда</strong></td><td>разные навыки вместе</td><td>Команда кросс-функциональна.</td></tr>
<tr><td><strong>прозрачность</strong></td><td>видимость работы</td><td>Прозрачность статуса.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Бэклог нужно приоритезировать.</li>
  <li>Доставим инкремент к пятнице.</li>
  <li>Соберём feedback после демо.</li>
  <li>Планы меняем по данным.</li>
  <li>Прозрачность снижает сюрпризы.</li>
    </ul>

    <h2>Dialogue — смена приоритета</h2>
    <p><strong>PO:</strong> Клиент просит фичу X раньше.<br><strong>Team:</strong> Тогда Y уходит из спринта.<br><strong>PO:</strong> Согласен, обновим бэклог.</p>

    <h2>Grammar focus — Мы / давайте</h2>
    <ul><li><strong>Давайте</strong> уточним ценность.</li><li>Мы <strong>адаптируем</strong> план.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Бэклог = сломанный стул. → ✅ Список работ.</li>
  <li>❌ Agile = нет дисциплины. → ✅ Дисциплина коротких циклов.</li>
    </ul>

    <h2>Reading — Гибкость с фокусом</h2>
    <p>Короткие циклы + ясные приоритеты + честный feedback.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Что такое бэклог?</li>
  <li>Зачем итерации?</li>
  <li>Пример смены приоритета.</li>
    </ol>

    <h2>Quick review</h2>
    <p>Agile · бэклог · итерация · feedback · инкремент</p>
""",
            ),
            _lec(
                'События Scrum',
                'rit-scrum-events',
                """
<h2>Lesson goal</h2>
    <p>Называть стендап, планирование, ревью, ретро.</p>

    <h2>Warm-up</h2>
    <p>Стендап — это отчёт боссу или синхронизация команды?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>спринт</strong></td><td>короткий рабочий цикл</td><td>Спринт на 2 недели.</td></tr>
<tr><td><strong>daily / стендап</strong></td><td>короткий синк</td><td>Стендап в 10:00.</td></tr>
<tr><td><strong>планирование</strong></td><td>выбор работ спринта</td><td>Planning завтра.</td></tr>
<tr><td><strong>обзор / review</strong></td><td>демо инкремента</td><td>Sprint review.</td></tr>
<tr><td><strong>ретроспектива</strong></td><td>улучшение процесса</td><td>Ретро в пятницу.</td></tr>
<tr><td><strong>блокер</strong></td><td>то, что мешает</td><td>У меня блокер.</td></tr>
<tr><td><strong>Scrum Master</strong></td><td>помогает процессу</td><td>SM убирает препятствия.</td></tr>
<tr><td><strong>Definition of Done</strong></td><td>критерии готовности</td><td>Не по DoD.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Вчера… Сегодня… Блокеры…</li>
  <li>Нужно вынести в offline.</li>
  <li>Ретро: что улучшить?</li>
  <li>DoD не выполнен — не Done.</li>
  <li>Planning: оценим capacity.</li>
    </ul>

    <h2>Dialogue — стендап</h2>
    <p><strong>Dev:</strong> Вчера закончил API, сегодня тесты, блокер — доступ к staging.<br><strong>SM:</strong> Помогу с доступом после митинга.</p>

    <h2>Grammar focus — Формула стендапа</h2>
    <p>Вчера / Сегодня / Блокеры — коротко.</p>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Ретро = игнор фидбека. → ✅ Улучшение процесса.</li>
  <li>❌ DoD = подсказка пароля. → ✅ Чек-лист готовности.</li>
    </ul>

    <h2>Reading — Ритм Scrum</h2>
    <p>Планируем → делаем → демо → ретро. Стендап держит синхрон.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Формула стендапа.</li>
  <li>Зачем ретро?</li>
  <li>Что такое DoD?</li>
    </ol>

    <h2>Quick review</h2>
    <p>спринт · стендап · ретро · блокер · DoD</p>
""",
            ),
            _lec(
                'User stories',
                'rit-user-stories',
                """
<h2>Lesson goal</h2>
    <p>Писать user story и acceptance criteria на русском.</p>

    <h2>Warm-up</h2>
    <p>Чем story отличается от технической задачи?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>user story</strong></td><td>история ценности для пользователя</td><td>Напишите story.</td></tr>
<tr><td><strong>как… я хочу… чтобы…</strong></td><td>шаблон story</td><td>Как клиент, я хочу…</td></tr>
<tr><td><strong>acceptance criteria</strong></td><td>условия готовности</td><td>AC неполные.</td></tr>
<tr><td><strong>оценка</strong></td><td>estimate</td><td>Оценим в story points.</td></tr>
<tr><td><strong>эпик</strong></td><td>крупная тема</td><td>Эпик «Онбординг».</td></tr>
<tr><td><strong>спайк</strong></td><td>исследование</td><td>Нужен spike.</td></tr>
<tr><td><strong>зависимость</strong></td><td>связь с другой работой</td><td>Есть зависимость.</td></tr>
<tr><td><strong>ценность</strong></td><td>польза</td><td>Какая ценность?</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Как пользователь, я хочу…, чтобы…</li>
  <li>AC: given/when/then.</li>
  <li>Без AC story не готова к разработке.</li>
  <li>Оценим после уточнения.</li>
  <li>Это эпик, разобьём.</li>
    </ul>

    <h2>Dialogue — уточнение story</h2>
    <p><strong>Dev:</strong> В story нет AC на ошибку оплаты.<br><strong>PO:</strong> Добавлю: при отказе банка показать сообщение и сохранить черновик.</p>

    <h2>Grammar focus — Шаблон</h2>
    <p><strong>Как</strong> …, <strong>я хочу</strong> …, <strong>чтобы</strong> …</p>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Story: «Сделать кнопку сейчас!» → ✅ Роль + цель + ценность.</li>
  <li>❌ AC = пароль офиса. → ✅ Условия Done.</li>
    </ul>

    <h2>Reading — Истории о людях</h2>
    <p>Хорошая story говорит о пользователе, а не только о таблице в БД.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Напишите story.</li>
  <li>3 AC для логина.</li>
  <li>Эпик vs story.</li>
    </ol>

    <h2>Quick review</h2>
    <p>user story · AC · эпик · оценка · ценность</p>
""",
            ),
            ],
            "practice": {
            'rit-agile-values': _quiz(
                    'rit-q-backlog',
                    'Бэклог',
                    'Agile.',
                    'Бэклог — это…',
                    [
                        'A) упорядоченный список работ',
                        'B) сломанный стул',
                        'C) malware',
                        'D) только cloud-счёт',
                    ],
                    'A',
                ),
            'rit-scrum-events': _quiz(
                    'rit-q-standup',
                    'Стендап',
                    'Scrum.',
                    'Daily в основном для…',
                    [
                        'A) короткого синка и блокеров',
                        'B) тайной переписки roadmap',
                        'C) только обеда',
                        'D) удаления репозиториев',
                    ],
                    'A',
                ),
            'rit-user-stories': _quiz(
                    'rit-q-ac',
                    'AC',
                    'Stories.',
                    'Acceptance criteria определяют…',
                    [
                        'A) условия, когда работа считается сделанной',
                        'B) пароль Wi‑Fi',
                        'C) температуру CPU',
                        'D) только даты отпуска',
                    ],
                    'A',
                ),
            },
            "exercises": [
            _quiz(
                'rit-m11-story',
                'Story',
                'Agile.',
                'Лучшая форма story:',
                [
                    'A) Как пользователь, я хочу…, чтобы…',
                    'B) Кнопку сделай сейчас!',
                    'C) Код вечно без цели.',
                    'D) Сервер удали ASAP.',
                ],
                'A',
            ),
            _quiz(
                'rit-m11-dod',
                'DoD',
                'Scrum.',
                'Definition of Done — это…',
                [
                    'A) чек-лист качества готовой работы',
                    'B) подсказка пароля',
                    'C) бренд монитора',
                    'D) меню обеда',
                ],
                'A',
                difficulty='medium',
            ),
            ],
            "homework": _hw(
                'Русский язык для IT — Модуль 11\n1) 5 принципов Agile своими словами.\n2) Стендап-скрипт.\n3) 3 user stories + AC.\n4) Глоссарий Scrum.'
            ),
        },
{
    "order": 12,
    "title": 'Texnik yordam (Техподдержка)',
    "slug": 'rit-tech-support',
    "description": 'Ticket tili, troubleshooting va escalate — ruscha.',
    "lectures": [
            _lec(
                'Язык тикетов',
                'rit-ticket-intake',
                """
<h2>Lesson goal</h2>
    <p>Вежливо принимать заявку и фиксировать факты.</p>

    <h2>Warm-up</h2>
    <p>Что спросить у пользователя в первые 30 секунд?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>заявка / тикет</strong></td><td>обращение</td><td>Создайте тикет.</td></tr>
<tr><td><strong>влияние</strong></td><td>impact</td><td>Какое влияние на бизнес?</td></tr>
<tr><td><strong>срочность</strong></td><td>urgency</td><td>Насколько срочно?</td></tr>
<tr><td><strong>SLA</strong></td><td>целевые сроки сервиса</td><td>В рамках SLA.</td></tr>
<tr><td><strong>приоритет</strong></td><td>очередь</td><td>Поставим P2.</td></tr>
<tr><td><strong>канал связи</strong></td><td>email/чат/телефон</td><td>Ответим в тикете.</td></tr>
<tr><td><strong>подтверждение</strong></td><td>ack</td><td>Подтверждаю получение.</td></tr>
<tr><td><strong>ETA</strong></td><td>оценка времени</td><td>ETA — 30 минут.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Подтверждаю получение заявки.</li>
  <li>Уточните влияние: один пользователь или все?</li>
  <li>Работаем в рамках SLA.</li>
  <li>ETA около часа.</li>
  <li>Держите тикет открытым для апдейтов.</li>
    </ul>

    <h2>Dialogue — приём заявки</h2>
    <p><strong>Юзер:</strong> Почта не работает!<br><strong>Support:</strong> Понял. Это только у вас или у команды? Когда началось?<br><strong>Юзер:</strong> У всего отдела с 10:00.</p>

    <h2>Grammar focus — Вежливые уточнения</h2>
    <p>Подскажите, пожалуйста… / Уточните… / Правильно ли я понял, что…</p>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ SLA = тип GPU. → ✅ Цели сервиса.</li>
  <li>❌ ETA = eat the apples. → ✅ Оценка времени.</li>
    </ul>

    <h2>Reading — Факты снимают панику</h2>
    <p>Кто затронут, с какого времени, что уже пробовали.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Скрипт приёма тикета.</li>
  <li>Impact vs urgency.</li>
  <li>Что такое SLA?</li>
    </ol>

    <h2>Quick review</h2>
    <p>тикет · SLA · impact · ETA · приоритет</p>
""",
            ),
            _lec(
                'Шаги диагностики',
                'rit-troubleshoot-steps',
                """
<h2>Lesson goal</h2>
    <p>Вести пользователя по чек-листу troubleshooting.</p>

    <h2>Warm-up</h2>
    <p>Почему важно воспроизвести проблему?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>воспроизвести</strong></td><td>повторить проблему</td><td>Можете воспроизвести?</td></tr>
<tr><td><strong>корневая причина</strong></td><td>root cause</td><td>Ищем root cause.</td></tr>
<tr><td><strong>симптом</strong></td><td>внешнее проявление</td><td>Симптом — ошибка 500.</td></tr>
<tr><td><strong>гипотеза</strong></td><td>предположение</td><td>Гипотеза: DNS.</td></tr>
<tr><td><strong>обходной путь</strong></td><td>workaround</td><td>Временный workaround.</td></tr>
<tr><td><strong>логи / скрин</strong></td><td>доказательства</td><td>Пришлите логи.</td></tr>
<tr><td><strong>изолировать</strong></td><td>сузить область</td><td>Изолируем сервис.</td></tr>
<tr><td><strong>решить / resolve</strong></td><td>закрыть проблему</td><td>Тикет resolved.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Давайте воспроизведём вместе.</li>
  <li>Временный workaround: …</li>
  <li>Пришлите скрин ошибки.</li>
  <li>Гипотеза подтвердилась.</li>
  <li>Корневая причина — сертификат.</li>
    </ul>

    <h2>Dialogue — диагностика</h2>
    <p><strong>Support:</strong> Ошибка на всех браузерах?<br><strong>Юзер:</strong> Только Chrome.<br><strong>Support:</strong> Очистите кэш; если не поможет — проверим расширение.</p>

    <h2>Grammar focus — Сначала / если не поможет</h2>
    <p>Сначала A. Если не поможет — B. Затем эскалация.</p>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Root cause = дерево. → ✅ Глубинная причина.</li>
  <li>❌ Workaround = удалить Землю. → ✅ Временная помощь.</li>
    </ul>

    <h2>Reading — Метод узких кругов</h2>
    <p>Симптом → воспроизведение → гипотезы → проверка → фикс/эскалация.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Чек-лист 5 шагов.</li>
  <li>Симптом vs причина.</li>
  <li>Когда давать workaround?</li>
    </ol>

    <h2>Quick review</h2>
    <p>reproduce · root cause · workaround · resolve</p>
""",
            ),
            _lec(
                'Эскалация',
                'rit-escalate',
                """
<h2>Lesson goal</h2>
    <p>Эскалировать чисто: факты, влияние, что уже сделано.</p>

    <h2>Warm-up</h2>
    <p>Когда эскалировать, а когда ещё пробовать самому?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>эскалация</strong></td><td>передача на уровень выше</td><td>Эскалируем на L2.</td></tr>
<tr><td><strong>handover</strong></td><td>передача контекста</td><td>Чистый handover.</td></tr>
<tr><td><strong>L1 / L2 / L3</strong></td><td>уровни поддержки</td><td>Нужен L3.</td></tr>
<tr><td><strong>владелец сервиса</strong></td><td>service owner</td><td>Тэгните owner.</td></tr>
<tr><td><strong>критичность</strong></td><td>насколько серьёзно</td><td>Критичность высокая.</td></tr>
<tr><td><strong>окно работ</strong></td><td>maintenance window</td><td>Нужно окно.</td></tr>
<tr><td><strong>статус для клиента</strong></td><td>update</td><td>Отправим статус.</td></tr>
<tr><td><strong>ответственность</strong></td><td>ownership</td><td>Кто owner дальше?</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Эскалирую с логами и шагами.</li>
  <li>Влияние: 200 пользователей.</li>
  <li>Уже пробовали A/B/C.</li>
  <li>Нужен L2 networking.</li>
  <li>Клиенту отправили временный статус.</li>
    </ul>

    <h2>Dialogue — handover</h2>
    <p><strong>L1:</strong> Эскалирую: VPN падает у филиала, 50 человек, reboot не помог, логи во вложении.<br><strong>L2:</strong> Принял, ETA 20 минут.</p>

    <h2>Grammar focus — Структура эскалации</h2>
    <ol><li>Суть</li><li>Влияние</li><li>Шаги</li><li>Доказательства</li><li>Просьба</li></ol>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Escalate = удалить тикет. → ✅ Передать выше.</li>
  <li>❌ Handover = только HELP. → ✅ Контекст и факты.</li>
    </ul>

    <h2>Reading — Уважение ко времени L2</h2>
    <p>Плохая эскалация без фактов замедляет всех.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Составьте handover.</li>
  <li>L1 vs L2.</li>
  <li>Что писать клиенту при эскалации?</li>
    </ol>

    <h2>Quick review</h2>
    <p>escalate · handover · L2 · impact · ownership</p>
""",
            ),
            ],
            "practice": {
            'rit-ticket-intake': _quiz(
                    'rit-q-sla',
                    'SLA',
                    'Support.',
                    'SLA связан с…',
                    [
                        'A) целями сервиса, например временем ответа',
                        'B) типом GPU',
                        'C) Scrum-перекусом',
                        'D) CSS-фреймворком',
                    ],
                    'A',
                ),
            'rit-troubleshoot-steps': _quiz(
                    'rit-q-root',
                    'Root cause',
                    'Debug.',
                    'Корневая причина — это…',
                    [
                        'A) основная причина проблемы',
                        'B) дерево в саду',
                        'C) случайная перезагрузка',
                        'D) новый эмодзи',
                    ],
                    'A',
                ),
            'rit-escalate': _quiz(
                    'rit-q-escalate',
                    'Эскалация',
                    'Support.',
                    'Эскалировать значит…',
                    [
                        'A) передать вопрос на более высокий/спец. уровень',
                        'B) удалить тикет навсегда',
                        'C) игнорировать пользователя',
                        'D) выключить мониторинг',
                    ],
                    'A',
                ),
            },
            "exercises": [
            _quiz(
                'rit-m12-workaround',
                'Workaround',
                'Support.',
                'Workaround — это…',
                [
                    'A) временный способ снизить влияние',
                    'B) финальное удаление Земли',
                    'C) фишинг',
                    'D) имя региона cloud',
                ],
                'A',
            ),
            _quiz(
                'rit-m12-eta',
                'ETA',
                'Support.',
                'ETA обычно значит…',
                [
                    'A) оценка времени решения/прибытия',
                    'B) eat the apples',
                    'C) empty the archive',
                    'D) extra test always',
                ],
                'A',
                difficulty='medium',
            ),
            ],
            "homework": _hw(
                'Русский язык для IT — Модуль 12\n1) Шаблон приёма тикета.\n2) Чек-лист troubleshooting.\n3) Handover L2.\n4) Глоссарий support.'
            ),
        },
{
    "order": 13,
    "title": 'Hujjatlar (Документация)',
    "slug": 'rit-documentation',
    "description": 'README/spec, user guide va changelog — ruscha.',
    "lectures": [
            _lec(
                'README и спецификации',
                'rit-readme-spec',
                """
<h2>Lesson goal</h2>
    <p>Писать README и коротко объяснять spec.</p>

    <h2>Warm-up</h2>
    <p>Что должно быть в README за 2 минуты чтения?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>README</strong></td><td>входной документ проекта</td><td>Обновите README.</td></tr>
<tr><td><strong>спецификация / spec</strong></td><td>требования/дизайн</td><td>Читайте spec.</td></tr>
<tr><td><strong>предварительные требования</strong></td><td>prerequisites</td><td>Укажите prerequisites.</td></tr>
<tr><td><strong>быстрый старт</strong></td><td>quick start</td><td>Добавьте quick start.</td></tr>
<tr><td><strong>репозиторий</strong></td><td>код проекта</td><td>Клонируйте репо.</td></tr>
<tr><td><strong>конфигурация</strong></td><td>настройки</td><td>Пример config.</td></tr>
<tr><td><strong>ответственный</strong></td><td>maintainer</td><td>Контакты maintainers.</td></tr>
<tr><td><strong>лицензия проекта</strong></td><td>условия использования</td><td>См. LICENSE.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>В README: установка за 5 шагов.</li>
  <li>Укажите prerequisites.</li>
  <li>Spec описывает поведение API.</li>
  <li>Пример конфига обязателен.</li>
  <li>Кто maintainer?</li>
    </ul>

    <h2>Dialogue — онбординг</h2>
    <p><strong>Новичок:</strong> Как запустить проект?<br><strong>Коллега:</strong> README → prerequisites → quick start. Если упрётесь — пишите в канал.</p>

    <h2>Grammar focus — Императив для инструкций</h2>
    <ul><li><strong>Установите</strong>…</li><li><strong>Скопируйте</strong> .env.example</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ README = рецепт пасты. → ✅ Как понять и запустить проект.</li>
  <li>❌ Spec = очки. → ✅ Детальные требования.</li>
    </ul>

    <h2>Reading — Документ = продукт</h2>
    <p>Хороший README экономит часы онбординга.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Структура README.</li>
  <li>Prerequisites для вашего проекта.</li>
  <li>Spec vs README.</li>
    </ol>

    <h2>Quick review</h2>
    <p>README · spec · quick start · prerequisites</p>
""",
            ),
            _lec(
                'Руководства пользователя',
                'rit-user-guide',
                """
<h2>Lesson goal</h2>
    <p>Писать понятные user guides простым языком.</p>

    <h2>Warm-up</h2>
    <p>Чем руководство отличается от внутреннего tech note?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>руководство</strong></td><td>инструкция для пользователя</td><td>См. user guide.</td></tr>
<tr><td><strong>простой язык</strong></td><td>ясные формулировки</td><td>Пишите просто.</td></tr>
<tr><td><strong>предупреждение</strong></td><td>warning</td><td>Добавьте предупреждение.</td></tr>
<tr><td><strong>скриншот</strong></td><td>снимок экрана</td><td>Нужен скрин.</td></tr>
<tr><td><strong>шаг за шагом</strong></td><td>пошагово</td><td>Опишите по шагам.</td></tr>
<tr><td><strong>аудитория</strong></td><td>для кого текст</td><td>Аудитория — менеджеры.</td></tr>
<tr><td><strong>FAQ</strong></td><td>частые вопросы</td><td>Добавьте FAQ.</td></tr>
<tr><td><strong>доступность</strong></td><td>понятность/a11y</td><td>Учтите доступность.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Не используйте лишний жаргон.</li>
  <li>Предупреждение: не удаляйте…</li>
  <li>Шаг 1… Шаг 2…</li>
  <li>Скрин устарел — обновите.</li>
  <li>FAQ закрывает 80% вопросов.</li>
    </ul>

    <h2>Dialogue — ревью гайда</h2>
    <p><strong>Writer:</strong> Можно «инициализировать модуль»?<br><strong>Editor:</strong> Для пользователей лучше: «Откройте раздел и нажмите Создать».</p>

    <h2>Grammar focus — Предупреждения</h2>
    <p><strong>Важно:</strong>… / <strong>Внимание:</strong>… / <strong>Примечание:</strong>…</p>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Plain language = только латынь. → ✅ Ясные слова для аудитории.</li>
  <li>❌ Warning как шутка. → ✅ Чёткий риск.</li>
    </ul>

    <h2>Reading — Пишите для читателя</h2>
    <p>Одна цель на раздел, короткие шаги, актуальные скрины.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Перепишите жаргонную фразу.</li>
  <li>Структура FAQ.</li>
  <li>Когда нужен warning?</li>
    </ol>

    <h2>Quick review</h2>
    <p>user guide · plain language · FAQ · warning</p>
""",
            ),
            _lec(
                'Changelog',
                'rit-change-log',
                """
<h2>Lesson goal</h2>
    <p>Вести changelog и объяснять breaking changes.</p>

    <h2>Warm-up</h2>
    <p>Зачем писать changelog, если есть коммиты?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>changelog</strong></td><td>список изменений по версиям</td><td>См. CHANGELOG.</td></tr>
<tr><td><strong>версия</strong></td><td>version</td><td>Версия 2.1.0.</td></tr>
<tr><td><strong>breaking change</strong></td><td>ломающее изменение</td><td>Есть breaking change.</td></tr>
<tr><td><strong>deprecate</strong></td><td>пометить устаревшим</td><td>Endpoint deprecated.</td></tr>
<tr><td><strong>миграция для клиентов</strong></td><td>как адаптироваться</td><td>Гайд миграции.</td></tr>
<tr><td><strong>исправления</strong></td><td>fixes</td><td>Fixes: …</td></tr>
<tr><td><strong>новое</strong></td><td>features</td><td>Added: …</td></tr>
<tr><td><strong>безопасность</strong></td><td>security notes</td><td>Security: …</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>В 2.1.0: Added… Fixed…</li>
  <li>Breaking: поле rename.</li>
  <li>Старый метод deprecated до 3.0.</li>
  <li>Посмотрите migration guide.</li>
  <li>Security patch обязателен.</li>
    </ul>

    <h2>Dialogue — релизные заметки</h2>
    <p><strong>PM:</strong> Что сказать клиентам?<br><strong>Tech writer:</strong> В changelog: новые фильтры, фикс экспорта, breaking — новый обязательный заголовок API.</p>

    <h2>Grammar focus — Категории</h2>
    <ul><li>Added / Changed / Fixed / Security / Deprecated</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Breaking = обеденный перерыв. → ✅ Ломает интеграции.</li>
  <li>❌ Deprecate = сделать вечным тайно. → ✅ Пометить к удалению.</li>
    </ul>

    <h2>Reading — Честность релиза</h2>
    <p>Клиенты ценят ясный breaking change больше, чем сюрприз в prod.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Запись changelog на версию.</li>
  <li>Как объявить deprecate?</li>
  <li>Зачем migration guide?</li>
    </ol>

    <h2>Quick review</h2>
    <p>changelog · breaking · deprecate · version · security</p>
""",
            ),
            ],
            "practice": {
            'rit-readme-spec': _quiz(
                    'rit-q-readme',
                    'README',
                    'Docs.',
                    'README в основном помогает…',
                    [
                        'A) быстро понять и запустить проект',
                        'B) готовить пасту',
                        'C) дизайнить растения',
                        'D) удалять prod вслепую',
                    ],
                    'A',
                ),
            'rit-user-guide': _quiz(
                    'rit-q-plain',
                    'Plain language',
                    'Docs.',
                    'Простой язык значит…',
                    [
                        'A) ясные формулировки для аудитории',
                        'B) только латинская поэзия',
                        'C) скрывать предупреждения',
                        'D) убрать все скрины',
                    ],
                    'A',
                ),
            'rit-change-log': _quiz(
                    'rit-q-breaking',
                    'Breaking',
                    'Docs.',
                    'Breaking change…',
                    [
                        'A) может сломать существующие интеграции',
                        'B) всегда ничего не чинит',
                        'C) обеденный перерыв',
                        'D) тип монитора',
                    ],
                    'A',
                ),
            },
            "exercises": [
            _quiz(
                'rit-m13-deprecate',
                'Deprecate',
                'Docs.',
                'Deprecate значит…',
                [
                    'A) пометить как устаревшее к будущему удалению',
                    'B) сделать вечным тайно',
                    'C) шифровать меню обеда',
                    'D) перезагрузить здание',
                ],
                'A',
            ),
            _quiz(
                'rit-m13-prereq',
                'Prerequisite',
                'Docs.',
                'Prerequisite — это…',
                [
                    'A) то, что нужно до начала',
                    'B) случайный мем',
                    'C) всегда сломанный кабель',
                    'D) скидка cloud',
                ],
                'A',
                difficulty='medium',
            ),
            ],
            "homework": _hw(
                'Русский язык для IT — Модуль 13\n1) README для учебного проекта.\n2) User guide на 1 фичу.\n3) Changelog на версию.\n4) Глоссарий docs.'
            ),
        },
{
    "order": 14,
    "title": 'Jamoa aloqasi (Командная коммуникация)',
    "slug": 'rit-team-comms',
    "description": 'Standup, Slack/Teams va muloyim feedback — ruscha.',
    "lectures": [
            _lec(
                'Русский для стендапа',
                'rit-standup-russian',
                """
<h2>Lesson goal</h2>
    <p>Коротко и ясно говорить апдейт на стендапе.</p>

    <h2>Warm-up</h2>
    <p>Как уложить апдейт в 30–40 секунд?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>апдейт</strong></td><td>краткий статус</td><td>Мой апдейт: …</td></tr>
<tr><td><strong>блокер</strong></td><td>препятствие</td><td>Блокер — доступ.</td></tr>
<tr><td><strong>вчера / сегодня</strong></td><td>рамка стендапа</td><td>Вчера… Сегодня…</td></tr>
<tr><td><strong>помощь</strong></td><td>запрос поддержки</td><td>Нужна помощь с…</td></tr>
<tr><td><strong>офлайн</strong></td><td>обсудить отдельно</td><td>Вынесем офлайн.</td></tr>
<tr><td><strong>зависимость</strong></td><td>ожидание другого</td><td>Зависимость от API.</td></tr>
<tr><td><strong>прогресс</strong></td><td>движение вперёд</td><td>Есть прогресс.</td></tr>
<tr><td><strong>риск</strong></td><td>возможная проблема</td><td>Риск сорвать дедлайн.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Вчера закончил X. Сегодня Y. Блокеров нет.</li>
  <li>Нужна помощь с доступом.</li>
  <li>Давайте вынесем в офлайн.</li>
  <li>Есть риск по сроку.</li>
  <li>Зависимость от команды payments.</li>
    </ul>

    <h2>Dialogue — длинный апдейт</h2>
    <p><strong>SM:</strong> Коротко, пожалуйста.<br><strong>Dev:</strong> Вчера — PR логина, сегодня — тесты, блокер — review от QA.</p>

    <h2>Grammar focus — Три части</h2>
    <p>Факт → план → просьба/блокер.</p>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Блокер = наушники. → ✅ То, что мешает работе.</li>
  <li>❌ Offline = выключить интернет навсегда. → ✅ Обсудить отдельно.</li>
    </ul>

    <h2>Reading — Уважение ко времени</h2>
    <p>Стендап — синк, не глубокий дизайн.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Ваш апдейт 30 сек.</li>
  <li>Как назвать блокер?</li>
  <li>Когда говорить «офлайн»?</li>
    </ol>

    <h2>Quick review</h2>
    <p>апдейт · блокер · офлайн · риск · зависимость</p>
""",
            ),
            _lec(
                'Чат Slack/Teams',
                'rit-slack-teams',
                """
<h2>Lesson goal</h2>
    <p>Писать в рабочих чатах без шума и двусмысленности.</p>

    <h2>Warm-up</h2>
    <p>Когда писать в канал, а когда в thread?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>тред / thread</strong></td><td>ветка обсуждения</td><td>Ответьте в треде.</td></tr>
<tr><td><strong>@channel / @here</strong></td><td>широкое упоминание</td><td>Не злоупотребляйте @channel.</td></tr>
<tr><td><strong>FYI</strong></td><td>для информации</td><td>FYI: релиз в 18:00.</td></tr>
<tr><td><strong>ASK / HELP</strong></td><td>метка просьбы</td><td>ASK: нужен ревью.</td></tr>
<tr><td><strong>дедлайн в чате</strong></td><td>срок ответа</td><td>Нужен ответ до 15:00.</td></tr>
<tr><td><strong>ссылка на тикет/PR</strong></td><td>контекст</td><td>Ссылка на PR.</td></tr>
<tr><td><strong>статус реакции</strong></td><td>emoji-ack</td><td>Поставьте ✅ если ок.</td></tr>
<tr><td><strong>шум</strong></td><td>лишние сообщения</td><td>Снизим шум в канале.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Отвечаю в треде.</li>
  <li>FYI без действия.</li>
  <li>ASK: ревью до 16:00.</li>
  <li>Не @channel для мелочей.</li>
  <li>Вот ссылка на тикет.</li>
    </ul>

    <h2>Dialogue — шумный канал</h2>
    <p><strong>Lead:</strong> Перенесите обсуждение бага в тред и приложите логи.<br><strong>Dev:</strong> Сделал, тред здесь.</p>

    <h2>Grammar focus — Ясная просьба</h2>
    <p>Контекст → просьба → срок → ссылка.</p>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Thread удаляет канал. → ✅ Организует ответы.</li>
  <li>❌ FYI = fix your internet. → ✅ For your information.</li>
    </ul>

    <h2>Reading — Чат = рабочий инструмент</h2>
    <p>Короткие сообщения с контекстом бьют длинные романы без ссылок.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Напишите ASK-сообщение.</li>
  <li>Когда @channel уместен?</li>
  <li>Что такое FYI?</li>
    </ol>

    <h2>Quick review</h2>
    <p>тред · FYI · ASK · @channel · дедлайн</p>
""",
            ),
            _lec(
                'Вежливый фидбек',
                'rit-feedback-polite',
                """
<h2>Lesson goal</h2>
    <p>Давать и принимать фидбек в ревью и 1:1.</p>

    <h2>Warm-up</h2>
    <p>Как критиковать код, не критикуя человека?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>фидбек</strong></td><td>обратная связь</td><td>Дайте фидбек.</td></tr>
<tr><td><strong>смягчение</strong></td><td>вежливая форма</td><td>Можем ли переименовать…?</td></tr>
<tr><td><strong>nit</strong></td><td>мелочь</td><td>Nit: пробел.</td></tr>
<tr><td><strong>blocking</strong></td><td>обязательно исправить</td><td>Blocking: утечка секрета.</td></tr>
<tr><td><strong>предложение</strong></td><td>suggestion</td><td>Suggestion: вынести в функцию.</td></tr>
<tr><td><strong>признание</strong></td><td>что хорошо</td><td>Отличная обработка ошибок.</td></tr>
<tr><td><strong>1:1</strong></td><td>личная встреча</td><td>Обсудим на 1:1.</td></tr>
<tr><td><strong>рост</strong></td><td>развитие</td><td>Зона роста: оценки сроков.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Можем ли переименовать функцию?</li>
  <li>Blocking: не коммитьте секреты.</li>
  <li>Nit: форматирование.</li>
  <li>Мне нравится структура модулей.</li>
  <li>Приму фидбек и поправлю.</li>
    </ul>

    <h2>Dialogue — ревью</h2>
    <p><strong>Ревьюер:</strong> Blocking: ключ в коде. Suggestion: вынести в env.<br><strong>Автор:</strong> Спасибо, уберу ключ и обновлю README.</p>

    <h2>Grammar focus — Вежливые формы</h2>
    <ul><li>Можем ли…?</li><li>Предлагаю…</li><li>Как насчёт…?</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ «Код мусор». → ✅ Конкретное blocking/suggestion.</li>
  <li>❌ Nit = авария. → ✅ Мелкая необязательная заметка.</li>
    </ul>

    <h2>Reading — Фидбек про работу</h2>
    <p>Хвалите конкретно, критикуйте поведение/код, предлагайте шаг.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Перепишите грубый комментарий.</li>
  <li>Nit vs blocking.</li>
  <li>Как принять фидбек?</li>
    </ol>

    <h2>Quick review</h2>
    <p>фидбек · nit · blocking · suggestion · 1:1</p>
""",
            ),
            ],
            "practice": {
            'rit-standup-russian': _quiz(
                    'rit-q-blocker-chat',
                    'Блокер',
                    'Comms.',
                    'На стендапе блокер — это…',
                    [
                        'A) то, что мешает прогрессу',
                        'B) тип наушников',
                        'C) скидка cloud',
                        'D) глагол changelog',
                    ],
                    'A',
                ),
            'rit-slack-teams': _quiz(
                    'rit-q-thread',
                    'Тред',
                    'Chat.',
                    'Тред помогает…',
                    [
                        'A) держать ответы по одной теме',
                        'B) удалить канал',
                        'C) скрыть решения навсегда',
                        'D) обойти безопасность',
                    ],
                    'A',
                ),
            'rit-feedback-polite': _quiz(
                    'rit-q-nit',
                    'Nit',
                    'Review.',
                    'Nit обычно значит…',
                    [
                        'A) мелкая необязательная заметка',
                        'B) критический сбой',
                        'C) правило firewall',
                        'D) отмена спринта',
                    ],
                    'A',
                ),
            },
            "exercises": [
            _quiz(
                'rit-m14-soft',
                'Смягчение',
                'Feedback.',
                'Самая вежливая просьба:',
                [
                    'A) Можем ли переименовать эту функцию?',
                    'B) Переименуй сейчас, идиот.',
                    'C) Твой код мусор.',
                    'D) Фикси или уходи.',
                ],
                'A',
            ),
            _quiz(
                'rit-m14-fyi',
                'FYI',
                'Chat.',
                'FYI в чате обычно значит…',
                [
                    'A) для вашего сведения',
                    'B) fix your internet',
                    'C) find your intern',
                    'D) free yellow ink',
                ],
                'A',
                difficulty='medium',
            ),
            ],
            "homework": _hw(
                'Русский язык для IT — Модуль 14\n1) 5 стендап-апдейтов.\n2) Шаблоны сообщений ASK/FYI.\n3) 5 вежливых review-комментов.\n4) Глоссарий comms.'
            ),
        },
{
    "order": 15,
    "title": 'Email va karyera (Email и карьера)',
    "slug": 'rit-career-email',
    "description": 'Email shablonlari, intervyu asoslari va LinkedIn/CV — ruscha.',
    "lectures": [
            _lec(
                'Шаблоны email',
                'rit-email-templates',
                """
<h2>Lesson goal</h2>
    <p>Писать деловые письма: тема, просьба, follow-up.</p>

    <h2>Warm-up</h2>
    <p>Почему тема письма важнее первого предложения?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>тема письма</strong></td><td>subject</td><td>Тема должна быть ясной.</td></tr>
<tr><td><strong>обращение</strong></td><td>приветствие</td><td>Здравствуйте, …</td></tr>
<tr><td><strong>просьба</strong></td><td>request</td><td>Прошу согласовать…</td></tr>
<tr><td><strong>срок</strong></td><td>deadline в письме</td><td>До пятницы.</td></tr>
<tr><td><strong>вложение</strong></td><td>attachment</td><td>Во вложении файл.</td></tr>
<tr><td><strong>follow-up</strong></td><td>повторное письмо</td><td>Пишу follow-up.</td></tr>
<tr><td><strong>копия / CC</strong></td><td>уведомить других</td><td>В копии менеджер.</td></tr>
<tr><td><strong>подпись</strong></td><td>signature</td><td>Добавьте подпись.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Тема: Доступ к staging — срочно до 15:00.</li>
  <li>Здравствуйте, прошу…</li>
  <li>Во вложении лог.</li>
  <li>Буду благодарен за ответ до…</li>
  <li>Направляю follow-up по вчерашней просьбе.</li>
    </ul>

    <h2>Dialogue — короткое письмо</h2>
    <p><strong>Тема:</strong> Ревью PR #241 до 16:00<br>Здравствуйте, Иван! Прошу посмотреть PR #241 (ссылка). Нужен merge сегодня. Спасибо!</p>

    <h2>Grammar focus — Структура</h2>
    <p>Тема → приветствие → контекст → просьба+срок → спасибо → подпись.</p>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Тема: «Привет». → ✅ Ясная тема и срочность.</li>
  <li>❌ Follow-up = malware. → ✅ Вежливое напоминание.</li>
    </ul>

    <h2>Reading — Письмо уважает время</h2>
    <p>Одна просьба на письмо, явный срок, ссылки вместо простыней.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Напишите просьбу о доступе.</li>
  <li>Follow-up на 3 предложения.</li>
  <li>Хорошая тема vs плохая.</li>
    </ol>

    <h2>Quick review</h2>
    <p>subject · просьба · follow-up · вложение · CC</p>
""",
            ),
            _lec(
                'IT-интервью: база',
                'rit-interview-it',
                """
<h2>Lesson goal</h2>
    <p>Готовить самопрезентацию и ответы о опыте (база до модуля 17).</p>

    <h2>Warm-up</h2>
    <p>Как уложить «расскажите о себе» в 60 секунд?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>самопрезентация</strong></td><td>pitch о себе</td><td>Короткий pitch.</td></tr>
<tr><td><strong>опыт</strong></td><td>experience</td><td>Опыт с Python 2 года.</td></tr>
<tr><td><strong>достижение</strong></td><td>результат</td><td>Снизил ошибки на 20%.</td></tr>
<tr><td><strong>мотивация</strong></td><td>почему роль</td><td>Хочу расти в backend.</td></tr>
<tr><td><strong>вопрос кандидату</strong></td><td>ваш вопрос</td><td>Как устроен онбординг?</td></tr>
<tr><td><strong>сильная сторона</strong></td><td>strength</td><td>Сильная сторона — отладка.</td></tr>
<tr><td><strong>зона роста</strong></td><td>weakness конструктивно</td><td>Улучшаю оценку сроков.</td></tr>
<tr><td><strong>пример</strong></td><td>конкретика</td><td>Приведу пример из проекта.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Я работал с… Результат: …</li>
  <li>В этой роли хочу…</li>
  <li>Сильная сторона — … Пример: …</li>
  <li>Вопрос: как выглядит первый спринт?</li>
  <li>Готов обсудить тестовое.</li>
    </ul>

    <h2>Dialogue — скрининг</h2>
    <p><strong>HR:</strong> Расскажите о себе.<br><strong>Кандидат:</strong> Я backend-разработчик, 2 года Python/Django, делал API платежей, снизил latency на 15%. Ищу роль с фокусом на надёжность.</p>

    <h2>Grammar focus — Настоящее совершенное для опыта</h2>
    <ul><li>Я <strong>работал</strong> с Git два года.</li><li>Я <strong>участвовал</strong> в on-call.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ «Я очень-очень крутой». → ✅ Роль + стек + результат.</li>
  <li>❌ Нет вопросов к компании. → ✅ 2–3 умных вопроса.</li>
    </ul>

    <h2>Reading — Конкретика побеждает клише</h2>
    <p>Цифры, стек, ответственность — лучше общих слов «ответственный».</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Pitch 60 сек.</li>
  <li>Сильная сторона + пример.</li>
  <li>3 вопроса работодателю.</li>
    </ol>

    <h2>Quick review</h2>
    <p>pitch · опыт · достижение · мотивация · зона роста</p>
""",
            ),
            _lec(
                'LinkedIn и CV',
                'rit-linkedin-cv',
                """
<h2>Lesson goal</h2>
    <p>Формулировать CV и заголовок LinkedIn на русском/смешанном IT-стиле.</p>

    <h2>Warm-up</h2>
    <p>Чем bullet CV отличается от обязанностей «делал всё»?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>заголовок профиля</strong></td><td>headline</td><td>Backend Developer | Django</td></tr>
<tr><td><strong>резюме / CV</strong></td><td>краткая биография опыта</td><td>Обновите CV.</td></tr>
<tr><td><strong>bullet</strong></td><td>пункт результата</td><td>Built REST API…</td></tr>
<tr><td><strong>глагол действия</strong></td><td>Action verb</td><td>Разработал / оптимизировал.</td></tr>
<tr><td><strong>стек</strong></td><td>технологии</td><td>Стек: Python, SQL.</td></tr>
<tr><td><strong>метрика</strong></td><td>цифра результата</td><td>+30% скорости.</td></tr>
<tr><td><strong>портфолио</strong></td><td>проекты</td><td>Ссылка на GitHub.</td></tr>
<tr><td><strong>релевантность</strong></td><td>под вакансию</td><td>Адаптируйте CV.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Разработал API заказов.</li>
  <li>Оптимизировал запрос: −40% времени.</li>
  <li>Headline: Junior QA | Manual + API testing.</li>
  <li>Стек перечислите честно.</li>
  <li>Под вакансию вынесите релевантное вверх.</li>
    </ul>

    <h2>Dialogue — правка CV</h2>
    <p><strong>Ментор:</strong> «Отвечал за систему» слабо.<br><strong>Кандидат:</strong> Заменю на: «Поддерживал Django API, закрыл 30+ тикетов/месяц, p95 latency < 200 мс».</p>

    <h2>Grammar focus — Глагол + объект + результат</h2>
    <p><strong>Сделал X → для Y → результат Z.</strong></p>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ «Responsible for things». → ✅ Глагол + результат.</li>
  <li>❌ Headline из эмодзи. → ✅ Роль и ценность.</li>
    </ul>

    <h2>Reading — CV читают 20 секунд</h2>
    <p>Верхняя треть должна доказывать fit на роль.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Перепишите 3 bullet.</li>
  <li>Соберите headline.</li>
  <li>Список стека без воды.</li>
    </ol>

    <h2>Quick review</h2>
    <p>CV · headline · bullet · метрика · стек</p>
""",
            ),
            ],
            "practice": {
            'rit-email-templates': _quiz(
                    'rit-q-subject',
                    'Тема',
                    'Email.',
                    'Хорошая тема должна…',
                    [
                        'A) ясно называть тему (и срочность при необходимости)',
                        'B) говорить только «Привет»',
                        'C) быть пустой',
                        'D) только эмодзи',
                    ],
                    'A',
                ),
            'rit-interview-it': _quiz(
                    'rit-q-star-base',
                    'STAR база',
                    'Interview.',
                    'STAR расшифровывается как…',
                    [
                        'A) Situation, Task, Action, Result',
                        'B) Server, Token, API, Router',
                        'C) Scrum, Test, Alert, Rollback',
                        'D) Soft, Tall, Angry, Random',
                    ],
                    'A',
                ),
            'rit-linkedin-cv': _quiz(
                    'rit-q-cv-verb',
                    'CV',
                    'Career.',
                    'Лучшее начало bullet:',
                    [
                        'A) Разработал REST API для трекинга заказов',
                        'B) Отвечал за всякое',
                        'C) Что-то происходило',
                        'D) Я очень хороший всегда',
                    ],
                    'A',
                ),
            },
            "exercises": [
            _quiz(
                'rit-m15-followup',
                'Follow-up',
                'Email.',
                'Follow-up письмо — это…',
                [
                    'A) вежливое повторное сообщение по просьбе',
                    'B) malware',
                    'C) вентилятор',
                    'D) отмена спринта',
                ],
                'A',
            ),
            _quiz(
                'rit-m15-could',
                'Вежливость',
                'Email.',
                'Самая формальная просьба:',
                [
                    'A) Не могли бы вы согласовать доступ до пятницы?',
                    'B) Согласуй сейчас!!!!',
                    'C) Дай доступ или иначе.',
                    'D) Access me immediately forever.',
                ],
                'A',
                difficulty='medium',
            ),
            ],
            "homework": _hw(
                'Русский язык для IT — Модуль 15\n1) 3 шаблона email.\n2) Pitch 60 сек.\n3) CV: 6 bullet с метриками.\n4) Глоссарий career.'
            ),
        }
]
