t = int(input())
while t>0:
    n, m = map(int,input().split())
    print(max(n, m) + 1)
    t-=1