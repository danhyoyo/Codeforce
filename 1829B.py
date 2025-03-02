t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    s, m = 0, 0
    for i in range(n):
        if l[i]==0:
            s+=1
        else:
            if s > m:
                m = s
            s = 0
    if s > m:
        m = s
    print(m)
    t-=1