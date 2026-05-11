---
name: extract
description: >
  Extract repeated patterns into reusable components. Identifies duplicated UI patterns and
  refactors them into shared components. Use when the design-orchestrator routes to extract,
  or when user says "repeated pattern", "component library", "reuse this", "DRY", "same
  card everywhere", or "extract component". Do NOT use for: building new components from
  scratch (use ui-styling), design system tokens (use design-system), or visual fixes
  (use critique + fix skills).
---

# Extract — Component Extraction

Find repeated UI patterns and turn them into shared components. If you see the same card/button/section pattern 3+ times with slight variations, it's a component waiting to be born.

## Protocol

### Step 1: Identify Repeated Patterns

Read the code. Look for:
- **Same structure, different data**: 3+ cards with same layout but different content
- **Copy-pasted blocks**: nearly identical JSX/HTML in multiple places
- **Consistent variations**: same base with small tweaks (size, color, icon)

### Step 2: Design the Component

For each pattern found:
1. **Identify the invariant**: what stays the same across all instances?
2. **Identify the variants**: what changes? (text, icon, color, size)
3. **Define props**: each variant = a prop. Keep props minimal
4. **Name it clearly**: `ProductCard`, `FeatureItem`, `TestimonialCard`

### Step 3: Extract and Replace

1. Create the component file with TypeScript props interface
2. Replace each instance with the component
3. Verify all variations are handled by props

### Step 4: Report

```markdown
## Extract Report

**Components extracted: N**

| # | Component | Instances | Props | Source |
|---|---|---|---|---|
| 1 | ProductCard | 6 instances | title, price, image, badge? | Products section |
| 2 | FeatureItem | 4 instances | icon, title, description | Features section |

**Lines reduced: ~X (from Y to Z)**
```
