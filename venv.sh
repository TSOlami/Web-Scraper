#!/bin/bash

# Check if the required argument (virtual environment name) is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <venv_name>"
  exit 1
fi

# Get the virtual environment name from the argument
venv_name="$1"

# Check if the virtual environment already exists
if [ -d "$venv_name" ]; then
  echo "Virtual environment '$venv_name' already exists."
  exit 1
fi

# Create the virtual environment
python3 -m venv "$venv_name"

# Activate the virtual environment
source "$venv_name/bin/activate"

# Upgrade pip (optional but recommended)
pip install --upgrade pip

# Install any required dependencies for your project (optional)
# For example:
# pip install requests

echo "Virtual environment '$venv_name' created and activated."
