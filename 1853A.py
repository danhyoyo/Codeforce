t = int(input())
while t:
    n, m = int(input()), 10**9
    l = list(map(int, input().split()))
    if sorted(l) != l:
        print(0)
    else:
        for i in range(1,n):
            m = min(m, (l[i]-l[i-1])//2+1)
        print(m)
    t-=1