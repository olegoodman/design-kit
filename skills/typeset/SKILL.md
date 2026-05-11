---
name: typeset
description: >
  Fix typography — font choices, hierarchy, sizing, weight, line height, letter spacing, and
  readability. Use when the design-orchestrator routes to typeset, when critique identifies
  Visual Hierarchy issues related to text, or when user says "fonts look wrong", "text
  hierarchy unclear", "headings don't stand out", "readability issues", "sizing feels off",
  "font pairing", or "text is hard to read". Do NOT use for: layout/spacing (use arrange),
  color (use colorize), content writing (just edit text), or brand font selection
  (use ui-ux-pro-max or brand).
---

# Typeset — Typography

Fix how text looks and reads. Typography is the backbone of visual hierarchy — if the type system is broken, nothing else matters. A clear typographic hierarchy tells users what to read first, second, and third without thinking.

## Protocol

### Step 1: Read and Map the Type System

Read the code. Before changing anything, inventory what exists:

- **Font families**: which fonts are in use? (font-sans, font-serif, custom fonts)
- **Size scale**: what text sizes appear? (text-sm, text-base, text-lg, text-xl, text-2xl, etc.)
- **Weight range**: what weights are used? (font-normal, font-medium, font-semibold, font-bold)
- **Line heights**: explicit leading values or Tailwind defaults?
- **Color range**: how many distinct text colors? (text-gray-500, text-gray-700, text-gray-900, etc.)

Map the hierarchy: what is H1 size/weight? H2? Body? Caption? How many levels exist?

### Step 2: Check for Issues

#### Hierarchy
- **Insufficient contrast between levels**: H1 and H2 too similar in size/weight — reader can't tell which is more important. Rule of thumb: each level should be visually distinct in at least 2 properties (size + weight, or size + color)
- **Too many levels**: more than 4-5 distinct text levels creates confusion. Simplify
- **Skipped visual jumps**: text-base → text-3xl with nothing between — feels discontinuous
- **Body text competes with headings**: body is too large or too bold relative to headings

#### Sizing
- **Body text too small**: below text-sm (14px) for primary content = readability problem
- **Body text too large**: above text-lg (18px) for dense content = feels childish
- **Headings too timid**: main headings below text-2xl on desktop won't anchor the page
- **Inconsistent sizing**: same-level elements use different sizes (one card title is text-lg, another is text-xl)

#### Weight
- **Everything is bold**: when everything is bold, nothing stands out. Reserve bold for key elements
- **Everything is normal weight**: page feels flat and monotone. Add weight contrast
- **Wrong weight for size**: large text (3xl+) usually looks better at font-semibold or lower. Small text needs font-medium minimum for readability

#### Line Height & Spacing
- **Line height too tight**: body text with leading-tight or leading-none — hard to read in paragraphs
- **Line height too loose**: headings with leading-relaxed — looks floaty and disconnected
- **No margin between text blocks**: paragraphs run together. Add mb-4 or similar
- **Letter spacing issues**: large headings can benefit from tracking-tight. Small caps need tracking-wide

#### Readability
- **Line length too long**: lines exceeding 75 characters are hard to read. Use max-w-prose or max-w-2xl
- **Low contrast text**: light gray on white (text-gray-400 on white) = WCAG failure and readability problem
- **All caps overuse**: more than a label or two in ALL CAPS = hard to scan
- **Inconsistent alignment**: mixing text-left and text-center without clear pattern

### Step 3: Apply Fixes

Fix directly with Edit tool. Each fix is surgical — one typographic property at a time.

**Key principles:**
- **Size × weight × color = hierarchy**: change at least 2 of these between levels
- **Heading closer to its content**: less margin above the paragraph that follows a heading, more margin above the heading itself (space above > space below)
- **Body text is king**: optimize body readability first (16-18px, leading-relaxed, max-w-prose), then fit headings around it
- **Fewer fonts, more contrast**: one font family with varying size/weight beats three font families

### Step 4: Report

```markdown
## Typeset Report: [Section Name]

**Fixes applied: N**

| # | Category | What | Before | After |
|---|---|---|---|---|
| 1 | Hierarchy | H1/H2 too similar | text-2xl/text-xl | text-4xl font-bold / text-2xl font-semibold |
| 2 | Readability | Line length unlimited | no max-width | max-w-prose on body text |
| 3 | Weight | All headings same weight | font-bold everywhere | H1 bold, H2 semibold, H3 medium |
| 4 | Spacing | Paragraphs run together | no margin | space-y-4 on text container |

**Type scale used: [e.g., sm/base/lg/xl/2xl/4xl]**
```

## Scope Boundaries

- Fix font size, weight, line-height, letter-spacing, text color contrast, line length, text alignment
- Don't change layout structure — that's `arrange`
- Don't change non-text colors or backgrounds — that's `colorize`
- Don't rewrite content — just fix how it's displayed
- If you find a spacing/layout issue while fixing type, note it: "Layout issue found — consider `arrange`"
