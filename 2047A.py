t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    s = 0
    c = 0
    for i in l:
        s += i
        if s**(1/2) == int(s**(1/2)) and s**(1/2)%2 == 1: c+=1
    print(c)
    t-=1