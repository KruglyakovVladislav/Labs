# variant.py
text = input("Введите строку: ")
words = text.split()
filtered_words = []
for word in words:
    stripped = word.strip(".,!?;:")
    normalized = stripped.lower()
    if not normalized:
        continue
    if "р" in normalized:
        filtered_words.append(normalized)
if not filtered_words:
    print("Нет совпадений")
    print("Количество: 0")
else:
    for word in filtered_words:
        print(word)
    print(f"Количество: {len(filtered_words)}")