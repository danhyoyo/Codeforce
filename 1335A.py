import math
t = int(input())
while t:
    n = int(input())
    if n>2:
        if n%2==0:
            print(n//2-1)
        else:
            print(n//2)
    else: print(0)
    t-=1