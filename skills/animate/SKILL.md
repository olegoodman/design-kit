---
name: animate
description: >
  Add purposeful animations, micro-interactions, transitions, and motion effects. Every
  animation should improve usability or create delight — never just for decoration. Use when
  the design-orchestrator routes to animate, when critique identifies missing interactive
  feedback, or when user says "add animations", "transitions", "hover effects", "scroll
  animations", "motion design", "micro-interactions", "loading states", or "feels static".
  Do NOT use for: layout fixes (use arrange), responsive (use adapt), performance of existing
  animations (use optimize), or reducing motion (use quieter).
---

# Animate — Purposeful Motion

Add motion that serves a purpose. Every animation should answer: "What does this help the user understand?" If the answer is "nothing — it just looks cool," it's probably noise. Good motion guides attention, confirms actions, and creates spatial relationships.

## Protocol

### Step 1: Read and Map Existing Motion

Read the code. Understand what motion exists:

- **Transitions**: which elements have `transition-*` classes? What properties? Duration?
- **Hover states**: which interactive elements respond to hover? How? (opacity, scale, color, shadow)
- **Scroll animations**: any intersection observer usage? Scroll-driven animations?
- **Loading states**: skeletons, spinners, or bare empty space?
- **prefers-reduced-motion**: respected anywhere?

### Step 2: Check for Issues

#### Missing Feedback
- **Dead buttons**: buttons with no hover/active/focus response — feels broken
- **Silent transitions**: page state changes (tab switch, accordion, modal) with no animation — feels jarring
- **No entry animation**: content appears instantly instead of fading/sliding in — misses chance to guide the eye
- **Ghost links**: text links with no hover indication — user unsure what's clickable

#### Animation Quality
- **Too fast**: transitions under 100ms feel glitchy. Under 150ms is borderline
- **Too slow**: transitions over 400ms feel sluggish. 500ms+ = user waiting for UI
- **Wrong easing**: linear motion feels robotic. Use ease-out for enters, ease-in for exits
- **Jank**: animating layout properties (width, height, top, left) instead of GPU-composited (transform, opacity)

#### Overuse
- **Everything moves**: too many simultaneous animations = cognitive overload
- **Attention hijacking**: decorative loops that distract from content
- **Motion sickness risk**: large-scale movement without `prefers-reduced-motion` check

### Step 3: Apply Fixes

Fix directly with Edit tool. Each animation is small and surgical.

**Timing reference:**

| Type | Duration | Easing | Example |
|---|---|---|---|
| Micro-feedback | 150ms | ease | Button hover color |
| State change | 200-300ms | ease-out | Accordion open, tab switch |
| Entry animation | 300-500ms | ease-out | Section fade-in on scroll |
| Exit animation | 200ms | ease-in | Modal close, toast dismiss |
| Loading | 1000-1500ms | ease-in-out | Skeleton pulse |

**Common fix patterns:**

```
Dead button → interactive:
  Before: bg-blue-600
  After:  bg-blue-600 hover:bg-blue-700 active:scale-[0.98] transition-all duration-150

Silent tab switch:
  Before: hidden / block (instant swap)
  After:  transition-opacity duration-200 + opacity-0/opacity-100

No entry animation (Tailwind + intersection observer):
  Add: opacity-0 translate-y-4 transition-all duration-500
  On visible: opacity-100 translate-y-0

Card hover:
  Before: no hover state
  After:  hover:shadow-lg hover:-translate-y-1 transition-all duration-200

Always add reduced-motion:
  @media (prefers-reduced-motion: reduce) { *, *::before, *::after { transition-duration: 0.01ms !important; animation-duration: 0.01ms !important; } }
```

**Key principles:**
- **Feedback > decoration**: prioritize hover/active/focus states over scroll animations
- **Transform + opacity only**: these are GPU-composited and won't cause layout reflow (60fps)
- **Stagger, don't blast**: if multiple elements enter, stagger by 50-100ms each — not all at once
- **Always respect `prefers-reduced-motion`**: add the media query or use Tailwind's `motion-reduce:` variant
- **One entry animation per viewport**: user should see one orchestrated entrance, not a fireworks show

### Step 4: Report

```markdown
## Animate Report: [Section Name]

**Animations added: N**
**prefers-reduced-motion: [respected / added / already present]**

| # | Type | Element | Animation | Duration |
|---|---|---|---|---|
| 1 | Feedback | Primary button | hover:bg-blue-700 active:scale-98 | 150ms |
| 2 | Feedback | Card | hover:shadow-lg hover:-translate-y-1 | 200ms |
| 3 | Entry | Section headings | fade-in + translate-y on scroll | 500ms |
| 4 | State | Accordion content | opacity + height transition | 300ms |

**Performance: all animations use transform/opacity (GPU-composited)**
```

## Scope Boundaries

- Add hover/active/focus transitions, entry animations, state change transitions, loading states
- Don't add complex JS-driven animations (that's `overdrive` territory)
- Don't change layout or spacing — that's `arrange`
- Don't change colors — that's `colorize`
- If animations already exist but are too much, that's `quieter`
- After adding animations, suggest `optimize` if bundle/performance concerns exist
