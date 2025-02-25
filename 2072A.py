import math
t = int(input())
while t:
    n, k ,p = map(int, input().split())
    a = math.ceil(abs(k)/p)
    if a <= n:
        print(a)
    else: print(-1)
    t-=1