# Python base image
FROM Python:3.10-slim

WORKDIR /app

# install system dependencies
RUN apt-get update && apt-get install -y \
    git curl && rm -rf /var/lib/apt/lists/*

# Install Python Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 📁 Copy Source Code and Configs
COPY src/ ./src/
COPY config/ ./config/
COPY token.json ./

# Environment Variables (values loaded from .env)
ENV PYTHONUNBUFFERED=1

# Start the Application
CMD [ "python", "-m", "src.main"]