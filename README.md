# Inventory Manager — Style fixes, tests, and environment scripts

## Overview ✅
This workspace contains the `inventory_manager` package. I fixed code-style / linting issues, added unit tests, and created environment & test automation scripts.

Files added or updated:

- `report.json` — Structured list of all code-style issues found and the fixes applied.
- `requirements.txt` — Python dependencies for running tests and linter.
- `run_test.sh` / `run_test.bat` — Scripts to run the linter and unit tests (Linux/macOS and Windows respectively).
- `setup.sh` — Quick environment setup script for Linux/macOS (creates virtualenv and installs deps).
- `Dockerfile` — Minimal image that installs dependencies and runs `auto_test.py`.
- `auto_test.py` — Auto-detection script that runs the appropriate test script and logs results to `logs/test_run.log`.
- `tests/` — Pytest unit tests that validate functionality and that style changes didn't break behavior.
- Updated source files in `inventory_manager/` to satisfy PEP8 and basic linting.


## Setup (Linux / macOS) ⚙️
1. Create and activate a virtual environment:
   - bash: `./setup.sh`
2. Run tests manually:
   - `./run_test.sh`

## Setup (Windows) ⚙️
1. Create a Python virtual environment (PowerShell):
   - `python -m venv .venv` then `.\.venv\Scripts\Activate.ps1`
2. Install requirements:
   - `pip install -r requirements.txt`
3. Run tests:
   - `run_test.bat`

## Docker
Build and run:

```
docker build -t inventory-manager .
docker run --rm inventory-manager
```

The Docker image runs `auto_test.py` which will execute the test script and write logs to `logs/test_run.log` inside the container.

## auto_test.py — automatic test runner ✨
- Detects environment (Windows vs POSIX, basic Docker heuristics).
- Runs `run_test.sh` on POSIX or `run_test.bat` on Windows.
- Appends logs to `logs/test_run.log` with ISO timestamps and a final status line: `TEST PASSED` or `TEST FAILED`.

Usage:
- `python auto_test.py`


## Logs
- Location: `logs/test_run.log`
- Each entry includes a UTC ISO timestamp.
- Final status is `TEST PASSED` (exit code 0) or `TEST FAILED` (non-zero).


## Linting & Tests
- Linter: `ruff` (configured via `requirements.txt`).
- Tests: `pytest` in the `tests/` folder.


## Notes / Next steps 💡
- You can extend `report.json` with additional issues if you want stricter rules (complexity, typing coverage, etc.).
- Consider adding a CI workflow that runs `run_test.sh` on PRs.
