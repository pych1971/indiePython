a=int(input())
maximum=1
minimum=9
while a>0:
    if a%10>maximum:
        maximum=a%10
    if a%10<minimum:
        minimum=a%10
    a=a//10
print(minimum)
print(maximum)
