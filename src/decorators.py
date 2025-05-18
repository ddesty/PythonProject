import datetime
import functools
from typing import Any
from typing import Callable
from typing import Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования вызовов функций."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = datetime.datetime.now()
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                write_log(log_message, filename)
                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                write_log(log_message, filename)
                raise

        def write_log(message: str, file: Optional[str]) -> None:
            """Записывает лог в файл или выводит в консоль."""
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"{timestamp} - {message}\n"
            if file:
                with open(file, "a", encoding="utf-8") as f:
                    f.write(log_entry)
            else:
                print(log_entry.strip())

        return wrapper

    return decorator
