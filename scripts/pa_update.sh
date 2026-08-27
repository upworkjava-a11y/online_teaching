#!/bin/bash
# Run on PythonAnywhere after git pull (Bash console).
# Usage:
#   bash scripts/pa_update.sh              # safe: migrate + static only
#   RUN_BOOTSTRAP=1 bash scripts/pa_update.sh   # also re-seed content
#
# Do NOT run bootstrap on every deploy — it used to delete exercises and
# CASCADE-wipe student scores. Content seeding is optional now.

set -euo pipefail
cd "$(dirname "$0")/.."
source .venv/bin/activate
export DJANGO_SETTINGS_MODULE=config.settings.pythonanywhere

pip install -r requirements/pythonanywhere.txt
python manage.py migrate --noinput

if [ "${RUN_BOOTSTRAP:-0}" = "1" ]; then
  echo "Running bootstrap_platform (content seed)..."
  python manage.py bootstrap_platform
else
  echo "Skipping bootstrap_platform (set RUN_BOOTSTRAP=1 to seed/update content)."
fi

python manage.py collectstatic --noinput
echo "Done. Click Reload on the PythonAnywhere Web tab."
