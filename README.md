# Banking System — Learning Project

A toy banking terminal app evolved into a full web application, used as a vehicle to learn software layers from the ground up.

## Goal

Start with a working Python terminal app and progressively add layers:
**terminal → tested code → REST API → frontend → deployment**

Each phase teaches a real concept. Nothing is skipped.

## Current State

Phases 1–4 complete:

- Python business logic with SQLite persistence
- Full pytest test suite (unit + integration)
- REST API built with Flask
- Vanilla HTML/CSS/JS frontend

## Project Structure

```
banking_system/
├── account.py          # BankAccount model
├── database.py         # SQLite persistence layer
├── utils.py            # Validation and hashing helpers
├── api.py              # Flask REST API + entry point
├── templates/
│   └── index.html      # Frontend HTML
├── static/
│   ├── style.css
│   └── app.js          # Frontend logic (fetch API)
├── tests/
│   ├── conftest.py     # Shared fixtures
│   ├── test_account.py
│   ├── test_utils.py
│   └── test_database.py
├── old_files/          # Archived terminal UI (app.py, main.py)
├── README.md
└── TODO.md
```

## How to Run

```bash
python api.py
```

Then open `http://127.0.0.1:5000/app` in your browser.

## How to Run Tests

```bash
pytest
```

## Known Limitations

- Sessions are in-memory (`active_sessions` dict) — tokens never expire and are lost on server restart. JWT planned for Phase 5.
- Passwords hashed with SHA-256 — bcrypt planned for Phase 5.

## Learning Path

See [TODO.md](TODO.md) for the full phased roadmap.
