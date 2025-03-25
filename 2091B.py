t = int(input())
while t:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    c = 0
    so =  0
    b = False
    a.sort(reverse=True)
    for i,j in enumerate(a):
        if j>=x:
            c+=1
        else:
            if not b:
                b = not b
                so = i
            else:
                if (i - so + 1) * min(a[so:i+1]) >= x:
                    c+=1
                    b = not b
    print(c)
    t-=1