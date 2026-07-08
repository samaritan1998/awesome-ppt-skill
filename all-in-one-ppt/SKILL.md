---
name: all-in-one-ppt
description: End-to-end PowerPoint and slides production skill for planning, creating, editing, reconstructing, QA-checking, and repairing presentations. Use when the task involves PPT, PPTX, PowerPoint, slide decks, presentations, Google Slides, HTML/Markdown slides, pitch decks, academic talks, template-based decks, image/PDF-to-editable-PPT reconstruction, or pre-delivery deck quality audits.
---

# All-in-One PPT

## Core Rule

Default to editable PPTX. Keep text, simple shapes, tables, and charts as native editable objects whenever practical. Use image-first slides only when the user explicitly prioritizes high visual impact over editability, or when the source material is image/PDF-only and reconstruction is underway.

Every nontrivial deck must go through:

1. Route selection
2. Brief extraction
3. `slide_plan.json`
4. Build or edit
5. Rendered preview
6. QA report
7. Targeted repair
8. Final delivery package

## Route Selection

Read `references/router.md` when the request is not a simple one-slide edit.

Use these routes:

- `native-pptx`: new editable PPTX from brief, document, notes, or outline.
- `edit-existing`: inspect and modify an existing `.pptx`.
- `template-extract`: derive style, layouts, and reusable components from a reference deck.
- `image-first`: generate visually rich slide images, then preserve editable text where practical.
- `reconstruct`: convert screenshots, PDF pages, or image-based decks into editable PPTX.
- `html-markdown`: build HTML, Marp, Slidev, or Markdown slides, optionally export to PPTX.
- `google-slides`: use only when cloud collaboration, Drive sharing, or Google Slides API work is required.
- `academic`: paper reading, literature report, thesis defense, research update, experiment-heavy deck.
- `business`: pitch deck, board update, customer proposal, consulting-style deck.
- `qa-audit`: inspect an existing deck and report/fix layout, fidelity, consistency, or editability issues.

## Standard Workflow

1. Define the brief. Capture audience, goal, language, page count, tone, output format, editability requirement, source files, brand constraints, and deadline.
2. Inspect inputs before rewriting. For existing decks, render thumbnails or inspect XML before editing. For PDF/images, inspect geometry visually before reconstructing.
3. Create `deck_brief.json` and `slide_plan.json`. Use schemas in `schemas/`.
4. Build from the selected route. Prefer native PPTX for deliverables. Keep generated assets under an `assets/` folder.
5. Render the deck to images or PDF. Never trust a deck that has not been rendered.
6. Run QA. Use `references/qa_checklist.md` and `scripts/qa_report.py`.
7. Repair locally. Fix only the failing slides when possible to avoid style drift.
8. Deliver: `.pptx`, rendered PDF/images, speaker notes if requested, `slide_plan.json`, assets, and QA notes.

## References

- Read `references/workflows.md` for route-specific procedures.
- Read `references/design_system.md` for visual and template rules.
- Read `references/academic_mode.md` for paper and research presentations.
- Read `references/business_mode.md` for pitch, board, customer, and consulting decks.
- Read `references/qa_checklist.md` before final delivery.
- Read `references/security.md` before installing third-party skills, running bundled scripts, or using networked APIs.

## Bundled Scripts

- `scripts/plan_from_markdown.py`: make a first `deck_brief.json` and `slide_plan.json` from a Markdown outline.
- `scripts/qa_report.py`: run structural QA on a `slide_plan.json`.
- `scripts/html_preview.py`: generate a simple static HTML preview from `slide_plan.json`.
- `scripts/build_pptx_pptxgenjs.mjs`: optional native PPTX builder when `pptxgenjs` is installed.

Run scripts from the skill directory unless the task has a project-specific output folder.

## Quality Bar

Do not deliver a deck with known text overflow, unreadable charts, missing fonts, distorted images, broken links, mismatched page sizes, inconsistent title placement, incorrect numbering, unexplained data, or unintended full-slide rasterization.
