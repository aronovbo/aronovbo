def get_body_mass_index(x, y):
    i = x / (y * 0.01) ** 2
    if i < 18.5:
        print('Недостаточная масса тела')
    elif 18.5 <= i <= 25:
        print('Норма')
    else:
        print('Избыточная масса тела')

get_body_mass_index(53,169)