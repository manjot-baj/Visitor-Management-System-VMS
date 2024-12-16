from .base import *

ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("DEV_DB_NAME"),
        "USER": config("DEV_DB_USER"),
        "PASSWORD": config("DEV_DB_PASSWORD"),
        "HOST": config("DEV_DB_HOST"),
        "PORT": config("DEV_DB_PORT"),
    },
}
