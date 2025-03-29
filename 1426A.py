t = int(input())
while t:
    n,x = map(int, input().split())
    if n == 1 or n == 2:
        print(1)
    else:
        n-=2
        print((n-1)//(x)+2)
    t-=1