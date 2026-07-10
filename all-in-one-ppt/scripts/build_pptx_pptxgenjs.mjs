#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);

function fail(message) {
  throw new Error(message);
}

function color(value, fallback) {
  if (typeof value !== "string" || !value) return fallback;
  return value.replace(/^#/, "").toUpperCase();
}

function bboxFor(obj) {
  const bbox = obj?.bbox;
  if (!bbox || typeof bbox !== "object") fail(`${obj?.id || "object"} is missing bbox`);
  for (const key of ["x", "y", "w", "h"]) {
    if (typeof bbox[key] !== "number") fail(`${obj?.id || "object"}.bbox.${key} must be numeric`);
  }
  return { x: bbox.x, y: bbox.y, w: bbox.w, h: bbox.h };
}

function textOptions(obj, fallback = {}) {
  const box = bboxFor(obj);
  const style = obj.style || {};
  return {
    ...box,
    fontFace: style.font_face || fallback.fontFace || "Aptos",
    fontSize: style.font_size || fallback.fontSize || 20,
    color: color(style.color, fallback.color || "111827"),
    bold: Boolean(style.bold),
    italic: Boolean(style.italic),
    align: style.align || fallback.align || "left",
    valign: style.valign || fallback.valign || "top",
    margin: style.margin ?? fallback.margin ?? 0.05,
    breakLine: false,
    fit: "shrink",
    ...fallback,
  };
}

function normalizeTable(content, id) {
  if (Array.isArray(content) && content.every(Array.isArray)) return content;
  if (content && typeof content === "object" && Array.isArray(content.rows)) {
    return Array.isArray(content.headers) ? [content.headers, ...content.rows] : content.rows;
  }
  fail(`${id} table content must be an array of rows or {headers, rows}`);
}

function normalizeChart(content, id, pptx) {
  if (!content || typeof content !== "object" || !Array.isArray(content.series) || !content.series.length) {
    fail(`${id} chart content must contain a non-empty series array`);
  }
  for (const [index, series] of content.series.entries()) {
    if (!series || !Array.isArray(series.labels) || !Array.isArray(series.values)) {
      fail(`${id} chart series ${index} must contain labels and values arrays`);
    }
    if (series.labels.length !== series.values.length) {
      fail(`${id} chart series ${index} labels/values length mismatch`);
    }
  }
  const chartType = content.chart_type || "bar";
  const resolved = pptx.ChartType[chartType];
  if (!resolved) fail(`${id} unsupported chart_type: ${chartType}`);
  return { chartType: resolved, series: content.series };
}

async function main() {
  const planArg = process.argv[2];
  const outArg = process.argv[3] || "deck.pptx";
  if (!planArg) {
    console.error("Usage: build_pptx_pptxgenjs.mjs slide_plan.json [out.pptx]");
    process.exit(2);
  }

  let pptxgenjs;
  try {
    pptxgenjs = require("pptxgenjs");
  } catch (error) {
    console.error("Missing or unusable dependency: run npm install in all-in-one-ppt");
    console.error(error.message);
    process.exit(2);
  }

  const PptxGenJS = pptxgenjs.default || pptxgenjs;
  const planPath = path.resolve(planArg);
  const outPath = path.resolve(outArg);
  const planDir = path.dirname(planPath);
  const plan = JSON.parse(fs.readFileSync(planPath, "utf8"));
  const assets = new Map((plan.assets || []).map((asset) => [asset.id, asset]));
  const pptx = new PptxGenJS();

  const canvas = plan.canvas || { width: 13.333, height: 7.5 };
  if (Math.abs(canvas.width - 13.333) < 0.02 && Math.abs(canvas.height - 7.5) < 0.02) {
    pptx.layout = "LAYOUT_WIDE";
  } else if (Math.abs(canvas.width - 10) < 0.02 && Math.abs(canvas.height - 7.5) < 0.02) {
    pptx.layout = "LAYOUT_4X3";
  } else {
    pptx.defineLayout({ name: "CUSTOM", width: canvas.width, height: canvas.height });
    pptx.layout = "CUSTOM";
  }

  const style = plan.style || {};
  const fonts = Array.isArray(style.fonts) && style.fonts.length ? style.fonts : ["Aptos", "Aptos Display"];
  const bodyFont = fonts[0];
  const headFont = fonts[1] || fonts[0];
  const palette = Array.isArray(style.colors) ? style.colors : [];
  const textColor = color(palette[0], "111827");
  const accentColor = color(palette[1], "2563EB");

  pptx.author = "all-in-one-ppt";
  pptx.subject = plan.deck_title || "Editable PowerPoint deck";
  pptx.title = plan.deck_title || "Editable PowerPoint deck";
  pptx.company = "all-in-one-ppt";
  pptx.lang = style.language || "en-US";
  pptx.theme = { headFontFace: headFont, bodyFontFace: bodyFont, lang: pptx.lang };

  for (const slidePlan of plan.slides || []) {
    const slide = pptx.addSlide();
    slide.background = { color: color(style.background, "FFFFFF") };

    slide.addText(String(slidePlan.title || "Untitled"), {
      x: 0.6,
      y: 0.38,
      w: canvas.width - 1.2,
      h: 0.5,
      fontFace: headFont,
      fontSize: 28,
      bold: true,
      color: textColor,
      margin: 0,
      fit: "shrink",
    });
    if (slidePlan.takeaway) {
      slide.addText(String(slidePlan.takeaway), {
        x: 0.62,
        y: 1.0,
        w: canvas.width - 1.24,
        h: 0.35,
        fontFace: bodyFont,
        fontSize: 15,
        color: accentColor,
        margin: 0,
        fit: "shrink",
      });
    }

    for (const obj of slidePlan.objects || []) {
      const type = obj.type;
      const id = obj.id || `${type}-object`;
      if (type !== "image" && obj.materialization !== "native") {
        fail(`${id} is ${obj.materialization}; the smoke builder only accepts native semantic objects`);
      }

      if (["text", "quote", "code", "equation", "icon"].includes(type)) {
        const content = typeof obj.content === "string" ? obj.content : JSON.stringify(obj.content, null, 2);
        slide.addText(content, textOptions(obj, {
          fontFace: type === "code" ? "Aptos Mono" : bodyFont,
          italic: type === "quote",
          color: textColor,
        }));
      } else if (type === "bullets") {
        if (!Array.isArray(obj.content)) fail(`${id} bullets content must be an array`);
        const runs = obj.content.map((item) => ({
          text: String(item),
          options: { bullet: { type: "bullet" }, breakLine: true },
        }));
        slide.addText(runs, textOptions(obj, { fontFace: bodyFont, color: textColor }));
      } else if (type === "image") {
        const asset = assets.get(obj.asset_id);
        if (!asset) fail(`${id} references missing asset ${obj.asset_id}`);
        if (!asset.path) fail(`${id} asset ${obj.asset_id} has no path`);
        const assetPath = path.isAbsolute(asset.path) ? asset.path : path.resolve(planDir, asset.path);
        if (!fs.existsSync(assetPath)) fail(`${id} asset file does not exist: ${assetPath}`);
        const box = bboxFor(obj);
        const fit = obj.style?.fit === "cover" ? "cover" : "contain";
        slide.addImage({
          path: assetPath,
          ...box,
          sizing: { type: fit, w: box.w, h: box.h },
          altText: asset.alt_text || id,
          objectName: id,
        });
      } else if (type === "table") {
        const rows = normalizeTable(obj.content, id);
        const box = bboxFor(obj);
        slide.addTable(rows, {
          ...box,
          fontFace: obj.style?.font_face || bodyFont,
          fontSize: obj.style?.font_size || 16,
          color: color(obj.style?.color, textColor),
          border: { type: "solid", color: color(obj.style?.border_color, "D1D5DB"), pt: 1 },
          fill: color(obj.style?.fill, "FFFFFF"),
          margin: 0.06,
        });
      } else if (type === "chart") {
        const { chartType, series } = normalizeChart(obj.content, id, pptx);
        const box = bboxFor(obj);
        slide.addChart(chartType, series, {
          ...box,
          showLegend: obj.content.show_legend ?? series.length > 1,
          showTitle: false,
          showValue: obj.content.show_values ?? false,
          catAxisLabelFontFace: bodyFont,
          valAxisLabelFontFace: bodyFont,
          chartColors: obj.content.colors || [accentColor, "10B981", "F59E0B", "EF4444"],
          showCatName: false,
        });
      } else if (type === "shape") {
        const box = bboxFor(obj);
        const content = obj.content && typeof obj.content === "object" ? obj.content : {};
        const shapeType = pptx.ShapeType[content.shape || "rect"];
        if (!shapeType) fail(`${id} unsupported shape: ${content.shape}`);
        slide.addShape(shapeType, {
          ...box,
          fill: { color: color(content.fill, "E5E7EB"), transparency: content.transparency || 0 },
          line: { color: color(content.line, "9CA3AF"), width: content.line_width || 1 },
          objectName: id,
        });
        if (content.text) {
          slide.addText(String(content.text), {
            ...box,
            fontFace: bodyFont,
            fontSize: obj.style?.font_size || 16,
            color: color(obj.style?.color, textColor),
            align: obj.style?.align || "center",
            valign: obj.style?.valign || "middle",
            margin: 0.05,
            fit: "shrink",
          });
        }
      } else if (type === "connector") {
        const box = bboxFor(obj);
        const content = obj.content && typeof obj.content === "object" ? obj.content : {};
        slide.addShape(pptx.ShapeType.line, {
          ...box,
          line: {
            color: color(content.color, "6B7280"),
            width: content.width || 1.5,
            beginArrowType: content.begin_arrow || "none",
            endArrowType: content.end_arrow || "triangle",
          },
          objectName: id,
        });
      } else if (type === "diagram") {
        fail(`${id} diagram must be expanded into native shape, connector, and text objects for this smoke builder`);
      } else {
        fail(`${id} unsupported object type for the smoke builder: ${type}`);
      }
    }

    if (slidePlan.speaker_notes) slide.addNotes(String(slidePlan.speaker_notes));
  }

  fs.mkdirSync(path.dirname(outPath), { recursive: true });
  await pptx.writeFile({ fileName: outPath });
  console.log(`Wrote ${outPath}`);
}

main().catch((error) => {
  console.error(error.message || error);
  process.exit(1);
});
