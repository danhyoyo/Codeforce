t = int(input())
while t:
    a,b,c = map(int, input().split())
    d1, d2 = a, abs(b-c)+c
    if d1>d2:
        print(2)
    elif d2>d1:
        print(1)
    else:
        print(3)
    t-=1