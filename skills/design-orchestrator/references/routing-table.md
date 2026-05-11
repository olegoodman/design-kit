# Routing Table

## NEW_SECTION — building from scratch

### Standard (no creative brief)
| Step | Skill | Why |
|---|---|---|
| 1 | `critique` | Assess surrounding context, existing design direction |
| 2 | `frontend-design` | Build with bold, distinctive visual code |
| 3 | `polish` | Final refinement pass |

### With creative brief (campaign, landing page, brand hero)
Trigger: user provides a brief, mentions campaign, "Big Idea", brand launch, or the section needs a creative concept — not just visual execution.

| Step | Skill | Why |
|---|---|---|
| 1 | `creative-director` | Generate concept: insight → ideation → evaluate (full cycle or Phase 2-3) |
| 2 | `frontend-design` | Build the concept into visual code |
| 3 | `critique` | Evaluate UX quality of the result |
| 4 | `polish` | Final refinement pass |

## IMPROVE — making existing design better

**Vague UX** ("make it better", "something's off", no specific aspect named):

| Step | Skill | Why |
|---|---|---|
| 1 | `critique` | Diagnose what's weak with scores |
| 2 | Point skill per findings | Fix the identified weakness |
| 3 | `polish` | Final pass if significant changes |

**Vague Creative** ("make it memorable", "too generic", "needs personality", "unique", "distinctive", "stands out from competitors"):

| Step | Skill | Why |
|---|---|---|
| 1 | `creative-director` Phase 4 | Evaluate creative quality, identify gaps (originality, brand uniqueness, emotional impact) |
| 2 | Based on gap analysis | `bolder` / `delight` / `typeset` / `colorize` etc. |
| 3 | `critique` | Verify UX not broken by creative changes |
| 4 | `polish` | Final pass |

**Specific** (user names the aspect): route directly to matching POINT_FIX.

## POINT_FIX — specific aspect

| Aspect | Skill(s) | Trigger phrases |
|---|---|---|
| Typography | `typeset` | fonts, text hierarchy, readability, sizing, weight |
| Color | `colorize` | palette, monochromatic, dull, needs warmth, gray |
| Layout | `arrange` | spacing, visual rhythm, grid, crowded, alignment |
| Animation | `animate` → `optimize` | transitions, hover, scroll effects, motion, micro-interactions |
| Too bland | `bolder` | generic, safe, boring, lacks personality, flat |
| Too loud | `quieter` | aggressive, overwhelming, garish, too bold |
| Responsive | `adapt` | mobile, breakpoints, viewport, touch targets |
| Simplify | `distill` | cluttered, too many elements, reduce noise |
| UX copy | `clarify` | labels, error messages, microcopy, confusing text |
| Personality | `delight` | joy, memorable, fun, boring but functional |
| Edge cases | `harden` | i18n, error handling, resilience, production-ready |
| Components | `extract` | repeated patterns, component library, reuse |
| Consistency | `normalize` | design drift, mismatched styles, tokens |
| Onboarding | `onboard` | first-run, empty states, activation flow |
| Ambitious effects | `overdrive` | shaders, spring physics, scroll-driven, 60fps |
| Performance | `optimize` | slow, laggy, janky, bundle size, loading |

## REVIEW — evaluate current state

### Quick review (default)
| Step | Skill | Why |
|---|---|---|
| 1 | `critique` | UX evaluation with quantitative scoring |
| 2 | `audit` | Technical: a11y, performance, responsive, anti-patterns |

### Full review (user asks for comprehensive/creative evaluation)
Trigger: "full review", "comprehensive review", "is this good enough?", "ready for launch?", or any review request that implies evaluating creative quality alongside UX/technical.

| Step | Skill | Why |
|---|---|---|
| 1 | `critique` | UX quality: hierarchy, spacing, cognitive load, brand consistency |
| 2 | `creative-director` Phase 4 | Creative quality: originality, emotional impact, brand uniqueness, specificity test |
| 3 | `audit` | Technical: a11y, performance, responsive, anti-patterns |
| 4 | Synthesize | Merge findings into one prioritized action plan |

## ASSET — generate visual asset

| Asset type | Skill | Trigger phrases |
|---|---|---|
| Image with text / logo / brand | `gpt-image-2` | slide, infographic, social post with copy, branded asset, vertical/9:16, "make a poster with text" |
| Image, free-form / artistic | `nano-banana` | blog featured image, thumbnail, illustration, pattern, hero photo, mood-board |
| LEINOS product card | `product-card-image` | product card, packshot, product photo |
| Banner | `banner-design` | social banner, ad creative, cover image (routes internally to gpt-image-2 or nano-banana) |
| Presentation (premium) | `design-system` | pitch deck, investor deck, strategic presentation, data-heavy slides |
| Presentation (quick) | `slides` | simple slides, quick presentation, lightweight deck |

## BRAND — identity and design system

| Aspect | Skill | Trigger phrases |
|---|---|---|
| Style direction | `ui-ux-pro-max` | palette, font pairing, style direction, design system choice |
| Brand voice & guidelines | `brand` | brand voice, tone of voice, messaging, brand guidelines, style guide, brand consistency, brand audit |
| Asset validation | `brand` | validate asset, check brand compliance, color check, asset naming |
| Brand assets | `design` | logo, CIP, brand identity, icons, brand creation |
| Design tokens | `design-system` | design tokens, CSS variables, token architecture, primitive/semantic/component tokens, hardcoded values |
| Token validation | `design-system` | validate tokens, find hardcoded, token compliance |

**Full brand setup** (new project): invoke `brand-setup` — it orchestrates the entire init chain.
**Full brand setup chain** (manual):
`ui-ux-pro-max` → `brand` → `design` → `design-system` → `ui-styling`

**Brand sync flow** (update existing):
`brand` (edit guidelines) → `design-system` (regenerate tokens) → verify

## COMPONENT — systematic UI

| Type | Skill | Trigger phrases |
|---|---|---|
| Any shadcn/ui component | `ui-styling` | form, table, dialog, dropdown, component, accessible |
