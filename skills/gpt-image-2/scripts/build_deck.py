#!/usr/bin/env python3
"""Assemble multiple PNG slides into a single PDF.

Examples:
    build_deck.py slide-*.png -o deck.pdf
    build_deck.py 01.png 02.png 03.png -o deck.pdf
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import fitz  # PyMuPDF


def main():
    p = argparse.ArgumentParser(description="Assemble PNG slides into a PDF")
    p.add_argument("images", nargs="+", help="PNG files in order")
    p.add_argument("-o", "--output", required=True, help="Output PDF path")
    args = p.parse_args()

    pngs = []
    for pat in args.images:
        path = Path(pat).expanduser()
        if path.exists():
            pngs.append(path)
        else:
            # Allow shell glob fallback (in case shell didn't expand)
            from glob import glob
            pngs.extend(Path(p).expanduser() for p in sorted(glob(pat)))

    if not pngs:
        print("❌ no input images", file=sys.stderr)
        sys.exit(1)

    doc = fitz.open()
    for png in pngs:
        img_doc = fitz.open(png)
        rect = img_doc[0].rect
        pdf_bytes = img_doc.convert_to_pdf()
        img_doc.close()
        single = fitz.open("pdf", pdf_bytes)
        page = doc.new_page(width=rect.width, height=rect.height)
        page.show_pdf_page(page.rect, single, 0)
        single.close()

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(out), garbage=4, deflate=True)
    doc.close()
    print(f"✅ {out} — {len(pngs)} pages")


if __name__ == "__main__":
    main()
