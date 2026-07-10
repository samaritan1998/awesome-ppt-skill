# Examples

这个目录提供一个最小可复现示例：从 Markdown 大纲生成可编辑 PPTX 的 brief/plan，执行结构与可编辑性 QA，再构建并检查 smoke deck。

```bash
python3 ../quick_validate.py ../all-in-one-ppt
python3 ../all-in-one-ppt/scripts/plan_from_markdown.py ppt_skill_research_outline.md --out ../out/demo
python3 ../all-in-one-ppt/scripts/validate_plan.py ../out/demo/slide_plan.json --brief ../out/demo/deck_brief.json
python3 ../all-in-one-ppt/scripts/qa_report.py ../out/demo/slide_plan.json --out ../out/demo/qa_report.json
python3 ../all-in-one-ppt/scripts/html_preview.py ../out/demo/slide_plan.json --out ../out/demo/preview.html
npm --prefix ../all-in-one-ppt ci
node ../all-in-one-ppt/scripts/build_pptx_pptxgenjs.mjs ../out/demo/slide_plan.json ../out/demo/deck.pptx
python3 ../all-in-one-ppt/scripts/inspect_pptx.py ../out/demo/deck.pptx --plan ../out/demo/slide_plan.json --out ../out/demo/pptx_report.json
```

生成文件默认放在仓库根目录的 `out/demo/`，不会被提交。PptxGenJS 构建器只覆盖 smoke-test 子集；正式 deck 由 Skill 路由到当前环境中能力最完整的原生 PPTX backend。

`native_objects_plan.json` 是 CI 使用的原生对象夹具，覆盖 editable table、chart、shape 和 connector，防止这些对象被静默降级成图片或文本。
