# Standard imports
import os

# Third-party imports.
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path='envs/.env.development')

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = True

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['*']

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

STATICFILES_DIRS = [BASE_DIR / 'static']
