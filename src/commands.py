"""Модуль команд-заглушек."""

from typing import List


def execute_ls(args: List[str]) -> str:
    """Заглушка команды ls.

    Args:
        args: Аргументы команды.

    Returns:
        Строку с именем команды и аргументами.
    """
    return f"ls: {', '.join(args)}"


def execute_cd(args: List[str]) -> str:
    """Заглушка команды cd.

    Args:
        args: Аргументы команды.

    Returns:
        Строку с именем команды и аргументами.
    """
    return f"cd: {', '.join(args)}"


def execute_exit(args: List[str]) -> str:
    """Команда выхода из эмулятора.

    Args:
        args: Аргументы команды (не используются).

    Returns:
        Пустую строку.
    """
    return ""


COMMANDS = {
    "ls": execute_ls,
    "cd": execute_cd,
    "exit": execute_exit,
}