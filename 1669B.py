from collections import Counter

t = int(input())
while t:
    n = int(input())
    l = list(dict(Counter(map(int, input().split()))).items())
    l.sort(key = lambda x: x[1])
    if l[len(l)-1][1] >=3:
        print(l[len(l)-1][0])
    else:
        print(-1)

    t-=1
