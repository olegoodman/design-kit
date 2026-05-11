---
name: distill
description: >
  Simplify cluttered UI — reduce element count, remove noise, clarify information hierarchy.
  Use when the design-orchestrator routes to distill, or when user says "too cluttered",
  "too many elements", "simplify", "reduce noise", "overwhelming content", "information
  overload", or "less is more". Do NOT use for: visual intensity (use quieter), layout
  restructuring (use arrange), or content rewriting (edit content directly).
---

# Distill — Simplify by Subtraction

Remove elements that don't earn their place. Every pixel on screen should justify its existence. If removing something doesn't hurt comprehension or conversion — remove it.

## Protocol

### Step 1: Audit Element Count

Read the code. Count distinct visual elements per section:
- How many CTAs? (>2 per section = competing)
- How many text blocks? (>3 = wall of text risk)
- How many icons/badges/tags? (>5 = visual clutter)
- How many navigation options? (>7 = decision paralysis)

### Step 2: Apply Subtractions

| Move | When | Example |
|---|---|---|
| **Merge duplicates** | Two elements say the same thing | Heading + subheading that repeat → one strong heading |
| **Remove secondary CTAs** | Multiple buttons compete | Keep 1 primary CTA, demote or remove others |
| **Progressive disclosure** | Too much info shown at once | Collapse details into expandable sections |
| **Remove decorative elements** | Icons/dividers that add no information | Remove purely ornamental dividers between sections |
| **Simplify lists** | Long feature lists nobody reads | 8 features → top 3-4 with clear benefit |
| **Consolidate navigation** | Too many nav options | Group under fewer categories |

**Key principle:** When in doubt, hide — don't delete. Use progressive disclosure (accordion, tabs, "show more") so information is accessible but not overwhelming.

### Step 3: Report

```markdown
## Distill Report: [Section Name]

**Elements before: ~N → after: ~M (reduced N%)**

| # | What | Action | Reason |
|---|---|---|---|
| 1 | Secondary CTA | Removed | Competed with primary CTA |
| 2 | Feature list (8 items) | Reduced to 4 | Top 4 cover 80% of value proposition |
| 3 | Decorative dividers | Removed | Whitespace alone creates separation |
```
