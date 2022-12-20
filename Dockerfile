FROM python:3.8-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN echo 'nameserver 185.51.200.2'>>/etc/resolv.conf && apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add gettext

RUN pip install --upgrade pip
COPY ./requirements .
RUN pip install -r requirements/production.txt

COPY ./datadump.json .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY . .

ENTRYPOINT [ "./scripts/entrypoint.sh" ]
