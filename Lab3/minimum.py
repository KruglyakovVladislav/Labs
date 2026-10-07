#minimum.py
a = int(input("Введите 1-ое число: "))
b = int(input("Введите 2-ое число: "))
c = int(input("Введите 3-е число: "))
if a <= b and a <= c:
    minimum = a
elif b <= c:
    minimum = b
else:
    minimum = c
print(f"Минимальное число: {minimum}")