from django.db import transaction

from .clients import HGBrasilClient

from ..base import BaseBackend

from ...models import Currency, Quotation


class HGBrasilBackend(BaseBackend):

    id = "hgbrasil"

    @transaction.atomic()
    def update(self):
        client = HGBrasilClient()

        currencies_queryset = Currency.objects.active()
        if currencies_queryset:
            response = client.get_quotations()

            dataset = []
            for currency in currencies_queryset:
                currency_info = self._get_currency_data(currency.code, response)

                amount = currency_info.get("buy")
                variation = currency_info.get("variation")

                insert_data = Quotation(
                    currency=currency, amount=amount, variation=variation
                )

                dataset.append(insert_data)

            if dataset:
                Quotation.objects.bulk_create(dataset)

    def _get_currency_data(self, needle, haystack):
        results = haystack.get("results")
        currencies = results.get("currencies")

        info = currencies.get(needle)

        return info
