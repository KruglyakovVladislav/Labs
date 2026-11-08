#functions.py
def sum_digits(number):
    n = abs(number)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
def average(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)
def normalize_text(text):
    text = text.strip()
    words = text.split()
    return " ".join(words)
def select_numbers(numbers, threshold):
    result = []
    for n in numbers:
        if n != threshold:
            result.append(n)
    return result