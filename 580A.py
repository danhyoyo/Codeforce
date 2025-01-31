n = input()
s = list(map(int,input().split()))
c = 1
m = 1
for i in range(1,len(s)):
    if s[i]>=s[i-1]:
        c+=1
        if c>m :
            m =c 
    else: c=1
print(m)