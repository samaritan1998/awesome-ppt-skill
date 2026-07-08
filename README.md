# All-in-One PPT Skill

An Agent Skill for planning, building, editing, reconstructing, QA-checking, and repairing PowerPoint / PPTX / Slides decks.

The main design decision is simple: default to editable PPTX, keep a structured `slide_plan.json`, render before delivery, and run QA before handing off the deck.

## What Is Included

- `all-in-one-ppt/SKILL.md`: compact agent instructions and route selection.
- `all-in-one-ppt/references/`: router, workflows, QA checklist, design system, academic mode, business mode, and security notes.
- `all-in-one-ppt/schemas/`: `deck_brief.schema.json` and `slide_plan.schema.json`.
- `all-in-one-ppt/scripts/`: small utilities for planning, QA, preview, and optional PptxGenJS generation.
- `research/`: summary of the PPT Skill research that motivated this design.

## Install

Copy `all-in-one-ppt/` into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R all-in-one-ppt "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Then ask:

```text
Use $all-in-one-ppt to turn this report into an editable, QA-checked PPTX.
```

## Quick Local Test

```bash
cd all-in-one-ppt
python3 scripts/plan_from_markdown.py ../examples/research_blog_outline.md --out /tmp/aio-ppt-demo
python3 scripts/qa_report.py /tmp/aio-ppt-demo/slide_plan.json
python3 scripts/html_preview.py /tmp/aio-ppt-demo/slide_plan.json --out /tmp/aio-ppt-demo/preview.html
```

Optional PPTX build:

```bash
npm install pptxgenjs
node scripts/build_pptx_pptxgenjs.mjs /tmp/aio-ppt-demo/slide_plan.json /tmp/aio-ppt-demo/deck.pptx
```

## Suggested Repository Name

`samaritan1998/all-in-one-ppt-skill`

The current environment did not have permission to create a new GitHub repository automatically, so this directory is prepared as a GitHub-ready repo.
