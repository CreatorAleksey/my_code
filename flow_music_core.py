import time


print("=" * 50)
print("     OPENNET PROJECTS - FLOWMUSIC STREAMING v1.2    ")
print("=" * 50)
time.sleep(0.4)

my_playlist = []

print("[SYSTEM] Запуск аудио приложения...")
print("-" * 50)

while True:
    print(f"\nТекущий плейлист: {my_playlist if my_playlist else '[ПУСТО]'}")
    track = input("Введите название трека для добавления (или 'выход' для запуска): ").strip()

    if track.lower() == 'выход':
        break
    elif track == "":
        continue
    else:
        my_playlist.append(track)
        print(f"[УСПЕШНО] Трек '{track}' добавлен в плейлист.")

print("-" * 50)
print("\n[ЗАПУСК СТРИМИНГА] Воспроизведение трека...")
time.sleep(0.5)

for index, song in enumerate(my_playlist, 1):
    print(f">> [PLAYING] Трек {index}: {song} [=== LINEAR FLOW ===]")
    time.sleep(0.8)

print("\n" + "=" * 50)
print("Система Opennet переходит в режим ожидания.")
print("=" * 50)