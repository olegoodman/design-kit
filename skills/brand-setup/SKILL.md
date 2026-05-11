---
name: brand-setup
description: >
  One-time project setup for brand voice and design token system.
  Use when initializing brand guidelines and design tokens for a new project,
  or when a project has design data but no docs/brand-guidelines.md or assets/design-tokens.json.
  Do NOT use for updating existing brand (use brand:update), creating assets (use design),
  or routine design work (use design-orchestrator).
---

# Brand Setup

Initialize brand and design-system infrastructure for a project. Runs once per project — scans what exists, creates what's missing, verifies the pipeline works.

## Pre-check

Before starting, verify setup is needed:

1. Check if `docs/brand-guidelines.md` exists
2. Check if `assets/design-tokens.json` exists
3. If both exist and are populated — **stop**. Tell user: "Brand already configured. Use `/brand update` to modify."

## Step 1: Audit existing design data

Scan the project for brand and design information already present:

- `tailwind.config.*` — colors, fonts, theme extensions
- `globals.css`, `app.css`, `index.css` — CSS variables, custom properties
- `CLAUDE.md`, `.impeccable.md` — brand voice, design direction notes
- `src/` — recurring color values, font imports, component patterns
- `public/` — logos, favicons (extract brand colors)
- `package.json` — font packages (@fontsource, google-fonts)
- Any existing `brand-guidelines`, `style-guide`, `design-tokens` files

Collect into a summary: colors (with hex), fonts (heading + body), voice keywords, existing tokens.

If critical data is missing (no colors found, no fonts), ask the user — do not invent defaults.

## Step 2: Create brand guidelines

Use template from `~/.claude/skills/brand/templates/brand-guidelines-starter.md` as structure.
Fill every field with **real project data** from Step 1. Sections to populate:

- Quick Reference (primary color, font, voice)
- Color Palette (primary, secondary, neutral, semantic — all from project)
- Typography (heading font, body font, scale)
- Brand Voice (tone, personality, do/don't)
- Logo Usage (if logo files found)

Show the draft to the user. Wait for approval before saving to `docs/brand-guidelines.md`.

## Step 3: Create design tokens

Use template from `~/.claude/skills/design-system/templates/design-tokens-starter.json` as structure.
Map project colors → primitive layer, then build semantic and component layers:

```
Primitive:  project hex values (blue.600: #2563EB)
Semantic:   purpose aliases (primary: {primitive.color.blue.600})
Component:  per-component (button.bg: {semantic.color.primary})
```

Include dark mode overrides if the project uses dark theme.

Show the draft to the user. Wait for approval before saving to `assets/design-tokens.json`.

## Step 4: Generate CSS and sync

1. Generate `assets/design-tokens.css` from JSON:
   ```bash
   node ~/.claude/skills/design-system/scripts/generate-tokens.cjs --config assets/design-tokens.json -o assets/design-tokens.css
   ```
2. If script fails, generate CSS manually from the JSON (var declarations matching the token structure).

## Step 5: Verify

Run brand context extraction:
```bash
node ~/.claude/skills/brand/scripts/inject-brand-context.cjs
```

Show output to user. Confirm:
- Colors extracted correctly
- Fonts extracted correctly
- Voice keywords present

Report: "Brand setup complete. Files created: docs/brand-guidelines.md, assets/design-tokens.json, assets/design-tokens.css"

## Common Mistakes

- **Using template defaults instead of project data.** The whole point is extracting what already exists. Blue/#2563EB from the starter template should never appear unless the project actually uses that color.
- **Skipping user review.** Always show guidelines and tokens before saving. The user knows their brand better than the audit.
- **Running in a project that's already set up.** Check pre-check first. Overwriting existing brand files destroys intentional customization.
