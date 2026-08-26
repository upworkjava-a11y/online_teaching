from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

load_dotenv(ROOT / ".env")

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    os.environ.get("DJANGO_SETTINGS_MODULE") or "config.settings.local",
)

import django

django.setup()

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
WEB_URL = os.environ.get("PLATFORM_WEB_URL", "http://127.0.0.1:8000").rstrip("/")
