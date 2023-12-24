a = input()
b = set()
for i in a:
    if 'a' <= i <= 'z':
        b.add(i)
print(len(b))
