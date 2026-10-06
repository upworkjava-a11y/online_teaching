"""Run student Python snippets for lesson playground (subprocess + timeout)."""

from __future__ import annotations

import logging
import os
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

from django.conf import settings

from .exceptions import QueryLimitError, QueryTimeoutError, SandboxError

logger = logging.getLogger("apps.sandbox")

_WORKER = r'''
import sys
from apps.sandbox.python_safe import run_user_code
source = sys.stdin.read()
out, err, code = run_user_code(source)
sys.stdout.write(out)
sys.stderr.write(err)
raise SystemExit(code)
'''


@dataclass
class PythonResult:
    stdout: str
    stderr: str
    ok: bool
    execution_ms: int = 0


class PythonExecutor:
    def execute(self, source: str) -> PythonResult:
        text = (source or "").strip()
        max_chars = int(getattr(settings, "SANDBOX_MAX_QUERY_CHARS", 8000))
        if not text:
            raise SandboxError("Kod bo‘sh.", "empty")
        if len(text) > max_chars:
            raise QueryLimitError("Kod juda uzun. Qisqartiring.")

        timeout = int(getattr(settings, "SANDBOX_QUERY_TIMEOUT_SECONDS", 5))
        max_output = int(getattr(settings, "PYTHON_SANDBOX_MAX_OUTPUT_CHARS", 20000))
        root = Path(settings.BASE_DIR)
        env = os.environ.copy()
        env["PYTHONPATH"] = str(root) + os.pathsep + env.get("PYTHONPATH", "")
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        # Block network-ish libs from picking up proxies accidentally — still rely on import allowlist.
        env.pop("HTTP_PROXY", None)
        env.pop("HTTPS_PROXY", None)

        started = __import__("time").monotonic()
        try:
            proc = subprocess.run(  # noqa: S603
                [sys.executable, "-B", "-c", _WORKER],
                input=text,
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=tempfile.gettempdir(),
                env=env,
            )
        except subprocess.TimeoutExpired as exc:
            logger.warning("python_timeout")
            raise QueryTimeoutError(
                "Kod juda uzoq ishladi. Tsikl yoki og‘ir hisobni soddalashtiring."
            ) from exc
        except Exception as exc:
            logger.warning("python_exec_error", extra={"error": type(exc).__name__})
            raise SandboxError(f"Python ishga tushmadi: {exc}") from exc

        ms = int((__import__("time").monotonic() - started) * 1000)
        stdout = (proc.stdout or "")[:max_output]
        stderr = (proc.stderr or "")[:max_output]
        if len(proc.stdout or "") > max_output or len(proc.stderr or "") > max_output:
            stderr = (stderr + "\n… (chiqish qisqartirildi)").strip()
        return PythonResult(
            stdout=stdout,
            stderr=stderr,
            ok=proc.returncode == 0,
            execution_ms=ms,
        )


python_executor = PythonExecutor()
