"""Тесты модуля выполнения скриптов."""

import os
import tempfile
from src.script_runner import load_script


def test_load_script_basic():
    """Тест загрузки простого скрипта."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".sh", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write("ls -la\ncd /home\n")
        tmp_path = tmp.name

    try:
        commands = load_script(tmp_path)
        assert commands == ["ls -la", "cd /home"]
    finally:
        os.unlink(tmp_path)


def test_load_script_with_comments():
    """Тест загрузки скрипта с комментариями."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".sh", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write("# this is a comment\nls\ncd /home\n")
        tmp_path = tmp.name

    try:
        commands = load_script(tmp_path)
        assert commands == ["ls", "cd /home"]
    finally:
        os.unlink(tmp_path)


def test_load_script_with_empty_lines():
    """Тест загрузки скрипта с пустыми строками."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".sh", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write("ls\n\ncd /home\n\n")
        tmp_path = tmp.name

    try:
        commands = load_script(tmp_path)
        assert commands == ["ls", "cd /home"]
    finally:
        os.unlink(tmp_path)


def test_load_script_not_found():
    """Тест загрузки несуществующего скрипта."""
    try:
        load_script("/nonexistent/path.sh")
        assert False, "Должно было возникнуть исключение"
    except FileNotFoundError:
        pass