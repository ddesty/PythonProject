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
```