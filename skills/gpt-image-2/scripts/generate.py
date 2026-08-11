#!/usr/bin/env python3
"""Generate an image from a text prompt using GPT Image 2.

Examples:
    generate.py "cinematic lime plaster wall, raking daylight" -o wall.png
    generate.py "..." --size 1080x1920 --quality high -o mobile.png
    generate.py "..." --size 1536x864 -o desktop.png
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


def main():
    p = argparse.ArgumentParser(description="Generate image via GPT Image 2")
    p.add_argument("prompt")
    p.add_argument("-o", "--output", required=True, help="Output PNG path")
    p.add_argument("--size", type=parse_size, help="WxH (e.g. 1536x864). Defaults from config.yaml")
    p.add_argument("--quality", choices=["low", "medium", "high", "auto"], help="Render quality")
    p.add_argument("--n", type=int, default=1, help="Number of images (writes -1.png, -2.png if >1)")
    args = p.parse_args()

    cfg = load_config()
    client = build_client(cfg)
    size = args.size or cfg.get("defaults", {}).get("size", "1536x864")
    quality = args.quality or cfg.get("defaults", {}).get("quality", "high")
    model = cfg.get("model", "gpt-image-2")

    print(f"→ generating {size} {quality} via {model}...", file=sys.stderr)
    res = call_safely(
        client.images.generate,
        model=model,
        prompt=args.prompt,
        size=size,
        quality=quality,
        n=args.n,
    )

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    for i, img in enumerate(res.data, 1):
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
        path = out if args.n == 1 else out.with_stem(f"{out.stem}-{i}")
        path.write_bytes(data)
        print(f"✅ {path}")


if __name__ == "__main__":
    main()
