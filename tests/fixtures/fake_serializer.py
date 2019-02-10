from abundantia_api.common.serializers import BaseReadSerializer
from abundantia_api.currency.models import Currency


class FakeReadSerializer(BaseReadSerializer):
    class Meta:
        model = Currency
        fields = ["code", "name", "is_active"]
