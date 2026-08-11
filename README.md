# Design Kit для Claude Code

Набор скиллов для дизайна сайтов, лендингов, дашбордов, презентаций и брендинга. Ставится одной командой и сразу подключается в Claude Code.

В наборе **35 скиллов**, организованных в 5 групп:

- **Tier 1 (Стратегия)** — что делать: диагностика качества, выбор направления, креативные концепты.
- **Tier 2 (Имплементация)** — как делать: код секций и компонентов, дизайн-токены, бренд-айдентика.
- **Motion** — решения по анимации: анимировать ли вообще, какой easing, какая длительность, ревью моушена.
- **Tier 3 (Шлифовка)** — улучшение конкретного аспекта: типографика, цвет, отступы, респонсив.
- **Tier 4 (Генерация ассетов)** — изображения, слайды, продуктовые карточки.

Над всем стоит **`design-orchestrator`** — он сам решает, какой скилл вызвать под задачу. Достаточно сказать «улучши вид этой секции» — оркестратор разберётся.

---

## Установка

### Вариант А: скриптом (рекомендуется — работает всё)

```bash
git clone https://github.com/olegoodman/design-kit.git
cd design-kit
./install.sh
```

Скрипт копирует скиллы в `~/.claude/skills/`, не трогая скиллы с такими же именами, если они у тебя уже есть (перезаписать с бэкапом — `./install.sh --force`). Дальше перезапусти Claude Code.

**Почему рекомендую именно этот вариант.** Четыре скилла (`gpt-image-2`, `nano-banana`, `design`, `brand-setup`) запускают свои python/node-скрипты по пути `~/.claude/skills/<имя>/scripts/...`. При установке плагином файлы лежат в `~/.claude/plugins/marketplaces/…`, и эти пути не находятся — генерация картинок падает с «No such file». Копия в `~/.claude/skills/` эту проблему снимает.

### Вариант Б: как плагин-marketplace (обновления одной командой)

```
/plugin marketplace add https://github.com/olegoodman/design-kit
/plugin install design-kit
```

Так удобнее обновляться (`/plugin update design-kit`), но скиллы со скриптами из абзаца выше работать не будут — им нужны пути `~/.claude/skills/`. Текстовые скиллы (а это 31 из 35) работают нормально.

### Проверка

Перезапусти Claude Code и набери `/help` — в списке скиллов должны появиться `design-orchestrator`, `taste-skill`, `critique`, `ui-ux-pro-max`.

---

## Что внутри

### Tier 1 — Стратегия

| Скилл | Что делает | Setup |
|---|---|---|
| **design-orchestrator** | Главный роутер. Классифицирует задачу и решает, какой скилл вызвать. Сам код не пишет. | Ничего не нужно |
| **ui-ux-pro-max** | База знаний: 50+ стилей, 161 палитра, 57 шрифтовых пар, 99 UX-правил, 25 типов графиков, 10 техстеков. | Ничего не нужно |
| **creative-director** | Big Idea и креативные концепты по SIT / TRIZ / Lateral Thinking. Рекурсивный self-assessment с калибровкой по Cannes/D&AD. | Ничего не нужно |
| **critique** | Диагностика «что не так»: 6-мерный скоринг, 3 персоны, маппинг каждой проблемы на конкретный fix-скилл. Рендерит страницу и смотрит на скриншот. | Playwright MCP — опционально, но сильно рекомендую (см. ниже) |
| **audit** | Технический аудит: WCAG 2.2 AA (10 проверок), Core Web Vitals (7), респонсив (5), качество кода (6), анти-паттерны (5). Health score. | Ничего не нужно |

### Tier 2 — Имплементация

