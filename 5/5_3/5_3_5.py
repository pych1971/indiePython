a=input()
b=input().split()
for i in range(len(b)):
    if a in b[i].lower():
        print(b[i])
