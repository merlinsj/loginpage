"""
Django settings for points_tracker project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
from pathlib import Path

# Custom User Model
AUTH_USER_MODEL = 'accounts.CustomUser'  # Ensure CustomUser model is defined in the accounts app

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret Key (Remember to use a proper secret key in production)
SECRET_KEY = 'django-insecure-9dtxx*kkat1yj(^_&pkwk&7iov9l*bx-=$-1-#=y%)@3aov-sp'

# Debugging Mode (Don't use DEBUG=True in production)
DEBUG = True

# Allowed Hosts (Set this in production)
ALLOWED_HOSTS = []

# Applications (Installed apps including REST framework, CORS headers, custom accounts)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # For API views
    'rest_framework.authtoken',  # For token authentication (you can remove if you're using JWT)
    'accounts',  # Your custom app for handling users
    'corsheaders',  # To handle CORS for cross-origin requests
]

# Middleware for handling requests, security, and CORS
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Middleware to allow CORS
]

# URL Configuration
ROOT_URLCONF = 'points_tracker.urls'

# Template Settings (If you're using HTML templates in Django, configure here)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Empty if using app-level templates
        'APP_DIRS': True,  # Ensure this is True to look for templates within each app
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

# WSGI Application
WSGI_APPLICATION = 'points_tracker.wsgi.application'

# Database Configuration (SQLite is good for development, but use Postgres or MySQL for production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password Validation (You can modify or extend these based on your security requirements)
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

# Localization Settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'  # URL for serving static files
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Location where static files are collected for production

# Directory for additional static files (useful for development)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# CORS Settings to allow requests from your React app (Change for production)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Allowing localhost:3000 for development
]
CORS_ALLOW_ALL_ORIGINS = True  # Enable if you want to allow all origins for development

# JWT Authentication (for using JWT tokens in API authentication)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# Media Files Configuration (for file uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type (Auto-incrementing integer or BigAutoField)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
