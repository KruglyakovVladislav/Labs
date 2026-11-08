# palindrome.py
text = input("Введите текст: ")
cleaned = "".join(ch.lower() for ch in text if ch != " ")
if not cleaned:
    print("Нет текста")
else:
    if cleaned == cleaned[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")
    is_palindrome_loop = True
    n = len(cleaned)
    for i in range(n // 2):
        if cleaned[i] != cleaned[n - 1 - i]:
            is_palindrome_loop = False
            break