import os
from pathlib import Path

# Load Environment variable
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


load_dotenv(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

DEBUG = True if os.getenv("DEBUG") == "True" else False
SECRET_KEY = os.getenv("SECRET_KEY")
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # My Apps
    "authentication",
    "project_catalog",
    # 3rd Party Apps
    "phonenumber_field",
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

ROOT_URLCONF = "csec_project_catalog.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "csec_project_catalog.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# Loading Database Settings from .env file
DB_CONFIG = {"ENGINE": os.getenv("ENGINE"), "NAME": os.getenv("NAME")}

if DB_CONFIG["ENGINE"] and "sqlite3" not in DB_CONFIG["ENGINE"]:
    DB_CONFIG["USER"] = os.getenv("USER")
    DB_CONFIG["PASSWORD"] = os.getenv("PASSWORD")
    DB_CONFIG["HOST"] = os.getenv("HOST")
    DB_CONFIG["PORT"] = os.getenv("PORT")

if DB_CONFIG["NAME"] == "db.sqlite3":
    DB_CONFIG["NAME"] = os.path.join(BASE_DIR, "db.sqlite3")

DATABASES = {"default": DB_CONFIG}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Setting Default user model
AUTH_USER_MODEL = "authentication.User"

LOGIN_REDIRECT_URL = "profile"
LOGIN_URL = "login"
LOGOUT_URL = "logout"
