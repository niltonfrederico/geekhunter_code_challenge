from decimal import Decimal
from unittest import mock

import pytest
import vcr

from autofixture import AutoFixture
from hamcrest import assert_that, has_entries, has_items

from abundantia_api.currency.tasks import task_update_all_currencies_quotations
from abundantia_api.currency.backends.hgbrasil.backends import HGBrasilBackend


pytestmark = pytest.mark.django_db


def test_task_quotations_update():
    with mock.patch.object(HGBrasilBackend, "update", return_value=True) as mock_method:
        task_update_all_currencies_quotations()

        mock_method.assert_called_once()
