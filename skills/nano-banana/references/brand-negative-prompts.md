# Brand Negative Prompts Library

> Адаптировано из msitarzewski/agency-agents (specialized-cultural-intelligence-strategist). MIT.
> Используй ВСЕГДА перед генерацией картинки для одного из брендов экосистемы. Negative prompts — это первая защита от model bias и культурно неуместных стереотипов.

## Принцип

Negative prompt = явный список того, **что НЕ должно быть на картинке**. AI image models имеют сильные cultural defaults (Western settings, stereotypes, clichés по теме). Без negative prompt модель сама "догадывается" — и часто промахивается.

Каждый бренд имеет уникальные red lines. Не помнить их = генерировать брак.

## LEINOS India

**Бренд**: Premium natural paints, German heritage (с 1985), для архитекторов и дизайнеров в Индии.

**ALWAYS negative-prompt:**
```
no cheap-looking industrial paint cans, no synthetic plastic finish, no bright primary colors,
no graffiti, no DIY-store aesthetics, no Asian Paints/Berger style branding,
no construction site debris, no exposed scaffolding, no chemical hazard symbols,
no workers in dirty overalls, no stereotypical "third world" depictions of India
```

**ALWAYS positive-direction:**
```
premium minimalist composition, natural wood textures, German-quality finish,
architect-friendly aesthetic, soft natural lighting, real materials (not CGI plastic),
heritage German paint can design when relevant
```

**Examples by use case:**
| Use case | Add to negative |
|---|---|
| Product hero | no human hands holding, no cluttered background |
| Architect's project | no generic stock-photo office, no Western suburb, must show Indian context (Delhi/Mumbai/Bangalore architecture) |
| Wood + paint demo | no synthetic plastic-looking surface, must show real wood grain |

## Lignofix India

**Бренд**: EU-certified bio wood protection (Czech), B2B + B2C, focus на termites + monsoon damage.

**ALWAYS negative-prompt:**
```
no toxic chemical hazard imagery, no aggressive pesticide branding,
no graphic termite/insect close-ups (unsuitable for B2B web), no spraying with masks/hazmat suits,
no factory smokestacks, no "industrial chemical" aesthetic
```

**ALWAYS positive-direction:**
```
clean professional composition, EU-quality presentation, wood at peace,
visible protection layer (subtle sheen), moderate Indian climate context (monsoon ambience OK),
educational / scientific clarity over alarmist imagery
```

## Superfood

**Бренд**: Indian sourcing → European sales (Germany primary). Founder is **Christian** — explicit rule: NO Ayurveda spiritual positioning.

**ALWAYS negative-prompt (CRITICAL):**
```
NO Ayurveda imagery, NO chakras, NO meditation poses, NO incense/smoke,
NO mandala patterns, NO "spiritual wellness" aesthetics, NO yoga,
NO orange/saffron robes, NO hindu religious symbolism, NO third-eye imagery,
NO traditional ayurvedic herbs in bowls/mortar (sandalwood, etc.) as primary subject,
NO new-age wellness clichés
```

**ALWAYS positive-direction:**
```
European clean food photography, Nordic minimalism, scientific/nutritional framing,
NPOP/EU Organic certification visual cues, modern kitchen contexts,
Christian-neutral wellness (sport/family/nature), sourced-from-India provenance is fine
when shown as agricultural (farms/farmers), NOT as spiritual
```

**Why so strict**: founder's identity + target market (German organic consumers) responds to scientific/clean positioning, NOT to Indian spiritual marketing. Ayurveda framing = brand suicide for this audience.

## Kids IN Asia

**Бренд**: Charity, partnership с children's homes (India + Nepal), FCRA-compliant.

**ALWAYS negative-prompt:**
```
NO poverty porn, NO crying children, NO dirty/torn clothing as primary subject,
NO "white saviour" framing (donor with kids), NO shame-driven imagery,
NO faces of identifiable real children (privacy/safeguarding),
NO slum/poverty as aesthetic spectacle
```

**ALWAYS positive-direction:**
```
dignified joy, hopeful warm lighting, children engaged in activities (NOT just posing for camera),
educational/play contexts, agency and capability showed, nature when possible,
abstract/illustrated representation OK if photo too sensitive,
faces blurred or back-of-head shots if real photos used
```

## Paperclip / ESC.marketing / claudeclaw

**Бренд**: Marketing automation platform (Paperclip), AI agency tooling.

**ALWAYS negative-prompt:**
```
no robotic dystopia, no glowing brain in jar, no Terminator-AI clichés,
no generic "AI" stock images (faceless humanoid, blue circuit board, brain hologram),
no startup-bro hustle aesthetics
```

**ALWAYS positive-direction:**
```
calm professional, founder/operator-friendly, real tools/dashboards,
warm minimalism, "calm tech" aesthetic, modular/component visuals
```

## Universal Rules (apply to ALL brands)

```
no AI-generated text on images (always include "no text" unless typography is the goal),
no extra fingers / malformed hands (model defect),
no watermarks/logos of OTHER brands by accident,
no fictional placeholder text ("Lorem ipsum" or random alphabet soup),
no censorship bars / blurred regions unless requested,
no excessive bokeh/blur if subject must be clear
```

## Workflow

Перед `gemini --yolo "/generate ..."`:

1. **Identify brand** из контекста (LEINOS / Lignofix / Superfood / Kids-IN-Asia / Paperclip / general)
2. **Lookup negative-prompt block** из этого файла
3. **Compose prompt**: `<positive description>, <brand positive-direction>, <negative-prompt block>`
4. Generate
5. Review для скрытого нарушения (особенно для Superfood — Ayurveda визуально может проскользнуть)

## Что добавлять со временем

Если генерация дала "это не наш бренд" / "это не Индия" / "это слишком западное" — добавь явное negative в этот файл. Каждый такой случай = +1 строка для следующих генераций.

## Связь с другими skills

- **`brand`** / **`brand-setup`** — там живут positive brand voice rules
- **`design-orchestrator`** — может маршрутизировать в nano-banana, должен передавать brand context
- **`product-card-image`** (LEINOS) — уже использует locked creative brief, этот файл = дополнительный safety layer
