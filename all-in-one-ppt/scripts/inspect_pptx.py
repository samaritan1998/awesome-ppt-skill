#!/usr/bin/env python3
"""Inspect PPTX package structure and compare native objects with a slide plan."""

from __future__ import annotations

import argparse
import json
import re
import zipfile
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET


NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "c": "http://schemas.openxmlformats.org/drawingml/2006/chart",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
}


def slide_number(name: str) -> int:
    match = re.search(r"slide(\d+)\.xml$", name)
    return int(match.group(1)) if match else 0


def add_issue(issues: list[dict[str, Any]], severity: str, slide: int | None, issue: str) -> None:
    issues.append({"severity": severity, "slide": slide, "issue": issue})


def load_plan(path: Path | None) -> dict[str, Any] | None:
    if path is None:
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def inspect(deck_path: Path, plan: dict[str, Any] | None) -> dict[str, Any]:
    issues: list[dict[str, Any]] = []
    slides_report: list[dict[str, Any]] = []

    try:
        archive = zipfile.ZipFile(deck_path)
    except (FileNotFoundError, zipfile.BadZipFile) as exc:
        return {"status": "fail", "issue_count": 1, "issues": [{"severity": "blocker", "slide": None, "issue": str(exc)}]}

    with archive:
        names = set(archive.namelist())
        if "ppt/presentation.xml" not in names:
            add_issue(issues, "blocker", None, "missing ppt/presentation.xml")
            return {"status": "fail", "issue_count": len(issues), "issues": issues}

        presentation = ET.fromstring(archive.read("ppt/presentation.xml"))
        size = presentation.find("p:sldSz", NS)
        slide_width = int(size.get("cx", "12192000")) if size is not None else 12192000
        slide_height = int(size.get("cy", "6858000")) if size is not None else 6858000
        slide_area = slide_width * slide_height

        slide_names = sorted(
            (name for name in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)),
            key=slide_number,
        )
        if not slide_names:
            add_issue(issues, "blocker", None, "PPTX contains no slides")

        expected_slides = plan.get("slides", []) if plan else []
        if plan and len(slide_names) != len(expected_slides):
            add_issue(issues, "blocker", None, f"slide count mismatch: PPTX={len(slide_names)}, plan={len(expected_slides)}")

        for index, name in enumerate(slide_names, start=1):
            root = ET.fromstring(archive.read(name))
            texts = [node.text or "" for node in root.findall(".//a:t", NS)]
            pictures = root.findall(".//p:pic", NS)
            tables = root.findall(".//a:tbl", NS)
            charts = root.findall(".//c:chart", NS)
            shapes = root.findall(".//p:sp", NS)
            connector_shapes = root.findall(".//p:cxnSp", NS)
            line_shapes = [
                shape
                for shape in shapes
                if (geometry := shape.find("p:spPr/a:prstGeom", NS)) is not None
                and geometry.get("prst") == "line"
            ]
            connector_count = len(connector_shapes) + len(line_shapes)

            full_slide_pictures = 0
            for picture in pictures:
                xfrm = picture.find("p:spPr/a:xfrm", NS)
                ext = xfrm.find("a:ext", NS) if xfrm is not None else None
                if ext is None:
                    continue
                width = int(ext.get("cx", "0"))
                height = int(ext.get("cy", "0"))
                if slide_area and (width * height) / slide_area >= 0.9:
                    full_slide_pictures += 1

            if full_slide_pictures and not any(text.strip() for text in texts):
                add_issue(issues, "blocker", index, "slide is effectively a full-slide bitmap with no native text")

            metrics = {
                "slide": index,
                "text_runs": len(texts),
                "shapes": len(shapes),
                "connectors": connector_count,
                "pictures": len(pictures),
                "tables": len(tables),
                "charts": len(charts),
                "full_slide_pictures": full_slide_pictures,
            }
            slides_report.append(metrics)

            if index <= len(expected_slides):
                expected = expected_slides[index - 1]
                objects = expected.get("objects", [])
                expected_counts = {
                    "image": sum(obj.get("type") == "image" for obj in objects),
                    "table": sum(obj.get("type") == "table" and obj.get("materialization") == "native" for obj in objects),
                    "chart": sum(obj.get("type") == "chart" and obj.get("materialization") == "native" for obj in objects),
                    "connector": sum(obj.get("type") == "connector" and obj.get("materialization") == "native" for obj in objects),
                }
                if len(pictures) < expected_counts["image"]:
                    add_issue(issues, "blocker", index, "fewer image objects than declared in the plan")
                if len(tables) < expected_counts["table"]:
                    add_issue(issues, "blocker", index, "native table declared in plan but missing from PPTX")
                if len(charts) < expected_counts["chart"]:
                    add_issue(issues, "blocker", index, "native chart declared in plan but missing from PPTX")
                if connector_count < expected_counts["connector"]:
                    add_issue(issues, "major", index, "native connector declared in plan but missing from PPTX")
                if expected.get("title") and not any(text.strip() for text in texts):
                    add_issue(issues, "blocker", index, "planned native title/text is missing from PPTX")

        status = "pass"
        if any(issue["severity"] == "blocker" for issue in issues):
            status = "fail"
        elif any(issue["severity"] == "major" for issue in issues):
            status = "needs-repair"

        return {
            "status": status,
            "slide_count": len(slide_names),
            "slide_size_emu": {"width": slide_width, "height": slide_height},
            "slides": slides_report,
            "issue_count": len(issues),
            "issues": issues,
        }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--plan", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    report = inspect(args.pptx, load_plan(args.plan))
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
