# Workflows

## Native PPTX

1. Create `deck_brief.json`.
2. Create `slide_plan.json` with one object list per slide.
3. Use native PowerPoint objects for text, charts, tables, shapes, and simple diagrams.
4. Use images only for photos, illustrations, screenshots, complex textures, or intentionally raster visuals.
5. Render and run QA before delivery.

## Edit Existing

1. Inspect the deck size, slide count, masters/layouts, fonts, and thumbnails.
2. Preserve aspect ratio and template styling.
3. Edit only requested slides unless broad restyling is requested.
4. Render before/after previews.
5. Confirm slide count, section order, notes, and source links remain intact.

## Template Extract

1. Render template thumbnails.
2. Identify title, section, content, chart, image, quote, agenda, and closing layouts.
3. Extract theme colors, font stack, logo placement, footer rules, chart style, spacing grid, and common components.
4. Store reusable decisions in the task's style library or `deck_brief.json`.

## Reconstruction

1. Render source PDF/images at high resolution.
2. Segment each page into text, tables, charts, images, and decorative shapes.
3. Recreate text and simple geometry as editable objects.
4. Use raster crops only where semantic reconstruction is unreliable.
5. Compare reconstructed slides against source thumbnails and report known fidelity gaps.

## HTML/Markdown

1. Use Markdown/HTML for rapid story and visual exploration.
2. Keep a source `slide_plan.json` so output can be ported to PPTX.
3. If exporting to PPTX, run fidelity QA because layout drift is common.

## Google Slides

1. Use only when cloud collaboration or Drive sharing is part of the task.
2. Confirm account, folder, sharing, and permission assumptions before changing external access.
3. Keep a local `slide_plan.json` for reproducibility.

## QA Audit

1. Render the deck.
2. Check structural, visual, content, and editability issues.
3. Classify issues as blocker, major, or minor.
4. Repair blocker and major issues before delivery when the user requested a finished deck.
