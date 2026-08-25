#!/usr/bin/env python3
"""Extract text from a PDF for the learning-kb skill.

Usage:
  extract_pdf.py <pdf_path> [--out <text_path>] [--pages <a>-<b>]

Outputs plain text (one line per source line, blank line between blocks) to
<text_path> (default: <pdf_path>.txt). Prints the total page count to stdout.
"""
import sys
import argparse
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    sys.stderr.write(
        "pypdf not found. Install it: python3 -m venv .agents/venv && "
        ".agents/venv/bin/pip install pypdf\n"
    )
    sys.exit(2)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--out")
    ap.add_argument("--pages", help="e.g. 1-20 or 35-35")
    args = ap.parse_args()

    reader = PdfReader(args.pdf)
    total = len(reader.pages)
    print(f"PAGES:{total}")

    lo, hi = 1, total
    if args.pages:
        a, b = args.pages.split("-")
        lo = int(a)
        hi = int(b) if b else total

    out = Path(args.out) if args.out else Path(args.pdf).with_suffix(".txt")
    with out.open("w", encoding="utf-8") as f:
        for i in range(lo - 1, min(hi, total)):
            try:
                text = reader.pages[i].extract_text() or ""
            except Exception as e:  # noqa: BLE001
                text = f"\n[page {i+1} extraction error: {e}]\n"
            f.write(f"\n\n----- page {i+1} -----\n\n")
            f.write(text)
    print(f"WROTE:{out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
