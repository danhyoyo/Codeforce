from collections import Counter

t = int(input())
while t:
    n = int(input())
    l = dict(Counter(map(int, input().split())))
    print(*l.keys())
    t-=1
