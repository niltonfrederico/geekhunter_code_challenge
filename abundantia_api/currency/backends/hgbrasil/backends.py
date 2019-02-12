from django.db import transaction

from .clients import HGBrasilClient

from ..base import BaseBackend

from ...models import Currency, Quotation


class HGBrasilBackend(BaseBackend):

    id = "hgbrasil"

    @transaction.atomic()
    def update(self):
        client = HGBrasilClient()

        currencies_queryset = self._get_currencies()
        if currencies_queryset:
            response = client.get_quotations()

            frozen_hash = hash(frozenset(response.items()))

            quotations_queryset = Quotation.objects.filter(unique_hash=frozen_hash)

            if quotations_queryset:
                return

            dataset = []
            for currency in currencies_queryset:
                currency_info = self._get_currency_data(currency.code, response)

                amount = currency_info.get("buy")
                variation = currency_info.get("variation")

                insert_data = Quotation(
                    backend_id=self.id,
                    currency=currency,
                    amount=amount,
                    variation=variation,
                )

                dataset.append(insert_data)

            if dataset:
                Quotation.objects.bulk_create(dataset)

    def _get_currency_data(self, needle, haystack):
        results = haystack.get("results")
        currencies = results.get("currencies")

        info = currencies.get(needle)

        return info
