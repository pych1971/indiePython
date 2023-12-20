a=int(input())
while a<=1000000000 and str(a)[0]!='1':
    a*=int(str(a)[0])
print(a)
