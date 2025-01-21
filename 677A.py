n ,t = map(int, input().split())
l = list(map(int, input().split()))
s = 0
for i in l:
    if i > t: s += 1
print(n-s+s*2)
