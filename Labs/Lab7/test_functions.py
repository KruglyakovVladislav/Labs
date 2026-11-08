#test_functions.py
from functions import average, normalize_text, sum_digits, select_numbers

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""
print("Базовые проверки пройдены")

assert select_numbers([-5, 0, 2, 5], 2) == [-5, 0, 5]
assert select_numbers([], 2) == []
assert select_numbers([], 0) == []
assert select_numbers([1, 2, 3], 2) == [1, 3]
assert select_numbers([0, -1, 1], 0) == [-1, 1]
assert select_numbers([2, 7, 2, -1, 7], 2) == [7, -1, 7]
assert select_numbers([4, 4, 4], 4) == []
original = [-5, 0, 2, 5]
snapshot = original[:]
result = select_numbers(original, 2)
assert original == snapshot, "Исходный список изменился!"
assert result == [-5, 0, 5]
assert abs(average([1, 2, 4]) - 7 / 3) < 1e-9
assert abs(average([-5, 0, 2, 5]) - 0.5) < 1e-9
print("Проверки варианта пройдены")