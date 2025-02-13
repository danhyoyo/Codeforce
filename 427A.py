n = int(input())
l = list(map(int, input().split()))
s, c= 0, 0
for i in l:
    if i!=-1:
        s+=i
    else:
        if s!=0:
            s-=1
        else: c+=1
print(c)
