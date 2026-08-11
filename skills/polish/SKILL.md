---
name: polish
description: >
  Final refinement pass — the "last 5%" before shipping. Fixes micro-details: alignment,
  spacing consistency, hover/focus states, transitions, overflow, border-radius, shadows.
  Does NOT change design decisions — only sharpens execution. Use when the design-orchestrator
  routes to polish as a final step, when "something feels off but I can't say what", as the
  last pass before shipping a section, or when the user says "clean it up", "tighten it",
  "make it feel finished". Polish is always the last skill in any multi-skill chain.
  Do NOT use for: redesigning (use critique + fix skills), new features, accessibility
  fixes (use audit), or creative direction changes (use creative-director).
---

# Polish — Final Refinement Pass

The last pass before shipping. Find and fix micro-imperfections that separate "good enough" from "professionally finished." You are not redesigning — you are sanding edges and tightening screws.

**Core rule: Polish never changes design decisions.** If the section uses a 3-column grid, you don't switch to 2. If the CTA is green, you don't change it to blue. You fix the 1px misalignment, the inconsistent padding, the missing hover state.

Think of it like this: the architect chose the layout, the designer chose the colors, the builder put up the walls. You're the finisher — you make sure every joint is flush, every surface is smooth, every detail is intentional.

## Protocol

### Step 1: Read the Code

Read the component/section code. Identify the design system in use:
- What spacing scale? (Tailwind: 4/6/8/12/16, or custom tokens)
- What border-radius pattern? (rounded-lg everywhere, or mixed?)
- What transition pattern? (duration-200 ease, or varied?)
- What shadow levels? (shadow-sm for cards, shadow-lg for modals?)

You conform to the existing system. Don't impose your own preferences.

### Step 2: Run the Checklist

Check every item. Fix issues directly with the Edit tool — no need to ask permission for micro-fixes. These are execution details, not design choices.

#### Spacing & Alignment

- [ ] **Consistent spacing scale** — gaps use the project's scale (e.g., gap-4, gap-6, gap-8 — not gap-4, gap-5, gap-7 mixing nearby values)
- [ ] **Section padding** — top/bottom padding matches across same-level sections
- [ ] **Content alignment** — elements align to a clear grid or content width
- [ ] **Left-right symmetry** — matching horizontal padding unless intentionally asymmetric
- [ ] **Vertical rhythm** — consistent margin-bottom on text blocks, headings lead their content

#### Interactive States

- [ ] **Hover feedback** — every clickable element has visible hover change (opacity, color, shadow, underline)
- [ ] **Focus-visible rings** — interactive elements show focus indicator, not suppressed without replacement
- [ ] **Active/pressed states** — buttons show feedback on press (slight scale, color shift, shadow change)
- [ ] **Disabled styling** — disabled elements: reduced opacity (0.5-0.6), `cursor-not-allowed`, no hover effect
- [ ] **Smooth transitions** — all state changes have `transition` (150-300ms, `ease` or `ease-out`). No jarring snaps

#### Visual Consistency

- [ ] **Border-radius match** — same-type elements use same radius (all cards = rounded-xl, all buttons = rounded-lg)
- [ ] **Shadow hierarchy** — shadow levels reflect z-order (flat < card < dropdown < modal)
- [ ] **Icon sizing** — icons consistent within same context (all nav icons = 20px, all feature icons = 24px)
- [ ] **Image handling** — `object-fit` set, no stretched images, aspect ratios maintained
- [ ] **Color consistency** — same semantic color used for same purpose (all primary buttons same shade)

#### Edge Case Resilience

- [ ] **Overflow handling** — no horizontal scrollbar, long text truncated or wrapped (test with long strings)
- [ ] **Empty states** — graceful display when data is empty (not just blank void)
- [ ] **Single-item layout** — grid/flex works with 1 item, not only the expected count
- [ ] **Long content** — titles, names, descriptions that exceed expected length don't break layout

### Step 3: Apply Fixes

Make changes directly with the Edit tool. Keep each change minimal and surgical:
- One spacing fix = one edit
- Adding a hover state = one edit
- Fixing a border-radius = one edit

Don't refactor or restructure. Don't combine unrelated fixes into one edit.

### Step 4: Report

After all fixes, output a brief summary:

```markdown
## Polish Report: [Section Name]

**Fixes applied: N**

| # | Category | What | Before | After |
|---|---|---|---|---|
| 1 | Spacing | Section padding inconsistent | py-8 / py-12 | py-10 (unified) |
| 2 | States | Card missing hover | — | hover:shadow-md transition-shadow |
| 3 | States | Button no focus ring | outline-none | focus-visible:ring-2 ring-primary |
| 4 | Visual | Border-radius mixed | rounded-md / rounded-lg | rounded-lg (unified) |
| 5 | Edge | Text overflow on title | no handling | truncate on mobile |

**No design decisions were changed.**
```

If you found issues beyond polish scope, note them at the bottom:

```markdown
### Beyond Polish Scope
- Visual hierarchy issue: CTA competes with secondary buttons. Consider `critique` for diagnosis.
- Missing loading skeleton for async section. Consider `harden` for edge cases.
```

## Important Boundaries

**Polish does:**
- Fix spacing inconsistencies within the existing scale
- Add missing hover/focus/active states
- Unify border-radius, shadows, transitions
- Handle text overflow and edge cases
- Ensure smooth transitions on state changes

**Polish does NOT:**
- Change colors, fonts, or layout structure (design decisions)
- Add new sections or components (building)
- Remove content or features (product decisions)
- Refactor code structure (engineering decisions)
- Fix accessibility violations (that's `audit`)
- Redesign visual hierarchy (that's `critique` → fix skills)

**If you find bigger problems:** Note them in "Beyond Polish Scope" but don't fix them. Polish is the finisher, not the architect.

## Visual Gate (mandatory before declaring polish complete)

You cannot see your output from code alone. Before reporting done:

1. Render the affected page (dev server + Playwright MCP: `browser_navigate` → `browser_take_screenshot`).
2. Screenshot at three widths: **390px, 768px, 1440px** (`browser_resize` between shots).
3. Compare each screenshot against the intent: alignment, spacing, states, overflow, nothing broken at any breakpoint.
4. Found an issue → fix → re-screenshot. Repeat until all three pass.
5. Only then output the polish report. Include the screenshots' verdict per breakpoint in the report.

If the page cannot be rendered (no dev server, non-web target), state this explicitly in the report instead of silently skipping the gate.
