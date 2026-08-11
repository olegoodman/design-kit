#!/usr/bin/env python3
"""Edit / compose with reference images via GPT Image 2.

Use this when you need to keep a real logo, product photo, or person consistent —
the model treats `--refs` images as authoritative source material and will
preserve them rather than hallucinate.

Examples:
    edit.py "place this logo in the top-right corner of a cinematic plaster wall scene" \
        --refs ~/.../leinos_logo.png \
        --size 1536x864 -o slide.png

    edit.py "show the product on a quiet bathroom shelf" \
        --refs ~/.../bucket.png,~/.../logo.png \
        --size 1080x1920 -o reel.png
"""
from __future__ import annotations

import argparse
import base64
import sys
from pathlib import Path

from _client import build_client, call_safely, load_config


def parse_size(s: str) -> str:
    if "x" not in s:
        raise argparse.ArgumentTypeError("size must be WxH e.g. 1536x864")
    w, h = s.lower().split("x")
    int(w); int(h)
    return f"{w}x{h}"


def parse_refs(s: str) -> list[Path]:
    paths = [Path(p.strip()).expanduser() for p in s.split(",") if p.strip()]
    for p in paths:
        if not p.exists():
            raise argparse.ArgumentTypeError(f"reference image not found: {p}")
    return paths


def main():
    p = argparse.ArgumentParser(description="Edit/compose image with reference images via GPT Image 2")
    p.add_argument("prompt")
    p.add_argument("-o", "--output", required=True)
    p.add_argument("--refs", type=parse_refs, required=True,
                   help="Comma-separated paths to reference images (logo, product photo, etc.)")
    p.add_argument("--size", type=parse_size, help="WxH (default from config.yaml)")
    p.add_argument("--quality", choices=["low", "medium", "high", "auto"])
    args = p.parse_args()

    cfg = load_config()
    client = build_client(cfg)
    size = args.size or cfg.get("defaults", {}).get("size", "1536x864")
    quality = args.quality or cfg.get("defaults", {}).get("quality", "high")
    model = cfg.get("model", "gpt-image-2")

    # OpenAI SDK accepts either a list of file handles or a single file
    image_files = [open(p, "rb") for p in args.refs]
    print(f"→ editing with {len(image_files)} ref(s), {size} {quality}...", file=sys.stderr)
    try:
        res = call_safely(
            client.images.edit,
            model=model,
            image=image_files if len(image_files) > 1 else image_files[0],
            prompt=args.prompt,
            size=size,
            quality=quality,
        )
    finally:
        for f in image_files:
            f.close()

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    img = res.data[0]
    if img.b64_json:
        data = base64.b64decode(img.b64_json)
    elif getattr(img, "url", None):
        import urllib.request
        req = urllib.request.Request(img.url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as r:
            data = r.read()
    else:
        print("⚠️  proxy returned neither b64_json nor url", file=sys.stderr)
        sys.exit(3)
    out.write_bytes(data)
    print(f"✅ {out}")


if __name__ == "__main__":
    main()
