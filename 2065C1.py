def giai(n,b,l):
    l[0] = min(l[0],b-l[0])
    for i in range(1, len(l)):
        if l[i]>b-l[i]:
            l[i] = b-l[i]
        if l[i]<l[i-1]:
            l[i] = b-l[i]
    if(sorted(l)==l): return "YES"
    return "NO"
t = int(input())
while t:
    n, m = map(int,input().split())
    l = list(map(int,input().split()))
    b = int(input())

    print(giai(n,b,l))
    t -= 1