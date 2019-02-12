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


class QuotationAnalyticsSerializer(serializers.ModelSerializer):
    last_day = serializers.SerializerMethodField()
    last_week = serializers.SerializerMethodField()
    last_month = serializers.SerializerMethodField()

    class Meta:
        model = Currency
        fields = ["last_day", "last_week", "last_month"]

    def get_last_day(self, obj):
        return obj.get_last_day_quotation()

    def get_last_week(self, obj):
        return obj.get_last_week_quotation()

    def get_last_month(self, obj):
        return obj.get_last_month_quotation()


class CurrencyWithQuotationSerializer(BaseReadSerializer):
    quotations = QuotationReadSerializer(many=True)

    class Meta:
        model = Currency
        fields = ["code", "name", "is_active", "is_cryptocurrency", "quotations"]
