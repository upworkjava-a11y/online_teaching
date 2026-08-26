import re

import sqlparse
from sqlparse.sql import Identifier, IdentifierList
from sqlparse.tokens import DML, Keyword

from .exceptions import ForbiddenSQLError, QueryLimitError

FORBIDDEN_KEYWORDS = {
    "DROP",
    "DELETE",
    "UPDATE",
    "INSERT",
    "ALTER",
    "CREATE",
    "TRUNCATE",
    "COPY",
    "GRANT",
    "REVOKE",
    "COMMENT",
    "EXECUTE",
    "CALL",
    "DO",
    "LOAD",
    "IMPORT",
    "EXPORT",
    "VACUUM",
    "REINDEX",
    "CLUSTER",
    "LOCK",
    "UNLOCK",
    "LISTEN",
    "NOTIFY",
    "UNLISTEN",
    "PREPARE",
    "DEALLOCATE",
    "DISCARD",
    "SECURITY",
    "OWNER",
    "ATTACH",
    "DETACH",
    "PRAGMA",
    "REPLACE",
    "MERGE",
    "UPSERT",
    "INTO",
    "SET",
    "RESET",
    "SHOW",
    "EXPLAIN",
}

FORBIDDEN_FUNCTIONS = {
    "pg_read_file",
    "pg_read_binary_file",
    "pg_ls_dir",
    "pg_stat_file",
    "lo_import",
    "lo_export",
    "lo_get",
    "dblink",
    "dblink_exec",
    "dblink_connect",
    "pg_sleep",
    "pg_terminate_backend",
    "pg_reload_conf",
}

ALLOWED_START = {"SELECT", "WITH"}


def normalize_sql(sql: str) -> str:
    return sqlparse.format(sql, strip_comments=True).strip()


def validate_student_sql(sql: str, max_chars: int) -> str:
    if not sql or not sql.strip():
        raise ForbiddenSQLError("SQL so‘rovini yozing.")
    if len(sql) > max_chars:
        raise QueryLimitError("So‘rov juda uzun. Uni qisqartirib qayta yozing.")

    cleaned = normalize_sql(sql)
    statements = [stmt for stmt in sqlparse.parse(cleaned) if stmt.tokens and str(stmt).strip()]
    if not statements:
        raise ForbiddenSQLError("SQL so‘rovini yozing.")
    if len(statements) > 1:
        raise ForbiddenSQLError("Bir vaqtning o‘zida faqat bitta so‘rov yuborish mumkin.")

    statement = statements[0]
    first = statement.token_first(skip_cm=True)
    first_value = first.value.upper() if first else ""
    if first_value not in ALLOWED_START:
        raise ForbiddenSQLError("Faqat SELECT so‘rovlari ruxsat etiladi.")

    text_upper = cleaned.upper()
    for keyword in FORBIDDEN_KEYWORDS:
        if re.search(rf"\b{keyword}\b", text_upper):
            if keyword == "INTO" and "INSERT" not in text_upper:
                # SELECT ... INTO is still dangerous
                if re.search(r"\bINTO\b", text_upper):
                    raise ForbiddenSQLError("INTO operatori ruxsat etilmagan.")
            elif keyword != "INTO":
                raise ForbiddenSQLError("Bu so‘rov ruxsat etilmagan.")

    lowered = cleaned.lower()
    for func in FORBIDDEN_FUNCTIONS:
        if f"{func}(" in lowered:
            raise ForbiddenSQLError("Xavfli funksiya ishlatilgan.")

    if ";" in cleaned.rstrip(";"):
        raise ForbiddenSQLError("Bir vaqtning o‘zida faqat bitta so‘rov yuborish mumkin.")

    _ensure_no_write_dml(statement)
    return cleaned.rstrip(";")


def _ensure_no_write_dml(statement) -> None:
    for token in statement.flatten():
        if token.ttype in (DML,) and token.value.upper() in {"INSERT", "UPDATE", "DELETE"}:
            raise ForbiddenSQLError("O‘zgartirish so‘rovlari ruxsat etilmagan.")
        if token.ttype is Keyword and token.value.upper() in FORBIDDEN_KEYWORDS - {"INTO", "SET", "SHOW"}:
            raise ForbiddenSQLError("Bu so‘rov ruxsat etilmagan.")
    _ = Identifier, IdentifierList
