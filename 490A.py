n = int(input())
l = list(map(int,input().split()))
a = [[0],[0],[0],[0]]
for i in range(n):
    a[l[i]].append(i+1)
    a[l[i]][0] += 1
m = min(a[1][0],a[2][0],a[3][0])
if m > 0:
    print(m)
    for i in range(1,m+1):
        print(a[1][i],a[2][i],a[3][i])
else: print(0)