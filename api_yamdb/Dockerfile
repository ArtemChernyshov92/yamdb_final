FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r ./requirements.txt --no-cache-dir

COPY ./ .

RUN mkdir ./static

COPY /static/redoc.yaml ./static

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]