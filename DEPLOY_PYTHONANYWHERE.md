# PythonAnywhere deploy guide

This project is set up so you can:
1. Deploy the current SQL-ready platform to PythonAnywhere
2. Keep coding locally (new courses, features)
3. Re-deploy safely with `git pull` + migrate + bootstrap + collectstatic

Local day-to-day work stays on `config.settings.local` (`run.bat`).  
Production on PA uses `config.settings.pythonanywhere`.

---

## 0. Before you start

- PythonAnywhere account (free Beginner is OK for SQLite)
- Project on GitHub/GitLab **or** upload a zip
- Do **not** commit `.env` or sqlite DB files

---

## 1. Upload the code

### Option A — Git (recommended for ongoing updates)

In a PythonAnywhere **Bash** console:

```bash
cd ~
git clone https://github.com/upworkjava-a11y/online_teaching.git My-online-platform
cd My-online-platform
```

### Option B — Zip upload

Upload a zip in the **Files** tab, then unzip into `/home/YOUR_USERNAME/My-online-platform`.

---

## 2. Virtualenv + packages

```bash
cd ~/My-online-platform
python3.12 -m venv .venv
# If 3.12 is missing, use python3.10 or whatever PA offers:
# python3.10 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements/pythonanywhere.txt
```

---

## 3. Environment file

```bash
cd ~/My-online-platform
cp .env.pythonanywhere.example .env
nano .env
```

Change at least:
- `SECRET_KEY` (long random string)
- `ALLOWED_HOSTS` / `CSRF_TRUSTED_ORIGINS` (`YOUR_USERNAME.pythonanywhere.com`)
- Admin bootstrap password

Leave `PYTHONANYWHERE_USE_MYSQL=0` for the first deploy (SQLite).

---

## 4. Database + content seed

```bash
cd ~/My-online-platform
source .venv/bin/activate
export DJANGO_SETTINGS_MODULE=config.settings.pythonanywhere
python manage.py migrate
python manage.py bootstrap_platform
python manage.py collectstatic --noinput
```

`bootstrap_platform` is safe to re-run later when you add SQL lessons / mashqlar.

Demo accounts after bootstrap (change them):

| Role | Email | Password |
| --- | --- | --- |
| Admin | admin@example.com | ChangeMeNow123! |
| Teacher | teacher@example.com | TeacherPass123! |
| Student | student@example.com | StudentPass123! |

---

## 5. Web app (WSGI)

Open **Web** → **Add a new web app** → Manual configuration → your Python version.

### Source code / Working directory

`/home/YOUR_USERNAME/My-online-platform`

### Virtualenv

`/home/YOUR_USERNAME/My-online-platform/.venv`

### WSGI file

Replace the file contents with (edit the path + username):

```python
import os
import sys

project_home = "/home/YOUR_USERNAME/My-online-platform"
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.pythonanywhere")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Static files (Web tab → Static files)

| URL | Directory |
| --- | --- |
| `/static/` | `/home/YOUR_USERNAME/My-online-platform/staticfiles` |
| `/media/` | `/home/YOUR_USERNAME/My-online-platform/media` |

WhiteNoise also serves `/static/` if the mapping is missing, but PA’s Static files mapping is preferred.

Click **Reload**.

Site: `https://YOUR_USERNAME.pythonanywhere.com`

---

## 6. After every content / code update

On your PC (local):

```powershell
# develop with run.bat / local settings
git add .
git commit -m "Describe the change"
git push
```

On PythonAnywhere Bash:

```bash
cd ~/My-online-platform
source .venv/bin/activate
git pull
pip install -r requirements/pythonanywhere.txt
export DJANGO_SETTINGS_MODULE=config.settings.pythonanywhere
python manage.py migrate
python manage.py bootstrap_platform
python manage.py collectstatic --noinput
```

Then **Web → Reload**.

This workflow is what you’ll use when adding Excel/Python content and new features later.

---

## 7. Optional: MySQL later

1. Create a MySQL database in the PA dashboard  
2. In `.env` set `PYTHONANYWHERE_USE_MYSQL=1` and MySQL credentials  
3. `pip install mysqlclient` (or PyMySQL)  
4. `migrate` + `bootstrap_platform` again  

SQL sandbox stays on **separate** `pa_sandbox.sqlite3` either way.

---

## 8. Google OAuth on the live site

In Google Cloud Console add:

- Origin: `https://YOUR_USERNAME.pythonanywhere.com`
- Redirect: `https://YOUR_USERNAME.pythonanywhere.com/accounts/google/callback/`

Update `.env` `GOOGLE_*` values and reload.

---

## 9. Troubleshooting

| Problem | Fix |
| --- | --- |
| DisallowedHost | Fix `ALLOWED_HOSTS` in `.env`, reload |
| CSRF failed | Fix `CSRF_TRUSTED_ORIGINS` to `https://...` |
| Static CSS missing | `collectstatic` + Static files mapping + Reload |
| Homework download 404 | Map `/media/` or keep `SERVE_MEDIA=True` |
| SECRET_KEY error | Set a non-default `SECRET_KEY` in `.env` |
| ImportError argon2 | `pip install -r requirements/pythonanywhere.txt` |

Error logs: **Web** → Log files → Error log.

---

## 10. What stays local vs production

| | Local (`run.bat`) | PythonAnywhere |
| --- | --- | --- |
| Settings | `config.settings.local` | `config.settings.pythonanywhere` |
| DB | `local_platform.sqlite3` | `pa_platform.sqlite3` |
| Sandbox | `local_sandbox.sqlite3` | `pa_sandbox.sqlite3` |
| Purpose | Build courses & features | Public students / teachers |

Never copy local `.env` with `DEBUG=True` to production.
