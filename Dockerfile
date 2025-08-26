FROM python:3.10-slim

WORKDIR /app

# Copy requirements and install
COPY config/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install zep-cloud

# Copy application
COPY . .

EXPOSE 8080

CMD ["python", "core/zep_cloud_server.py"]