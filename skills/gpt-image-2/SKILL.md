---
name: gpt-image-2
description: Generate or edit images via OpenAI's GPT Image 2 — production-grade image model with reasoning before rendering, 99% text accuracy, all 8 aspect ratios (incl. mobile-first 9:16), and reference-image preservation for branded logos/products. Use this skill whenever the user asks to make a slide, deck, banner, social post, branded mockup, infographic, marketing asset, or precision visual where text legibility and brand consistency matter — especially when reference images (logos, products, faces) must be kept intact across many slides. Use this OVER nano-banana when the work involves: rendered text inside the image, dense layouts, brand logos that must not drift, or vertical/landscape format flexibility. Russian triggers — "сделай слайд", "сгенерируй слайд", "презентация", "бренд-картинка", "vertical/9:16", "портрет/landscape", "рекламный креатив", "социальный пост", "инфографика", "GPT Image 2", "image-2".
---

# GPT Image 2 skill

OpenAI's flagship image generation model (released April 21, 2026) wrapped as a CLI tool for branded slide / asset / social-media work.

## When to use

- **Slides & decks** — single slides or full deck workflow, especially with rendered text, charts, infographics
- **Branded assets** — when a real logo / product photo / person must be preserved across many images (use `edit.py` with `--refs`)
- **Mobile-first** — 9:16 vertical for Instagram Reels / Stories / WhatsApp Status
- **Multi-format batches** — same prompt rendered as both 16:9 desktop and 9:16 mobile in one workflow
- **Multilingual visuals** — including Hindi / CJK rendered in image (text accuracy ~99%)

## When NOT to use

- Casual / playful illustrations, blog featured images → use `nano-banana` instead (cheaper, faster for low-stakes)
- Character consistency across many serial images (use Nano Banana Pro)
- Background removal / matting / color-correction → use Photoshop / cv2

## Architecture

```
~/.claude/skills/gpt-image-2/
├── SKILL.md             # this file
├── config.yaml          # endpoint + key + defaults — edit when key/balance runs out
├── scripts/
│   ├── _client.py       # shared client + credit/auth error detection
│   ├── generate.py      # text → image
│   ├── edit.py          # prompt + reference images → image
│   └── build_deck.py    # PNGs → single PDF
├── presets/
│   └── leinos-brand.yaml  # brand kit for LEINOS India project
└── output/              # default scratch space (not committed)
```

## Configuration & key rotation (IMPORTANT)

The endpoint and API key live in `config.yaml`:

```yaml
api:
  endpoint: https://llm-ai.hopto.org/v1
  key: sk-...
```

When the key runs out of credit, the user buys a new one (often with a different endpoint). Update `config.yaml` — no restart needed, the skill reads it on every invocation.

If a generation fails with auth/credit/quota error, the skill prints in Russian:

> ⚠️ GPT Image 2 не отвечает — похоже на закончившийся ключ или баланс.
> Обнови API: открой `~/.claude/skills/gpt-image-2/config.yaml` и замени api.endpoint и api.key на новые.

If you (Claude) see this message after a generation attempt, ask the user for the new endpoint and key, update the file, retry.

## Healthcheck

```bash
python3 ~/.claude/skills/gpt-image-2/scripts/_client.py
```

Lists models from the endpoint to confirm key + endpoint work. Cheap (free for most proxies). Run this first when troubleshooting.

## Usage

### Single image, text prompt

```bash
python3 ~/.claude/skills/gpt-image-2/scripts/generate.py \
  "cinematic close-up of lime plaster wall, raking daylight, mineral texture" \
  --size 1536x864 --quality high \
  -o ~/Desktop/wall.png
```

### With reference images (preserves logo / product)

```bash
python3 ~/.claude/skills/gpt-image-2/scripts/edit.py \
  "place this LEINOS bucket on a quiet bathroom shelf, dramatic side-lit, mineral white walls. Add the logo as a small bookmark in the top-right corner" \
  --refs /tmp/leinos_branding/leinos_logo_kurz.png,/Users/zep4ik/Desktop/lime\ paint\ 665/665\ 10l\ Kalkfarbe\ Kopie.png \
  --size 1536x864 --quality high \
  -o slide-cover.png
```

### Build a multi-page PDF deck from generated PNGs

```bash
python3 ~/.claude/skills/gpt-image-2/scripts/build_deck.py \
  ~/Desktop/deck/01.png ~/Desktop/deck/02.png ... \
  -o ~/Desktop/deck.pdf
```

## Aspect-ratio cheatsheet (all native to GPT Image 2)

| Use case | Size param | Ratio |
|---|---|---|
| Desktop slide / boardroom PDF | `1536x864` | 16:9 |
| Mobile Reel / Story / WhatsApp Status | `1080x1920` | 9:16 |
| Instagram feed post / square | `1024x1024` | 1:1 |
| Instagram portrait post | `1024x1280` | 4:5 |
| LinkedIn banner | `1584x528` | 3:1 |
| Cinematic poster | `2560x1440` | 16:9 (2K) |
| 4K landscape | `3840x2160` | 16:9 (4K) |
| 4K portrait | `2160x3840` | 9:16 (4K) |

Constraints (from OpenAI docs): max edge ≤ 3840px, both edges multiples of 16, long-to-short ratio ≤ 3:1, total pixels 655 360–8 294 400.

## Prompt patterns for branded slides

Treat the prompt as a **spec for a designer**, not an illustration request:

1. **Name the artifact**: "one pitch-deck slide titled X", "vertical Instagram Reel cover", "LinkedIn banner"
2. **Define canvas + hierarchy**: "16:9 dark slate background, big number on left third, supporting copy on right"
3. **Provide real text exactly**: include all rendered text verbatim in the prompt
4. **Describe visual language**: typography, palette, photographic vs illustration, mood
5. **Constrain**: "no clipart, no stock-photo people, no decorative gradients, generous white space"
6. **Add reference images** for any element that must be preserved (`edit.py --refs`)

Anti-patterns: vague prompts, decorative requests without spec, trying to render brand-critical text as part of generated photography (text in illustration is fine because of 99% accuracy, but keep it intentional).

## Cost guide (rough — varies by proxy)

| Quality | Square 1024² | Portrait 1024×1536 | Landscape 1536×1024 |
|---|---|---|---|
| Low | 272 tokens | 408 | 400 |
| Medium | 1056 | 1584 | 1568 |
| High | 4160 | 6240 | 6208 |

12 high-quality landscape slides ≈ 75K tokens. Run `_client.py` healthcheck regularly to confirm balance.

## Limits

- No transparent backgrounds (use solid color and key out later if needed)
- No streaming — full image returns at once
- Edit mode keeps source layout — for completely new compositions use `generate.py`
