t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    m = [[x, l[x]] for x in range(n)]
    m.sort(key = lambda x: x[1])
    for i in range(n):
        j = n-1
        if m[j][0] == i:
            j-=1
        print(l[i] - m[j][1], end = ' ')
    print()
    t -= 1