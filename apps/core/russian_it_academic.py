"""
Academic Russian for IT / Computer Science — EAP module + lesson enrichments.
"""

from __future__ import annotations

from apps.core.russian_it_content import _hw, _lec, _quiz

_LESSON_ENRICHMENT = """
<h2>Collocations & useful chunks</h2>
<ul>
  <li><strong>создать тикет</strong> / <strong>закрыть проблему</strong> / <strong>поделиться апдейтом</strong></li>
  <li><strong>успеть к дедлайну</strong> / <strong>заблокировать релиз</strong> / <strong>проверить pull request</strong></li>
  <li><strong>в production</strong> / <strong>на staging</strong> / <strong>с отставанием от графика</strong></li>
</ul>

<h2>Academic / study tip</h2>
<p>Когда изучаете тему для университета или сертификации, практикуйте <strong>парафраз</strong>:
прочитайте абзац, закройте страницу и запишите идею своими словами.
Технические термины (API, спринт, latency) сохраняйте, структуру предложения меняйте.
Не копируйте фразу из статьи без ссылки.</p>

<h2>Mini writing task</h2>
<p>Напишите 4–6 предложений: краткий пересказ урока для одногруппника, который отсутствовал.
Используйте настоящее время для фактов и формы совета (<em>нужно / рекомендуется</em>).</p>
""".strip()


