"""Restricted in-process helpers for the Python lesson sandbox worker."""

from __future__ import annotations

import ast
import builtins
import io
import sys
import traceback

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
        # Introspection / escape helpers
        "getattr",
        "setattr",
        "delattr",
        "hasattr",
        "globals",
        "locals",
        "vars",
        "dir",
        "memoryview",
        "classmethod",
        "staticmethod",
        "property",
        "super",
    }
)

_FORBIDDEN_NAMES = frozenset(
    {
        "__builtins__",
        "__import__",
        "__loader__",
        "__spec__",
        "__package__",
        "__file__",
        "__cached__",
        "__class__",
        "__bases__",
        "__mro__",
        "__subclasses__",
        "__globals__",
        "__code__",
        "__closure__",
        "__getattribute__",
        "__dict__",
        "__reduce__",
        "__reduce_ex__",
        "getattr",
        "setattr",
        "delattr",
        "hasattr",
        "globals",
        "locals",
        "vars",
        "dir",
        "exec",
        "eval",
        "compile",
        "open",
        "breakpoint",
        "memoryview",
        "super",
        "classmethod",
        "staticmethod",
        "property",
    }
)


class UnsafePythonError(ValueError):
    """Raised when student code fails static security checks."""


class _SecurityVisitor(ast.NodeVisitor):
    def visit_Attribute(self, node: ast.Attribute) -> None:
        # Block dunder / private escape hatches (__class__, __subclasses__, ...)
        if node.attr.startswith("__"):
            raise UnsafePythonError(f"Xavfli atribut: {node.attr}")
        self.generic_visit(node)

    def visit_Name(self, node: ast.Name) -> None:
        if node.id in _FORBIDDEN_NAMES or node.id.startswith("__"):
            raise UnsafePythonError(f"Xavfli nom: {node.id}")
        self.generic_visit(node)

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            root = alias.name.split(".", 1)[0]
            if alias.name not in ALLOWED_MODULES and root not in ALLOWED_MODULES:
                raise UnsafePythonError(f"Modul ruxsat etilmagan: {alias.name}")
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        mod = node.module or ""
        root = mod.split(".", 1)[0] if mod else ""
        if node.level and node.level > 0:
            raise UnsafePythonError("Relative import ruxsat etilmagan.")
        if mod and mod not in ALLOWED_MODULES and root not in ALLOWED_MODULES:
            raise UnsafePythonError(f"Modul ruxsat etilmagan: {mod}")
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        # Block getattr(obj, "__class__") style even if getattr slips through
        if isinstance(node.func, ast.Name) and node.func.id in {
            "getattr",
            "setattr",
            "delattr",
            "hasattr",
            "globals",
            "locals",
            "vars",
            "dir",
            "eval",
            "exec",
            "compile",
            "open",
            "__import__",
            "memoryview",
        }:
            raise UnsafePythonError(f"Funksiya ruxsat etilmagan: {node.func.id}")
        # Ban type(name, bases, dict) metaclass construction; allow type(x) pedagogy.
        if isinstance(node.func, ast.Name) and node.func.id == "type" and len(node.args) >= 2:
            raise UnsafePythonError("type() faqat bitta argument bilan ruxsat etiladi.")
        self.generic_visit(node)


def validate_python_source(source: str) -> ast.AST:
    try:
        tree = ast.parse(source, mode="exec")
    except SyntaxError as exc:
        raise UnsafePythonError(f"Sintaksis xatosi: {exc.msg}") from exc
    _SecurityVisitor().visit(tree)
    return tree


def _deny_io(*_args, **_kwargs):
    raise PermissionError("Fayl/IO amali sandboxda ruxsat etilmagan.")


_PANDAS_BLOCKED = (
    "read_csv",
    "read_table",
    "read_fwf",
    "read_excel",
    "read_json",
    "read_html",
    "read_xml",
    "read_clipboard",
    "read_pickle",
    "read_sas",
    "read_spss",
    "read_stata",
    "read_feather",
    "read_parquet",
    "read_orc",
    "read_hdf",
    "read_sql",
    "read_sql_query",
    "read_sql_table",
    "read_gbq",
    "ExcelFile",
    "HDFStore",
)
_NUMPY_BLOCKED = ("load", "loadtxt", "genfromtxt", "fromfile", "save", "savez", "savez_compressed", "fromregex")
_DF_BLOCKED = (
    "to_csv",
    "to_excel",
    "to_pickle",
    "to_hdf",
    "to_sql",
    "to_parquet",
    "to_feather",
    "to_orc",
    "to_gbq",
    "to_stata",
)


def _harden_imported_module(name: str, module):
    """Strip filesystem / network I/O from allowlisted scientific libs."""
    root = name.split(".", 1)[0]
    if root == "pandas":
        for attr in _PANDAS_BLOCKED:
            if hasattr(module, attr):
                setattr(module, attr, _deny_io)
        try:
            import pandas as pd

            if hasattr(pd, "DataFrame"):
                for attr in _DF_BLOCKED:
                    if hasattr(pd.DataFrame, attr):
                        setattr(pd.DataFrame, attr, _deny_io)
        except Exception:
            pass
    elif root == "numpy":
        for attr in _NUMPY_BLOCKED:
            if hasattr(module, attr):
                setattr(module, attr, _deny_io)
    elif root == "matplotlib":
        try:
            import matplotlib.pyplot as plt

            if hasattr(plt, "savefig"):
                plt.savefig = _deny_io
        except Exception:
            pass
    return module


def _safe_import(name, globals=None, locals=None, fromlist=(), level=0):  # noqa: A002
    if level and level > 0:
        raise ImportError("Relative import ruxsat etilmagan.")
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
    return _harden_imported_module(name, module)


def build_safe_builtins() -> dict:
    safe = {k: getattr(builtins, k) for k in dir(builtins) if not k.startswith("_")}
    for name in _BLOCKED_BUILTINS:
        safe.pop(name, None)
    safe["__import__"] = _safe_import
    safe["__build_class__"] = builtins.__build_class__
    safe["__name__"] = "__student__"
    # isinstance / issubclass / type(x) kept for pedagogy; dunder attrs blocked by AST.
    return safe


def run_user_code(source: str) -> tuple[str, str, int]:
    """Execute student code. Returns (stdout, stderr, exit_code)."""
    stdout = io.StringIO()
    stderr = io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = stdout, stderr
    code = 0
    try:
        validate_python_source(source)
        compiled = compile(source, "<student>", "exec")
        env: dict = {"__builtins__": build_safe_builtins(), "__name__": "__main__"}
        exec(compiled, env, env)  # noqa: S102 — intentional sandbox exec
    except UnsafePythonError as exc:
        code = 1
        stderr.write(f"Xavfsizlik: {exc}\n")
    except Exception:
        code = 1
        traceback.print_exc(file=stderr)
    finally:
        sys.stdout, sys.stderr = old_out, old_err
    return stdout.getvalue(), stderr.getvalue(), code
