t = int(input())
while t:
    a, b = map(int, input().split())
    print(min(a,b), max(a,b))
    t-=1