from ..base import BaseClient


class HGBrasilClient(BaseClient):
    def __init__(self):
        self.base_url = ""
        self.token = ""

    def get_quotations(self):
        endpoint = self.build_url(
            "/finance?array_limit=1&fields=only_results,bitcoin,currencies"
        )

        return self.get(endpoint)
