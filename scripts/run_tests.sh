#!/bin/sh

apk add gcc musl-dev linux-headers libffi-dev
# Navigate to the /app directory
cd /app

# Install Python packages using 'uv' with specified options
uv pip install --no-cache --system --requirement requirements-dev.lock

# Run tests using pytest in quiet mode with two parallel workers
uv run pytest -n 4 -q tests/conversion/
