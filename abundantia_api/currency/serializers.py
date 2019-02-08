from abundantia_api.common.serializers import BaseReadSerializer


class CurrencyReadSerializer(BaseReadSerializer):
    class Meta:
        fields = ["code", "name", "is_active"]
