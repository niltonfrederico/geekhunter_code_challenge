from rest_framework.decorators import detail_route
from rest_framework.response import Response

from abundantia_api.common.viewsets import BaseViewSet

from .serializers import CurrencyReadSerializer, CurrencyWithQuotationSerializer

from .models import Currency


class CurrencyViewSet(BaseViewSet):
    serializers = {
        "default": CurrencyReadSerializer,
        "quotations": CurrencyWithQuotationSerializer,
    }

    queryset = Currency.objects.prefetch_related("quotations").all()
    http_method_names = ["get", "put", "post"]

    ordering_fields = ("code",)
    ordering = ("code",)

    @detail_route(methods=["get"], url_path="quotations")
    def quotations(self, request, pk=None, **kwargs):
        currency = self.get_object()
        serializer = self.get_serializer()
        return Response(serializer.data)
