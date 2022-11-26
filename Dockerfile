<<<<<<< HEAD
FROM python:3.10

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

=======
FROM python:3.10

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

>>>>>>> 8276790fcfb9569ce09ab823b7fcecf686097c4c
CMD ["python", "./app/main.py"]