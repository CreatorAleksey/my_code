import random
import time

print("=" * 45)
print("FSOCIETY DARKNET BREACH DETEKTOR v3.0")
print("=" * 45)

target_user = input("Введите никнейм для проверки в базе утечек: ")

print(f"\n [СКАНИРОВАНИЕ] Поиск совпадений для аккаунта: {target_user}. . .")
print("-" * 45)
time.sleep(1)

servers = ["NSA_SERVER_MAIN", "EVIL_CORP_BACKEND", "CRYPTO_EXCHANGE_DATA", "PENTAGON_LOGS_RESERVE"]
status_codes = ["[SUCCESS]", "[BYPASS]", "[CONNECTED]", "[OVERRIDE]"]

for i in range(5):
    current_server = random.choice(servers)
    code = random.choice(status_codes)
    ip_address = f"{random.randint(100, 999)}.{random.randint(10, 99)}.{random.randint(0, 255)}.{random.randint(1, 254)}"

    print(f"Попытка доступа к {current_server}. . . IP: {ip_address} -> {code}")
    time.sleep(0.6)

print("-" * 45)
print("Анализ уязвимостей паролей...")
time.sleep(1)

leak_found = random.choice([True, False])

if leak_found:
    fake_pass = f"p@$$w0rd_{random.randint(1000, 9999)}"
    print(f"Внимание! Найдена утечка в базе даркнета!")
    print(f"Возможно старый пароль от {target_user}: [ {fake_pass} ]")
    print("СТАТУС БЕЗОПАСНОСТИ: КРИТИЧЕСКИЙ (Уязвимый)")
else:
    print("СТАТУС БЕЗОПАСНОСТИ: СТАБИЛЬНЫЙ (Утечек не обнаружено)")
    print("Твой Firewall надежно защищает аккаунт!")

print("=" * 45)