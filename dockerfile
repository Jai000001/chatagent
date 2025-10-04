# Use a lightweight base image
FROM python:3.9-slim

# Create a non-root user with specific UID/GID
RUN groupadd -g 1000 appuser && useradd -u 1000 -g 1000 -m -s /bin/bash appuser

# Set the working directory
WORKDIR /cogent_app

# Install system dependencies and Python dependencies in one layer
RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat-openbsd \
    ffmpeg \
    libsm6 \
    libxext6 \
    dos2unix \
    tesseract-ocr \
    libgdiplus \
    wget \
    build-essential \
    cmake \
    git \
    curl \
    libopenblas-dev \
    libomp-dev \
    pkg-config \
    libpq-dev \
    gcc \
    && apt-get clean && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir --upgrade pip

RUN wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.0g-2ubuntu4_amd64.deb \
    && dpkg -i libssl1.1_1.1.0g-2ubuntu4_amd64.deb \
    && rm libssl1.1_1.1.0g-2ubuntu4_amd64.deb

# Install compatible ICU version (libicu70 instead of newer libicu72)
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/i/icu/libicu70_70.1-2_amd64.deb \
    && dpkg -i libicu70_70.1-2_amd64.deb \
    && rm libicu70_70.1-2_amd64.deb

# Copy only the requirements file first to utilize Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --timeout=120 --no-cache-dir --use-feature=fast-deps --use-pep517 -r requirements.txt
RUN pip install pandas
# Install Playwright system dependencies (explicit, for Ubuntu)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     wget ca-certificates fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libatk1.0-0 libcups2 libdbus-1-3 \
#     libnspr4 libnss3 libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 xdg-utils libu2f-udev libvulkan1 \
#     libxss1 libxtst6 lsb-release && \
#     rm -rf /var/lib/apt/lists/*

# Copy the rest of your application code
COPY . .

# Convert line endings if needed and make the startup script executable (do this before changing ownership)
RUN dos2unix start.sh && chmod +x start.sh

# Create necessary directories and set permissions
RUN mkdir -p /tmp/uploads && \
    chown -R appuser:appuser /cogent_app /tmp/uploads

# Switch to non-root user BEFORE installing Playwright browsers
USER appuser

# Set environment variable for Playwright to use system-wide installation
# ENV PLAYWRIGHT_BROWSERS_PATH=/home/appuser/.cache/ms-playwright

# Install Playwright browsers as the appuser
# RUN playwright install chromium

# Expose the port your application runs on
EXPOSE 5000

# Use the startup script as the entry point
CMD ["./start.sh"]