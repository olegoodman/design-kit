---
name: clarify
description: >
  Fix UX copy — labels, error messages, button text, placeholder text, empty states, microcopy.
  Makes interface language clear and actionable. Use when the design-orchestrator routes to
  clarify, or when user says "confusing text", "unclear labels", "bad error messages",
  "microcopy", "UX writing", or "button text doesn't make sense". Do NOT use for: marketing
  copy (use copywriting), visual design (use critique + fix skills), or content strategy
  (use content-strategy).
---

# Clarify — UX Copy

Fix the words on the interface. Good UX copy is invisible — users understand without thinking. Bad UX copy makes users stop, re-read, and guess.

## Protocol

### Step 1: Scan All Interface Text

Read the code. Identify every text element users see:
- Headings and labels
- Button/link text
- Form placeholders and helper text
- Error messages
- Empty state messages
- Tooltips and microcopy
- Navigation labels

### Step 2: Check Against Rules

| Rule | Bad | Good |
|---|---|---|
| **Buttons = verbs** | "Submit", "OK", "Yes" | "Save changes", "Create account", "Send message" |
| **Labels = nouns** | "Enter your info here" | "Email address" |
| **Errors = cause + fix** | "Invalid input" | "Email must include @. Example: name@company.com" |
| **Empty = action** | "No data" | "No projects yet — create your first one" |
| **Placeholder ≠ label** | Placeholder as only label (disappears on focus) | Label above + placeholder as example |
| **Consistent terminology** | "Save" / "Submit" / "Confirm" for same action | Pick one term, use everywhere |
| **No jargon** | "Authenticate credentials" | "Sign in" |

### Step 3: Fix and Report

```markdown
## Clarify Report: [Section Name]

**Fixes: N**

| # | Element | Before | After | Rule |
|---|---|---|---|---|
| 1 | Submit button | "Submit" | "Send message" | Buttons = verbs |
| 2 | Error message | "Invalid" | "Please enter a valid email" | Errors = cause + fix |
| 3 | Empty state | "No results" | "No results for 'X' — try broader terms" | Empty = action |
```
