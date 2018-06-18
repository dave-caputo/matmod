
from .base import *

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'


# Postgres database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'matmod_dev',
        'USER': 'davecaputo',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
