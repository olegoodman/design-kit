# Design Kit для Claude Code

Полный набор скиллов для дизайна сайтов, лендингов, дашбордов, презентаций и брендинга. Всё устанавливается одной командой и сразу подключается в Claude Code.

В наборе **33 скилла**, организованных в 4 уровня (Tier 4 поменялся в v1.1.0 — добавлен `gpt-image-2`, убран `canva`):

- **Tier 1 (Стратегия)** — что делать: оценка качества, выбор направления, креативные концепты.
- **Tier 2 (Имплементация)** — как делать: код для компонентов, дизайн-токены, бренд-айдентика.
- **Tier 3 (Шлифовка)** — улучшение конкретного аспекта: типографика, цвет, анимация, респонсив и т.д.
- **Tier 4 (Генерация ассетов)** — изображения, баннеры, слайды, продуктовые карточки.

Над всем стоит **`design-orchestrator`** — он сам решает, какой скилл вызвать под твою задачу. Тебе достаточно сказать «улучши вид этой секции» — оркестратор разберётся.

---

## Установка

### Вариант А: как marketplace (рекомендую — будут обновления)

Если ты получил папку `design-kit` локально:
```bash
# в Claude Code:
/plugin marketplace add ~/path/to/design-kit
/plugin install design-kit
```

Если выложено на GitHub:
```bash
/plugin marketplace add <github-url>
/plugin install design-kit
```

### Вариант Б: ручная копия (без marketplace)

```bash
# скопировать содержимое skills/ к себе в пользовательскую папку скиллов
cp -R ~/path/to/design-kit/skills/* ~/.claude/skills/
```

Этот вариант проще, но обновления придётся катать руками.

### Проверка

В новой сессии Claude Code напиши `/help` и скрольни до списка скиллов — должны появиться `design-orchestrator`, `ui-ux-pro-max`, `critique` и остальные.

---

## Что внутри (33 скилла)

### Tier 1 — Стратегия

| Скилл | Что делает | Setup |
|---|---|---|
| **design-orchestrator** | Главный роутер. Решает, какой Tier 2/3 скилл вызвать под задачу. Не пишет код сам. | Ничего не нужно |
| **ui-ux-pro-max** | Большая база знаний: 50+ стилей, 161 палитра, 57 шрифтовых пар, 99 UX-правил, 25 типов графиков, 10 техстеков. | Ничего не нужно |
| **creative-director** | Big Idea и креативные концепты по методологиям SIT / TRIZ / Lateral Thinking. Рекурсивный self-assessment с калибровкой по Cannes/D&AD. | Ничего не нужно |
| **critique** | Диагностика «что не так с дизайном»: 6-мерный скоринг, 3 персоны (UX-дизайнер, PM, пользователь), маппинг каждой проблемы на конкретный fix-скилл. | Ничего не нужно |
| **audit** | Технический аудит: WCAG 2.2 AA (10 проверок), Core Web Vitals (7), responsive (5), code quality (6), anti-patterns (5). Health score. | Ничего не нужно |

### Tier 2 — Имплементация

| Скилл | Что делает | Setup |
|---|---|---|
| **frontend-design** | Креативный, «вау»-код для лендинг-героев и one-off секций. Избегает generic SaaS-вида. | Ничего не нужно |
| **ui-styling** | Системные компоненты shadcn/ui + Tailwind. Доступные, композируемые, TS-first. Большой (5.7 MB) — содержит примеры компонентов. | Ничего не нужно. Опционально: **shadcn MCP** для поиска компонентов |
| **brand-setup** | One-time инициализация: создаёт `brand-guidelines.md` и `design-tokens.json/.css` из реальных значений проекта. | Ничего не нужно. Запускается **один раз на проект** |
| **brand** | Голос бренда, идентичность, messaging, валидация ассетов, управление палитрой. | Ничего не нужно |
| **design** | Логотипы (55 стилей), CIP (50 deliverables), баннеры (22 стиля), иконки (15 стилей), соцфото. Под капотом использует Gemini AI. | ⚠️ Нужен **Gemini CLI** (`gemini auth login`) — см. ниже |
| **design-system** | Трёхслойные токены (primitive → semantic → component), CSS-переменные, премиум-презентации с BM25 поиском по слайдам, Chart.js. | Ничего не нужно для токенов. Для слайдов опционально: Python 3 + `pip install rank-bm25` |

