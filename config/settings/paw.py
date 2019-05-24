# Settings for PythonAnywhere
from .base import *
import os


DEBUG = False

# Mysql database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'davecaputo$matmod',
        'USER': 'davecaputo',
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': 'davecaputo.mysql.pythonanywhere-services.com',
    }
}

SECRET_KEY = os.environ.get('SECRET_KEY', '')
