# Python base image
FROM python:3.10-slim

WORKDIR /app

# install system dependencies
RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y \
    git curl && rm -rf /var/lib/apt/lists/*

# Install Python Dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy Source Code
COPY src/*.py /app/

# Start the Application
CMD [ "python", "-m", "main"]