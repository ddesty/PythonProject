import logging
from pathlib import Path
from typing import Any
from typing import Dict
from typing import Hashable
from typing import List

import pandas as pd

logger = logging.getLogger(__name__)

# Определяем базовый путь к папке с данными
base_path = Path(r"C:\Users\Alexey\Desktop\PythonProject\data")


def read_csv_file() -> List[Dict[Hashable, Any]]:
    """
    Читает транзакции из CSV-файла.
    """
    file_path = base_path / "transactions.csv"
    try:
        if not file_path.exists():
            logger.error(f"CSV файл не найден: {file_path}")
            raise FileNotFoundError(f"Файл {file_path} не существует")

        df = pd.read_csv(
            file_path,
            sep=';',
            encoding='utf-8',
            parse_dates=['date'],
            dtype={'amount': float}
        )
        logger.info(f"Успешно прочитан CSV файл: {file_path}")
        return df.to_dict('records')

    except pd.errors.EmptyDataError:
        logger.error(f"CSV файл пустой: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Ошибка чтения CSV файла {file_path}: {str(e)}")
        raise


def read_excel_file() -> List[Dict[Hashable, Any]]:
    """
    Читает транзакции из Excel-файла.
    """
    file_path = base_path / "transactions_excel.xlsx"
    try:
        if not file_path.exists():
            logger.error(f"Excel файл не найден: {file_path}")
            raise FileNotFoundError(f"Файл {file_path} не существует")

        df = pd.read_excel(
            file_path,
            parse_dates=['date'],
            dtype={'amount': float}
        )
        logger.info(f"Успешно прочитан Excel файл: {file_path}")
        return df.to_dict('records')

    except pd.errors.EmptyDataError:
        logger.error(f"Excel файл пустой: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Ошибка чтения Excel файла {file_path}: {str(e)}")
        raise
