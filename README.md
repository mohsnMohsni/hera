# CLASSIMAX Shop

Buy or sell and enjoy. Develope online markting with Django base backend and js/jquery base front.

## Technologies

Technologies that are use in this project

* Django
* RESTapi
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

```
pip3 install -r requirements.txt
```

Run manage.py migrate 

```bash
python3 manage.py migrate
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
