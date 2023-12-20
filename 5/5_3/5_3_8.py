a=input().lower()
x=0
for i in range(len(a)):
    if a.count(a[i])>x:
        x=a.count(a[i])
print(x)
