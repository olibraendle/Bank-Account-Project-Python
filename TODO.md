# TODO — Banking System Learning Roadmap

Each phase builds on the last. Complete a phase before moving to the next.
Checkboxes are for tracking progress.

---

## Phase 1 — Fix the Foundation (Terminal App)

Fix known bugs and improve the core code before building on top of it.
Broken foundations make everything harder later.

- [ ] Hash passwords with `hashlib` (sha256) — never store plain text
- [ ] Fix DB connection leak in `db_updatebalance` (`cu.close()` → `cx.close()`)
- [ ] Fix mutable default argument in `BankAccount.__init__` (`account_history=None`)
- [ ] Replace bare `except: pass` with `except sqlite3.OperationalError: pass`
- [ ] Add `PRIMARY KEY` / `UNIQUE` constraint on `username` in DB schema
- [ ] Extract a single `init_db()` function — remove the repeated create-table blocks
- [ ] Fix the withdrawal logic (allow withdrawing exact balance)
- [ ] Fix the typo in `utils.py`: "invalid amount" → "valid amount"
- [ ] Rename `exit` variable in `app.py` (shadows built-in)
- [ ] Delete or clean up `db_test.py`
- [ ] Fix `check_amount` return type annotation (`-> float` should be `-> bool`)

**What you learn:** defensive programming, security basics, Python pitfalls

---

## Phase 2 — Testing

Before adding new layers, write tests to lock in correct behavior.
This protects you when you refactor for the web.

- [ ] Set up `pytest` (`pip install pytest`)
- [ ] Create a `tests/` directory
- [ ] Write unit tests for `BankAccount`
  - [ ] `test_deposit` — balance increases correctly
  - [ ] `test_withdrawal` — balance decreases correctly
  - [ ] `test_withdrawal_insufficient_funds` — blocked correctly
  - [ ] `test_history_records_correctly`
- [ ] Write unit tests for `utils.py` validation functions
  - [ ] `test_check_amount_negative`
  - [ ] `test_check_amount_valid`
  - [ ] `test_check_amountwithdrawal_over_balance`
- [ ] Write integration tests for `database.py` using a temporary in-memory DB (`:memory:`)
  - [ ] `test_insert_and_fetch_user`
  - [ ] `test_password_check`
  - [ ] `test_update_balance`
  - [ ] `test_duplicate_username_rejected`
- [ ] Make sure all tests pass with `pytest tests/`

**What you learn:** pytest, unit vs integration tests, test isolation, TDD mindset

---

## Phase 3 — REST API (Backend Web Layer)

Turn the terminal app into an HTTP API. This is the most important phase —
it teaches how the web actually works under the hood.

- [ ] Learn the basics first (read / watch):
  - [ ] What is HTTP? (methods: GET, POST, PUT, DELETE; status codes: 200, 400, 401, 404)
  - [ ] What is JSON and why APIs use it
  - [ ] What is a REST API?
- [ ] Install Flask (`pip install flask`)
- [ ] Create `api.py` — a Flask app with these endpoints:

  | Method | Route | Description |
  |--------|-------|-------------|
  | POST | `/register` | Create a new account |
  | POST | `/login` | Authenticate, return session token |
  | GET | `/balance` | Get current balance (auth required) |
  | POST | `/deposit` | Deposit money (auth required) |
  | POST | `/withdraw` | Withdraw money (auth required) |
  | GET | `/history` | Get transaction history (auth required) |

- [ ] Return proper JSON responses and HTTP status codes
- [ ] Add simple token-based auth (generate a token on login, require it on protected routes)
- [ ] Test your API manually with `curl` or Postman/Insomnia
- [ ] Write API tests using `pytest` + `flask.testing.FlaskClient`

**What you learn:** HTTP, REST, Flask routing, request/response cycle, JSON, basic auth

---

## Phase 4 — Frontend (What the User Sees)

Build a simple HTML/CSS/JS frontend that talks to your API.
No frameworks — vanilla only. This teaches you what React/Vue are actually replacing.

- [ ] Learn the basics first:
  - [ ] How browsers render HTML
  - [ ] What the DOM is
  - [ ] How CSS styles elements
  - [ ] How JavaScript interacts with the DOM
- [ ] Create a `static/` or `frontend/` folder
- [ ] Build these pages as plain `.html` files:
  - [ ] `login.html` — login form
  - [ ] `register.html` — registration form
  - [ ] `dashboard.html` — shows balance, deposit/withdraw forms, history
- [ ] Use the `fetch()` API in JavaScript to call your Flask backend
- [ ] Handle API errors and show them to the user (wrong password, insufficient funds, etc.)
- [ ] Serve the frontend from Flask using `static_folder`

**What you learn:** HTML, CSS, DOM manipulation, `fetch`, async/await, frontend ↔ backend communication

---

## Phase 5 — Security Hardening

Once it works, make it safer. Security is a layer, not an afterthought.

- [ ] Replace raw sha256 with `bcrypt` for password hashing (`pip install bcrypt`)
- [ ] Use proper session management (Flask sessions or JWT)
  - [ ] Learn what a JWT is and why it's used
  - [ ] Implement with `flask-jwt-extended` or `PyJWT`
- [ ] Add input validation and sanitization on all API endpoints
- [ ] Add rate limiting to login endpoint (prevent brute-force)
- [ ] Set secure HTTP headers (look up OWASP Secure Headers)
- [ ] Understand and prevent: XSS, CSRF, SQL injection (review your current code)

**What you learn:** real-world web security, JWT, OWASP top 10

---

## Phase 6 — Deployment

Make it accessible from the internet.

- [ ] Learn what a WSGI server is (vs Flask's dev server) — try `gunicorn`
- [ ] Write a `requirements.txt` (`pip freeze > requirements.txt`)
- [ ] Learn what Docker is and why it exists
  - [ ] Write a `Dockerfile` for the app
  - [ ] Run it locally with `docker build` / `docker run`
- [ ] Deploy to a free platform (Railway, Render, or Fly.io)
- [ ] Point a domain at it (optional but satisfying)
- [ ] Learn the difference between HTTP and HTTPS — enable HTTPS on your deployment

**What you learn:** production servers, containerization, deployment pipelines, DNS basics

---

## Optional / Bonus

These are real features, worth adding once the above is done.

- [ ] Migrate from SQLite to PostgreSQL (understand why)
- [ ] Add an admin view to list all users / accounts
- [ ] Add email notifications on login / transactions (learn SMTP)
- [ ] Add 2FA (TOTP — learn how authenticator apps work)
- [ ] Replace the Flask API with FastAPI — compare the two
- [ ] Write a proper CI pipeline with GitHub Actions (run tests on every push)
- [ ] Add logging (replace `print()` with Python's `logging` module)

---

## Current Phase: 1
