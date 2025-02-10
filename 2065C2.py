def giai(n,l,m,l1):
    l[0] = min(min(l1)-l[0],l[0])
    if(sorted(l)==l): return "YES"
    for i in range(1, len(l)):
        o = l[i]
        for j in range(len(l1)):
            k = l[i]+1 
            if (l1[j]-l[i]>=l[i-1]):
                k = l1[j]-l[i]
            if k < o: o = k 
        l[i] = o
        if(sorted(l)==l): return "YES"
    return "NO"
t = int(input())
while t:
    n, m = map(int,input().split())
    l = list(map(int,input().split()))
    l1 = list(map(int,input().split()))

    print(giai(n,l,m,l1))
    t -= 1