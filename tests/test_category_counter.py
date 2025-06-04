from src.category_counter import count_categories


def test_count_categories():
    transactions = [
        {'description': 'Перевод'},
        {'description': 'Перевод'},
        {'description': 'Покупка'}
    ]

    result = count_categories(transactions)
    assert result == {'Перевод': 2, 'Покупка': 1}
