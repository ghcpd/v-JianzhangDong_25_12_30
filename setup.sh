#!/bin/bash

# Setup script for Linux/macOS
# This script sets up the Python environment and installs dependencies

set -e  # Exit on error

echo "=========================================="
echo "Setting up Inventory Manager Environment"
echo "=========================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

echo "Python version:"
python3 --version

# Create a virtual environment
echo ""
echo "Creating virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Create logs directory
echo "Creating logs directory..."
mkdir -p logs

echo ""
echo "=========================================="
echo "Setup completed successfully!"
echo "=========================================="
echo ""
echo "To activate the virtual environment, run:"
echo "  source venv/bin/activate"
echo ""
echo "To run the test script, run:"
echo "  bash run_test.sh"
echo ""
echo "To run auto tests, run:"
echo "  python auto_test.py"
