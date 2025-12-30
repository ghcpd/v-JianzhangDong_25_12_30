#!/usr/bin/env python3
"""
Auto Test Script
Automatically detects the current environment and runs appropriate test scripts.
Logs results to logs/test_run.log with timestamp and final status.
"""

import os
import sys
import platform
import subprocess
import shutil
from datetime import datetime
from pathlib import Path


def get_environment():
    """
    Detect the current environment (Windows, Linux, macOS, or Docker).
    
    Returns:
        str: Environment type ('windows', 'linux', 'darwin', 'docker')
    """
    if os.path.exists('/.dockerenv'):
        return 'docker'
    
    system = platform.system()
    if system == 'Windows':
        return 'windows'
    elif system == 'Linux':
        return 'linux'
    elif system == 'Darwin':
        return 'darwin'
    else:
        return 'unknown'


def create_logs_directory():
    """Create logs directory if it doesn't exist."""
    logs_dir = Path('logs')
    logs_dir.mkdir(exist_ok=True)
    return logs_dir


def run_test_script(test_script, environment):
    """
    Run the appropriate test script for the environment.
    
    Args:
        test_script (str): Path to the test script
        environment (str): Environment type
        
    Returns:
        tuple: (exit_code, stdout, stderr)
    """
    try:
        if environment in ['windows']:
            # Windows batch file
            result = subprocess.run(
                ['cmd', '/c', test_script],
                capture_output=True,
                text=True,
                timeout=300
            )
        else:
            # Shell script (Linux, macOS, Docker)
            # Make script executable
            os.chmod(test_script, 0o755)
            
            result = subprocess.run(
                ['bash', test_script],
                capture_output=True,
                text=True,
                timeout=300
            )
        
        return result.returncode, result.stdout, result.stderr
    
    except subprocess.TimeoutExpired:
        return -1, "", "Test script execution timed out"
    except FileNotFoundError:
        return -1, "", f"Test script not found: {test_script}"
    except Exception as e:
        return -1, "", str(e)


def format_log_entry(timestamp, environment, test_script, exit_code, stdout, stderr):
    """
    Format log entry with all test information.
    
    Args:
        timestamp (str): Test execution timestamp
        environment (str): Detected environment
        test_script (str): Script executed
        exit_code (int): Exit code from script
        stdout (str): Standard output
        stderr (str): Standard error
        
    Returns:
        str: Formatted log entry
    """
    log_entry = []
    log_entry.append("=" * 80)
    log_entry.append(f"Test Execution Timestamp: {timestamp}")
    log_entry.append(f"Environment Detected: {environment.upper()}")
    log_entry.append(f"Test Script: {test_script}")
    log_entry.append("=" * 80)
    log_entry.append("")
    
    log_entry.append("--- STANDARD OUTPUT ---")
    log_entry.append(stdout if stdout else "(No output)")
    log_entry.append("")
    
    if stderr:
        log_entry.append("--- STANDARD ERROR ---")
        log_entry.append(stderr)
        log_entry.append("")
    
    log_entry.append("--- TEST RESULT ---")
    if exit_code == 0:
        log_entry.append("STATUS: TEST PASSED")
    else:
        log_entry.append(f"STATUS: TEST FAILED (Exit Code: {exit_code})")
    
    log_entry.append("")
    log_entry.append("=" * 80)
    log_entry.append("")
    
    return "\n".join(log_entry)


def main():
    """Main execution function."""
    # Create logs directory
    logs_dir = create_logs_directory()
    log_file = logs_dir / 'test_run.log'
    
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Detect environment
    environment = get_environment()
    
    print(f"[*] Auto Test Script Started")
    print(f"[*] Timestamp: {timestamp}")
    print(f"[*] Detected Environment: {environment.upper()}")
    print(f"[*] Log file: {log_file}")
    print("")
    
    # Select appropriate test script
    if environment == 'windows':
        test_script = 'run_test.bat'
    else:
        test_script = 'run_test.sh'
    
    # Check if test script exists
    if not os.path.exists(test_script):
        error_msg = f"Error: Test script '{test_script}' not found"
        print(error_msg)
        
        # Write error to log
        with open(log_file, 'a', encoding='utf-8') as f:
            error_log = format_log_entry(
                timestamp,
                environment,
                test_script,
                -1,
                "",
                error_msg
            )
            f.write(error_log)
        
        sys.exit(1)
    
    print(f"[*] Running test script: {test_script}")
    print("")
    
    # Run test script
    exit_code, stdout, stderr = run_test_script(test_script, environment)
    
    # Format and write log
    log_entry = format_log_entry(
        timestamp,
        environment,
        test_script,
        exit_code,
        stdout,
        stderr
    )
    
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(log_entry)
    
    # Print results
    print("Test output:")
    print(stdout)
    
    if stderr:
        print("Errors:")
        print(stderr)
    
    print("")
    print("=" * 80)
    if exit_code == 0:
        print("FINAL STATUS: TEST PASSED")
        print("=" * 80)
        sys.exit(0)
    else:
        print(f"FINAL STATUS: TEST FAILED (Exit Code: {exit_code})")
        print("=" * 80)
        sys.exit(exit_code)


if __name__ == '__main__':
    main()
