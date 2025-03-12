t = int(input())
while t:
    a = set()
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    r = list(map(int, input().split()))
    for i in range(n):
        for j in range(x[i]-r[i], x[i]+r[i]+1):
            for k in range(0,r[i]+1):
                if (j - x[i]) ** 2 + (k ** 2) <= (r[i] ** 2):
                    a.add((j,k))
                    a.add((j,-k))
                    #print((j,k),(j,-k), end = ' ')
                else:
                    break
    print(len(a))
    t-=1
#if (j ** 2 + k ** 2) <= (r[i] ** 2):