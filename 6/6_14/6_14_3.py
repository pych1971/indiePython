a = input()
s = 0
x = 0
for index, value in enumerate(a):
    if index % 2 != 0:
        s += int(value)
    else:
        x = int(value) * 2
        while x > 9:
            x -= 9
        s += x
if s % 10 == 0:
    print('True')
else:
    print('False')
