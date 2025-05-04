import pytest


@pytest.fixture
def sample_cards():
    return ["7000792289606361", "1234567812345678", "1111222233334444"]  # Visa  # Mastercard  # Неизвестный тип


@pytest.fixture
def sample_accounts():
    return ["73654108430135874305", "12345678901234567890"]


@pytest.fixture
def sample_operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-02T15:30:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-03T09:15:00"},
    ]
