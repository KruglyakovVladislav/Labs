#README.py
"""
намеренно вносим ошибку, заменив в functions.py условие в select_numbers

def select_numbers(numbers, threshold):
    result = []
    for n in numbers:
        if n == threshold:        # было: if n != threshold  ← ошибка
            result.append(n)
    return result

Traceback (most recent call last):
  File "C:\Users\Aorus\PycharmProjects\Labs\Lab7\test_functions.py", line 13, in <module>
    assert select_numbers([-5, 0, 2, 5], 2) == [-5, 0, 5]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
"""
"""
В functions.py убираем смену регистра через .lower
Traceback (most recent call last):
  File "C:\Users\Aorus\PycharmProjects\Labs\Lab7\test_functions.py", line 9, in <module>
    assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
"""