t = int(input())
while t:
    a,b,c=sorted(map(int,input().split()))
    if a+b!=c: print("NO")
    else: print("YES")
    t-=1