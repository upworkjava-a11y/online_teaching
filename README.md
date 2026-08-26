# Data Analytics Akademiyasi

Production-oriented Django platform for learning Data Analytics. The first live course is **SQL**, with Uzbek student-facing content, a real SQL sandbox, homework review, and teacher analytics.

## What is implemented

- Register, login, logout, and Google account sign-in
- Published/hidden courses, modules, and lectures
- Per-user allow/block access control enforced in views
- Lecture progress and continue-learning
- Interactive SQL exercises with Monaco editor
- Result-set validation (not SQL string comparison)
- Isolated SQL sandbox (never the production database)
- Homework upload, history, teacher/admin review
- Student dashboard and teacher analytics dashboard
- Django Admin for content, users, datasets, and access rules
- Sample Uzbek SQL content (3 published modules, 3 lectures and 3 exercises each)
- Docker Compose, Nginx, Gunicorn, Redis, PostgreSQL + sandbox PostgreSQL
- Automated test suite

## Project structure

```text
apps/
  accounts/     users, auth, profiles
  courses/      courses, modules, lectures, enrollments
  access/       per-user content allow/block
  progress/     lecture/course progress
  sandbox/      SQL security, executor, comparison
  exercises/    exercises, attempts, expected results
  homework/     assignments, submissions, reviews
  learning/     lecture pages
  dashboard/    student dashboard
  analytics/    teacher dashboard
  core/         health check, bootstrap
config/         Django settings
templates/      Uzbek UI
docker/         Nginx + sandbox init
tests/          automated tests
```

## How to run locally without Docker

Python 3.12 is enough for local development. SQLite is used for both Django and the SQL sandbox.

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements\development.txt
copy .env.example .env
$env:DJANGO_SETTINGS_MODULE="config.settings.local"
python manage.py migrate
python manage.py bootstrap_platform
python manage.py runserver
```

Open http://127.0.0.1:8000

## How to run locally with Docker

```bash
copy .env.example .env
docker compose up --build
```

Open http://localhost

## Docker commands

```bash
docker compose up --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py bootstrap_platform
docker compose exec web python manage.py test tests --settings=config.settings.test
docker compose exec web python manage.py check --deploy --settings=config.settings.production
docker compose -f docker-compose.prod.yml up --build -d
```

## Environment variables

See `.env.example`. Important groups:

- `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`
- Production PostgreSQL: `POSTGRES_*`
- SQL sandbox PostgreSQL: `SANDBOX_*` (must be a separate database)
- `REDIS_URL`
- Google OAuth: `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_OAUTH_REDIRECT_URI`

## Google account registration

1. Open [Google Cloud Console](https://console.cloud.google.com/apis/credentials).
2. Create an OAuth client of type **Web application**.
3. Add authorized JavaScript origins:
   - `http://127.0.0.1:8000`
   - `http://localhost:8000`
4. Add authorized redirect URIs:
   - `http://127.0.0.1:8000/accounts/google/callback/`
   - `http://localhost:8000/accounts/google/callback/`
5. Put the client ID and secret into `.env`:

```text
GOOGLE_CLIENT_ID=your-client-id
GOOGLE_CLIENT_SECRET=your-client-secret
GOOGLE_OAUTH_REDIRECT_URI=http://127.0.0.1:8000/accounts/google/callback/
```

6. Restart the server. Login and register pages show Google’s account list. Choosing an account logs the user in or creates a student account. No extra form is required.

Never commit a real `.env`.

## Default accounts after bootstrap

| Role | Email | Password |
| --- | --- | --- |
| Admin | `admin@example.com` | `ChangeMeNow123!` |
| Teacher | `teacher@example.com` | `TeacherPass123!` |
| Student | `student@example.com` | `StudentPass123!` |

Change these immediately outside local development.

## Deploy to PythonAnywhere

Step-by-step: see **[DEPLOY_PYTHONANYWHERE.md](DEPLOY_PYTHONANYWHERE.md)**.

Quick idea:
- Local coding → `config.settings.local` + `run.bat`
- Live site → `config.settings.pythonanywhere` + SQLite (free tier OK)
- After content updates: `git pull` then `bash scripts/pa_update.sh` and **Reload** the web app

## Tests

```bash
python manage.py test tests --settings=config.settings.test
```

## Remaining limitations / roadmap

- Excel, Power BI, Statistics, Python courses exist in the DB but are marked **Hozir jarayonda** for students until you open them in `OPEN_COURSE_SLUGS`
- Keep adding lectures/exercises via content modules + `bootstrap_platform` (idempotent)
- Notifications are stored as event hooks only
- Tailwind is loaded from CDN; compile it into the asset pipeline before a heavy public launch
- Celery is not included because the current MVP has no required background jobs
