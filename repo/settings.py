#-*- coding: utf-8 -*-
"""
Django settings for repo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
os.path.join(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u3om#^gz6niz&@n&025vj#og5n#nc_a-p6+rdc!6o6ad$80!i('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#TEMPLATE_DEBUG = True
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = (
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'repo.helpApp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'repo.urls'

WSGI_APPLICATION = 'repo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Chongqing'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

ALLOWED_INCLUDE_ROOTS = (
    '/var/www/html/repo/log',
)

APPEND_SLASH = True

STATIC_URL = '/linux/'
#STATIC_URL = '/'
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), STATIC_URL.replace("/", "")),
)
STATIC_ROOT = '/var/www/html/repo/'
#MEDIA_ROOT = os.path.join(BASE_DIR, STATIC_URL.replace("/", ""))

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
)
