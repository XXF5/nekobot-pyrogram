FROM python:3.11-slim

# منع buffering
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependencies system
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Run bot
CMD ["python", "neko.py"]
