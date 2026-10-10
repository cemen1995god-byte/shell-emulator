"""Модуль парсинга командной строки."""

from typing import List, Tuple


def _is_separator(char: str, in_single: bool, in_double: bool) -> bool:
    """Проверяет, является ли символ разделителем.

    Args:
        char: Символ для проверки.
        in_single: Флаг нахождения в одинарных кавычках.
        in_double: Флаг нахождения в двойных кавычках.

    Returns:
        True, если символ — разделитель.
    """
    return char == ' ' and not in_single and not in_double


def _handle_quote(
    char: str, in_single: bool, in_double: bool
) -> Tuple[bool, bool, bool]:
    """Обрабатывает кавычки и возвращает новые состояния.

    Args:
        char: Текущий символ.
        in_single: Флаг нахождения в одинарных кавычках.
        in_double: Флаг нахождения в двойных кавычках.

    Returns:
        Кортеж (in_single, in_double, is_quote).
    """
    if char == "'" and not in_double:
        return not in_single, in_double, True
    if char == '"' and not in_single:
        return in_single, not in_double, True
    return in_single, in_double, False


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
        in_single_quote, in_double_quote, is_quote = _handle_quote(
            char, in_single_quote, in_double_quote
        )

        if is_quote:
            continue

        if _is_separator(char, in_single_quote, in_double_quote):
            if current:
                tokens.append(current)
                current = ""
        else:
            current += char

    if current:
        tokens.append(current)

    return tokens