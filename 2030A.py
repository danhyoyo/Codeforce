t = int(input())
while t:
    n = int(input())
    l = list(map(int,input().split()))
    s = 0 + (n-1) * (max(l)-min(l))
    print(s)
    t-=1