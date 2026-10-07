#statistics.py
n = int(input("Введите целое n (n >= 1): "))
total_sum = 0
positive_count = 0
first_number = int(input("Введите число: "))
total_sum += first_number
maximum = first_number
if first_number > 0:
    positive_count += 1
    for _ in range(n - 1):
        num = int(input("Введите число: "))
        total_sum += num
        if num > 0:
            positive_count += 1
        if num > maximum:
            maximum = num
    print(f"Сумма: {total_sum}")
    print(f"Число положительных значений: {positive_count}")
    print(f"Максимум: {maximum}")