def count_strings(*args):
    n = 0
    for i in args:
        if isinstance(i, str):
            n += 1
    return n
