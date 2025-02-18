t = int(input())
while t:
    n = int(input())
    s = 0
    for i in range(len(str(n))+1):
        s+=i
    print((n%10-1)*10+s)
    t-=1