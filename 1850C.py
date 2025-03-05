t = int(input())

while t:
    s = ''
    for _ in range(8):
        s += input()
    for i in s:
        if i != '.':
            print(i, end='')
    if t != 1: print()
    t-=1