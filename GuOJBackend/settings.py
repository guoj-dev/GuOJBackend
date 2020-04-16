"""
Django settings for GuOJBackend project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, 'config.json'), 'rt') as f:
    config = json.load(f)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['SecretKey']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = config['AllowedHosts']


# Application definition

INSTALLED_APPS = [
    #'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'django_filters',
    #'gunicorn',
    'channels',
    'Databases',
    'Judgement',
    'API',
    'crispy_forms',
    'reversion',
    "django_apscheduler",
    'django_rest_passwordreset',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'GuOJBackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'GuOJBackend.wsgi.application'

ASGI_APPLICATION = "GuOJBackend.routing.application"

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config["Database"]["DatabaseName"],  
        'USER': config["Database"]["DatabaseUser"],  
        'PASSWORD': config["Database"]["DatabasePassword"],  
        'HOST': config["Database"]["DatabaseHost"],  
        'PORT': config["Database"]["DatabasePort"],  
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

SITE_ID = 1

AUTH_USER_MODEL = 'Databases.User'

ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

ACCOUNT_EMAIL_REQUIRED = True

EMAIL_HOST = config['Email']['EmailServer']

EMAIL_PORT = config['Email']['EmailPort']

EMAIL_HOST_USER = config['Email']['EmailUser']

EMAIL_HOST_PASSWORD = config['Email']['EmailPassword'] 

EMAIL_USE_SSL = config['Email']['UseSSL']

EMAIL_USE_TLS = config['Email']['UseTLS']

EMAIL_FROM = config['Email']['EmailFrom'] 

DEFAULT_FROM_EMAIL = config['Email']['DefaultEmailFrom'] 

ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN = 60

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1

ACCOUNT_EMAIL_VERIFICATION = "mandatory"

ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5

ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

OLD_PASSWORD_FIELD_ENABLED = True

ACCOUNT_ADAPTER = 'GuOJBackend.adapter.CustomAccountAdapter'

REST_AUTH_SERIALIZERS = {
    'PASSWORD_RESET_SERIALIZER': 'API.serializers.PasswordResetSerializer',
}