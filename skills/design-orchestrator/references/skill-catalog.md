# Design Skill Catalog

## Tier 1 — Strategy (WHAT to do)

### ui-ux-pro-max
**Purpose:** Full design intelligence — 50+ styles, 161 color palettes, 57 font pairings, 99 UX guidelines, 25 chart types across 10 tech stacks.
**When:** Choosing style direction, palette, font pairing, component patterns, UX review, design system decisions.
**Size:** 45KB (heavy — loads full design knowledge base)

### creative-director
**Purpose:** Campaign-level creative concepts using SIT, TRIZ, Lateral Thinking, bisociation methodologies. Recursive self-assessment with Cannes/D&AD calibration.
**When:** Big Idea generation, campaign concepts, brand positioning. NOT for UI implementation.
**Size:** 15KB

### critique
**Purpose:** UX evaluation with quantitative scoring, 3-persona panel (UX Designer, PM, End User), 6-dimension scoring (Visual Hierarchy, Spacing, Cognitive Load, Brand Consistency, Accessibility, Screenshot-Worthiness), structured verdict with issue-to-skill mapping.
**When:** Assess current design quality before improving. Diagnose "what's wrong" for vague requests. Pre-improvement analysis.
**Invoke via:** `Skill tool` — has full SKILL.md with rubrics, calibration anchors, anti-inflation rules.
**Pairs with:** Any Tier 2/3 skill (critique first, then fix). Each issue maps to a specific fix skill.
**Output:** `VERDICT: NEEDS_REVISION | APPROVED` + `ISSUES[]` with severity (P0-P3) and `FIX_SKILL` per issue.

### audit
**Purpose:** Technical quality audit — accessibility (WCAG 2.2 AA, 10 checks), performance (CWV, 7 checks), responsive (5 checks), code quality (6 checks), anti-patterns (5 checks). Health score with P0-P3 severity findings.
**When:** Pre-launch quality gate, accessibility compliance, performance check, "is this production-ready?".
**Invoke via:** `Skill tool` — has full SKILL.md with 33 concrete checks, severity matrix, weighted health score.
**Pairs with:** `critique` (UX + technical = full review). Run critique first (design direction), audit second (technical execution).

---

## Tier 2 — Implementation (HOW to do it)

### frontend-design
**Purpose:** Creative, distinctive visual code. Bold aesthetics, "wow factor". Avoids generic AI/SaaS look. Prioritizes memorable design over systematic consistency.
**When:** Building visually striking sections, creative one-offs, landing page heroes, visual experiments.
**Size:** 4.5KB
**Key rule:** Choose extreme aesthetic direction and execute with precision. Never default to Inter/Roboto/purple gradients.

### ui-styling
**Purpose:** Systematic shadcn/ui + Tailwind components. Accessible, composable, TypeScript-first.
**When:** Forms, tables, dialogs, navigation, data displays — any component that needs accessibility and design system consistency.
**Size:** 10KB

### brand-setup
**Purpose:** One-time project initialization — scans existing design data, creates brand-guidelines.md and design-tokens.json/.css from real project values, verifies the pipeline.
**When:** New project needs brand + tokens, or project has design data but missing guideline/token files.
**Run once per project.** After setup, use `brand` and `design-system` directly.

### brand
**Purpose:** Brand voice, visual identity, messaging frameworks, asset management, brand consistency. Scripts for injecting brand context into prompts, syncing guidelines to design tokens, validating assets, extracting/comparing colors against palette.
**When:** Brand voice definition, style guide development, messaging framework, brand consistency review/audit, asset validation (naming, size, format), color palette management, typography specs.
**Pairs with:** `design` (brand manages guidelines → design creates assets), `design-system` (brand syncs guidelines → tokens)
**Key script:** `inject-brand-context.cjs` — extracts brand context for other skills to consume.

### design
**Purpose:** Unified brand asset skill — logo generation (55 styles), CIP (50 deliverables), design tokens, banners (22 styles), icons (15 styles), social photos.
**When:** Brand identity work, logo creation, corporate identity program, design token setup.
**Size:** 12KB
**Sub-routing:** Routes internally to logo/CIP/banner/icon sub-skills.
**Pairs with:** `brand` (brand defines guidelines → design creates matching assets)

