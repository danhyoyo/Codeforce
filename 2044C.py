n = int(input())
while n>0:
    m, a, b, c = map(int, input().split())
    s = 0
    if a >= m: a = m
    else:
        a += c
        if(a-m>=0):
            c = a-m
            a = m
        else: c = 0
    if b >= m: b = m
    else:
        b += c
        if(b-m>=0):
            c = b-m
            b = m
        else: c = 0
    print(a+b)
    n-=1