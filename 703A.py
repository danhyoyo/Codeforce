t = int(input())
a, b = 0, 0
while t:
    c, d = map(int,input().split())
    if c>d:
        a+=1
    elif d>c:
        b+=1
    t-=1

if a>b:
    print("Mishka")
elif a==b:
    print("Friendship is magic!^^")
else:
    print("Chris")