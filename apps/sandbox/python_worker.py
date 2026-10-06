"""Standalone worker process for student Python snippets (no Django)."""

from __future__ import annotations

import sys

from apps.sandbox.python_safe import run_user_code


def main() -> int:
    source = sys.stdin.read()
    out, err, code = run_user_code(source)
    sys.stdout.write(out)
    sys.stderr.write(err)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
