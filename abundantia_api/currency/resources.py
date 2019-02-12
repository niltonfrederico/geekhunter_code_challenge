from rest_framework.decorators import action
from rest_framework.response import Response

from abundantia_api.common.viewsets import BaseViewSet

from .serializers import (
    CurrencyReadSerializer,
    CurrencyWithQuotationSerializer,
    QuotationAnalyticsSerializer,
)

from .models import Currency


class CurrencyViewSet(BaseViewSet):
    """
    retrieve:
    Returns information on a given existing currency.

    list:
    Return a list of all the existing currencies.

    create:
    Create a new currency instance.

    update:
    Updates a new currency instance.

    quotations:
    Returns information on a given existing currency with its quotations.

    analytics:
    Returns analytics information on a given existing currency.
    """

    serializers = {
        "default": CurrencyReadSerializer,
        "quotations": CurrencyWithQuotationSerializer,
        "analytics": QuotationAnalyticsSerializer,
    }

    lookup_field = "code"

    queryset = Currency.objects.prefetch_related("quotations").all()
    http_method_names = ["get", "put", "post"]

    ordering_fields = ("code",)
    ordering = ("code",)

    @action(detail=True, methods=["get"], url_path="quotations")
    def quotations(self, request, pk=None, **kwargs):
        currency = self.get_object()
        context = self.get_serializer_context()
        serializer = self.get_serializer(instance=currency, context=context)
        return Response(serializer.data)

    @action(detail=True, methods=["get"], url_path="analytics")
    def analytics(self, request, pk=None, **kwargs):
        currency = self.get_object()
        context = self.get_serializer_context()
        serializer = self.get_serializer(instance=currency, context=context)
        return Response(serializer.data)
