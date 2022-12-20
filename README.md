# CLASSIMAX Shop
Buy or sell and enjoy. Develop online marketing with Django base backend and js/jquery base front.

[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

# core based on:
  - Python 3.8 version
  - Django 3.1 version


## Technologies

Technologies that are use in this project

* Django
* RESTapi
* Redis
* Bootstrap
* SCSS
* JQuery
* Docker
* Shell-script

## Launch

At first rename `env-sample` to `.env` and set secret key and debug mode

```bash
mv env-sample .env
```

Install python3 and pip3

```bash
sudo apt install -y python3; sudo apt insall -y python3-pip
```

It's opptional to run on **virtualenv**

```bash
sudo apt install -y python3-venv && python3 -m venv venv; source venv/bin/activate
```

Install requirements.txt

```bash
pip3 install -r requirements.txt
```

Run manage.py migrate

```bash
python3 manage.py migrate
```

Compile messages to binary code to enable multi-languages

```bash
python3 manage.py compilemessages
```

## Launch in docker for production mode

Image will be use:

* postgres:12.0-alpine
* python:3.8-alpine
* nginx:1.19.0-alpine

Install **Docker** from [Get-Docker](https://docs.docker.com/get-docker/)

Install **Docker Compose** from [Get-Docker-compose](https://docs.docker.com/compose/install/)

Run `docker-compose build` to build images

```bash
docker-compose build
```

Run `docker-compose up` to run project

```bash
docker-compose up -d
```
