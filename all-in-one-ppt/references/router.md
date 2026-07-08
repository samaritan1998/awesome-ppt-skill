# Router

Use this file to choose the production path before building or editing a deck.

## Inputs To Check

- Is there an existing `.pptx`, PDF, screenshot, image, Markdown file, HTML deck, template, spreadsheet, or research paper?
- Does the user require editable PowerPoint objects?
- Is the deck for a business, academic, technical, training, sales, or creative presentation?
- Does the user need Google Slides collaboration?
- Is this primarily creation, editing, reconstruction, or QA?

## Route Rules

Choose exactly one primary route and optional secondary modes.

| Signal | Primary route | Secondary mode |
| --- | --- | --- |
| "make a PPT", "turn this into slides", source text or outline | `native-pptx` | `business` or `academic` when relevant |
| existing `.pptx` and edit request | `edit-existing` | `qa-audit` |
| company template, brand deck, master slides | `template-extract` | `native-pptx` |
| screenshots, exported slide images, scanned PDF | `reconstruct` | `qa-audit` |
| Markdown, Marp, Slidev, HTML, code talk | `html-markdown` | `native-pptx` if PPTX is required |
| Drive, sharing, comments, online collaboration | `google-slides` | `qa-audit` |
| paper, arXiv, thesis, experiment, method/results | `academic` | `native-pptx` |
| pitch, board, customer, consulting, roadmap | `business` | `native-pptx` |
| "check", "polish", "fix layout", "make editable" | `qa-audit` | route based on source format |

## Default Decision

If unclear, ask only the minimum blocking question. Otherwise use `native-pptx` with editable output, 16:9 layout, concise slide plan, rendered preview, and QA.
