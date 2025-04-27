from datetime import datetime
from typing import List
from typing import TypedDict


class Operation(TypedDict):
    id: int
    state: str
    date: str


def filter_by_state(operations: List[Operation], state: str = "EXECUTED") -> List[Operation]:
    """
    Фильтрует список операций по статусу (EXECUTED или CANCELED).

    Args:
        operations: Список операций (каждая операция — словарь).
        state: Статус для фильтрации (по умолчанию "EXECUTED").

    Returns:
        Отфильтрованный список операций.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: List[Operation], reverse: bool = True) -> List[Operation]:
    """
    Сортирует операции по дате (новые сверху или снизу).

    Args:
        operations: Список операций.
        reverse: Если True — новые сверху (по умолчанию True).

    Returns:
        Отсортированный список.
    """
    return sorted(operations, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
