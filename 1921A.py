t = int(input())

while t:
    s = set()
    for _ in range(4):
        n, m = map(int, input().split())
        s.add(n)
    l = list(s)
    print((l[0]-l[1])**2)
    t-=1