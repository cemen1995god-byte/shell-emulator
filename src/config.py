"""Модуль обработки параметров командной строки."""

import argparse


def create_parser() -> argparse.ArgumentParser:
    """Создаёт парсер аргументов командной строки.

    Returns:
        Настроенный парсер аргументов.
    """
    parser = argparse.ArgumentParser(
        description="Эмулятор оболочки UNIX-подобной ОС."
    )
    parser.add_argument(
        "--vfs-path",
        type=str,
        default=None,
        help="Путь к физическому расположению VFS."
    )
    parser.add_argument(
        "--script",
        type=str,
        default=None,
        help="Путь к стартовому скрипту."
    )
    return parser


def parse_cli_args() -> argparse.Namespace:
    """Разбирает аргументы командной строки.

    Returns:
        Пространство имён с параметрами.
    """
    parser = create_parser()
    return parser.parse_args()


def print_config(args: argparse.Namespace) -> None:
    """Выводит отладочную информацию о конфигурации.

    Args:
        args: Параметры командной строки.
    """
    print("=== Конфигурация эмулятора ===")
    vfs = args.vfs_path or "не задан"
    script = args.script or "не задан"
    print(f"VFS Path: {vfs}")
    print(f"Script: {script}")
    print("================================")