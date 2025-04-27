# 🏦 Bank Operations Widget

**Проект для обработки банковских операций.**  
Фильтрация по статусу (`EXECUTED`/`CANCELED`) и сортировка по дате.

## 📦 Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-username/bank-operations-widget.git
   cd bank-operations-widget
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
Запуск линтеров:
```bash
poetry run flake8    # Проверка стиля
poetry run mypy src  # Проверка типов
```