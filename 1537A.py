t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    s = sum(l)
    if s / len(l) >= 1:
        print(s - len(l))
    else:
        print(1)
    t-=1