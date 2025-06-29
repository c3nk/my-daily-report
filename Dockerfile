# Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY report.py .

RUN pip install --no-cache-dir

CMD ["python", "report.py"]
