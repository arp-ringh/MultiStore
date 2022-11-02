"""
Django settings for multishop project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-868&sb=h#d*ns02^(=20i&t&x+pfouxyw_p5&cymc33ruw^1n)"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.store.apps.StoreConfig",
    "apps.vendor.apps.VendorConfig",
    "apps.product.apps.ProductConfig",
    "apps.cart.apps.CartConfig",
    "apps.order.apps.OrderConfig",
    "apps.customers.apps.CustomersConfig",
    "crispy_forms",
    "corsheaders",
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",

]

ROOT_URLCONF = "multishop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.product.context_processors.bulk_categories",
                "apps.product.context_processors.bulk_subcategories",
                "apps.cart.context_processors.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "multishop.wsgi.application"
AUTH_USER_MODEL = 'store.CustomUser'


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

#CORS_ORIGIN_ALLOW_ALL = True
SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = 'cart'

STRIPE_PUB_KEY = 'pk_test_51LzKoHAU5Vcqx3suQD50KkWL8evRbRs1DUPKxgoEPtop0uSXWh1Ptoxseu9kZifNMPazJ7a3lkHu58iwRG7ASUhQ00qVbdiZxO'
STRIPE_SECRET_KEY = 'sk_test_51LzKoHAU5Vcqx3suyD7F3z1oV6Qi9x44XstXWBwNucoVqV6K9TbAMrNyYyI4ZuCuRAsSk16ZwqG0WvLIODGi038R00opH82F1E'



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
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


import os

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,"media")



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
