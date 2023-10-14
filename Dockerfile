FROM python:3.11.4

ENV PYTHONUNBUFFERED=1

WORKDIR /quiz_app

COPY . .

RUN pip install -r requirements.txt