import os
import sys
import webbrowser

# Внедряем твою фирменную ковбойскую оптимизацию строк!
print("=" * 50)
print("🤖 JARVIS TEXT OS TERMINAL v1.0 STARTED 🤖")
print("=" * 50)
print("Приветствую, Сеньор Алексей! Я готов выполнять ваши приказы.")
print("Доступные команды: yandex, github, exit")
print("-" * 50)

while True:
    # Запрашиваем команду у создателя
    command = input("Введите приказ ▷ ")
    command = command.lower().strip()

    if command == "yandex":
        print("🌐 Открываю браузер Яндекс...")
        webbrowser.open("https://yandex.ru")

    elif command == "github":
        print("🐍 Открываю ваш личный репозиторий...")
        webbrowser.open("https://github.com")

    elif command == "exit":
        print("🔋 Выгружаю логи Джарвиса... Системы отключены. До связи, Алексей!")
        print("=" * 50)
        sys.exit()

    else:
        print("❌ Ошибка: Неизвестная команда. Попробуйте еще раз.")
    print("-" * 50)
