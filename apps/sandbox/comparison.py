from decimal import Decimal, InvalidOperation
from typing import Any


def _normalize_value(value: Any, numeric_precision: int = 6):
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, (int,)):
        return value
    if isinstance(value, (float, Decimal)):
        try:
            return str(Decimal(str(value)).quantize(Decimal("1." + "0" * numeric_precision)))
        except InvalidOperation:
            return str(value)
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    text = str(value)
    try:
        if text.replace(".", "", 1).replace("-", "", 1).isdigit():
            return str(Decimal(text).quantize(Decimal("1." + "0" * numeric_precision)))
    except InvalidOperation:
        pass
    return text


def _normalize_row(row: list[Any], numeric_precision: int = 6) -> tuple:
    return tuple(_normalize_value(item, numeric_precision) for item in row)


def compare_results(
    actual_columns: list[str],
    actual_rows: list[list[Any]],
    expected_columns: list[str],
    expected_rows: list[list[Any]],
    require_row_order: bool = False,
    require_column_order: bool = False,
    numeric_precision: int = 6,
) -> tuple[bool, str]:
    if require_column_order:
        actual_cols = [c.lower() for c in actual_columns]
        expected_cols = [c.lower() for c in expected_columns]
        if actual_cols != expected_cols:
            return False, "Ustunlar tartibi yoki nomlari mos kelmadi."
        actual_norm = [_normalize_row(row, numeric_precision) for row in actual_rows]
        expected_norm = [_normalize_row(row, numeric_precision) for row in expected_rows]
    else:
        if len(actual_columns) != len(expected_columns):
            return False, "Ustunlar soni mos kelmadi."
        actual_map = {name.lower(): index for index, name in enumerate(actual_columns)}
        try:
            order = [actual_map[name.lower()] for name in expected_columns]
        except KeyError:
            return False, "Ustun nomlari mos kelmadi."
        actual_norm = [
            _normalize_row([row[i] for i in order], numeric_precision) for row in actual_rows
        ]
        expected_norm = [_normalize_row(row, numeric_precision) for row in expected_rows]

    if len(actual_norm) != len(expected_norm):
        return False, "Qatorlar soni mos kelmadi."

    if require_row_order:
        if actual_norm != expected_norm:
            return False, "Natija qatorlari kutilgan natijaga mos kelmadi."
        return True, "To‘g‘ri!"

    def _sort_key(row: tuple):
        return tuple((0, "") if v is None else (1, str(v)) for v in row)

    if sorted(actual_norm, key=_sort_key) != sorted(expected_norm, key=_sort_key):
        return False, "Natija qatorlari kutilgan natijaga mos kelmadi."
    return True, "To‘g‘ri!"
