#normalize.py
text = input("Введите строку: ")
stripped = text.strip()
normalized = " ".join(stripped.split())
word_count = len(normalized.split())
print(f"Исходная длина: {len(text)}")
print(f"Новая длина: {len(normalized)}")
print(f"Нормализованный текст: {normalized}")
print(f"Количество слов: {word_count}")