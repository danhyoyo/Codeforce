t = int(input())
while t:
    l = list(map(int, input().split()))
    s = set({l[0]+l[1], l[2]-l[1], l[3]-l[2]})
    c = len(s)
    print(3-c+1)
    t-=1