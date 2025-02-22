n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
c = 0
for i in range(2,n,3):
    if l[i]+k<=5: c+=1
print(c)