import datetime
import os

import pytest

from src.decorators import log


@log()
def successful_function(a: int, b: int) -> int:
    return a + b


@log(filename="test_log.txt")
def failing_function(a: int, b: int) -> int:
    raise ValueError("Example error")


def test_log_to_console(capsys: pytest.CaptureFixture) -> None:
    successful_function(1, 2)
    captured = capsys.readouterr()
    assert "successful_function ok" in captured.out


def test_log_to_file() -> None:
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    try:
        failing_function(3, 4)
    except ValueError:
        pass

    with open("test_log.txt", "r", encoding="utf-8") as f:
        content = f.read()
        assert "failing_function error: ValueError" in content
        assert "Inputs: (3, 4), {}" in content


def test_log_format() -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{timestamp} - test_function ok\n"
    assert log_message.count("-") == 1