def enrich_lecture_html(html: str) -> str:
    """Add collocations, academic tip, and mini writing if not already present."""
    text = (html or "").strip()
    if not text:
        return text
    if "Academic / study tip" in text or "Collocations & useful chunks" in text:
        return text
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
    "title": 'Akademik rus tili (Академический русский для IT)',
    "slug": 'rit-academic',
    "description": 'CS/IT talabalari uchun: abstract, iqtibos, hisobot va taqdimot — ruscha.',
    "lectures": [
            _lec(
                'Чтение статей и аннотаций',
                'rit-academic-abstracts',
                """
<h2>Lesson goal</h2>
    <p>Просматривать аннотацию CS/IT: цель, метод, результат.</p>

    <h2>Warm-up</h2>
    <p>Что вы ищете в abstract за 60 секунд?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>аннотация / abstract</strong></td><td>краткое резюме статьи</td><td>Сначала abstract.</td></tr>
<tr><td><strong>гипотеза</strong></td><td>проверяемая идея</td><td>Наша гипотеза…</td></tr>
<tr><td><strong>методология</strong></td><td>как проводили исследование</td><td>Методология описана в разделе 3.</td></tr>
<tr><td><strong>датасет</strong></td><td>набор данных</td><td>Обучали на публичном датасете.</td></tr>
<tr><td><strong>результаты / findings</strong></td><td>что обнаружили</td><td>Findings: +12%.</td></tr>
<tr><td><strong>ограничение</strong></td><td>limitation</td><td>Ограничение — малая выборка.</td></tr>
<tr><td><strong>цитировать</strong></td><td>дать ссылку на источник</td><td>Всегда цитируйте.</td></tr>
<tr><td><strong>рецензируемый</strong></td><td>peer-reviewed</td><td>Предпочитайте peer-reviewed.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Статья исследует / предлагает / оценивает…</li>
  <li>Авторы утверждают, что…</li>
  <li>Согласно аннотации, вклад в том, что…</li>
  <li>Исследование основано на экспериментах.</li>
  <li>Нужны дальнейшие исследования…</li>
    </ul>

    <h2>Dialogue — учебная группа</h2>
    <p><strong>Студент A:</strong> Понял abstract?<br><strong>Студент B:</strong> В основном. Предлагают кэш для мобильных API.<br><strong>A:</strong> Метод?<br><strong>B:</strong> Сравнили три алгоритма на одном датасете. Latency −12%, но выборка мала.</p>

    <h2>Grammar focus — Глаголы пересказа</h2>
    <ul><li>Авторы <strong>утверждают</strong> / <strong>показывают</strong> / <strong>делают вывод</strong>, что…</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Статья про про AI. → ✅ Статья исследует AI.</li>
  <li>❌ Копирую фразу из paper. → ✅ Парафраз + цитата.</li>
    </ul>

    <h2>Reading — Образец аннотации</h2>
    <p>Мобильные приложения часто тормозят на слабой сети. Работа предлагает лёгкую стратегию кэширования ответов API. Мы сравнили метод с двумя baseline на трёх датасетах. Среднее снижение latency — 12%. Ограничение — только Android. Дальше — бенчмарки iOS.<br><strong>Проверка:</strong> проблема / метод / результат / limitation?</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Что такое abstract?</li>
  <li>Перескажите образец.</li>
  <li>3 академических вопроса партнёру.</li>
    </ol>

    <h2>Quick review</h2>
    <p>abstract · гипотеза · findings · цитировать · limitation</p>
""",
            ),
            _lec(
                'Отчёты и цитирование',
                'rit-academic-writing',
                """
<h2>Lesson goal</h2>
    <p>Структурировать отчёт и корректно цитировать источники.</p>

    <h2>Warm-up</h2>
    <p>Чем парафраз отличается от копипаста?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>отчёт</strong></td><td>письменная работа</td><td>Сдайте отчёт.</td></tr>
<tr><td><strong>парафраз</strong></td><td>пересказ своими словами</td><td>Сделайте парафраз.</td></tr>
<tr><td><strong>плагиат</strong></td><td>чужой текст без кредита</td><td>Плагиат недопустим.</td></tr>
<tr><td><strong>ссылка / citation</strong></td><td>указание источника</td><td>Добавьте citation.</td></tr>
<tr><td><strong>список литературы</strong></td><td>references</td><td>Оформите references.</td></tr>
<tr><td><strong>раздел методов</strong></td><td>methods</td><td>В methods — пассив.</td></tr>
<tr><td><strong>введение / заключение</strong></td><td>рамка текста</td><td>В заключении — итог.</td></tr>
<tr><td><strong>академический тон</strong></td><td>нейтральный стиль</td><td>Без разговорных штампов.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>По данным Иванова (2023), …</li>
  <li>В данном отчёте мы описываем…</li>
  <li>Метод был протестирован на…</li>
  <li>Следует отметить ограничение…</li>
  <li>Таким образом, можно сделать вывод…</li>
    </ul>

    <h2>Dialogue — про плагиат</h2>
    <p><strong>Преподаватель:</strong> Это слишком похоже на статью.<br><strong>Студент:</strong> Я перепишу парафразом и добавлю ссылку.</p>

    <h2>Grammar focus — Пассив в methods</h2>
    <ul><li>Модель <strong>была обучена</strong> на 10 000 примерах.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Плагиат = форматирование слайдов. → ✅ Чужой текст без кредита.</li>
  <li>❌ Methods: «мы круто потренировали». → ✅ Нейтральный пассив/факты.</li>
    </ul>

    <h2>Reading — Честность письма</h2>
    <p>Идея может быть общей, формулировка и кредит — ваши обязательства.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Парафраз 4 предложения.</li>
  <li>Скелет отчёта 6 заголовков.</li>
  <li>Пример citation.</li>
    </ol>

    <h2>Quick review</h2>
    <p>парафраз · плагиат · citation · methods · заключение</p>
""",
            ),
            _lec(
                'Презентации и семинары',
                'rit-academic-presentations',
                """
<h2>Lesson goal</h2>
    <p>Структурировать доклад и отвечать на вопросы.</p>

    <h2>Warm-up</h2>
    <p>Что сказать вместо чтения слайда слово в слово?</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>доклад / презентация</strong></td><td>устное выступление</td><td>Презентация на 5 минут.</td></tr>
<tr><td><strong>слайд</strong></td><td>кадр презентации</td><td>На слайде — схема.</td></tr>
<tr><td><strong>навигация / signpost</strong></td><td>указатели речи</td><td>Далее объясню метод.</td></tr>
<tr><td><strong>Q&A</strong></td><td>вопросы и ответы</td><td>Оставим время на Q&A.</td></tr>
<tr><td><strong>раздатка</strong></td><td>handout</td><td>В раздатке формулы.</td></tr>
<tr><td><strong>уточнить</strong></td><td>clarify</td><td>Позвольте уточнить.</td></tr>
<tr><td><strong>демо</strong></td><td>показ</td><td>Короткое демо.</td></tr>
<tr><td><strong>ограничения проекта</strong></td><td>что не сделали</td><td>Честно назовите limitations.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Добрый день. Сегодня расскажу о…</li>
  <li>Сначала проблема, затем метод, потом результат.</li>
  <li>Как видно на слайде…</li>
  <li>Отличный вопрос. Коротко…</li>
  <li>Спасибо за внимание. Готов к вопросам.</li>
    </ul>

    <h2>Dialogue — после доклада</h2>
    <p><strong>Студент:</strong> Вопросы?<br><strong>Слушатель:</strong> Почему Redis?<br><strong>Студент:</strong> Нужна низкая latency для сессий. Memcached не сравнивали — это limitation.</p>

    <h2>Grammar focus — Планы</h2>
    <ul><li><strong>Сейчас покажу</strong>…</li><li><strong>Затем перейдём</strong> к результатам.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Я буду чтобы презентовать. → ✅ Я презентую / расскажу.</li>
  <li>❌ Читать весь слайд. → ✅ Говорить, слайды короткие.</li>
    </ul>

    <h2>Reading — Структура 5 минут</h2>
    <p>Хук → проблема → подход → результат → limitations → Q&A.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Интро 60 сек.</li>
  <li>Ответ «почему эта технология?»</li>
  <li>Закрытие + приглашение вопросов.</li>
    </ol>

    <h2>Quick review</h2>
    <p>signpost · Q&A · слайд · limitation · демо</p>
""",
            ),
            ],
            "practice": {
            'rit-academic-abstracts': _quiz(
                    'rit-q-abstract',
                    'Abstract',
                    'Academic.',
                    'Аннотация в основном…',
                    [
                        'A) краткое резюме цели, метода и результатов',
                        'B) список паролей',
                        'C) кабель',
                        'D) Scrum-перекус',
                    ],
                    'A',
                    editorial='Abstract = краткое резюме.',
                ),
            'rit-academic-writing': _quiz(
                    'rit-q-plagiarism',
                    'Плагиат',
                    'Writing.',
                    'Плагиат значит…',
                    [
                        'A) использовать чужую работу без кредита',
                        'B) форматировать слайды',
                        'C) переименовать переменную',
                        'D) закрыть тикет',
                    ],
                    'A',
                    editorial='Всегда парафраз + ссылка.',
                ),
            'rit-academic-presentations': _quiz(
                    'rit-q-signpost',
                    'Signposting',
                    'Talks.',
                    'Лучшая навигирующая фраза:',
                    [
                        'A) Далее объясню метод.',
                        'B) Сейчас штуки.',
                        'C) Пароль!',
                        'D) Опять ты?',
                    ],
                    'A',
                    editorial='Ведите аудиторию.',
                ),
            },
            "exercises": [
            _quiz(
                'rit-m16-cite',
                'Цитирование',
                'Academic.',
                'Цитировать источник значит…',
                [
                    'A) указать автора оригинала',
                    'B) удалить список литературы',
                    'C) спрятать датасет',
                    'D) пропустить abstract',
                ],
                'A',
            ),
            _quiz(
                'rit-m16-passive',
                'Methods',
                'Writing.',
                'Лучшее предложение methods:',
                [
                    'A) Модель была обучена на 10 000 примерах.',
                    'B) Модель мы вчера круто.',
                    'C) Трейн очень очень.',
                    'D) Password training forever.',
                ],
                'A',
                difficulty='medium',
            ),
            ],
            "homework": _hw(
                'Русский язык для IT — Модуль 16 (Academic)\n1) Парафраз короткой IT-аннотации (6 предложений).\n2) Каркас мини-отчёта (6 заголовков).\n3) Скрипт доклада 90 сек с signposting.\n4) Глоссарий: abstract, гипотеза, парафраз, плагиат, citation, Q&A.'
            ),
        }

