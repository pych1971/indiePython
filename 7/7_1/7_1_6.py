def get_body_mass_index(m, l):
    i = m / (l / 100) ** 2
    if i < 18.5:
        print('Недостаточная масса тела')
    elif 18.5 <= i <= 25:
        print('Норма')
    elif i > 25:
        print('Избыточная масса тела')
