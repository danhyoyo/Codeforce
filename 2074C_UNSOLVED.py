t = int(input())
while t:
    a = int(input())
    pos = -1
    for b in range(a-1, 0,-1):
        c = a^b
        if a+b>c and a+c>b and b+c>a:
            pos = b
            break
    print(pos)
    t-=1