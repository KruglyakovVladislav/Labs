#purchase
price = int(input("Введите цену одной тетради (руб.): "))
count = int(input("Введите количество тетрадей: "))
paid = int(input("Введите переданную сумму (руб.): "))
cost = price * count
change = paid - cost
print(f"стоимость {cost}, сдача {change}")