---
name: normalize
description: >
  Fix design inconsistencies across sections — mismatched styles, drifted tokens, uneven
  treatment of same-type elements. Use when the design-orchestrator routes to normalize,
  or when user says "inconsistent", "sections look different", "style drift", "doesn't
  match", "uneven design", or "normalize styles". Do NOT use for: building design tokens
  from scratch (use design-system), brand guidelines (use brand), or point fixes in one
  section (use specific Tier 3 skill).
---

# Normalize — Cross-Section Consistency

Fix the design drift that happens when sections are built at different times or by different prompts. Each section may look fine alone, but side by side: different heading sizes, different card styles, different spacing.

## Protocol

### Step 1: Cross-Section Audit

Read multiple sections/pages. Map the patterns:
- **Heading sizes**: does every section use the same h2 size? Same h3?
- **Card styles**: same border-radius? Same shadow? Same padding?
- **Spacing between sections**: consistent py-? between all sections?
- **Color usage**: same gray for body text everywhere? Same accent color?
- **Button styles**: all primary buttons same size/color/radius?
- **Icon sizes**: all section icons same dimensions?

### Step 2: Establish the "Correct" Pattern

For each inconsistency, pick the best existing version as the standard:
- The version used most frequently wins (convention)
- If tied, the version that matches design tokens/brand wins
- If no tokens, the version that looks most intentional wins

### Step 3: Normalize to the Standard

Fix directly with Edit tool. Each fix aligns one element to the standard.

### Step 4: Report

```markdown
## Normalize Report

**Inconsistencies fixed: N**

| # | Pattern | Variants found | Normalized to | Sections affected |
|---|---|---|---|---|
| 1 | Section heading size | text-2xl / text-3xl / text-xl | text-3xl font-bold | Hero, Features, About |
| 2 | Card border-radius | rounded-md / rounded-lg / rounded-xl | rounded-xl | Products, Team, Blog |
| 3 | Section padding | py-12 / py-16 / py-20 | py-16 | All sections |
```
