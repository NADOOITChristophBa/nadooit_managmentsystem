"""
Django settings for NADOOIT project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Production
# config_json = Path.home().joinpath('NADOOIT').joinpath('config').joinpath('config.json')
# Development
config_json = (
    Path.home().joinpath("NADOOIT").joinpath("config").joinpath("config_dev.json")
)

with open(config_json) as config_file:
    config = json.load(config_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-r_!=ggg^bx66haa&uq%q9!u1)%rax+f((om7_!c3qn)8#ch3#t'
SECRET_KEY = config.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "sslserver",
    "django_is_url_active_templatetag",
    "grappelli",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "nadooit_auth",
    "nadooit_api_key",
    "nadooit_crm",
    "nadooit_hr",
    "nadooit_time_account",
    "nadooit_workflow",
    "nadooit_network",
    "nadooit_program",
    "nadooit_program_ownership_system",
    "nadooit_api_executions_system.apps.NadooitApiExecutionsSystemConfig",
    "nadooit_website.apps.NadooitWebsiteConfig",
    "nadooit_os",
    "rest_framework",
    "pwa",
    "debug_toolbar",
    "django_extensions",
    "mfa",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
ROOT_URLCONF = "nadooit.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "nadooit.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config.get("POSTGRE_SQL_DB_NAME"),
        "USER": config.get("POSTGRE_SQL_DB_USER"),
        "PASSWORD": config.get("POSTGRE_SQL_DB_PASSWORD"),
        "HOST": "localhost",
        "PORT": config.get("POSTGRE_SQL_DB_PORT"),
    }
}

# Default user model
AUTH_USER_MODEL = "nadooit_auth.User"

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

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
INTERNAL_IPS = [
    "127.0.0.1",
]

STATIC_URL = "/static/"
# OLD STATICFILES_DIRS = [BASE_DIR / "static", "/var/www/static/"]
# according to doc STATIC_ROOT = "/var/www/nadooit.de/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [(os.path.join(BASE_DIR, "static")), "/var/www/static/"]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# PWA settings
PWA_SERVICE_WORKER_PATH = os.path.join(
    BASE_DIR, "static", "js", "nadooit_serviceworker.js"
)
PWA_APP_NAME = "NADOOIT"
PWA_APP_DESCRIPTION = "NADOOIT PWA"
PWA_APP_THEME_COLOR = "#000000"
PWA_APP_BACKGROUND_COLOR = "#ffffff"
PWA_APP_DISPLAY = "standalone"
PWA_APP_SCOPE = "/"
PWA_APP_ORIENTATION = "any"
PWA_APP_START_URL = "/nadooit-os"
PWA_APP_STATUS_BAR_COLOR = "default"
PWA_APP_ICONS = [{"src": "static/appicon/maskable_icon_x192.png", "sizes": "192x192"}]
PWA_APP_ICONS_APPLE = [
    {"src": "static/appicon/maskable_icon_x192.png", "sizes": "192x192"}
]
PWA_APP_SPLASH_SCREEN = [
    {
        "src": "static/splashscreen/nadooit.png",
        "media": "(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)",
    }
]
PWA_APP_DIR = "ltr"
PWA_APP_LANG = "de-DE"


# FIDO2
MFA_UNALLOWED_METHODS = ()  # Methods that shouldn't be allowed for the user
MFA_LOGIN_CALLBACK = "nadooit_auth.views.log_user_in"  # A function that should be called by username to login the user in session
MFA_RECHECK = True  # Allow random rechecking of the user
MFA_RECHECK_MIN = 10  # Minimum interval in seconds
MFA_RECHECK_MAX = 30  # Maximum in seconds
MFA_QUICKLOGIN = True  # Allow quick login for returning users by provide only their 2FA
MFA_HIDE_DISABLE = ("FIDO2",)  # Can the user disable his key (Added in 1.2.0).
MFA_OWNED_BY_ENTERPRISE = False  # Who owns security keys

TOKEN_ISSUER_NAME = "nadooit"  # TOTP Issuer name

if DEBUG:
    U2F_APPID = "https://localhost"  # URL For U2F
    FIDO_SERVER_ID = (
        "localhost"  # Server rp id for FIDO2, it is the full domain of your project
    )
else:
    U2F_APPID = "https://nadooit.de"  # URL For U2F
    FIDO_SERVER_ID = "nadooit.de"

FIDO_SERVER_NAME = "nadooit"
MFA_REDIRECT_AFTER_REGISTRATION = (
    "nadooit_os:nadooit-os"  # Allows Changing the page after successful registeration
)
MFA_SUCCESS_REGISTRATION_MSG = (
    "Schlüssel erfolgreich registriert"  # The text of the link
)
