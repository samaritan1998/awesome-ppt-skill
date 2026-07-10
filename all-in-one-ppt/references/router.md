# Router

Choose the operation that best describes the user's intent. The final artifact remains an editable PPTX unless the user explicitly asks for another format.

Use exactly one canonical route ID: `create`, `edit`, `reconstruct`, or `audit-repair`. Never invent or extend route IDs. Record details such as source format, 30-to-10 compression, redesign, translation, or image assistance in the brief/constraints instead.

The only modifier IDs are `template`, `academic`, and `business`. `editable`, `imagegen`, `board`, `thesis-defense`, `no-template`, and similar descriptions are not modifiers; store them in their dedicated brief fields.

## Primary Routes

| Signal | Route | First action |
| --- | --- | --- |
| "make a PPT", source notes, report, document, URL, or data | `create` | Extract the brief and build a claim-led storyline |
| Existing `.pptx` plus change request | `edit` | Render and inspect the complete source deck before editing |
| Screenshots, PDF pages, scans, or image-only slides | `reconstruct` | Segment each page into semantic and visual objects |
| "check", "polish", "fix", "make editable", or "why is this broken" | `audit-repair` | Render, inspect object structure, classify issues, then repair if requested |

If several routes apply, choose the route that changes the artifact first, then run `audit-repair` as the final gate. Example: reconstructing a PDF uses `reconstruct`, not `audit-repair`, even though QA follows.

## Modifiers

- `template`: a supplied PPTX, master, brand deck, or reference deck controls layout and visual language. Never mix it with an unrelated default theme.
- `academic`: evidence, methods, results, citations, and limitations drive the story.
- `business`: decisions, outcomes, metrics, risks, recommendations, and next actions drive the story.

Modifiers may combine, such as `create + template + business`. Use only `template`, `academic`, and `business` as modifier IDs; keep other descriptors in the brief.

## Inputs Are Not Routes

Treat Markdown, HTML, Word, PDF, spreadsheets, images, and web pages as sources to ingest. Do not choose a different output architecture merely because the source format differs.

Treat Google Slides as a downstream import/export target when explicitly requested. Build and verify the editable PPTX first unless the host has a native Google Slides workflow that preserves the same object-level contract.

## Default

When the user says only "make a PPT", use `create`, 16:9, editable PPTX, concise audience-facing copy, native objects, restrained visuals, and render-based QA. Ask a question only if audience, purpose, or source ambiguity would materially change the result.
