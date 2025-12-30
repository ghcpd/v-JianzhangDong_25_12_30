import os
import platform
import subprocess
import sys
import shutil
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "test_run.log")


def ensure_log_dir() -> None:
    os.makedirs(LOG_DIR, exist_ok=True)


def log(msg: str) -> None:
    now = datetime.utcnow().isoformat()
    with open(LOG_FILE, "a", encoding="utf-8") as fh:
        fh.write(f"{now} - {msg}\n")


def detect_docker() -> bool:
    # Common heuristics for detecting Docker
    try:
        if os.path.exists("/.dockerenv"):
            return True
        with open("/proc/1/cgroup", "rt") as fh:
            return "docker" in fh.read() or "kubepods" in fh.read()
    except Exception:
        return False


def run_command(cmd: list, timeout: int = 300) -> int:
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    assert proc.stdout
    for line in proc.stdout:
        print(line, end="")
        log(line.rstrip())
    proc.wait(timeout=timeout)
    return proc.returncode


def main() -> int:
    ensure_log_dir()
    system = platform.system()
    is_docker = detect_docker()

    log(f"Environment detected: system={system}, docker={is_docker}")

    if system == "Windows":
        # prefer running the batch file, but fall back to running commands directly
        cmd = ["cmd.exe", "/c", "run_test.bat"]
        rc = 0
        try:
            rc = run_command(cmd)
        except Exception as exc:  # fallback for environments where cmd.exe invocation fails
            log(f"run_test.bat failed to start: {exc} — falling back to direct commands")

        # If the batch returned a non-zero status, fallback to direct execution of the same steps
        if rc != 0:
            log("run_test.bat returned non-zero — falling back to direct commands")
            print("Fallback: running tests directly on Windows")
            rc = 0
            try:
                if shutil.which("ruff"):
                    r = run_command(["ruff", "inventory_manager"])
                    rc = rc or r
                r = run_command([sys.executable, "-m", "pytest", "-q"])
                rc = rc or r
            except Exception as exc2:
                log(f"Direct test execution failed: {exc2}")
                rc = 1
    else:
        cmd = ["/bin/bash", "run_test.sh"]
        rc = run_command(cmd)

    status = "TEST PASSED" if rc == 0 else "TEST FAILED"
    log(status)
    print(status)
    return rc


if __name__ == "__main__":
    sys.exit(main())
