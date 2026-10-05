"""Тесты модуля парсинга."""

from src.parser import parse_arguments


def test_empty_line():
    """Тест пустой строки."""
    assert parse_arguments("") == []


def test_single_command():
    """Тест одной команды без аргументов."""
    assert parse_arguments("ls") == ["ls"]


def test_command_with_args():
    """Тест команды с аргументами."""
    assert parse_arguments("ls -la /home") == ["ls", "-la", "/home"]


def test_double_quotes():
    """Тест аргументов в двойных кавычках."""
    result = parse_arguments('ls "my folder"')
    assert result == ["ls", "my folder"]


def test_single_quotes():
    """Тест аргументов в одинарных кавычках."""
    result = parse_arguments("cd 'my folder'")
    assert result == ["cd", "my folder"]


def test_mixed_quotes():
    """Тест смешанных кавычек."""
    result = parse_arguments('echo "hello" \'world\'')
    assert result == ["echo", "hello", "world"]


def test_nested_quotes():
    """Тест вложенных кавычек."""
    result = parse_arguments('echo "it\'s"')
    assert result == ["echo", "it's"]