t = int(input())
while t:
    l = list(map(int, input().split()))
    x = l[0]
    l = sorted(l, reverse = True)
    print(l.index(x))
    t-=1