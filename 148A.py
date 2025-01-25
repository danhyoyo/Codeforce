q = int(input())
w = int(input())
e = int(input())
r = int(input())
d = int(input())
s=0
for i in range(1,d+1):
    if i%q == 0 or i%w == 0 or i%e == 0 or i%r == 0:
        s+=1
print(s)