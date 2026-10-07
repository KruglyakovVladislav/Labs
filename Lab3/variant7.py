#variant7.py
value = int(input("Введите процент прочитанной книги от 0 до 100%: "))
if value < 0 or value > 100:
    print("Ошибка диапазона")
else:
    if value <= 9:
        print("Начало")
    elif value <= 89:
        print("Чтение")
    else:
        print("Почти готово")