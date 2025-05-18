import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}, "description": "Transaction 1"},
        {"id": 2, "operationAmount": {"currency": {"code": "EUR"}}, "description": "Transaction 2"},
        {"id": 3, "operationAmount": {"currency": {"code": "USD"}}, "description": "Transaction 3"},
    ]


def test_filter_by_currency(sample_transactions):
    usd_transactions = filter_by_currency(sample_transactions, "USD")
    assert next(usd_transactions)["id"] == 1
    assert next(usd_transactions)["id"] == 3
    with pytest.raises(StopIteration):
        next(usd_transactions)


def test_transaction_descriptions(sample_transactions):
    descriptions = transaction_descriptions(sample_transactions)
    assert next(descriptions) == "Transaction 1"
    assert next(descriptions) == "Transaction 2"


@pytest.mark.parametrize(
    "start,end,expected",
    [(1, 1, "0000 0000 0000 0001"), (9999, 10000, ["0000 0000 0000 9999", "0000 0000 0001 0000"])],
)
def test_card_number_generator(start, end, expected):
    generator = card_number_generator(start, end)
    if isinstance(expected, list):
        assert next(generator) == expected[0]
        assert next(generator) == expected[1]
    else:
        assert next(generator) == expected
