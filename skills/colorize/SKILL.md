---
name: colorize
description: >
  Add strategic color to monochromatic or dull designs. Fixes palette issues, low contrast,
  monotone sections, and weak color hierarchy. Use when the design-orchestrator routes to
  colorize, when critique identifies Brand Consistency or Screenshot-Worthiness color issues,
  or when user says "too gray", "needs more color", "dull", "monochromatic", "palette feels
  off", "no warmth", or "colors don't work together". Do NOT use for: layout/spacing
  (use arrange), typography (use typeset), brand palette selection from scratch
  (use ui-ux-pro-max or brand), or toning down aggressive colors (use quieter).
---

# Colorize — Strategic Color

Add color with purpose. Every color choice should communicate something — hierarchy, state, emotion, or brand. You're not painting walls randomly; you're using color as a functional design tool.

## Protocol

### Step 1: Read and Map the Color System

Read the code. Before adding any color, understand what exists:

- **Palette in use**: which Tailwind colors appear? (gray-*, blue-*, emerald-*, etc.)
- **Brand colors**: are there custom colors in tailwind.config? CSS custom properties?
- **Color roles**: which color = primary action? secondary? accent? destructive?
- **Neutral range**: how many gray shades? (gray-50 through gray-900)
- **Current contrast**: light bg + dark text? dark bg + light text? mixed?

Map the color hierarchy: what draws the eye first? What fades into background?

### Step 2: Check for Issues

#### Monotone / Gray Desert
- **All-gray syndrome**: entire section uses only gray shades — no color accent anywhere
- **Undefined primary**: no single color stands out as "the action color" (CTAs blend in)
- **No color differentiation**: different types of elements (links, buttons, tags, badges) all look the same

#### Palette Harmony
- **Too many hues**: 4+ unrelated colors competing — looks chaotic. Stick to 1-2 hues + neutrals
- **Clashing temperatures**: warm accent (orange) on cool palette (blue/slate) without intentional contrast
- **Unanchored accent**: bright color appears once randomly — feels like a mistake, not a choice

#### Contrast & Readability
- **Low-contrast text**: text-gray-400 on white = fails WCAG AA (4.5:1 needed). Text-gray-500 is borderline
- **Invisible secondary text**: muted text too similar to background — information gets lost
- **CTA doesn't pop**: primary button same visual weight as surrounding elements

#### Color as Hierarchy
- **Flat color weight**: everything same saturation/brightness — no visual hierarchy via color
- **Important = invisible**: key information (price, status, deadline) has no color emphasis
- **Decorative > functional**: colors used for decoration but not to communicate meaning

### Step 3: Apply Fixes

Fix directly with Edit tool. Each change should be intentional.

**Key principles:**
- **60-30-10 rule**: 60% dominant neutral, 30% secondary color, 10% accent. This creates natural hierarchy
- **One hue + variations**: safer than multiple hues. blue-50/100/500/700/900 gives rich palette from one hue
- **Warm vs cool signals**: warm colors (amber, orange) = friendly, approachable. Cool colors (blue, slate) = professional, calm
- **Color = meaning**: once a color means "primary action", use it consistently for all primary actions
- **Saturation creates depth**: desaturated versions of accent color for backgrounds (blue-50), full saturation for interactive elements (blue-600)

**Common fix patterns:**

```
Gray desert → add accent:
  Before: bg-gray-100, text-gray-700, border-gray-200
  After:  bg-gray-50, text-gray-700, border-gray-200 + blue-600 CTA + blue-50 highlight bg

Low-contrast text:
  Before: text-gray-400 (contrast ~3:1 on white)
  After:  text-gray-600 (contrast ~5.7:1 on white)

CTA blends in:
  Before: bg-gray-200 text-gray-700 (looks like a disabled element)
  After:  bg-blue-600 text-white hover:bg-blue-700 (clear primary action)

Flat hierarchy:
  Before: all headings text-gray-900, all body text-gray-700
  After:  headings text-gray-900, body text-gray-600, captions text-gray-500
```

### Step 4: Report

```markdown
## Colorize Report: [Section Name]

**Fixes applied: N**
**Palette used: [e.g., gray + blue-600 primary + amber-500 accent]**

| # | Category | What | Before | After |
|---|---|---|---|---|
| 1 | Accent | No primary color | all gray | blue-600 on CTAs |
| 2 | Contrast | Body text too light | text-gray-400 | text-gray-600 |
| 3 | Hierarchy | Headings same as body | text-gray-700 both | gray-900 / gray-600 |
| 4 | Background | Flat white everywhere | bg-white | alternating bg-white / bg-gray-50 |

**Color roles established: primary=blue-600, accent=amber-500, neutral=gray**
```

## Scope Boundaries

- Fix color palette, contrast, color hierarchy, accent usage, background variation
- Conform to existing brand palette if one exists — don't invent new brand colors
- Don't change layout or spacing — that's `arrange`
- Don't change typography — that's `typeset`
- If the design is too colorful/loud, that's `quieter`, not colorize
