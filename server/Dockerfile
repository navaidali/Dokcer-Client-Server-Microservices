FROM python:3.8-slim

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
CMD ["python", "app/server.py"]