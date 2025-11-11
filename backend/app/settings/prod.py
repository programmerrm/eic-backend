#########################################################
"""
Production settings configuration
"""
#########################################################
from app.settings.base import *

# BASE CONFIGRATION
DEBUG = env('DEBUG')
ALLOWED_HOSTS = ['*']
SECRET_KEY = env('SECRET_KEY')

# DATABASE CONFIGRATION
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}
