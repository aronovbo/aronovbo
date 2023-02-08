

def format_name_list(names: list[dict]) -> str:
    w = []
    for i in names:
        w.append(i["name"])
    if len(w) == 0:
        return ''
    elif len(w) == 1:
        return w[0]
    elif len(w) == 2:
        return f'{w[0]} и {w[1]}'
    else:
        a = ''
        for i in range(1, len(w) - 1):
            a += (w[i - 1] + ', ')
        a += f'{w[-2]} и {w[-1]}'
        return a



