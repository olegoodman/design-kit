---
name: delight
description: >
  Add personality, joy, and memorable moments to functional-but-boring interfaces. Small
  touches that make users smile. Use when the design-orchestrator routes to delight, or when
  user says "too corporate", "needs personality", "boring but works", "add charm", "feels
  lifeless", or "memorable moments". Do NOT use for: major visual changes (use bolder),
  animations (use animate), or brand voice (use brand).
---

# Delight — Add Personality

Add small, unexpected touches that make the interface memorable. Delight lives in micro-details: a clever empty state, a playful hover effect, a warm success message. Never at the expense of usability — delight is the cherry on top, not the cake.

## Protocol

### Step 1: Find Delight Opportunities

Read the code. Look for moments where a small touch would surprise:
- **Success states**: "Saved" → something warmer
- **Empty states**: blank → illustration + personality
- **Loading waits**: spinner → playful skeleton or message
- **Error recovery**: "Error" → empathetic + helpful
- **Hover/interaction**: static → micro-reaction
- **Copy tone**: corporate → human

### Step 2: Add Delight Touches (2-3 max)

| Touch | Example |
|---|---|
| **Personality in copy** | "Welcome back" → "Welcome back, good to see you" |
| **Playful empty state** | Generic "no items" → illustration + "Nothing here yet — let's change that" |
| **Success celebration** | "Saved" → "All set!" with a subtle checkmark animation |
| **Easter egg hover** | Logo subtle rotation on hover, cursor change to something fun |
| **Warm error messages** | "Something went wrong" → "Oops, that didn't work. Let's try again" |

**Key principles:**
- **Frequency inverse to intensity**: common actions get subtle delight, rare achievements get bigger celebration
- **Brand-appropriate**: fun startup ≠ legal firm. Match the personality to the context
- **Never block the user**: delight that adds friction (forced animations, modal celebrations) = anti-delight

### Step 3: Report

```markdown
## Delight Report: [Section Name]

**Touches added: N**

| # | Where | What | Why |
|---|---|---|---|
| 1 | Empty state | Illustration + playful copy | Turns absence into invitation |
| 2 | Success toast | "All set!" + checkmark animation | Celebrates completion warmly |
```
