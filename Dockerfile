# Temel imaj
FROM python:3.11-slim

# Çalışma dizini
WORKDIR /app

# Tüm dosyaları konteynere kopyala
COPY . .

# Gerekiyorsa bağımlılıkları yükle
# requirements.txt yoksa bu satırı kaldır veya pip install kısmını ekle
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Konteyner başladığında ne çalışacak
CMD ["python", "report.py"]
