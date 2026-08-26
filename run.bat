@echo off
cd /d "%~dp0"
set DJANGO_SETTINGS_MODULE=config.settings.local
if not exist ".venv\Scripts\python.exe" (
  echo Python virtualenv not found. Create it first:
  echo   py -3.12 -m venv .venv
  echo   .venv\Scripts\pip install -r requirements\development.txt
  pause
  exit /b 1
)
".venv\Scripts\python.exe" manage.py migrate --noinput
if errorlevel 1 (
  pause
  exit /b 1
)
echo.
echo Site: http://127.0.0.1:8000
echo.
".venv\Scripts\python.exe" manage.py runserver 127.0.0.1:8000
