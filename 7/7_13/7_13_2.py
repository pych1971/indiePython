def create_accumulator(s=0, n=0):
    def inner(n):
        nonlocal s
        s += n
        return s

    return inner
