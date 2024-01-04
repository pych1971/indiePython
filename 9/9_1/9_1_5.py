f = open('numbers.txt')
n = len(f.readlines())
f.seek(0)
s = 0
i = 0
for j in range(n):
    a = f.readline().strip()
    if len(a) == 3:
        i += 1
    elif len(a) == 2:
        s += int(a)
f.close()
print(i, s)