| Скилл | Что делает | Setup |
|---|---|---|
| **taste-skill** ⭐ | Базовый билдер секций и лендингов. Design Read (тип страницы / vibe / аудитория / бренд → одна строка направления), три ручки (variance / motion / density), матрица «бриф → официальная дизайн-система» (Fluent, Carbon, Polaris, GOV.UK), запрет на AI-палитры и AI-шрифты, протокол редизайна. | Ничего не нужно |
| **frontend-design** | Смелый «вау»-код для one-off штук: постеры, одностраничники, визуальные эксперименты вне продуктовой кодовой базы. | Ничего не нужно |
| **ui-styling** | Системные компоненты shadcn/ui + Tailwind. Доступные, композируемые, TS-first. Тяжёлый (5.7 MB) — внутри примеры компонентов. | Опционально: shadcn MCP |
| **brand-setup** | One-time инициализация проекта: создаёт `brand-guidelines.md` и `design-tokens.json/.css` из реальных значений проекта. | Запускается один раз на проект |
| **brand** | Голос бренда, идентичность, messaging, валидация ассетов, работа с палитрой. | Ничего не нужно |
| **design** | Логотипы (55 стилей), CIP (50 deliverables), баннеры (22 стиля), иконки (15 стилей), соцфото. Под капотом Gemini. | Нужен Gemini CLI |
| **design-system** | Трёхслойные токены (primitive → semantic → component), CSS-переменные, состояния компонентов, премиум-презентации с BM25-поиском по слайдам и Chart.js. | Для слайдов опционально: Python 3 + `pip install rank-bm25` |

> **Важное правило: один базовый билдер на задачу.** `taste-skill` и `frontend-design` не запускаются вместе — два конкурирующих дизайн-скилла тянут результат к среднему. По умолчанию берётся `taste-skill`; `frontend-design` — только для одиночных артефактов вне продукта.

### Motion — решения по анимации

| Скилл | Что делает |
|---|---|
| **emil-design-eng** | Философия Эмиля Ковальски: анимировать ли вообще (таблица частоты: действие 100+ раз в день → никогда), какая цель, какой easing (вход/выход → ease-out, движение по экрану → ease-in-out, ease-in в UI — никогда), длительность UI < 300 мс. |
| **apple-design** | Принципы Apple HIG для веба: spring-физика, прерываемые переходы, жесты (drag/swipe/sheets), полупрозрачные материалы, оптическая типографика. |
| **animation-vocabulary** | Обратный словарь: расплывчатое описание эффекта → его точное название («такая пружинистая штука» → Pop in). Чтобы точно формулировать запрос. |
| **review-animations** | Строгое ревью моушен-кода по 10 стандартам (оправданность, ease-out, < 300 мс, transform-origin, только GPU-свойства, `prefers-reduced-motion`). Вызывается только явно по имени. |

### Tier 3 — Шлифовка (всё работает сразу)

| Скилл | Когда вызывать |
|---|---|
| **polish** | Финальные 5% перед шипом: alignment, отступы, hover/focus/disabled, переходы, overflow, тени |
| **typeset** | Типографика — иерархия, размеры, веса, line-height, читаемость, длина строки |
| **arrange** | Лейаут, отступы, визуальный ритм; кривая сетка, неровные gap'ы, сбитое выравнивание |
| **colorize** | Палитра, контраст, 60-30-10; всё серое или цвета конфликтуют |
| **bolder** | Усилить пресный дизайн; «выглядит как шаблон». Максимум 2–3 смелых хода на секцию |
| **quieter** | Приглушить кричащий, перегруженный дизайн |
| **optimize** | Производительность UI: скорость, рендеринг, бандл, изображения |
| **adapt** | Респонсив: 320 / 768 / 1024 / 1440 px, тач-таргеты, мобильный лейаут |
| **clarify** | UX-копирайт: ошибки, лейблы, инструкции, микрокопи |
| **distill** | Упростить, убрать лишнее, less is more |
| **delight** | Добавить радость, личность, запоминающиеся детали |
| **harden** | Edge cases: loading / error / empty states, длинный контент, i18n |
| **extract** | Вынести повторяющиеся паттерны в дизайн-систему |
| **normalize** | Выровнять под систему: расхождения в стилях, дрейф токенов |
| **onboard** | Онбординг-флоу, empty states, first-run experience |

### Tier 4 — Генерация ассетов

