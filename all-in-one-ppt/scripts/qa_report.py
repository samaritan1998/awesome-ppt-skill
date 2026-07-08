#!/usr/bin/env python3
"""Run lightweight structural QA on an all-in-one-ppt slide_plan.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def object_text_length(obj: dict[str, Any]) -> int:
    content = obj.get("content", "")
    if isinstance(content, list):
        return sum(len(str(item)) for item in content)
    if isinstance(content, dict):
        return len(json.dumps(content, ensure_ascii=False))
    return len(str(content))


def overlap(a: dict[str, float], b: dict[str, float]) -> bool:
    return not (
        a["x"] + a["w"] <= b["x"]
        or b["x"] + b["w"] <= a["x"]
        or a["y"] + a["h"] <= b["y"]
        or b["y"] + b["h"] <= a["y"]
    )


def qa(plan: dict[str, Any]) -> dict[str, Any]:
    issues: list[dict[str, Any]] = []
    slides = plan.get("slides", [])
    if not slides:
        issues.append({"severity": "blocker", "slide": None, "issue": "slide_plan has no slides"})

    expected = 1
    for slide in slides:
        no = slide.get("slide_no")
        if no != expected:
            issues.append({"severity": "major", "slide": no, "issue": f"slide_no should be {expected}"})
        expected += 1

        if not slide.get("title"):
            issues.append({"severity": "blocker", "slide": no, "issue": "missing title"})
        if not slide.get("takeaway"):
            issues.append({"severity": "major", "slide": no, "issue": "missing takeaway"})
        objects = slide.get("objects", [])
        if not objects:
            issues.append({"severity": "blocker", "slide": no, "issue": "slide has no objects"})

        total_text = sum(object_text_length(obj) for obj in objects)
        if total_text > 900:
            issues.append({"severity": "major", "slide": no, "issue": f"too much text ({total_text} chars)"})
        elif total_text > 550:
            issues.append({"severity": "minor", "slide": no, "issue": f"dense slide text ({total_text} chars)"})

        for obj in objects:
            if obj.get("type") in {"title", "text", "bullets", "table", "chart", "shape"} and obj.get("editable") is False:
                issues.append({"severity": "major", "slide": no, "issue": f"{obj.get('id')} should usually be editable"})
            bbox = obj.get("bbox")
            if bbox:
                for key in ("x", "y", "w", "h"):
                    if key not in bbox:
                        issues.append({"severity": "major", "slide": no, "issue": f"{obj.get('id')} bbox missing {key}"})
                if bbox.get("w", 1) <= 0 or bbox.get("h", 1) <= 0:
                    issues.append({"severity": "major", "slide": no, "issue": f"{obj.get('id')} has non-positive bbox size"})

        boxes = [(obj.get("id", "?"), obj.get("bbox")) for obj in objects if isinstance(obj.get("bbox"), dict)]
        for i, (id_a, box_a) in enumerate(boxes):
            for id_b, box_b in boxes[i + 1 :]:
                if overlap(box_a, box_b):
                    issues.append({"severity": "major", "slide": no, "issue": f"bbox overlap: {id_a} and {id_b}"})

    status = "pass"
    if any(item["severity"] == "blocker" for item in issues):
        status = "fail"
    elif any(item["severity"] == "major" for item in issues):
        status = "needs-repair"
    return {"status": status, "issue_count": len(issues), "issues": issues}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slide_plan", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    plan = json.loads(args.slide_plan.read_text(encoding="utf-8"))
    report = qa(plan)
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 1 if report["status"] == "fail" else 0


if __name__ == "__main__":
    raise SystemExit(main())
