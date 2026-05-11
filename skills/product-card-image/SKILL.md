---
name: product-card-image
description: Generate professional product card images for LEINOS website. Use this skill whenever the user asks to create, generate, update, or redo product images, product cards, product photos, or packshot composites. Also use when the user references product image pipeline, card backgrounds, or wants to process multiple product images in batch. Triggers on phrases like "сделай карточки", "обнови картинки продуктов", "product images", "packshot", or any reference to the 3-step composite pipeline.
---

# Product Card Image Pipeline

Generate photorealistic product card images by compositing real packshot photos onto category-specific backgrounds, then using Gemini AI to blend them naturally.

## Why this pipeline exists

LEINOS sells natural wood coatings. AI image generators (like Gemini `/generate`) draw fake product cans instead of using the real ones. Simple ImageMagick compositing looks "pasted" — the can floats above the surface. This 3-step pipeline solves both problems: ImageMagick handles precise positioning, Gemini handles photorealistic integration (shadows, lighting, blending), and the real packshot is preserved exactly.

## Project context

- Working directory: `/Users/zep4ik/AI/projects/leinos-web`
- All commands run from project root
- Card aspect ratio on site: **4:3** (`aspect-[4/3]` with `object-cover` in `ProductGrid.tsx`)
- Output format: **800px wide WebP**, target 25-40KB
- Product data: `src/src/content/data.ts` — `image` field already exists for all 43 products

## Three backgrounds by product category

Each category has its own background to reflect brand identity:

| Category | Background | File |
|----------|-----------|------|
| **Wood** (interior-wood, exterior-wood, lacquer) | Dark walnut table, warm golden light, soft greenery | `nanobanana-output/bg-option-2-dark-walnut.png` |
| **Mineral** (interior-walls) | Light pine surface, Scandinavian style, bright white wall | `nanobanana-output/bg-option-3-light-pine.png` |
| **Care** | Light oak table, warm beige wall, soft daylight | `nanobanana-output/bg-option-1-oak-table.png` |

Category mapping for each product is in `data.ts` field `category`. Map like this:
- `interior-wood`, `exterior-wood`, `lacquer` → Wood background
- `interior-walls` → Mineral background
- `care` → Care background

### Background preparation (one-time)

Backgrounds are 1024x1024 squares. Crop to 4:3 before use:

```bash
magick nanobanana-output/bg-option-2-dark-walnut.png -gravity South -crop 1024x768+0+0 +repage /tmp/bg-wood-4x3.png
magick nanobanana-output/bg-option-3-light-pine.png -gravity South -crop 1024x768+0+0 +repage /tmp/bg-mineral-4x3.png
magick nanobanana-output/bg-option-1-oak-table.png -gravity South -crop 1024x768+0+0 +repage /tmp/bg-care-4x3.png
```

## Packshot source

- Directory: `Фото банок/all/`
- Prefer **0.75l** size when multiple sizes available
- All packshots are PNG with transparent background (alpha channel)
- Example filename: `150-0,75l-Holzgrund.png`

## The Pipeline (3 steps)

### Step 1: ImageMagick Composite

Position the packshot on the category background. No shadow — Gemini handles that.

```bash
BG="/tmp/bg-wood-4x3.png"  # or bg-mineral-4x3.png or bg-care-4x3.png
PACKSHOT="Фото банок/all/150-0,75l-Holzgrund.png"
TARGET_H=$(( 768 * 72 / 100 ))  # 553px = 72% of frame height

magick "$BG" \
  \( "$PACKSHOT" -resize "x${TARGET_H}" \) \
  -gravity South -geometry +0+40 -composite \
  /tmp/composite-temp.png
```

Key parameters:
- **Can height**: 72% of frame height (553px out of 768px)
- **Position**: centered horizontally, 40px above bottom edge
- **No shadow**: ImageMagick only does positioning

### Step 2: Gemini /edit Blend

Make the composite look like a real photograph. This is the proven prompt — do not modify it without testing:

```bash
gemini --yolo "/edit '/tmp/composite-temp.png' 'The product can has been placed on a wooden table but it looks pasted. Make it look photorealistic as if the can was actually photographed standing on this table. Specifically: 1) Add a natural soft shadow behind and to the right of the can, as if warm light comes from the left - the shadow should fall gently on the table surface behind the can, like a real photograph. 2) Add natural contact darkening where the can base meets the wood. 3) Subtly adjust the lighting on the can to match the warm left-side lighting of the scene. 4) Blend the bottom edge of the can naturally with the table. Do NOT add any reflection. Do NOT change the label, logo, text, colors, or lid. Do NOT add new objects. Keep background unchanged.' --preview"
```

The output goes to `nanobanana-output/` with an auto-generated filename.

### Step 3: Convert and Deploy

```bash
# Find the latest generated file
LATEST=$(ls -t nanobanana-output/edit*.png | head -1)

# Resize to 800px width and convert to WebP
sips -Z 800 "$LATEST" --out /tmp/product-resized.png > /dev/null 2>&1
cwebp -q 80 /tmp/product-resized.png -o "src/public/images/products/{slug}-{code}.webp" > /dev/null 2>&1
```

Naming convention: `{product-slug}-{product-code}.webp`
Example: `impregnation-wood-primer-150.webp`

The slug and code come from `data.ts`.

## Quality Checklist

After each image, verify:

- [ ] Original packshot preserved exactly (label, red tree logo, text, lid, colors)
- [ ] Natural shadow falls behind/right of can (light source from left)
- [ ] Can looks like it's standing ON the table (not floating)
- [ ] No black rim or artifact at can base
- [ ] No reflection on wood surface
- [ ] No extra objects added by Gemini
- [ ] File size 25-40KB
- [ ] Image fills card without cropping important parts (4:3 aspect)

## Batch Processing

When processing multiple products, follow this order:

1. Crop all 3 backgrounds to 4:3 (one-time)
2. Group products by category
3. Process each group: Step 1 → Step 2 → Step 3 per product
4. After each product, visually verify with Read tool
5. After batch, rebuild site: `cd src && npm run build`

For efficiency, run Step 1 (ImageMagick) for several products, then Step 2 (Gemini) one at a time (Gemini needs sequential processing), then Step 3 (convert) in batch.

## Products WITHOUT packshots

6 products have no packshot photo: 266, 637, 815, 850, 855, 910.

These use a DIFFERENT approach — scene-only lifestyle images via Nano Banana `/generate` (not this pipeline). Generate a scene showing the result of using the product, without any product can in the frame.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Gemini alters the label/logo | Re-run Step 2 — results vary between runs |
| Black rim at can base | Make sure Step 1 has NO shadow (no `-shadow` flag in magick) |
| Can looks floating | Re-run Step 2 with emphasis on "contact darkening" |
| Image too dark/light | Check background file — may need regeneration |
| Wrong aspect ratio | Verify background was cropped to 1024x768 |
| Gemini adds objects | Re-run — the prompt says "do not add objects" but Gemini occasionally does |
