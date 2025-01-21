m, n = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
s = 0
for i in range(0,n):
    if l[i]<0: s-=l[i]
print(s)
