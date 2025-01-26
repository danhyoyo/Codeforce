n = int(input())
l = list(map(int, input().split()))
minn = min(l)
maxx = max(l)
c = 0
i = n-1
while l[i] != minn:
    i-=1
j = l.index(maxx)
if i>j: print(n-1-i + j)
else: print(n-1-i + j -1)