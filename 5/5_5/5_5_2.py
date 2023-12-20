n = input()
spisok = map(int, input().split())
count = [0] * 201
for i in spisok:
    count[i + 100] += 1
for i in range(201):
    if count[i] > 0:
        for j in range(count[i]):
            print(i - 100, end=' ')
