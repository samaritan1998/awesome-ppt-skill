# Workflows

## Create

1. Inspect source material and separate facts, claims, evidence, and open assumptions.
2. Define the audience action: understand, decide, approve, buy, learn, or discuss.
3. Build a storyline with one purpose and one takeaway per slide.
4. Select a layout family before writing final copy. Shorten copy to fit the layout; do not shrink type to rescue a weak plan.
5. Map every object to `native`, `raster`, or `hybrid`.
6. Fill only genuine visual-asset gaps through supplied assets, search, or image generation.
7. Build the PPTX, render all slides, run QA, repair locally, and repeat.

## Edit

1. Preserve the input file and render the complete source deck.
2. Inspect slide size, masters/layouts, theme, fonts, notes, charts, tables, links, media, and object structure.
3. Identify exact edit targets and invariants: what changes and what must remain untouched.
4. Reuse the deck's existing components and visual grammar. Do not introduce an unrelated theme.
5. Edit only the necessary objects/slides unless a full redesign is requested.
6. Compare before/after renders and verify that untouched slides, notes, and package relationships remain intact.

## Template Modifier

1. Audit the full reference deck, not only the most attractive slide.
2. Catalog its title, section, content, chart, table, image, quote, and closing layouts.
3. Record theme fonts/colors, spacing, title positions, grid, logo/footer rules, image treatment, and chart styling.
4. Map each planned slide to an inherited layout. Add a new layout only when no source layout can carry the content responsibly.
5. Preserve master/layout semantics when the backend supports them.

## Reconstruct

1. Render source pages at high resolution and preserve the original page geometry.
2. Segment each page into text, tables, charts, images, equations, and decoration.
3. OCR text, then proofread against the source; never trust OCR blindly.
4. Rebuild semantic content with native objects. Crop and reuse only irreducibly complex visual regions.
5. Keep annotations and labels native even when the visual core remains raster.
6. Compare source and reconstruction side by side. Report fidelity and editability exceptions explicitly.

## Audit And Repair

1. Render every slide and inspect object structure.
2. Check narrative/content, visual layout, data/source integrity, and editability separately.
3. Classify issues as blocker, major, or minor and attach each to a slide/object.
4. Repair blockers and majors locally; avoid broad restyling unless requested.
5. Re-export and re-render affected slides, then rerun deck-level consistency checks.

## Planning And Validation

For nontrivial work:

1. Create `deck_brief.json` and `slide_plan.json`.
2. Run `scripts/validate_plan.py slide_plan.json --brief deck_brief.json`.
3. Run `scripts/qa_report.py slide_plan.json` before building to catch structural/editability mistakes.
4. Use `scripts/html_preview.py` only as a fast plan preview.
5. After building, render the actual PPTX and perform final artifact QA. Plan validation is not final deck validation.
