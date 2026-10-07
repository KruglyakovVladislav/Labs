# variant7.py
# Расчёт заказа из двух позиций. Только последовательные команды.

# --- Ввод общих данных ---
order_name = input("Введите название заказа: ")
customer_name = input("Введите имя заказчика: ")

# --- Первая позиция ---
item_1 = input("Введите название первой позиции: ")
qty_1 = int(input("Введите количество (целое неотрицательное): "))
price_1 = float(input("Введите цену единицы в рублях (неотрицательное дробное): "))

# --- Вторая позиция ---
item_2 = input("Введите название второй позиции: ")
qty_2 = int(input("Введите количество (целое неотрицательное): "))
price_2 = float(input("Введите цену единицы в рублях (неотрицательное дробное): "))

# --- Доставка и внесённая сумма ---
delivery = float(input("Введите стоимость доставки в рублях (неотрицательная): "))
deposited = float(input("Введите внесённую сумму в рублях: "))

# --- Скидка ---
discount_percent = float(input("Введите скидку в процентах (от 0 до 100): "))

# --- Расчёт стоимости позиций ---
cost_1 = qty_1 * price_1
cost_2 = qty_2 * price_2

# --- Стоимость товаров без доставки ---
goods_total = cost_1 + cost_2

# --- Скидка ---
discount_amount = goods_total * discount_percent / 100
goods_total_discounted = goods_total - discount_amount

# --- Общая сумма со скидкой и доставкой ---
total_with_delivery = goods_total_discounted + delivery

# --- Общее количество единиц ---
total_qty = qty_1 + qty_2

# --- Сдача ---
change = deposited - total_with_delivery

# --- Вывод результатов ---
print("\n" + "=" * 55)
print(f"ЗАКАЗ: {order_name}")
print(f"Заказчик: {customer_name}")
print("=" * 55)
print(f"{item_1} | {qty_1} | {price_1:.2f} | {cost_1:.2f}")
print(f"{item_2} | {qty_2} | {price_2:.2f} | {cost_2:.2f}")
print("-" * 55)
print(f"Стоимость товаров без доставки: {goods_total:.2f} руб.")
print(f"Скидка: {discount_percent}% — {discount_amount:.2f} руб.")
print(f"Стоимость товаров со скидкой: {goods_total_discounted:.2f} руб.")
print(f"Доставка: {delivery:.2f} руб.")
print(f"Итого со скидкой и доставкой: {total_with_delivery:.2f} руб.")
print(f"Общее количество единиц: {total_qty}")
print(f"Внесено: {deposited:.2f} руб.")
print(f"Сдача: {change:.2f} руб.")
print("=" * 55)