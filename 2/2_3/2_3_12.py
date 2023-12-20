a=input()
a=a.lower()
a=a.replace('a', '').replace('o', '').replace('y', '').replace('e', '').replace('u', '').replace('i', '').replace('', '.')
print(a[:-1])
