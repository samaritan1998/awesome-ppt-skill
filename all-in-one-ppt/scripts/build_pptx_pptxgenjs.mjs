#!/usr/bin/env node
import fs from "node:fs";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);

function optionsFromBbox(obj, fallback) {
  const bbox = obj && obj.bbox;
  if (!bbox || typeof bbox !== "object") return fallback;
  for (const key of ["x", "y", "w", "h"]) {
    if (typeof bbox[key] !== "number") return fallback;
  }
  return { ...fallback, x: bbox.x, y: bbox.y, w: bbox.w, h: bbox.h };
}

async function main() {
  const planPath = process.argv[2];
  const outPath = process.argv[3] || "deck.pptx";
  if (!planPath) {
    console.error("Usage: build_pptx_pptxgenjs.mjs slide_plan.json [out.pptx]");
    process.exit(2);
  }

  let pptxgenjs;
  try {
    pptxgenjs = require("pptxgenjs");
  } catch (error) {
    console.error("Missing or unusable dependency: npm install pptxgenjs");
    console.error(error.message);
    process.exit(2);
  }

  const pptxgen = pptxgenjs.default || pptxgenjs;
  const plan = JSON.parse(fs.readFileSync(planPath, "utf8"));
  const pptx = new pptxgen();
  pptx.layout = "LAYOUT_WIDE";
  pptx.author = "all-in-one-ppt";
  pptx.subject = plan.deck_title || "Generated deck";
  pptx.title = plan.deck_title || "Generated deck";
  pptx.company = "all-in-one-ppt";
  pptx.lang = "en-US";
  pptx.theme = {
    headFontFace: "Aptos Display",
    bodyFontFace: "Aptos",
    lang: "en-US"
  };

  for (const slidePlan of plan.slides || []) {
    const slide = pptx.addSlide();
    slide.background = { color: "FFFFFF" };
    slide.addText(slidePlan.title || "Untitled", {
      x: 0.55,
      y: 0.35,
      w: 12.2,
      h: 0.45,
      fontFace: "Aptos Display",
      fontSize: 26,
      bold: true,
      color: "111827",
      margin: 0
    });
    if (slidePlan.takeaway) {
      slide.addText(slidePlan.takeaway, {
        x: 0.58,
        y: 0.95,
        w: 11.9,
        h: 0.45,
        fontSize: 15,
        color: "2563EB",
        margin: 0
      });
    }

    let y = 1.65;
    for (const obj of slidePlan.objects || []) {
      if (obj.type === "bullets" && Array.isArray(obj.content)) {
        slide.addText(obj.content.map((text) => ({ text, options: { bullet: { type: "ul" } } })), optionsFromBbox(obj, {
          x: 0.75,
          y,
          w: 11.4,
          h: 4.6,
          fontSize: 18,
          color: "111827",
          breakLine: false,
          fit: "shrink"
        }));
        y += 2.4;
      } else if (obj.type === "image" && typeof obj.content === "string" && fs.existsSync(obj.content)) {
        slide.addImage(optionsFromBbox(obj, { path: obj.content, x: 0.8, y, w: 5.5, h: 3.1 }));
        y += 3.35;
      } else {
        const content = typeof obj.content === "string" ? obj.content : JSON.stringify(obj.content, null, 2);
        slide.addText(content, optionsFromBbox(obj, {
          x: 0.75,
          y,
          w: 11.4,
          h: 1.25,
          fontSize: 17,
          color: "111827",
          fit: "shrink",
          margin: 0.05
        }));
        y += 1.35;
      }
    }
    if (slidePlan.speaker_notes) {
      slide.addNotes(String(slidePlan.speaker_notes));
    }
  }

  await pptx.writeFile({ fileName: outPath });
  console.log(`Wrote ${outPath}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
