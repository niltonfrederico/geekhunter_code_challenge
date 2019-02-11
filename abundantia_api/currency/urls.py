from rest_framework_extensions.routers import ExtendedDefaultRouter

from .resources import CurrencyViewSet

router = ExtendedDefaultRouter()

router.register("", CurrencyViewSet, basename="currencies")
