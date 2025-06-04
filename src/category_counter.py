from collections import Counter
from typing import Dict
from typing import List


def count_categories(transactions: List[Dict]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям.

    Args:
        transactions: Список транзакций

    Returns:
        Словарь с количеством операций по категориям
    """
    descriptions = [t.get('description', 'Unknown') for t in transactions]
    return dict(Counter(descriptions))
