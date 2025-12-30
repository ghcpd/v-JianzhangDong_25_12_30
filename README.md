# Inventory Manager — Lint & Test Suite

## Overview ✅
This repository includes the inventory manager code and added files to enforce code style and provide testing automation.

Files added/modified:
- `report.json` — Lint/style findings and suggested fixes.
- `requirements.txt` — Python dependencies (pandas, openpyxl, flake8, pytest).
- `Dockerfile` — Containerized environment to run tests.
- `setup.sh` — Create virtualenv and install dependencies (Linux/macOS).
- `run_test.sh` — Run tests on Linux/macOS.
- `run_test.bat` — Run tests on Windows.
- `auto_test.py` — Detect environment, run tests, and log results to `logs/test_run.log`.
- `tests/test_lint.py` — Pytest wrapper that runs `flake8`.
- Modified Python modules in `inventory_manager/` to follow PEP8 and add docstrings.

## Environment setup (Linux/macOS) ⚙️
1. Install Python 3.11+.
2. Run:
   ```bash
   ./setup.sh
   ```
3. Activate the venv and run tests:
   ```bash
   source .venv/bin/activate
   ./run_test.sh
   ```

## Environment setup (Windows) ⚙️
1. Install Python 3.11+.
2. Create and activate virtualenv and install requirements manually:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
3. Run tests:
   ```powershell
   .\run_test.bat
   ```

## Using `auto_test.py` (cross-platform) 🧪
`auto_test.py` detects the OS and runs `run_test.sh` or `run_test.bat`. All output is appended to `logs/test_run.log` with timestamp and final status line `TEST PASSED` or `TEST FAILED`.

Run it with:
```bash
python auto_test.py
```

## Interpreting logs 📄
Logs are located at `logs/test_run.log`. Each run includes a timestamp and ends with either `TEST PASSED` or `TEST FAILED`.

## Notes 💡
- The lint checks are performed using `flake8`. Fix any reported issues and re-run tests.
- `pandas` with `openpyxl` is required for `export_report` to write Excel files.
