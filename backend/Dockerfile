FROM python:3.12-slim   
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY .env .env
EXPOSE 8000
