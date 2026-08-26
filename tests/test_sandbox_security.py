from django.conf import settings
from django.db import connection
from django.test import TestCase

from apps.sandbox.exceptions import ForbiddenSQLError, QueryLimitError
from apps.sandbox.executor import sql_executor
from apps.sandbox.security import validate_student_sql


class SandboxSecurityTests(TestCase):
    def test_drop_blocked(self):
        with self.assertRaises(ForbiddenSQLError):
            validate_student_sql("DROP TABLE customers", 8000)

    def test_delete_blocked(self):
        with self.assertRaises(ForbiddenSQLError):
            validate_student_sql("DELETE FROM customers", 8000)

    def test_update_blocked(self):
        with self.assertRaises(ForbiddenSQLError):
            validate_student_sql("UPDATE customers SET name='x'", 8000)

    def test_insert_blocked(self):
        with self.assertRaises(ForbiddenSQLError):
            validate_student_sql("INSERT INTO customers(name) VALUES('x')", 8000)

    def test_alter_blocked(self):
        with self.assertRaises(ForbiddenSQLError):
            validate_student_sql("ALTER TABLE customers ADD COLUMN x INT", 8000)

    def test_truncate_blocked(self):
        with self.assertRaises(ForbiddenSQLError):
            validate_student_sql("TRUNCATE TABLE customers", 8000)

    def test_query_size_limit(self):
        with self.assertRaises(QueryLimitError):
            validate_student_sql("SELECT " + "a" * 50, 10)

    def test_production_db_not_used(self):
        self.assertNotEqual(str(settings.SANDBOX_DATABASE["NAME"]), str(settings.DATABASES["default"]["NAME"]))
        self.assertNotEqual(settings.SANDBOX_DATABASE["NAME"], connection.settings_dict["NAME"])

    def test_select_allowed(self):
        cleaned = validate_student_sql("SELECT name FROM customers", 8000)
        self.assertIn("SELECT", cleaned.upper())
