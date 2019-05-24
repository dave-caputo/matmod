# Settings for PythonAnywhere

from django.db.backends.mysql.base import DatabaseWrapper

from .base import *

DatabaseWrapper.data_types['DateTimeField'] = 'datetime'  # fix for MySQL 5.5


DEBUG = False

ALLOWED_HOSTS = ['davecaputo.pythonanywhere.com']

# Mysql database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'davecaputo$matmod',
        'USER': 'davecaputo',
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': 'davecaputo.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

SECRET_KEY = os.environ.get('SECRET_KEY', '')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
