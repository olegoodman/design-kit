---
name: critique
description: >
  UX evaluation with quantitative scoring, persona-based testing, and visual hierarchy
  assessment. Diagnoses design quality before improvement. Use when the design-orchestrator
  routes to critique, when assessing "what's wrong" with a design, for vague "make it better"
  requests, or as pre-improvement analysis before any Tier 2/3 skill. Produces structured
  verdicts with issues mapped to specific fix skills. Always use this skill when evaluating
  existing UI/UX quality — even if the user doesn't say "critique", if the task requires
  understanding what's weak before fixing it, this is the right starting point.
  Do NOT use for: technical code audits (use audit), creative campaign evaluation
  (use creative-director), fixing issues (use Tier 2/3 skills), or pure content edits.
---

# Critique — UX Design Evaluation

Evaluate existing designs through structured UX analysis. Your role is diagnostic — identify what's weak and why, score it, and point to specific fixes. You are not a cheerleader; you are a building inspector for user experience. Be honest, specific, and actionable.

The research is clear on this: LLMs are surprisingly good at finding design problems when given explicit criteria after the fact, but bad at spontaneously avoiding them during generation (Agentic Design System, 2026). That's exactly what this skill exploits — structured retrospective evaluation.

## Protocol

### Step 1: Read the Design

Read the component/section/page code. If a screenshot is available, read that too. Understand:
- What is this section trying to accomplish?
- Who is the target user?
- What is the surrounding context (other sections, page flow)?

If the code is in a framework (React, Vue, Svelte), focus on the rendered output — what the user sees — not implementation details. Implementation quality is `audit`'s job.

### Step 2: Three-Persona Evaluation

Evaluate through three distinct lenses. Each persona reviews independently and writes 2-4 specific observations. These personas are deliberately different from creative-director's panel (CD/Strategist/Consumer/Jury) — critique evaluates UX, not creative quality.

#### Persona 1: UX Designer
> "Does this design communicate clearly and guide the user's eye?"

Focus: visual hierarchy, information architecture, whitespace usage, typography hierarchy, color contrast, CTA visibility, cognitive load, Gestalt principles (proximity, similarity, continuity).

#### Persona 2: Product Manager
> "Does this achieve the business goal and serve the target user?"

Focus: conversion clarity, value proposition visibility, trust signals, content priority, user flow logic, mobile-first considerations, competitive differentiation.

#### Persona 3: End User (first-time visitor)
> "Can I understand what this is and what to do in 5 seconds?"

Focus: 5-second test (what is this page about?), cognitive load (too many choices?), reading patterns (F-pattern/Z-pattern compliance), emotional first impression, perceived credibility, friction points.

### Step 3: Score Six Dimensions

Score each dimension 0-10. Be calibrated — most real-world designs score 4-6. A 7 is genuinely good. An 8 is excellent. A 9+ is exceptional and rare.

| Dimension | What it measures |
|---|---|
| **Visual Hierarchy** | Eye flow, emphasis on key elements, clear reading order |
| **Spacing & Rhythm** | Consistent spacing, breathing room, visual rhythm |
| **Cognitive Load** | Ease of processing, decision simplicity, information density |
| **Brand Consistency** | Adherence to established visual identity, recognizable voice |
| **Accessibility** | Perceivable, operable for diverse users, contrast, labels |
| **Screenshot-Worthiness** | Would this look good in a portfolio? Would someone share it? |

**Calibration anchors** (use these to prevent score drift):

| Score | What it means | Real-world equivalent |
|---|---|---|
| 2-3 | Weak — obvious problems visible immediately | Default HTML with minimal styling, homework project |
| 4-5 | Below average — functional but unpolished | Generic template with minor customization |
| 6 | Average — decent but forgettable | Standard SaaS landing page, competent but unremarkable |
| 7 | Good — intentional design choices visible | Well-designed product page that feels considered |
| 8 | Excellent — noticeably polished | Top-tier SaaS (Stripe, Linear, Vercel level) |
| 9-10 | Exceptional — sets the standard | Award-winning design, people screenshot and share |

