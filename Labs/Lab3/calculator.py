#calculator.py
number1 = float(input("Введите первое число: "))
operation = input("Введите операцию (+, -, *, /): ").strip()
number2 = float(input("Введите второе число: "))
if operation == "+":
    result = number1 + number2
    print(f"{result:.2f}")
elif operation == "-":
    result = number1 - number2
    print(f"{result:.2f}")
elif operation == "*":
    result = number1 * number2
    print(f"{result:.2f}")
elif operation == "/":
    if number2 == 0:
        print("Деление на ноль запрещено")
    else:
        result = number1 / number2
        print(f"{result:.2f}")
else:
    print("Неизвестная операция")