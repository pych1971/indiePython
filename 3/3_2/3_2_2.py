a=int(input())
b=int(input())
(minimum, maximum) = (b, a) if a > b else (a, b)
print(minimum, maximum)
