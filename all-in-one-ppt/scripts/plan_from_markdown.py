#!/usr/bin/env python3
"""Create deck_brief.json and slide_plan.json skeletons from a Markdown outline."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def split_slides(markdown: str) -> list[dict]:
    lines = markdown.splitlines()
    slides: list[dict] = []
    current: dict | None = None
    body: list[str] = []

    def flush() -> None:
        nonlocal current, body
        if current is None:
            return
        bullets = [line.strip("-* ").strip() for line in body if line.strip().startswith(("-", "*"))]
        paragraph = " ".join(line.strip() for line in body if line.strip() and not line.strip().startswith(("-", "*")))
        objects = []
        if bullets:
            objects.append({"id": "bullets", "type": "bullets", "content": bullets, "editable": True})
        elif paragraph:
            objects.append({"id": "body", "type": "text", "content": paragraph, "editable": True})
        else:
            objects.append({"id": "body", "type": "text", "content": "TBD", "editable": True})
        current["objects"] = objects
        slides.append(current)
        current = None
        body = []

    for line in lines:
        match = re.match(r"^#{1,3}\s+(.+?)\s*$", line)
        if match:
            flush()
            title = match.group(1)
            current = {
                "slide_no": len(slides) + 1,
                "title": title,
                "takeaway": title,
                "layout": "title-and-content",
                "speaker_notes": "",
                "source_refs": [],
            }
        else:
            body.append(line)

    flush()
    if not slides:
        slides.append(
            {
                "slide_no": 1,
                "title": "Untitled deck",
                "takeaway": "Define the core message.",
                "layout": "title-and-content",
                "speaker_notes": "",
                "source_refs": [],
                "objects": [{"id": "body", "type": "text", "content": markdown.strip() or "TBD", "editable": True}],
            }
        )
    return slides


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--out", type=Path, default=Path("out"))
    parser.add_argument("--title", default=None)
    parser.add_argument("--route", default="native-pptx")
    args = parser.parse_args()

    text = args.markdown.read_text(encoding="utf-8")
    slides = split_slides(text)
    deck_title = args.title or slides[0]["title"]
    args.out.mkdir(parents=True, exist_ok=True)

    deck_brief = {
        "task_type": args.route,
        "audience": "TBD",
        "goal": "Turn the supplied outline into an editable, QA-checked presentation.",
        "language": "auto",
        "page_count": len(slides),
        "tone": "clear and professional",
        "output": ["pptx", "pdf", "slide_plan", "qa_report"],
        "editability": "native-first",
        "sources": [{"path_or_url": str(args.markdown), "kind": "markdown"}],
        "constraints": ["Preserve editability for text and simple objects."],
    }
    slide_plan = {
        "deck_title": deck_title,
        "route": args.route,
        "style": {"aspect_ratio": "16:9", "theme": "clean-professional"},
        "slides": slides,
    }

    (args.out / "deck_brief.json").write_text(json.dumps(deck_brief, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.out / "slide_plan.json").write_text(json.dumps(slide_plan, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {args.out / 'deck_brief.json'}")
    print(f"Wrote {args.out / 'slide_plan.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
