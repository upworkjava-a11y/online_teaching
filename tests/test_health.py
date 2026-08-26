from django.test import TestCase, override_settings
from django.urls import reverse


class HealthCheckTests(TestCase):
    def test_health_ok(self):
        response = self.client.get(reverse("health"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")
        self.assertTrue(response.json()["database"])


class SandboxLimitTests(TestCase):
    def test_result_limit_truncates(self):
        from apps.sandbox.datasets import seed_sandbox_database
        from apps.sandbox.executor import sql_executor

        seed_sandbox_database()
        with override_settings(SANDBOX_MAX_ROWS=2):
            result = sql_executor.execute("SELECT id FROM transactions")
        self.assertEqual(len(result.rows), 2)
        self.assertTrue(result.truncated)
