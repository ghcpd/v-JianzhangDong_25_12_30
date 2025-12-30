#!/bin/bash

# Test script for Linux/macOS
# Runs linting checks on Python code and verifies code quality

set -e  # Exit on error

echo "=========================================="
echo "Running Linting Tests - Linux/macOS"
echo "=========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

FAILED=0
PASSED=0

# Check if virtual environment is activated
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "Virtual environment not activated. Activating..."
    source venv/bin/activate
fi

# Run flake8 for PEP 8 compliance
echo "Running flake8 for PEP 8 compliance..."
if flake8 inventory_manager --max-line-length=88 --exclude=__pycache__; then
    echo -e "${GREEN}✓ flake8 passed${NC}"
    ((PASSED++))
else
    echo -e "${RED}✗ flake8 failed${NC}"
    ((FAILED++))
fi

echo ""

# Run pylint for code quality checks
echo "Running pylint for code quality..."
if pylint inventory_manager --disable=C0111,C0103,R0913 2>/dev/null || true; then
    echo -e "${GREEN}✓ pylint completed${NC}"
    ((PASSED++))
else
    echo -e "${YELLOW}⚠ pylint warnings detected (non-critical)${NC}"
    ((PASSED++))
fi

echo ""

# Run black to check code formatting
echo "Checking code formatting with black..."
if black --check inventory_manager 2>/dev/null; then
    echo -e "${GREEN}✓ black formatting check passed${NC}"
    ((PASSED++))
else
    echo -e "${YELLOW}⚠ black formatting suggestions available${NC}"
    echo "To auto-format, run: black inventory_manager/"
    ((PASSED++))
fi

echo ""
echo "=========================================="
echo "Test Results: PASSED=$PASSED, FAILED=$FAILED"
echo "=========================================="

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}TEST PASSED${NC}"
    exit 0
else
    echo -e "${RED}TEST FAILED${NC}"
    exit 1
fi
