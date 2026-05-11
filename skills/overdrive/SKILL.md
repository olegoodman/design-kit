---
name: overdrive
description: >
  Ambitious visual effects — shaders, spring physics, scroll-driven animations, 3D transforms,
  particle systems, WebGL, GSAP-level motion. Use when the design-orchestrator routes to
  overdrive, or when user says "wow effect", "advanced animation", "3D", "parallax",
  "spring physics", "particle effect", "shader", "GSAP", "framer motion advanced", or
  "60fps scroll animation". Do NOT use for: basic hover/transition (use animate), layout
  (use arrange), or reducing motion (use quieter).
---

# Overdrive — Ambitious Effects

Push beyond CSS transitions into advanced visual territory. This is for when the user wants effects that make people say "how did they do that?" — not for every button hover.

**Warning:** Overdrive effects have real costs — bundle size, mobile performance, accessibility. Every effect must justify its weight.

## Protocol

### Step 1: Understand the Effect Goal

Before building, clarify:
- **What feeling?** (premium, playful, futuristic, organic)
- **Where?** (hero only, throughout, specific interaction)
- **Budget?** (can we add a library? how much bundle weight is acceptable?)
- **Mobile?** (must work on mobile, or desktop-only acceptable?)

### Step 2: Choose the Right Tool

| Effect | Tool | Bundle cost | Mobile? |
|---|---|---|---|
| Spring/physics animations | Framer Motion | ~30KB | Yes |
| Scroll-driven parallax | CSS scroll-timeline / GSAP ScrollTrigger | 0 / ~25KB | Yes / Careful |
| 3D transforms | CSS transform-style: preserve-3d | 0 | Yes |
| Particle systems | tsParticles / custom Canvas | ~20KB | Careful |
| Shader effects | Three.js / custom WebGL | ~150KB | No (fallback needed) |
| Text reveal/split | Splitting.js + CSS | ~5KB | Yes |
| Smooth scroll | Lenis | ~10KB | Yes |
| Complex timelines | GSAP | ~25KB | Yes |

### Step 3: Implement with Fallbacks

1. Build the effect
2. Add `prefers-reduced-motion` fallback (static version)
3. Add mobile fallback if needed (simpler version or disabled)
4. Test performance: must maintain 60fps on target devices

### Step 4: Report

```markdown
## Overdrive Report: [Section Name]

**Effects added: N**

| # | Effect | Tool | Bundle cost | Mobile fallback |
|---|---|---|---|---|
| 1 | Parallax hero | CSS scroll-timeline | 0KB | Static positioning |
| 2 | Card 3D tilt | CSS preserve-3d + JS | 0KB | Standard hover shadow |

**Performance: 60fps on [tested devices]**
**prefers-reduced-motion: respected**
```
