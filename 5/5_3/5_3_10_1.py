spisok = list(map(int, input().split()))
result = 'True'
for i in range(len(spisok) - 1):
    if spisok[i] <= spisok[i + 1]:
        continue
    else:
        result = 'False'
        break
print(result)
