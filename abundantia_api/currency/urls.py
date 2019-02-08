from rest_framework.routers import DefaultRouter

from .resources import CurrencyViewSet

router = DefaultRouter()

router.register("", CurrencyViewSet, basename="currencies")
