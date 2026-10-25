#!/usr/bin/env python3
"""Compare one Instagram post with a historical CSV baseline.

Standard-library only. This is descriptive analysis, not a virality predictor.
"""

from __future__ import annotations

import argparse
import csv
import json
import statistics
from pathlib import Path


METRICS = ("views", "reach", "likes", "comments", "shares", "saves", "profile_visits", "follows")


def number(value: str | None) -> float | None:
    if value is None or not value.strip():
        return None
    try:
        return float(value.replace(",", "").strip())
    except ValueError:
        return None


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("CSV contains no data rows")
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--post-id", required=True, help="Value from the post_id column")
    args = parser.parse_args()

    rows = load_rows(args.csv_path)
    matches = [row for row in rows if row.get("post_id") == args.post_id]
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one row for post_id={args.post_id!r}; found {len(matches)}")
    current = matches[0]

    comparable = [
        row for row in rows
        if row is not current
        and (not current.get("format") or row.get("format") == current.get("format"))
    ]
    if not comparable:
        raise ValueError("No historical rows with the same format were found")

    results: dict[str, object] = {
        "post_id": args.post_id,
        "format": current.get("format", ""),
        "baseline_posts": len(comparable),
        "warning": "Descriptive account-relative ratios only; not a virality prediction.",
        "metrics": {},
    }

    metric_results: dict[str, object] = {}
    for metric in METRICS:
        current_value = number(current.get(metric))
        history = [value for row in comparable if (value := number(row.get(metric))) is not None]
        if current_value is None or not history:
            continue
        median = statistics.median(history)
        metric_results[metric] = {
            "current": current_value,
            "baseline_median": median,
            "ratio_to_median": None if median == 0 else round(current_value / median, 3),
        }
    results["metrics"] = metric_results
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
