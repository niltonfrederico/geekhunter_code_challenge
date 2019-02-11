from django.views.generic import View
from django.conf.urls import url, include
from django.http import HttpResponse

from .currency.urls import router as currency_router


class PingView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("pong")


urlpatterns = [
    url(r"^ping/$", PingView.as_view()),
    # currencies
    url(r"^currencies/", include((currency_router.urls, "currencies"))),
]
