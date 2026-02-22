# Banking System — Learning Project

A toy banking terminal app that evolves into a full web application, used as a vehicle to learn software layers from the ground up.

## Goal

Start with a working Python terminal app and progressively add layers:
**terminal → tested code → REST API → frontend → deployment**

Each phase teaches a real concept. Nothing is skipped.

## Current State

- Python terminal app
- SQLite persistence via `sqlite3`
- Basic account operations: deposit, withdrawal, history

## Project Structure

```
banking_system/
├── account.py      # BankAccount model
├── app.py          # Terminal UI / controller
├── database.py     # SQLite persistence layer
├── utils.py        # Validation and display helpers
├── main.py         # Entry point
├── README.md
└── TODO.md
```

## How to Run (Terminal)

```bash
python main.py
```

## Learning Path

See [TODO.md](TODO.md) for the full phased roadmap.