### design-system
**Purpose:** Three-layer token architecture (primitive → semantic → component), CSS variable systems, component state specs, Tailwind integration. Advanced slide generation with BM25 search, 8 decision CSVs, contextual strategies, Chart.js, pattern breaking (Duarte Sparkline).
**When:** Design token creation/validation, component state definitions, spacing/typography scales, design-to-code handoff, Tailwind theme config, brand-compliant premium presentations.
**Pairs with:** `brand` (extracts primitives from brand colors/typography), `ui-styling` (component tokens → Tailwind config)
**Key scripts:** `generate-tokens.cjs` (JSON → CSS), `validate-tokens.cjs` (find hardcoded values), `search-slides.py` (BM25 contextual slide search)
**Note:** For presentations, `design-system` is the premium engine; `slides` is the lightweight fallback.

### teach-impeccable
**Purpose:** One-time setup — creates `.impeccable.md` with project's design context (colors, fonts, brand, style direction).
**When:** First time using any Impeccable skill in a project. Must exist before Tier 3 skills can work effectively.
**Run once per project.**

---

## Tier 3 — Refinement (SHARPEN specific aspect)

### polish
**Purpose:** Final refinement pass — alignment, spacing consistency, hover/focus/active/disabled states, transitions, overflow, border-radius, shadows. The "last 5%" before shipping. Never changes design decisions — only sharpens execution.
**When:** Last step in any multi-skill chain, before shipping, "something feels off but I can't say what", "clean it up".
**Invoke via:** `Skill tool` — has full SKILL.md with 20-item checklist, applies fixes directly via Edit tool, outputs before/after diff report.
**Key rule:** If polish finds a real design problem (not micro-detail), it notes it but doesn't fix — suggests running `critique` instead.

### typeset
**Purpose:** Typography — font hierarchy, sizing, weight, line height, letter spacing, readability, line length. Makes text hierarchy clear and intentional.
**When:** Fonts look wrong, text hierarchy unclear, sizing feels off, readability issues, headings don't stand out.
**Invoke via:** `Skill tool` — has full SKILL.md with type system mapping, hierarchy checks, sizing/weight/line-height rules, readability checks.

### arrange
**Purpose:** Layout, spacing, visual rhythm. Fixes monotonous grids, inconsistent gaps, misalignment, crowded/sparse areas.
**When:** Layout feels off, crowded, grid is boring, alignment problems, spacing inconsistencies, visual rhythm broken.
**Invoke via:** `Skill tool` — has full SKILL.md with spacing system mapping, grid/alignment/rhythm checks, before/after report.

### colorize
**Purpose:** Strategic color — palette harmony, contrast fixes, color hierarchy, accent usage, 60-30-10 rule. Fixes monotone, low-contrast, and palette clash issues.
**When:** Design looks gray, dull, lacks warmth, needs more color, too monochromatic, colors clash.
**Invoke via:** `Skill tool` — has full SKILL.md with color system mapping, palette harmony checks, contrast fixes, common fix patterns.

### bolder
**Purpose:** Amplify safe/bland designs — scale contrast, weight contrast, color punch, negative space, typography personality, asymmetry, dark sections. Max 2-3 bold moves per section.
**When:** Design is bland, generic, too safe, lacks personality, needs more visual punch, "looks like a template".
**Invoke via:** `Skill tool` — has full SKILL.md with 9 bold move types, screenshot test, concentrated impact principle.

### quieter
**Purpose:** Tone down aggressive or overstimulating designs. Reduces intensity while preserving quality.
**When:** Too bold, too loud, overwhelming, aggressive, garish, needs calming down.

### animate
**Purpose:** Purposeful animations — hover/active/focus transitions, entry animations, state changes, loading states. Transform+opacity only (GPU-composited). Always respects prefers-reduced-motion.
**When:** Adding transitions, hover effects, scroll animations, motion design, loading states, "feels static".
**Invoke via:** `Skill tool` — has full SKILL.md with timing reference table, common fix patterns, stagger rules, performance principles.
**Pairs with:** `optimize` (check performance after adding animations)

### optimize
**Purpose:** Diagnose and fix UI performance — loading speed, rendering, animations, images, bundle size.
**When:** Slow, laggy, janky, poor Core Web Vitals, heavy bundle.

### adapt
**Purpose:** Responsive design — breakpoints, mobile layout, touch targets, viewport behavior. Checks at 4 viewports (320px, 768px, 1024px, 1440px). Fixes grid collapse, padding scaling, touch targets, overflow.
**When:** Mobile layout broken, viewport issues, needs breakpoint work, touch target problems, "doesn't work on phone".
**Invoke via:** `Skill tool` — has full SKILL.md with 4-viewport protocol, mobile-first fix patterns, common responsive fixes.

