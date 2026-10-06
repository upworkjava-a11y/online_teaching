# Gamification design — Code With Me (from pa_platform / pa_sandbox dumps)

## 1. Database structure (source of truth)

### `pa_platform (3).sqlite3` — learning platform
| Signal | Table / field | Notes |
|--------|----------------|-------|
| Users | `accounts_user` | 36 users (33 students) |
| Courses | `courses_course` | sql, english-banking, english-it, russian-it, python (+ excel etc.) |
| Topics | `courses_module` | Real SQL topics via module slugs |
| Lessons | `courses_lecture` + `progress_lectureprogress` | 167 progress rows |
| Puzzles/tests | `exercises_exercise` | kind=sql\|quiz, difficulty, is_skill_test |
| Submissions | `exercises_exerciseattempt` | 1855 rows; is_correct; sql_query; timestamps |
| Streaks | `progress_studentstreak` | 17 rows |
| Certificates | `progress_certificate` | 38 |
| Ranking input | distinct correct attempts × difficulty | Existing leaderboard |

### `pa_sandbox (3).sqlite3` — SQL practice datasets only
LeetCode-style tables (`customers`, `transactions`, …). **Not** used for achievements.

### Relationship
```
User → Course → Module (topic) → Lecture / Exercise → ExerciseAttempt → is_correct
                                                      → StudentStreak / certificates
```

## 2. Available learning signals
- Distinct correct solves (`is_correct=1`, prefer `is_skill_test=0` for “puzzles”)
- Difficulty: easy / medium / hard
- Topic via **module slug** (SQL: joins, ctes, window-functions, …)
- Lessons completed (`LectureProgress.completed`)
- Streak days (existing + activity dates from attempts)
- Course affiliation via `exercise.module.course.slug`
- **No** separate topic tag table — modules are topics

## 3. Real usage snapshot
- Correct attempts: 857; distinct (user,exercise) solves: 764
- Almost all activity is **SQL** (829 correct); Banking English: 28; Python/Dev*: ~0 in this dump
- SQL modules (non-skill puzzles): asoslari, filtrlash, agregatsiyalar, group-by-having, joins, subqueries, ctes, case, date-time, window-functions, advanced-sql
- Top solvers: 192 / 176 / 144 distinct exercises

## 4. Architecture decision
**Extend existing `apps.badges`** (Badge + UserBadge + catalog + metrics + evaluate on solve).  
Do **not** create a second Achievement app or a competing XP ladder.

- Ranking points already = difficulty-weighted distinct solves → treat as XP display, no farmable second currency.
- Activity = correct solve or completed lesson (not page views).
- Skill tests excluded from “puzzle” counts; language courses may count quizzes via course_slug meta.

## 5. Proposed achievements (implemented)

| Achievement | Category | Module | Requirement | Data Source |
| ----------- | -------- | ------ | ----------- | ----------- |
| First Step … Challenge Hunter | Problem | all | 1/10/25/50 puzzles | distinct correct, `is_skill_test=0` |
| Century Coder | Problem | all | 100 puzzles | same |
| Easy / Medium / Hard * | Problem | all | 25 / 15 / 3 by difficulty | `exercise.difficulty` |
| SELECT / JOIN / GROUP / Subquery / CTE / CASE / Window | Mastery | SQL | 5 topic puzzles | `courses_module.slug` map |
| SQL Solver / Master | Mastery | SQL | 25 / 50 course puzzles | course slug `sql` |
| Banking / DevEN / DevRU Starter | Learning | lang | 10 correct (incl. quizzes) | course slug + skill tests |
| Python Starter / Solver | Mastery | Python | 5 / 15 | python course |
| Multi-Skilled / Polyglot | Platform | cross | 2 / 3 courses with ≥5 solves | course aggregates |
| Streaks 3/7/14/30 | Consistency | — | longest streak | `StudentStreak` |
| Lessons / Course Finisher | Learning | — | lessons / full course | `LectureProgress` |
| Top 10/3/#1 | Competition | — | historical best rank | leaderboard + `UserRankPeak` |
| Legend | Platform | — | 20 other badges | `UserBadge` count |

## 6. Explicitly NOT building (data doesn't justify)
- Separate XP currency (leaderboard points already = difficulty-weighted unique solves)
- Daily “minutes practiced” goals (no duration field)
- Sandbox-table-based achievements (sandbox DB has no user progress)

## 7. Commands
```bash
python manage.py import_pa_backup --platform "…/pa_platform (3).sqlite3" --sandbox "…/pa_sandbox (3).sqlite3"
python manage.py sync_achievements
```
