s = 'abcabc'
def first_unique_char(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            print(i)
            break

    else:
        print('-1')
first_unique_char(s)
