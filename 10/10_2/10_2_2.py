def gen_fibonacci_numbers(n: int) -> int:
    a = 1
    b = 1
    i = 1
    while i <= n:
        yield a
        a, b = b, a + b
        i += 1
