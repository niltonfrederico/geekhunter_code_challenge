import logging

from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from abundantia_api.celery_app import app
from abundantia_api.common.exceptions import ClientHttpException
from abundantia_api.common.tasks import AutologTask

from .backends import QuotationsBackendManager


logger = logging.getLogger(__name__)


@app.task(
    base=AutologTask,
    bind=True,
    logger=logger,
    autoretry_for=(ConnectionError, Timeout, TooManyRedirects, ClientHttpException),
    retry_backoff=15,
)
def task_update_all_currencies_quotations(self):
    backends = QuotationsBackendManager.get_backends()

    for backend in backends:
        backend.update()
