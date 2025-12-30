@echo off

REM Run tests script for Windows

echo Running style checks...

REM Install flake8 if not present
pip install flake8

REM Run flake8
flake8 . --max-line-length=88

REM Check exit code
if %errorlevel% equ 0 (
    echo All style checks passed.
    exit /b 0
) else (
    echo Style checks failed.
    exit /b 1
)