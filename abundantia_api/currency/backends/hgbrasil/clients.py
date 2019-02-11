from django.conf import settings

from abundantia_api.common.exceptions import ClientHttpException

from ..base import BaseClient


HGBRASIL_API_URL = getattr(settings, "HGBRASIL_API_URL", "https://api.hgbrasil.com/{}")
HGBRASIL_API_TOKEN = getattr(settings, "HGBRASIL_API_TOKEN", "")


class HGBrasilClient(BaseClient):
    def __init__(self):
        self.base_url = HGBRASIL_API_URL
        self.token = HGBRASIL_API_TOKEN

    def get_quotations(self):
        endpoint = self.build_url(
            "finance?array_limit=1&fields=only_results,bitcoin,currencies"
        )

        response = self.get(endpoint)

        if response.status_code not in range(200, 299):
            raise ClientHttpException

        return response.json()
