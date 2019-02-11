from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY", default="123")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    "default": env.db(
        default="djongo://abundantia_api:XVqVnYnvBo6pH79z@cluster0-jhafu.mongodb.net/test?retryWrites=true"
    )
}

# CELERY
CELERY_BROKER_URL = env.str(
    "CELERY_BROKER_URL", default="redis://abundantia_redis:6379/0"
)
CELERY_RESULT_BACKEND = env.str(
    "CELERY_RESULT_BACKEND", default="redis://abundantia_redis:6379/1"
)
CELERY_BEAT_SCHEDULE = {}

# HGBRASIL API
HGBRASIL_API_URL = env.str("HGBRASIL_API_URL", default="https://api.hgbrasil.com/{}")
HGBRASIL_API_TOKEN = env.str("HGBRASIL_API_TOKEN", "123")
