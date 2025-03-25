t = int(input())
while t:
    n = int(input())
    a = []
    if n % 2 == 0:
        print(-1)
    else:
        for i in range(1,n+1,2):
            a.append(i)
        for i in range(2,n,2):
            a.append(i)
        print(*a)
    t-=1