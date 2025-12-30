#!/usr/bin/env bash
set -euo pipefail

# Run linters and tests
python -m pytest -q
