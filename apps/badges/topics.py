"""Map course modules / exercise hints to badge topics."""

from __future__ import annotations

# Canonical topic keys used by badge requirements
TOPIC_SELECT = "select_filter"
TOPIC_GROUP = "group_by"
TOPIC_JOIN = "join"
TOPIC_WINDOW = "window"
TOPIC_SUBQUERY = "subquery"
TOPIC_CTE = "cte"
TOPIC_CASE = "case"
TOPIC_DATETIME = "datetime"
TOPIC_PYTHON = "python"
TOPIC_PY_VARS = "python_vars"
TOPIC_PY_COND = "python_conditions"
TOPIC_PY_LOOPS = "python_loops"

SQL_TOPIC_LABELS = {
    TOPIC_SELECT: "SELECT / Filtering",
    TOPIC_GROUP: "GROUP BY / Aggregation",
    TOPIC_JOIN: "JOIN",
    TOPIC_WINDOW: "Window Functions",
    TOPIC_SUBQUERY: "Subqueries",
    TOPIC_CTE: "CTE",
    TOPIC_CASE: "CASE",
    TOPIC_DATETIME: "Date / Time",
}

# Module slug → topic (SQL curriculum)
MODULE_TOPIC_MAP: dict[str, str] = {
    "sql-asoslari": TOPIC_SELECT,
    "filtrlash-va-saralash": TOPIC_SELECT,
    "agregatsiyalar": TOPIC_GROUP,
    "group-by-having": TOPIC_GROUP,
    "joins": TOPIC_JOIN,
    "inner-join": TOPIC_JOIN,
    "left-join": TOPIC_JOIN,
    "subqueries": TOPIC_SUBQUERY,
    "ctes": TOPIC_CTE,
    "case": TOPIC_CASE,
    "date-time": TOPIC_DATETIME,
    "window-functions": TOPIC_WINDOW,
    "window-rank": TOPIC_WINDOW,
    "window-sum": TOPIC_WINDOW,
    # Python modules
    "py-noldan": TOPIC_PY_VARS,
    "py-asoslari": TOPIC_PY_VARS,
    "py-mantiq": TOPIC_PY_COND,
    "py-tuzilma": TOPIC_PY_LOOPS,
    "py-numpy": TOPIC_PYTHON,
    "py-pandas": TOPIC_PYTHON,
    "py-clean": TOPIC_PYTHON,
    "py-agg": TOPIC_PYTHON,
    "py-eda": TOPIC_PYTHON,
    "py-capstone": TOPIC_PYTHON,
}

# Explicit exercise slug overrides (first puzzles across concepts)
EXERCISE_TOPIC_MAP: dict[str, str] = {
    # SQL first three conceptual puzzles
    "mijoz-ismlari": TOPIC_SELECT,
    "jami-summa": TOPIC_GROUP,
    "mijoz-tranz-join": TOPIC_JOIN,
    # Python first three conceptual puzzles
    "py-ex-noldan-path": TOPIC_PY_VARS,
    "py-ex-if-bug": TOPIC_PY_COND,
    "py-p-sum-loop": TOPIC_PY_LOOPS,
}


def topic_for_exercise(exercise) -> str | None:
    slug = getattr(exercise, "slug", "") or ""
    if slug in EXERCISE_TOPIC_MAP:
        return EXERCISE_TOPIC_MAP[slug]
    module = getattr(exercise, "module", None)
    if module is None:
        return None
    mod_slug = getattr(module, "slug", "") or ""
    if mod_slug in MODULE_TOPIC_MAP:
        return MODULE_TOPIC_MAP[mod_slug]
    course = getattr(module, "course", None)
    if course and getattr(course, "slug", "") == "python":
        return TOPIC_PYTHON
    if course and getattr(course, "slug", "") == "sql":
        return TOPIC_SELECT
    return None


def is_python_exercise(exercise) -> bool:
    course = getattr(getattr(exercise, "module", None), "course", None)
    if course and course.slug == "python":
        return True
    topic = topic_for_exercise(exercise)
    return bool(topic and topic.startswith("python"))


def is_sql_exercise(exercise) -> bool:
    course = getattr(getattr(exercise, "module", None), "course", None)
    if course and course.slug == "sql":
        return True
    topic = topic_for_exercise(exercise)
    return bool(topic and topic in SQL_TOPIC_LABELS)
