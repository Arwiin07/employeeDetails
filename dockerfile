FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .

EXPOSE 80

CMD ["gunicorn", "--bind", "0.0.0.0:80", "main:app"]
