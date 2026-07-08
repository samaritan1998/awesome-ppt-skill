#!/usr/bin/env python3
"""Repo-root wrapper for the all-in-one PPT skill validator."""

from __future__ import annotations

import runpy
import sys
from pathlib import Path


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    validator = Path(__file__).resolve().parent / "all-in-one-ppt/scripts/quick_validate.py"
    if not validator.exists():
        fail(f"missing validator: {validator}")
    runpy.run_path(str(validator), run_name="__main__")


if __name__ == "__main__":
    main()
