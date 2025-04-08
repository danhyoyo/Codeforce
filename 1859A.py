t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[n-1]:
        print(-1)
    else:
        tmp = a.count(a[0])
        print(tmp, n-tmp)
        for i in range(tmp):
            print(a[0],end   = ' ')
        print()
        c = [a[i] for i in range(tmp,n)]
        print(*c)
    t -= 1
