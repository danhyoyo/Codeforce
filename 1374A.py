t = int(input())
while t:
    x, y ,n =  map(int, input().split())
    print(n-(n-y)%x)
    t-=1