import pytest

from src.widget import get_date
from src.widget import mask_account_card


class TestWidget:
    """Тестирование виджета."""

    @pytest.mark.parametrize(
        "input_str, expected",
        [
            ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
            ("Счет 73654108430135874305", "Счет **4305"),
        ],
    )
    def test_mask_account_card(self, input_str, expected):
        """Тест маскировки карт/счетов в строке."""
        assert mask_account_card(input_str) == expected

    def test_get_date(self):
        """Тест форматирования даты."""
        assert get_date("2023-01-01T12:00:00") == "01.01.2023"
