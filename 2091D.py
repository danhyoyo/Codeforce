from math import *
t = int(input())
while t:
    n, m, k = map(int, input().split())
    mi = 10**10
    mot_hang = ceil(k/n)
    if m == mot_hang:
        print(m)
    else:
        for i in range(2,mot_hang+1):
            c = floor(mot_hang / i) - 1
            if mot_hang % i != 0:
                c += 1
            if c + mot_hang <= m:
                mi = min(mi, ceil(mot_hang/i))
        print(mi)
    t-=1