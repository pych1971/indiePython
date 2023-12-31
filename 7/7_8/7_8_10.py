def flatten(a: list, b=None) -> list:
    if b is None:
        b = []
    for i in a:
        if type(i) is list:
            flatten(i, b)
        else:
            b.append(i)
    return b
