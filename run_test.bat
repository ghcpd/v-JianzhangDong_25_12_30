@echo off
REM Run ruff if available, then unit tests on Windows (simpler control flow)
where ruff >nul 2>&1
if errorlevel 1 (
  echo ruff not found - skipping linter
) else (
  echo Running ruff (linter)...
  ruff inventory_manager || goto :fail
)
pytest -q
if errorlevel 1 goto :fail
echo TESTS_SUCCEEDED
exit /b 0
:fail
echo TESTS_FAILED
exit /b 1
