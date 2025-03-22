# Use a minimal, security-focused Python image
FROM python:3.11-slim AS base

# Set environment variables for non-interactive installs & security
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Create a dedicated user to enhance security
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies efficiently
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy application files
COPY . .

# Change file ownership for security
RUN chown -R appuser:appgroup /app
USER appuser

# Expose application port
EXPOSE 8000

# Run Gunicorn with optimal settings
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers=4", "--threads=4", "backend.wsgi:application"]