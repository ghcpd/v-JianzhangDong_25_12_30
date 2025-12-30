"""Automatic test runner that detects environment and runs the appropriate test script.

- Writes a timestamped log to logs/test_run.log
- Exits with code 0 when tests pass, 1 when they fail
"""
from __future__ import annotations

import os
import platform
import shlex
import subprocess
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LOGS = ROOT / "logs"
LOGS.mkdir(exist_ok=True)
LOG_FILE = LOGS / "test_run.log"


def detect_environment() -> str:
    system = platform.system().lower()
    # simple docker detection
    if Path("/.dockerenv").exists() or "docker" in platform.platform().lower():
        return "docker"
    if system.startswith("win"):
        return "windows"
    return "unix"


def run_cmd(cmd: str, shell: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd if shell else shlex.split(cmd),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        shell=shell,
    )


def main() -> int:
    env = detect_environment()
    if env == "windows":
        runner = str(ROOT / "run_test.bat")
        cmd = runner
        shell = True
    else:
        runner = str(ROOT / "run_test.sh")
        cmd = runner
        shell = True

    start = datetime.utcnow().isoformat() + "Z"
    header = f"=== TEST RUN START: {start} (env={env}) ===\n"

    proc = run_cmd(cmd, shell=shell)
    end = datetime.utcnow().isoformat() + "Z"

    with LOG_FILE.open("a", encoding="utf-8") as fh:
        fh.write(header)
        fh.write(proc.stdout or "(no output)")
        fh.write("\n")
        if proc.returncode == 0:
            fh.write(f"TEST PASSED: {end}\n")
        else:
            fh.write(f"TEST FAILED: {end} (exit_code={proc.returncode})\n")
        fh.write("=== END ===\n\n")

    if proc.returncode == 0:
        print("TEST PASSED")
        return 0

    print("TEST FAILED")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
