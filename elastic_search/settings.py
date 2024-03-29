"""
Django settings for elastic_search project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import django
from django.utils.encoding import force_str
django.utils.encoding.force_text = force_str
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h2%%w^!n#(ce9#p)&jf6_%-fje*b^zi+t=i&4picrkp^$e!z_c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'django_elasticsearch_dsl',
    'django_elasticsearch_dsl_drf',

    # Local apps
    'cars',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'elastic_search.urls'

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

WSGI_APPLICATION = 'elastic_search.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

IS_MONGO = True
if not IS_MONGO:
    DATABASES = {
		'default': {
		    'ENGINE': 'django.db.backends.sqlite3',
		    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		}
		# ,
		# 'default2': {
		#     'ENGINE': 'django.db.backends.postgresql',
		#     'NAME': 'postgres',
		#     'USER': 'postgres',
		#     'PASSWORD': 'postgres',
		#     'HOST': 'db',
		#     'PORT': '5432',
		# }
	}
else:
    # pip install pymongo==3.12.3
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'mydatabase',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                # 'host': '0.0.0.0',
                'host': 'mongodb',
                'port': 27017,
                'username': 'root',
                'password': 'rootpassword',
                'authSource': 'admin',
                'authMechanism': 'SCRAM-SHA-1'
            }
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# Elasticsearch configuration
ELASTICSEARCH_DSL = {
    'default': {
        # 'hosts': 'localhost:9200',
        'hosts': 'elasticsearch:9200'
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
