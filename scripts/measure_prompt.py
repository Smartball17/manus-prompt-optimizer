#!/usr/bin/env python3
"""Compare visible-text metrics for two UTF-8 prompt files.

This tool intentionally does not estimate model tokens, cost, or latency. Those
values depend on the model and runtime. It reports deterministic design metrics
that support a before/after review.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

WORD_RE = re.compile(r"\b[\wÀ-ÖØ-öø-ÿ'-]+\b", re.UNICODE)
WHITESPACE_RE = re.compile(r"\s+")


def normalise_line(line: str) -> str:
    return WHITESPACE_RE.sub(" ", line).strip().casefold()


def metric(path: Path) -> dict[str, Any]:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise ValueError(f"File does not exist: {path}") from None
    except UnicodeDecodeError:
        raise ValueError(f"File is not UTF-8 encoded: {path}") from None

    lines = text.splitlines()
    nonempty = [line for line in lines if line.strip()]
    normalised = [normalise_line(line) for line in nonempty]
    frequencies = Counter(line for line in normalised if line)
    duplicate_groups = sum(1 for count in frequencies.values() if count > 1)
    duplicate_extra_lines = sum(count - 1 for count in frequencies.values() if count > 1)

    return {
        "path": str(path),
        "characters": len(text),
        "bytes_utf8": len(text.encode("utf-8")),
        "words": len(WORD_RE.findall(text)),
        "lines": len(lines),
        "nonempty_lines": len(nonempty),
        "duplicate_line_groups": duplicate_groups,
        "duplicate_extra_lines": duplicate_extra_lines,
    }


def delta(before: int, after: int) -> dict[str, float | int | None]:
    absolute = after - before
    percent = None if before == 0 else round((absolute / before) * 100, 1)
    return {"absolute": absolute, "percent": percent}


def compare(before: dict[str, Any], after: dict[str, Any]) -> dict[str, Any]:
    keys = [
        "characters",
        "bytes_utf8",
        "words",
        "lines",
        "nonempty_lines",
        "duplicate_line_groups",
        "duplicate_extra_lines",
    ]
    return {key: delta(before[key], after[key]) for key in keys}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare visible-text metrics for two UTF-8 prompt files."
    )
    parser.add_argument("original", type=Path, help="Original prompt file")
    parser.add_argument("optimized", type=Path, help="Optimized prompt file")
    args = parser.parse_args()

    try:
        original = metric(args.original)
        optimized = metric(args.optimized)
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2

    result = {
        "notice": (
            "Metrics compare visible text. They are not runtime tokens, cost, "
            "or latency."
        ),
        "original": original,
        "optimized": optimized,
        "optimized_minus_original": compare(original, optimized),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
