from rest_framework import serializers

from abundantia_api.common.serializers import BaseReadSerializer

from .models import Currency, Quotation


class CurrencyReadSerializer(BaseReadSerializer):
    class Meta:
        model = Currency
        fields = ["code", "name", "is_active", "is_cryptocurrency"]


class QuotationReadSerializer(BaseReadSerializer):
    code = serializers.SerializerMethodField("get_currency_code")
    name = serializers.SerializerMethodField("get_currency_name")

    class Meta:
        model = Quotation
        fields = ["code", "name", "amount", "variation"]

    def get_currency_code(self, obj):
        return obj.currency.code

    def get_currency_name(self, obj):
        return obj.currency.name


class CurrencyWithQuotationSerializer(BaseReadSerializer):
    quotations = QuotationReadSerializer(many=True)

    class Meta:
        model = Currency
        fields = ["code", "name", "is_active", "is_cryptocurrency", "quotations"]
