# PPT Skill Research Summary

Date: 2026-07-08

The research filtered public Agent Skill / Claude Skill / Codex Skill / SKILL.md entries down to concrete PPT / PowerPoint / PPTX / Slides / Presentation / Deck skills. Generic indexes, broad writing tools, broad chart tools, and non-PPT Office automation entries were removed.

Full strict list with links and descriptions:

- Markdown: [`ppt_skill_list_2026_07_08.md`](ppt_skill_list_2026_07_08.md)
- CSV: [`ppt_skill_list_2026_07_08.csv`](ppt_skill_list_2026_07_08.csv)
- JSON: [`ppt_skill_list_2026_07_08.json`](ppt_skill_list_2026_07_08.json)

Source conversation: https://chatgpt.com/c/6a4de5f8-eedc-83ee-99a5-557c0a34e336

## Filtered Set

Total concrete PPT/Slides skills: 121

| Category | Count |
| --- | ---: |
| HTML / Markdown Slides | 39 |
| PPTX creation/editing | 19 |
| PPT design | 13 |
| Academic / paper PPT | 12 |
| PPT generation | 11 |
| Image/PDF to PPT | 9 |
| Official / core | 5 |
| Business / deck | 4 |
| Google Slides | 3 |
| Quality checks | 3 |
| Editable PPT | 2 |
| LibreOffice Impress | 1 |

Priority labels:

| Priority | Count |
| --- | ---: |
| Strong priority | 22 |
| Priority | 45 |
| Worth reading | 53 |
| Audit only | 1 |

## Architecture Conclusion

The best PPT Skill is not a single prompt or one generator. It should be:

```text
PPT Router + structured slide plan + multiple build backends + design system + editable object policy + rendered QA + repair loop
```

## Capabilities To Absorb

- OpenAI slides: PptxGenJS, render, overflow/overlap/font checks.
- Anthropic pptx: broad trigger for any `.pptx`, read/edit/create/template/speaker notes/OOXML coverage.
- Microsoft powerpoint: deck-as-code with structured content and style YAML.
- Image-first PPT skills: high-visual exploration, but optional because editability suffers.
- Google Workspace gws-slides: cloud collaboration route only when needed.

## Main Tradeoff

Native PPTX gives editability and enterprise usefulness. HTML/image-first gives stronger visual control. The All-in-One Skill should default to native PPTX and selectively invoke visual-first routes when the task justifies the tradeoff.