### Tier 3 — Шлифовка (всё работает сразу, ничего не нужно)

| Скилл | Когда вызывать |
|---|---|
| **polish** | Финальные 5% перед шипом: alignment, spacing, hover/focus states, transitions |
| **typeset** | Типографика — иерархия, размеры, веса, line-height, читаемость |
| **arrange** | Лейаут, spacing, визуальный ритм; кривая сетка, неровные отступы |
| **colorize** | Палитра, контраст, 60-30-10; всё серое или цвета конфликтуют |
| **bolder** | Усилить пресный/безликий дизайн; «выглядит как шаблон» |
| **quieter** | Приглушить кричащий, перегруженный дизайн |
| **animate** | Осмысленные анимации (transform + opacity, GPU-композитинг, prefers-reduced-motion) |
| **optimize** | Производительность UI: скорость, рендеринг, бандл, изображения |
| **adapt** | Респонсив: 320 / 768 / 1024 / 1440 px, тач-таргеты, мобильный лейаут |
| **clarify** | UX-копирайт: ошибки, лейблы, инструкции, микрокопи |
| **distill** | Упростить, убрать лишнее, less is more |
| **delight** | Добавить радость, личность, запоминающиеся детали |
| **harden** | Edge cases: loading / error / empty states, long content, i18n |
| **extract** | Вынести повторяющиеся паттерны в дизайн-систему |
| **normalize** | Выровнять под систему: расхождения в стилях, дрейф токенов |
| **onboard** | Онбординг-флоу, empty states, first-run experience |
| **overdrive** | Шейдеры, spring-physics, scroll-driven анимации, 60fps. Тяжёлая артиллерия |

### Tier 4 — Генерация ассетов

| Скилл | Что делает | Setup |
|---|---|---|
| **gpt-image-2** ⭐ | OpenAI GPT Image 2. **99% точность текста в картинке**, все 8 aspect ratios (включая 9:16 mobile-first), edit-mode сохраняет логотипы/продукты. Default для брендированных/текстовых ассетов. | ⚠️ **OpenAI API key** — см. ниже |
| **nano-banana** | Генерация через **Google Gemini**. Дешевле и быстрее, но текст в картинке хуже. Default для блог-обложек, иллюстраций, паттернов, mood-board. | ⚠️ **Gemini CLI** — см. ниже |
| **product-card-image** | LEINOS-специфичные карточки товаров. 3-step pipeline (ImageMagick + Gemini), 4:3, 800px WebP. | ⚠️ **ImageMagick** + **Gemini CLI**. Только для LEINOS — можно удалить, если не нужно |
| **banner-design** | Баннеры для соцсетей, рекламы, веба, печати. 22 стиля. Внутри сама роутится: текст → gpt-image-2, чистая картинка → nano-banana. | ⚠️ **OpenAI** и/или **Gemini** |
| **slides** | Стратегические HTML-презентации с Chart.js, дизайн-токенами, респонсив-лейаутом. | Ничего не нужно |

#### Как оркестратор выбирает между `gpt-image-2` и `nano-banana`

| Задача | Скилл | Почему |
|---|---|---|
| Слайд / инфографика / соц-пост с текстом | `gpt-image-2` | Текст рендерится без артефактов (99% accuracy) |
| Баннер с надписью «Скидка 30%» | `gpt-image-2` | То же — текст читаемый |
| Изображение, где должен быть **наш логотип** или **наш продукт** | `gpt-image-2` с `--refs` | Edit-mode сохраняет референсы across много генераций |
| Вертикальный формат 9:16 (Reels, Stories) | `gpt-image-2` | Поддерживает все 8 aspect ratios нативно |
| Блог-обложка, YouTube thumbnail (без критичного текста) | `nano-banana` | Дешевле, быстрее, картинка важнее текста |
| Иллюстрация, паттерн, mood-board, hero-photo | `nano-banana` | Свободная стилистика, low-stakes |
| Много вариантов «накидать идей» | `nano-banana` | Volume + cost |

Просто говори задачу — оркестратор сам выберет правильный движок. Если хочешь явно — упомяни имя скилла.

---

## Setup: что и куда

Ниже — что нужно завести **только для Tier 4 и `design` из Tier 2**. Всё остальное работает из коробки.

