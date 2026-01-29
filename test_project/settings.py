from pathlib import Path
import os
from datetime import timedelta
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv('DEBUG', 'False').strip().lower() in ('true', '1', 'yes')
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")
CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # library app
    'rest_framework', 'rest_framework_simplejwt',
    'corsheaders', 'django_extensions', 'django_filters',
    'rest_framework_simplejwt.token_blacklist',
    
    'core',
    
    
]


# ================================================================================
# ==================== Rest Frame Work Configurations Start====================
ENABLE_BROWSABLE_API = os.getenv('ENABLE_BROWSABLE_API', 'False') == 'True'
if ENABLE_BROWSABLE_API:
    DEFAULT_RENDERER_CLASSES_ = [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
else:
    DEFAULT_RENDERER_CLASSES_ = [
        'rest_framework.renderers.JSONRenderer'
    ]

REST_FRAMEWORK = {
    # 'DEFAULT_RENDERER_CLASSES': DEFAULT_RENDERER_CLASSES_,
    'rest_framework.renderers.BrowsableAPIRenderer'
    
    'EXCEPTION_HANDLER': 'find_worker_config.exceptions.custom_exception_handler',
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 5,
    
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
    'BLACKLIST_AFTER_ROTATION': True,
    'ROTATE_REFRESH_TOKENS': True,
    # 'ROTATE_REFRESH_TOKENS': False,
    
    'ACCESS_TOKEN_LIFETIME': timedelta(days=60),
    # 'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=60),
    
    "UPDATE_LAST_LOGIN": True,
}

CORS_ORIGIN_ALLOW_ALL = True

# ==================== Rest Frame Work Configurations End====================
# ================================================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'test_project.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'GMT'
USE_I18N = True
USE_TZ = True


STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.getenv('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'media'))

AUTH_USER_MODEL = "core.User"
