"""Точка входа в эмулятор оболочки."""

from src.repl import run_repl
from src.commands import COMMANDS


def main() -> None:
    """Запускает эмулятор оболочки."""
    run_repl(COMMANDS)


if __name__ == "__main__":
    main()