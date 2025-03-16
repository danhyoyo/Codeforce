t = int(input())
while t:
    n, k = map(int, input().split())
    x = input()
    s = input()
    c, b = 0, False

    while len(x) <= 200:
        if s in x:
            b = True
            break
        c += 1
        x += x
    if b:
        print(c)
    else:
        print(-1)
    t-=1