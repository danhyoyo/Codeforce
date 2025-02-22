from math import ceil
n, m = map(int, input().split())
c=0
for b in range(0, 1001):
    if (m - b**2)**2 + b == n:
        a = m - b**2
        if a == ceil(a) and a>=0:
            c+=1
print(c)