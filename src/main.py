"""Точка входа в эмулятор оболочки."""

from src.config import parse_cli_args, print_config
from src.repl import run_repl
from src.script_runner import run_script
from src.commands import COMMANDS


def main() -> None:
    """Запускает эмулятор оболочки."""
    args = parse_cli_args()
    print_config(args)

    if args.script:
        run_script(args.script, COMMANDS)
    else:
        run_repl(COMMANDS)


if __name__ == "__main__":
    main()