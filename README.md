# Adeyemi Oluwaseyi Alao — Portfolio

A Flask-powered personal portfolio with a working, database-backed contact form.

## What's inside

```
portfolio/
├── app.py              # Flask app: routes, SQLite, email notification
├── data.py             # ALL site content — edit this to update the page
├── templates/
│   └── index.html      # Jinja template (renders from data.py)
├── static/
│   ├── css/style.css   # styles
│   └── js/main.js      # scroll reveal + gauge animation
├── requirements.txt
├── .env.example        # copy to .env and fill in
└── messages.db         # auto-created on first run (git-ignored)
```

## Run it locally

```bash
# 1. (recommended) create a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux

# 2. install dependencies
pip install -r requirements.txt

# 3. set up environment
copy .env.example .env        # Windows  (cp on macOS/Linux)
#   then open .env and set a SECRET_KEY (any long random string)

# 4. run
python app.py
```

Open **http://127.0.0.1:5000**.

## The contact form

- Submissions are validated, then saved to `messages.db` (SQLite).
- If email is configured in `.env`, you also get an email notification.
  **Email is optional** — without it, messages are still saved.

### Enabling email (Gmail example)

1. Turn on 2-Step Verification on your Google account.
2. Create an **App Password** (Google Account → Security → App passwords).
3. In `.env`, set `MAIL_USERNAME` to your Gmail and `MAIL_PASSWORD` to the
   app password. `MAIL_TO` is where messages are delivered.

### Reading saved messages

```bash
python -c "import sqlite3; [print(r) for r in sqlite3.connect('messages.db').execute('SELECT created_at,name,email,message FROM messages ORDER BY id DESC')]"
```

## Project detail pages

Every project on the home page links to its own case-study page at
`/work/<slug>` (e.g. `/work/sign-language-recognition`). The content for each
lives in the `detail` block of that project in [`data.py`](data.py):

- `overview`, `problem`, `approach`, `results` — the write-up sections.
- `links` — list of `{"label", "url"}`. Leave `url` as `"#"` and it shows a
  muted "soon" chip until you paste a real GitHub / demo URL.
- `gallery` — image filenames to show on the page. Drop the files in
  `static/img/` and list their names here (empty list = no gallery).

Prev/next navigation between projects is automatic, based on their order in
`PROJECTS`.

## Updating your content

Everything is in [`data.py`](data.py) — projects, experience, skills,
education, metrics, contact details. Add a dict to `PROJECTS`, a job to
`EXPERIENCE`, etc., and it appears on the page automatically. No HTML editing
needed.

## Deploying later

This is structured to deploy cleanly on Render / Railway / PythonAnywhere.
When ready, add a `Procfile` (`web: gunicorn app:app`) and `gunicorn` to
requirements. Ask and I'll set it up.

> Note: the original single-file `index.html` is kept at the project root as a
> reference snapshot. The live app is served from `templates/index.html`.
