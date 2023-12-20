x=input()
y=input()
if ((ord((x)[0])+int(x[1]))%2==0 and (ord((y)[0])+int(y[1]))%2==0) or ((ord((x)[0])+int(x[1]))%2==1 and (ord((y)[0])+int(y[1]))%2==1):
    print('YES')
else:
    print('NO')
