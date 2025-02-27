t = int(input())
while t:
    n = int(input())
    a, b = (n//15)*3, n%15
    if b >= 2:
        a+=3
    elif b >= 1:
        a+=2
    elif b == 0:
        a+=1
    print(a)
    t-=1