@echo off
cd /d "%~dp0"
set DJANGO_SETTINGS_MODULE=config.settings.local
if not exist ".venv\Scripts\python.exe" (
  echo Virtualenv topilmadi.
  pause
  exit /b 1
)
echo Telegram bot ishga tushmoqda...
echo To'xtatish: Ctrl+C
echo.
".venv\Scripts\python.exe" -m telegram_bot.bot
if errorlevel 1 pause
