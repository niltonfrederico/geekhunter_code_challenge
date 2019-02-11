from abundantia_api.currency.backends.base import BaseClient


class FakeClient(BaseClient):
    def __init__(self):
        self.base_url = ""
        self.token = ""

    def get_fake(self):
        return {"status": True}
