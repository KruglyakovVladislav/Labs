# profile.py

def get_int(prompt, min_val, max_val):
    """Запрашивает целое число  от 1 до 120."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Пожалуйста, введите число от {min_val} до {max_val}.")
        except ValueError:
            print("Это не целое число. Попробуйте снова.")

def get_float_non_negative(prompt):
    """Запрашивает неотрицательное дробное число."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Число должно быть неотрицательным. Попробуйте снова.")
        except ValueError:
            print("Это не число. Попробуйте снова.")

# Запрос данных (7 значений)
last_name = input("Введите фамилию: ")
first_name = input("Введите имя: ")
group = input("Введите номер группы: ")
city = input("Введите город: ")
age = get_int("Введите возраст в полных годах (от 1 до 120): ", 1, 120)
favorite_subject = input("Введите любимый предмет: ")
hours_per_week = get_float_non_negative("Введите количество часов подготовки в неделю: ")

# Расчёты
age_in_4_years = age + 4
hours_in_4_weeks = hours_per_week * 4
avg_hours_per_day = hours_per_week / 7

# Вывод карточки
print("\n" + "=" * 40)
print("КАРТА СТУДЕНТА")
print("=" * 40)
print(f"Полное имя: {first_name} {last_name}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Текущий возраст: {age}")
print(f"Возраст через 4 года: {age_in_4_years}")
print(f"Любимый предмет: {favorite_subject}")
print(f"Часы подготовки в неделю: {hours_per_week:.2f}")
print(f"Время подготовки за 4 недели: {hours_in_4_weeks:.2f} ч")
print(f"Среднее время подготовки в день: {avg_hours_per_day:.2f} ч")
print("=" * 40)
