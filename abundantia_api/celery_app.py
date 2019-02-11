import os

from celery import Celery
from django.conf import settings

from celery.app import default_app as app

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "abundantia_api.settings.development")

app = Celery("abundantia_app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
