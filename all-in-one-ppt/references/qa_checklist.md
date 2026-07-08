# QA Checklist

## Blockers

- Text overflow or clipped text.
- Overlapping objects that hide content.
- Missing or substituted fonts that change layout.
- Distorted images or charts.
- Wrong aspect ratio or unintended slide size changes.
- Broken embedded media or links.
- Full-slide images when the user required editable PPTX.
- Incorrect data, inconsistent totals, or mismatched numbers across slides.

## Major Issues

- Inconsistent title placement.
- Weak visual hierarchy.
- Too much text on a slide.
- Low color contrast.
- Chart labels too small to read.
- Unclear source attribution for data or quoted claims.
- Speaker notes missing when requested.
- Template/brand mismatch.

## Minor Issues

- Uneven spacing.
- Inconsistent punctuation or capitalization.
- Repeated icons with slightly different sizes.
- Footer/page number drift.

## Required Final Checks

- Render all slides and inspect thumbnails.
- Check slide count and ordering against the plan.
- Verify native editability for text, charts, tables, and simple shapes.
- Verify output files open successfully.
- Save `slide_plan.json` and QA notes with the final deck.
