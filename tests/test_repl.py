"""Тесты модуля REPL."""

from src.repl import process_command
from src.commands import COMMANDS


def test_unknown_command():
    """Тест неизвестной команды."""
    result = process_command("unknown", COMMANDS)
    assert result == "Неизвестная команда: unknown"


def test_ls_command():
    """Тест команды ls."""
    result = process_command("ls -la", COMMANDS)
    assert result == "ls: -la"


def test_cd_command():
    """Тест команды cd."""
    result = process_command("cd /home", COMMANDS)
    assert result == "cd: /home"


def test_empty_input():
    """Тест пустого ввода."""
    result = process_command("", COMMANDS)
    assert result == ""


def test_exit_command():
    """Тест команды exit."""
    result = process_command("exit", COMMANDS)
    assert result == ""