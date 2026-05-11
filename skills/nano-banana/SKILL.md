---
name: nano-banana
description: >
  Generate and edit free-form, artistic images via Google Gemini (Nano Banana CLI).
  Best for low-stakes visuals where cost and speed matter more than precision.
  Use when: blog featured images, YouTube thumbnails, illustrations, decorative
  patterns, hero photos without critical text, mood-board exploration, high-volume
  experimental generations, abstract artwork, backgrounds. Russian triggers —
  "картинка для блога", "иллюстрация", "обложка", "фон", "паттерн", "мудборд",
  "сгенерируй картинку" (без текста или логотипа).
  Do NOT use for images with rendered text the reader must read (slides, banners
  with copy, infographics, social posts with quotes) — use gpt-image-2 instead.
  Do NOT use when a real brand logo, product photo, or specific face must stay
  intact — use gpt-image-2 with --refs. Do NOT use for vertical 9:16 formats
  (Reels, Stories, Shorts) — use gpt-image-2 for proper aspect ratio support.
allowed-tools: Bash(gemini:*)
---

# Nano Banana Image Generation

Generate professional images via the Gemini CLI's nanobanana extension.

## When to Use This Skill

ALWAYS use this skill when the user:
- Asks for any image, graphic, illustration, or visual
- Wants a thumbnail, featured image, or banner
- Requests icons, diagrams, or patterns
- Asks to edit, modify, or restore a photo
- Uses words like: generate, create, make, draw, design, visualize

Do NOT attempt to generate images through any other method.

## Before First Use

1. Verify extension is installed:
   ```bash
   gemini extensions list | grep nanobanana
   ```
2. If missing, install it:
   ```bash
   gemini extensions install https://github.com/gemini-cli-extensions/nanobanana
   ```
3. Verify API key is set:
   ```bash
   [ -n "$GEMINI_API_KEY" ] && echo "API key configured" || echo "Missing GEMINI_API_KEY"
   ```

## Command Selection

| User Request | Command |
|--------------|---------|
| "make me a blog header" | `/generate` |
| "create an app icon" | `/icon` |
| "draw a flowchart of..." | `/diagram` |
| "fix this old photo" | `/restore` |
| "remove the background" | `/edit` |
| "create a repeating texture" | `/pattern` |
| "make a comic strip" | `/story` |

## Available Commands

**Note:** Always use the `--yolo` flag to automatically approve all tool actions.

| Command | Use Case |
|---------|----------|
| `gemini --yolo "/generate 'prompt'"` | Text-to-image generation |
| `gemini --yolo "/edit file.png 'instruction'"` | Modify existing image |
| `gemini --yolo "/restore old_photo.jpg 'fix scratches'"` | Repair damaged photos |
| `gemini --yolo "/icon 'description'"` | App icons, favicons, UI elements |
| `gemini --yolo "/diagram 'description'"` | Flowcharts, architecture diagrams |
| `gemini --yolo "/pattern 'description'"` | Seamless textures and patterns |
| `gemini --yolo "/story 'description'"` | Sequential/narrative images |
| `gemini --yolo "/nanobanana prompt"` | Natural language interface |

## Common Options

- `--yolo` - **Required.** Auto-approve all tool actions (no confirmation prompts)
- `--count=N` - Generate N variations (1-8)
- `--preview` - Auto-open generated images
- `--styles="style1,style2"` - Apply artistic styles
- `--format=grid|separate` - Output arrangement

## Common Sizes

| Use Case | Dimensions | Notes |
|----------|------------|-------|
| YouTube thumbnail | 1280x720 | `--aspect=16:9` |
| Blog featured image | 1200x630 | Social preview friendly |
| Square social | 1080x1080 | Instagram, LinkedIn |
| Twitter/X header | 1500x500 | Wide banner |
| Vertical story | 1080x1920 | `--aspect=9:16` |

## Model Selection

Default: `gemini-2.5-flash-image` (~$0.04/image)

For higher quality (4K, better reasoning):
```bash
export NANOBANANA_MODEL=gemini-3-pro-image-preview
```

## Blog Featured Image Examples

```bash
# Modern illustration style
gemini --yolo "/generate 'modern flat illustration of developer coding at laptop, purple and blue gradient background, minimalist style, no text' --preview"

# Professional photography style
gemini --yolo "/generate 'professional editorial photo of coffee cup next to laptop on wooden desk, morning sunlight, shallow depth of field, no text' --count=3"

# Tech/abstract
gemini --yolo "/generate 'abstract visualization of neural network connections, dark background with glowing blue nodes, futuristic style' --preview"
```

## Icon Generation

```bash
gemini --yolo "/icon 'minimalist app logo for productivity tool' --sizes='64,128,256,512' --type='app-icon' --corners='rounded'"
```

## Diagram Generation

```bash
gemini --yolo "/diagram 'user authentication flow with OAuth' --type='flowchart' --style='modern'"
```

## Output Location

All generated images are saved to `./nanobanana-output/` in the current directory.

## Presenting Results

After generation completes:
1. List contents of `./nanobanana-output/` to find generated files
2. Present the most recent image(s) to the user
3. Offer to regenerate with variations if needed
4. **Suggest watermark removal**: "Хотите убрать водяной знак Gemini? Скажите `/unwatermark`"

## Watermark Removal

Generated images have a visible Gemini sparkle logo in the bottom-right corner. To remove it, use the `/unwatermark` skill:
```bash
python ~/.claude/skills/unwatermark/scripts/remove_watermark.py ./nanobanana-output/
```
This overwrites originals in place using reverse alpha blending — no quality loss.

## Refinements and Iterations

When the user asks for changes:
- **"Try again" / "Give me options"**: Regenerate with `--count=3`
- **"Make it more [adjective]"**: Adjust prompt and regenerate
- **"Edit this one"**: Use `gemini --yolo "/edit nanobanana-output/filename.png 'adjustment'"`
- **"Different style"**: Add `--styles="requested_style"` to the command

## Prompt Tips

1. **Be specific**: Include style, mood, colors, composition details
2. **Add "no text"**: If you don't want text rendered in the image
3. **Reference styles**: "editorial photography", "flat illustration", "3D render", "watercolor"
4. **Specify aspect ratio context**: "wide banner", "square thumbnail", "vertical story"

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `GEMINI_API_KEY` not set | `export GEMINI_API_KEY="your-key"` |
| Extension not found | Run install command from setup section |
| Quota exceeded | Wait for reset or switch to flash model |
| Image generation failed | Check prompt for policy violations, simplify request |
| Output directory missing | Will be created automatically on first run |

## Brand Negative Prompts (REQUIRED for branded content)

Before generating any image for LEINOS / Lignofix / Superfood / Kids-IN-Asia / Paperclip — **read `references/brand-negative-prompts.md`** and prepend the brand-specific negative-prompt block to your generation prompt.

Critical examples (full list in reference file):
- **Superfood**: NO Ayurveda / chakras / spiritual / yoga / saffron / mandalas (founder is Christian, target market is German organic — Ayurveda framing kills the brand)
- **Kids IN Asia**: NO poverty porn / crying children / white-saviour framing / identifiable real children faces
- **LEINOS**: NO industrial paint cans / Asian Paints aesthetic / cheap DIY-store look
- **Lignofix**: NO toxic chemical hazard imagery / hazmat / aggressive pesticide branding
- **Universal**: always add "no text" unless typography is the goal; "no extra fingers/malformed hands" (model defect)

If you skip this step you will generate brand-inappropriate images.