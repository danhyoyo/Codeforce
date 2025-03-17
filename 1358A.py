import math
t = int(input())
while t:
    n, m = map(int, input().split())
    print(math.ceil(n*m/2))
    t-=1