import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date


class TestProcessing:
    """Тестирование обработки операций."""

    def test_filter_by_state(self, sample_operations):
        """Фильтрация по статусу."""
        executed = filter_by_state(sample_operations, "EXECUTED")
        assert len(executed) == 2
        assert all(op["state"] == "EXECUTED" for op in executed)

    @pytest.mark.parametrize(
        "reverse, first_date",
        [(True, "2023-01-03T09:15:00"), (False, "2023-01-01T12:00:00")],  # Новые сверху  # Старые сверху
    )
    def test_sort_by_date(self, sample_operations, reverse, first_date):
        """Параметризованный тест сортировки."""
        sorted_ops = sort_by_date(sample_operations, reverse)
        assert sorted_ops[0]["date"] == first_date
