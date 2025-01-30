t = int(input())
while t:
    n = int(input())
    s = len(set(input().split()))
    if s == n:
        print("YES")
    else: print("NO")
    t-=1