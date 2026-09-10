import random
import time

print("fsociety encryption tool v2.0")
print("-" * 30)
time.sleep(0.5)

leet_rules = {
    'a': '@', 'A': '4',
    'e': '3', 'E': '3',
    'i': '1', 'I': '1',
    'o': '0', 'O': '0',
    's': '$', 'S': '5',
    't': '7', 'T': '7',
    'b': '8', 'B': '8',
}

tails = ["_root", "_fociety", "_X", "_shadow", "_bypass", "_777"]

word = input("Введите базовое слово на английском: ")

print("\nЗапуск алгоритма шифрования . . .")
time.sleep(0.8)

hacked_word = ""

for char in word:
    if char in leet_rules:
        hacked_word += leet_rules[char]
    else:
        hacked_word += char

secure_password = hacked_word + random.choice(tails)

print("-" * 30)
print(f" СГЕНЕРИРОВАН СЕКРЕТНЫЙ ПАРОЛЬ: {secure_password}")
print("-" * 30)