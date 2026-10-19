"""Модуль выполнения стартовых скриптов."""

from typing import List, Dict, Callable

from src.parser import parse_arguments


def load_script(path: str) -> List[str]:
    """Загружает скрипт из файла.

    Игнорирует пустые строки и комментарии.

    Args:
        path: Путь к файлу скрипта.

    Returns:
        Список команд из скрипта.

    Raises:
        FileNotFoundError: Если файл не найден.
    """
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    commands: List[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            commands.append(stripped)

    return commands


def run_script(
    path: str,
    commands: Dict[str, Callable[[List[str]], str]],
) -> None:
    """Выполняет стартовый скрипт.

    Имитирует диалог с пользователем: выводит ввод и результат.

    Args:
        path: Путь к файлу скрипта.
        commands: Словарь доступных команд.
    """
    try:
        script_commands = load_script(path)
    except FileNotFoundError:
        print(f"Ошибка: скрипт не найден: {path}")
        return

    for command_line in script_commands:
        print(f"vfs> {command_line}")

        tokens = parse_arguments(command_line)
        if not tokens:
            continue

        command_name = tokens[0]
        args = tokens[1:]

        if command_name not in commands:
            print(f"Неизвестная команда: {command_name}")
        else:
            result = commands[command_name](args)
            if result:
                print(result)