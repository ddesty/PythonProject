from src.search_operations import filter_by_description


def test_filter_by_description():
    transactions = [
        {'description': 'Перевод организации'},
        {'description': 'Перевод с карты на карту'},
        {'description': 'Открытие вклада'}
    ]

    result = filter_by_description(transactions, 'перевод')
    assert len(result) == 2
    assert all('Перевод' in t['description'] for t in result)
