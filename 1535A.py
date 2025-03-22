t = int(input())
while t:
    l = list(map(int, input().split()))
    s = sorted(l)
    c = s[2:4]
    a, b = sorted(l[0:2]), sorted(l[2:4])
    #print(a,b,c)
    if a == c or b == c:
        print("NO")
    else:
        print("YES")
    t -= 1