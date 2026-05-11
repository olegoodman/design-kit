---
name: design-orchestrator
description: >
  Mandatory router for ALL visual and design tasks across web projects.
  Use when task involves: appearance, styling, layout, color, typography,
  animation, responsive design, UX copy, component creation, asset generation,
  brand work, or design review. Also triggers on Russian keywords: дизайн, стиль,
  вид, красив, лейаут, шрифт, цвет, анимация, адаптив, секция, компонент.
  Do NOT use for: pure logic, TypeScript fixes, content-only edits,
  build/deploy, infrastructure, API calls, or routing changes.
---

# Design Orchestrator

Route visual tasks to the correct design skill(s). Never write code — only classify, route, and invoke.

## Process

### 1. Classify

Determine the task type:

| Type | Signal |
|---|---|
| `NEW_SECTION` | Building a section, page, or component from scratch |
| `IMPROVE` | Making existing design better |
| `POINT_FIX` | Specific aspect: typography, color, spacing, animation |
| `REVIEW` | Evaluating or auditing current design |
| `ASSET` | Generating an image, banner, card, presentation |
| `BRAND` | Design system, logo, CIP, tokens |
| `COMPONENT` | Systematic UI component (form, table, dialog) |

### 2. Route

Load `[[references/routing-table.md]]` and find the matching route.

### 3. Pre-flight

Before invoking Tier 2/3 skills:

1. **`.impeccable.md` exists?** If no and project needs one → invoke `teach-impeccable` first
2. **Brand context loaded?** If `brand` skill available, run `inject-brand-context.cjs` for palette, fonts, tokens. Otherwise read project's design tokens manually
3. **Clean base?** For NEW_SECTION, verify starting from correct branch state (not rejected work)

### 4. Output

```
TASK: [rephrased request, 1 line]
TYPE: [classification]
ROUTE:
  1. invoke [skill] — [why]
  2. invoke [skill] — [why]
  3. invoke [skill] — [why]
```

Then immediately invoke the first skill in the route using the **Skill tool**. Skills with SKILL.md files (critique, audit, polish, frontend-design, ui-styling, etc.) must be invoked via the Skill tool to load their full methodology. For Tier 3 skills that don't yet have SKILL.md files, follow the description from the skill catalog.

## Key Rules

- **Never write CSS/Tailwind/HTML.** Only route to skills that do.
- **Ambiguous "make better" requests** → start with `critique` to diagnose UX issues.
- **"Make it memorable/unique/distinctive"** → start with `creative-director` Phase 4 to evaluate creative quality. This is a creative problem, not a UX problem.
- **Creative brief for new section** (campaign, landing page, brand hero) → `creative-director` first for concept, then build.
- **NEW_SECTION** → always end route with `polish` as final pass.
- **Multiple aspects** → chain skills (e.g., `typeset` then `colorize` then `polish`).

## Skill Tiers (summary)

**Tier 1 — Strategy:** `ui-ux-pro-max`, `creative-director`, `critique`, `audit`
**Tier 2 — Implementation:** `frontend-design`, `ui-styling`, `brand`, `design`, `design-system`, `teach-impeccable`
**Tier 3 — Refinement:** `polish`, `typeset`, `arrange`, `colorize`, `bolder`, `quieter`, `animate`, `optimize`, `adapt`, `clarify`, `distill`, `delight`, `harden`, `extract`, `normalize`, `onboard`, `overdrive`
**Tier 4 — Assets:** `gpt-image-2` (default for text/logo/branded), `nano-banana` (default for free-form/artistic), `product-card-image`, `banner-design`, `slides`

Full catalog with descriptions: `[[references/skill-catalog.md]]`

## Adding a New Skill

1. Add entry to `references/skill-catalog.md` in the right tier
2. Add routing row to `references/routing-table.md`
3. Done — no structural changes needed
