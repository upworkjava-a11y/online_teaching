#!/bin/bash
# Run on PythonAnywhere after git pull (Bash console).
# Usage: bash scripts/pa_update.sh

set -euo pipefail
cd "$(dirname "$0")/.."
source .venv/bin/activate
export DJANGO_SETTINGS_MODULE=config.settings.pythonanywhere

pip install -r requirements/pythonanywhere.txt
python manage.py migrate --noinput
python manage.py bootstrap_platform
python manage.py collectstatic --noinput
echo "Done. Click Reload on the PythonAnywhere Web tab."
