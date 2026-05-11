"""Shared client for the gpt-image-2 skill.

- Loads endpoint + key from ~/.claude/skills/gpt-image-2/config.yaml
- Builds an OpenAI-compatible client (works with any base_url proxy)
- Detects credit/auth failures and prints a Russian-language message telling
  the user to update config.yaml (endpoint + key)

Imported by generate.py / edit.py / build_deck.py.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import yaml
from openai import OpenAI, APIStatusError, AuthenticationError

SKILL_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = SKILL_DIR / "config.yaml"


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        die(
            f"Конфиг не найден: {CONFIG_PATH}\n"
            "Создай файл с полями api.endpoint и api.key — см. presets/leinos-brand.yaml как пример."
        )
    with CONFIG_PATH.open("r") as f:
        cfg = yaml.safe_load(f) or {}
    if not cfg.get("api", {}).get("endpoint") or not cfg.get("api", {}).get("key"):
        die(
            f"В {CONFIG_PATH} нет api.endpoint или api.key.\n"
            "Заполни оба поля и попробуй снова."
        )
    return cfg


def build_client(cfg: dict | None = None) -> OpenAI:
    cfg = cfg or load_config()
    return OpenAI(
        api_key=cfg["api"]["key"],
        base_url=cfg["api"]["endpoint"],
        timeout=600.0,
        max_retries=2,
    )


# ----- credit / auth failure detection ------------------------------------

CREDIT_KEYWORDS = (
    "insufficient_quota", "insufficient quota", "quota exceeded",
    "balance", "credits", "out of credit", "no credit",
    "exceeded", "expired", "deactivated",
    "unauthorized", "invalid api key", "invalid_api_key",
    "billing", "payment",
)


def is_credit_or_auth_error(err: Exception) -> bool:
    if isinstance(err, AuthenticationError):
        return True
    if isinstance(err, APIStatusError):
        if err.status_code in (401, 402, 403, 429):
            return True
    msg = str(err).lower()
    return any(k in msg for k in CREDIT_KEYWORDS)


def die_credit_exhausted(err: Exception) -> None:
    print("", file=sys.stderr)
    print("⚠️  GPT Image 2 не отвечает — похоже на закончившийся ключ или баланс.", file=sys.stderr)
    print("", file=sys.stderr)
    print(f"   Ошибка: {err}", file=sys.stderr)
    print("", file=sys.stderr)
    print(f"   Обнови API: открой {CONFIG_PATH}", file=sys.stderr)
    print("   и замени api.endpoint и api.key на новые. Скилл перечитает config", file=sys.stderr)
    print("   при следующем запуске — рестарт не нужен.", file=sys.stderr)
    print("", file=sys.stderr)
    sys.exit(2)


def die(msg: str) -> None:
    print(f"❌ {msg}", file=sys.stderr)
    sys.exit(1)


def call_safely(fn, *args, **kwargs):
    """Run an OpenAI client call, intercept credit/auth failures with friendly message."""
    try:
        return fn(*args, **kwargs)
    except Exception as e:
        if is_credit_or_auth_error(e):
            die_credit_exhausted(e)
        raise


# ----- self-test -----------------------------------------------------------

def healthcheck() -> int:
    """Smoke-test the endpoint with a tiny model list / cheap call. Returns 0 if OK."""
    cfg = load_config()
    client = build_client(cfg)
    try:
        # Models list is the cheapest valid request supported by most OpenAI-compatible proxies.
        models = client.models.list()
        names = sorted({m.id for m in models.data})[:10]
        print(f"✅ endpoint OK: {cfg['api']['endpoint']}")
        print(f"   ключ: ...{cfg['api']['key'][-6:]}")
        print(f"   модели (первые 10): {', '.join(names) if names else '(нет)'}")
        return 0
    except Exception as e:
        if is_credit_or_auth_error(e):
            die_credit_exhausted(e)
        print(f"❌ endpoint не ответил: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(healthcheck())
