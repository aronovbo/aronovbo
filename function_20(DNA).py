dna = input()
def count_AGTC(dna):
    d =[]
    # a = 0
    # g = 0
    # t = 0
    # c = 0

    a, g, t, c = 0, 0, 0, 0
    for i in dna:
        if i == 'A':
            a += 1
        elif i == 'G':
            g += 1
        elif i == 'T':
            t += 1
        elif i == 'C':
            c += 1
    z = a, g, t, c
    return z
print(count_AGTC(dna))