| Скилл | Что делает | Setup |
|---|---|---|
| **gpt-image-2** ⭐ | OpenAI GPT Image 2: 99% точность текста в картинке, все 8 aspect ratios (включая 9:16), edit-mode сохраняет логотипы и продукты между генерациями. Дефолт для брендированных и текстовых ассетов. | OpenAI API key |
| **nano-banana** | Генерация через Google Gemini. Дешевле и быстрее, текст в картинке хуже. Дефолт для блог-обложек, иллюстраций, паттернов, mood-board. | Gemini CLI |
| **product-card-image** | Карточки товаров для сайта LEINOS: 3-шаговый пайплайн (ImageMagick + Gemini), 4:3, 800px WebP. Специфичен для одного проекта — можно смело удалять. | ImageMagick + Gemini CLI |
| **slides** | HTML-презентации с Chart.js, дизайн-токенами и респонсив-лейаутом. | Ничего не нужно |

#### Как выбирается движок картинок

| Задача | Скилл | Почему |
|---|---|---|
| Слайд / инфографика / соц-пост с текстом | `gpt-image-2` | Текст рендерится без артефактов |
| Баннер с надписью «Скидка 30%» | `gpt-image-2` | То же — надпись читаемая |
| Нужен реальный логотип, продукт или лицо | `gpt-image-2` с `--refs` | Edit-mode держит референс на серии генераций |
| Вертикаль 9:16 (Reels, Stories) | `gpt-image-2` | Нативная поддержка всех соотношений |
| Блог-обложка, YouTube-превью без критичного текста | `nano-banana` | Дешевле и быстрее |
| Иллюстрация, паттерн, mood-board | `nano-banana` | Свободная стилистика, low-stakes |
| Много вариантов «накидать идей» | `nano-banana` | Объём и цена |

---

## Setup: что и куда

Из 35 скиллов **31 работает сразу**. Настройка нужна только для картинок и (опционально) для скриншот-гейта.

### 1. Playwright MCP — для скриншот-гейта в `critique` и `polish`

Это главное отличие v1.2.0: `critique` не оценивает дизайн по коду, а рендерит страницу и смотрит на скриншот минимум на 390 px и 1440 px; `polish` перед вердиктом «готово» снимает три ширины — 390 / 768 / 1440 — и правит, пока все три не пройдут. Без Playwright скиллы работают, но честно понижают уверенность вердикта и пишут, что оценка сделана только по коду.

```bash
claude mcp add playwright -- npx -y @playwright/mcp@latest
```

### 2. OpenAI API key — для `gpt-image-2`

Платный API. Один слайд в high quality ≈ $0.03–0.10.

