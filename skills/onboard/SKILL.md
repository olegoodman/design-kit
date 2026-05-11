---
name: onboard
description: >
  Design first-run experiences, empty states, activation flows, and new user guidance. Use
  when the design-orchestrator routes to onboard, or when user says "first-time user", "empty
  state", "onboarding", "activation flow", "new user experience", or "getting started". Do
  NOT use for: edge case handling broadly (use harden), UX copy fixes (use clarify), or
  tutorial/docs content (write content directly).
---

# Onboard — First-Run Experience

Design the experience for users who have no data yet. The empty state is the most important screen most designers ignore — it's the first thing new users see, and it determines whether they come back.

## Protocol

### Step 1: Identify First-Run Moments

Read the code. Find screens/sections that depend on user data:
- Dashboards with zero items
- Lists/grids before any content exists
- Profiles before completion
- Settings before configuration

### Step 2: Design Empty States

For each empty moment, add:

1. **Visual**: illustration or icon (not just blank space)
2. **Message**: what this area will contain + why it matters
3. **Action**: primary CTA to create the first item
4. **Optional**: sample/demo data to show what it will look like

**Template:**
```jsx
<div className="text-center py-16">
  {/* Visual — illustration or icon */}
  <div className="text-gray-400 mb-4">[Icon/Illustration]</div>
  {/* Message — what + why */}
  <h3 className="text-lg font-semibold text-gray-900 mb-2">[What goes here]</h3>
  <p className="text-gray-500 mb-6 max-w-md mx-auto">[Why it matters, 1-2 sentences]</p>
  {/* Action — create first item */}
  <Button>[Create first X]</Button>
</div>
```

### Step 3: Report

```markdown
## Onboard Report: [Section Name]

**Empty states designed: N**

| # | Screen | Before | After |
|---|---|---|---|
| 1 | Projects list | Blank white space | Illustration + "Create your first project" CTA |
| 2 | Dashboard | "No data" text | Sample metrics + "Connect your first data source" |
```
