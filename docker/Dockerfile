FROM python:3.10.15-alpine3.20

# Ensure that Python output is sent straight to terminal (e.g., for logging)
ENV PYTHONUNBUFFERED=1

# Set the Python path to the /app directory
ENV PYTHONPATH=/app

RUN pip install uv

# Set the working directory to /app
WORKDIR /app

# Copy the requirements lock file into the image
COPY ../../requirements.lock ./

# Install dependencies from the lock file without caching
RUN uv pip install --no-cache --system -r requirements.lock

# Copy the source code into the image
COPY ../../src /app/src
