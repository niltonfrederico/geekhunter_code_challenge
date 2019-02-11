from abundantia_api.common.serializers import BaseReadSerializer

from .models import Currency


class CurrencyReadSerializer(BaseReadSerializer):
    class Meta:
        model = Currency
        fields = ["code", "name", "is_active", "is_cryptocurrency"]
