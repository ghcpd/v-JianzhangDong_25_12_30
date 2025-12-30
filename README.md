# Inventory Manager - Code Quality & Testing Guide

## Overview

This project includes comprehensive code style analysis, automated fixes, and environment-specific testing scripts to ensure code quality and maintainability. This document describes all generated files and how to use them effectively.

---

## Generated Files and Their Purpose

### 1. **report.json**
- **Purpose**: Contains a structured analysis of all code style and linting issues found in the project
- **Contents**:
  - Summary: Total vulnerabilities count (critical, high, medium, low severity)
  - Details: List of each issue with file location, line numbers, original code, fixed code, and explanation
- **Usage**: Review this file to understand what code issues were identified and how they were fixed

### 2. **requirements.txt**
- **Purpose**: Lists all Python package dependencies required to run the project
- **Packages**:
  - `pandas` - Data manipulation library (for report export)
  - `openpyxl` - Excel file support
  - `pylint` - Code quality checker
  - `flake8` - PEP 8 compliance checker
  - `black` - Code formatter

### 3. **Dockerfile**
- **Purpose**: Container configuration for building and running the application in Docker
- **Features**:
  - Uses Python 3.11-slim base image
  - Installs all dependencies from requirements.txt
  - Creates logs directory
  - Sets up environment for automatic testing

### 4. **setup.sh** (Linux/macOS)
- **Purpose**: Automated environment setup script
- **Functions**:
  - Checks Python 3 availability
  - Creates Python virtual environment
  - Installs all dependencies
  - Creates logs directory
  - Provides activation instructions

### 5. **run_test.sh** (Linux/macOS)
- **Purpose**: Runs linting tests for PEP 8 compliance and code quality
- **Tests Performed**:
  - **flake8**: Checks PEP 8 compliance (max line length: 88)
  - **pylint**: Performs comprehensive code quality checks
  - **black**: Verifies code formatting standards
- **Output**: Detailed test results with pass/fail status

### 6. **run_test.bat** (Windows)
- **Purpose**: Windows equivalent of run_test.sh
- **Tests Performed**: Same as run_test.sh but for Windows environment
- **Output**: Colored test results with status indicators

### 7. **auto_test.py**
- **Purpose**: Automatic environment detection and test execution
- **Features**:
  - Auto-detects OS (Windows/Linux/macOS) or Docker
  - Selects and runs appropriate test script
  - Logs all output with timestamps
  - Generates final status (TEST PASSED or TEST FAILED)
  - Saves logs to `logs/test_run.log`

### 8. **inventory_manager/** (Fixed Python Files)
All Python files have been updated with PEP 8 compliant formatting:
- Fixed spacing around operators (E225)
- Added proper spacing after colons in type hints
- Removed multiple statements on single line (E701)
- Wrapped long lines to 88 characters max (E501)
- Renamed function to snake_case convention (N802)
- Organized imports alphabetically

---

## Step-by-Step Setup Instructions

### For Linux/macOS:

#### 1. Make setup script executable
```bash
chmod +x setup.sh
chmod +x run_test.sh
chmod +x auto_test.py
```

#### 2. Run setup script
```bash
./setup.sh
```

This will:
- Create a Python virtual environment
- Install all dependencies
- Create logs directory

#### 3. Activate virtual environment
```bash
source venv/bin/activate
```

### For Windows:

#### 1. Run setup using Python
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
mkdir logs
```

#### 2. Alternative: Using PowerShell
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
New-Item -ItemType Directory -Path logs -Force
```

### For Docker:

#### 1. Build the Docker image
```bash
docker build -t inventory-manager .
```

#### 2. Run the container with auto tests
```bash
docker run --rm inventory-manager
```

---

## Running Tests

### Linux/macOS - Manual Test Script

Run the test script to check code quality:
```bash
bash run_test.sh
```

**Output example:**
```
==========================================
Running Linting Tests - Linux/macOS
==========================================

Running flake8 for PEP 8 compliance...
✓ flake8 passed

Running pylint for code quality...
✓ pylint completed

Checking code formatting with black...
✓ black formatting check passed

==========================================
Test Results: PASSED=3, FAILED=0
==========================================
TEST PASSED
```

### Windows - Manual Test Script

Run the batch file:
```bash
run_test.bat
```

### Automatic Testing with auto_test.py

Run the auto test script on any platform:
```bash
python auto_test.py
```

**Features:**
- Auto-detects your environment (Windows/Linux/macOS/Docker)
- Selects appropriate test script automatically
- Runs tests and captures all output
- Saves results to `logs/test_run.log`
- Displays final status: `TEST PASSED` or `TEST FAILED`

