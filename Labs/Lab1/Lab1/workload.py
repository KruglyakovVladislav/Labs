# workload.py

def get_non_negative_int(prompt):
    """Запрашивает неотрицательное целое число."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Число должно быть неотрицательным. Попробуйте снова.")
        except ValueError:
            print("Это не целое число. Попробуйте снова.")

def get_positive_int(prompt):
    """Запрашивает положительное целое число."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Число должно быть положительным. Попробуйте снова.")
        except ValueError:
            print("Это не целое число. Попробуйте снова.")

# --- Ввод данных для первого предмета ---
subject_1 = input("Введите название первого предмета: ")
classes_1 = get_non_negative_int(f"Введите количество занятий по {subject_1} за неделю: ")
duration_1 = get_positive_int(f"Введите продолжительность одного занятия по {subject_1} в минутах: ")

# --- Ввод данных для второго предмета ---
subject_2 = input("Введите название второго предмета: ")
classes_2 = get_non_negative_int(f"Введите количество занятий по {subject_2} за неделю: ")
duration_2 = get_positive_int(f"Введите продолжительность одного занятия по {subject_2} в минутах: ")

# --- Расчёт недельной нагрузки в минутах ---
load_minutes_1 = classes_1 * duration_1
load_minutes_2 = classes_2 * duration_2
total_load_minutes = load_minutes_1 + load_minutes_2

# --- Перевод в часы ---
total_load_hours = total_load_minutes / 60

# --- Ввод доступного времени ---
while True:
    try:
        available_hours = float(input("Введите доступное время на неделю в часах: "))
        if available_hours >= total_load_hours:
            break
        else:
            print(f"Доступное время должно быть не меньше суммарной нагрузки ({total_load_hours:.2f} ч). Попробуйте снова.")
    except ValueError:
        print("Это не число. Попробуйте снова.")

# --- Расчёты ---
free_time_hours = available_hours - total_load_hours
load_4_weeks_minutes = total_load_minutes * 4
load_4_weeks_hours = load_4_weeks_minutes / 60

# --- Вывод результатов ---
print("\n" + "=" * 50)
print("ОТЧЁТ ПО УЧЕБНОЙ НАГРУЗКЕ")
print("=" * 50)

print(f"\nПредмет: {subject_1}")
print(f"  Время в неделю: {load_minutes_1} мин")

print(f"\nПредмет: {subject_2}")
print(f"  Время в неделю: {load_minutes_2} мин")

print("\n--- Суммарная нагрузка ---")
print(f"Общая нагрузка в неделю: {total_load_minutes} мин ({total_load_hours:.2f} ч)")
print(f"Нагрузка за 4 недели: {load_4_weeks_minutes} мин ({load_4_weeks_hours:.2f} ч)")

print("\n--- Баланс времени ---")
print(f"Доступное время: {available_hours:.2f} ч")
print(f"Остаток свободного времени: {free_time_hours:.2f} ч")
print("=" * 50)