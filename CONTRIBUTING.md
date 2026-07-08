# Contributing

这个仓库欢迎两类贡献：补充 PPT / Slides Skill 调研项，以及改进 `all-in-one-ppt` Skill 本身。

## 添加调研项

新增条目需要满足这些条件：

- 明确指向 PPT / PowerPoint / PPTX / Slides / Presentation / Deck。
- 是具体 Agent Skill、Claude Skill、Codex Skill、`SKILL.md`、GitHub Skill 仓库或 marketplace Skill 页面。
- 有可访问链接和一句明确描述。
- 不是泛索引站、泛 Office 助手、泛写作工具或非 PPT 专项资源。

同步更新这些文件：

- `research/ppt_skill_list_2026_07_08.md`
- `research/ppt_skill_list_2026_07_08.csv`
- `research/ppt_skill_list_2026_07_08.json`
- `README.md` 中的统计和折叠清单

## 改进 All-in-One Skill

优先改进这些方向：

- 更清晰的 route selection。
- 更可靠的 `deck_brief.json` / `slide_plan.json` 契约。
- 更接近真实交付的 PPTX 构建、渲染和 QA。
- 更好的 academic / business 场景规则。
- 更安全的第三方依赖和脚本执行说明。

## 本地校验

```bash
python3 quick_validate.py all-in-one-ppt
python3 all-in-one-ppt/scripts/plan_from_markdown.py examples/ppt_skill_research_outline.md --out out/demo
python3 all-in-one-ppt/scripts/validate_plan.py out/demo/slide_plan.json --brief out/demo/deck_brief.json
python3 all-in-one-ppt/scripts/qa_report.py out/demo/slide_plan.json --out out/demo/qa_report.json
python3 all-in-one-ppt/scripts/html_preview.py out/demo/slide_plan.json --out out/demo/preview.html
```

PPTX smoke test 需要 Node.js：

```bash
npm --prefix all-in-one-ppt install
node all-in-one-ppt/scripts/build_pptx_pptxgenjs.mjs out/demo/slide_plan.json out/demo/deck.pptx
```
