from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY", default="123")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

STATIC_ROOT = "./static/"

MONGODB_NAME = env.str("MONGODB_NAME")
MONGODB_HOST = env.str("MONGODB_HOST")

DATABASES = {
    "default": {"ENGINE": "djongo", "NAME": MONGODB_NAME, "HOST": MONGODB_HOST}
}

# CELERY
AWS_ACCESS_ID = env.str("AWS_ACCESS_ID")
AWS_SECRET_KEY = env.str("AWS_SECRET_KEY")

CELERY_BROKER_URL = "sqs://{access_id}:{secret}@".format(
    access_id=AWS_ACCESS_ID, secret=AWS_SECRET_KEY
)
CELERY_RESULT_BACKEND = None
CELERY_BEAT_SCHEDULE = {
    "currency-fetch-data": {
        "task": "abundantia_api.currency.tasks.task_update_all_currencies_quotations",
        "schedule": crontab(hour="*/1", minute=0),
    }
}
CELERY_TIMEZONE = TIME_ZONE

# HGBRASIL API
HGBRASIL_API_URL = env.str("HGBRASIL_API_URL", default="https://api.hgbrasil.com/{}")
HGBRASIL_API_TOKEN = env.str("HGBRASIL_API_TOKEN", "123")

