t = int(input())
l1 ,l2 = [], []
while t:
    a, b = map(int,input().split())
    l1.append(a)
    l2.append(b)
    t-=1
c = 0
for i in range(len(l1)):
    c+=l2.count(l1[i])
print(c)
