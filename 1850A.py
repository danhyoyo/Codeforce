t = int(input())
while t:
    l = sorted(list(map(int, input().split())))
    if (l[1]+l[2]>=10):
        print("YES")
    else: print("NO")
    t-=1