---
name: arrange
description: >
  Fix layout, spacing, and visual rhythm in UI sections. Addresses grid issues, inconsistent
  gaps, misalignment, crowded or sparse areas, and monotonous layouts. Use when the
  design-orchestrator routes to arrange, when critique identifies Spacing & Rhythm issues,
  or when user says "fix spacing", "layout feels off", "too crowded", "alignment is wrong",
  "grid is boring", or "spacing inconsistent". Do NOT use for: typography (use typeset),
  color changes (use colorize), responsive breakpoints (use adapt), or full redesign
  (use critique first).
---

# Arrange — Layout & Spacing

Fix spatial relationships between elements. You're adjusting the furniture in the room — not repainting walls or replacing furniture.

## Protocol

### Step 1: Read and Map the Spacing System

Read the component/section code. Before touching anything, identify the existing spacing system:

- **Tailwind scale in use**: which gap/padding/margin values appear? (gap-4, gap-6, gap-8, py-12, etc.)
- **Spacing rhythm**: is there a consistent base unit? (e.g., multiples of 4: 4/8/12/16/20/24)
- **Section pattern**: how are sibling sections spaced? (py-16 each? py-20?)

You conform to this system. If the project uses gap-4/gap-8/gap-16, don't introduce gap-6. Stay on the existing scale.

### Step 2: Check for Issues

Run through these categories. Note every issue found.

#### Grid & Layout Structure
- **Monotonous grid**: all sections use the same grid (e.g., everything is 3-col). Vary grid patterns between sections for rhythm
- **Grid gaps don't match content density**: sparse content with tight grid = awkward whitespace. Dense content with wide grid = cramped
- **Flex/grid misuse**: items that should align don't (missing items-center, justify-between, etc.)
- **Container width inconsistent**: content width varies between sections without reason

#### Spacing Consistency
- **Nearby values**: gap-4 next to gap-5, or py-8 next to py-10 — pick one, they're too close to be intentionally different
- **Unbalanced padding**: section has py-16 top but py-8 bottom (unless there's a design reason)
- **Inconsistent component spacing**: same-type cards have different internal padding
- **Missing spacing scale**: arbitrary values (mt-[13px], gap-[22px]) instead of scale values

#### Visual Rhythm
- **Wall of sameness**: every section looks structurally identical — same padding, same grid, same height
- **No breathing room**: elements packed tight with no whitespace to rest the eye
- **Orphaned elements**: a single element floating with too much space around it
- **Content gravity**: heavy content clusters at top, empty space at bottom (or vice versa)

#### Alignment
- **Left-edge drift**: text blocks don't align to a consistent left edge
- **Center vs left mixing**: some elements centered, others left-aligned, without clear intent
- **Vertical alignment in rows**: items in a flex row not aligned (text baseline, icon center, etc.)
- **Grid cell alignment**: content inside grid cells aligned differently across cells

### Step 3: Apply Fixes

Fix issues directly with Edit tool. Each fix should be minimal and targeted.

**Key principles:**
- **Spacing creates hierarchy**: more space above a heading than below it (heading belongs to following content, not preceding)
- **Proximity = relationship**: elements that belong together should be closer than elements that don't
- **Consistent scale beats "looks right"**: if the scale is 4/8/12/16, use it even if 14 "looks right" — consistency matters more
- **White space is a design element**: don't fill every gap. Breathing room makes content scannable

### Step 4: Report

```markdown
## Arrange Report: [Section Name]

**Fixes applied: N**

| # | Category | What | Before | After |
|---|---|---|---|---|
| 1 | Spacing | Section padding inconsistent | py-8 / py-16 | py-12 (unified) |
| 2 | Grid | Monotonous 3-col everywhere | grid-cols-3 all | 2-col intro + 3-col features |
| 3 | Alignment | Cards misaligned vertically | items-start | items-stretch |
| 4 | Rhythm | No space between sections | gap-0 | gap-y-24 |

**Spacing scale used: [e.g., 4/8/12/16/20/24 (Tailwind default)]**
```

## Scope Boundaries

- Fix spacing, gaps, padding, margins, grid structure, alignment
- Don't change colors, fonts, or content — that's other skills' territory
- Don't add/remove sections or components — that's building
- If you find a typography issue while fixing layout, note it: "Typography issue found — consider `typeset`"
