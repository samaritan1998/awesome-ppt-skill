#!/usr/bin/env python3
"""Create editable-PPTX planning contracts from a Markdown outline."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


PRIMARY_ROUTES = ["create", "edit", "reconstruct", "audit-repair"]
MODIFIERS = ["template", "academic", "business"]


def split_slides(markdown: str) -> list[dict]:
    lines = markdown.splitlines()
    slides: list[dict] = []
    current_title: str | None = None
    body: list[str] = []

    def flush() -> None:
        nonlocal current_title, body
        if current_title is None:
            return

        bullets = [line.strip("-* ").strip() for line in body if line.strip().startswith(("-", "*"))]
        paragraph = " ".join(
            line.strip() for line in body if line.strip() and not line.strip().startswith(("-", "*"))
        )
        if bullets:
            obj_type = "bullets"
            content: str | list[str] = bullets
        else:
            obj_type = "text"
            content = paragraph or "TBD"

        slide_no = len(slides) + 1
        slides.append(
            {
                "slide_no": slide_no,
                "title": current_title,
                "purpose": f"Explain {current_title}",
                "takeaway": current_title,
                "layout": "title-and-content",
                "speaker_notes": "",
                "source_refs": ["source-1"],
                "objects": [
                    {
                        "id": f"s{slide_no}-body",
                        "type": obj_type,
                        "role": "body",
                        "content": content,
                        "materialization": "native",
                        "editable": True,
                        "bbox": {"x": 0.8, "y": 1.55, "w": 11.75, "h": 4.95},
                        "style": {"font_size": 22},
                    }
                ],
            }
        )
        current_title = None
        body = []

    for line in lines:
        match = re.match(r"^#{1,3}\s+(.+?)\s*$", line)
        if match:
            flush()
            current_title = match.group(1)
        else:
            body.append(line)

    flush()
    if not slides:
        slides.append(
            {
                "slide_no": 1,
                "title": "Untitled deck",
                "purpose": "Introduce the topic",
                "takeaway": "Define the core message.",
                "layout": "title-and-content",
                "speaker_notes": "",
                "source_refs": ["source-1"],
                "objects": [
                    {
                        "id": "s1-body",
                        "type": "text",
                        "role": "body",
                        "content": markdown.strip() or "TBD",
                        "materialization": "native",
                        "editable": True,
                        "bbox": {"x": 0.8, "y": 1.55, "w": 11.75, "h": 4.95},
                        "style": {"font_size": 22},
                    }
                ],
            }
        )
    return slides


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--out", type=Path, default=Path("out"))
    parser.add_argument("--title", default=None)
    parser.add_argument("--route", default="create", choices=PRIMARY_ROUTES)
    parser.add_argument("--modifier", "--mode", dest="modifiers", action="append", choices=MODIFIERS, default=[])
    args = parser.parse_args()

    text = args.markdown.read_text(encoding="utf-8")
    slides = split_slides(text)
    deck_title = args.title or slides[0]["title"]
    args.out.mkdir(parents=True, exist_ok=True)

    deck_brief = {
        "route": args.route,
        "modifiers": args.modifiers,
        "audience": "TBD",
        "goal": "Turn the supplied outline into an editable, QA-checked PowerPoint deck.",
        "presentation_context": "TBD",
        "language": "auto",
        "slide_count": len(slides),
        "tone": "clear and professional",
        "deliverable": {"format": "pptx", "editable": True, "extras": ["plan", "qa-report"]},
        "editability": {
            "policy": "native-first",
            "full_slide_raster_allowed": False,
            "native_required": ["text", "bullets", "table", "chart", "shape", "connector", "diagram"],
            "raster_allowed": ["photo", "illustration", "screenshot", "texture", "complex-figure"],
        },
        "sources": [{"id": "source-1", "path_or_url": str(args.markdown), "kind": "markdown"}],
        "constraints": ["Keep semantic slide content editable and use generated images only as replaceable assets."],
        "open_questions": ["Confirm audience and presentation context."],
    }
    slide_plan = {
        "deck_title": deck_title,
        "route": args.route,
        "modifiers": args.modifiers,
        "canvas": {"width": 13.333, "height": 7.5, "unit": "in"},
        "style": {"theme": "clean-professional", "colors": [], "fonts": ["Aptos"]},
        "assets": [],
        "slides": slides,
    }

    (args.out / "deck_brief.json").write_text(json.dumps(deck_brief, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.out / "slide_plan.json").write_text(json.dumps(slide_plan, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {args.out / 'deck_brief.json'}")
    print(f"Wrote {args.out / 'slide_plan.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
