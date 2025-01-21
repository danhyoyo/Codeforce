n = int(input())
a = []
g = 1
for i in range(n):
    a.append(input())
for i in range(1,n):
    if a[i-1][1]==a[i][0]: g+=1
print(g)