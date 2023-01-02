"""
Django settings for lifang_django project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-tjx9zo&%c*^2hj8v$+-*@-eyxigt_0#rd*ga#9b$hbpnnj5p=@"

# SECURITY WARNING: don't run with debug turned on in production! 리눅스 서버 연결을 위한 디버그 
DEBUG = True

# 리눅스 서버 연결을 위한 디버그 설정

# if ENV == "dev":
#     DEBUG = True
# elif:
#     DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

BATON = {    
    'SITE_HEADER': '리팡 관리자',
    'SITE_TITLE': '리팡 관리자',
    'INDEX_TILTE': '리팡 관리자',
    'SUPPORT_HREF': 'http://naver.com',
    'COPYRIGHT' : 'copyright © 2023 lifang admin',
    'POWERED_BY': '<a href="http://naver.com">리팡 홈페이지</a>',
    'MENU_TITLE': '리팡 어드민',
    'MENU': (
    { 'type': 'title', 'label': 'main', 'apps': ('lifanguser','order', 'product') },
    {
        'type': 'app',
        'name': 'lifanguser',
        'label': '리팡사용자',
        'icon': 'fa fa-lock',
        'models': (
            {
                'name': 'lifanguser',
                'label': '리팡사용자'
            },
   
        )
    },
    { 'type': 'free', 'label': '주문', 'default_open': True, 'children': [
        { 'type': 'model', 'label': '주문', 'name': 'order', 'app': 'order' },
        { 'type': 'free', 'label': '주문 날짜뷰', 'url': '/admin/order/order/date_view/' },
    ] 
    
    },         
   
        
      {
        'type': 'app',
        'name': 'product',
        'label': '상품',
        'models': (
            {
                'name': 'product',
                'label': '상품'
            },
   
        )
     },        
        
    
     { 'type': 'free', 'label': '매뉴얼', 'url': '/admin/manual/' 
     
     
     
     },
   
    ),

}


INSTALLED_APPS = [
    'baton',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "rest_framework",
    "lifanguser.apps.LifanguserConfig",
    "order.apps.OrderConfig",
    "product.apps.ProductConfig",    
    'baton.autodiscover',        
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "lifang_django.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [ os.path.join(BASE_DIR, 'templates')
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "lifang_django.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

import os

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles')


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
