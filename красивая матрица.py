a = []
for i in range(5):
    a.append(list(map(int, input().split())))
# a = [list(map(int, input().split())) for i in range(5)]
for i in range(len(a)):
    for j in range(len(a)):
        if a[i][j] == 1:
            print(abs(2-i) + abs(2-j))











