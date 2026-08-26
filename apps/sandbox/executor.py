import logging
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from django.conf import settings

from .exceptions import QueryLimitError, QueryTimeoutError, SandboxError
from .security import validate_student_sql

logger = logging.getLogger("apps.sandbox")


@dataclass
class QueryResult:
    columns: list[str]
    rows: list[list]
    truncated: bool = False
    execution_ms: int = 0


class SQLExecutor:
    def execute(self, sql: str) -> QueryResult:
        cleaned = validate_student_sql(sql, settings.SANDBOX_MAX_QUERY_CHARS)
        engine = settings.SANDBOX_DATABASE.get("ENGINE")
        if engine == "sqlite" or not settings.SANDBOX_DATABASE.get("HOST"):
            return self._execute_sqlite(cleaned)
        return self._execute_postgres(cleaned)

    def _execute_postgres(self, sql: str) -> QueryResult:
        try:
            import psycopg
            from psycopg import errors
        except ImportError as exc:
            raise SandboxError("Sandbox ulanishi sozlanmagan.") from exc

        cfg = settings.SANDBOX_DATABASE
        timeout_ms = settings.SANDBOX_QUERY_TIMEOUT_SECONDS * 1000
        max_rows = settings.SANDBOX_MAX_ROWS
        try:
            with psycopg.connect(
                dbname=cfg["NAME"],
                user=cfg["USER"],
                password=cfg["PASSWORD"],
                host=cfg["HOST"],
                port=cfg["PORT"],
                connect_timeout=5,
                autocommit=True,
            ) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SET default_transaction_read_only = on")
                    cursor.execute(f"SET statement_timeout = {timeout_ms}")
                    cursor.execute(f"SET idle_in_transaction_session_timeout = {timeout_ms}")
                    cursor.execute(sql)
                    if cursor.description is None:
                        raise SandboxError("So‘rov natija qaytarmadi.")
                    columns = [col.name for col in cursor.description]
                    rows = cursor.fetchmany(max_rows + 1)
        except errors.QueryCanceled as exc:
            logger.warning("sql_timeout", extra={"error": str(exc)})
            raise QueryTimeoutError() from exc
        except errors.InsufficientPrivilege as exc:
            logger.warning("sql_privilege", extra={"error": str(exc)})
            raise SandboxError("Bu amal sandboxda ruxsat etilmagan.") from exc
        except Exception as exc:
            logger.warning("sql_execution_error", extra={"error": type(exc).__name__})
            raise SandboxError(f"SQL xatosi: {exc}") from exc

        truncated = len(rows) > max_rows
        rows = rows[:max_rows]
        return QueryResult(columns=columns, rows=[list(row) for row in rows], truncated=truncated)

    def _execute_sqlite(self, sql: str) -> QueryResult:
        db_path = settings.SANDBOX_DATABASE["NAME"]
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        max_rows = settings.SANDBOX_MAX_ROWS
        try:
            conn = sqlite3.connect(db_path, timeout=settings.SANDBOX_QUERY_TIMEOUT_SECONDS)
            conn.execute("PRAGMA query_only = ON")
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(sql)
            if cursor.description is None:
                raise SandboxError("So‘rov natija qaytarmadi.")
            columns = [item[0] for item in cursor.description]
            rows = cursor.fetchmany(max_rows + 1)
            conn.close()
        except sqlite3.OperationalError as exc:
            message = str(exc).lower()
            if "timeout" in message or "locked" in message:
                raise QueryTimeoutError() from exc
            logger.warning("sql_execution_error", extra={"error": type(exc).__name__})
            raise SandboxError(f"SQL xatosi: {exc}") from exc
        except Exception as exc:
            logger.warning("sql_execution_error", extra={"error": type(exc).__name__})
            raise SandboxError(f"SQL xatosi: {exc}") from exc

        truncated = len(rows) > max_rows
        rows = rows[:max_rows]
        return QueryResult(columns=columns, rows=[list(row) for row in rows], truncated=truncated)


sql_executor = SQLExecutor()
