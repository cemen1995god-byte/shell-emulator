"""Модуль парсинга командной строки."""

from typing import List


def parse_arguments(line: str) -> List[str]:
    """Разбирает строку ввода на команду и аргументы.

    Поддерживает одинарные и двойные кавычки.

    Args:
        line: Строка пользовательского ввода.

    Returns:
        Список токенов [команда, аргумент1, ...].
    """
    tokens: List[str] = []
    current: str = ""
    in_single_quote: bool = False
    in_double_quote: bool = False

    for char in line:
        if char == "'" and not in_double_quote:
            in_single_quote = not in_single_quote
        elif char == '"' and not in_single_quote:
            in_double_quote = not in_double_quote
        elif char == ' ' and not in_single_quote and not in_double_quote:
            if current:
                tokens.append(current)
                current = ""
        else:
            current += char

    if current:
        tokens.append(current)

    return tokens