#positions.py
s = input().strip()

if not s:
    print("Нет данных")
else:
    numbers = [int(x) for x in s.split()]
    if len(numbers) == 0:
        print("Нет данных")
    else:
        maximum = numbers[0]
        for n in numbers[1:]:
            if n > maximum:
                maximum = n
        indices = []
        for idx, value in enumerate(numbers):
            if value == maximum:
                indices.append(idx)
        print(indices)