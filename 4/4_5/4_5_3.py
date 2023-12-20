a,b=map(int, input().split())
a1=a
b1=b
while b>0:
    a,b=b,a%b
print(int(a1*b1/a))
