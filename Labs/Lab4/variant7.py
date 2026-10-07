#variant7.py
n = int(input("Введите n (n >= 0): "))
total_sum = 0
count = 0
for _ in range(n):
    num = int(input("Введите целое число: "))
    if num % 3 != 0:
        total_sum += num
        count += 1
print(f"Количество чисел, не кратных 3: {count}")
print(f"Сумма этих чисел: {total_sum}")