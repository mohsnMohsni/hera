# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set shecan and then install wheel,
# install postgresql
# install psycopg2 for postgresql
# install pillow for images
RUN echo 'nameserver 185.51.200.2'>>/etc/resolv.conf && apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps \ 
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy data json file
COPY ./datadump.json .

# copy entrypoint file and change file mode
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# copy project
COPY . .

ENTRYPOINT [ "/entrypoint.sh" ]