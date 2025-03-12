t = int(input())
while t:
    l = set(list(map(int, input().split())))
    if len(l) == 1:
        print("Yes")
    else: print("No")
    t-=1