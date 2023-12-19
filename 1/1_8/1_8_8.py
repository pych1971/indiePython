n=int(input())
chasy=n//60
chasy=chasy-chasy//24*24
minuty=n%60
print(chasy, minuty)
