#!/usr/bin/env python3
"""Run plan-level structural and editability QA for all-in-one-ppt."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


NATIVE_REQUIRED = {"text", "bullets", "chart", "table", "shape", "connector", "diagram", "quote", "code"}


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


def add_issue(issues: list[dict[str, Any]], severity: str, slide: int | None, issue: str, obj: str | None = None) -> None:
    item: dict[str, Any] = {"severity": severity, "slide": slide, "issue": issue}
    if obj:
        item["object"] = obj
    issues.append(item)


def qa(plan: dict[str, Any]) -> dict[str, Any]:
    issues: list[dict[str, Any]] = []
    slides = plan.get("slides", [])
    if not slides:
        add_issue(issues, "blocker", None, "slide_plan has no slides")

    canvas = plan.get("canvas", {})
    canvas_width = float(canvas.get("width", 13.333))
    canvas_height = float(canvas.get("height", 7.5))
    canvas_area = canvas_width * canvas_height

    assets = {asset.get("id"): asset for asset in plan.get("assets", []) if isinstance(asset, dict) and asset.get("id")}
    asset_usage: Counter[str] = Counter()

    expected = 1
    for slide in slides:
        no = slide.get("slide_no")
        if no != expected:
            add_issue(issues, "major", no, f"slide_no should be {expected}")
        expected += 1

        if not slide.get("title"):
            add_issue(issues, "blocker", no, "missing title")
        if not slide.get("purpose"):
            add_issue(issues, "major", no, "missing purpose")
        if not slide.get("takeaway"):
            add_issue(issues, "major", no, "missing takeaway")

        objects = slide.get("objects", [])
        if not objects:
            add_issue(issues, "blocker", no, "slide has no objects")
            continue

        total_text = sum(object_text_length(obj) for obj in objects)
        if total_text > 900:
            add_issue(issues, "major", no, f"too much text ({total_text} chars)")
        elif total_text > 550:
            add_issue(issues, "minor", no, f"dense slide text ({total_text} chars)")

        boxes: list[tuple[dict[str, Any], dict[str, float]]] = []
        for obj in objects:
            obj_id = str(obj.get("id", "?"))
            obj_type = obj.get("type")
            materialization = obj.get("materialization")

            if materialization == "native" and obj.get("editable") is not True:
                add_issue(issues, "major", no, "native object is not marked editable", obj_id)
            if materialization == "raster" and obj.get("editable") is not False:
                add_issue(issues, "major", no, "raster object must not claim internal editability", obj_id)
            if obj_type in NATIVE_REQUIRED and materialization != "native":
                severity = "blocker" if not obj.get("raster_reason") else "major"
                add_issue(issues, severity, no, f"semantic {obj_type} should be native", obj_id)

            if obj_type == "image":
                asset_id = obj.get("asset_id")
                if not asset_id or asset_id not in assets:
                    add_issue(issues, "major", no, "image does not reference a declared asset", obj_id)
                else:
                    asset_usage[asset_id] += 1
                if obj.get("replaceable") is not True:
                    add_issue(issues, "major", no, "image is not marked replaceable", obj_id)

            bbox = obj.get("bbox")
            if isinstance(bbox, dict) and all(isinstance(bbox.get(key), (int, float)) for key in ("x", "y", "w", "h")):
                if bbox["w"] <= 0 or bbox["h"] <= 0:
                    add_issue(issues, "major", no, "non-positive bbox size", obj_id)
                if bbox["x"] < 0 or bbox["y"] < 0 or bbox["x"] + bbox["w"] > canvas_width or bbox["y"] + bbox["h"] > canvas_height:
                    add_issue(issues, "major", no, "object exceeds slide canvas", obj_id)

                coverage = (bbox["w"] * bbox["h"]) / canvas_area if canvas_area else 0
                if obj_type == "image" and coverage >= 0.9 and obj.get("role") != "background":
                    add_issue(issues, "blocker", no, "full-slide raster image is not an explicit background", obj_id)
                boxes.append((obj, bbox))

        for index, (obj_a, box_a) in enumerate(boxes):
            for obj_b, box_b in boxes[index + 1 :]:
                if obj_a.get("allow_overlap") or obj_b.get("allow_overlap"):
                    continue
                if obj_a.get("role") == "background" or obj_b.get("role") == "background":
                    continue
                if overlap(box_a, box_b):
                    add_issue(
                        issues,
                        "major",
                        no,
                        f"bbox overlap: {obj_a.get('id', '?')} and {obj_b.get('id', '?')}",
                    )

    for asset_id, asset in assets.items():
        if asset.get("source") == "imagegen":
            if not asset.get("prompt"):
                add_issue(issues, "major", None, f"generated asset {asset_id} has no saved prompt")
            if not asset.get("alt_text"):
                add_issue(issues, "minor", None, f"generated asset {asset_id} has no alt text")
        if asset_usage[asset_id] > 1 and not asset.get("reusable"):
            add_issue(issues, "minor", None, f"asset {asset_id} is reused on {asset_usage[asset_id]} slides")

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
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
