#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "Usage: scripts/render_pptx_preview.sh deck.pptx [out_dir]" >&2
  exit 2
fi

deck_path="$1"
out_dir="${2:-preview}"

if [[ ! -f "$deck_path" ]]; then
  echo "Missing deck: $deck_path" >&2
  exit 2
fi

if ! command -v soffice >/dev/null 2>&1; then
  echo "Missing LibreOffice CLI: install LibreOffice and ensure 'soffice' is on PATH." >&2
  exit 2
fi

mkdir -p "$out_dir"
soffice --headless --convert-to pdf --outdir "$out_dir" "$deck_path" >/dev/null

pdf_path="$out_dir/$(basename "${deck_path%.*}").pdf"
if [[ -f "$pdf_path" ]] && command -v pdftoppm >/dev/null 2>&1; then
  pdftoppm -png -r 160 "$pdf_path" "$out_dir/slide" >/dev/null
fi

echo "Wrote preview artifacts to $out_dir"
