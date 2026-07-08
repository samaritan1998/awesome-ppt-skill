#!/usr/bin/env python3
"""Generate a simple static HTML preview from slide_plan.json."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
from typing import Any


def render_object(obj: dict[str, Any]) -> str:
    content = obj.get("content", "")
    kind = obj.get("type", "text")
    if kind == "bullets" and isinstance(content, list):
        items = "".join(f"<li>{html.escape(str(item))}</li>" for item in content)
        return f"<ul>{items}</ul>"
    if kind == "image":
        return f"<div class='placeholder'>image: {html.escape(str(content))}</div>"
    if kind in {"chart", "table", "diagram"}:
        return f"<pre>{html.escape(json.dumps(content, ensure_ascii=False, indent=2))}</pre>"
    return f"<p>{html.escape(str(content))}</p>"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slide_plan", type=Path)
    parser.add_argument("--out", type=Path, default=Path("preview.html"))
    args = parser.parse_args()
    plan = json.loads(args.slide_plan.read_text(encoding="utf-8"))
    slides = []
    for slide in plan.get("slides", []):
        body = "\n".join(render_object(obj) for obj in slide.get("objects", []))
        slides.append(
            f"<section class='slide'><div class='num'>{slide.get('slide_no')}</div>"
            f"<h1>{html.escape(slide.get('title', 'Untitled'))}</h1>"
            f"<h2>{html.escape(slide.get('takeaway', ''))}</h2>{body}</section>"
        )
    doc = f"""<!doctype html>
<html lang="en">
<meta charset="utf-8">
<title>{html.escape(plan.get('deck_title', 'Deck preview'))}</title>
<style>
body {{ margin: 0; background: #111827; font-family: Arial, sans-serif; color: #111827; }}
.deck {{ display: grid; gap: 24px; padding: 24px; }}
.slide {{ width: 960px; min-height: 540px; background: #fff; padding: 48px; box-sizing: border-box; position: relative; }}
.num {{ position: absolute; right: 24px; bottom: 18px; color: #6b7280; }}
h1 {{ margin: 0 0 12px; font-size: 34px; }}
h2 {{ margin: 0 0 28px; font-size: 20px; color: #2563eb; font-weight: 600; }}
p, li, pre {{ font-size: 22px; line-height: 1.35; }}
.placeholder {{ border: 2px dashed #9ca3af; padding: 28px; color: #6b7280; font-size: 20px; }}
</style>
<main class="deck">
{''.join(slides)}
</main>
</html>
"""
    args.out.write_text(doc, encoding="utf-8")
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
