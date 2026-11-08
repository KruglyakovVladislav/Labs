#variant7.py
s = input().strip()
if not s:
    numbers = []
else:
    numbers = [int(x) for x in s.split()]
suitable = [n for n in numbers if n % 3 != 0]
print(suitable)
print(len(suitable))
print(sum(suitable))
print(sorted(suitable))