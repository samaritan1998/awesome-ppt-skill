---
name: all-in-one-ppt
description: Create, edit, reconstruct, audit, and repair genuinely editable PowerPoint (.pptx) decks. Use when a request mentions PPT, PPTX, PowerPoint, slides, presentation, or deck and the result should remain editable; supports source documents, existing decks, reference templates, screenshots/PDFs, native charts/tables/diagrams, academic or business narratives, optional AI-generated visual assets, and render-based QA.
---

# All-in-One Editable PowerPoint

## Machine Contract

Use these exact planning IDs:

```text
route = create | edit | reconstruct | audit-repair
modifiers = any subset of [template, academic, business]
```

Do not put source formats, audience names, output properties, techniques, or descriptive aliases in these fields. Values such as `document_to_deck`, `create_from_pdf`, `board`, `editable`, `imagegen`, `no_template`, and `scientific-fidelity` are invalid. Store them in `sources`, `audience`, `goal`, `constraints`, `editability`, or the asset plan instead. Use an empty modifier list when no canonical modifier applies.

Examples:

- Annual report to a board deck: `route: create`, `modifiers: [business]`.
- Research PDF to an editable thesis deck: `route: reconstruct`, `modifiers: [academic]`.

## Outcome Contract

Deliver a real, editable `.pptx` by default. Treat editability as an object-level contract, not as a file-extension check.

- Keep titles, body text, labels, tables, charts, simple diagrams, connectors, and basic decoration as native PowerPoint objects.
- Use raster images only for photographs, screenshots, textures, complex illustrations, and generated visual assets.
- Never use a full-slide image as the normal implementation of a slide.
- Never bake slide copy, chart labels, table values, or simple diagrams into an AI-generated image.
- Preserve the source deck and write a new file unless the user explicitly requests an in-place edit.
- Deliver the PPTX only after rendering every slide and repairing known content, layout, and editability defects.

Read [references/editability_contract.md](references/editability_contract.md) before choosing an implementation backend or materializing slide objects.

## Route the Task

Choose one primary route. Set `route` to exactly one canonical ID from the table below; never invent an alias such as `document-to-deck` or `image-assisted-create`. Put source type, compression ratio, audience, and other specifics in the brief or constraints. Treat templates, academic rules, and business rules as modifiers, not competing output formats.

| Route | Use for | Required result |
| --- | --- | --- |
| `create` | Build a new deck from a prompt, document, outline, data, or research | New editable PPTX |
| `edit` | Revise, extend, translate, restyle, or correct an existing PPTX | Edited copy with unaffected objects preserved |
| `reconstruct` | Convert screenshots, PDF pages, or image-only slides | Editable reconstruction plus a fidelity note |
| `audit-repair` | Inspect and fix content, design, layout, data, or editability | QA report and repaired PPTX when repair is requested |

Set `modifiers` only to a subset of `template`, `academic`, and `business`. Add `template` when a reference deck or company template controls the visual system. Add `academic` or `business` only when those narrative rules apply. Put all other descriptors in the brief. Read [references/router.md](references/router.md) when the route is not obvious.

HTML, Markdown, PDFs, documents, spreadsheets, and web pages are input sources. Google Slides may be an import destination after the PPTX is verified. Do not switch the primary deliverable away from editable PPTX unless the user asks.

## Execute the Workflow

For a small, local edit, keep the plan lightweight. For a new deck, reconstruction, redesign, or multi-slide edit, use the complete workflow.

