t = int(input())
while t:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    m = max(a[0], (x - a[n-1]) * 2)
    for i in range(1, n):
        m = max(m, a[i] - a[i-1])
    print(m)
    t -= 1
