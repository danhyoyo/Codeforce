t = int(input())
while t:
    n, k = map(int,input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())), reverse = True)
    s = 0
    for i in range(n):
        if i<k:
            s += max(a[i],b[i])
        else: s += a[i]
    print(s)
    t -= 1