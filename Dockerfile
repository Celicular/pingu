FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ping_monitor.py .

CMD ["python", "ping_monitor.py"] 