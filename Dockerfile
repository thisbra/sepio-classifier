# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV POETRY_VERSION=1.4.2 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION"

# Set the working directory to /app
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files to the working directory
COPY pyproject.toml poetry.lock /app/

# Install the dependencies
RUN poetry install --no-root --no-dev

# Copy the rest of the application code to the working directory
COPY . /app

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
