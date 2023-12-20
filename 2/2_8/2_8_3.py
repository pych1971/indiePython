a=int(input())
p=a-1
n=a+1
p='Для числа {a} предыдущим будет число {p}.'.format(a=a, p=p)
n='Для числа {a} следующим будет число {n}.'.format(a=a, n=n)
print(p,n,sep='\n')
