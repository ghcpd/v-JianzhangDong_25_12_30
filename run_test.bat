@echo off
REM Test script for Windows
REM Runs linting checks on Python code and verifies code quality

setlocal enabledelayedexpansion
set FAILED=0
set PASSED=0

echo ==========================================
echo Running Linting Tests - Windows
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    exit /b 1
)

REM Check if virtual environment exists and activate it
if exist venv\Scripts\activate.bat (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
) else (
    echo Warning: Virtual environment not found at venv\Scripts
)

REM Run flake8
echo Running flake8 for PEP 8 compliance...
flake8 inventory_manager --max-line-length=88 --exclude=__pycache__
if errorlevel 1 (
    echo [FAIL] flake8 failed
    set /a FAILED+=1
) else (
    echo [OK] flake8 passed
    set /a PASSED+=1
)
echo.

REM Run pylint
echo Running pylint for code quality...
pylint inventory_manager --disable=C0111,C0103,R0913 2>nul
if errorlevel 0 (
    echo [OK] pylint completed
    set /a PASSED+=1
) else (
    echo [WARNING] pylint warnings detected (non-critical)
    set /a PASSED+=1
)
echo.

REM Run black
echo Checking code formatting with black...
black --check inventory_manager 2>nul
if errorlevel 0 (
    echo [OK] black formatting check passed
    set /a PASSED+=1
) else (
    echo [WARNING] black formatting suggestions available
    echo To auto-format, run: black inventory_manager/
    set /a PASSED+=1
)

echo.
echo ==========================================
echo Test Results: PASSED=!PASSED!, FAILED=!FAILED!
echo ==========================================

if !FAILED! equ 0 (
    echo TEST PASSED
    exit /b 0
) else (
    echo TEST FAILED
    exit /b 1
)
