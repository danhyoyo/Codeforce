n = int(input())
tong, s = 0, 0
while tong<=n:
    s+=1
    tong+=s*(s+1)/2
print(s-1)