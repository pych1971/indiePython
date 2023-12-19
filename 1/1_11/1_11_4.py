import math
L, W, H = map(int, input().split())
S=(L+W)*H*2
print(math.ceil(S/16))
