t = int(input())
while t:
    n = int(input())
    ma , pos = 0, 0
    for i in range(2,n+1):
        j, s = 0, 0
        while (j<=n):
            s+=j
            j+=i
        if ma<s:
            ma = s
            pos = i
    print(pos)
    t-=1