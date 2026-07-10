#!/usr/bin/env python3
"""Validate editable-PPTX deck_brief.json and slide_plan.json contracts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


PRIMARY_ROUTES = {"create", "edit", "reconstruct", "audit-repair"}
MODIFIERS = {"template", "academic", "business"}
OBJECT_TYPES = {
    "text",
    "bullets",
    "image",
    "chart",
    "table",
    "shape",
    "connector",
    "diagram",
    "icon",
    "quote",
    "code",
    "equation",
    "video",
}
MATERIALIZATIONS = {"native", "raster", "hybrid"}
NATIVE_REQUIRED = {"text", "bullets", "chart", "table", "shape", "connector", "diagram", "quote", "code"}
ASSET_SOURCES = {"supplied", "search", "imagegen", "derived"}
ASSET_STATUSES = {"planned", "ready", "rejected"}


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"__json_error__": str(exc)}


def require(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def validate_brief(brief: dict[str, Any], errors: list[str]) -> None:
    for key in ("route", "audience", "goal", "deliverable", "editability"):
        require(errors, key in brief, f"deck_brief missing {key}")

    require(errors, brief.get("route") in PRIMARY_ROUTES, f"route must be one of {sorted(PRIMARY_ROUTES)}")
    for modifier in brief.get("modifiers", []):
        require(errors, modifier in MODIFIERS, f"unsupported modifier: {modifier}")

    deliverable = brief.get("deliverable")
    require(errors, isinstance(deliverable, dict), "deck_brief deliverable must be an object")
    if isinstance(deliverable, dict):
        require(errors, deliverable.get("format") == "pptx", "deliverable.format must be pptx")
        require(errors, deliverable.get("editable") is True, "deliverable.editable must be true")

    editability = brief.get("editability")
    require(errors, isinstance(editability, dict), "deck_brief editability must be an object")
    if isinstance(editability, dict):
        require(errors, editability.get("policy") == "native-first", "editability.policy must be native-first")
        require(
            errors,
            editability.get("full_slide_raster_allowed") is False,
            "editability.full_slide_raster_allowed must be false",
        )


def validate_bbox(
    bbox: Any,
    obj_path: str,
    canvas_width: float,
    canvas_height: float,
    errors: list[str],
) -> None:
    require(errors, isinstance(bbox, dict), f"{obj_path}.bbox must be an object")
    if not isinstance(bbox, dict):
        return

    for key in ("x", "y", "w", "h"):
        require(errors, isinstance(bbox.get(key), (int, float)), f"{obj_path}.bbox.{key} must be numeric")
    if not all(isinstance(bbox.get(key), (int, float)) for key in ("x", "y", "w", "h")):
        return

    require(errors, bbox["x"] >= 0 and bbox["y"] >= 0, f"{obj_path}.bbox must start inside the slide")
    require(errors, bbox["w"] > 0 and bbox["h"] > 0, f"{obj_path}.bbox size must be positive")
    require(errors, bbox["x"] + bbox["w"] <= canvas_width + 1e-6, f"{obj_path}.bbox exceeds slide width")
    require(errors, bbox["y"] + bbox["h"] <= canvas_height + 1e-6, f"{obj_path}.bbox exceeds slide height")


def validate_plan(plan: dict[str, Any], errors: list[str]) -> None:
    for key in ("deck_title", "route", "canvas", "assets", "slides"):
        require(errors, key in plan, f"slide_plan missing {key}")

    require(errors, plan.get("route") in PRIMARY_ROUTES, f"slide_plan route must be one of {sorted(PRIMARY_ROUTES)}")
    for modifier in plan.get("modifiers", []):
        require(errors, modifier in MODIFIERS, f"unsupported modifier: {modifier}")

    canvas = plan.get("canvas")
    require(errors, isinstance(canvas, dict), "slide_plan canvas must be an object")
    canvas_width = 13.333
    canvas_height = 7.5
    if isinstance(canvas, dict):
        require(errors, canvas.get("unit") == "in", "canvas.unit must be in")
        require(errors, isinstance(canvas.get("width"), (int, float)), "canvas.width must be numeric")
        require(errors, isinstance(canvas.get("height"), (int, float)), "canvas.height must be numeric")
        if isinstance(canvas.get("width"), (int, float)) and canvas["width"] > 0:
            canvas_width = float(canvas["width"])
        else:
            errors.append("canvas.width must be positive")
        if isinstance(canvas.get("height"), (int, float)) and canvas["height"] > 0:
            canvas_height = float(canvas["height"])
        else:
            errors.append("canvas.height must be positive")

    assets = plan.get("assets")
    require(errors, isinstance(assets, list), "assets must be a list")
    asset_ids: set[str] = set()
    if isinstance(assets, list):
        for index, asset in enumerate(assets):
            path = f"assets[{index}]"
            require(errors, isinstance(asset, dict), f"{path} must be an object")
            if not isinstance(asset, dict):
                continue
            asset_id = asset.get("id")
            require(errors, isinstance(asset_id, str) and bool(asset_id), f"{path}.id must be a non-empty string")
            if isinstance(asset_id, str) and asset_id:
                require(errors, asset_id not in asset_ids, f"duplicate asset id: {asset_id}")
                asset_ids.add(asset_id)
            require(errors, asset.get("source") in ASSET_SOURCES, f"{path}.source is unsupported")
            require(errors, asset.get("status") in ASSET_STATUSES, f"{path}.status is unsupported")
            if asset.get("source") == "imagegen":
                require(errors, bool(asset.get("prompt")), f"{path}.prompt is required for imagegen assets")
                require(errors, bool(asset.get("alt_text")), f"{path}.alt_text is required for imagegen assets")
            if asset.get("status") == "ready":
                require(errors, bool(asset.get("path")), f"{path}.path is required when status is ready")

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
        for key in ("title", "purpose", "takeaway", "layout", "objects"):
            require(errors, key in slide, f"{path} missing {key}")

        objects = slide.get("objects", [])
        require(errors, isinstance(objects, list) and bool(objects), f"{path}.objects must be a non-empty list")
        if not isinstance(objects, list):
            continue

        object_ids: set[str] = set()
        for index, obj in enumerate(objects):
            obj_path = f"{path}.objects[{index}]"
            require(errors, isinstance(obj, dict), f"{obj_path} must be an object")
            if not isinstance(obj, dict):
                continue
            for key in ("id", "type", "content", "materialization", "editable"):
                require(errors, key in obj, f"{obj_path} missing {key}")

            obj_id = obj.get("id")
            require(errors, isinstance(obj_id, str) and bool(obj_id), f"{obj_path}.id must be a non-empty string")
            if isinstance(obj_id, str) and obj_id:
                require(errors, obj_id not in object_ids, f"duplicate object id on slide {expected}: {obj_id}")
                object_ids.add(obj_id)

            obj_type = obj.get("type")
            materialization = obj.get("materialization")
            require(errors, obj_type in OBJECT_TYPES, f"{obj_path}.type is unsupported: {obj_type}")
            require(errors, materialization in MATERIALIZATIONS, f"{obj_path}.materialization is unsupported")
            require(errors, isinstance(obj.get("editable"), bool), f"{obj_path}.editable must be boolean")

            if materialization == "native":
                require(errors, obj.get("editable") is True, f"{obj_path} is native and must be editable")
            if materialization == "raster":
                require(errors, obj.get("editable") is False, f"{obj_path} is raster and editable must be false")
            if obj_type in NATIVE_REQUIRED and materialization != "native":
                require(errors, bool(obj.get("raster_reason")), f"{obj_path} requires raster_reason for non-native semantic content")
            if obj_type == "image":
                require(errors, materialization in {"raster", "hybrid"}, f"{obj_path} image must be raster or hybrid")
                require(errors, obj.get("replaceable") is True, f"{obj_path} image must be replaceable")
                require(errors, obj.get("asset_id") in asset_ids, f"{obj_path}.asset_id must reference a declared asset")

            if "bbox" in obj:
                validate_bbox(obj.get("bbox"), obj_path, canvas_width, canvas_height, errors)


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
                if brief.get("route") and plan.get("route") and brief.get("route") != plan.get("route"):
                    errors.append(f"brief route ({brief.get('route')}) does not match slide_plan route ({plan.get('route')})")

    report = {"status": "pass" if not errors else "fail", "error_count": len(errors), "errors": errors}
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
