#!/usr/bin/env python3
"""Auto test runner.

Detects the environment and runs the appropriate test script.
Logs results to `logs/test_run.log` with a timestamp and final status.
"""
import datetime
import platform
import subprocess
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "test_run.log"


def run_command(cmd, shell=False):
    proc = subprocess.run(cmd, capture_output=True, text=True, shell=shell)
    return proc.returncode, proc.stdout, proc.stderr


def main():
    # Use timezone-aware UTC timestamp to avoid deprecation warnings.
    ts = datetime.datetime.now(datetime.timezone.utc).isoformat()

    if platform.system().lower().startswith("win"):
        cmd = ["cmd.exe", "/c", "run_test.bat"]
    else:
        cmd = ["bash", "run_test.sh"]

    return_code, out, err = run_command(cmd)

    with LOG_FILE.open("a", encoding="utf-8") as fh:
        fh.write(f"=== Test run at {ts} ===\n")
        fh.write(out)
        fh.write(err)
        if return_code == 0:
            fh.write("TEST PASSED\n")
        else:
            fh.write("TEST FAILED\n")

    if return_code != 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
