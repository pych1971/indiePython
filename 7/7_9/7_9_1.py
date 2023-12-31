def flatten_dict(d: dict, prefix: str = '', result: dict = None) -> dict:
    if result == None:
        result = {}
    for key, value in d.items():
        if isinstance(value, int):
            result[prefix + key] = value
        if isinstance(value, dict):
            result.update(flatten_dict(value, prefix + key + '_'))
    return result
