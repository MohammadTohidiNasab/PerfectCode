from . base import *


DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'usersDB', 
        'USER': 'PerfectCode', 
        'PASSWORD': 'pa$$word',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = [
    'http://127.0.0.1:8000',
]
