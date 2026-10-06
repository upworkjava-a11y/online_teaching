"""Restricted in-process helpers for the Python lesson sandbox worker."""

from __future__ import annotations

import builtins
import io
import sys
import traceback
from types import ModuleType

ALLOWED_MODULES = frozenset(
    {
        "math",
        "statistics",
        "collections",
        "datetime",
        "re",
        "json",
        "itertools",
        "functools",
        "decimal",
        "fractions",
        "random",
        "string",
        "typing",
        "numpy",
        "pandas",
        "matplotlib",
        "matplotlib.pyplot",
        "seaborn",
    }
)

_BLOCKED_BUILTINS = frozenset(
    {
        "open",
        "input",
        "breakpoint",
        "exit",
        "quit",
        "help",
        "copyright",
        "credits",
        "license",
        "exec",
        "eval",
        "compile",
        "__import__",
    }
)


def _safe_import(name, globals=None, locals=None, fromlist=(), level=0):  # noqa: A002
    root = name.split(".", 1)[0]
    if name not in ALLOWED_MODULES and root not in ALLOWED_MODULES:
        raise ImportError(f"Modul ruxsat etilmagan: {name}")
    module = builtins.__import__(name, globals, locals, fromlist, level)
    if name == "matplotlib" or name.startswith("matplotlib."):
        try:
            import matplotlib

            matplotlib.use("Agg", force=True)
        except Exception:
            pass
    return module


def build_safe_builtins() -> dict:
    safe = {k: getattr(builtins, k) for k in dir(builtins) if not k.startswith("_")}
    for name in _BLOCKED_BUILTINS:
        safe.pop(name, None)
    safe["__import__"] = _safe_import
    safe["__build_class__"] = builtins.__build_class__
    safe["__name__"] = "__student__"
    return safe


def run_user_code(source: str) -> tuple[str, str, int]:
    """Execute student code. Returns (stdout, stderr, exit_code)."""
    stdout = io.StringIO()
    stderr = io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = stdout, stderr
    code = 0
    try:
        compiled = compile(source, "<student>", "exec")
        env: dict = {"__builtins__": build_safe_builtins(), "__name__": "__main__"}
        exec(compiled, env, env)  # noqa: S102 — intentional sandbox exec
    except Exception:
        code = 1
        traceback.print_exc(file=stderr)
    finally:
        sys.stdout, sys.stderr = old_out, old_err
    return stdout.getvalue(), stderr.getvalue(), code
