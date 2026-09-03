"""English and Russian HTML bodies for SQL lessons, keyed by lecture slug."""

from __future__ import annotations

SQL_LESSON_HTML: dict[str, dict[str, str]] = {
    "select-nima": {
        "en": """
<p>Hello. If you have never written SQL — that’s fine. We start from this lesson; you don’t need to know anything beforehand.</p>

<p>At work, data usually lives in a <strong>table</strong>, like in Excel: rows and columns. The difference is that a database can hold millions of rows, and filtering them with a mouse is hard. That’s why we give the computer a <em>plain-language command</em>: “From this table, bring me these columns.”</p>

<p>That command language is <strong>SQL</strong>. The full name is Structured Query Language — a “structured query language”. The name sounds intimidating, but in practice you start with 2–3 words.</p>

<p>In our workshop we have a bank example. Customers live in the <code>customers</code> table. Here’s how it looks:</p>
<table>
  <tr><th>id</th><th>name</th><th>city</th></tr>
  <tr><td>1</td><td>Ali Valiyev</td><td>Toshkent</td></tr>
  <tr><td>2</td><td>Malika Karimova</td><td>Samarqand</td></tr>
  <tr><td>3</td><td>Javohir Saidov</td><td>Buxoro</td></tr>
</table>
<p>A horizontal line is a <strong>row</strong>: one person. Vertical is a <strong>column</strong>: id, name, city. Same logic as a “row” and a “column” in Excel.</p>

<p>Now the most important command. To say “bring me the names” we write:</p>
<pre>SELECT name FROM customers;</pre>
<p>This is easy to read: <code>SELECT</code> — “choose / bring”, <code>name</code> — which column, <code>FROM customers</code> — from where. The semicolon at the end is optional in many places, but people usually put it.</p>
<p>Result: Ali Valiyev, Malika Karimova, Javohir Saidov. Other columns don’t appear — because we didn’t ask for them.</p>

<p>If you want to see everything, use a star:</p>
<pre>SELECT * FROM customers;</pre>
<p><code>*</code> means “all columns”. Useful while learning. Later at work we learn to name columns explicitly — I’ll explain why in the next lesson.</p>

<p>One more thing: don’t think of SQL as a “change the data” language. Today’s <code>SELECT</code> only <strong>reads</strong>. Nothing in the table is deleted or broken. Practice with a calm mind.</p>

<p>Below you’ll see these queries. Then in the exercise you’ll write one yourself: take a single column from a table. That first success is the point.</p>
""",
        "ru": """
<p>Привет. Если вы никогда не писали SQL — это нормально. Начнём с этого урока; заранее ничего знать не нужно.</p>

<p>На работе данные обычно лежат в <strong>таблице</strong>, как в Excel: строки и столбцы. Разница в том, что в базе могут быть миллионы строк, и фильтровать их мышкой сложно. Поэтому мы даём компьютеру <em>команду на простом языке</em>: «Из этой таблицы принеси вот эти столбцы».</p>

<p>Этот язык команд — <strong>SQL</strong>. Полное название Structured Query Language, то есть «язык структурированных запросов». Имя пугает, но на практике начинают с двух–трёх слов.</p>

<p>В нашем занятии есть банковский пример. Клиенты лежат в таблице <code>customers</code>. Вот как она выглядит:</p>
<table>
  <tr><th>id</th><th>name</th><th>city</th></tr>
  <tr><td>1</td><td>Ali Valiyev</td><td>Toshkent</td></tr>
  <tr><td>2</td><td>Malika Karimova</td><td>Samarqand</td></tr>
  <tr><td>3</td><td>Javohir Saidov</td><td>Buxoro</td></tr>
</table>
<p>Горизонтальная линия — <strong>строка</strong>: один человек. Вертикальная — <strong>столбец</strong>: id, имя, город. Та же логика, что «строка» и «столбец» в Excel.</p>

<p>Теперь самая важная команда. Чтобы сказать «принеси имена», пишем:</p>
<pre>SELECT name FROM customers;</pre>
<p>Читать легко: <code>SELECT</code> — «выбери / принеси», <code>name</code> — какой столбец, <code>FROM customers</code> — откуда. Точка с запятой в конце во многих системах необязательна, но её обычно ставят.</p>
<p>Результат: Ali Valiyev, Malika Karimova, Javohir Saidov. Другие столбцы не появятся — мы их не просили.</p>

<p>Если нужно увидеть всё, звёздочка:</p>
<pre>SELECT * FROM customers;</pre>
<p><code>*</code> значит «все столбцы». Полезно при учёбе. Позже на работе научимся писать конкретные столбцы — почему, расскажу в следующем уроке.</p>

<p>Ещё одно: не думайте о SQL как о «языке изменений». Сегодняшний <code>SELECT</code> только <strong>читает</strong>. Данные в таблице не удаляются и не портятся. Тренируйтесь спокойно.</p>

<p>Ниже вы увидите эти запросы. Затем в упражнении напишете сами: возьмите из таблицы только один столбец. Первый успех — вот он.</p>
""",
    },
    "ustunlarni-tanlash": {
        "en": """
<p>In the previous lesson we took the whole table with <code>SELECT *</code>. That’s “dump everything on the desk”. In a report you usually need 2–3 columns.</p>

<p>Imagine a manager asks: “Where do the customers live?” They don’t need <code>id</code> or a signup date. What they need is name and city.</p>
<pre>SELECT name, city FROM customers;</pre>
<p>Columns are written with a <strong>comma</strong>. The order is yours: if you put <code>name</code> first, the first result column is the name.</p>
<table>
  <tr><th>name</th><th>city</th></tr>
  <tr><td>Ali Valiyev</td><td>Toshkent</td></tr>
  <tr><td>Malika Karimova</td><td>Samarqand</td></tr>
</table>

<p>Why not always use the star? Three reasons, in plain language:</p>
<ul>
  <li>Extra columns distract the eye and slow the query on a large table.</li>
  <li>If tomorrow someone adds an “internal note” column, <code>*</code> will dump it too — sometimes something confidential.</li>
  <li>A person reading what you asked should understand it. Specific columns mean a specific question.</li>
</ul>

<p>Sometimes the column name is English and the report must be in Uzbek. Then <code>AS</code> helps — an alias, a new heading only for this query:</p>
<pre>SELECT name AS mijoz, city AS shahar
FROM customers;</pre>
<p>The data does not change. Only the result columns are labeled “mijoz” and “shahar”. In exercises the system may expect that name — so don’t ignore things like <code>AS total</code>.</p>

<p>Small tip: first write the question in plain language (“I need name and city”), then turn it into SQL. Don’t do it backwards.</p>
""",
        "ru": """
<p>В прошлом уроке мы взяли всю таблицу через <code>SELECT *</code>. Это «вывалить всё на стол». В отчёте обычно нужны 2–3 столбца.</p>

<p>Представьте, руководитель спрашивает: «Где живут клиенты?» Ему не нужны ни <code>id</code>, ни дата регистрации. Нужны имя и город.</p>
<pre>SELECT name, city FROM customers;</pre>
<p>Столбцы пишутся через <strong>запятую</strong>. Порядок ваш: если сначала <code>name</code>, первый столбец результата — имя.</p>
<table>
  <tr><th>name</th><th>city</th></tr>
  <tr><td>Ali Valiyev</td><td>Toshkent</td></tr>
  <tr><td>Malika Karimova</td><td>Samarqand</td></tr>
</table>

<p>Почему не стоит всегда ставить звёздочку? Три причины простыми словами:</p>
<ul>
  <li>Лишние столбцы отвлекают и на большой таблице замедляют запрос.</li>
  <li>Если завтра в базу добавят столбец «внутренний комментарий», <code>*</code> вытащит и его — иногда секретное.</li>
  <li>Человек, который читает ваш запрос, должен понять, что вы спросили. Конкретные столбцы — конкретный вопрос.</li>
</ul>

<p>Иногда имя столбца английское, а отчёт должен быть на узбекском. Тогда помогает <code>AS</code> — псевдоним, новый заголовок только для этого запроса:</p>
<pre>SELECT name AS mijoz, city AS shahar
FROM customers;</pre>
<p>Данные не меняются. В результате столбцы просто подписаны «mijoz» и «shahar». В упражнениях система может ждать именно это имя — поэтому не пропускайте вещи вроде <code>AS total</code>.</p>

<p>Маленький совет: сначала сформулируйте вопрос обычным языком («нужны имя и город»), потом переведите в SQL. Не наоборот.</p>
""",
    },
    "natijani-oqish": {
        "en": """
<p>You wrote a query and pressed the button. A table appeared on the screen. You also need to learn how to read it — otherwise you’ll think “it worked” and draw the wrong conclusion.</p>

<p><strong>Each row is one fact.</strong> In the customers table, one row = one person. In payments, one row = one operation. If 0 rows come back, the program is not broken: there is no record that matches the condition. In analysis, “nobody” is also an answer.</p>

<p>Now repetition. If you write:</p>
<pre>SELECT city FROM customers;</pre>
<p>Toshkent may appear twice — because two customers live in Toshkent. That is not an error. But the question can be different: “Which cities exist at all?” You don’t need duplicates. Then:</p>
<pre>SELECT DISTINCT city FROM customers;</pre>
<p><code>DISTINCT</code> means “without duplicates”. Each city once. If you ask how many unique cities there are:</p>
<pre>SELECT COUNT(DISTINCT city) AS shahar_soni FROM customers;</pre>
<p>You don’t have to memorize this yet. The idea matters: duplicates vs unique — two different questions.</p>

<p>Another idea: <strong>NULL</strong>. It means “unknown”. If a city was never entered, the cell is not empty text — it is NULL. It is not 0 either. Later we’ll learn <code>IS NULL</code>. For now remember: if you compare NULL with <code>= 'Toshkent'</code>, that row usually does not appear.</p>

<p>To skim a large table you sometimes need only 5 rows:</p>
<pre>SELECT * FROM customers LIMIT 5;</pre>
<p>That’s “the first 5”. If you don’t sort, which 5 they are may not be well defined. We’ll learn ordering in the next module.</p>

<p>In short: the result is an ordinary table. Read it. Are there duplicates? Is it empty? Is there NULL? Those three questions turn you from a “robot querier” into an analyst.</p>
""",
        "ru": """
<p>Вы написали запрос и нажали кнопку. На экране появилась таблица. Её тоже нужно уметь читать — иначе скажете «сработало» и сделаете неверный вывод.</p>

<p><strong>Каждая строка — один факт.</strong> В таблице клиентов одна строка = один человек. В платежах одна строка = одна операция. Если вернулось 0 строк, программа не сломалась: нет записи, которая подходит под условие. В анализе «никто» — тоже ответ.</p>

<p>Теперь про повторы. Если написать:</p>
<pre>SELECT city FROM customers;</pre>
<p>Toshkent может появиться дважды — потому что два клиента живут в Toshkent. Это не ошибка. Но вопрос может быть другим: «Какие города вообще есть?» Повторы не нужны. Тогда:</p>
<pre>SELECT DISTINCT city FROM customers;</pre>
<p><code>DISTINCT</code> — «без повторов». Каждый город один раз. Если спросить, сколько уникальных городов:</p>
<pre>SELECT COUNT(DISTINCT city) AS shahar_soni FROM customers;</pre>
<p>Сейчас это не нужно помнить наизусть. Важна идея: повтор и уникальность — два разных вопроса.</p>

<p>Ещё одно понятие: <strong>NULL</strong>. Это «неизвестно». Если город не ввели, ячейка не пустой текст, а NULL. Это не 0 и не пустая строка. Позже выучим <code>IS NULL</code>. Пока запомните: если сравнить NULL с <code>= 'Toshkent'</code>, эта строка обычно не появится.</p>

<p>Чтобы просмотреть большую таблицу, иногда нужны только 5 строк:</p>
<pre>SELECT * FROM customers LIMIT 5;</pre>
<p>Это «первые 5». Без сортировки не всегда ясно, какие именно 5. Порядок разберём в следующем модуле.</p>

<p>Итог: результат — обычная таблица. Прочитайте её. Есть повторы? Пусто? Есть NULL? Эти три вопроса превращают вас из «робота-запросчика» в аналитика.</p>
""",
    },
    "where-operatori": {
        "en": """
<p>So far we took the whole table. In practice it’s: “Only Toshkent”, “Only large payments”. Choosing rows is <code>WHERE</code>. In English: “where / with which condition”.</p>

<p>Remember the reading order, as if you were speaking a sentence:</p>
<p><em>From the customers table, of those whose city is Toshkent, bring name and city.</em></p>
<pre>SELECT name, city
FROM customers
WHERE city = 'Toshkent';</pre>
<p>Ali appears. Malika (Samarqand) does not. The filter worked.</p>

<p>Two rules — most mistakes start here:</p>
<p><strong>Text</strong> — inside single quotes. <code>'Toshkent'</code>, <code>'debit'</code>. Without quotes, SQL may think it is a column name.</p>
<p><strong>Numbers</strong> — no quotes. <code>amount &gt; 100000</code>. No thousand separators, no currency symbols.</p>
<pre>SELECT id, amount FROM transactions WHERE amount &gt; 100000;</pre>

<p>Comparison signs in everyday language:</p>
<ul>
  <li><code>=</code> equal</li>
  <li><code>&lt;&gt;</code> or <code>!=</code> not equal</li>
  <li><code>&gt;</code> greater, <code>&gt;=</code> greater or equal</li>
  <li><code>&lt;</code> less, <code>&lt;=</code> less or equal</li>
</ul>
<p>When two conditions must both hold — <code>AND</code>:</p>
<pre>SELECT name, city FROM customers
WHERE city = 'Toshkent' AND name = 'Ali Valiyev';</pre>
<p>Both must be true. In the next lesson we expand with <code>OR</code>, <code>LIKE</code>, <code>IN</code>. Today: <code>=</code>, <code>&gt;</code>, <code>AND</code>.</p>

<p>Text length — <code>LENGTH</code>. For example, very long notes:</p>
<pre>SELECT id FROM transactions
WHERE LENGTH(note) &gt; 15;</pre>
<p><code>LENGTH(column)</code> — number of characters. <code>&gt; 15</code> is strictly greater (not 15, but 16 and up).</p>

<p>Arithmetic can live in WHERE too. For example density = population / area. If you divide integer by integer, the fraction can disappear — so turn one side into a decimal:</p>
<pre>SELECT name,
       ROUND(population * 1.0 / area, 2) AS density
FROM World
WHERE population * 1.0 / area &gt; 90
  AND gdp &gt;= 10000000000;</pre>
<p><code>ROUND(..., 2)</code> — two decimal places. <code>AS density</code> — the result column name. The exercise will expect that name.</p>

<p>If finance says “show only debit”:</p>
<pre>SELECT id, transaction_type
FROM transactions
WHERE transaction_type = 'debit';</pre>
<p>If you write <code>debit</code> without quotes — it may not work. Make that mistake once, then you won’t forget.</p>

<p>Remember: <code>WHERE</code> keeps or drops a row. Choosing columns is still in <code>SELECT</code>. First “which people”, then “which fields from them”.</p>
""",
        "ru": """
<p>До сих пор мы брали всю таблицу. На практике: «Только Toshkent», «Только крупные платежи». Выбор строк — <code>WHERE</code>. По-английски «где / с каким условием».</p>

<p>Запомните порядок чтения, будто произносите фразу:</p>
<p><em>Из таблицы customers, у тех, чей город Toshkent, принеси имя и город.</em></p>
<pre>SELECT name, city
FROM customers
WHERE city = 'Toshkent';</pre>
<p>Ali появится. Malika (Samarqand) — нет. Фильтр сработал.</p>

<p>Два правила — отсюда выходит много ошибок:</p>
<p><strong>Текст</strong> — в одинарных кавычках. <code>'Toshkent'</code>, <code>'debit'</code>. Без кавычек SQL может принять это за имя столбца.</p>
<p><strong>Число</strong> — без кавычек. <code>amount &gt; 100000</code>. Разделители тысяч и знаки валюты не ставят.</p>
<pre>SELECT id, amount FROM transactions WHERE amount &gt; 100000;</pre>

<p>Знаки сравнения обычным языком:</p>
<ul>
  <li><code>=</code> равно</li>
  <li><code>&lt;&gt;</code> или <code>!=</code> не равно</li>
  <li><code>&gt;</code> больше, <code>&gt;=</code> больше или равно</li>
  <li><code>&lt;</code> меньше, <code>&lt;=</code> меньше или равно</li>
</ul>
<p>Если нужны оба условия сразу — <code>AND</code>:</p>
<pre>SELECT name, city FROM customers
WHERE city = 'Toshkent' AND name = 'Ali Valiyev';</pre>
<p>Оба должны быть истинны. В следующем уроке расширим <code>OR</code>, <code>LIKE</code>, <code>IN</code>. Сегодня: <code>=</code>, <code>&gt;</code>, <code>AND</code>.</p>

<p>Длина текста — <code>LENGTH</code>. Например, очень длинные комментарии:</p>
<pre>SELECT id FROM transactions
WHERE LENGTH(note) &gt; 15;</pre>
<p><code>LENGTH(столбец)</code> — число символов. <code>&gt; 15</code> — строго больше (не 15, а 16 и выше).</p>

<p>В WHERE может быть и расчёт. Например плотность = население / площадь. Если делить целое на целое, дробь может пропасть — поэтому один операнд сделайте дробным:</p>
<pre>SELECT name,
       ROUND(population * 1.0 / area, 2) AS density
FROM World
WHERE population * 1.0 / area &gt; 90
  AND gdp &gt;= 10000000000;</pre>
<p><code>ROUND(..., 2)</code> — два знака после запятой. <code>AS density</code> — имя столбца результата. В упражнении ждут именно это имя.</p>

<p>Если в финансах говорят «покажи только debit»:</p>
<pre>SELECT id, transaction_type
FROM transactions
WHERE transaction_type = 'debit';</pre>
<p>Если написать <code>debit</code> без кавычек — может не сработать. Сделайте эту ошибку один раз, потом не забудете.</p>

<p>Помните: <code>WHERE</code> оставляет или отбрасывает строку. Выбор столбцов по-прежнему в <code>SELECT</code>. Сначала «какие люди», потом «какие поля у них».</p>
""",
    },
    "order-by": {
        "en": """
<p>We filtered. But the result may come out “however it landed”. A manager says “start from the largest payment”. That is sorting: <code>ORDER BY</code>.</p>

<p>By default SQL sorts ascending: small to large, A to Z. That’s called <code>ASC</code>; even if you don’t write it, that’s the default. The opposite is <code>DESC</code> (descending, going down).</p>
<pre>SELECT id, amount
FROM transactions
ORDER BY amount DESC;</pre>
<p>The first row is the largest sum. Almost every “top” report uses <code>DESC</code>.</p>

<p>If you need cheap to expensive, drop <code>DESC</code> or write <code>ASC</code>:</p>
<pre>ORDER BY amount ASC</pre>

<p>Sometimes there are two criteria: first city, then name within the same city.</p>
<pre>SELECT name, city
FROM customers
ORDER BY city, name;</pre>
<p>SQL sorts by <code>city</code> first. When the city is the same, it looks at <code>name</code>. Directions can mix: <code>ORDER BY city ASC, amount DESC</code>.</p>

<p>If they say “the largest 3”, first sort, then limit:</p>
<pre>SELECT id, amount
FROM transactions
ORDER BY amount DESC
LIMIT 3;</pre>
<p>If you put <code>LIMIT 3</code> without sorting, you may get three random rows. First who is first, then how many.</p>

<p>Often filtering + unique + order come together. Remember <code>WHERE</code>, <code>DISTINCT</code>, <code>AS</code> from previous lessons:</p>
<pre>SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;</pre>
<p>First the condition, then drop duplicates, then ascending order. The column is named <code>id</code> because of <code>AS id</code>.</p>

<p>When an exercise says “row order is checked” — don’t forget <code>ORDER BY</code>. Right columns, wrong order — still counted as wrong.</p>
""",
        "ru": """
<p>Отфильтровали. Но результат может выйти «как получится». Руководитель говорит: «начни с самого крупного платежа». Это сортировка: <code>ORDER BY</code>.</p>

<p>По умолчанию SQL ставит по возрастанию: от малого к большому, от A до Z. Это <code>ASC</code>; даже если не напишете, будет так. Обратное — <code>DESC</code> (descending, по убыванию).</p>
<pre>SELECT id, amount
FROM transactions
ORDER BY amount DESC;</pre>
<p>Первая строка — самая большая сумма. Почти все отчёты «топ» — это <code>DESC</code>.</p>

<p>Если нужно от дешёвого к дорогому, уберите <code>DESC</code> или напишите <code>ASC</code>:</p>
<pre>ORDER BY amount ASC</pre>

<p>Иногда два критерия: сначала город, в одном городе — имя.</p>
<pre>SELECT name, city
FROM customers
ORDER BY city, name;</pre>
<p>SQL сначала ставит по <code>city</code>. Если город одинаковый — смотрит на <code>name</code>. Направления могут быть разными: <code>ORDER BY city ASC, amount DESC</code>.</p>

<p>Если сказали «самые большие 3», сначала порядок, потом ограничение:</p>
<pre>SELECT id, amount
FROM transactions
ORDER BY amount DESC
LIMIT 3;</pre>
<p>Если поставить <code>LIMIT 3</code> без сортировки, могут выйти случайные 3 строки. Сначала кто первый, потом сколько.</p>

<p>Часто вместе идут фильтр + без повторов + порядок. Вспомните <code>WHERE</code>, <code>DISTINCT</code>, <code>AS</code> из прошлых уроков:</p>
<pre>SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;</pre>
<p>Сначала условие, потом убрать повторы, потом по возрастанию. Столбец называется <code>id</code> из‑за <code>AS id</code>.</p>

<p>Если в упражнении сказано «порядок строк проверяется» — не забудьте <code>ORDER BY</code>. Верные столбцы, неверный порядок — это ошибка.</p>
""",
    },
    "bir-nechta-shart": {
        "en": """
<p>In real life one condition is rarely enough. “Toshkent <em>and</em> the name starts with A”, “Toshkent <em>or</em> Samarqand”. This is where <code>AND</code> and <code>OR</code> come in.</p>

<p><code>AND</code> is a strict parent: <strong>everything</strong> must be true.</p>
<pre>SELECT * FROM customers
WHERE city = 'Toshkent' AND name LIKE 'A%';</pre>
<p>An Ali who doesn’t live in Toshkent will not appear. A Toshkent resident whose name doesn’t start with A will not appear either.</p>

<p><code>OR</code> is softer: <strong>one</strong> true condition is enough.</p>
<pre>SELECT * FROM customers
WHERE city = 'Toshkent' OR city = 'Samarqand';</pre>
<p>A shorter path: <code>city IN ('Toshkent', 'Samarqand')</code>. A list is easier to read.</p>

<p>Now a trap. If you skip parentheses, SQL decides “who comes first” on its own and may bring people you didn’t expect.</p>
<pre>WHERE city = 'Toshkent' AND (name LIKE 'A%' OR name LIKE 'M%')</pre>
<p>This means: A or M in Toshkent. Without parentheses you might get “Toshkent and A” <em>or</em> “name starts with M — any city”. Read it out loud, then add parentheses.</p>

<p><code>LIKE</code> is a text search. Two symbols:</p>
<ul>
  <li><code>%</code> — anything, even nothing: <code>'A%'</code> starts with A, <code>'%ov'</code> ends with ov, <code>'%ali%'</code> contains ali</li>
  <li><code>_</code> — exactly one character: <code>'_oshkent'</code> can match Toshkent</li>
</ul>
<p>If codes are separated by spaces (for example <code>ACNE DIAB100</code>), the code can sit at the <em>start</em> of the row or <em>after a space</em>. Cover both:</p>
<pre>WHERE conditions LIKE 'DIAB1%'
   OR conditions LIKE '% DIAB1%'</pre>
<p>Note: in <code>'% DIAB1%'</code> there is a <strong>space</strong> after <code>%</code>. Then something like <code>XDIAB1</code> will not match by accident. <code>DIAB100</code> matches (it starts with <code>DIAB1</code>), <code>DIAB201</code> does not.</p>

<p>Upper/lower case can matter in some databases. In our exercises write the sample exactly.</p>

<p>A money range:</p>
<pre>WHERE amount BETWEEN 10000 AND 50000</pre>
<p>Both 10000 and 50000 are included. “From … to …, including the edges.”</p>

<p>Advice: first try one condition; if it works, add the second. Don’t write a three-line WHERE immediately and then sit wondering “why is it empty?”</p>
""",
        "ru": """
<p>В жизни одного условия почти никогда не хватает. «Toshkent <em>и</em> имя на A», «Toshkent <em>или</em> Samarqand». Здесь входят <code>AND</code> и <code>OR</code>.</p>

<p><code>AND</code> — строгий родитель: должно быть верно <strong>всё</strong>.</p>
<pre>SELECT * FROM customers
WHERE city = 'Toshkent' AND name LIKE 'A%';</pre>
<p>Ali, который не живёт в Toshkent, не появится. Житель Toshkent, чьё имя не начинается на A, тоже не появится.</p>

<p><code>OR</code> мягче: достаточно, чтобы было верно <strong>одно</strong>.</p>
<pre>SELECT * FROM customers
WHERE city = 'Toshkent' OR city = 'Samarqand';</pre>
<p>Короче: <code>city IN ('Toshkent', 'Samarqand')</code>. Список читать легче.</p>

<p>Теперь ловушка. Без скобок SQL сам решает «кто первый» и может принести людей, которых вы не ждали.</p>
<pre>WHERE city = 'Toshkent' AND (name LIKE 'A%' OR name LIKE 'M%')</pre>
<p>Это: в Toshkent имена на A или M. Без скобок может получиться «Toshkent и A» <em>или</em> «имя на M — любой город». Прочитайте вслух, потом поставьте скобки.</p>

<p><code>LIKE</code> — поиск по тексту. Два символа:</p>
<ul>
  <li><code>%</code> — что угодно, даже ничего: <code>'A%'</code> начинается с A, <code>'%ov'</code> заканчивается на ov, <code>'%ali%'</code> внутри есть ali</li>
  <li><code>_</code> — ровно один символ: <code>'_oshkent'</code> может подойти к Toshkent</li>
</ul>
<p>Если коды разделены пробелом (например <code>ACNE DIAB100</code>), код может стоять в <em>начале</em> строки или <em>после пробела</em>. Покрыть оба случая:</p>
<pre>WHERE conditions LIKE 'DIAB1%'
   OR conditions LIKE '% DIAB1%'</pre>
<p>Внимание: в <code>'% DIAB1%'</code> после <code>%</code> есть <strong>пробел</strong>. Тогда ложное совпадение вроде <code>XDIAB1</code> не пройдёт. <code>DIAB100</code> подходит (начинается с <code>DIAB1</code>), <code>DIAB201</code> — нет.</p>

<p>Регистр в некоторых базах важен. В наших упражнениях пишите образец точно.</p>

<p>Диапазон денег:</p>
<pre>WHERE amount BETWEEN 10000 AND 50000</pre>
<p>И 10000, и 50000 входят. «От … до …, включая края.»</p>

<p>Совет: сначала проверьте одно условие, если работает — добавьте второе. Не пишите сразу трёхстрочный WHERE и потом не сидите с вопросом «почему пусто?»</p>
""",
    },
    "count": {
        "en": """
<p>An analyst’s first question is often “how many?”. Not a list — a <strong>number</strong>. That’s what <code>COUNT</code> is for.</p>

<p>The simplest:</p>
<pre>SELECT COUNT(*) AS total FROM customers;</pre>
<p>How many rows are in the table — that’s it. <code>AS total</code> names the result. Without a name the column comes out “nameless”; an exercise may expect <code>total</code> or <code>cnt</code>.</p>

<p>Only the number of people in Toshkent — first filter, then count:</p>
<pre>SELECT COUNT(*) AS total
FROM customers
WHERE city = 'Toshkent';</pre>
<p>There is no <code>GROUP BY</code> here. One question, one number.</p>

<p>Tell the three COUNTs apart, or NULL will trick you:</p>
<ul>
  <li><code>COUNT(*)</code> — rows; even if there is NULL, the row still counts</li>
  <li><code>COUNT(city)</code> — only rows where city is filled (not NULL)</li>
  <li><code>COUNT(DISTINCT city)</code> — how many <em>different</em> cities</li>
</ul>
<p>5 customers, 2 in Toshkent, 2 in Samarqand, 1 with an empty city. <code>COUNT(*)</code> = 5. <code>COUNT(city)</code> = 4. <code>COUNT(DISTINCT city)</code> = 2.</p>

<p>We won’t fully do “a separate number for each city” today — that’s the next lesson, <code>GROUP BY</code>. Today: one question → one COUNT.</p>
""",
        "ru": """
<p>Первый вопрос аналитика часто «сколько?». Не список, а <strong>число</strong>. Для этого <code>COUNT</code>.</p>

<p>Самый простой:</p>
<pre>SELECT COUNT(*) AS total FROM customers;</pre>
<p>Сколько строк в таблице — вот и всё. <code>AS total</code> даёт имя результату. Без имени столбец выйдет «безымянным»; в упражнении могут ждать <code>total</code> или <code>cnt</code>.</p>

<p>Только число жителей Toshkent — сначала фильтр, потом подсчёт:</p>
<pre>SELECT COUNT(*) AS total
FROM customers
WHERE city = 'Toshkent';</pre>
<p>Здесь нет <code>GROUP BY</code>. Один вопрос, одно число.</p>

<p>Различайте три COUNT, иначе NULL вас обманет:</p>
<ul>
  <li><code>COUNT(*)</code> — строки; даже если есть NULL, строка считается</li>
  <li><code>COUNT(city)</code> — только те, где город заполнен (не NULL)</li>
  <li><code>COUNT(DISTINCT city)</code> — сколько <em>разных</em> городов</li>
</ul>
<p>5 клиентов, 2 в Toshkent, 2 в Samarqand, у 1 город пустой. <code>COUNT(*)</code> = 5. <code>COUNT(city)</code> = 4. <code>COUNT(DISTINCT city)</code> = 2.</p>

<p>Сегодня мы не делаем полностью «отдельное число для каждого города» — это следующий урок, <code>GROUP BY</code>. Сегодня: один вопрос → один COUNT.</p>
""",
    },
    "sum-va-avg": {
        "en": """
<p>After “how many?” comes “how much money?”. We don’t add rows by hand. <code>SUM</code> adds, <code>AVG</code> takes the average. <code>MIN</code> and <code>MAX</code> show the edges.</p>
<pre>SELECT SUM(amount) AS total FROM transactions;</pre>
<p>The total of all payments. If they ask for debit separately, we add <code>WHERE</code> — first the needed rows, then the sum:</p>
<pre>SELECT SUM(amount) AS total
FROM transactions
WHERE transaction_type = 'debit';</pre>

<p>Average check:</p>
<pre>SELECT AVG(amount) AS avg_amount FROM transactions;</pre>
<p>Be honest about averages: one huge payment can send the average into the sky. Reports sometimes need a median for a “typical check” — that’s statistics. In SQL, first make SUM/AVG reliable.</p>

<p>NULL matters here too: SUM and AVG usually skip NULL cells; they don’t treat them as 0. “Unknown” and “zero soum” are different things.</p>
<pre>SELECT MIN(amount) AS eng_kichik, MAX(amount) AS eng_katta
FROM transactions;</pre>
<p>Two aggregates in one query — allowed. It returns everything as a single row.</p>

<p>Sometimes the thing you add is not a column but an <em>expression</em>. For example session minutes = out − in:</p>
<pre>SELECT SUM(out_time - in_time) AS total_time
FROM EmployeeAttendance;</pre>
<p>Inside <code>SUM</code>, <code>out_time - in_time</code> is the difference per row, then the total. Still no <code>GROUP BY</code>: the whole table → one number. “Per employee / per day” is the next lesson.</p>

<p>In exercises put the requested column name with <code>AS</code>. The right number with the wrong name — the system may reject it. Fussy, but in a report the heading matters too.</p>
""",
        "ru": """
<p>После «сколько?» приходит «сколько денег?». Строки руками не складываем. <code>SUM</code> суммирует, <code>AVG</code> берёт среднее. <code>MIN</code> и <code>MAX</code> показывают края.</p>
<pre>SELECT SUM(amount) AS total FROM transactions;</pre>
<p>Сумма всех платежей. Если отдельно просят debit, добавляем <code>WHERE</code> — сначала нужные строки, потом сумма:</p>
<pre>SELECT SUM(amount) AS total
FROM transactions
WHERE transaction_type = 'debit';</pre>

<p>Средний чек:</p>
<pre>SELECT AVG(amount) AS avg_amount FROM transactions;</pre>
<p>Про среднее честно: один огромный платёж задирает среднее в небеса. В отчёте иногда нужна медиана для «типичного чека» — это статистика. В SQL сначала сделайте SUM/AVG надёжными.</p>

<p>NULL здесь тоже важен: SUM и AVG обычно отбрасывают ячейки NULL и не считают их нулём. «Неизвестно» и «ноль сум» — разное.</p>
<pre>SELECT MIN(amount) AS eng_kichik, MAX(amount) AS eng_katta
FROM transactions;</pre>
<p>Два агрегата в одном запросе — можно. Всё вернётся одной строкой.</p>

<p>Иногда суммируют не столбец, а <em>выражение</em>. Например минуты сессии = выход − вход:</p>
<pre>SELECT SUM(out_time - in_time) AS total_time
FROM EmployeeAttendance;</pre>
<p>Внутри <code>SUM</code> <code>out_time - in_time</code> — разница по каждой строке, потом сумма. Пока нет <code>GROUP BY</code>: вся таблица → одно число. «По сотруднику / по дню» — следующий урок.</p>

<p>В упражнении поставьте запрошенное имя столбца через <code>AS</code>. Верное число, неверное имя — система может не принять. Капризно, но в отчёте заголовок тоже важен.</p>
""",
    },
    "group-by-asoslari": {
        "en": """
<p>Until now we got one number for one question: how many in total, how much in total. Now the question changes: how many payments <em>for each customer</em>? How many people <em>for each city</em>?</p>
<p>That’s grouping. <code>GROUP BY</code>. Imagine stacking rows on a table into piles: “this customer”, “that customer”. Then we count or add inside each pile.</p>
<pre>SELECT customer_id, COUNT(*) AS cnt
FROM transactions
GROUP BY customer_id;</pre>
<p>In the result each <code>customer_id</code> is one row. Next to it is that person’s payment count. If you need a sum, use <code>SUM(amount) AS total</code> instead of <code>COUNT</code>.</p>

<p>A question like subscriber counts: how many rows per <code>user_id</code>, then sort:</p>
<pre>SELECT user_id, COUNT(*) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;</pre>
<p><code>ORDER BY</code> still works after grouping — it sorts the result rows.</p>

<p>If a repeated value must be counted once — <code>COUNT(DISTINCT ...)</code>:</p>
<pre>SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;</pre>
<p>If one subject is written on two departments, plain <code>COUNT(*)</code> counts twice; <code>COUNT(DISTINCT subject_id)</code> — one subject.</p>

<p>Golden rule, this is where many people fall: a plain column in <code>SELECT</code> (not COUNT/SUM) must also be in <code>GROUP BY</code>. Otherwise SQL asks: “Which amount? There are 6 different amounts in the pile.”</p>
<p>Wrong idea: <code>SELECT customer_id, amount, COUNT(*)</code> — amount is not grouped. Right: group key + a calculation.</p>

<p>Two more words. <code>WHERE</code> drops rows <em>before</em> piling: for example, only debit first. <code>HAVING</code> says <em>after</em> piling “this pile is too small, drop it”.</p>
<pre>SELECT customer_id, COUNT(*) AS cnt
FROM transactions
GROUP BY customer_id
HAVING COUNT(*) &gt; 5;</pre>
<p>Only those with more than 5 payments. <code>WHERE COUNT(*) &gt; 5</code> usually doesn’t work — the count doesn’t exist yet; there is no COUNT at row level.</p>
<p>We’ll revisit HAVING more slowly in the next module. Today: GROUP BY = “for each one”. In SELECT: the key and COUNT/SUM. Name it with <code>AS</code>.</p>
""",
        "ru": """
<p>До сих пор на один вопрос мы получали одно число: всего сколько, всего на какую сумму. Теперь вопрос другой: сколько платежей <em>у каждого клиента</em>? Сколько людей <em>в каждом городе</em>?</p>
<p>Это группировка. <code>GROUP BY</code>. Представьте, что строки на столе сложили кучками: «этот клиент», «тот клиент». Потом в каждой кучке считаем или складываем.</p>
<pre>SELECT customer_id, COUNT(*) AS cnt
FROM transactions
GROUP BY customer_id;</pre>
<p>В результате каждый <code>customer_id</code> — одна строка. Рядом — число платежей этого человека. Если нужна сумма, вместо <code>COUNT</code> пишите <code>SUM(amount) AS total</code>.</p>

<p>Вопрос вроде числа подписчиков: сколько строк на каждый <code>user_id</code>, потом сортировка:</p>
<pre>SELECT user_id, COUNT(*) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;</pre>
<p><code>ORDER BY</code> работает и после группировки — сортирует строки результата.</p>

<p>Если повтор нужно посчитать один раз — <code>COUNT(DISTINCT ...)</code>:</p>
<pre>SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;</pre>
<p>Если один предмет записан на две кафедры, обычный <code>COUNT(*)</code> посчитает дважды; <code>COUNT(DISTINCT subject_id)</code> — один предмет.</p>

<p>Золотое правило, здесь многие падают: обычный столбец в <code>SELECT</code> (не COUNT/SUM) должен быть и в <code>GROUP BY</code>. Иначе SQL спросит: «Какой amount? В кучке 6 разных amount.»</p>
<p>Плохая идея: <code>SELECT customer_id, amount, COUNT(*)</code> — amount не сгруппирован. Правильно: ключ группы + расчёт.</p>

<p>Ещё два слова. <code>WHERE</code> отбрасывает строки <em>до</em> кучек: например, сначала только debit. <code>HAVING</code> говорит <em>после</em> группировки «эта кучка слишком маленькая, выкинь».</p>
<pre>SELECT customer_id, COUNT(*) AS cnt
FROM transactions
GROUP BY customer_id
HAVING COUNT(*) &gt; 5;</pre>
<p>Только те, у кого больше 5 платежей. <code>WHERE COUNT(*) &gt; 5</code> обычно не работает — подсчёта ещё нет, на уровне строки COUNT нет.</p>
<p>HAVING медленнее разберём в следующем модуле. Сегодня: GROUP BY = «для каждого». В SELECT — ключ и COUNT/SUM. Имя дайте через <code>AS</code>.</p>
""",
    },
    "having-nima": {
        "en": """
<p>In the previous module we grouped. Now we choose the group itself. Don’t mix people up: dropping a row is <code>WHERE</code>. “Do we need this group?” is <code>HAVING</code>.</p>

<p>A real question: “Groups with at least N members.” First you count per group, then you drop the small ones. Counting happens after grouping, so HAVING. The table and the threshold in the exercise may differ — the idea is the same.</p>
<p>Bank example: cities with at least 2 customers.</p>
<pre>SELECT city, COUNT(*) AS cnt
FROM customers
WHERE city &lt;&gt; 'Buxoro'
GROUP BY city
HAVING COUNT(*) &gt;= 2;</pre>
<p>First we ignore Buxoro entirely (row filter), then among remaining cities “at least 2 customers” (group filter).</p>
<p>Memorize the writing order: SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY. Say it out loud as you write — you won’t get mixed up.</p>
<p>Rule: a COUNT, SUM, AVG condition — HAVING. A plain column condition — WHERE.</p>
""",
        "ru": """
<p>В прошлом модуле мы группировали. Теперь выбираем саму группу. Людей не путайте: отбросить строку — <code>WHERE</code>. «Нужна ли нам эта группа?» — <code>HAVING</code>.</p>

<p>Житейский вопрос: «Группы, в которых хотя бы N участников.» Сначала считаете по группе, потом мелкие отбрасываете. Подсчёт после группировки — поэтому HAVING. Таблица и порог в упражнении могут быть другими — идея та же.</p>
<p>Банковский пример: города минимум с 2 клиентами.</p>
<pre>SELECT city, COUNT(*) AS cnt
FROM customers
WHERE city &lt;&gt; 'Buxoro'
GROUP BY city
HAVING COUNT(*) &gt;= 2;</pre>
<p>Сначала Buxoro вообще не учитываем (фильтр строк), потом среди оставшихся городов «минимум 2 клиента» (фильтр групп).</p>
<p>Запомните порядок записи: SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY. Произносите вслух, пока пишете — не запутаетесь.</p>
<p>Правило: условие на COUNT, SUM, AVG — HAVING. Условие на обычный столбец — WHERE.</p>
""",
    },
    "group-by-kop-ustun": {
        "en": """
<p>Sometimes a group is not one column. Not “each actor”, but “actor and director as a pair”. Like pivoting two columns together in Excel.</p>
<pre>SELECT customer_id, transaction_type, COUNT(*) AS c
FROM transactions
GROUP BY customer_id, transaction_type;</pre>
<p>Each customer + type pair has its own count. If you group by <code>customer_id</code> and leave <code>transaction_type</code> out, SQL asks the same question again: which type?</p>
<p>Every “plain” column in SELECT must stand in GROUP BY. COUNT is a calculation, not a group key.</p>

<p>If you only need pairs that appear at least N times — group, count, then <code>HAVING</code>:</p>
<pre>SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) &gt;= 3;</pre>
<p>Two keys in GROUP BY. The count is inside the pair. Small pairs are dropped with HAVING.</p>

<p>At work: city + channel, month + product. Say the question as “for each X and Y” — two keys appear.</p>
""",
        "ru": """
<p>Иногда группа — не один столбец. Не «каждый актёр», а «пара актёр и режиссёр». Как сводная по двум столбцам сразу в Excel.</p>
<pre>SELECT customer_id, transaction_type, COUNT(*) AS c
FROM transactions
GROUP BY customer_id, transaction_type;</pre>
<p>У каждой пары клиент + тип — своё число. Если сгруппировать по <code>customer_id</code> и не взять <code>transaction_type</code>, SQL снова спросит: какой тип?</p>
<p>Каждый «обычный» столбец в SELECT должен стоять в GROUP BY. COUNT — это расчёт, не ключ группы.</p>

<p>Если нужны только пары, которые встречаются минимум N раз — сгруппируйте, посчитайте, потом <code>HAVING</code>:</p>
<pre>SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) &gt;= 3;</pre>
<p>Два ключа в GROUP BY. Подсчёт внутри пары. Мелкие пары отбрасывает HAVING.</p>

<p>На работе: город + канал, месяц + продукт. Скажите вопрос как «для каждого X и Y» — появятся два ключа.</p>
""",
    },
    "agregat-filtr": {
        "en": """
<p>Sometimes a question doesn’t fit in one query. For example: “The largest among numbers that appear only once.” First you count, then filter, then MAX.</p>
<p>Think in steps; don’t write pretty code immediately.</p>
<ol>
  <li>How many times does each value appear? Group and count</li>
  <li>Keep only those that appeared once</li>
  <li>The largest among what’s left</li>
</ol>
<p>Step 3 is an outer query: the inner result becomes a small table. In the bank: the largest among amounts that appear only once.</p>
<pre>SELECT MAX(amount) AS amount
FROM (
  SELECT amount FROM transactions
  GROUP BY amount
  HAVING COUNT(*) = 1
) AS t;</pre>
<p>The inner part — “lonely numbers”. The outer — the largest of them. <code>AS t</code> names the inner table; some systems reject it without a name.</p>
<p>Later we’ll write the same thing more clearly with <code>WITH</code> (CTE). For now the idea: split a big question into small ones.</p>
""",
        "ru": """
<p>Иногда вопрос не помещается в один запрос. Например: «Самое большое среди чисел, которые встретились только один раз.» Сначала считаете, потом фильтр, потом MAX.</p>
<p>Думайте по шагам, сразу красивый код не пишите.</p>
<ol>
  <li>Сколько раз каждое значение? Группировка и подсчёт</li>
  <li>Оставить только встретившиеся один раз</li>
  <li>Самое большое среди оставшихся</li>
</ol>
<p>3-й шаг — внешний запрос: результат внутри становится маленькой таблицей. В банке: самое большое среди сумм, которые встретились один раз.</p>
<pre>SELECT MAX(amount) AS amount
FROM (
  SELECT amount FROM transactions
  GROUP BY amount
  HAVING COUNT(*) = 1
) AS t;</pre>
<p>Внутренняя часть — «одинокие числа». Внешняя — самое большое из них. <code>AS t</code> — имя внутренней таблицы; некоторые системы без имени не принимают.</p>
<p>Позже то же самое напишем понятнее через <code>WITH</code> (CTE). Сейчас идея: большой вопрос режьте на маленькие.</p>
""",
    },
    "inner-join": {
        "en": """
<p>Until now, one table. In life the name is in one place and the payment in another. In Excel you would have used VLOOKUP. In SQL that’s <code>JOIN</code>.</p>

<p>What connects them? A shared key. On a payment <code>customer_id = 1</code>, in customers <code>id = 1</code> — that’s Ali.</p>
<p><strong>INNER JOIN</strong> means: only matches. A customer with no payment disappears from this query. A payment whose customer was deleted usually disappears too. Only the intersection.</p>
<pre>SELECT c.name, t.amount
FROM customers AS c
INNER JOIN transactions AS t
  ON c.id = t.customer_id;</pre>
<p><code>AS c</code> and <code>AS t</code> are short nicknames, so you don’t get tired. <code>ON</code> is “which columns mean the same person.”</p>
<p>Dropping the word <code>INNER</code> and writing only <code>JOIN</code> often means the same thing.</p>
<p>Next lesson we’ll ask: do we also need customers without payments? Then INNER is not enough.</p>
""",
        "ru": """
<p>До сих пор одна таблица. В жизни имя в одном месте, платёж в другом. В Excel вы бы сделали VLOOKUP. В SQL это — <code>JOIN</code>.</p>

<p>Что связывает? Общий ключ. В платеже <code>customer_id = 1</code>, в клиентах <code>id = 1</code> — это Ali.</p>
<p><strong>INNER JOIN</strong> значит: только совпавшие. Клиент без платежа в этом запросе пропадёт. Платёж, чей клиент удалён, обычно тоже не выйдет. Только пересечение.</p>
<pre>SELECT c.name, t.amount
FROM customers AS c
INNER JOIN transactions AS t
  ON c.id = t.customer_id;</pre>
<p><code>AS c</code> и <code>AS t</code> — короткие прозвища, чтобы не уставать. <code>ON</code> — «какие столбцы означают одного человека».</p>
<p>Слово <code>INNER</code> часто опускают и пишут просто <code>JOIN</code> — смысл тот же.</p>
<p>В следующем уроке спросим: нужны ли клиенты без платежей? Тогда INNER не хватит.</p>
""",
    },
    "left-join": {
        "en": """
<p>The manager: “All customers. If there is a payment, write it; if not, still keep them on the list.” That’s not INNER. That’s <code>LEFT JOIN</code>.</p>
<p>The left table is the main one — “drop nobody”. The right table is extra. If there is no match, the right side becomes <code>NULL</code>; the name on the left stays.</p>
<pre>SELECT c.name, t.id
FROM customers AS c
LEFT JOIN transactions AS t
  ON c.id = t.customer_id;</pre>
<p>For a person with no payment, <code>t.id</code> comes out empty (NULL). In an inner JOIN they weren’t there at all.</p>

<p>Exactly through that NULL we find “people who never paid”:</p>
<pre>SELECT c.name
FROM customers AS c
LEFT JOIN transactions AS t ON c.id = t.customer_id
WHERE t.customer_id IS NULL;</pre>
<p>The right key is NULL — meaning no pair was found. This is a classic method. Memorize it; interviews ask it too.</p>
<p>Which table is on the left matters. Swap the left side and the question changes too.</p>
""",
        "ru": """
<p>Руководитель: «Все клиенты. Если платёж есть — запишите, если нет — всё равно оставьте в списке.» Это не INNER. Это — <code>LEFT JOIN</code>.</p>
<p>Левая таблица — основная, «никого не выкидывай». Правая — дополнительная. Если пары нет, справа будет <code>NULL</code>, имя слева сохранится.</p>
<pre>SELECT c.name, t.id
FROM customers AS c
LEFT JOIN transactions AS t
  ON c.id = t.customer_id;</pre>
<p>У человека без платежа <code>t.id</code> выйдет пустым (NULL). Во внутреннем JOIN его вообще не было.</p>

<p>Именно через этот NULL находим «тех, кто никогда не платил»:</p>
<pre>SELECT c.name
FROM customers AS c
LEFT JOIN transactions AS t ON c.id = t.customer_id
WHERE t.customer_id IS NULL;</pre>
<p>Правый ключ NULL — значит пара не нашлась. Классический приём. Запомните, на собеседовании тоже спрашивают.</p>
<p>Какая таблица слева — важно. Поменяете левую — изменится и вопрос.</p>
""",
    },
    "join-null": {
        "en": """
<p>You did a LEFT JOIN and now want to filter “bonus under 1000 or no bonus at all”. There’s a trap here.</p>
<p><code>WHERE bonus &lt; 1000</code> usually swallows the NULL row. Because “is unknown smaller than 1000?” — SQL does not say yes. You wanted “people with no bonus” too.</p>
<p>One fix is to read NULL as 0. Bank example: all customers on the left, payments on the right; “amount under 20 000 or no payment”:</p>
<pre>SELECT c.name, t.amount
FROM customers AS c
LEFT JOIN transactions AS t ON c.id = t.customer_id
WHERE COALESCE(t.amount, 0) &lt; 20000;</pre>
<p><code>COALESCE</code> — “take the first non-NULL”. No bonus becomes 0, and 0 is smaller than 1000 — the row stays. Or write it openly: <code>bonus &lt; 1000 OR bonus IS NULL</code>.</p>
<p>When you write WHERE after a JOIN, think about NULL for five seconds. A lot of “why did people disappear?” comes from here.</p>
""",
        "ru": """
<p>Сделали LEFT JOIN и теперь хотите фильтр «бонус меньше 1000 или бонуса вообще нет». Здесь ловушка.</p>
<p><code>WHERE bonus &lt; 1000</code> обычно проглатывает строку с NULL. Потому что «неизвестно меньше 1000?» — SQL не говорит «да». А вы хотели и тех, у кого бонуса нет.</p>
<p>Одно решение — читать NULL как 0. Банк: слева все клиенты, справа платежи; «сумма меньше 20 000 или платежа нет»:</p>
<pre>SELECT c.name, t.amount
FROM customers AS c
LEFT JOIN transactions AS t ON c.id = t.customer_id
WHERE COALESCE(t.amount, 0) &lt; 20000;</pre>
<p><code>COALESCE</code> — «возьми первое не NULL». Нет бонуса → 0, 0 меньше 1000 — строка остаётся. Или напишите явно: <code>bonus &lt; 1000 OR bonus IS NULL</code>.</p>
<p>Когда после JOIN пишете WHERE, пять секунд подумайте про NULL. Много «почему люди пропали?» растёт отсюда.</p>
""",
    },
    "subquery-where": {
        "en": """
<p>Sometimes the answer lives inside another query. “Payments more expensive than average” — first you find the average, then you compare. The inner query sits in parentheses. People call this a subquery; don’t be scared: it’s just a query inside a query.</p>
<pre>SELECT id, amount
FROM transactions
WHERE amount &gt; (SELECT AVG(amount) FROM transactions);</pre>
<p>The inner part returns one number — the average. The outer compares each row to that number.</p>
<p>It can also be a list:</p>
<pre>SELECT name FROM customers
WHERE id NOT IN (SELECT customer_id FROM transactions);</pre>
<p>Inner: IDs that placed an order. Outer: those not on that list. Reminder: if the inner list has NULL, <code>NOT IN</code> can give a weird empty result. Then LEFT JOIN … IS NULL or NOT EXISTS is calmer.</p>
<p>Read a subquery as “first answer this question, then use it”.</p>
""",
        "ru": """
<p>Иногда ответ живёт внутри другого запроса. «Платежи дороже среднего» — сначала находите среднее, потом сравниваете. Внутренний запрос стоит в скобках. Это называют subquery, не пугайтесь: просто запрос внутри запроса.</p>
<pre>SELECT id, amount
FROM transactions
WHERE amount &gt; (SELECT AVG(amount) FROM transactions);</pre>
<p>Внутренняя часть возвращает одно число — среднее. Внешняя сравнивает каждую строку с этим числом.</p>
<p>Может быть и список:</p>
<pre>SELECT name FROM customers
WHERE id NOT IN (SELECT customer_id FROM transactions);</pre>
<p>Внутри: ID тех, кто делал заказ. Снаружи: тех, кого нет в этом списке. Напомню: если во внутреннем списке есть NULL, <code>NOT IN</code> может странно вернуть пустоту. Тогда спокойнее LEFT JOIN … IS NULL или NOT EXISTS.</p>
<p>Подзапрос читайте как «сначала ответь на этот вопрос, потом используй».</p>
""",
    },
    "subquery-from": {
        "en": """
<p>You can put an inner query not only in WHERE but also in FROM. Meaning: “First build a small table, then SELECT from it.”</p>
<pre>SELECT MAX(amount) AS amount
FROM (
  SELECT amount FROM transactions
  GROUP BY amount
  HAVING COUNT(*) = 1
) AS singles;</pre>
<p>What’s in parentheses is a temporary table. Always give it a name — <code>singles</code>. Outer SQL reads it like an ordinary table.</p>
<p>If it gets messy, the next lesson’s <code>WITH</code> lifts that same thing to the top and it becomes easier to read. The idea is the same: step by step.</p>
""",
        "ru": """
<p>Внутренний запрос можно ставить не только в WHERE, но и в FROM. Смысл: «Сначала собери маленькую таблицу, потом сделай из неё SELECT.»</p>
<pre>SELECT MAX(amount) AS amount
FROM (
  SELECT amount FROM transactions
  GROUP BY amount
  HAVING COUNT(*) = 1
) AS singles;</pre>
<p>То, что в скобках — временная таблица. Ей обязательно дайте имя — <code>singles</code>. Внешний SQL читает её как обычную таблицу.</p>
<p>Если станет запутанно, <code>WITH</code> из следующего урока вынесет то же самое наверх, читать станет легче. Идея одна: шаг за шагом.</p>
""",
    },
    "exists-in": {
        "en": """
<p>Two close questions: “Is this value in a list?” and “Is there any related row for this customer?”</p>
<p><code>IN</code> is a list. By hand or from a subquery:</p>
<pre>WHERE city IN ('Toshkent', 'Buxoro')
WHERE id IN (SELECT customer_id FROM transactions)</pre>
<p><code>EXISTS</code> — “does the inner query return at least one row?” The column doesn’t matter, so people often write <code>SELECT 1</code>:</p>
<pre>SELECT c.name
FROM customers AS c
WHERE EXISTS (
  SELECT 1 FROM transactions AS t
  WHERE t.customer_id = c.id
);</pre>
<p>People who have a payment. The opposite: <code>NOT EXISTS</code> — people with no payment.</p>
<p>When which? A short list — IN. “Is there a related record?” — EXISTS. If you’re afraid of NULL, use NOT EXISTS or LEFT JOIN instead of NOT IN.</p>
""",
        "ru": """
<p>Два близких вопроса: «Есть ли это значение в списке?» и «Есть ли у этого клиента хотя бы одна связанная строка?»</p>
<p><code>IN</code> — список. Вручную или из подзапроса:</p>
<pre>WHERE city IN ('Toshkent', 'Buxoro')
WHERE id IN (SELECT customer_id FROM transactions)</pre>
<p><code>EXISTS</code> — «внутренний запрос вернул хотя бы одну строку?» Столбец не важен, поэтому часто пишут <code>SELECT 1</code>:</p>
<pre>SELECT c.name
FROM customers AS c
WHERE EXISTS (
  SELECT 1 FROM transactions AS t
  WHERE t.customer_id = c.id
);</pre>
<p>Те, у кого есть платёж. Наоборот: <code>NOT EXISTS</code> — у кого платежа нет.</p>
<p>Когда что? Короткий список — IN. «Есть связанная запись?» — EXISTS. Если боитесь NULL, вместо NOT IN берите NOT EXISTS или LEFT JOIN.</p>
""",
    },
    "cte-asoslari": {
        "en": """
<p>When a query gets long, nested parentheses become unreadable. As a teacher I’ll say: SQL you can’t understand is bad SQL, even if it works.</p>
<p>With <code>WITH</code> we name a step. That’s called a CTE (Common Table Expression). Temporary, only for this query.</p>
<pre>WITH yolgiz AS (
  SELECT amount FROM transactions
  GROUP BY amount
  HAVING COUNT(*) = 1
)
SELECT MAX(amount) AS amount FROM yolgiz;</pre>
<p>First we called “lonely numbers” <code>singles</code>. Then a plain SELECT. Same work as a subquery in FROM, but the story reads top to bottom.</p>
<p>At work: first cleaned payments, then a group, then a report. Each step — its own WITH.</p>
""",
        "ru": """
<p>Когда запрос длиннеет, вложенные скобки перестают читаться. Как преподаватель скажу: SQL, который нельзя понять — плохой SQL, даже если он правильный.</p>
<p>Через <code>WITH</code> мы даём шагу имя. Это CTE (Common Table Expression). Временно, только для этого запроса.</p>
<pre>WITH yolgiz AS (
  SELECT amount FROM transactions
  GROUP BY amount
  HAVING COUNT(*) = 1
)
SELECT MAX(amount) AS amount FROM yolgiz;</pre>
<p>Сначала «одинокие числа» назвали <code>singles</code>. Потом обычный SELECT. Работа та же, что у подзапроса в FROM, но история читается сверху вниз.</p>
<p>На работе: сначала очищенные платежи, потом группа, потом отчёт. Каждый шаг — свой WITH.</p>
""",
    },
    "cte-bir-nechta": {
        "en": """
<p>One WITH can hold several names. Comma-separated. The second can use the first — a chain.</p>
<pre>WITH a AS (
  SELECT city, COUNT(*) AS cnt FROM customers GROUP BY city
),
b AS (
  SELECT city FROM a WHERE cnt &gt;= 2
)
SELECT * FROM b;</pre>
<p>First we counted, then we filtered. You can also turn HAVING into an ordinary WHERE this way — sometimes easier to read.</p>
<p><code>WITH</code> is written once. At the end there must be a main SELECT. Remember: CTEs are not stored in the database, only for this run.</p>
""",
        "ru": """
<p>В одном WITH может быть несколько имён. Через запятую. Второй может использовать первый — цепочка.</p>
<pre>WITH a AS (
  SELECT city, COUNT(*) AS cnt FROM customers GROUP BY city
),
b AS (
  SELECT city FROM a WHERE cnt &gt;= 2
)
SELECT * FROM b;</pre>
<p>Сначала посчитали, потом отфильтровали. HAVING так можно превратить в обычный WHERE — иногда читать легче.</p>
<p><code>WITH</code> пишется один раз. В конце обязательно основной SELECT. Не забудьте: CTE в базу не сохраняются, только на этот запуск.</p>
""",
    },
    "cte-amal": {
        "en": """
<p>Let’s use a CTE for work, not for decoration. Grouping inside, filter outside:</p>
<pre>WITH j AS (
  SELECT customer_id, COUNT(*) AS c
  FROM transactions
  GROUP BY customer_id
)
SELECT customer_id
FROM j
WHERE c &gt;= 3;</pre>
<p>If something is wrong, first try only <code>SELECT * FROM j</code>. Does the step work? Then the outer filter. That’s how you debug — not the whole pig in one bite.</p>
<p>An analyst usually: 1) a clean fact CTE, 2) a KPI SELECT. A teammate who reads it will thank you.</p>
""",
        "ru": """
<p>Давайте применим CTE не «для красоты», а для работы. Группировка внутри, фильтр снаружи:</p>
<pre>WITH j AS (
  SELECT customer_id, COUNT(*) AS c
  FROM transactions
  GROUP BY customer_id
)
SELECT customer_id
FROM j
WHERE c &gt;= 3;</pre>
<p>Если ошибка, сначала попробуйте только <code>SELECT * FROM j</code>. Шаг работает? Потом внешний фильтр. Так и отлаживают — не всю свинью одним укусом.</p>
<p>Аналитик обычно: 1) чистый fact CTE, 2) KPI SELECT. Коллега, который это прочитает, скажет спасибо.</p>
""",
    },
    "case-when": {
        "en": """
<p>Excel had IF: if the condition is true, one thing, otherwise another. In SQL that’s <code>CASE</code>. It walks row by row, takes the first true condition, and doesn’t read the rest. If nothing matches — <code>ELSE</code>; if that’s missing too, NULL.</p>
<pre>SELECT id, amount,
  CASE
    WHEN amount &lt; 20000 THEN 'kichik'
    WHEN amount &lt; 50000 THEN 'orta'
    ELSE 'katta'
  END AS segment
FROM transactions;</pre>
<p>Order matters. If you don’t put “small” first, 10 thousand can fall into “medium”. Write the borders from the top or from the bottom, in sequence.</p>
<p>Don’t forget <code>END</code> — that’s where SQL’s IF finishes. The name is with <code>AS segment</code>.</p>
<p>The triangle example is the same IF: if the triangle inequality holds, Yes, otherwise No. Same logic.</p>
""",
        "ru": """
<p>В Excel был IF: условие истинно — одно, иначе другое. В SQL это — <code>CASE</code>. Идёт по строкам, берёт первое верное условие и остальное не читает. Если ничего не подошло — <code>ELSE</code>, если и его нет — NULL.</p>
<pre>SELECT id, amount,
  CASE
    WHEN amount &lt; 20000 THEN 'kichik'
    WHEN amount &lt; 50000 THEN 'orta'
    ELSE 'katta'
  END AS segment
FROM transactions;</pre>
<p>Порядок важен. Если «маленький» не поставить первым, 10 тысяч может попасть в «средний». Границы пишите сверху или снизу подряд.</p>
<p><code>END</code> не забудьте — здесь у SQL заканчивается IF. Имя через <code>AS segment</code>.</p>
<p>Пример с треугольником — тот же IF: неравенство сторон верно — Yes, иначе No. Логика одна.</p>
""",
    },
    "case-select": {
        "en": """
<p>We output CASE as a new column: bonus, yes/no, a flag. The table doesn’t change — only the result.</p>
<pre>SELECT id,
  CASE
    WHEN amount &gt;= 50000 THEN amount
    ELSE 0
  END AS katta_summa
FROM transactions;</pre>
<p>A matching payment keeps its amount, the others get zero. That’s a “report field”. Tomorrow if the rule changes, you change CASE and don’t touch the raw data.</p>
<p>Next step: put that CASE inside SUM and count how many. First understand the one-row logic.</p>
""",
        "ru": """
<p>CASE выводим как новый столбец: бонус, да/нет, флаг. Таблица не меняется — только результат.</p>
<pre>SELECT id,
  CASE
    WHEN amount &gt;= 50000 THEN amount
    ELSE 0
  END AS katta_summa
FROM transactions;</pre>
<p>Подходящий платёж оставляет свою сумму, остальные — ноль. Это «поле отчёта». Завтра правило другое — меняете CASE, сырые данные не трогаете.</p>
<p>Следующий шаг: этот CASE внутрь SUM и посчитать сколько. Сначала поймите логику на одной строке.</p>
""",
    },
    "case-agregat": {
        "en": """
<p>Now we turn CASE into a calculation. Close to COUNTIFS / SUMIF in Excel.</p>
<pre>SELECT transaction_type,
  SUM(CASE WHEN amount &gt;= 50000 THEN 1 ELSE 0 END) AS katta_soni,
  COUNT(*) AS jami
FROM transactions
GROUP BY transaction_type;</pre>
<p>For each type: how many are “large”, how many in total. Adding 1 and 0 is a counting trick.</p>
<p>Money works the same way:</p>
<pre>SUM(CASE WHEN transaction_type = 'debit' THEN amount ELSE 0 END) AS debit_sum</pre>
<p>In one query a debit total, next to it credit — like a pivot. The group key can be something else (city, month).</p>
<p>If you don’t want NULL, put ELSE 0. If you forget ELSE, non-matches are NULL; SUM may skip them — not the 0 you expected.</p>
""",
        "ru": """
<p>Теперь превращаем CASE в расчёт. Близко к COUNTIFS / SUMIF в Excel.</p>
<pre>SELECT transaction_type,
  SUM(CASE WHEN amount &gt;= 50000 THEN 1 ELSE 0 END) AS katta_soni,
  COUNT(*) AS jami
FROM transactions
GROUP BY transaction_type;</pre>
<p>Для каждого типа: сколько «крупных», сколько всего. Складывать 1 и 0 — трюк для подсчёта.</p>
<p>Деньги так же:</p>
<pre>SUM(CASE WHEN transaction_type = 'debit' THEN amount ELSE 0 END) AS debit_sum</pre>
<p>В одном запросе сумма debit, рядом credit — похоже на сводную. Ключ группы может быть другим (город, месяц).</p>
<p>Чтобы не было NULL, ставьте ELSE 0. Если ELSE забыть, неподошедшие станут NULL, SUM может их отбросить — не тот 0, который ждали.</p>
""",
    },
    "sana-filtr": {
        "en": """
<p>A date is an ordinary column, but the format confuses people. A safe habit: <code>'2024-03-01'</code> (year-month-day). Day/month mix-ups happen less in that format.</p>
<pre>SELECT DISTINCT city
FROM customers
WHERE city = 'Toshkent';</pre>
<p>An exact value. A range — March:</p>
<pre>WHERE transaction_date BETWEEN '2024-03-01' AND '2024-03-31'</pre>
<p>BETWEEN includes both edges. If the column also has a time (12:00), “the night of the 31st” can fall out. Then <code>&gt;= '2024-03-01' AND &lt; '2024-04-01'</code> is more precise. In our exercises it’s usually just a day.</p>
<p>Comparing text dates works in ISO order. You don’t write “March” in Uzbek — use numbers.</p>
""",
        "ru": """
<p>Дата — обычный столбец, но формат путает людей. Безопасная привычка: <code>'2024-03-01'</code> (год-месяц-день). Ошибки «день/месяц перепутали» в этом формате реже.</p>
<pre>SELECT DISTINCT city
FROM customers
WHERE city = 'Toshkent';</pre>
<p>Точное значение. Диапазон — март:</p>
<pre>WHERE transaction_date BETWEEN '2024-03-01' AND '2024-03-31'</pre>
<p>BETWEEN берёт оба края. Если в столбце ещё и время (12:00), «ночь 31-го» может выпасть. Тогда точнее: <code>&gt;= '2024-03-01' AND &lt; '2024-04-01'</code>. В наших упражнениях обычно только день.</p>
<p>Сравнение текстовых дат работает в порядке ISO. «Март» словами не пишут — цифры.</p>
""",
    },
    "sana-group": {
        "en": """
<p>Daily activity: how many people per day. That’s GROUP BY date + a unique count.</p>
<pre>SELECT transaction_date AS day,
       COUNT(*) AS cnt
FROM transactions
GROUP BY transaction_date;</pre>
<p>If one person enters 10 times in a day, <code>COUNT(DISTINCT user_id)</code> counts them once. Plain <code>COUNT(*)</code> would count every visit — a different question.</p>
<p>Sales by month (SQLite, our environment):</p>
<pre>SELECT strftime('%Y-%m', transaction_date) AS oy,
       SUM(amount) AS total
FROM transactions
GROUP BY oy;</pre>
<p>PostgreSQL has a different function. Write down which system the report uses. The idea is still: cut time, group, SUM/COUNT.</p>
""",
        "ru": """
<p>Дневная активность: сколько людей за каждый день. Это GROUP BY по дате + уникальный подсчёт.</p>
<pre>SELECT transaction_date AS day,
       COUNT(*) AS cnt
FROM transactions
GROUP BY transaction_date;</pre>
<p>Если один человек за день зашёл 10 раз, <code>COUNT(DISTINCT user_id)</code> посчитает его один раз. Обычный <code>COUNT(*)</code> считал бы каждый заход — другой вопрос.</p>
<p>Продажи по месяцам (SQLite, наша среда):</p>
<pre>SELECT strftime('%Y-%m', transaction_date) AS oy,
       SUM(amount) AS total
FROM transactions
GROUP BY oy;</pre>
<p>В PostgreSQL будет другая функция. В отчёте запишите, какая система. Идея всё равно: нарезать время, сгруппировать, SUM/COUNT.</p>
""",
    },
    "sana-farq": {
        "en": """
<p>Marketing: “This day, this brand — how many unique leads?” Counting repeated IDs once — DISTINCT again.</p>
<pre>SELECT transaction_date, transaction_type,
       COUNT(*) AS cnt
FROM transactions
GROUP BY transaction_date, transaction_type;</pre>
<p>The group is two things: day and brand. Each cell is its own slice.</p>
<p>Was delivery late? The difference of two dates. In SQLite <code>julianday(delivered) - julianday(promised)</code> gives days. A large positive number — late. Negative — early. The formula depends on the system; the question is general: don’t look at SLA only as an average, look at the delay tail too.</p>
""",
        "ru": """
<p>Маркетинг: «Этот день, этот бренд — сколько уникальных лидов?» Повторяющиеся ID считать один раз — снова DISTINCT.</p>
<pre>SELECT transaction_date, transaction_type,
       COUNT(*) AS cnt
FROM transactions
GROUP BY transaction_date, transaction_type;</pre>
<p>Группа из двух: день и бренд. Каждая ячейка — свой срез.</p>
<p>Доставка опоздала? Разность двух дат. В SQLite <code>julianday(доставлено) - julianday(обещано)</code> даёт дни. Большое положительное — поздно. Отрицательное — рано. Формула зависит от системы, вопрос общий: SLA смотрите не только средним, смотрите и хвост опозданий.</p>
""",
    },
    "window-asos": {
        "en": """
<p>GROUP BY “packs” rows and leaves one row per group. Sometimes you still need all rows, with a rank or a total next to them. A window function does that. The row doesn’t disappear.</p>
<pre>SELECT id, amount,
       ROW_NUMBER() OVER (ORDER BY amount DESC) AS rn
FROM transactions;</pre>
<p><code>OVER (ORDER BY amount DESC)</code> — “in this order 1, 2, 3…” Each payment stays on its row, with a number beside it.</p>
<p>If you add <code>PARTITION BY city</code>, numbering restarts from 1 inside each city. In Excel that’s “rank inside a group”.</p>
<p>For now one sentence: OVER is the window. ORDER BY is how to count. PARTITION is which inner group (optional).</p>
""",
        "ru": """
<p>GROUP BY «сжимает» строки и оставляет по одной на группу. Иногда нужны все строки, а рядом порядковый номер или итог. Это делает оконная (window) функция. Строка не пропадает.</p>
<pre>SELECT id, amount,
       ROW_NUMBER() OVER (ORDER BY amount DESC) AS rn
FROM transactions;</pre>
<p><code>OVER (ORDER BY amount DESC)</code> — «в этом порядке 1, 2, 3…» Каждый платёж остаётся на своей строке, рядом номер.</p>
<p>Если добавить <code>PARTITION BY city</code>, внутри каждого города нумерация начнётся с 1. В Excel это «порядок внутри группы».</p>
<p>Пока одна фраза: OVER — окно. ORDER BY — как считать. PARTITION — какая внутренняя группа (необязательно).</p>
""",
    },
    "window-rank": {
        "en": """
<p>If two people have the same score, what is the place? Athletes know: sometimes 1, 1, 3 (no second), sometimes 1, 1, 2.</p>
<ul>
  <li><code>ROW_NUMBER()</code> — still 1, 2, 3. Even ties get different numbers (by inner order)</li>
  <li><code>RANK()</code> — ties share a place, then a gap: 1, 1, 3</li>
  <li><code>DENSE_RANK()</code> — ties share a place, no gap: 1, 1, 2</li>
</ul>
<pre>SELECT id, amount,
       RANK() OVER (ORDER BY amount DESC) AS rnk
FROM transactions;</pre>
<p>The highest score is 1. If you need a unique “top-1”, ROW_NUMBER is often handy. A report rank is RANK or DENSE_RANK. Say the question in plain language, then pick the function.</p>
""",
        "ru": """
<p>Если у двоих одинаковый балл, какое место? Спортсмены понимают: иногда 1, 1, 3 (второго нет), иногда 1, 1, 2.</p>
<ul>
  <li><code>ROW_NUMBER()</code> — всё равно 1, 2, 3. Даже при равенстве номера разные (по внутреннему порядку)</li>
  <li><code>RANK()</code> — равные одно место, потом дырка: 1, 1, 3</li>
  <li><code>DENSE_RANK()</code> — равные одно место, дырки нет: 1, 1, 2</li>
</ul>
<pre>SELECT id, amount,
       RANK() OVER (ORDER BY amount DESC) AS rnk
FROM transactions;</pre>
<p>Самый высокий балл — 1. Если нужно уникально взять «топ-1», удобен ROW_NUMBER. Место в отчёте — RANK или DENSE_RANK. Скажите вопрос обычным языком, потом выберите функцию.</p>
""",
    },
    "window-sum": {
        "en": """
<p>If each row needs “total seats” or “this customer’s total payments”, you don’t have to collapse with GROUP BY.</p>
<pre>SELECT id, amount,
       COUNT(*) OVER () AS jami
FROM transactions;</pre>
<p><code>OVER ()</code> is the whole result window. The same total on every row.</p>
<p><code>SUM(amount) OVER (PARTITION BY customer_id)</code> — next to each payment, that customer’s sum. For a running total (growing day by day) add ORDER BY date. The default frame depends on the system — in exercises write the expected column exactly.</p>
<p>Short difference: GROUP BY squeezes. A window writes beside the row.</p>
""",
        "ru": """
<p>Если в каждой строке нужно «всего мест» или «сумма платежей этого клиента», сжимать GROUP BY не обязательно.</p>
<pre>SELECT id, amount,
       COUNT(*) OVER () AS jami
FROM transactions;</pre>
<p><code>OVER ()</code> — окно всего результата. На каждой строке одно и то же всего.</p>
<p><code>SUM(amount) OVER (PARTITION BY customer_id)</code> — рядом с каждым платежом сумма этого клиента. Для накопительного итога (растёт день за днём) добавляют ORDER BY по дате. Рамка по умолчанию зависит от системы — в упражнении пишите ожидаемый столбец точно.</p>
<p>Короткая разница: GROUP BY сжимает. Окно пишет рядом.</p>
""",
    },
    "null-coalesce": {
        "en": """
<p>NULL again, slowly. This is not an “empty cell”. It is “we don’t know.” 10 + unknown = unknown. That’s why <code>10 + NULL</code> is usually NULL.</p>
<p>Check with <code>city IS NULL</code> / <code>IS NOT NULL</code>. Never <code>city = NULL</code> — that doesn’t work, because unknown equals unknown?</p>
<p>If you need a substitute value, the standard way:</p>
<pre>COALESCE(amount, 0)
COALESCE(city, '—')</pre>
<p>The first real value in the list. MySQL has IFNULL, SQL Server has ISNULL — similar. In the course write COALESCE — more places understand it.</p>
<p>NULL after a LEFT JOIN is normal. Replacing it with 0 or text, or leaving it as “missing”, is a business question. Auto-zero is not always right (for example, calling an unknown salary 0 ruins the average).</p>
""",
        "ru": """
<p>NULL ещё раз, медленно. Это не «пустая ячейка». Это «не знаем». 10 + неизвестно = неизвестно. Поэтому <code>10 + NULL</code> обычно NULL.</p>
<p>Проверка: <code>city IS NULL</code> / <code>IS NOT NULL</code>. Никогда <code>city = NULL</code> — не работает, потому что неизвестно равно неизвестно?</p>
<p>Если нужно значение-замена, стандартный путь:</p>
<pre>COALESCE(amount, 0)
COALESCE(city, '—')</pre>
<p>Первое настоящее значение в списке. В MySQL есть IFNULL, в SQL Server — ISNULL, похожие. В курсе пишите COALESCE — его понимают чаще.</p>
<p>NULL сразу после LEFT JOIN — обычное дело. Заменить на 0 или текст или оставить «нет» — вопрос бизнеса. Автоматический 0 не всегда верен (например, неизвестную зарплату назвать 0 — среднее сломается).</p>
""",
    },
    "combine-tables": {
        "en": """
<p>A classic task: people in one table, addresses in another. Not everyone has an address. INNER would drop people without an address. So LEFT — people on the left.</p>
<pre>SELECT c.name, t.amount
FROM customers AS c
LEFT JOIN transactions AS t ON c.id = t.customer_id;</pre>
<p>A customer with no payment has amount NULL. That’s not a bug — the question is: “all people, add the payment if it exists.”</p>
<p>If key names are the same you also see <code>USING (personId)</code>. <code>ON</code> is clearer to understand. Interview “Combine Two Tables” is mostly this.</p>
""",
        "ru": """
<p>Классическая задача: люди в одной таблице, адрес в другой. Адрес есть не у всех. INNER потеряет тех, у кого адреса нет. Поэтому LEFT — люди слева.</p>
<pre>SELECT c.name, t.amount
FROM customers AS c
LEFT JOIN transactions AS t ON c.id = t.customer_id;</pre>
<p>У клиента без платежа amount будет NULL. Это не ошибка — вопрос такой: «все люди, платёж добавь, если есть».</p>
<p>Если имена ключей одинаковые, встречается и <code>USING (personId)</code>. Для понимания <code>ON</code> открытее. Интервьюшный «Combine Two Tables» — в основном это.</p>
""",
    },
    "advanced-review": {
        "en": """
<p>Last lesson. No new magic. A report at work is usually a mix: first join, then clean, then group, sometimes CASE.</p>
<p>Talk it through to yourself:</p>
<ol>
  <li>Which tables? What’s the key? INNER or LEFT?</li>
  <li>Which rows? WHERE. Did you forget NULL?</li>
  <li>A per-group calculation? GROUP BY + COUNT/SUM</li>
  <li>Conditional counting? SUM(CASE…)</li>
  <li>Is the column name the same as in the exercise? AS</li>
  <li>Does order matter? ORDER BY</li>
</ol>
<pre>SELECT c.name, COUNT(*) AS cnt
FROM customers AS c
JOIN transactions AS t ON c.id = t.customer_id
GROUP BY c.name;</pre>
<p>First we got the product name with JOIN, then we counted. Don’t write a 20-line query in one breath. A small SELECT, then add to it.</p>
<p>You now have, from zero: what a table is, SELECT, filter, order, count, group, JOIN, subquery, CTE, CASE, dates, windows, NULL. The rest is practice and stating the question clearly. Read the next exercise like a teacher: “Which lesson is this question from?” — then write.</p>
""",
        "ru": """
<p>Последний урок. Новой магии нет. Рабочий отчёт обычно смесь: сначала связать, потом почистить, потом группа, иногда CASE.</p>
<p>Проговорите себе:</p>
<ol>
  <li>Какие таблицы? Какой ключ? INNER или LEFT?</li>
  <li>Какие строки? WHERE. NULL не забыли?</li>
  <li>Есть расчёт «для каждого»? GROUP BY + COUNT/SUM</li>
  <li>Условный подсчёт? SUM(CASE…)</li>
  <li>Имя столбца как в упражнении? AS</li>
  <li>Важен порядок? ORDER BY</li>
</ol>
<pre>SELECT c.name, COUNT(*) AS cnt
FROM customers AS c
JOIN transactions AS t ON c.id = t.customer_id
GROUP BY c.name;</pre>
<p>Сначала имя продукта взяли JOIN-ом, потом посчитали. Не пишите 20-строчный запрос на одном дыхании. Маленький SELECT, потом добавляйте.</p>
<p>Теперь у вас с нуля: что такое таблица, SELECT, фильтр, порядок, подсчёт, группа, JOIN, подзапрос, CTE, CASE, даты, окна, NULL. Остальное — практика и ясно сказать вопрос. Следующее упражнение читайте как преподаватель: «К какому уроку этот вопрос?» — потом пишите.</p>
""",
    },
}
