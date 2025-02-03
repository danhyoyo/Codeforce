n = int(input())
l = list(map(int,input().split()))
c = 0
ma, mi = l[0], l[0]
for i in range(1,n):
    if l[i]>ma:
        c+=1
        ma = l[i]
    elif l[i]<mi: 
        c+=1
        mi = l[i]
print(c)