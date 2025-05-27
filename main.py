from src.external_api.currency_converter import convert_to_rub
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.utils.file_reader import read_json_file

transactions = read_json_file("data/operations.json")
executed_transactions = filter_by_state(transactions)
sorted_transactions = sort_by_date(executed_transactions)

for transaction in sorted_transactions:
    amount_rub = convert_to_rub(transaction)
    print(f"{transaction['date']}: {amount_rub} RUB")
