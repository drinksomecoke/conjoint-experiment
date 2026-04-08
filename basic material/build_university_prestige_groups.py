from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


SOURCE = Path("/Users/dingshaokai/work/cv_project/tonglin/resume-generator/us_news.csv")
OUTPUT_DIR = Path("/Users/dingshaokai/work/cv_project/conjoint experiment/basic material")
YEAR = "2026"
GROUP_SIZE = 20


def main() -> None:
    df = pd.read_csv(SOURCE)
    df = df.dropna(subset=[YEAR]).copy()
    df[YEAR] = pd.to_numeric(df[YEAR], errors="coerce")
    df = df.dropna(subset=[YEAR]).sort_values([YEAR, "University Name"]).reset_index(drop=True)

    total = len(df)
    base = total // 3
    remainder = total % 3
    third_sizes = [base + (1 if i < remainder else 0) for i in range(3)]

    starts = [0, third_sizes[0], third_sizes[0] + third_sizes[1]]
    ends = [third_sizes[0], third_sizes[0] + third_sizes[1], total]
    specs = [
        ("highly_prestigious", "Graduated from a highly prestigious university"),
        ("mid_tier", "Graduated from a mid-tier university"),
        ("less_prestigious", "Graduated from a less prestigious university"),
    ]

    groups: dict[str, dict] = {}
    rows: list[dict] = []

    for group_index, ((group_key, label), start, end) in enumerate(zip(specs, starts, ends), start=1):
        chunk = df.iloc[start:end].copy()
        selected = chunk.head(GROUP_SIZE).copy()

        records = []
        for within_group_rank, (_, row) in enumerate(selected.iterrows(), start=1):
            record = {
                "university_name": row["University Name"],
                "state": row["State"],
                "ipeds": int(row["IPEDS"]),
                "rank_2026": int(row[YEAR]),
                "overall_sorted_position": int(start + within_group_rank),
                "within_group_order": within_group_rank,
                "prestige_group": group_key,
                "prestige_label": label,
            }
            records.append(record)
            rows.append(record)

        groups[group_key] = {
            "label": label,
            "group_index": group_index,
            "source_slice_start": start + 1,
            "source_slice_end": end,
            "source_slice_rank_min": int(chunk[YEAR].min()),
            "source_slice_rank_max": int(chunk[YEAR].max()),
            "selected_count": len(records),
            "selected_rank_min": int(selected[YEAR].min()),
            "selected_rank_max": int(selected[YEAR].max()),
            "universities": records,
        }

    json_payload = {
        "source_file": str(SOURCE),
        "ranking_year": int(YEAR),
        "total_ranked_universities_used": total,
        "tertile_sizes": third_sizes,
        "selection_rule": (
            "Sort by 2026 US News rank ascending, split the ranked schools into three equal tertiles, "
            "then take the first 20 schools from each tertile."
        ),
        "groups": groups,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "university_prestige_groups_2026.json").write_text(
        json.dumps(json_payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    pd.DataFrame(rows).to_csv(OUTPUT_DIR / "university_prestige_groups_2026.csv", index=False)


if __name__ == "__main__":
    main()