**Example output:**
```
[*] Auto Test Script Started
[*] Timestamp: 2024-01-15 10:30:45
[*] Detected Environment: WINDOWS
[*] Log file: logs/test_run.log
[*] Running test script: run_test.bat

Test output:
[OK] flake8 passed
[OK] pylint completed
[OK] black formatting check passed

================================================================================
FINAL STATUS: TEST PASSED
================================================================================
```

---

## Understanding Test Results

### Test Passed
```
TEST PASSED
```
**Meaning**: All code quality checks passed. No PEP 8 violations, proper formatting, and acceptable code quality metrics.

### Test Failed
```
TEST FAILED (Exit Code: 1)
```
**Meaning**: One or more code quality checks failed. Review the test output to identify and fix issues.

---

## Checking Logs

All test execution logs are saved to `logs/test_run.log` with the following information:

```
================================================================================
Test Execution Timestamp: 2024-01-15 10:30:45
Environment Detected: WINDOWS
Test Script: run_test.bat
================================================================================

--- STANDARD OUTPUT ---
[Output from test script...]

--- STANDARD ERROR ---
[Any errors encountered...]

--- TEST RESULT ---
STATUS: TEST PASSED

================================================================================
```

### To view the latest log:
```bash
# Linux/macOS
cat logs/test_run.log

# Windows (PowerShell)
Get-Content logs/test_run.log

# Windows (Command Prompt)
type logs/test_run.log
```

### To view last 50 lines:
```bash
# Linux/macOS
tail -50 logs/test_run.log

# Windows (PowerShell)
Get-Content logs/test_run.log -Tail 50
```

---

## Code Quality Metrics

### Severity Levels in report.json

- **Critical (0)**: Issues that may cause runtime errors or security vulnerabilities
- **High (5)**: PEP 8 violations and naming convention issues
- **Medium (10)**: Formatting and spacing issues
- **Low (3)**: Minor style issues

### Total Issues Addressed: 18

All issues have been identified, documented in `report.json`, and fixed in the source code.

---

## Common Issues and Solutions

### Virtual Environment Issues

**Problem**: `venv\Scripts\activate.bat` not found
**Solution**:
```bash
python -m venv venv --clear
```

**Problem**: `source: command not found` (on Windows using Git Bash)
**Solution**: Use Command Prompt or PowerShell instead, or:
```bash
. venv/Scripts/activate
```

### Test Script Not Executable

**Problem**: Permission denied on Linux/macOS
**Solution**:
```bash
chmod +x setup.sh run_test.sh auto_test.py
```

### Missing Dependencies

**Problem**: Module not found errors
**Solution**: Reinstall dependencies:
```bash
pip install -r requirements.txt --force-reinstall
```

### Docker Issues

**Problem**: Docker daemon not running
**Solution**: Start Docker Desktop or service:
```bash
# macOS
open /Applications/Docker.app

# Linux
sudo systemctl start docker
```

---

## File Structure

```
.
├── inventory_manager/          # Main package (all files fixed)
│   ├── __init__.py
│   ├── config.py
│   ├── constants.py
│   ├── database.py
│   ├── exceptions.py
│   ├── main.py
│   ├── models.py
│   ├── report.py
│   └── utils.py
├── logs/                        # Test execution logs (created at runtime)
│   └── test_run.log            # Latest test results
├── venv/                        # Python virtual environment (created by setup)
├── report.json                  # Linting issues analysis
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker configuration
├── setup.sh                     # Linux/macOS setup script
├── run_test.sh                  # Linux/macOS test script
├── run_test.bat                 # Windows test script
├── auto_test.py                 # Cross-platform auto test script
└── README.md                    # This file
```

---

## Quick Start Summary

### Fastest way to verify code quality:

**On Linux/macOS:**
```bash
chmod +x setup.sh run_test.sh auto_test.py
./setup.sh
source venv/bin/activate
python auto_test.py
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python auto_test.py
```

**With Docker:**
```bash
docker build -t inventory-manager .
docker run --rm inventory-manager
```

---

## Additional Resources

### PEP 8 Style Guide
- https://www.python.org/dev/peps/pep-0008/

### Flake8 Documentation
- https://flake8.pycqa.org/

### Pylint Documentation
- https://www.pylint.org/

### Black Code Formatter
- https://black.readthedocs.io/

---

## Support

For issues or questions:

1. Check the `report.json` for detailed issue descriptions
2. Review the test logs in `logs/test_run.log`
3. Ensure all dependencies are installed: `pip install -r requirements.txt`
4. Verify Python version: `python --version` (requires Python 3.7+)

---

**Last Updated**: December 30, 2024  
**Project**: Inventory Manager - Code Quality & Testing Suite
