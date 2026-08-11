#!/usr/bin/env bash
# design-kit — установка скиллов напрямую в ~/.claude/skills/
#
# Зачем этот скрипт, если есть /plugin marketplace add:
# часть скиллов (gpt-image-2, nano-banana, design, brand-setup) запускает
# свои python/node-скрипты по пути ~/.claude/skills/<имя>/scripts/...
# При установке плагином файлы лежат в другом месте и эти пути не находятся.
# Копия в ~/.claude/skills/ делает все скиллы рабочими без правок.
#
# Использование:
#   ./install.sh            — поставить, не трогая уже существующие скиллы с теми же именами
#   ./install.sh --force    — перезаписать, сделав бэкап старых в ~/.claude/skill-backups/

set -euo pipefail

SRC="$(cd "$(dirname "$0")" && pwd)/skills"
DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
BACKUP="$HOME/.claude/skill-backups/design-kit-$(date +%Y%m%d-%H%M%S)"
FORCE=0
[ "${1:-}" = "--force" ] && FORCE=1

if [ ! -d "$SRC" ]; then
  echo "Не найдена папка skills/ рядом со скриптом ($SRC). Запускай install.sh из корня design-kit." >&2
  exit 1
fi

mkdir -p "$DEST"

installed=0
skipped=0
replaced=0

for dir in "$SRC"/*/; do
  name="$(basename "$dir")"
  target="$DEST/$name"

  if [ -d "$target" ]; then
    if [ "$FORCE" -eq 1 ]; then
      mkdir -p "$BACKUP"
      mv "$target" "$BACKUP/$name"
      cp -R "$dir" "$target"
      replaced=$((replaced + 1))
      echo "  заменён:  $name (старый → $BACKUP/$name)"
    else
      skipped=$((skipped + 1))
      echo "  пропущен: $name — уже есть в $DEST (перезаписать: ./install.sh --force)"
    fi
  else
    cp -R "$dir" "$target"
    installed=$((installed + 1))
    echo "  поставлен: $name"
  fi
done

echo
echo "Итог: поставлено $installed, заменено $replaced, пропущено $skipped → $DEST"

if [ -f "$DEST/gpt-image-2/config.yaml.example" ] && [ ! -f "$DEST/gpt-image-2/config.yaml" ]; then
  echo
  echo "Ещё один шаг для gpt-image-2 (генерация картинок через OpenAI):"
  echo "  cp $DEST/gpt-image-2/config.yaml.example $DEST/gpt-image-2/config.yaml"
  echo "  затем открой config.yaml и замени sk-REPLACE_ME на свой ключ OpenAI."
  echo "  Не нужен OpenAI — просто удали: rm -rf $DEST/gpt-image-2"
fi

echo
echo "Перезапусти Claude Code — скиллы подхватываются при старте сессии."
