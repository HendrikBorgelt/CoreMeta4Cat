"""
generate_example_outputs.py

Publishes the real-world CatalysisDataset examples (tests/data/valid/
CatalysisDataset-<dataset-id>.yaml, e.g. -2d6m-exeb.yaml) as downloadable
.json and .yaml files under docs/assets/examples/, so the "Working with
Data" documentation page can link to them.

These files are already validated as part of `just test`
(tests/data/valid/ is the schema's test suite); this script only
republishes the already-valid YAML in JSON form and copies the YAML
alongside it, it does not re-validate.

Run:
    just gen-example-outputs
  or directly:
    uv run python scripts/generate_example_outputs.py
"""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = REPO_ROOT / "tests" / "data" / "valid"
OUTPUT_DIR = REPO_ROOT / "docs" / "assets" / "examples"

# Real-world dataset examples, identified by the dataset-id suffix in their
# filename (CatalysisDataset-<suffix>.yaml). Purely-numeric suffixes (001,
# 002, ...) are synthetic schema-testing fixtures and are excluded here --
# only handle-style dataset ids (e.g. 2d6m-exeb) get published.
DATASET_ID_PATTERN = re.compile(r"^CatalysisDataset-(.+)\.yaml$")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    published = []
    for source_file in sorted(SOURCE_DIR.glob("CatalysisDataset-*.yaml")):
        match = DATASET_ID_PATTERN.match(source_file.name)
        if not match:
            continue
        dataset_id = match.group(1)
        if dataset_id.isdigit():
            continue
        with open(source_file, encoding="utf-8") as f:
            data = yaml.safe_load(f)

        yaml_out = OUTPUT_DIR / f"CatalysisDataset-{dataset_id}.yaml"
        shutil.copyfile(source_file, yaml_out)

        json_out = OUTPUT_DIR / f"CatalysisDataset-{dataset_id}.json"
        with open(json_out, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")

        published.append(dataset_id)
        print(f"  OK {yaml_out.relative_to(REPO_ROOT)}")
        print(f"  OK {json_out.relative_to(REPO_ROOT)}")

    print(f"\nPublished {len(published)} example dataset(s) to {OUTPUT_DIR.relative_to(REPO_ROOT)}: {', '.join(published)}")


if __name__ == "__main__":
    main()
