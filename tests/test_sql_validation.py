from django.test import SimpleTestCase

from apps.sandbox.comparison import compare_results


class ResultComparisonTests(SimpleTestCase):
    def test_row_ordering_required(self):
        ok, _ = compare_results(
            ["id"],
            [[2], [1]],
            ["id"],
            [[1], [2]],
            require_row_order=True,
        )
        self.assertFalse(ok)
        ok, _ = compare_results(["id"], [[1], [2]], ["id"], [[1], [2]], require_row_order=True)
        self.assertTrue(ok)

    def test_column_ordering(self):
        ok, _ = compare_results(
            ["name", "id"],
            [["A", 1]],
            ["id", "name"],
            [[1, "A"]],
            require_column_order=True,
        )
        self.assertFalse(ok)
        ok, _ = compare_results(
            ["name", "id"],
            [["A", 1]],
            ["id", "name"],
            [[1, "A"]],
            require_column_order=False,
        )
        self.assertTrue(ok)

    def test_null_and_empty(self):
        ok, _ = compare_results(["city"], [[None]], ["city"], [[None]])
        self.assertTrue(ok)
        ok, _ = compare_results(["city"], [], ["city"], [])
        self.assertTrue(ok)
        ok, _ = compare_results(["city"], [], ["city"], [[None]])
        self.assertFalse(ok)

    def test_numeric_precision(self):
        ok, _ = compare_results(["amount"], [[10.0000001]], ["amount"], [[10.0]])
        self.assertTrue(ok)

    def test_alternative_valid_shapes(self):
        ok, _ = compare_results(
            ["customer_id", "count"],
            [[1, 6], [2, 2]],
            ["count", "customer_id"],
            [[6, 1], [2, 2]],
        )
        self.assertTrue(ok)
