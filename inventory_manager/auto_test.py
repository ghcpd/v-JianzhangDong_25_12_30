#!/usr/bin/env python3

import os
import platform
import subprocess
import datetime


def detect_environment():
    system = platform.system()
    if system == 'Windows':
        return 'Windows'
    elif system == 'Linux':
        # Check if in Docker
        try:
            with open('/proc/1/cgroup', 'r') as f:
                if 'docker' in f.read():
                    return 'Docker'
        except Exception:
            pass
        return 'Linux'
    elif system == 'Darwin':
        return 'macOS'
    else:
        return 'Unknown'


def run_test(env):
    # Create logs directory
    os.makedirs('logs', exist_ok=True)

    timestamp = datetime.datetime.now().isoformat()
    log_file = 'logs/test_run.log'

    with open(log_file, 'a') as log:
        log.write(f"{timestamp} - Starting test for {env}\n")

    if env == 'Windows':
        script = 'run_test.bat'
    elif env in ['Linux', 'macOS', 'Docker']:
        script = './run_test.sh'
    else:
        print("Unknown environment")
        return False

    try:
        result = subprocess.run(
            [script],
            capture_output=True,
            text=True,
            shell=(env == 'Windows')
        )
        output = result.stdout + result.stderr
        success = result.returncode == 0

        with open(log_file, 'a') as log:
            log.write(output)
            if success:
                log.write("TEST PASSED\n")
            else:
                log.write("TEST FAILED\n")

        print(output)
        return success
    except Exception as e:
        with open(log_file, 'a') as log:
            log.write(f"Error running test: {e}\nTEST FAILED\n")
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    env = detect_environment()
    print(f"Detected environment: {env}")
    success = run_test(env)
    if success:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
