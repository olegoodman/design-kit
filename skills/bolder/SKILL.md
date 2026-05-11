---
name: bolder
description: >
  Amplify safe, bland, or generic designs. Increases visual impact while maintaining
  usability. Pushes designs from "competent but forgettable" to "distinctive and memorable".
  Use when the design-orchestrator routes to bolder, when critique gives low
  Screenshot-Worthiness scores, or when user says "too bland", "too safe", "generic",
  "boring", "lacks personality", "looks like a template", "needs more punch", or "not
  memorable". Do NOT use for: toning down (use quieter), layout fixes (use arrange),
  adding color to gray designs (use colorize), or full creative direction (use
  creative-director).
---

# Bolder — Amplify Impact

Push designs past "safe" into "distinctive." The most common AI output problem: everything looks competent but identical. Same Inter font, same gray palette, same rounded-lg cards, same gradient hero. Bolder breaks that pattern — intentionally, not randomly.

The line between bold and chaos is intent. Every bold choice must be traceable to a reason: "this is bold because it draws the eye to the CTA" or "this contrast creates memorability." Bold without reason = noise.

## Protocol

### Step 1: Read and Identify "Template Syndrome"

Read the code. Look for signs of generic design:

- **Safe fonts**: Inter, Roboto, system-ui with no character
- **Safe colors**: gray/blue palette with no accent personality
- **Safe layout**: predictable grid, centered text, rounded-lg everything
- **Safe spacing**: comfortable but unremarkable — nothing tight, nothing generous
- **Safe imagery**: stock-photo vibes, no distinctive visual language
- **Same components**: every card/section looks structurally identical

Rate: how many of these apply? 4+ = strong candidate for bolder.

### Step 2: Choose Bold Moves

Pick 2-3 bold moves maximum. The key: concentrated impact, not scattered changes. Bold everything = bold nothing.

**Bold move palette:**

| Move | What it does | When to use |
|---|---|---|
| **Scale contrast** | Make one element dramatically larger/smaller than its neighbors | Hero heading, key metric, featured testimonial |
| **Weight contrast** | Pair ultra-light with ultra-bold in the same section | Headlines vs body, creating visual tension |
| **Color punch** | One saturated color against muted surroundings | CTA, key badge, accent stripe |
| **Negative space** | Dramatically more whitespace than expected | Premium feel, focusing attention on one thing |
| **Typography personality** | Distinctive font choice (display, serif, mono) for headings | Brand differentiation, hero sections |
| **Asymmetry** | Break grid symmetry intentionally | Creative sections, portfolio, about pages |
| **Oversized element** | One element breaks expected proportions | Hero image, testimonial quote, feature icon |
| **Texture/pattern** | Subtle background texture, grid, dots, gradient mesh | Sections that feel flat and empty |
| **Dark section** | Invert one section to dark bg + light text | Breaking visual rhythm, emphasis |

### Step 3: Apply Bold Moves

Fix directly with Edit tool. Each move is a deliberate choice.

**Key principles:**
- **Bold one thing per section**: if the heading is bold, keep the body calm. If the layout is asymmetric, keep the colors simple
- **Boldness cascades**: a bold hero sets the tone — subsequent sections can be calmer and still feel designed
- **Don't sacrifice usability**: text must remain readable, CTAs must remain findable, navigation must work
- **Before → after contrast**: the change should be immediately noticeable. If you have to squint to see the difference, it's not bold enough
- **Test the "screenshot test"**: would someone screenshot this and share it? If not, push further

**Example transformations:**

```
Bland hero → bold hero:
  Before: text-3xl font-semibold text-gray-900 + text-lg text-gray-600 + centered
  After:  text-6xl font-black tracking-tight text-gray-900 + text-xl text-gray-500 font-light + left-aligned with asymmetric image

Generic cards → distinctive:
  Before: rounded-lg shadow-sm p-6 (every card identical)
  After:  featured card: col-span-2 + accent border-l-4 border-blue-500 + larger text. Rest: minimal, no shadow

Flat section → bold section:
  Before: bg-white py-16 (same as all other sections)
  After:  bg-gray-950 text-white py-24 (dark section breaks rhythm)
```

### Step 4: Report

```markdown
## Bolder Report: [Section Name]

**Bold moves applied: N**
**Approach: [e.g., "scale contrast + dark section inversion"]**

| # | Move | Element | Before | After | Why |
|---|---|---|---|---|---|
| 1 | Scale contrast | Hero heading | text-3xl | text-6xl font-black tracking-tight | Anchors the page, unmissable |
| 2 | Dark section | Testimonials | bg-white | bg-gray-950 text-white | Breaks visual rhythm, creates emphasis |
| 3 | Color punch | CTA | bg-blue-500 | bg-amber-500 ring-4 ring-amber-200 | Stands out from blue palette |

**Screenshot test: [pass/fail — would someone share this?]**
**Usability preserved: [yes — text readable, CTA visible, navigation works]**
```

## Scope Boundaries

- Amplify visual impact through scale, weight, color, space, typography, contrast
- Maximum 2-3 bold moves per section — concentrated, not scattered
- Don't compromise readability or usability for boldness
- Don't tone down — that's `quieter`
- Don't add layout structure — that's `arrange`
- Don't add animations — that's `animate`
- If the design needs a complete creative rethink, suggest `creative-director`
