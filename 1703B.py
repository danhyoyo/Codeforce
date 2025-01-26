t = int(input())
while t:
    n = int(input())
    s = list(input())
    s.sort()
    a = s[0]
    c = 2
    for i in range(1,n):
        if s[i] == a:
            c+=1
        else:
            a = s[i]
            c += 2
    print(c)
    t-=1