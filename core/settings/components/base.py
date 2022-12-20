# Standard imports
from pathlib import Path
from easy_thumbnails.conf import Settings as ThumbnailSettings


BASE_DIR = Path(__file__).resolve().parent.parent.parent

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

# Auth Config
LOGIN_URL = 'account:login'
AUTH_USER_MODEL = 'accounts.User'

STATIC_URL = '/static/'

# Media Config
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Internationalization Config
# https://docs.djangoproject.com/en/3.1/topics/i18n/
LANGUAGES = (
    ('en', 'English'),
    ('fa', 'Persian'),
)
LANGUAGE_CODE = 'fa'
LOCALE_PATHS = [BASE_DIR / 'locale']
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

THUMBNAIL_PROCESSORS = (
                           'image_cropping.thumbnail_processors.crop_corners',
                       ) + ThumbnailSettings.THUMBNAIL_PROCESSORS
IMAGE_CROPPING_SIZE_WARNING = True
