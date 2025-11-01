FROM python:3.11-slim

WORKDIR /app

# Copy requirements lebih dulu (supaya layer cache tidak invalid)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file aplikasi
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]

