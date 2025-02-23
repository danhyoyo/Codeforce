t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    cc, cl = 0, 0
    for i in range(n):
        if l[i]%2!=0:
            cl+=1
    if cl%2==0:
        print("YES")
    else: print("NO")
    t-=1
