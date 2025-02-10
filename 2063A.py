t = int(input())
while t:
    a, b= map(int, input().split())
    if( a == b == 1): print(1)
    else: print(abs(a-b))
    t-=1