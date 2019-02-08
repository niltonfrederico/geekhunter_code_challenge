from django.conf.urls import url, include

from .currency.urls import router as currency_router

urlpatterns = [
    # currencies
    url(r"^/currencies/", include(currency_router.urls))
]
