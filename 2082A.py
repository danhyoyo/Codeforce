t = int(input())
while t:
    n,m = map(int,input().split())
    a = [list(map(int, input())) for i in range(n)]
    b = [[row[i] for row in a] for i in range(len(a[0]))]
    c, r = 0, 0
    for i in range(n):
        r += 1 if sum(a[i]) % 2 == 1 else 0
    for i in range(m):
        c += 1 if sum(b[i]) % 2 == 1 else 0
    print(max(r,c))
    t -= 1