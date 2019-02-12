import logging

from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from abundantia_api.celery_app import app
from abundantia_api.common.exceptions import ClientHttpException

from .backends import QuotationsBackendManager


logger = logging.getLogger(__name__)


@app.task(
    bind=True,
    autoretry_for=(ConnectionError, Timeout, TooManyRedirects, ClientHttpException),
    retry_backoff=15,
)
def task_update_all_currencies_quotations(self):
    backends = QuotationsBackendManager.get_backends()

    for backend_class in backends:
        backend = backend_class()
        backend.update()
