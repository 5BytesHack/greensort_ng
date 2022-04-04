FROM python:3.8.13-alpine3.14
ENV PYTHONUNBUFFERED 1
ENV IN_DOCKER 1

COPY requirements.txt /requirements.txt

RUN apk add --no-cache --virtual .build-deps build-base \
    && pip3 install pip --upgrade \
    && pip3 install -r /requirements.txt \
    && apk del .build-deps
    && docker-compose up
    && python3 xls_to_mongo.py

EXPOSE 8080

WORKDIR /app

ADD . /app

VOLUME /app

CMD python -m app.main