import sys
import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 1

INSTALLED_APPS = [
    'graphene_django',
    'tests',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django_test.sqlite',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
    },
]

GRAPHENE = {
    'SCHEMA': 'tests.conf.schema_view.schema'
}

ROOT_URLCONF = 'tests.conf.urls'
