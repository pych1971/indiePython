a = input().split(',')
b = set()
s = 0
for i in range(len(a)):
    b.add(a[i].lower())
    if len(b) > s:
        print('НЕТ')
        s = len(b)
    else:
        print('ДА')