### clarify
**Purpose:** UX copy — error messages, labels, microcopy, instructions. Makes interfaces easier to understand.
**When:** Confusing text, unclear labels, bad error messages, hard-to-follow instructions.

### distill
**Purpose:** Simplify by removing unnecessary complexity. Strip to essence.
**When:** Cluttered, too many elements, noisy, needs decluttering, "less is more".

### delight
**Purpose:** Add joy, personality, memorable touches. Elevates functional to delightful.
**When:** Functional but boring, needs personality, wants to be memorable and enjoyable.

### harden
**Purpose:** Edge case resilience — loading states, error states, empty states, long content handling, null/undefined guards, single-item layouts, i18n. Checklist covers loading/error/empty/content-extremes/special-chars.
**When:** Preparing for production, handling edge cases, "what if data is missing", error states, defensive UI.
**Invoke via:** `Skill tool` — has full SKILL.md with happy-path analysis, edge case checklist by category, common fix patterns.

### extract
**Purpose:** Extract reusable components, design tokens, patterns into design system.
**When:** Repeated UI patterns, component library work, design system enrichment.

### normalize
**Purpose:** Realign to design system standards, spacing, tokens, patterns.
**When:** Design drift, mismatched styles, inconsistent tokens, feature drifted from system.

### onboard
**Purpose:** Onboarding flows, empty states, first-run experiences. Help users reach value quickly.
**When:** New user experience, empty state design, activation flow, getting-started screens.

### overdrive
**Purpose:** Technically ambitious — shaders, spring physics, scroll-driven reveals, 60fps animations.
**When:** Want to wow/impress, go all-out, something extraordinary. High technical ambition.
**Warning:** Heavy — use only when the "wow" justifies the complexity.

---

## Tier 4 — Asset Generation

### gpt-image-2 ⭐ (default for branded / text-heavy / structured images)
**Purpose:** OpenAI GPT Image 2 — production-grade image model. **99% text-in-image accuracy**, all 8 aspect ratios (incl. 9:16 mobile-first), edit-mode preserves real logos/products across many images.
**When to prefer over nano-banana:**
- Rendered text inside the image (slides, banners, infographics, social posts with copy)
- Brand logo / real product / specific face must stay intact (use `edit.py --refs`)
- Vertical/landscape format flexibility (Stories, Reels, posters)
- Dense layouts, multilingual visuals (Hindi/CJK rendered legibly)
- Marketing assets where precision matters
**Cost:** Higher per image than Gemini. Use deliberately, not for throwaway generations.
**Setup:** OpenAI key in `config.yaml` (template: `config.yaml.example`).

### nano-banana (default for free-form / artistic / cheap generations)
**Purpose:** Image generation via Google Gemini. Cheap, fast, good for free-form aesthetic work.
**When to prefer over gpt-image-2:**
- Blog featured images, YouTube thumbnails (no critical in-image text)
- Illustrations, patterns, decorative artwork, hero photos
- Throwaway/experimental generations, mood-board exploration
- High volume where cost matters
- Tasks where text in the image is decorative, not load-bearing
**Setup:** Gemini CLI (`gemini auth login`).

### Quick routing rule
- **Image has text the user reads?** → `gpt-image-2`
- **Image has a real logo / product / face that must stay accurate?** → `gpt-image-2` (with `--refs`)
- **Image is vertical (9:16) or non-standard ratio?** → `gpt-image-2`
- **Pure aesthetic / illustration / mood / blog hero?** → `nano-banana`
- **High volume / throwaway?** → `nano-banana`

### product-card-image
**Purpose:** LEINOS-specific product card composites. 3-step compositing pipeline (ImageMagick + Gemini). 4:3 aspect ratio, 800px WebP.
**When:** Creating product photos/cards for LEINOS website specifically.

### banner-design
**Purpose:** Banners for social media, ads, web, print. 22 art direction styles across all platforms.
**When:** Facebook/Instagram/LinkedIn/YouTube banners, ad creatives, cover images, web heroes.
**Engine:** Routes internally to `gpt-image-2` (if text in banner) or `nano-banana` (if purely visual).

### slides
**Purpose:** Strategic HTML presentations with Chart.js data visualization, design tokens, responsive layouts.
**When:** Pitch decks, data presentations, slide decks.
**Note:** For slides where the slide itself is a generated image (not HTML), use `gpt-image-2 build_deck.py`.
