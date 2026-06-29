"""
Adeyemi Oluwaseyi Alao — portfolio.

A small Flask app that serves the portfolio page (content driven by data.py)
and handles a working contact form: messages are validated, saved to a SQLite
database, and — if email is configured in .env — forwarded to your inbox.

Run locally:
    python app.py
then open http://127.0.0.1:5000
"""
import json
import os
import re
import sqlite3
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from flask import (
    Flask, abort, flash, jsonify, redirect, render_template, request, url_for,
)
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

import data

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "messages.db"

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-only-insecure-key")
csrf = CSRFProtect(app)


# --------------------------------------------------------------------------- #
# Contact form
# --------------------------------------------------------------------------- #
class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=120)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=200)])
    message = TextAreaField(
        "Message", validators=[DataRequired(), Length(min=10, max=4000)]
    )


# --------------------------------------------------------------------------- #
# Database (plain sqlite3 — no extra dependency)
# --------------------------------------------------------------------------- #
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS messages (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                name      TEXT    NOT NULL,
                email     TEXT    NOT NULL,
                message   TEXT    NOT NULL,
                created_at TEXT   NOT NULL
            )
            """
        )


def save_message(name, email, message):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO messages (name, email, message, created_at) "
            "VALUES (?, ?, ?, ?)",
            (name, email, message, datetime.now(timezone.utc).isoformat()),
        )


# --------------------------------------------------------------------------- #
# Email notification via Web3Forms (HTTPS — works on hosts that block SMTP).
# Best-effort: failures never break the form. Set WEB3FORMS_ACCESS_KEY in the
# host's environment (get a free key at https://web3forms.com).
# --------------------------------------------------------------------------- #
def send_notification(name, email, message):
    access_key = os.environ.get("WEB3FORMS_ACCESS_KEY")
    if not access_key:
        return False  # not configured — message is still saved to the DB

    payload = json.dumps({
        "access_key": access_key,
        "subject": f"Portfolio contact — {name}",
        "from_name": "Portfolio contact form",
        "name": name,
        "email": email,
        "replyto": email,
        "message": message,
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.web3forms.com/submit",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            # Web3Forms is behind Cloudflare, which 403s the default
            # "Python-urllib" agent — present a normal browser UA.
            "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/120.0.0.0 Safari/537.36"),
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            if body.get("success"):
                return True
            app.logger.warning("Web3Forms rejected the message: %s", body)
            return False
    except Exception as exc:  # noqa: BLE001 — log and carry on
        app.logger.warning("Email notification failed: %s", exc)
        return False


# --------------------------------------------------------------------------- #
# Routes
# --------------------------------------------------------------------------- #
@app.route("/")
def index():
    form = ContactForm()
    return render_template(
        "index.html",
        form=form,
        profile=data.PROFILE,
        metrics=data.METRICS,
        about=data.ABOUT_PARAGRAPHS,
        focus=data.FOCUS_AREAS,
        projects=data.PROJECTS,
        experience=data.EXPERIENCE,
        skills=data.SKILLS,
        education=data.EDUCATION,
        certifications=data.CERTIFICATIONS,
        year=datetime.now().year,
    )


@app.route("/work/<slug>")
def work_detail(slug):
    projects = data.PROJECTS
    idx = next((i for i, p in enumerate(projects) if p["slug"] == slug), None)
    if idx is None:
        abort(404)
    return render_template(
        "project.html",
        profile=data.PROFILE,
        p=projects[idx],
        prev=projects[idx - 1] if idx > 0 else None,
        next=projects[idx + 1] if idx < len(projects) - 1 else None,
        year=datetime.now().year,
    )


@app.errorhandler(404)
def not_found(_e):
    return render_template("404.html", profile=data.PROFILE), 404


@app.route("/contact", methods=["POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        save_message(form.name.data, form.email.data, form.message.data)
        send_notification(form.name.data, form.email.data, form.message.data)
        flash("Thanks — your message landed. I'll get back to you soon.", "success")
    else:
        flash("Please check the form — some fields need attention.", "error")
        # Re-render with field errors instead of losing them on redirect.
        return render_template(
            "index.html",
            form=form,
            profile=data.PROFILE,
            metrics=data.METRICS,
            about=data.ABOUT_PARAGRAPHS,
            focus=data.FOCUS_AREAS,
            projects=data.PROJECTS,
            experience=data.EXPERIENCE,
            skills=data.SKILLS,
            education=data.EDUCATION,
            certifications=data.CERTIFICATIONS,
            year=datetime.now().year,
        ), 400
    return redirect(url_for("index") + "#contact")


# --------------------------------------------------------------------------- #
# "Ask about Adeyemi" assistant — rule-based, answers from data.py
# --------------------------------------------------------------------------- #
def _match_project(msg):
    """Pick the project whose slug words best match the message."""
    best, best_key = None, (0, 0.0)
    for pr in data.PROJECTS:
        kws = [k for k in pr["slug"].split("-") if len(k) >= 4]
        hits = sum(1 for k in kws if k in msg)
        if not hits:
            continue
        key = (hits, hits / len(kws))
        if key > best_key:
            best, best_key = pr, key
    return best


def _find_skill(msg):
    for heading, items in data.SKILLS:
        for item in items:
            if item.lower() in msg:
                return item, heading
    return None


def bot_reply(message):
    msg = " ".join(message.lower().split())
    tokens = set(re.findall(r"[a-z0-9+#.]+", msg))
    p = data.PROFILE

    def has(*w):
        return any(x in msg for x in w)

    def word(*w):
        return any(x in tokens for x in w)

    if not msg:
        return ("Ask me about Adeyemi's skills, projects, experience, education, "
                "or how to get in touch.")
    if word("hi", "hello", "hey", "hiya") or has("good morning", "good afternoon", "good evening"):
        return ("Hi! I'm Adeyemi's portfolio assistant. Ask me about his skills, "
                "projects, experience, education, or how to reach him.")

    # a specific project
    proj = _match_project(msg)
    if proj:
        unit = proj["metric_unit"]
        return (f"{proj['title']} — {proj['desc']} "
                f"({proj['metric']}{unit} · {proj['metric_label']}). "
                f"Full case study: /work/{proj['slug']}")

    # contact / hiring
    if has("contact", "email", "reach", "get in touch", "mail", "hire", "recruit"):
        return (f"You can reach Adeyemi by email at {p['email']} or phone "
                f"{p['phone_display']}. He's based in {p['location']} and is open "
                "to AI/ML, data science, full-stack, and teaching roles.")
    if has("phone", "call"):
        return f"Adeyemi's phone number is {p['phone_display']}."
    if has("location", "based", "where is he", "where does he", "country", "city", "relocat"):
        return f"Adeyemi is based in {p['location']}."
    if has("available", "availability", "open to", "looking for", "roles", "freelance", "remote", "opportunit"):
        return ("Adeyemi is open to AI/ML engineering, data science, and full-stack "
                f"roles, plus teaching and collaboration. The fastest way to reach "
                f"him is email: {p['email']}.")

    # projects overview
    if has("project", "portfolio", "built", "build", "made", "case study", "what has he"):
        titles = ", ".join(pr["title"] for pr in data.PROJECTS)
        return ("Adeyemi's selected projects: " + titles + ". Ask about any one for "
                "details — e.g. 'tell me about the sign-language project'.")

    # skills overview
    if has("skill", "stack", "tool", "framework", "proficient", "technolog", "good at", "what can he"):
        cats = "; ".join(f"{h}: {', '.join(items)}" for h, items in data.SKILLS)
        return "Adeyemi's toolkit — " + cats

    # specific tech
    tech = _find_skill(msg)
    if tech:
        return f"Yes — Adeyemi works with {tech[0]} (part of his {tech[1]} skills)."

    # domains
    if has("computer vision", "vision", "image"):
        return ("Computer vision is a core focus — a Vision Transformer for "
                "sign-language recognition (96%) and CNN-based emotion recognition (84%).")
    if has("nlp", "language model", "chatbot", "llm", "natural language"):
        return ("On NLP: an AI chatbot (OpenAI API + Hugging Face Transformers) and a "
                "spam-email detection classifier (~98%).")

    # experience
    if has("experience", "work history", "worked", "career", "background", "employ", "where has he"):
        lines = [f"• {j['role'].replace('&amp;', '&')} — "
                 f"{j['org'].replace('&amp;', '&')} ({j['when']})"
                 for j in data.EXPERIENCE]
        return "Adeyemi's experience:\n" + "\n".join(lines)
    if has("teach", "mentor", "train", "educator", "3mtt", "student", "learner"):
        return ("Adeyemi is also an educator — through Nigeria's 3MTT program he's "
                "trained 250+ learners in data science and AI, mentoring hands-on "
                "Agile projects.")
    if has("how long", "years of experience", "years experience", "how many years"):
        return ("Adeyemi has 8+ years in tech — spanning front-end and design, and "
                "now AI/ML and data science.")

    # education
    if has("education", "degree", "study", "studied", "school", "university", "academic", "qualification"):
        lines = [f"• {t} — {pl} ({yr})" for yr, t, pl in data.EDUCATION]
        return "Education:\n" + "\n".join(lines)
    if has("cert", "certificate"):
        lines = [f"• {t} — {pl} ({yr})" for yr, t, pl in data.CERTIFICATIONS]
        return "Certifications:\n" + "\n".join(lines)

    # bio / who
    if has("who is", "about adeyemi", "about him", "tell me about", "summary", "introduce", "bio", "himself"):
        return p["lede"]

    if has("help", "menu", "what can you", "what can i ask", "options"):
        return ("You can ask about: who Adeyemi is, his skills, his projects (and "
                "details of each), work experience, education, teaching, and how to "
                "contact or hire him.")
    if word("thanks", "thank") or "thank you" in msg:
        return "You're welcome! Anything else about Adeyemi?"
    if word("bye", "goodbye"):
        return f"Thanks for stopping by — reach Adeyemi at {p['email']}."

    return ("I can tell you about Adeyemi's skills, projects, experience, "
            "education, teaching, or how to get in touch. What would you like to know?")


@app.route("/chat", methods=["POST"])
@csrf.exempt  # read-only: returns info to the page, changes no state
def chat():
    payload = request.get_json(silent=True) or {}
    message = str(payload.get("message", ""))[:500]
    return jsonify(reply=bot_reply(message))


init_db()

if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    app.run(debug=debug, port=5000)
