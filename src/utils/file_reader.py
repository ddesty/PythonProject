import json
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """Читает JSON-файл и возвращает список словарей."""
    path = Path(file_path)

    # Проверка существования файла
    if not path.exists():
        return []

    # Проверка, что файл не пустой
    if path.stat().st_size == 0:
        return []

    try:
        # Чтение и парсинг файла
        with path.open('r', encoding='utf-8') as file:
            data = json.load(file)

        # Гарантируем, что возвращаем список
        return data if isinstance(data, list) else []

    except (json.JSONDecodeError, UnicodeDecodeError):
        return []
