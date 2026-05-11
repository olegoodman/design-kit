---
name: canva
description: >
  Create, edit, and export Canva designs via MCP: social media posts, presentations,
  flyers, posters, business cards. Use when user asks to make a design, create a post
  for Instagram/LinkedIn/YouTube, build a presentation, edit an existing Canva design,
  export to PDF/PNG, set up brand kit, or organize Canva folders.
  Do NOT use for: Figma, Photoshop, image generation (use nano-banana), drawing art
  on canvas (that's canvas-design skill), or Canva Apps SDK development.
---

# Canva Design Assistant

Orchestrate Canva MCP tools into reliable design workflows. Every design task follows
a predictable sequence — this skill ensures correct order, required confirmations,
and avoids known pitfalls.

## Core Principle

**Always confirm with the user before irreversible actions.** Show thumbnails, present
candidates for selection, get approval before committing edits.

## Decision Tree

```
User request
├── "set up brand kit" / first time → Brand Kit Setup
├── "create/make/design [something]"
│   ├── presentation / slides → Presentation Flow
│   └── everything else → Design Generation Flow
├── "edit/change/update [design]" → Editing Flow
├── "export/download [design]" → Export Flow
├── "find/search/organize" → Organization Flow
└── shortlink (canva.link/xxx) → resolve-shortlink FIRST, then relevant flow
```

---

## Brand Kit Setup

Run this when user has no brand kit or asks to set one up.

1. `list-brand-kits` — check if any exist
2. If none found:
   - Tell user to create brand kit in Canva UI (colors, fonts, logo)
   - Link: canva.com → Brand Kit (left sidebar)
   - Brand kits cannot be created via API — only read
3. If found — show list with names and thumbnails, let user pick default
4. Save chosen `brand_kit_id` for session — offer it by default in all generation calls

**Always ask** "Use brand kit [name]?" before generation. Never assume.

---

## Design Generation Flow

For: social media posts, flyers, posters, business cards, logos, invitations, etc.

### Step 1: Clarify parameters

Determine from user request:
- **design_type** — match to supported types (see `references/design-types.md`)
- **query** — MUST be detailed and specific, not generic
- **brand_kit_id** — ask if user wants brand kit applied
- **assets** — ask if user has images/videos to include

### Step 2: Upload assets (if any)

For each asset URL:
```
upload-asset-from-url(url, name) → job starts
Poll until status = "success" → get asset_id
```
Collect up to 10 asset_ids. Order matters — first = highest priority.

### Step 3: Generate candidates

```
generate-design(
  query: "detailed specific description",
  design_type: "instagram_post",
  brand_kit_id: "...",        # if user confirmed
  asset_ids: ["...", "..."]   # if uploaded
)
```

**Critical:** If query is too generic → error "Common queries will not be generated".
Fix: add details about colors, mood, content, audience, style.

### Step 4: Present candidates to user

Show all returned candidates. Let user pick one by number.

### Step 5: Create design from chosen candidate

```
create-design-from-candidate(job_id, candidate_id)
→ returns design_id (11 chars, starts with D)
```

**WARNING:** URLs from generate-design response are NOT design_ids.
Only use the design_id from create-design-from-candidate.

### Step 6: Offer next steps

- "Edit this design?" → Editing Flow
- "Export?" → Export Flow
- "Create another size?" → resize-design or new generation

---

## Presentation Flow

Presentations have a separate mandatory flow. Do NOT use `generate-design` for presentations.

### Step 1: Gather info

- Topic (max 150 chars)
- Audience: `casual`, `professional`, `educational`, or custom
- Style: `minimalist`, `playful`, `organic`, `modular`, `elegant`, `digital`, `geometric`, or custom
- Length: `short` (1-5 slides), `balanced` (5-15), `comprehensive` (15+)
- Brand kit (optional)

### Step 2: Create outline and request review

```
request-outline-review(
  topic, pages: [{title, description}, ...],
  audience, style, length, brand_kit_id?
)
```

This shows a widget to the user. **Wait for user approval in widget** before proceeding.

### Step 3: Generate presentation

Only after user approves outline:
```
generate-design-structured(
  topic, audience, style, length,
  presentation_outlines: [approved outline],
  brand_kit_id?, asset_ids?
)
```

### Step 4: Offer editing or export

---

## Editing Flow

For modifying text, images, layout in an existing design.

### Step 1: Get design_id

- If user provides Canva URL → extract 11-char design_id (starts with D)
- If user provides shortlink → `resolve-shortlink` first
- If user describes design → `search-designs(query)` → let them pick

### Step 2: Understand current state

```
get-design-pages(design_id) → list of pages with thumbnails
get-design-content(design_id, content_types: ["richtexts"]) → text content with element_ids
```

Show user what's on each page. Identify elements they want to change.

### Step 3: Start editing transaction

```
start-editing-transaction(design_id) → transaction_id
```

**The transaction locks the design.** Always commit or cancel — never leave hanging.

### Step 4: Perform operations

```
perform-editing-operations(
  transaction_id,
  operations: [...],   # batch multiple ops in one call
  page_index: 1        # 1-based
)
```

Available operations (see `references/editing-ops.md` for full params):
- `replace_text` — full text replacement in element
- `find_and_replace_text` — partial replacement (preferred, saves tokens)
- `update_fill` — replace image/video in element
- `insert_fill` — add new image/video to page
- `delete_element` — remove element
- `position_element` — move element (top/left in px)
- `resize_element` — change size (text: width only, height auto)
- `format_text` — color, size, weight, style, alignment, lists, links
- `update_title` — rename design

**Batch operations:** combine multiple ops in one call when possible.

### Step 5: Show preview and confirm

```
get-design-thumbnail(transaction_id, page_index) → thumbnail
```

Show thumbnail to user. Ask: "Commit these changes?"

### Step 6: Commit or cancel

- User approves → `commit-editing-transaction(transaction_id)`
- User declines → `cancel-editing-transaction(transaction_id)`

**If commit fails — ALL changes are lost.** Transaction_id becomes invalid.

---

## Export Flow

### Step 1: Check available formats

```
get-export-formats(design_id) → list of supported formats
```

### Step 2: Choose format based on task

| Task | Recommended format | Key params |
|------|--------------------|------------|
| Social media | PNG | `transparent_background: false` |
| Print (flyer, poster) | PDF | `size: "a4"`, `export_quality: "pro"` |
| Presentation handoff | PPTX | — |
| Animation / video | MP4 | `quality: "horizontal_1080p"` |
| Web use | JPG | `quality: 85` |
| Design asset | PNG | `transparent_background: true`, `lossless: true` |

### Step 3: Export

```
export-design(
  design_id,
  format: { type: "png", pages: [1], ... }
) → download URL
```

**Download URLs expire.** Tell user to download immediately or provide the link right away.

### Step 4: Offer resize

If user needs same design in different size:
```
resize-design(design_id, design_type: { type: "custom", width: X, height: Y })
```
This creates a copy — original stays unchanged.

---

## Organization Flow

### Search designs
```
search-designs(query: "...", ownership: "owned", sort_by: "modified_descending")
```

### Browse folders
```
list-folder-items(folder_id: "root", item_types: ["design", "folder"])
```

### Create folder and organize
```
create-folder(name: "LEINOS SMM", parent_folder_id: "root")
move-item-to-folder(item_id: "...", to_folder_id: "...")
```

---

## Known Limitations

- **font-family** cannot be changed via API (only weight, size, style, color)
- **Brand kits** are read-only — create/edit only in Canva UI
- **Autofill brand templates** requires Canva Enterprise plan
- **Headless mode** (`claude -p`) does not load Canva MCP tools (known bug)
- **Comments API** is in preview — may be unstable
- **Rate limits** exist but aren't publicly documented — use exponential backoff on errors

## Common Mistakes

1. **Generic query** → "Common queries will not be generated" error. Fix: be specific
2. **Using generate-design for presentations** → broken output. Fix: use outline flow
3. **Treating candidate URL as design_id** → all subsequent calls fail
4. **Forgetting to commit/cancel transaction** → design stays locked
5. **Expecting sync upload/export** → both are async, must poll
6. **Skipping brand kit question** → user gets unbranded design, disappointed
7. **Not showing thumbnail before commit** → user can't verify changes
