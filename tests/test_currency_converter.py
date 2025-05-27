from unittest.mock import patch

import pytest

from src.external_api.currency_converter import convert_to_rub


class TestCurrencyConverter:
    @pytest.mark.parametrize("transaction,expected", [
        ({"operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}, 100.0),
        ({"operationAmount": {"amount": "0", "currency": {"code": "RUB"}}}, 0.0),
    ])
    def test_rub_transaction(self, transaction, expected):
        assert convert_to_rub(transaction) == expected

    @patch('requests.get')
    def test_usd_conversion(self, mock_get):
        mock_get.return_value.json.return_value = {"rates": {"RUB": 75.5}}
        mock_get.return_value.status_code = 200

        transaction = {
            "operationAmount": {
                "amount": "10",
                "currency": {"code": "USD"}
            }
        }

        assert convert_to_rub(transaction) == 755.0
