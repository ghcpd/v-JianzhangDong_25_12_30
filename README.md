# inventory_manager — lint fixes, tests and automation

This workspace contains a small inventory package and the accompanying developer tooling I added:

- `requirements.txt` — Python dependencies required to run tests and linting
- `run_test.sh` / `run_test.bat` — run linter (flake8) and unit tests (pytest)
- `setup.sh` — bootstrap a virtualenv and install dependencies (Linux/macOS)
- `Dockerfile` — container image that runs the test suite
- `auto_test.py` — detects environment (Windows/Linux/Docker), runs the correct test script and writes `logs/test_run.log`
- `tests/test_basic.py` — unit tests that validate functionality and basic integration
- `report.json` — detailed, structured list of the style/lint issues that were found and fixed

Quickstart
---------

1. Linux/macOS

```bash
./setup.sh
source .venv/bin/activate
./run_test.sh
```

2. Windows (PowerShell / cmd)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
run_test.bat
```

3. Docker

```bash
docker build -t inventory-manager:local .
docker run --rm inventory-manager:local
```

Using `auto_test.py`
-------------------

The script detects the platform and runs the appropriate test script, saving full output to `logs/test_run.log`.

```bash
python auto_test.py
# then check:
cat logs/test_run.log
```

Interpreting results
--------------------

- `logs/test_run.log` contains a timestamped run with the full output and a final line `TEST PASSED` or `TEST FAILED`.
- `run_test.sh`/`run_test.bat` exit with non-zero on failure so CI systems can detect regressions.

Files changed
-------------
- Code: cleaned for PEP8, added type hints and dataclasses
- Tests: added `tests/test_basic.py`
- Tooling: added scripts, Dockerfile and `auto_test.py`
- `report.json` contains the detailed lint report
