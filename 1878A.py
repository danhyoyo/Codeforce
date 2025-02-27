t = int(input())
while t:
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    if k in s:
        print("YES")
    else: print("NO")
    t-=1