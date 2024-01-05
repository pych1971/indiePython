def find_keys(**kwargs):
    result = []
    for i in kwargs:
        if isinstance(kwargs[i], (list, tuple)):
            result.append(i)
    return sorted(result, key=str.lower)
