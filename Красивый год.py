n = int(input())

while 1000 <= n <= 9000:
    n += 1
    s = [i for i in str(n)]
    ss = set(s)
    if len(ss) == 4:
        print(*s,sep='')
        break


