"""Модуль для обработки информации о счетах и картах."""

from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета из входной строки.

    Args:
        data (str): Строка с типом и номером, например "Visa Platinum 7000792289606361" или "Счет 73654108430135874305".

    Returns:
        str: Строка с замаскированным номером.
    """
    if data.startswith("Счет"):
        parts = data.split()
        number = parts[-1]
        masked = get_mask_account(int(number))
        return f"Счет {masked}"
    else:
        *name_parts, number = data.split()
        masked = get_mask_card_number(int(number))
        name = " ".join(name_parts)
        return f"{name} {masked}"

from datetime import datetime

def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата "2024-03-11T02:26:18.671407" в формат "ДД.ММ.ГГГГ".

    Args:
        date_str (str): Строка с датой в формате "2024-03-11T02:26:18.671407".

    Returns:
        str: Дата в формате "ДД.ММ.ГГГГ".
    """
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")
