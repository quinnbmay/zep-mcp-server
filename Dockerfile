FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install fastmcp zep-cloud

EXPOSE 8080

CMD ["python", "server.py"]