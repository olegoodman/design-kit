---
name: adapt
description: >
  Fix responsive design — breakpoints, mobile layout, touch targets, viewport behavior.
  Ensures sections work across devices from 320px to 1440px+. Use when the design-orchestrator
  routes to adapt, when critique or audit identifies responsive issues, or when user says
  "fix mobile", "breakpoints broken", "doesn't work on phone", "responsive issues", "touch
  targets too small", or "layout breaks on tablet". Do NOT use for: desktop-only layout fixes
  (use arrange), typography scaling (use typeset), performance optimization (use optimize),
  or full mobile redesign (use critique first).
---

# Adapt — Responsive Design

Make sections work across all screen sizes. Mobile isn't an afterthought — it's where most users are. The goal: every section looks intentional on every device, not like a desktop design that got squeezed.

## Protocol

### Step 1: Read and Map the Breakpoint System

Read the code. Identify what exists:

- **Breakpoint usage**: which Tailwind breakpoints appear? (sm:, md:, lg:, xl:, 2xl:)
- **Mobile-first?**: are base styles mobile and breakpoints scale up? Or desktop-first with overrides?
- **Grid behavior**: do grids collapse on mobile? (grid-cols-1 md:grid-cols-2 lg:grid-cols-3)
- **Hidden/shown elements**: anything with hidden md:block or md:hidden?

### Step 2: Check at Four Viewports

Mentally simulate (or check if you can) at these widths:

| Viewport | Width | Device | Priority |
|---|---|---|---|
| Mobile | 320-375px | iPhone SE / small Android | Highest — most users |
| Tablet | 768px | iPad portrait | Medium |
| Laptop | 1024px | Standard laptop | Medium |
| Desktop | 1440px | External monitor | Lower |

For each viewport, check:

#### Layout
- **Grid collapse**: multi-column grids → single column on mobile. If 3-col stays 3-col at 375px = broken
- **Flex wrap**: flex items that should wrap on mobile but don't (missing flex-wrap)
- **Container overflow**: content wider than viewport → horizontal scroll (the cardinal sin of mobile)
- **Stack order**: does content stack in a logical reading order? (image below text on mobile, not above if text needs context first)

#### Sizing
- **Text too small/large**: body text below 14px on mobile = unreadable. Headings above 3xl on mobile = too big
- **Images full-bleed**: images should typically be w-full on mobile, not fixed pixel widths
- **Padding too small**: px-2 on mobile = content hits edge. Minimum px-4 for breathing room
- **Padding too large**: desktop px-24 on mobile = content squeezed to a tiny column

#### Touch
- **Touch targets**: all clickable elements minimum 44x44px on mobile (WCAG 2.5.8). Tiny links/buttons = missed taps
- **Hover-dependent UI**: anything that only shows on hover is invisible on touch devices. Add tap alternative or show by default
- **Close-proximity targets**: buttons/links too close together → accidental taps. Minimum 8px gap between targets

#### Navigation & Content
- **Horizontal elements**: tabs, navbars, horizontal lists that overflow on mobile → add overflow-x-auto or stack vertically
- **Tables**: wide tables → horizontal scroll wrapper or stack cells vertically on mobile
- **Long forms**: form fields should be full-width on mobile (w-full), not side-by-side

### Step 3: Apply Fixes

Fix directly with Edit tool. Mobile-first approach:

**Key principles:**
- **Base = mobile, breakpoints = larger**: write mobile styles first, add md: and lg: for larger screens
- **Grid formula**: `grid-cols-1 md:grid-cols-2 lg:grid-cols-3` — start single column, expand
- **Padding formula**: `px-4 md:px-8 lg:px-16` — tight on mobile, spacious on desktop
- **Text formula**: `text-2xl md:text-3xl lg:text-4xl` — scale headings up, not body text
- **Hide wisely**: if hiding content on mobile (md:block hidden), make sure nothing critical is lost

**Common fix patterns:**

```
Grid not collapsing:
  Before: grid-cols-3
  After:  grid-cols-1 md:grid-cols-2 lg:grid-cols-3

Overflow on mobile:
  Before: flex gap-8
  After:  flex flex-col md:flex-row gap-4 md:gap-8

Touch target too small:
  Before: p-1 text-sm
  After:  p-3 text-sm min-h-[44px] min-w-[44px]

Desktop padding on mobile:
  Before: px-16 py-24
  After:  px-4 py-12 md:px-8 md:py-16 lg:px-16 lg:py-24
```

### Step 4: Report

```markdown
## Adapt Report: [Section Name]

**Fixes applied: N**
**Viewports verified: 320px, 768px, 1024px, 1440px**

| # | Viewport | What | Before | After |
|---|---|---|---|---|
| 1 | 320px | Grid doesn't collapse | grid-cols-3 | grid-cols-1 md:grid-cols-3 |
| 2 | 375px | Horizontal overflow | fixed width image | w-full max-w-none |
| 3 | 768px | Touch targets too small | p-1 on links | p-3 min-h-[44px] |
| 4 | All | Desktop padding on mobile | px-16 | px-4 md:px-8 lg:px-16 |

**Breakpoint system: [e.g., sm:640 md:768 lg:1024 xl:1280]**
```

## Scope Boundaries

- Fix breakpoints, grid collapse, padding scaling, touch targets, overflow, mobile stacking
- Don't redesign the desktop layout — that's `arrange`
- Don't change fonts or type scale — that's `typeset`
- Don't add mobile-specific features (hamburger menu, mobile nav) — that's building new functionality
- If you find a desktop layout issue while fixing responsive, note it: "Desktop layout issue found — consider `arrange`"
