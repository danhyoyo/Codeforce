t = int(input())
while t:
    n,s,m = map(int, input().split())
    l = []
    for i in range(n):
        a,b = map(int, input().split())
        l.append([a,b])
    ma = l[0][0]
    l.sort(key = lambda x: x[0])
    for i in range(1,n):
        tmp = l[i][0] - l[i-1][1]
        ma = max(ma, tmp)
    ma = max(ma, m - l[n-1][1])
    if ma >= s:
        print("YES")
    else:
        print("NO")
    t-=1