import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


class TestMasks:
    """Тестирование функций маскировки."""

    def test_card_masking(self, sample_cards):
        """Проверка маскировки карт."""
        assert get_mask_card_number(sample_cards[0]) == "7000 79** **** 6361"
        assert get_mask_card_number(sample_cards[1]) == "1234 56** **** 5678"

    @pytest.mark.parametrize(
        "account, expected", [("73654108430135874305", "**4305"), ("12345678901234567890", "**7890")]
    )
    def test_account_masking(self, account, expected):
        """Параметризованный тест для счетов."""
        assert get_mask_account(account) == expected

    def test_empty_input(self):
        """Проверка обработки пустого ввода."""
        with pytest.raises(ValueError):
            get_mask_card_number("")
