t = int(input())
while t:
    n = int(input())
    s = set(map(int,input().split()))
    if max(s)-min(s)>=len(s): print("NO")
    else: print("YES")
    t-=1