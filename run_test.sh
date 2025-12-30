#!/usr/bin/env bash
set -euo pipefail

# Run ruff if available, otherwise skip. Then run unit tests.
if command -v ruff >/dev/null 2>&1; then
  echo "Running ruff (linter)..."
  ruff inventory_manager
else
  echo "ruff not found — skipping linter"
fi

echo "Running pytest..."
pytest -q
