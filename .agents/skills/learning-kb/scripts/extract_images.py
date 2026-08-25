#!/usr/bin/env python3
"""Extract embedded images from a PDF, dedupe, and lay them out for learning-kb.

Usage:
  extract_images.py <pdf> --out <dir>

For each unique embedded image (deduped by pixel-content hash) writes:
  <dir>/<theme>/imgs/p<page>-<idx>.png
and a manifest <dir>/<theme>/imgs/manifest.json mapping each saved file to the
(page, index) occurrences it came from, so the agent can place images by provenance.

Images that are tiny (<= 64px on either side) are skipped as UI-chrome noise.
"""
import sys
import json
import hashlib
import argparse
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    sys.stderr.write("pypdf not found. Install: .agents/venv/bin/pip install pypdf[image]\n")
    sys.exit(2)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--out", required=True, help="theme dir, e.g. zap/")
    args = ap.parse_args()

    reader = PdfReader(args.pdf)
    out_dir = Path(args.out) / "imgs"
    out_dir.mkdir(parents=True, exist_ok=True)

    seen: dict[str, str] = {}          # hash -> saved filename
    manifest: dict[str, list] = {}     # saved filename -> [(page, idx)]
    saved = 0
    skipped_tiny = 0

    for pno, page in enumerate(reader.pages, 1):
        try:
            images = page.images
        except Exception:  # noqa: BLE001
            continue
        for iidx, img in enumerate(images, 1):
            try:
                pil = img.image
            except Exception:  # noqa: BLE001
                continue
            w, h = pil.size
            if w <= 64 or h <= 64:
                skipped_tiny += 1
                continue
            data = pil.tobytes()
            hkey = hashlib.sha256(data).hexdigest()
            if hkey in seen:
                manifest[seen[hkey]].append([pno, iidx])
                continue
            fname = f"p{pno:02d}-{iidx:02d}.png"
            pil.save(out_dir / fname)
            seen[hkey] = fname
            manifest[fname] = [[pno, iidx]]
            saved += 1

    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"UNIQUE:{saved} SKIPPED_TINY:{skipped_tiny} DIR:{out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
