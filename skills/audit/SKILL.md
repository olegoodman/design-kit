---
name: audit
description: >
  Technical quality audit for web UI: accessibility (WCAG 2.2 AA), performance (Core Web
  Vitals), responsive design, code quality, and anti-patterns. Produces a scored report with
  P0-P3 severity findings. Use when the design-orchestrator routes to audit, for pre-launch
  quality gates, accessibility compliance checks, performance reviews, or technical design
  reviews. Pairs with critique (UX evaluation) for comprehensive review — critique assesses
  visual/UX quality, audit checks technical correctness. Also use when the user mentions
  accessibility, WCAG, a11y, performance, responsive, or "is this production-ready".
  Do NOT use for: SEO site audits (use seo-audit), visual/UX quality (use critique),
  full website crawls, or content quality (use seo-content). This audits UI component CODE.
---

# Audit — Technical Design Quality

Check the technical quality of UI code across five categories. You are a code reviewer with a checklist — methodical, thorough, evidence-based. Every finding must reference a specific line number or code pattern. No vague "could be improved" — point to the exact problem.

## Protocol

### Step 1: Read the Code

Read the component/section/page code thoroughly. Identify:
- **Tech stack**: React/Vue/Svelte/plain HTML, Tailwind/CSS modules/styled-components
- **Framework patterns**: SSR/CSR, component library in use (shadcn, Radix, etc.)
- **Design system**: tokens, CSS custom properties, Tailwind config

This context calibrates your checks — a Tailwind project has different anti-patterns than a CSS modules project.

### Step 2: Run Five Category Checks

For each item: PASS, FAIL, or N/A (with reason). Every FAIL must cite a specific line or pattern.

#### Category A: Accessibility (WCAG 2.2 AA)

| # | Check | What to look for |
|---|---|---|
| A1 | Color contrast | Text ≥ 4.5:1 (normal), ≥ 3:1 (large/bold). Check Tailwind text/bg class pairs |
| A2 | Image alt text | All `<img>` have meaningful alt. Decorative images: `alt=""` + `aria-hidden="true"` |
| A3 | Heading hierarchy | h1 → h2 → h3 sequential, no skipped levels within a section |
| A4 | Form labels | Every input has `<label>`, `aria-label`, or `aria-labelledby` |
| A5 | Keyboard navigation | Interactive elements reachable via Tab. No keyboard traps |
| A6 | Focus indicators | `focus-visible` styles present. Not removed via `outline-none` without replacement |
| A7 | ARIA correctness | Roles/attributes used correctly, not redundant with semantic HTML |
| A8 | Motion sensitivity | `prefers-reduced-motion` media query respected for animations |
| A9 | Touch targets | Clickable areas ≥ 44x44px on mobile (check padding on links/buttons) |
| A10 | Semantic HTML | Uses `<nav>`, `<main>`, `<article>`, `<section>` — not `<div>` soup |

#### Category B: Performance

| # | Check | What to look for |
|---|---|---|
| B1 | Image optimization | Next-gen formats (webp/avif), proper sizing, `srcset` for responsive |
| B2 | Lazy loading | Below-fold images/iframes use `loading="lazy"` |
| B3 | Layout shifts (CLS) | Fixed dimensions on images/embeds/cards to prevent reflow |
| B4 | Bundle impact | No heavy imports (full lodash, moment.js). Check for tree-shakeable alternatives |
| B5 | CSS efficiency | No redundant Tailwind, no inline styles where classes work |
| B6 | Font loading | `font-display: swap` or `optional`. Subset fonts if possible |
| B7 | Animation performance | Animations use `transform`/`opacity` (GPU-composited), not `width`/`height`/`top` |

#### Category C: Responsive Design

| # | Check | What to look for |
|---|---|---|
| C1 | Mobile-first | Base styles are mobile, breakpoints scale up (sm → md → lg → xl) |
| C2 | Breakpoint coverage | Layout works at 320px, 375px, 768px, 1024px, 1440px |
| C3 | Text overflow | Long text truncated (`truncate`/`line-clamp`) or wrapped, no layout break |
| C4 | Touch vs hover | Hover-only interactions have touch/click alternatives |
| C5 | Viewport meta | `<meta name="viewport" content="width=device-width, initial-scale=1">` present |

#### Category D: Code Quality

