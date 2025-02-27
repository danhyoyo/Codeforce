t = int(input())
while t:
    n, x, k = map(int, input().split())
    i, pos, c, j = 0, x, 0, 0
    s = input()
    l = len(s)
    check1, check2, b = 0, 0, True
    while i != k and j != l:
        i+=1
        if s[j] == 'L':
            pos -= 1
        elif s[j] == 'R':
            pos += 1
        if pos == 0:
            c+=1
            j = -1
        if c==1 and b:
            check1 = i
            b = False
        if c==2:
            check2 = i
            break
        j+=1
    if c<=1 :
        print(c)
    else:
        print(2+(k-check2)//(check2-check1))

    t-=1