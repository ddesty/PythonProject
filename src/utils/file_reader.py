import json
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List

from . import logger


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей.

    Args:
        file_path: Путь к JSON-файлу

    Returns:
        Список словарей с данными или пустой список при ошибках
    """
    path = Path(file_path)

    try:
        if not path.exists():
            logger.error(f"Файл не найден: {file_path}")
            return []

        if path.stat().st_size == 0:
            logger.warning(f"Пустой файл: {file_path}")
            return []

        with path.open('r', encoding='utf-8') as file:
            data = json.load(file)

        logger.info(f"Успешно прочитан файл: {file_path}")
        return data if isinstance(data, list) else []

    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}: {str(e)}")
        return []
    except UnicodeDecodeError as e:
        logger.error(f"Ошибка кодировки файла {file_path}: {str(e)}")
        return []
    except Exception as e:
        logger.critical(f"Непредвиденная ошибка при чтении {file_path}: {str(e)}")
        return []
