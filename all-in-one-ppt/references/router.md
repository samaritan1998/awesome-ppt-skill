# Router

Use this file to choose the production path before building or editing a deck.

## Inputs To Check

- Is there an existing `.pptx`, PDF, screenshot, image, Markdown file, HTML deck, template, spreadsheet, or research paper?
- Does the user require editable PowerPoint objects?
- Is the deck for a business, academic, technical, training, sales, or creative presentation?
- Does the user need Google Slides collaboration?
- Is this primarily creation, editing, reconstruction, or QA?

## Route Rules

Choose exactly one primary route, then add optional modes or follow-up routes when needed.

| Signal | Primary route | Mode / follow-up |
| --- | --- | --- |
| "make a PPT", "turn this into slides", source text or outline | `native-pptx` | add `business` or `academic` mode when relevant |
| existing `.pptx` and edit request | `edit-existing` | follow with `qa-audit` |
| company template, brand deck, master slides | `template-extract` | follow with `native-pptx` |
| screenshots, exported slide images, scanned PDF | `reconstruct` | follow with `qa-audit` |
| Markdown, Marp, Slidev, HTML, code talk | `html-markdown` | follow with `native-pptx` if PPTX is required |
| Drive, sharing, comments, online collaboration | `google-slides` | follow with `qa-audit` |
| paper, arXiv, thesis, experiment, method/results | `native-pptx` | add `academic` mode |
| pitch, board, customer, consulting, roadmap | `native-pptx` | add `business` mode |
| "check", "polish", "fix layout", "make editable" | `qa-audit` | inspect source format first |

## Default Decision

If unclear, ask only the minimum blocking question. Otherwise use `native-pptx` with editable output, 16:9 layout, concise slide plan, rendered preview, and QA.