1. **Inspect inputs.** Inventory source files, slide size, masters/layouts, theme, fonts, notes, charts, tables, media, and existing object editability. Render existing decks before editing them.
2. **Resolve the brief.** Record audience, decision or learning goal, context, language, desired length, presentation setting, required sources, brand constraints, and output path. Ask only for information that blocks a responsible result.
3. **Build the narrative.** Create a claim-led storyline before styling. Give every slide one job and one audience-facing takeaway. Read the relevant academic or business reference when a mode is active.
4. **Create the plan.** Write `deck_brief.json` and `slide_plan.json` for nontrivial work. Define each slide's purpose, action title, evidence, layout, objects, sources, notes, and visual assets before implementation. Validate both files with `scripts/validate_plan.py`.
5. **Choose object materialization.** Mark each planned object as `native`, `raster`, or `hybrid`. Apply the editability contract; record a reason for every non-native semantic object.
6. **Plan visual assets.** Reuse supplied assets first. Use licensed/search assets when appropriate. Invoke `$imagegen` or the host's image-generation tool only when a custom photo, illustration, texture, or complex visual materially improves the slide. Follow [references/image_assets.md](references/image_assets.md).
7. **Build with a native PPTX backend.** Use the strongest available presentation engine that preserves native objects, themes, notes, and layout semantics. Follow a supplied template exactly when one exists. The bundled PptxGenJS script is a smoke-test backend, not a design engine.
8. **Render and inspect.** Render the exported PPTX to slide images. Inspect every slide at full size and inspect a montage for deck-level rhythm. Do not rely on code inspection alone.
9. **Run three QA gates.** Check content and data, visual layout, then editability. Run `scripts/qa_report.py` for plan-level checks and [references/qa_checklist.md](references/qa_checklist.md) for final artifact checks.
10. **Repair locally and repeat.** Fix failing slides or objects, re-export, and re-render. Stop only when no blocker or major issue remains.
11. **Deliver cleanly.** Return the final `.pptx`; include PDF, slide images, notes, plan, source ledger, or QA report only when requested or operationally useful.

## Generated-Image Rule

Generated images are replaceable slide assets, never flattened slides.

Before generation, derive the asset's aspect ratio, crop, subject placement, and negative space from the target layout. Ask the image model for no words, labels, logos, or watermarks unless text is itself the subject. Save the final prompt and asset path in the plan, insert the image as an independently selectable object, and keep all explanatory copy native in PowerPoint.

Do not generate icons, common geometric diagrams, charts, or tables as images when native PowerPoint objects can express them cleanly.

## Quality Gates

Do not deliver when any of these are true:

- A title, label, or body text is clipped, wrapped unexpectedly, or unreadable at presentation distance.
- Objects overlap unintentionally, sit outside the slide, or move because of missing fonts.
- A chart or table is rasterized without a documented reason, uses incorrect data, or lacks units/source context.
- A generated image contains accidental text, a watermark, distorted anatomy/objects, or a crop that conflicts with the layout.
- The deck contains unresolved placeholders, duplicated assets, inconsistent titles, distorted images, or broken links/media.
- A standard content slide is implemented as one full-slide bitmap.
- The final deck has not passed an editability smoke test in PowerPoint-compatible software.

## Reference Map

- [references/router.md](references/router.md): route and modifier selection.
- [references/editability_contract.md](references/editability_contract.md): native/raster/hybrid rules and backend acceptance criteria.
- [references/workflows.md](references/workflows.md): route-specific procedures.
- [references/design_system.md](references/design_system.md): narrative, layout, typography, charts, and templates.
- [references/image_assets.md](references/image_assets.md): source/search/image-generation asset workflow.
- [references/academic_mode.md](references/academic_mode.md): research and thesis decks.
- [references/business_mode.md](references/business_mode.md): decision, pitch, board, and customer decks.
- [references/qa_checklist.md](references/qa_checklist.md): content, visual, editability, and delivery QA.
- [references/security.md](references/security.md): private inputs, external services, and third-party code.

## Bundled Utilities

- `scripts/plan_from_markdown.py`: create starter brief/plan files from a Markdown outline.
- `scripts/validate_plan.py`: validate planning contracts.
- `scripts/qa_report.py`: run plan-level structural and editability checks.
- `scripts/html_preview.py`: preview planned slide copy and object boxes; not a final presentation route.
- `scripts/render_pptx_preview.sh`: render a PPTX through LibreOffice when available.
- `scripts/build_pptx_pptxgenjs.mjs`: create a smoke-test editable PPTX from a supported plan subset.
- `scripts/inspect_pptx.py`: inspect PPTX/OOXML structure and compare native object counts with the plan.

These utilities support the workflow; they do not replace visual judgment or the host's full presentation tooling.
