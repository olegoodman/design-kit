---
name: harden
description: >
  Add edge case resilience — loading states, error states, empty states, long content
  handling, i18n readiness, and production-ready defensive UI. Use when the design-orchestrator
  routes to harden, when audit identifies missing state handling, or when user says "edge
  cases", "error handling", "loading state", "empty state", "production-ready", "what if
  data is missing", "defensive UI", or "resilience". Do NOT use for: visual design fixes
  (use critique + fix skills), accessibility compliance (use audit), performance
  (use optimize), or responsive layout (use adapt).
---

# Harden — Edge Case Resilience

Make UI production-ready by handling what happens when things go wrong, are slow, are empty, or are unexpected. The happy path is where designs live in Figma. The real world is where loading spinners, error messages, empty states, and 47-character German compound nouns live.

## Protocol

### Step 1: Read and Identify the Happy Path

Read the code. Identify what the component expects:

- **Data dependencies**: what data does this section need? (array of items, user object, API response)
- **Async operations**: what loads from an API? What could be slow?
- **User input**: any forms, search, filters?
- **Dynamic content**: text that varies in length? Lists that vary in count?
- **Conditional rendering**: what gets shown/hidden based on state?

### Step 2: Check the Edge Case Checklist

For each data dependency, check all states:

#### Loading States
- [ ] **Initial load**: skeleton or spinner while data fetches (not blank space)
- [ ] **Skeleton matches layout**: skeleton shape resembles final content (not generic spinner)
- [ ] **Partial load**: if section has 3 data sources, what shows when 2/3 are loaded?
- [ ] **Slow connection**: what happens after 3+ seconds? (progress indicator, not frozen UI)

#### Error States
- [ ] **API failure**: graceful message, not blank section or stack trace
- [ ] **Retry option**: user can retry failed load without refreshing entire page
- [ ] **Partial failure**: if one subsection fails, others still render
- [ ] **Error boundary**: component errors don't crash the entire page (React: ErrorBoundary)

#### Empty States
- [ ] **Zero items**: list/grid with 0 items shows helpful message, not empty void
- [ ] **Empty message is actionable**: "No projects yet — create your first one" with CTA, not just "No data"
- [ ] **First-time user**: new user with no data sees guidance, not emptiness
- [ ] **Filtered to zero**: search/filter with no results explains why and suggests action

#### Content Extremes
- [ ] **Long text**: titles/names/descriptions that exceed expected length — truncated or wrapped, not breaking layout
- [ ] **Short text**: single-word title doesn't look lonely in a space designed for a sentence
- [ ] **Long numbers**: prices, counts, percentages with many digits don't overflow
- [ ] **Missing optional fields**: component handles undefined/null gracefully (not "undefined" rendered as text)
- [ ] **Single item**: grid/list with 1 item looks intentional, not broken
- [ ] **Many items**: 50+ items paginated or virtualized, not rendered all at once

#### Special Characters & i18n
- [ ] **HTML entities**: user-generated content sanitized (no XSS via <script> in title)
- [ ] **Unicode**: emoji, RTL text, accented characters display correctly
- [ ] **Long words**: German/Finnish compound words don't overflow — use `break-words` or `hyphens-auto`

### Step 3: Apply Fixes

Fix directly with Edit tool. Each fix handles one edge case.

**Common fix patterns:**

```
No loading state → skeleton:
  Before: {data.map(item => <Card />)}
  After:  {isLoading ? <div className="animate-pulse space-y-4">
            {[...Array(3)].map((_, i) => <div key={i} className="h-24 bg-gray-200 rounded-lg" />)}
           </div> : data.map(item => <Card />)}

No empty state → helpful message:
  Before: {items.map(item => <Card />)}
  After:  {items.length === 0 ? (
            <div className="text-center py-12">
              <p className="text-gray-500">No items yet</p>
              <Button className="mt-4">Create first item</Button>
            </div>
           ) : items.map(item => <Card />)}

Long text breaks layout:
  Before: <h3>{title}</h3>
  After:  <h3 className="line-clamp-2 break-words">{title}</h3>

Null/undefined renders as text:
  Before: <p>{user.company}</p>
  After:  {user.company && <p>{user.company}</p>}

Error boundary:
  Wrap section in ErrorBoundary with fallback UI
```

### Step 4: Report

```markdown
## Harden Report: [Section Name]

**Edge cases handled: N**

| # | Category | What | Fix |
|---|---|---|---|
| 1 | Loading | No skeleton for product grid | Added 3-item animated skeleton |
| 2 | Empty | No message when list empty | Added "No items" + CTA |
| 3 | Content | Long titles break card layout | Added line-clamp-2 break-words |
| 4 | Error | API failure shows blank | Added error message + retry button |
| 5 | Content | Null company renders "undefined" | Added conditional render |

**States covered: loading / error / empty / content-extremes**
**Not covered: [any states still missing]**
```

## Scope Boundaries

- Add loading, error, empty states; handle content extremes; defensive rendering
- Don't change visual design — that's critique + fix skills
- Don't fix accessibility — that's `audit`
- Don't optimize performance — that's `optimize`
- Don't add features — only handle edge cases of existing features
- If the component has no data dependencies (pure static), harden has nothing to do — skip
