#!/bin/bash

# Abort script if any command returns an error.
set -euo pipefail

# Setup python virtual environment.
rye sync

# Activate the python virtual environment.
source .venv/bin/activate

# Install pre-commit hooks.
pre-commit install

# Set the safe.directory
git config --global --add safe.directory `pwd`
