def create_accumulator(n=0):
    s = 0

    def inner(n):
        nonlocal s
        s += n
        return s

    return inner
