"""Keep SQL keywords and code samples untranslated."""

from __future__ import annotations

import re

SQL_KEYWORDS = (
    "SELECT",
    "DISTINCT",
    "FROM",
    "WHERE",
    "JOIN",
    "INNER",
    "LEFT",
    "RIGHT",
    "FULL",
    "OUTER",
    "CROSS",
    "ON",
    "USING",
    "GROUP",
    "BY",
    "ORDER",
    "HAVING",
    "LIMIT",
    "OFFSET",
    "AS",
    "AND",
    "OR",
    "NOT",
    "IN",
    "IS",
    "NULL",
    "LIKE",
    "BETWEEN",
    "EXISTS",
    "CASE",
    "WHEN",
    "THEN",
    "ELSE",
    "END",
    "COUNT",
    "SUM",
    "AVG",
    "MIN",
    "MAX",
    "CAST",
    "COALESCE",
    "NULLIF",
    "UNION",
    "ALL",
    "INSERT",
    "UPDATE",
    "DELETE",
    "CREATE",
    "TABLE",
    "VIEW",
    "INDEX",
    "WITH",
    "RECURSIVE",
    "OVER",
    "PARTITION",
    "ROWS",
    "RANGE",
    "UNBOUNDED",
    "PRECEDING",
    "FOLLOWING",
    "CURRENT",
    "ROW",
    "ROW_NUMBER",
    "RANK",
    "DENSE_RANK",
    "LAG",
    "LEAD",
    "NTILE",
    "FIRST_VALUE",
    "LAST_VALUE",
    "ASC",
    "DESC",
    "TRUE",
    "FALSE",
    "INNER JOIN",
    "LEFT JOIN",
    "RIGHT JOIN",
    "FULL JOIN",
    "GROUP BY",
    "ORDER BY",
    "PARTITION BY",
    "IS NULL",
    "IS NOT NULL",
    "NOT NULL",
    "LEFT JOIN",
    "INNER JOIN",
    "CTE",
    "RDBMS",
    "SQL",
    "DAX",
    "ETL",
    "KPI",
    "EDA",
    "NumPy",
    "Pandas",
    "XLOOKUP",
    "Power Query",
    "Power BI",
    "Get Data",
    "W3Schools",
    "CodeChef",
    "LeetCode",
)

# Longest first so "GROUP BY" wins over "GROUP" / "BY"
_SQL_PATTERN = re.compile(
    r"\b(?:" + "|".join(re.escape(k) for k in sorted(set(SQL_KEYWORDS), key=len, reverse=True)) + r")\b",
    re.IGNORECASE,
)

# Table/column identifiers used in lessons and the sandbox. Keep Latin.
SCHEMA_IDENTIFIERS = (
    "id",
    "name",
    "city",
    "amount",
    "customers",
    "transactions",
    "orders",
    "customer_id",
    "registration_date",
    "transaction_date",
    "transaction_type",
    "shop_products",
    "category",
    "price",
    "product_id",
    "quantity",
    "order_date",
    "products",
    "product",
    "world",
    "tweets",
    "views",
    "cinema",
    "patients",
    "followers",
    "employeeattendance",
    "teacher",
    "courses",
    "actordirector",
    "mynumbers",
    "employees",
    "employeeuni",
    "employee",
    "bonus",
    "sales",
    "triangle",
    "activity",
    "dailysales",
    "person",
    "address",
    "seat",
    "scores",
    "lccustomers",
    "lcorders",
    "low_fats",
    "recyclable",
    "continent",
    "area",
    "population",
    "gdp",
    "tweet_id",
    "content",
    "article_id",
    "author_id",
    "viewer_id",
    "view_date",
    "movie",
    "description",
    "rating",
    "patient_id",
    "patient_name",
    "conditions",
    "user_id",
    "follower_id",
    "emp_id",
    "event_day",
    "in_time",
    "out_time",
    "teacher_id",
    "subject_id",
    "dept_id",
    "student",
    "class",
    "actor_id",
    "director_id",
    "timestamp",
    "num",
    "unique_id",
    "empid",
    "supervisor",
    "salary",
    "product_name",
    "sale_id",
    "year",
    "session_id",
    "activity_date",
    "activity_type",
    "date_id",
    "make_name",
    "lead_id",
    "partner_id",
    "personid",
    "lastname",
    "firstname",
    "addressid",
    "state",
    "customerid",
    "score",
    "total",
    "cnt",
    "rn",
    "rnk",
    "pct",
    "label",
    "debit",
    "credit",
)

_IDENT_PATTERN = re.compile(
    r"\b(?:" + "|".join(re.escape(k) for k in sorted(set(SCHEMA_IDENTIFIERS), key=len, reverse=True)) + r")\b",
    re.IGNORECASE,
)
_SNAKE_IDENT = re.compile(r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+)+\b")
_CODE_BLOCKS = re.compile(
    r"(<pre\b[^>]*>.*?</pre>|<code\b[^>]*>.*?</code>|<kbd\b[^>]*>.*?</kbd>)",
    re.IGNORECASE | re.DOTALL,
)
_INLINE_BACKTICK = re.compile(r"`[^`]+`")
_HTML_TAG = re.compile(r"</?[^>]+>")
_TH_BLOCK = re.compile(r"<th\b[^>]*>(.*?)</th>", re.IGNORECASE | re.DOTALL)


def _is_schema_header(inner: str) -> bool:
    text = re.sub(r"<[^>]+>", "", inner).strip()
    if not text or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", text):
        return False
    if "_" in text or any(ch.isdigit() for ch in text) or text.islower():
        return True
    if text.isupper() and len(text) >= 2:
        return True
    if re.search(r"[a-z][A-Z]", text):
        return True
    return text.lower() in SCHEMA_IDENTIFIERS


def protect_sql_and_code(text: str) -> tuple[str, dict[str, str]]:
    """Replace SQL keywords, identifiers, and code with tokens. Returns (masked, token_map)."""
    if not text:
        return text, {}
    tokens: dict[str, str] = {}

    def stash(chunk: str) -> str:
        key = f"⟦{len(tokens)}⟧"
        tokens[key] = chunk
        return key

    def stash_code(match: re.Match) -> str:
        return stash(match.group(0))

    masked = _CODE_BLOCKS.sub(stash_code, text)
    masked = _INLINE_BACKTICK.sub(stash_code, masked)

    def stash_th(match: re.Match) -> str:
        if _is_schema_header(match.group(1)):
            return stash(match.group(0))
        return match.group(0)

    masked = _TH_BLOCK.sub(stash_th, masked)
    masked = _HTML_TAG.sub(stash_code, masked)

    def stash_sql(match: re.Match) -> str:
        return stash(match.group(0))

    masked = _SQL_PATTERN.sub(stash_sql, masked)
    masked = _SNAKE_IDENT.sub(stash_sql, masked)
    masked = _IDENT_PATTERN.sub(stash_sql, masked)
    return masked, tokens


def restore_protected(text: str, tokens: dict[str, str]) -> str:
    for key, value in sorted(tokens.items(), key=lambda item: len(item[0]), reverse=True):
        text = text.replace(key, value)
    return text
