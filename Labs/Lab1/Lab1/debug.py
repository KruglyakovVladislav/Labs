# debug.py
#Фрагмент А: требуется сумма чисел 5, а не соединение строк 23.
print("\n" + "=" * 40)
print("Фрагмент А")
first = "2"
second = "3"
print("Ошибочный результат:")
print(first + second)
print(f"тип до преобразования:{type(first+second)}")
# Ожидаемый результат: 5
# Причина ошибки: first и second — строки ("2" и "3"), оператор + для строк делает конкатенацию → "23"
first_int = int(2)
second_int = int(3)
print("Верный результат:")
print(first_int + second_int)
print(f"тип после преобразования:{type(first_int+second_int)}")
print("\n" + "=" * 40)
#Фрагмент Б: требуется возраст через год. Ввод для проверки — 17. Ниже приведён намеренно ошибочный код.
#Причина ошибки: input() возвращает строку, а попытка прибавить к строке число вызывает TypeErrorprint("Фрагмент Б")
print("Фрагмент Б")
age_str = input("Возраст: ")
age = int(age_str)
print(f"тип до преобразования:{type(age_str)}")
print("Ошибочный тип")
age = int(input("Возраст: "))
print(f"тип после преобразования:{type(age)}")
print(age + 1)
print("\n" + "=" * 40)
#Фрагмент В: требуется среднее трёх чисел 4, 7, 10; правильный результат — 7.0.
"""first = 4
   second = 7
   third = 10
   average = first + second + third / 3
   print(average)"""
# Причина ошибки: последовательность операций — сначала выполняется third / 3, потом складываются first + second + third / 3
print("Фрагмент В")
first = 4
second = 7
third = 10
wrong_average = first + second + third / 3
print(f"Неправильный расчёт (без скобок): {wrong_average}")
average = (first + second + third) / 3
print(f"Правильный расчёт (со скобками): {average}")