### 1. OpenAI API key (для `gpt-image-2`, частично `banner-design`)

GPT Image 2 — платный API от OpenAI. Один генерируемый слайд high quality ≈ $0.03-0.10.

**Шаги:**
1. Завести ключ на [platform.openai.com/api-keys](https://platform.openai.com/api-keys) (нужен оплаченный баланс).
2. Скопировать template в реальный конфиг:
   ```bash
   cp ~/.claude/plugins/cache/<...>/design-kit/skills/gpt-image-2/config.yaml.example \
      ~/.claude/plugins/cache/<...>/design-kit/skills/gpt-image-2/config.yaml
   ```
   (точный путь зависит от того, как ты ставил плагин; ищи `gpt-image-2/config.yaml.example`)
3. Открыть `config.yaml`, заменить `sk-REPLACE_ME` на свой ключ.
4. Проверить: `python3 ~/.../gpt-image-2/scripts/_client.py` — должно сказать «✅ API доступно».

**Альтернатива — прокси.** Если хочешь использовать прокси (OpenRouter, hopto-прокси, etc.), поменяй `endpoint` в `config.yaml` на нужный URL.

Если не хочешь возиться с OpenAI — **просто удали скилл**:
```bash
rm -rf ~/.claude/skills/gpt-image-2
```
Тогда оркестратор автоматически будет роутить все картинки на `nano-banana`.

### 2. Gemini CLI (для `design`, `nano-banana`, `product-card-image`, `banner-design`)

Бесплатный CLI от Google для генерации картинок через Gemini.

```bash
# установка
npm install -g @google/gemini-cli

# аутентификация — откроет браузер
gemini auth login

# проверка
gemini --version
```

Если не хочешь Gemini — удали:
```bash
rm -rf ~/.claude/skills/{nano-banana,banner-design,product-card-image,design}
```

### 3. ImageMagick (только для `product-card-image`)

```bash
# macOS
brew install imagemagick

# Linux
sudo apt install imagemagick
```

### 4. shadcn MCP (опционально, для `ui-styling`)

Сам `ui-styling` работает и без MCP — он знает shadcn-паттерны изнутри. MCP даёт **живой поиск компонентов** в реестре shadcn. Подробности: `~/.claude/skills/ui-styling/SKILL.md`.

---

## Что НЕ требует никакого setup'а (большая часть)

Из 33 скиллов **28 работают сразу** без единой настройки:

```
design-orchestrator, ui-ux-pro-max, creative-director, critique, audit,
frontend-design, ui-styling, brand-setup, brand, design-system,
polish, typeset, arrange, colorize, bolder, quieter, animate,
optimize, adapt, clarify, distill, delight, harden, extract,
normalize, onboard, overdrive, slides
```

Если хочешь **минимальный набор без ключей** — удали 5 скиллов и забудь про setup:
```bash
cd ~/.claude/skills/
rm -rf gpt-image-2 nano-banana banner-design product-card-image design
```

Или **только OpenAI без Gemini** (если ОК с тем, что блог-обложек не будет, зато слайды/баннеры с текстом работают):
```bash
rm -rf ~/.claude/skills/{nano-banana,product-card-image,design}
# оставляем gpt-image-2 и banner-design (он сам обойдётся без gemini)
```

Или **только Gemini без OpenAI** (как было в v1.0.0):
```bash
rm -rf ~/.claude/skills/gpt-image-2
```

---

## Как этим пользоваться

В 90% случаев тебе не нужно знать, какой именно скилл вызывать — `design-orchestrator` сделает выбор за тебя.

**Просто пиши задачу естественным языком:**

```
«Сделай эту секцию более выразительной»
   → orchestrator выберет: critique → bolder → polish

«Проверь весь сайт на мобилке»
   → orchestrator выберет: critique + audit + adapt

«Сгенерируй баннер для Instagram про скидку 30%»
   → orchestrator выберет: banner-design → gpt-image-2 (текст «-30%» должен быть читаемым)

«Сделай обложку для блога про дизайн-системы»
   → orchestrator выберет: nano-banana (картинка без критичного текста, дешевле)

«Сделай 8 слайдов про наш продукт с нашим логотипом»
   → orchestrator выберет: gpt-image-2 build_deck.py с --refs логотипа

«Создай дизайн-систему с нуля»
   → orchestrator выберет: brand-setup → design-system → ui-styling

«Этот лендинг скучный»
   → orchestrator выберет: critique → bolder → colorize → polish
```

Если хочешь вызвать конкретный скилл напрямую — упомяни его имя:
```
«Запусти critique для главной страницы»
«Применить polish к секции hero»
```

---

## Структура пакета

```
design-kit/
├── .claude-plugin/
│   ├── plugin.json          # манифест плагина
│   └── marketplace.json     # манифест маркетплейса
├── skills/
│   ├── design-orchestrator/ # ← главный роутер
│   ├── ui-ux-pro-max/       # ← база знаний (1.8 MB)
│   ├── critique/
│   ├── audit/
│   ├── creative-director/
│   ├── frontend-design/
│   ├── ui-styling/          # ← компоненты shadcn (5.7 MB)
│   ├── design-system/       # ← токены + слайды (236 KB)
│   ├── ...                  # 17 Tier 3 скиллов
│   └── ...                  # 5 Tier 4 скиллов
└── README.md                # ← этот файл
```

Общий размер: **~11 MB**.

---

## Удаление

```bash
# если ставил как плагин:
/plugin uninstall design-kit
/plugin marketplace remove design-kit-marketplace

# если копировал руками:
cd ~/.claude/skills/
rm -rf design-orchestrator ui-ux-pro-max creative-director critique audit \
       frontend-design ui-styling brand-setup brand design design-system \
       polish typeset arrange colorize bolder quieter animate optimize \
       adapt clarify distill delight harden extract normalize onboard \
       overdrive gpt-image-2 nano-banana product-card-image banner-design slides
```

---

## Troubleshooting

**Q: Я устанавил всё, но скиллы не появляются в `/help`.**
Перезапусти Claude Code (`/quit` → запустить заново). Скиллы подхватываются на старте сессии.

**Q: `design` или `nano-banana` ругаются на Gemini.**
Запусти `gemini auth login` ещё раз. Если не помогло — `gemini --version` должна выдавать версию; если нет — переустанови CLI.

**Q: `gpt-image-2` пишет «⚠️ Обнови API» / 401 / 429.**
Открой `gpt-image-2/config.yaml` и проверь:
- Поле `key:` — там настоящий `sk-...`, а не `sk-REPLACE_ME`
- Баланс на [platform.openai.com/usage](https://platform.openai.com/usage) — если 0, GPT Image 2 не будет работать
- `endpoint:` — официальный `https://api.openai.com/v1` или твой прокси

Скилл читает `config.yaml` на каждом вызове, рестарт Claude Code не нужен.

**Q: Скилл вообще не запускается, хотя должен.**
Открой `~/.claude/skills/<имя>/SKILL.md`, проверь поле `description:` — оно должно содержать триггеры под твою задачу. Иногда фразу нужно переформулировать, чтобы Claude её подцепил.

**Q: Хочу свой скилл добавить в набор.**
Положи папку в `skills/<имя>/` со структурой `SKILL.md` (frontmatter: `name`, `description`, остальное опционально). Сразу заработает.

---

## Что НЕ входит в набор (специально)

Эти скиллы у меня (Олега) есть в `~/.claude/skills/`, но **намеренно не положены** в `design-kit`, потому что они не дизайнерские:

- `seo-*` (16 скиллов) — SEO-аудит, контент, schema, sitemaps
- `paid-ads`, `ad-creative`, `ad-operations` — реклама
- `copywriting`, `cold-email`, `email-sequence` — копирайтинг
- `priya-trainer`, `whatsapp-sales-india`, `telecrm` — продажи / CRM
- `research`, `research-day`, `research-youtube` — ресерч
- `bd`/`task`/`save`/`work` — личный workflow

Если что-то из этого захочется — спроси, могу собрать отдельный пакет.

---

## Версии и автор

- **v1.1.0** (май 2026) — убран `canva` (отказались от подписки); добавлен `gpt-image-2` (OpenAI flagship image model); routing-table перенастроена: gpt-image-2 ↔ nano-banana по правилам «текст в картинке / референсы / vertical → gpt-image-2, всё остальное → nano-banana».
- **v1.0.0** (май 2026) — первая сборка, 33 скилла.
- Автор: Oleg.
- Лицензия: используй как хочешь, без гарантий.
