from typing import Dict
from typing import List

from src.category_counter import count_categories
from src.file_readers.universal_reader import read_csv_file
from src.file_readers.universal_reader import read_excel_file
from src.processing.filter import filter_by_state
from src.processing.sort import sort_by_date
from src.search_operations import filter_by_description
from src.utils.file_reader import read_json_file
from src.widget import get_date
from src.widget import mask_account_card


def get_transactions(file_type: str) -> List[Dict]:
    """Загружает транзакции из файла по типу."""
    file_path = input("Введите путь к файлу: ")
    if file_type == '1':
        return read_json_file(file_path)
    elif file_type == '2':
        return read_csv_file(file_path)
    elif file_type == '3':
        return read_excel_file(file_path)
    return []


def get_status() -> str:
    """Запрашивает и проверяет статус операций."""
    valid_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        status = input(
            "Введите статус (EXECUTED, CANCELED, PENDING): "
        ).upper()
        if status in valid_statuses:
            return status
        print(f"Статус '{status}' недоступен. Попробуйте снова.")


def print_transaction(transaction: Dict) -> None:
    """Выводит информацию о транзакции."""
    date = get_date(transaction['date'])
    amount = transaction['amount']
    currency = transaction['currency_code']

    print(f"{date} {transaction['description']}")

    if 'from' in transaction:
        print(f"{mask_account_card(transaction['from'])} -> ", end='')
    print(mask_account_card(transaction['to']))

    print(f"Сумма: {amount} {currency}\n")


def main():
    """Основная функция программы."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_type = input("Ваш выбор: ")
    transactions = get_transactions(file_type)

    status = get_status()
    filtered = filter_by_state(transactions, status)
    print(f"Операции отфильтрованы по статусу '{status}'")

    if input("Отсортировать операции по дате? (Да/Нет): ").lower() == 'да':
        reverse = input("По возрастанию или по убыванию? (возрастанию/убыванию): ") == 'убыванию'
        filtered = sort_by_date(filtered, reverse=reverse)

    if input("Выводить только рублевые транзакции? (Да/Нет): ").lower() == 'да':
        filtered = [t for t in filtered if t.get('currency_code') == 'RUB']

    if input("Фильтровать по слову в описании? (Да/Нет): ").lower() == 'да':
        word = input("Введите слово для поиска: ")
        filtered = filter_by_description(filtered, word)

    if not filtered:
        print("Не найдено ни одной транзакции, подходящей под ваши условия")
        return

    print(f"\nВсего банковских операций в выборке: {len(filtered)}\n")
    for t in filtered:
        print_transaction(t)

    if input("Показать статистику по категориям? (Да/Нет): ").lower() == 'да':
        stats = count_categories(filtered)
        print("\nСтатистика по категориям:")
        for cat, count in stats.items():
            print(f"{cat}: {count} операций")


if __name__ == "__main__":
    main()
