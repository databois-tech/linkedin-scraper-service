FROM python:3.10.12

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt --default-timeout=100 --retries=5

COPY . .

CMD ["gunicorn", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "--bind", "0.0.0.0:8001", "--timeout", "60", "--log-level", "debug", "--log-file", "-", "--keep-alive", "60", "--graceful-timeout", "180", "--worker-connections", "1000"]