INTERVIEW_MODULE = {
    "order": 17,
    "title": 'IT intervyu (Подготовка к собеседованию)',
    "slug": 'rit-interview',
    "description": 'IT suhbatiga tayyorgarlik: STAR, texnik savollar, salary va follow-up — ruscha.',
    "lectures": [
            _lec(
                'Поведенческое интервью (STAR)',
                'rit-interview-star',
                """
<h2>Lesson goal</h2>
    <p>Отвечать на behavioural-вопросы по STAR на уверенном B1 русском.</p>

    <h2>Warm-up</h2>
    <p>Интервьюеры спрашивают: «Расскажите случай, когда…». Им нужна структура, не роман.</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>STAR</strong></td><td>Situation, Task, Action, Result</td><td>Ответил по STAR.</td></tr>
<tr><td><strong>поведенческий вопрос</strong></td><td>про прошлый опыт</td><td>Опишите конфликт.</td></tr>
<tr><td><strong>сильная / слабая сторона</strong></td><td>strength / weakness</td><td>Сильная сторона — коммуникация.</td></tr>
<tr><td><strong>ответственность / ownership</strong></td><td>взять на себя</td><td>Я взял ownership инцидента.</td></tr>
<tr><td><strong>компромисс / trade-off</strong></td><td>выбор вариантов</td><td>Обсудили trade-off.</td></tr>
<tr><td><strong>follow-up</strong></td><td>письмо после интервью</td><td>Отправлю follow-up.</td></tr>
<tr><td><strong>cultural fit</strong></td><td>совпадение ценностей</td><td>Спросили про culture fit.</td></tr>
<tr><td><strong>сроки выхода</strong></td><td>timeline</td><td>Могу выйти через 2 недели.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>В предыдущей роли… / На прошлом проекте…</li>
  <li>Моя задача была…</li>
  <li>Я решил… / Я скоординировал…</li>
  <li>В результате мы снизили… / успели в срок.</li>
  <li>Я вынес урок…</li>
    </ul>

    <h2>Dialogue — фрагмент интервью</h2>
    <p><strong>Интервьюер:</strong> Расскажите, как чинили прод под давлением.<br><strong>Кандидат:</strong> Ситуация: API оплаты начал таймаутить в пятницу вечером.<br><strong>Кандидат:</strong> Задача: быстро вернуть платежи и держать команду в курсе.<br><strong>Кандидат:</strong> Действия: логи, откат деплоя, монитор.<br><strong>Кандидат:</strong> Результат: платежи за 25 минут, короткий постмортем.</p>

    <h2>Grammar focus — Прошедшее время для историй</h2>
    <ul><li>Я <strong>подключился</strong> к war room. Мы <strong>нашли</strong> причину.</li><li>Для опыта: Я <strong>работал</strong> с Python три года.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Я всегда трудяга. → ✅ Вот пример ownership…</li>
  <li>❌ Винить только команду. → ✅ Фокус на действиях и уроке.</li>
  <li>❌ Говорить 8 минут. → ✅ STAR ≈ 90–120 секунд.</li>
    </ul>

    <h2>Reading — Топ поведенческих тем</h2>
    <p>Подготовьте 4–5 историй: конфликт, дедлайн, ошибка, инициатива, обучение. По возможности добавляйте цифры (время, %, инциденты).</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>«Расскажите о себе» 60 сек.</li>
  <li>STAR: сложный баг.</li>
  <li>STAR: спор на code review.</li>
    </ol>

    <h2>Quick review</h2>
    <p>STAR · ownership · trade-off · follow-up · timeline</p>
""",
            ),
            _lec(
                'Техническое интервью на русском',
                'rit-interview-tech',
                """
<h2>Lesson goal</h2>
    <p>Объяснять системы, trade-off и отладку ясным языком.</p>

    <h2>Warm-up</h2>
    <p>Техническое интервью проверяет и знания, и коммуникацию.</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>уточнить требования</strong></td><td>clarify</td><td>Сначала уточню требования.</td></tr>
<tr><td><strong>ограничения</strong></td><td>constraints</td><td>Какие ограничения по памяти?</td></tr>
<tr><td><strong>архитектура</strong></td><td>устройство системы</td><td>Кратко об архитектуре.</td></tr>
<tr><td><strong>узкое место</strong></td><td>bottleneck</td><td>Bottleneck в БД.</td></tr>
<tr><td><strong>отладка</strong></td><td>debugging</td><td>Шаги отладки…</td></tr>
<tr><td><strong>оценка сложности</strong></td><td>complexity</td><td>Сложность O(n).</td></tr>
<tr><td><strong>тест-кейсы</strong></td><td>проверки</td><td>Проверю edge cases.</td></tr>
<tr><td><strong>не уверен</strong></td><td>честность</td><td>Не уверен, проверю документацию.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Правильно ли я понял задачу: …?</li>
  <li>Рассмотрю два подхода и trade-off.</li>
  <li>Сначала напишу тест-кейсы.</li>
  <li>Bottleneck, скорее всего, в I/O.</li>
  <li>Могу ошибаться — давайте проверим на примере.</li>
    </ul>

    <h2>Dialogue — уточнение</h2>
    <p><strong>Кандидат:</strong> Нужно ли учитывать одновременные записи?<br><strong>Интервьюер:</strong> Да.<br><strong>Кандидат:</strong> Тогда добавлю блокировку/очередь и обсужу latency.</p>

    <h2>Grammar focus — Сначала мышление вслух</h2>
    <p>Уточняю → предлагаю план → пишу/рисую → тестирую → усложняю.</p>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Молчать 20 минут. → ✅ Проговаривать план.</li>
  <li>❌ Оскорблять условие. → ✅ Уточнять ограничения.</li>
  <li>❌ Притворяться, что знаете всё. → ✅ Честно обозначить пробел + как проверить.</li>
    </ul>

    <h2>Reading — Коммуникация = часть оценки</h2>
    <p>Даже неполный ответ с ясным рассуждением часто сильнее «угадайки» без объяснений.</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Уточните задачу вслух.</li>
  <li>Объясните trade-off кэша.</li>
  <li>Опишите отладку 500 на API.</li>
    </ol>

    <h2>Quick review</h2>
    <p>clarify · trade-off · bottleneck · edge case · архитектура</p>
""",
            ),
            _lec(
                'Зарплата, оффер и follow-up',
                'rit-interview-offer',
                """
<h2>Lesson goal</h2>
    <p>Спокойно обсуждать вилку, процесс и писать thank-you письмо.</p>

    <h2>Warm-up</h2>
    <p>Денежный разговор чувствителен: подготовьте цифры заранее.</p>

    <h2>Key vocabulary</h2>
    <table>
      <tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
      <tr><td><strong>компенсация / пакет</strong></td><td>оклад + бенефиты</td><td>Какой total package?</td></tr>
<tr><td><strong>базовая зарплата</strong></td><td>fixed pay</td><td>Base salary конкурентоспособный.</td></tr>
<tr><td><strong>бонус / equity</strong></td><td>доп. выплата / доля</td><td>Есть ли бонус или equity?</td></tr>
<tr><td><strong>срок уведомления</strong></td><td>notice period</td><td>Notice period — 2 недели.</td></tr>
<tr><td><strong>оффер</strong></td><td>письменное предложение</td><td>Пришлите offer letter.</td></tr>
<tr><td><strong>торговаться</strong></td><td>negotiate</td><td>Хочу обсудить дату выхода.</td></tr>
<tr><td><strong>встречное предложение</strong></td><td>counter-offer</td><td>Вежливый counter-offer.</td></tr>
<tr><td><strong>благодарственное письмо</strong></td><td>thank-you note</td><td>Отправил thank-you в тот же день.</td></tr>
    </table>

    <h2>Useful phrases (memorise)</h2>
    <ul>
      <li>Ориентируюсь на вилку … в зависимости от обязанностей и пакета.</li>
  <li>Можете поделиться бюджетом роли?</li>
  <li>Гибок по дате выхода, если сойдёмся по офферу.</li>
  <li>Спасибо за разговор. Было интересно узнать о команде.</li>
  <li>Подскажите следующие шаги и сроки.</li>
    </ul>

    <h2>Dialogue — вопрос про зарплату</h2>
    <p><strong>Интервьюер:</strong> Какие ожидания по зарплате?<br><strong>Кандидат:</strong> По рынку и роли ориентируюсь на X–Y total package. Готов обсуждать при хорошем совпадении обязанностей.<br><strong>Интервьюер:</strong> Обычно ближе к середине вилки.<br><strong>Кандидат:</strong> Звучит перспективно. Можете также рассказать про бонус, бенефиты и сроки процесса?</p>

    <h2>Grammar focus — Смягчения</h2>
    <ul><li><strong>Хотел бы</strong> понять полный пакет.</li><li><strong>Не могли бы вы</strong> подсказать следующие шаги?</li><li><strong>Я гибок</strong> по удалённым дням / дате выхода.</li></ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>❌ Первый вопрос: Сколько денег? → ✅ Сначала роль, потом компенсация.</li>
  <li>❌ Принять, не читая. → ✅ Попросите offer letter и изучите.</li>
  <li>❌ Без follow-up. → ✅ Короткое thank-you в течение 24 часов.</li>
    </ul>

    <h2>Reading — Шаблон follow-up</h2>
    <p>Тема: Спасибо — собеседование Backend Engineer<br>Здравствуйте, …! Спасибо за разговор о роли … Мне особенно интересно было обсудить … Готов предоставить доп. информацию. Буду рад следующим шагам.<br>С уважением, Имя</p>

    <h2>Speaking practice</h2>
    <ol>
      <li>Ожидания по зарплате — 3 предложения.</li>
  <li>3 умных вопроса о команде.</li>
  <li>Прочитайте thank-you вслух.</li>
    </ol>

    <h2>Quick review</h2>
    <p>вилка · package · notice · offer · thank-you</p>
""",
            ),
            ],
            "practice": {
            'rit-interview-star': _quiz(
                    'rit-q-star',
                    'STAR',
                    'Interview.',
                    'STAR расшифровывается как…',
                    [
                        'A) Situation, Task, Action, Result',
                        'B) Server, Token, API, Router',
                        'C) Soft, Tall, Angry, Random',
                        'D) SQL, Test, Alert, Rollback',
                    ],
                    'A',
                    editorial='STAR = структура истории.',
                ),
            'rit-interview-tech': _quiz(
                    'rit-q-clarify',
                    'Clarify',
                    'Tech interview.',
                    'Лучший первый шаг в техзадаче:',
                    [
                        'A) уточнить требования / переформулировать задачу',
                        'B) оскорбить интервьюера',
                        'C) молчать 20 минут',
                        'D) гадать без размышлений',
                    ],
                    'A',
                    editorial='Сначала уточняйте.',
                ),
            'rit-interview-offer': _quiz(
                    'rit-q-followup',
                    'Follow-up',
                    'After interview.',
                    'Thank-you обычно отправляют…',
                    [
                        'A) в течение примерно 24 часов',
                        'B) никогда',
                        'C) через год',
                        'D) только факсом в 1990',
                    ],
                    'A',
                    editorial='Лучше в тот же день.',
                ),
            },
            "exercises": [
            _quiz(
                'rit-m17-ownership',
                'Ownership',
                'Behavioural.',
                'Лучшая привычка на интервью:',
                [
                    'A) описывать свои действия и измеримый результат',
                    'B) только винить других',
                    'C) отказаться от примеров',
                    'D) смотреть в телефон всё время',
                ],
                'A',
            ),
            _quiz(
                'rit-m17-tradeoff',
                'Trade-off',
                'Tech talk.',
                'Trade-off значит…',
                [
                    'A) выбор между вариантами с разными плюсами/минусами',
                    'B) тип клавиатуры',
                    'C) бесплатный обед',
                    'D) удаление prod ради шутки',
                ],
                'A',
                difficulty='medium',
            ),
            ],
            "homework": _hw(
                'Русский язык для IT — Модуль 17 (Interview)\n1) 5 STAR-историй (баг, конфликт, дедлайн, обучение, лидерство).\n2) Pitch проекта 90 сек + обзор архитектуры.\n3) Скрипт вилки зарплаты + thank-you email.\n4) Глоссарий: STAR, trade-off, bottleneck, edge case, notice period, offer letter.'
            ),
        }
