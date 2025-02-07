t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    mot, hai = l.count(1), l.count(2)
    if (mot != 0 and mot % 2 == 0) or (hai % 2 == 0 and mot == 0):
        print("YES")
    else: print("NO")
    t -= 