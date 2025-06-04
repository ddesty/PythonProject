import re
from typing import Dict
from typing import List


def filter_by_description(transactions: List[Dict], search_str: str) -> List[Dict]:
    """
    Фильтрует транзакции по строке в описании с использованием регулярных выражений.

    Args:
        transactions: Список транзакций
        search_str: Строка для поиска в описании

    Returns:
        Отфильтрованный список транзакций
    """
    try:
        pattern = re.compile(search_str, re.IGNORECASE)
        return [t for t in transactions if 'description' in t and pattern.search(t['description'])]
    except re.error:
        return []
