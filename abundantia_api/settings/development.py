from .base import *

INSTALLED_APPS = INSTALLED_APPS + ["django_extensions"]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "c@vc)dkhlqrutz3y$1y!7^1t_()a(y@$n3z-g@kgw_e$%=goq&"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    "default": env.db(
        default="djongo://root:abundantia@abundantia_mongo:27017/abundantia"
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
HGBRASIL_API_TOKEN = env.str("HGBRASIL_API_TOKEN", default="1cd8e6f4")

# Schedule
CELERY_BEAT_SCHEDULE = {
    "currency-fetch-data": {
        "task": "abundantia_api.currency.tasks.task_update_all_currencies_quotations",
        "schedule": crontab(hour="*/1", minute="0"),
    }
}
