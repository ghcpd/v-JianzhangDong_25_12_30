@echo off
REM Run linter and tests on Windows
where python >nul 2>&1 || (
  echo Python not found in PATH && exit /b 1
)
python -m pip install --quiet --disable-pip-version-check -r requirements.txt
flake8 inventory_manager tests
pytest -q --maxfail=1
IF %ERRORLEVEL% NEQ 0 (
  EXIT /B %ERRORLEVEL%
)
EXIT /B 0
