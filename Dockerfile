FROM python:3.11-slim

# Set working dir
WORKDIR /app

# Install dependencies for building (optional but recommended)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy dependency file & install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Ekspos port Flask default
EXPOSE 5000

# Jalankan aplikasi
CMD ["python", "crudapp.py"]