**Anti-inflation rules:**
- Score BEFORE writing rationale — writing explanations first biases toward higher scores
- If all 6 scores are 7+, pause and recalibrate against the anchors above
- Ask: "Would a senior designer at a top agency be impressed?" If the honest answer is "no", cap at 7
- Compare against the best design you've seen in this category, not just "is it ok"

### Step 4: Identify Issues

For each issue found, provide:

```
ISSUE: [specific problem description]
DIMENSION: [which of the 6 dimensions]
SEVERITY: P0-blocker | P1-major | P2-minor | P3-polish
EVIDENCE: [what specifically in the code/design shows this]
ACTION: [verb] — [what to change]
FIX_SKILL: [which Tier 3 skill handles this]
```

**Action verbs** (use these instead of vague "improve"):
- RESTRUCTURE — rearrange layout/hierarchy
- INCREASE / DECREASE — spacing, sizing, contrast
- ADD — missing element (label, state, indicator)
- REMOVE — distracting or competing element
- REPLACE — swap inappropriate element
- ALIGN — fix alignment inconsistency
- DIFFERENTIATE — make distinct elements more different
- GROUP — apply proximity principle

**Issue-to-skill mapping:**

| Issue pattern | Fix skill |
|---|---|
| Typography hierarchy, font sizing, readability | `typeset` |
| Color palette, contrast, monotone | `colorize` |
| Layout, spacing, grid, alignment | `arrange` |
| Too bland, generic, lacks personality | `bolder` |
| Too aggressive, overwhelming | `quieter` |
| Animation, transitions needed | `animate` |
| Responsive, mobile breakpoints | `adapt` |
| Cluttered, too many elements | `distill` |
| Confusing labels, UX copy | `clarify` |
| Missing delight, personality | `delight` |
| Edge cases, error states | `harden` |
| Repeated patterns, extract component | `extract` |
| Inconsistent styles, design drift | `normalize` |
| First-run, empty states | `onboard` |
| Performance, loading | `optimize` |

### Step 5: Verdict

```
VERDICT: NEEDS_REVISION | APPROVED
COMPOSITE_SCORE: X.X / 10
DIMENSIONS: { vh: X, sr: X, cl: X, bc: X, a11y: X, sw: X }
ISSUES_COUNT: N (P0: X, P1: X, P2: X, P3: X)
RECOMMENDED_ROUTE: [ordered skill chain, highest-severity issues first]
TOP_ISSUE: [single most impactful fix]
```

**Verdict logic:**
- **APPROVED**: composite >= 7.0 AND zero P0/P1 issues
- **NEEDS_REVISION**: composite < 7.0 OR any P0/P1 issue exists

## Output Format

```markdown
# UX Critique: [Section/Component Name]

## Persona Observations

### UX Designer
- [observation 1]
- [observation 2]

### Product Manager
- [observation 1]
- [observation 2]

### End User
- [observation 1]
- [observation 2]

## Scores

| Dimension | Score | Rationale |
|---|---|---|
| Visual Hierarchy | X/10 | [one line why] |
| Spacing & Rhythm | X/10 | [one line why] |
| Cognitive Load | X/10 | [one line why] |
| Brand Consistency | X/10 | [one line why] |
| Accessibility | X/10 | [one line why] |
| Screenshot-Worthiness | X/10 | [one line why] |
| **Composite** | **X.X/10** | |

## Issues

[structured issues per Step 4 format]

## Verdict

[structured verdict per Step 5 format]
```

## Scope Boundaries

- **Not for technical code quality** — that's `audit` (a11y compliance, performance, code patterns)
- **Not for creative concept evaluation** — that's `creative-director` Phase 4 (originality, insight, HumanKind)
- **Not for fixing** — critique diagnoses, Tier 2/3 skills fix
- **Skip critique** when the user already knows the specific problem ("fix the spacing" → go to `arrange` directly)
