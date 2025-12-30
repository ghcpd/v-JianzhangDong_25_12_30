#!/bin/bash

# Run tests script for Linux/macOS

echo "Running style checks..."

# Install flake8 if not present
pip3 install flake8

# Run flake8
flake8 . --max-line-length=88

# Check exit code
if [ $? -eq 0 ]; then
    echo "All style checks passed."
    exit 0
else
    echo "Style checks failed."
    exit 1
fi