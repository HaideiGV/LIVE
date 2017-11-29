"""
Django settings for liveproject project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z1#6litaz4a3p0=*q#vxa$4rch-e@mh01f_*tcko8x+mdc6!)$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['glacial-bastion-94113.herokuapp.com', 'localhost', '*', '127.0.0.1', '0.0.0.0']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'liveupdate',
    'kombu.transport.django',
    'opbeat.contrib.django',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
)

OPBEAT = {
    'ORGANIZATION_ID': '419beab043604b6da4360b71acfe5813',
    'APP_ID': '83626ae470',
    'SECRET_TOKEN': '0671c09a0ee5f47c463ca793bae2e32f3ee48869',
}

ROOT_URLCONF = 'liveproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
)

WSGI_APPLICATION = 'liveproject.wsgi.application'


# if sys.platform == 'win32':
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         }
#     }
# elif sys.platform == 'linux2':
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': 'liveupdate',
#         }
#     }

# local
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'live',
#         'USER': 'live',
#         'PASSWORD': 'live',
#         'HOST': 'localhost',
#         'PORT': 5432
#     }
# }

#
# #heroku configs haideigv
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'd12sa18ng59qbd',
#         'USER': 'jtjmzihicddigb',
#         'PASSWORD':'Q2XfgklhLmKVJSZkm3yxtQZWN7',
#         'HOST': 'ec2-54-235-153-179.compute-1.amazonaws.com',
#         'PORT': '',
#     }
# }

# gaydeyvo
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbf8h88202hudn',
        'USER': 'sbmbrqjijjxtnh',
        'PASSWORD': 'fe2ae896fdef191b8bcf2d6d25244f403c7570e61e034b316db391a00cd74a34',
        'HOST': 'ec2-54-235-210-115.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}





# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

STATIC_ROOT = '/static/'

MEDIA_ROOT = '/static/files/'


AUTHENTICATION_BACKENDS = (
   'django.contrib.auth.backends.ModelBackend',
)