---
name: optimize
description: >
  Fix UI performance — loading speed, rendering, animation jank, image optimization, bundle
  impact, Core Web Vitals. Use when the design-orchestrator routes to optimize, or when user
  says "slow", "laggy", "janky", "loading too long", "bundle size", "performance", "Core Web
  Vitals", or "LCP/CLS/INP". Do NOT use for: SEO performance audits (use seo-technical),
  visual design fixes (use critique + fix skills), or responsive layout (use adapt).
---

# Optimize — UI Performance

Make the interface fast. Users notice delays above 100ms and abandon above 3s. Every millisecond counts for conversion and Core Web Vitals.

## Protocol

### Step 1: Identify Performance Bottlenecks

Read the code. Check for:

#### Images (biggest LCP impact)
- Unoptimized formats (PNG/JPG where WebP/AVIF works)
- Missing `width`/`height` (causes CLS)
- No `loading="lazy"` on below-fold images
- Missing `srcset` for responsive images
- Oversized images (2000px served for 400px display)

#### JavaScript
- Heavy imports: full lodash, moment.js, chart libraries loaded upfront
- No code splitting: everything in one bundle
- Unused dependencies in the render path
- Client-side rendering where SSR/SSG would work

#### CSS/Animations
- Animating layout properties (width, height, top, left) — causes reflow
- Missing `will-change` on animated elements
- Large unused CSS
- No `content-visibility: auto` on below-fold sections

#### Rendering
- Missing React.memo on expensive components
- Lists without virtualization (rendering 100+ DOM nodes)
- No Suspense boundaries for async components
- Synchronous data fetching blocking render

### Step 2: Apply Fixes

Fix directly with Edit tool. Priority order: images → JS bundle → CSS → rendering.

**Common fix patterns:**
```
Image optimization:
  Before: <img src="hero.png">
  After:  <Image src="hero.webp" width={1200} height={600} loading="lazy" />

Heavy import:
  Before: import _ from 'lodash'
  After:  import debounce from 'lodash/debounce'

Animation jank:
  Before: transition: width 300ms (causes layout reflow)
  After:  transition: transform 300ms (GPU-composited)

Below-fold content:
  Before: always rendered
  After:  content-visibility: auto; contain-intrinsic-size: 500px;
```

### Step 3: Report

```markdown
## Optimize Report: [Section Name]

**Fixes applied: N**
**Estimated impact: [LCP/CLS/INP improvement]**

| # | Category | What | Before | After | Impact |
|---|---|---|---|---|---|
| 1 | Images | Hero image format | PNG 2.1MB | WebP 180KB | LCP -2s |
| 2 | JS | Full lodash import | 72KB gzipped | 4KB (debounce only) | Bundle -68KB |
| 3 | Animation | Width transition | 30fps, janky | 60fps, smooth | INP improved |
```
