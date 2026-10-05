"""Тесты модуля команд."""

from src.commands import execute_ls, execute_cd, execute_exit


def test_ls_no_args():
    """Тест ls без аргументов."""
    assert execute_ls([]) == "ls: "


def test_ls_with_args():
    """Тест ls с аргументами."""
    assert execute_ls(["-la"]) == "ls: -la"


def test_cd_no_args():
    """Тест cd без аргументов."""
    assert execute_cd([]) == "cd: "


def test_cd_with_args():
    """Тест cd с аргументами."""
    assert execute_cd(["/home"]) == "cd: /home"


def test_exit():
    """Тест команды exit."""
    assert execute_exit([]) == ""