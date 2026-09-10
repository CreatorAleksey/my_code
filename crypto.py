import time 

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord("a") if char.islower() else ord("A")
            result += chr((ord(char) - start + shift) % 26 + start) 
    return result 

print("fsociety crypto system activated")
print("-" * 20)
time.sleep(1)

message = input("Введите текст на английском: ")
secret_key = 3

encrypted_message = encrypt(message, secret_key)
print(f"Зашифрованный код: {encrypted_message}")

time.sleep(1)
decrypted_message = encrypt(encrypted_message, -secret_key)
print(f"Расшифрованный текст: {decrypted_message}")