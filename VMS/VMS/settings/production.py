from .base import *

ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("PROD_DB_NAME"),
        "USER": config("PROD_DB_USER"),
        "PASSWORD": config("PROD_DB_PASSWORD"),
        "HOST": config("PROD_DB_HOST"),
        "PORT": config("PROD_DB_PORT"),
    }
}
