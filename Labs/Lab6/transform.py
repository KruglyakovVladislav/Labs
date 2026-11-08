#transform.py
quantity = input().strip()
if not quantity:
    original = []
else:
    original = [int(x) for x in quantity.split()]
transformed = [abs(x) if x < 0 else x for x in original]
print(original)
print(transformed)