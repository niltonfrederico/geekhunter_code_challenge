from abundantia_api.currency.backends.base import BaseBackend


class FakeBackend(BaseBackend):
    def update(self):
        return True
