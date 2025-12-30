#!/usr/bin/env bash
set -euo pipefail

# Run linter then unit tests. Exit non-zero on failure so callers (CI / auto_test.py) can detect failures.
flake8 inventory_manager tests
pytest -q --maxfail=1
