a = set()
x = 0
for i in range(77):
    a.add(x := x * 10 + 7)
my_frozen = frozenset(a)
