t = int(input())
while t:
    n = int(input())
    a = list(map(int,input().split()))
    m, s = min(a), 0
    for i in a:
        s += i-m
    print(s)
    t-=1