import math
t = int(input())
while t:
    n = int(input())
    l = list(map(int,input().split()))
    ec = pose = 0

    for i in range(0,n):
        if l[i]%2==0:
            ec+=1
            if i%2==0:
                pose+=1
    if math.ceil(n/2) == ec:
        print(ec-pose)
    else: print(-1)
    t-=1