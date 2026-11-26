import argparse
import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASELINE = "so4_bilingual_full_ps3_pc_jp_zh"
WORKING = ROOT / "tsv" / "so4_working.tsv"
WORK_FIELDS = ("stable_id", "module", "workflow", "zh_edit")


def read_baseline():
    rows = json.loads((ROOT / f"{BASELINE}.json").read_text(encoding="utf-8"))
    with (ROOT / "tsv" / f"{BASELINE}.tsv").open(
        encoding="utf-8-sig", newline=""
    ) as file:
        reader = csv.DictReader(file, delimiter="\t", strict=True)
        if not rows or reader.fieldnames != list(rows[0]):
            raise ValueError("Baseline header mismatch")
        ids = set()
        for json_row, tsv_row in zip(rows, reader, strict=True):
            stable_id = json_row["stable_id"]
            if not stable_id or stable_id in ids:
                raise ValueError(f"Missing or duplicate stable ID: {stable_id!r}")
            if {key: str(value) for key, value in json_row.items()} != tsv_row:
                raise ValueError(f"Baseline mismatch at {stable_id}")
            ids.add(stable_id)
    return rows


def workflow(row):
    if row["pc_zh"].strip():
        return "polish"
    if row["ps3_jp"].strip() or row["pc_jp"].strip():
        return "translate_then_polish"
    return "no_source"


def main():
    parser = argparse.ArgumentParser(description="Verify the SO4 localization tables.")
    parser.add_argument("--init", action="store_true", help="Create a new work queue.")
    args = parser.parse_args()
    try:
        rows = read_baseline()
        expected = [(row["stable_id"], row["module"], workflow(row)) for row in rows]
        if args.init:
            with WORKING.open("x", encoding="utf-8", newline="") as file:
                writer = csv.writer(file, delimiter="\t", lineterminator="\n")
                writer.writerow(WORK_FIELDS)
                writer.writerows((*row, "") for row in expected)

        edited = 0
        with WORKING.open(encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file, delimiter="\t", strict=True)
            if reader.fieldnames != list(WORK_FIELDS):
                raise ValueError("Work queue header mismatch")
            for (stable_id, module, route), row in zip(expected, reader, strict=True):
                edit = row.pop("zh_edit")
                if edit is None or row != dict(
                    stable_id=stable_id, module=module, workflow=route
                ):
                    raise ValueError(f"Work queue mismatch at {stable_id}")
                if edit and (route == "no_source" or not edit.strip()):
                    raise ValueError(f"Invalid Chinese override at {stable_id}")
                edited += bool(edit)
    except (OSError, ValueError, csv.Error) as error:
        parser.exit(1, f"Alignment check failed: {error}\n")

    counts = Counter(route for _, _, route in expected)
    summary = ", ".join(f"{route}={counts[route]}" for route in (
        "polish", "translate_then_polish", "no_source"
    ))
    print(f"Verified {len(expected):,} records ({summary}, edited={edited}).")


if __name__ == "__main__":
    main()
