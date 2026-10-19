
echo === Запуск тестов ===
python -m pytest tests/ -v

echo.
echo === Проверка цикломатической сложности ===
radon cc src/ -s

echo.
echo === Тест интерактивного режима ===
echo exit | python -m src.main

echo.
echo === Тест со скриптом ===
python -m src.main --vfs-path C:\tmp\vfs --script scripts\test_basic.sh