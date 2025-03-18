t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = True
    for i in range(n-2):
        if a[i] == a[i+1] and a[i] == a[i+2]:
            print(a[i])
            b = False
            break
    if b:
        print(-1)
    t-=1
