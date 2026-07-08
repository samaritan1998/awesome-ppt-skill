# Examples

这个目录提供一个最小可复现示例，从 Markdown 大纲生成 `deck_brief.json`、`slide_plan.json`、QA 报告和 HTML 预览。

```bash
python3 ../quick_validate.py ../all-in-one-ppt
python3 ../all-in-one-ppt/scripts/plan_from_markdown.py ppt_skill_research_outline.md --out ../out/demo
python3 ../all-in-one-ppt/scripts/validate_plan.py ../out/demo/slide_plan.json --brief ../out/demo/deck_brief.json
python3 ../all-in-one-ppt/scripts/qa_report.py ../out/demo/slide_plan.json --out ../out/demo/qa_report.json
python3 ../all-in-one-ppt/scripts/html_preview.py ../out/demo/slide_plan.json --out ../out/demo/preview.html
```

可选 PPTX smoke test：

```bash
npm --prefix ../all-in-one-ppt install
node ../all-in-one-ppt/scripts/build_pptx_pptxgenjs.mjs ../out/demo/slide_plan.json ../out/demo/deck.pptx
```

生成文件默认放在仓库根目录的 `out/demo/`，不会被提交。
