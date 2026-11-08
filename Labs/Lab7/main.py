import functions
number = int(input("Введите целое число: "))
print(f"Сумма цифр модуля: {functions.sum_digits(number)}")

numbers_input = input("Введите числа через пробел: ").strip()
if numbers_input:
    numbers = [float(x) for x in numbers_input.split()]
else:
    numbers = []

result = functions.average(numbers)
if result is None:
    print("Нет данных")
else:
    print(f"Среднее: {result:.2f}")

text = input("Введите произвольный текст: ")
print(f"Нормализованный текст: '{functions.normalize_text(text)}'")

threshold = int(input("Введите порог: "))
filtered = functions.select_numbers(numbers, threshold)
print(f"Исходный список: {numbers}")
print(f"Числа, не равные порогу: {filtered}")