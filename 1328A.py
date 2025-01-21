import math
t = int(input())
while t:
    a, b = map(int,input().split())
    print(math.ceil(a/b)*b-a)
    t-=1