# Inventory Manager

This is a simple inventory management system written in Python. It allows adding products, calculating totals, and exporting reports to Excel.

## Generated Files

- `report.json`: JSON report of identified code style/linting issues before fixes.
- `requirements.txt`: Python dependencies for the project.
- `Dockerfile`: Docker configuration to run the application in a container.
- `setup.sh`: Setup script for Linux/macOS to install Python and dependencies.
- `run_test.sh`: Test script for Linux/macOS to run style checks.
- `run_test.bat`: Test script for Windows to run style checks.
- `auto_test.py`: Automated test runner that detects the environment and runs the appropriate test script.
- `logs/test_run.log`: Log file for test runs (created by auto_test.py).

## Setup Instructions

### Option 1: Local Setup

#### Windows
1. Ensure Python 3 is installed.
2. Run `pip install -r requirements.txt` to install dependencies.

#### Linux/macOS
1. Run `./setup.sh` to install Python and dependencies.

### Option 2: Docker
1. Build the Docker image: `docker build -t inventory-manager .`
2. Run the container: `docker run inventory-manager`

## Running the Application

Execute `python main.py` to run the inventory manager. It will create a database, add sample products, calculate totals, and export a report to `report.xlsx`.

## Running Tests

### Manual Test Execution

#### Linux/macOS
Run `./run_test.sh` to perform style checks.

#### Windows
Run `run_test.bat` to perform style checks.

### Automated Test Execution

Run `python auto_test.py` to automatically detect the environment (Windows, Linux, macOS, or Docker) and execute the corresponding test script. The script will log all output to `logs/test_run.log` with a timestamp and a final status of `TEST PASSED` or `TEST FAILED`.

### Checking Logs

After running `auto_test.py`, check `logs/test_run.log` for detailed output. The log includes:
- Timestamp of the test run
- All output from the test script
- Final status: `TEST PASSED` if all style checks pass, `TEST FAILED` otherwise.

Interpret the status:
- `TEST PASSED`: All code style and linting issues have been resolved.
- `TEST FAILED`: There are remaining style or linting issues that need to be addressed.