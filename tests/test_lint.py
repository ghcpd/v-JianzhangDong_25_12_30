import subprocess
import sys


def test_flake8():
    """Run flake8 and fail if linting issues remain."""
    res = subprocess.run(
        [sys.executable, "-m", "flake8"], capture_output=True, text=True
    )
    if res.returncode != 0:
        print("flake8 output:\n", res.stdout)
        print(res.stderr)

    assert (
        res.returncode == 0
    ), "flake8 reported style issues. See output above."
