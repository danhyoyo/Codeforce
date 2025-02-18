t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    a = [0]*101
    for i in range(n):
        a[l[i]]+=1
    print(l.index(a.index(1))+1)
    t-=1