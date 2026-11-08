#statistics.py
quantity = input().strip()
if not quantity:
    print("Нет данных")
else:
    numbers = [int(x) for x in quantity.split()]
    if len(numbers) == 0:
        print("Нет данных")
    else:
        count = len(numbers)
        total = sum(numbers)
        minimum = numbers[0]
        maximum = numbers[0]
        for n in numbers[1:]:
            if n < minimum:
                minimum = n
            if n > maximum:
                maximum = n
        average = total / count
        print(count)
        print(total)
        print(minimum)
        print(maximum)
        print(f"{average:.2f}")