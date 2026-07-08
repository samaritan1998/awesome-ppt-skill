#!/usr/bin/env python3
"""Validate deck_brief.json and slide_plan.json without third-party packages."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


PRIMARY_ROUTES = {
    "native-pptx",
    "edit-existing",
    "template-extract",
    "image-first",
    "reconstruct",
    "html-markdown",
    "google-slides",
    "qa-audit",
}

MODES = {"academic", "business"}

OBJECT_TYPES = {
    "text",
    "title",
    "bullets",
    "image",
    "chart",
    "table",
    "shape",
    "diagram",
    "quote",
    "code",
    "equation",
}


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"__json_error__": str(exc)}


def require(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def validate_brief(brief: dict[str, Any], errors: list[str]) -> None:
    for key in ("task_type", "audience", "goal", "output", "editability"):
        require(errors, key in brief, f"deck_brief missing {key}")
    task_type = brief.get("task_type")
    primary_route = brief.get("primary_route", task_type)
    require(errors, primary_route in PRIMARY_ROUTES, f"primary_route must be one of {sorted(PRIMARY_ROUTES)}")
    for mode in brief.get("modes", []):
        require(errors, mode in MODES, f"unsupported mode: {mode}")
    require(errors, isinstance(brief.get("output", []), list), "deck_brief output must be a list")


def validate_plan(plan: dict[str, Any], errors: list[str]) -> None:
    for key in ("deck_title", "route", "slides"):
        require(errors, key in plan, f"slide_plan missing {key}")

    route = plan.get("route")
    require(errors, route in PRIMARY_ROUTES, f"slide_plan route must be one of {sorted(PRIMARY_ROUTES)}")
    for mode in plan.get("modes", []):
        require(errors, mode in MODES, f"unsupported mode: {mode}")

    slides = plan.get("slides")
    require(errors, isinstance(slides, list) and bool(slides), "slides must be a non-empty list")
    if not isinstance(slides, list):
        return

    for expected, slide in enumerate(slides, start=1):
        path = f"slides[{expected - 1}]"
        require(errors, isinstance(slide, dict), f"{path} must be an object")
        if not isinstance(slide, dict):
            continue
        require(errors, slide.get("slide_no") == expected, f"{path}.slide_no must be {expected}")
        for key in ("title", "takeaway", "layout", "objects"):
            require(errors, key in slide, f"{path} missing {key}")
        objects = slide.get("objects", [])
        require(errors, isinstance(objects, list) and bool(objects), f"{path}.objects must be a non-empty list")
        if not isinstance(objects, list):
            continue
        for index, obj in enumerate(objects):
            obj_path = f"{path}.objects[{index}]"
            require(errors, isinstance(obj, dict), f"{obj_path} must be an object")
            if not isinstance(obj, dict):
                continue
            for key in ("id", "type", "content"):
                require(errors, key in obj, f"{obj_path} missing {key}")
            require(errors, obj.get("type") in OBJECT_TYPES, f"{obj_path}.type is unsupported: {obj.get('type')}")
            bbox = obj.get("bbox")
            if bbox is not None:
                require(errors, isinstance(bbox, dict), f"{obj_path}.bbox must be an object")
                if isinstance(bbox, dict):
                    for key in ("x", "y", "w", "h"):
                        require(errors, isinstance(bbox.get(key), (int, float)), f"{obj_path}.bbox.{key} must be numeric")
                    if isinstance(bbox.get("w"), (int, float)):
                        require(errors, bbox["w"] > 0, f"{obj_path}.bbox.w must be positive")
                    if isinstance(bbox.get("h"), (int, float)):
                        require(errors, bbox["h"] > 0, f"{obj_path}.bbox.h must be positive")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slide_plan", type=Path)
    parser.add_argument("--brief", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    errors: list[str] = []
    plan = load_json(args.slide_plan)
    if "__json_error__" in plan:
        errors.append(f"{args.slide_plan} is not valid JSON: {plan['__json_error__']}")
    elif not isinstance(plan, dict):
        errors.append("slide_plan must be a JSON object")
    else:
        validate_plan(plan, errors)

    if args.brief:
        brief = load_json(args.brief)
        if "__json_error__" in brief:
            errors.append(f"{args.brief} is not valid JSON: {brief['__json_error__']}")
        elif not isinstance(brief, dict):
            errors.append("deck_brief must be a JSON object")
        else:
            validate_brief(brief, errors)
            if isinstance(plan, dict) and "__json_error__" not in plan:
                primary_route = brief.get("primary_route", brief.get("task_type"))
                if primary_route and plan.get("route") and primary_route != plan.get("route"):
                    errors.append(f"brief primary_route ({primary_route}) does not match slide_plan route ({plan.get('route')})")

    report = {"status": "pass" if not errors else "fail", "error_count": len(errors), "errors": errors}
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
