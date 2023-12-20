a=int(input())
i=0
while 2**i<=a:
    if 2**i==a:
        print(i)
    i+=1
if 2**(i-1)!=a:
    print('НЕТ')