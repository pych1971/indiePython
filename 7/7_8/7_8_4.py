def double_fact(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return double_fact(n - 2) * n
