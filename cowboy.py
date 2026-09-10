import random
import time 

adjectives = ["Дырявый", "Косолапый"]
nouns = ["баскетболист", "кибер-нуб", "челик"]
actions = ["мажет трехочковые", "улетел в бан", "потярял мяч"]

print("Запуск рандомайзера слов")
print("-" * 30)
time.sleep(0.5)


for i in range(3):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    act = random.choice(actions)

    print(f"Робот выдал: {adj} {noun} {act}")
    time.sleep(0.5)

print("\n Все напарник генератор закрыт!")