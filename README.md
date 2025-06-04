# 🏦 Bank Operations Widget

**Проект для обработки банковских операций.**  
Фильтрация по статусу (`EXECUTED`/`CANCELED`) и сортировка по дате.

## 📦 Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ddesty/PythonProject.git
   cd PythonProject
   ```
2. Установите зависимости через Poetry:
   ```bash
   poetry install
   ```
   Или через pip:
   ```bash
   pip install -r requirements.txt
   ```

## 🛠 Примеры использования
### Фильтрация операций
```python
from src.processing import filter_by_state

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2023-01-01"},
    {"id": 2, "state": "CANCELED", "date": "2023-01-02"}
]

# Только выполненные операции
filtered = filter_by_state(operations)
print(filtered)  # [{'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'}]
```

### Сортировка операций
```python
from src.processing import sort_by_date

# По умолчанию: новые сверху
sorted_ops = sort_by_date(operations)

# Старые сверху
sorted_asc = sort_by_date(operations, reverse=False)
```

## 🚀 Запуск
Если есть точка входа (`main.py`):
```bash
python main.py
```

## 🧪 Тестирование
```bash
# Запуск тестов
poetry run pytest

# С покрытием кода
poetry run pytest --cov=src --cov-report=html
```
**Покрытие:** 100% (актуально на 04.05.2025)

## 🌀 Модуль generators

### filter_by_currency
```python
from src.generators import filter_by_currency
usd_transactions = filter_by_currency(transactions, "USD")
print(next(usd_transactions))
```

### transaction_descriptions
```python
from src.generators import transaction_descriptions
for desc in transaction_descriptions(transactions):
    print(desc)
```

### card_number_generator
```python
from src.generators import card_number_generator
for card in card_number_generator(1, 5):
    print(card)  # 0000 0000 0000 0001 ... 0000 0000 0000 0005
```


## 🛠 Модуль decorators

### Декоратор `log`
Логирует вызовы функций. Пример использования:
```python
from src.decorators import log

@log(filename="app.log")
def calculate(a: int, b: int) -> int:
    return a + b

calculate(10, 20)  # Запись в app.log
```

## 📁 Поддержка разных форматов данных

Теперь проект поддерживает несколько форматов файлов с транзакциями:

### CSV
```python
from src.file_readers.universal_reader import read_csv_file
transactions = read_csv_file("data/transactions.csv")
```
### Excel (XLSX)
```python
from src.file_readers.universal_reader import read_excel_file
transactions = read_excel_file("data/transactions.xlsx")
```

## 🔍 Поиск и анализ операций

### Поиск по описанию
```python
from src.processing.search_operations import filter_by_description
result = filter_by_description(transactions, 'перевод')
```

## Статистика по категориям

```python
from src.processing.category_counter import count_categories
stats = count_categories(transactions)
```

### Основное меню
Запустите main.py для интерактивной работы с транзакциями.