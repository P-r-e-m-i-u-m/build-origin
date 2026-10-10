#!/usr/bin/env python3
"""Lost Paths: search, track, and learn from past experiments."""

import argparse
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RECORDS = ROOT / "experiments.json"
OUTCOMES = ("success", "failed", "abandoned", "inconclusive")


def load_records():
    if not RECORDS.exists():
        return []

    try:
        data = json.loads(RECORDS.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        raise SystemExit(f"Cannot read {RECORDS.name}: {exc}")

    if not isinstance(data, list):
        raise SystemExit(f"{RECORDS.name} must contain a JSON list.")

    if not all(isinstance(item, dict) for item in data):
        raise SystemExit("Every experiment must be a JSON object.")

    return data


def save_records(records):
    temporary = RECORDS.with_suffix(".json.tmp")
    try:
        temporary.write_text(
            json.dumps(records, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        temporary.replace(RECORDS)
    except OSError as exc:
        temporary.unlink(missing_ok=True)
        raise SystemExit(f"Cannot save experiments: {exc}")


def add_record(args):
    fields = {
        "title": args.title.strip(),
        "idea": args.idea.strip(),
        "reason": args.reason.strip(),
        "evidence": args.evidence.strip(),
    }

    for name in ("title", "idea", "reason"):
        if not fields[name]:
            raise SystemExit(f"{name.capitalize()} must not be empty.")

    records = load_records()
    now = datetime.now(timezone.utc)
    record = {
        "id": f"LP-{now.strftime('%Y%m%dT%H%M%S%fZ')}",
        "created_at": now.isoformat(timespec="microseconds"),
        **fields,
        "outcome": args.outcome,
    }

    records.append(record)
    save_records(records)
    print(f"Recorded {record['id']}: {record['title']}")
    print(f"Outcome: {record['outcome']}")


def list_records(args):
    records = load_records()

    if args.outcome:
        records = [
            r for r in records
            if r.get("outcome") == args.outcome
        ]

    if not records:
        print("No matching experiments found.")
        return

    for record in records:
        print(f"\n[{record.get('id', '?')}] {record.get('title', 'Untitled')}")
        print(f"Date: {record.get('created_at', 'Unknown')}")
        print(f"Outcome: {record.get('outcome', 'unknown')}")
        print(f"Idea: {record.get('idea', '')}")
        print(f"Reason: {record.get('reason', '')}")
        if record.get("evidence"):
            print(f"Evidence: {record['evidence']}")

    print(f"\nShowing {len(records)} experiment(s).")


def search_records(args):
    records = load_records()
    query = args.query.strip().casefold()

    if not query:
        raise SystemExit("Search query cannot be empty.")

    matches = []
    for record in records:
        searchable = " ".join(
            str(record.get(key, ""))
            for key in ("id", "title", "idea", "outcome", "reason", "evidence")
        )
        if query in searchable.casefold():
            matches.append(record)

    if not matches:
        print(f"No experiments matched '{args.query}'.")
        return

    print(f"Found {len(matches)} matching experiment(s):")
    for record in matches:
        print(
            f"\n[{record.get('id', '?')}] "
            f"{record.get('title', 'Untitled')} "
            f"({record.get('outcome', 'unknown')})"
        )
        print(f"Reason: {record.get('reason', '')}")
        if record.get("evidence"):
            print(f"Evidence: {record['evidence']}")


def show_stats(_args):
    records = load_records()
    counts = Counter(r.get("outcome", "unknown") for r in records)
    total = len(records)

    print("LOST PATHS | EXPERIMENT SUMMARY")
    print(f"Total experiments: {total}")

    for outcome in (*OUTCOMES, "unknown"):
        count = counts.get(outcome, 0)
        if count or outcome != "unknown":
            percentage = (count / total * 100) if total else 0
            print(f"{outcome.capitalize():<14} {count:>4}  ({percentage:.1f}%)")

    if total:
        resolved = counts.get("success", 0) + counts.get("failed", 0)
        print(f"\nRecorded successes: {counts.get('success', 0)}")
        print(f"Unresolved paths: {counts.get('abandoned', 0) + counts.get('inconclusive', 0)}")


def build_parser():
    parser = argparse.ArgumentParser(
        description="Keep the reasoning behind experiments and past decisions."
    )
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="Record an experiment")
    add.add_argument("--title", required=True, help="Short experiment title")
    add.add_argument("--idea", required=True, help="What you wanted to try")
    add.add_argument("--outcome", required=True, choices=OUTCOMES)
    add.add_argument("--reason", required=True, help="Why it ended this way")
    add.add_argument("--evidence", default="", help="Optional result, link, or observation")
    add.set_defaults(func=add_record)

    show = commands.add_parser("list", help="List recorded experiments")
    show.add_argument("--outcome", choices=OUTCOMES, help="Filter by outcome")
    show.set_defaults(func=list_records)

    search = commands.add_parser("search", help="Search experiment history")
    search.add_argument("query", help="Text to find across experiment records")
    search.set_defaults(func=search_records)

    stats = commands.add_parser("stats", help="Summarize experiment outcomes")
    stats.set_defaults(func=show_stats)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
