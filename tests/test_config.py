"""Тесты модуля конфигурации."""

from src.config import create_parser


def test_parser_default_values():
    """Тест значений по умолчанию."""
    parser = create_parser()
    args = parser.parse_args([])
    assert args.vfs_path is None
    assert args.script is None


def test_parser_vfs_path():
    """Тест параметра vfs-path."""
    parser = create_parser()
    args = parser.parse_args(["--vfs-path", "/tmp/vfs"])
    assert args.vfs_path == "/tmp/vfs"


def test_parser_script():
    """Тест параметра script."""
    parser = create_parser()
    args = parser.parse_args(["--script", "test.sh"])
    assert args.script == "test.sh"


def test_parser_both_args():
    """Тест обоих параметров вместе."""
    parser = create_parser()
    args = parser.parse_args([
        "--vfs-path", "/home/vfs",
        "--script", "run.sh"
    ])
    assert args.vfs_path == "/home/vfs"
    assert args.script == "run.sh"