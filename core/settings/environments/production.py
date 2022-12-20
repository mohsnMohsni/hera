import os

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = False

SECRET_KEY = os.getenv('SECRET_KEY')


ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('NAME'),
            'HOST': os.getenv('HOST'),
            'PORT': 5432,
            'USER': os.getenv('USER'),
            'PASSWORD': os.getenv('PASSWORD'),
        }
    }

STATIC_ROOT = BASE_DIR / 'static'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_USE_TLS = True
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
