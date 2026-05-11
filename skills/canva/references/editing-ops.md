# Editing Operations Reference

## Transaction lifecycle

```
start-editing-transaction(design_id) → transaction_id
  ↓
perform-editing-operations(transaction_id, operations[], page_index)
  ↓ (repeat as needed, batch when possible)
get-design-thumbnail(transaction_id, page_index) → show preview
  ↓
commit-editing-transaction(transaction_id)   # save
cancel-editing-transaction(transaction_id)   # discard
```

## Operations

### replace_text
Replace ALL text in an element.
```json
{ "type": "replace_text", "element_id": "...", "text": "New full text" }
```

### find_and_replace_text
Replace a substring. **Preferred over replace_text** — saves tokens.
```json
{ "type": "find_and_replace_text", "element_id": "...", "find_text": "old", "replace_text": "new" }
```

### update_fill
Replace image/video in an existing element.
```json
{ "type": "update_fill", "element_id": "...", "asset_type": "image", "asset_id": "...", "alt_text": "..." }
```
asset_id must come from `upload-asset-from-url` or `get-assets`.

### insert_fill
Add NEW image/video to a page.
```json
{
  "type": "insert_fill", "page_id": "...",
  "asset_type": "image", "asset_id": "...", "alt_text": "...",
  "width": 400, "height": 300, "left": 100, "top": 50,
  "rotation": 0, "opacity": 1.0
}
```
All positioning params optional. rotation: -180..180. opacity: 0..1.

### delete_element
```json
{ "type": "delete_element", "element_id": "..." }
```

### position_element
Move element on page. Values in pixels.
```json
{ "type": "position_element", "element_id": "...", "top": 100, "left": 200 }
```

### resize_element
```json
{ "type": "resize_element", "element_id": "...", "width": 500, "height": 300, "preserve_aspect_ratio": false }
```
- **Text elements:** only `width` works, height adjusts automatically
- With `preserve_aspect_ratio: true`: set only width OR height

### format_text
```json
{
  "type": "format_text",
  "element_id": "...",
  "formatting": {
    "color": "#FF5733",
    "font_size": 24,
    "font_weight": "bold",
    "font_style": "italic",
    "decoration": "underline",
    "strikethrough": "none",
    "text_align": "center",
    "line_height": 1.5,
    "link": "https://example.com",
    "list_level": 1,
    "list_marker": "disc"
  }
}
```

All formatting fields are optional. Only include what you want to change.

**NOT supported:** font-family (cannot change font via API).

| Field | Values |
|-------|--------|
| color | hex `#RRGGBB` |
| font_size | 1–800 |
| font_weight | `normal`, `bold` |
| font_style | `normal`, `italic` |
| decoration | `none`, `underline` |
| strikethrough | `none`, `strikethrough` |
| text_align | `start`, `center`, `end` |
| line_height | 0.5–2.5 |
| link | URI string (empty = remove link) |
| list_level | 0 = not a list, 1+ = nesting depth |
| list_marker | `none`, `disc`, `circle`, `square`, `decimal`, `lower-alpha`, `lower-roman` |

### update_title
Rename the design itself (not text on canvas).
```json
{ "type": "update_title", "title": "New Design Name" }
```

## Tips

- **Batch operations:** combine multiple ops in one `perform-editing-operations` call
- **Page index is 1-based** (first page = 1)
- **Always show thumbnail** after operations, before commit
- **Transaction timeout:** if left too long without activity, may expire — commit promptly
