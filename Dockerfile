FROM python:3.12-slim

WORKDIR /app

COPY report.py .

# Bu satıra GEREK YOK:
# RUN pip install --no-cache-dir

CMD ["python", "report.py"]
