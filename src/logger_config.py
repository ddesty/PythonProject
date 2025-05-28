import logging
from pathlib import Path


def setup_logger(
        name: str,
        log_file: str,
        level: int = logging.DEBUG,
        fmt: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt: str = '%Y-%m-%d %H:%M:%S'
) -> logging.Logger:
    """
    Настройка логгера для модуля.

    Args:
        name: Имя логгера (обычно __name__)
        log_file: Имя файла для логов (например 'utils.log')
        level: Уровень логирования (по умолчанию DEBUG)
        fmt: Формат сообщения
        datefmt: Формат даты

    Returns:
        Настроенный объект логгера
    """
    # Создаём папку logs если её нет
    logs_dir = Path(__file__).parent.parent / "logs"
    logs_dir.mkdir(exist_ok=True)

    # Создаём логгер
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Очищаем предыдущие хендлеры
    logger.handlers = []

    # Настраиваем файловый обработчик
    file_handler = logging.FileHandler(
        filename=logs_dir / log_file,
        mode='w',  # Перезапись при каждом запуске
        encoding='utf-8'
    )
    file_handler.setLevel(level)

    # Настраиваем форматтер
    formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
    file_handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)

    return logger
