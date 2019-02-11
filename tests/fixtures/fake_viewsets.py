from abundantia_api.common.viewsets import BaseViewSet
from abundantia_api.currency.models import Currency

from .fake_serializers import FakeReadSerializer, FakeWriteSerializer


class FakeViewSet(BaseViewSet):
    serializers = {"default": FakeReadSerializer, "create": FakeWriteSerializer}

    queryset = Currency.objects.all()

    def create(self, request, *args, **kwargs):
        return True
