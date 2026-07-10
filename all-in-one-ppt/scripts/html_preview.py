#!/usr/bin/env python3
"""Generate a geometry-aware static HTML preview from slide_plan.json."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
from typing import Any


def render_content(obj: dict[str, Any]) -> str:
    content = obj.get("content", "")
    kind = obj.get("type", "text")
    if kind == "bullets" and isinstance(content, list):
        items = "".join(f"<li>{html.escape(str(item))}</li>" for item in content)
        return f"<ul>{items}</ul>"
    if kind == "image":
        return f"<div class='placeholder'>asset: {html.escape(str(obj.get('asset_id', 'missing')))}</div>"
    if kind in {"chart", "table", "diagram", "shape", "connector"}:
        return f"<pre>{html.escape(json.dumps(content, ensure_ascii=False, indent=2))}</pre>"
    return f"<p>{html.escape(str(content))}</p>"


def render_object(obj: dict[str, Any], width: float, height: float) -> str:
    bbox = obj.get("bbox")
    classes = f"object type-{html.escape(str(obj.get('type', 'text')))}"
    label = html.escape(f"{obj.get('id', '?')} · {obj.get('materialization', '?')}")
    if not isinstance(bbox, dict):
        return f"<div class='{classes} flow'><span class='label'>{label}</span>{render_content(obj)}</div>"
    left = bbox.get("x", 0) / width * 100
    top = bbox.get("y", 0) / height * 100
    box_width = bbox.get("w", width) / width * 100
    box_height = bbox.get("h", height) / height * 100
    style = f"left:{left:.4f}%;top:{top:.4f}%;width:{box_width:.4f}%;height:{box_height:.4f}%;"
    return f"<div class='{classes}' style='{style}'><span class='label'>{label}</span>{render_content(obj)}</div>"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slide_plan", type=Path)
    parser.add_argument("--out", type=Path, default=Path("preview.html"))
    args = parser.parse_args()
    plan = json.loads(args.slide_plan.read_text(encoding="utf-8"))
    canvas = plan.get("canvas", {})
    width = float(canvas.get("width", 13.333))
    height = float(canvas.get("height", 7.5))
    ratio = height / width * 100
    slides = []
    for slide in plan.get("slides", []):
        objects = "\n".join(render_object(obj, width, height) for obj in slide.get("objects", []))
        slides.append(
            f"<section class='slide' style='--ratio:{ratio:.4f}%'>"
            f"<div class='num'>{slide.get('slide_no')}</div>"
            f"<h1>{html.escape(slide.get('title', 'Untitled'))}</h1>"
            f"<h2>{html.escape(slide.get('takeaway', ''))}</h2>{objects}</section>"
        )
    doc = f"""<!doctype html>
<html lang="en">
<meta charset="utf-8">
<title>{html.escape(plan.get('deck_title', 'Deck preview'))}</title>
<style>
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: #111827; font-family: Arial, sans-serif; color: #111827; }}
.deck {{ display: grid; gap: 24px; padding: 24px; }}
.slide {{ width: 960px; height: calc(960px * {height:.6f} / {width:.6f}); background: #fff; position: relative; overflow: hidden; }}
.num {{ position: absolute; right: 18px; bottom: 12px; color: #6b7280; z-index: 5; }}
h1 {{ position: absolute; left: 4.5%; top: 5%; width: 91%; margin: 0; font-size: 30px; line-height: 1.1; }}
h2 {{ position: absolute; left: 4.65%; top: 13.5%; width: 90%; margin: 0; font-size: 15px; color: #2563eb; font-weight: 600; }}
.object {{ position: absolute; border: 1px dashed #9ca3af; padding: 8px; overflow: hidden; }}
.object.flow {{ position: relative; margin: 12px; }}
.label {{ position: absolute; right: 3px; top: 2px; color: #9ca3af; font-size: 9px; }}
p, li, pre {{ font-size: 16px; line-height: 1.28; }}
pre {{ white-space: pre-wrap; }}
.placeholder {{ width: 100%; height: 100%; display: grid; place-items: center; color: #6b7280; background: #f3f4f6; }}
</style>
<main class="deck">{''.join(slides)}</main>
</html>
"""
    args.out.write_text(doc, encoding="utf-8")
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
