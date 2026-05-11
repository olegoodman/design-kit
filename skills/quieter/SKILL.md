---
name: quieter
description: >
  Tone down aggressive, overstimulating, or chaotic designs. Reduces visual intensity while
  preserving quality and information. Use when the design-orchestrator routes to quieter,
  or when user says "too loud", "overwhelming", "aggressive", "garish", "too bold", "tone
  it down", "too many colors", or "visual noise". Do NOT use for: amplifying bland designs
  (use bolder), adding color (use colorize), or layout restructuring (use arrange).
---

# Quieter — Reduce Visual Intensity

Calm the design down without making it boring. The goal: from "shouting" to "confident." Every reduction should preserve the design's intent while removing excess.

## Protocol

### Step 1: Identify Sources of Visual Noise

Read the code. Find what's fighting for attention:
- **Color overload**: too many saturated colors competing
- **Weight overload**: everything bold/black, nothing recedes
- **Size overload**: multiple oversized elements per section
- **Animation overload**: too many moving elements
- **Decoration overload**: gradients, shadows, borders, patterns all at once
- **Contrast overload**: everything is high-contrast, nothing is subtle

### Step 2: Apply Reductions (pick 2-3)

| Move | What it does | Example |
|---|---|---|
| **Desaturate** | Replace full-saturation with muted tones | blue-600 → blue-500, or use slate instead of gray |
| **Reduce weight** | Lighten heavy text elements | font-black → font-bold, font-bold → font-semibold |
| **Scale down** | Reduce oversized elements | text-6xl → text-4xl, p-12 → p-8 |
| **Simplify shadows** | Remove or reduce shadow layers | shadow-2xl → shadow-md, or remove entirely |
| **Mute backgrounds** | Tone down bright backgrounds | bg-blue-600 → bg-blue-50 with blue-600 text |
| **Remove decoration** | Strip gradients, borders, patterns that don't serve function | gradient bg → solid bg |
| **Slow/remove animation** | Reduce motion or remove decorative animations | Remove parallax, reduce hover scale |

**Key principles:**
- **One voice per section**: reduce until one element clearly leads, rest support
- **Hierarchy through subtlety**: muted elements make the important ones stand out without screaming
- **Preserve the intent**: if the design was bold for brand reasons, keep the boldness — just focus it

### Step 3: Report

```markdown
## Quieter Report: [Section Name]

**Reductions applied: N**

| # | What | Before | After | Why |
|---|---|---|---|---|
| 1 | Desaturate bg | bg-red-600 | bg-red-50 text-red-700 | Background competed with CTA |
| 2 | Reduce heading weight | font-black text-5xl | font-bold text-4xl | Two oversized headings competed |
| 3 | Remove shadow | shadow-2xl on all cards | shadow-sm | Heavy shadows created visual noise |
```
