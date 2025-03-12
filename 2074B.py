t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    print(sum(l)-(n-1))
    t-=1