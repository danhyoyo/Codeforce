import math
t = int(input())
while t:
    n = int(input())
    print(2**math.floor(math.log2(n))-1)
    t-=1