| # | Check | What to look for |
|---|---|---|
| D1 | Component size | Single responsibility, <200 lines per component |
| D2 | Type safety | TypeScript props typed, no `any` for visual/layout props |
| D3 | Key props | List renders use stable keys (not array index for dynamic/reorderable lists) |
| D4 | State handling | Loading, error, and empty states handled (no bare `data?.map()`) |
| D5 | Design tokens | Spacing/colors use scale or tokens, no magic numbers (`mt-[13px]`) |
| D6 | Dark mode | If theme support exists in the project, dark: variants are present and correct |

#### Category E: Anti-Patterns

| # | Check | What to look for |
|---|---|---|
| E1 | Z-index escalation | Values reasonable and systematic, no `z-[9999]` or `z-50` without context |
| E2 | !important abuse | Zero `!important` unless overriding third-party library styles |
| E3 | Nested complexity | No deeply nested ternaries in className; extract to variables/functions |
| E4 | Mixed units | Consistent use of rem/Tailwind scale; no mixing px/rem/em/arbitrary values |
| E5 | Dead code | No commented-out code, unused props, orphaned styles |

### Step 3: Assign Severity

| Severity | Meaning | Examples |
|---|---|---|
| **P0 — Blocker** | Breaks functionality or access, legal risk | No keyboard access to main CTA, missing form labels (a11y lawsuit risk) |
| **P1 — Major** | Significant UX degradation, fails standard | Low contrast body text, horizontal scroll on mobile, no loading states |
| **P2 — Minor** | Noticeable but not blocking | Inconsistent border-radius, minor CLS on images, missing dark mode on one section |
| **P3 — Polish** | Code quality, nice-to-have | Commented-out code, slightly redundant Tailwind classes, minor type issues |

### Step 4: Calculate Health Score

```
Raw score = PASS count / (PASS + FAIL count)
```

Category weighting (accessibility and performance matter most for real users):
- Category A (Accessibility): weight 2.0
- Category B (Performance): weight 1.5
- Category C (Responsive): weight 1.5
- Category D (Code Quality): weight 1.0
- Category E (Anti-Patterns): weight 1.0

```
Health Score = weighted average of category scores × 100
```

| Score | Rating | Recommendation |
|---|---|---|
| 90-100% | Excellent | Ship it |
| 75-89% | Good | Fix P0/P1, then ship |
| 60-74% | Needs Work | Fix P0/P1/P2 before shipping |
| <60% | Poor | Significant rework needed |

### Step 5: Output Report

```markdown
# Technical Audit: [Section/Component Name]

**Health Score: XX% — [Rating]**
**Stack:** [React/Vue/etc] + [Tailwind/CSS/etc]
**Findings:** N total (P0: X, P1: X, P2: X, P3: X)

## Critical Findings (P0)

- **[A5] Keyboard navigation** (line 82): `<div onClick={...}>` without `role="button"` or `tabIndex`. Not reachable via keyboard.
  **Fix:** Replace with `<button>` or add `role="button" tabIndex={0} onKeyDown={handleEnter}`.

## Major Findings (P1)

[same format...]

## Minor Findings (P2)

[same format...]

## Polish (P3)

[same format...]

## Category Summary

| Category | Checks | Pass | Fail | N/A | Score |
|---|---|---|---|---|---|
| A: Accessibility | 10 | X | X | X | XX% |
| B: Performance | 7 | X | X | X | XX% |
| C: Responsive | 5 | X | X | X | XX% |
| D: Code Quality | 6 | X | X | X | XX% |
| E: Anti-Patterns | 5 | X | X | X | XX% |
| **Total** | **33** | **X** | **X** | **X** | **XX%** |

## Quick Wins

Top 3 highest-impact, lowest-effort fixes:
1. [fix description] — [effort: ~2 min]
2. [fix description] — [effort: ~5 min]
3. [fix description] — [effort: ~5 min]
```

## Scope Boundaries

- **Not for visual/UX quality** — that's `critique` (hierarchy, cognitive load, brand feel)
- **Not for creative evaluation** — that's `creative-director` (originality, insight)
- **Not for fixing** — audit diagnoses technical issues; the developer (or a fix skill) resolves them
- **If a section has both UX and technical issues**, run `critique` first (fixes UX direction), then `audit` (fixes technical execution)
