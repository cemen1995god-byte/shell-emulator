"""Модуль интерактивного цикла чтения-выполнения."""

from typing import Dict, Callable, List

from src.parser import parse_arguments
from src.commands import COMMANDS

PROMPT = "vfs> "
EXIT_CODE = "exit"


def process_command(
    line: str,
    commands: Dict[str, Callable[[List[str]], str]],
) -> str:
    """Обрабатывает одну строку ввода.

    Args:
        line: Строка пользовательского ввода.
        commands: Словарь доступных команд.

    Returns:
        Результат выполнения команды.
    """
    tokens = parse_arguments(line)

    if not tokens:
        return ""

    command_name = tokens[0]
    args = tokens[1:]

    if command_name not in commands:
        return f"Неизвестная команда: {command_name}"

    return commands[command_name](args)


def run_repl(
    commands: Dict[str, Callable[[List[str]], str]],
    prompt: str = PROMPT,
) -> None:
    """Запускает интерактивный цикл.

    Args:
        commands: Словарь доступных команд.
        prompt: Строка приглашения ввода.
    """
    while True:
        try:
            line = input(prompt)
        except EOFError:
            print()
            break

        result = process_command(line, commands)

        if result:
            print(result)

        if line.strip() == EXIT_CODE:
            break