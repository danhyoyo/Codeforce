t = int(input())
while t:
    a,b = map(int,input().split())
    print(max(max(a,b),min(a,b)*2)**2)
    t-=1