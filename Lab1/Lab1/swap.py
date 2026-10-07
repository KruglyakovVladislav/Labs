# swap.py
first_room= input("Введите первую аудиторию:")
second_room= input("Введите вторую аудиторию:")
print("До обмена:")
print(f"Первая аудитория: {first_room}")
print(f"Вторая аудитория: {second_room}")
variable=first_room
first_room=second_room
second_room=variable
print("После обмена:")
print(f"Первая аудитория: {first_room}")
print(f"Вторая аудитория: {second_room}")
