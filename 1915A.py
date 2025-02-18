t = int(input())
while t:
    l = list(map(int, input().split()))
    l.sort()
    if (l.count(l[0])>l.count(l[2])):
        print(l[2])
    else: (print(l[0]))
    t-=1