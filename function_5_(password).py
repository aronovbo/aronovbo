def check_password(psw):
    d = 0
    a = 0
    s = "!@#$%*"
    ss = 0
    for i in list(psw):
        if i.isdigit():
            d += 1
        elif i.isupper():
            a += 1
        elif i in s:
            ss += 1

    print(d,a,ss)
    if a >= 1 and d >= 3 and ss >= 1 and len(psw) >=10:
        print('Perfect password')
    else:
        print('Easy peasy')

check_password('Qwerty1357!')
