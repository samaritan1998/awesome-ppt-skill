# Visual Assets And Image Generation

Use image generation to fill a visual-asset gap, not to outsource slide composition.

## Source Order

1. Reuse user-supplied, brand-approved, or source-document assets.
2. Reuse charts, figures, or screenshots that carry evidence, with attribution.
3. Search for an appropriate licensed asset when provenance matters.
4. Generate a custom image when the required subject, composition, style, or negative space is unavailable.

## Good Image-Generation Uses

- A cover or section-break visual tailored to the deck's subject.
- A concept illustration, product context scene, texture, or abstract background.
- A complex artistic or scientific visual whose explanatory labels will be added natively.
- A replacement visual when stock imagery would be generic or off-brand.

## Do Not Generate

- A complete slide.
- Charts, tables, timelines, common icons, or simple diagrams.
- Images containing the slide's title, bullets, data labels, citations, or body copy.
- Brand logos or factual product/UI screenshots that must be exact.

## Asset Brief

Create an asset record before invoking `$imagegen` or the host image-generation tool:

- `id`, target slide, purpose, and asset type;
- target box and aspect ratio;
- intended crop and subject placement;
- required negative space for native slide copy;
- visual style, lighting, palette, and relation to the deck design;
- must-keep and must-avoid constraints;
- exact text only when text is inherently part of the depicted object;
- privacy/provenance constraints.

Prompt for the final placement. If copy sits on the left, place the subject on the right and leave calm negative space on the left. Request no words, labels, logo, signature, frame, or watermark by default.

## Generation Loop

1. Generate one asset per distinct need; do not ask one image to serve unrelated slides.
2. Inspect subject accuracy, composition, style, crop tolerance, accidental text, watermarks, and visual artifacts.
3. Iterate with one targeted change at a time.
4. Save the selected asset inside the project or task workspace with a stable descriptive filename.
5. Record generation method, final prompt, file path, target slide, and any usage limitation in `slide_plan.json` or the source ledger.
6. Insert it as an independently selectable image with alt text. Keep titles, labels, callouts, and citations as native PowerPoint objects.

## Reconstruction And Hybrid Visuals

For complex source figures or generated infographics, use a hybrid treatment:

- raster visual core;
- native title, legend, labels, annotations, and takeaway;
- native source note;
- documented reason the visual core is not editable.

## Privacy And Rights

Do not upload confidential source decks, customer data, unreleased product imagery, or identifiable personal material to an external image service without user authorization. Keep the prompt/source ledger when provenance or commercial reuse matters.
