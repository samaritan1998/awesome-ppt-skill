# Editability Contract

Editability is an object-level property. A `.pptx` that contains one bitmap per slide does not satisfy this contract.

## Materialization Matrix

| Content | Default | Requirement |
| --- | --- | --- |
| Titles, body copy, captions, labels, citations | `native` | Selectable PowerPoint text with real font, size, color, alignment, and language |
| Tables | `native` | Editable cells; preserve row/column meaning and units |
| Data charts | `native` | Editable chart or native shapes backed by recorded data; keep labels and sources editable |
| Simple diagrams, timelines, processes, callouts | `native` | Native shapes and connectors; keep connectors behind nodes and labels readable |
| Icons and simple marks | `native` or `hybrid` | Prefer native SVG/icon assets; keep labels separate |
| Equations | `native` or `hybrid` | Prefer editable equation objects; otherwise use a tightly cropped equation asset with editable explanation |
| Photos and supplied artwork | `raster` | One independently selectable image per asset with preserved aspect ratio and alt text |
| Screenshots | `raster` | Crop intentionally; add editable callouts rather than burning annotations into the screenshot |
| AI-generated photos/illustrations/textures | `raster` | Keep as replaceable assets; keep all slide copy and data native |
| Complex scientific or artistic illustration | `hybrid` | Illustration may be raster; labels, legend, title, and explanatory annotations remain native |

## Forbidden Defaults

- Full-slide screenshots or generated slide images for ordinary content slides.
- Charts, tables, or simple diagrams rendered into a bitmap merely for convenience.
- Text rendered into SVG, PNG, or background images when native text can reproduce it.
- Rebuilding an existing deck from scratch when direct object-level editing can preserve its masters, theme, notes, and untouched slides.
- Converting every object to independent shapes when a real table or chart is more editable and semantically correct.

## Backend Selection

Choose the strongest available backend for the route:

- New decks: a native PPTX presentation library or artifact system that supports text, shapes, tables, charts, images, notes, and theme/layout control.
- Existing decks: PowerPoint/Office APIs, OOXML-aware tools, or a library that preserves untouched objects and package parts.
- Reconstruction: OCR/layout analysis plus native PPTX construction; use raster crops only for regions that cannot be reconstructed reliably.

Do not select a backend only because it is easy to call. Confirm that it can preserve the object types required by the plan.

## Plan Requirements

For every planned object, record:

- stable `id` and semantic `type`;
- `materialization`: `native`, `raster`, or `hybrid`;
- `editable`: boolean;
- position and size when known;
- content/data or referenced asset;
- source reference when the object makes a factual claim;
- `raster_reason` when semantic content is not native.

Use `hybrid` only when a visual core must be raster while its labels, annotations, or explanation remain native.

## Final Editability Smoke Test

Open the final deck in PowerPoint-compatible software and verify a representative sample plus every exceptional slide:

1. Select and edit a title and body text.
2. Edit one table cell.
3. Edit chart data or confirm the documented native-shape chart strategy.
4. Move a diagram node and verify connectors/labels remain usable.
5. Replace a generated or supplied image without disturbing slide copy.
6. Inspect speaker notes, theme fonts, slide size, masters/layouts, and reading order where supported.
7. Confirm no ordinary slide is a single full-canvas image.

Record any unavoidable limitation in the QA report and user-facing delivery note.
