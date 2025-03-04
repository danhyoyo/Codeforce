t = int(input())
while t:
    n = int(input())
    c, le = 0, 0
    l = list(map(int, input().split()))
    for i in l:
        if i % 2 == 0:
            c += 1
        else:
            le += 1
    if le == 0 or (le % 2 == 0 and c == 0):
        print("NO")
    else: print("YES")
    t-=1