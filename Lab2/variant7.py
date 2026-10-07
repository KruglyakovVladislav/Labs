#variant7.py
all = int(input("Введите общее количество саженцев: "))
capacity = int(input("Введите количество саженцев в ряду: "))
total_number = all // capacity
surplus = all % capacity
has_elements = int(all > 0)
total_units = ((all + capacity - 1) // capacity) * has_elements
print(f"Полных {total_number}, остаток {surplus}, всего {total_units}")