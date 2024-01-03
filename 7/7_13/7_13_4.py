def create_dict():
    slovar = dict()
    key = 1

    def inner(x):
        nonlocal key
        slovar[key] = x
        key += 1
        return slovar

    return inner
