from .base import * #noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="hAIEwJQcR9oyVRQAKGfVLAGzkJVeFd-qha3YQb6fO2Zz9i5ZTA0",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGNS=["http://localhost:8080"]