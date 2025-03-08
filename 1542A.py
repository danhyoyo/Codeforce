t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    c,s = 0,0
    for i in l:
        if i & 1 == 0:
            c += 1
        else: s += 1
    if c == s:
        print("Yes")
    else:
        print("No")
    t-=1