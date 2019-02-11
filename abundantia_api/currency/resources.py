from abundantia_api.common.viewsets import BaseViewSet

from .serializers import CurrencyReadSerializer

from .models import Currency


class CurrencyViewSet(BaseViewSet):
    serializers = {"default": CurrencyReadSerializer}

    queryset = Currency.objects.all()
    http_method_names = ["get", "put", "post"]
