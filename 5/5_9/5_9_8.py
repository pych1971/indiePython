n = int(input())
from string import ascii_uppercase

b = ascii_uppercase
a = [b[i] * (i + 1) for i in range(len(ascii_uppercase)) if i < n]
print(a)
