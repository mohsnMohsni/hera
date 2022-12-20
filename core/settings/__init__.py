# Standard imports
from os import environ

# Third-party imports.
from split_settings.tools import include


ENV = environ.get('DJANGO_ENV') or 'development'

base_settings = [
    'components/*.py',
    'environments/{0}.py'.format(ENV),
]

include(*base_settings)
