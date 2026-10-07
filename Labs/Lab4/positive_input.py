#positive_input.py
count_rejected = 0
while True:
    num = int(input("Введите целое число: "))
    if num > 0:
        break
    count_rejected += 1
square = num * num
print(f"Положительное число: {num}")
print(f"Его квадрат: {square}")
print(f"Количество отклонённых попыток: {count_rejected}")