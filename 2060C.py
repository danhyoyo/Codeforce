t = int(input())
while t:
    n, k = map(int,(input().split()))
    l = list(map(int,(input().split())))
    s, i, n = 0, 0, n-1
    l.sort()
    while i<n:
        r = l[i]+l[n]
        s+=r==k
        i+=(r<=k)
        n-=(r>=k)
    print(s)
    t-=1