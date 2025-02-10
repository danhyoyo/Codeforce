t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    l[l.index(min(l))]+=1
    ans = 1
    for i in l: ans*=i  
    print(ans)
    t -= 1