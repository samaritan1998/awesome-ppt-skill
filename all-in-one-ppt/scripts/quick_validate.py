#!/usr/bin/env python3
"""Quick structural validation for the all-in-one PPT skill."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "package.json",
    "agents/openai.yaml",
    "references/router.md",
    "references/editability_contract.md",
    "references/workflows.md",
    "references/qa_checklist.md",
    "references/design_system.md",
    "references/image_assets.md",
    "references/academic_mode.md",
    "references/business_mode.md",
    "references/security.md",
    "schemas/deck_brief.schema.json",
    "schemas/slide_plan.schema.json",
    "scripts/quick_validate.py",
    "scripts/validate_plan.py",
    "scripts/plan_from_markdown.py",
    "scripts/qa_report.py",
    "scripts/html_preview.py",
    "scripts/render_pptx_preview.sh",
    "scripts/build_pptx_pptxgenjs.mjs",
    "scripts/inspect_pptx.py",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_skill_md(skill_md: Path) -> None:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML front matter")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        fail("SKILL.md front matter is not closed")
    front_matter = parts[1]
    body = parts[2]
    for key in ("name:", "description:"):
        if key not in front_matter:
            fail(f"SKILL.md front matter missing {key}")
    if "# All-in-One Editable PowerPoint" not in body:
        fail("SKILL.md missing # All-in-One Editable PowerPoint heading")


def validate_json(path: Path) -> None:
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path} is not valid JSON: {exc}")


def main() -> None:
    if len(sys.argv) > 2:
        fail("usage: python3 scripts/quick_validate.py [path/to/all-in-one-ppt]")

    if len(sys.argv) == 2:
        skill_dir = Path(sys.argv[1]).resolve()
    else:
        skill_dir = Path(__file__).resolve().parents[1]

    if not skill_dir.is_dir():
        fail(f"{skill_dir} is not a directory")

    missing = [rel for rel in REQUIRED_FILES if not (skill_dir / rel).exists()]
    if missing:
        fail("missing required files: " + ", ".join(missing))

    validate_skill_md(skill_dir / "SKILL.md")
    validate_json(skill_dir / "schemas/deck_brief.schema.json")
    validate_json(skill_dir / "schemas/slide_plan.schema.json")
    validate_json(skill_dir / "package.json")

    for script in skill_dir.glob("scripts/*.py"):
        compile(script.read_text(encoding="utf-8"), str(script), "exec")

    render_script = skill_dir / "scripts/render_pptx_preview.sh"
    if not render_script.read_text(encoding="utf-8").startswith("#!/usr/bin/env bash"):
        fail("scripts/render_pptx_preview.sh must be a bash script")

    print(f"OK: {skill_dir.name} has {len(REQUIRED_FILES)} required files")


if __name__ == "__main__":
    main()
