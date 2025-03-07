# Dockerfile - Containerized deployment
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "collect_data.py"]
