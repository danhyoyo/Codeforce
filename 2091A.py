t = int(input())
while t:
    s0,s1,s2,s3,s5 = 0,0,0,0,0
    n = int(input())
    a = list(map(int, input().split()))
    so = 0
    for j,i in enumerate(a):
        if i == 0:
            s0 +=1
        if i == 1:
            s1 += 1
        if i == 2:
            s2 += 1
        if i == 3:
            s3 += 1
        if i == 5:
            s5 += 1
        if s0 >= 3 and s1 >= 1 and s2 >= 2 and s3 >= 1 and s5 >= 1:
            so = j+1
            break
    print(so)
    t-=1