# QA Checklist

Run plan checks before building, then inspect the exported PPTX itself. A passing JSON report is not proof of a good deck.

## Gate 1: Content And Data

- The deck answers the user's request for the intended audience.
- The storyline is coherent and every slide has one clear purpose/takeaway.
- Claims, quotations, figures, chart values, table values, units, dates, and totals are correct.
- Evidence and citations are traceable; assumptions are not presented as facts.
- No planning notes, placeholders, internal instructions, or unsupported claims appear on slides.

## Gate 2: Visual Render

Render every slide and inspect it at full size. Also inspect a montage for consistency and pacing.

- No clipped, overflowing, unexpectedly wrapped, or undersized text.
- No unintended overlaps, off-slide objects, broken connectors, or hidden labels.
- Images are sharp, undistorted, intentionally cropped, and free of accidental text/watermarks.
- Titles, margins, spacing, page markers, footers, and brand elements are consistent.
- Charts and tables are readable at presentation distance.
- Layouts vary enough to sustain attention without losing visual coherence.

## Gate 3: Editability

- Titles, body copy, labels, citations, tables, charts, and simple diagrams are native objects.
- Generated images and supplied artwork are independent, replaceable image objects.
- No ordinary content slide is one full-canvas bitmap.
- Every rasterized semantic object has a documented reason and editable labels/annotations where practical.
- A representative title, body text, table cell, chart, diagram, and image replacement pass the smoke test.
- Existing-deck edits preserve unaffected slides, notes, masters/layouts, links, and media.

## Blockers

- Incorrect or contradictory data.
- Missing requested content or unresolved placeholders.
- Text clipping/overflow, severe overlap, or off-slide content.
- Broken file, wrong slide size, missing media, or destructive font substitution.
- Full-slide rasterization when editable PPTX is required.
- AI-generated asset with misleading factual content, accidental words, watermark, or severe artifact.

## Major Issues

- Weak narrative or slide takeaway.
- Dense copy, unreadable chart/table, weak contrast, or distorted image.
- Inconsistent template/brand treatment.
- Semantic content rasterized without justification.
- Missing source context, units, notes, or accessibility text when required.

## Repair Loop

1. Attach each issue to a slide/object and classify severity.
2. Repair blockers and majors locally.
3. Re-export and re-render affected slides.
4. Recheck the full deck for consistency and regressions.
5. Deliver only when no known blocker or major issue remains; disclose unavoidable limitations.
