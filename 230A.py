s, n = map(int,input().split())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append((x,y))
b = True
for i in sorted(a):
    if s > i[0]:
        s += i[1]
    else: b = False
if b: print("YES")
else: print("NO")
