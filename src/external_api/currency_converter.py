import os
from typing import Dict
from typing import Optional

import requests
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env


def convert_to_rub(transaction: Dict) -> Optional[float]:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными транзакции

    Returns:
        Сумма в рублях (float) или None при ошибках
    """
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]

        if currency == "RUB":
            return amount

        if currency in ("USD", "EUR"):
            api_key = os.getenv("EXCHANGE_RATE_API_KEY")
            if not api_key:
                raise ValueError("API key not found")

            response = requests.get(
                f"https://api.apilayer.com/exchangerates_data/latest?base={currency}",
                headers={"apikey": api_key},
                timeout=10
            )
            response.raise_for_status()

            rate = float(response.json()["rates"]["RUB"])  # Явное преобразование в float
            return round(amount * rate, 2)

        return None  # Для других валют

    except (KeyError, requests.RequestException, ValueError, TypeError):
        return None