1. Завести ключ на [platform.openai.com/api-keys](https://platform.openai.com/api-keys) (нужен положительный баланс).
2. Скопировать шаблон конфига и вписать ключ:
   ```bash
   cp ~/.claude/skills/gpt-image-2/config.yaml.example ~/.claude/skills/gpt-image-2/config.yaml
   # открыть config.yaml и заменить sk-REPLACE_ME на свой ключ
   ```
3. Проверить: `python3 ~/.claude/skills/gpt-image-2/scripts/_client.py` — должно ответить «✅ API доступно».

Конфиг читается на каждом вызове, перезапускать Claude Code не нужно. Не нужен OpenAI — `rm -rf ~/.claude/skills/gpt-image-2`, тогда все картинки пойдут на `nano-banana`.

### 3. Gemini CLI — для `nano-banana`, `design`, `product-card-image`

```bash
npm install -g @google/gemini-cli
gemini auth login      # откроет браузер
gemini --version       # проверка
```

Не нужен — `rm -rf ~/.claude/skills/{nano-banana,design,product-card-image}`.

### 4. ImageMagick — только для `product-card-image`

```bash
brew install imagemagick        # macOS
sudo apt install imagemagick    # Linux
```

### 5. shadcn MCP — опционально, для `ui-styling`

`ui-styling` знает shadcn-паттерны изнутри и работает без MCP. MCP добавляет живой поиск компонентов в реестре.

### Минимальные наборы

```bash
# совсем без ключей и без генерации картинок (31 скилл)
rm -rf ~/.claude/skills/{gpt-image-2,nano-banana,design,product-card-image}

# только OpenAI, без Gemini
rm -rf ~/.claude/skills/{nano-banana,design,product-card-image}

# только Gemini, без OpenAI
rm -rf ~/.claude/skills/gpt-image-2
```

---

## Про листинг скиллов — прочитай, если ставишь весь набор

Claude Code загружает описания **всех** установленных скиллов в контекст каждой сессии, и на это есть бюджет — примерно 1% контекстного окна. Если у тебя, кроме этого набора, есть свои скиллы, суммарный листинг может в бюджет не влезть: Claude Code тогда молча обрезает описания, и часть скиллов перестаёт вызываться сама — включая нужные.

Лечится штатным механизмом `skillOverrides` в `~/.claude/settings.json`: значение `name-only` убирает описание скилла из листинга, но оставляет его вызываемым по точному имени.

```json
{
  "skillOverrides": {
    "typeset": "name-only",
    "colorize": "name-only",
    "harden": "name-only"
  }
}
```

У меня в `name-only` вынесены 20 скиллов набора:

```
typeset  bolder  quieter  optimize  clarify  delight  harden  extract  normalize  onboard
animation-vocabulary  apple-design  review-animations
audit  brand  brand-setup  design  design-system  frontend-design  product-card-image
```

В листинге с описаниями остались те, что реально вызываются сами: `design-orchestrator`, `taste-skill`, `critique`, `polish`, `arrange`, `colorize`, `adapt`, `distill`, `emil-design-eng`, `ui-styling`, `ui-ux-pro-max`, `creative-director`, `gpt-image-2`, `nano-banana`, `slides`. Остальные оркестратор вызывает по точному имени — источник правды для него `skills/design-orchestrator/references/skill-catalog.md`, а не листинг.

Проверить, обрезан ли листинг: `/doctor` в Claude Code.

---

## Как пользоваться

В большинстве случаев не нужно знать, какой скилл вызывать — оркестратор выберет сам.

```
«Сделай эту секцию более выразительной»
   → critique → bolder → polish

«Собери секцию с ценами для лендинга»
   → taste-skill → polish

«Проверь весь сайт на мобилке»
   → critique + audit + adapt

«Стоит ли анимировать это меню и как»
   → emil-design-eng

«Сгенерируй баннер для Instagram про скидку 30%»
   → gpt-image-2 (текст «-30%» должен быть читаемым)

«Сделай обложку для блога про дизайн-системы»
   → nano-banana (картинка без критичного текста, дешевле)

«Сделай 8 слайдов про наш продукт с нашим логотипом»
   → gpt-image-2 build_deck.py с --refs логотипа

«Создай дизайн-систему с нуля»
   → brand-setup → design-system → ui-styling

«Этот лендинг скучный»
   → critique → bolder → colorize → polish
```

Нужен конкретный скилл — назови его по имени: «запусти critique для главной», «применить polish к hero».

---

## Структура пакета

```
design-kit/
├── .claude-plugin/
│   ├── plugin.json          # манифест плагина
│   └── marketplace.json     # манифест маркетплейса
├── install.sh               # установка в ~/.claude/skills/
├── skills/
│   ├── design-orchestrator/ # ← роутер + skill-catalog.md (источник правды)
│   ├── taste-skill/         # ← базовый билдер
│   ├── ui-ux-pro-max/       # ← база знаний (1.8 MB)
│   ├── ui-styling/          # ← компоненты shadcn (5.7 MB)
│   ├── creative-director/   # ← 3.0 MB
│   └── ...                  # ещё 30 скиллов
└── README.md
```

Общий размер: **~12 MB**.

---

## Обновление

```bash
# если ставил скриптом:
cd design-kit && git pull && ./install.sh --force
# старые версии уедут в ~/.claude/skill-backups/design-kit-<дата>/

# если ставил плагином:
/plugin update design-kit
```

## Удаление

```bash
# если ставил плагином:
/plugin uninstall design-kit
/plugin marketplace remove design-kit-marketplace

# если ставил скриптом:
cd ~/.claude/skills/
rm -rf design-orchestrator ui-ux-pro-max creative-director critique audit \
       taste-skill frontend-design ui-styling brand-setup brand design design-system \
       emil-design-eng review-animations apple-design animation-vocabulary \
       polish typeset arrange colorize bolder quieter optimize adapt clarify \
       distill delight harden extract normalize onboard \
       gpt-image-2 nano-banana product-card-image slides
```

---

## Troubleshooting

**Скиллы не появляются в `/help`.** Перезапусти Claude Code (`/quit` и заново) — скиллы подхватываются при старте сессии, `/clear` не помогает.

**`gpt-image-2` пишет «Обнови API», 401 или 429.** Проверь в `config.yaml`: в поле `key:` настоящий `sk-...`, а не `sk-REPLACE_ME`; баланс на [platform.openai.com/usage](https://platform.openai.com/usage) не нулевой; `endpoint:` — официальный `https://api.openai.com/v1` или твой прокси.

**`nano-banana` или `design` ругаются на Gemini.** Повтори `gemini auth login`. Если `gemini --version` не отвечает — переустанови CLI.

**Скилл со скриптами падает с «No such file».** Ты поставил набор плагином, а скрипт ищет себя в `~/.claude/skills/`. Поставь через `./install.sh` — это ровно тот случай, ради которого он есть.

**Скилл не вызывается сам, хотя должен.** Сначала проверь `/doctor` — не обрезан ли листинг (см. раздел про листинг выше). Если не в этом дело, открой `~/.claude/skills/<имя>/SKILL.md` и посмотри `description:` — там должны быть триггеры под твою формулировку.

**Хочу добавить свой скилл в набор.** Положи папку в `skills/<имя>/` с файлом `SKILL.md` (frontmatter: `name`, `description`). Заработает сразу.

---

## Что НЕ входит (специально)

В `~/.claude/skills/` у меня есть ещё скиллы, но они не дизайнерские и в набор не положены: `seo-*` (SEO-аудит, schema, sitemaps), `paid-ads` / `ad-creative` / `ad-operations` (реклама), `copywriting` / `cold-email` / `email-sequence`, `research*`, скиллы личного workflow (`save`, `work`). Понадобится что-то из этого — скажи, соберу отдельным пакетом.

Ещё: `product-card-image` и часть примеров в `gpt-image-2/SKILL.md` завязаны на проект LEINOS (пути к файлам на моей машине). Это только примеры команд — на работу скиллов у тебя они не влияют.

---

## Версии

- **v1.2.0** (август 2026) — большая перестройка по итогам аудита вызовов за 90 дней (19 из 29 дизайн-скиллов не вызывались ни разу):
  - `taste-skill` стал базовым билдером вместо `frontend-design`; правило «один базовый скилл на задачу»;
  - `animate` и `overdrive` убраны, вместо них motion-ось из 4 скиллов: `emil-design-eng`, `apple-design`, `animation-vocabulary`, `review-animations`;
  - в `critique` и `polish` вшит скриншот-гейт: рендер на 390 / 768 / 1440 px и сравнение, а не оценка по коду;
  - `banner-design` убран — его работу делят `gpt-image-2` (с текстом) и `nano-banana` (без);
  - починены битые ссылки: `critique` и `bolder` роутили анимации на удалённый `animate`;
  - добавлен `install.sh` и раздел про бюджет листинга скиллов.
- **v1.1.1** (май 2026) — у `nano-banana` убран overtrigger «REQUIRED for all image generation», добавлены явные negative triggers с передачей в `gpt-image-2`.
- **v1.1.0** (май 2026) — убран `canva`, добавлен `gpt-image-2`, перенастроена routing-table между двумя движками картинок.
- **v1.0.0** (май 2026) — первая сборка, 33 скилла.

Автор: Oleg. Лицензия: используй как хочешь, без гарантий.
