@echo off
REM Run linters and tests on Windows
python -m pytest -q
if %ERRORLEVEL% NEQ 0 (
    exit /b %ERRORLEVEL%
)
exit /b 0
