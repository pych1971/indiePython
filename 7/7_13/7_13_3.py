def multiply(value):
    def inner(a):
        return value * a

    return inner
