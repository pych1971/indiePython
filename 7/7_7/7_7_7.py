def create_actor(**kwargs):
    dic = {'name': 'Райан',
           'surname': 'Рейнольдс',
           'age': 46, }
    dic.update(kwargs)
    return dic
