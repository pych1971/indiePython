n=int(input())
hours=n//3600
minutes=(n-hours*3600)//60
seconds=n-hours*3600-minutes*60
print(hours,end=":")
print(minutes//10, minutes%10, sep="", end=":")
print(seconds//10, seconds%10, sep="")