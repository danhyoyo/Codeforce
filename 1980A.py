t = int(input())
while t:
    n, m = map(int, input().split())
    s = input()
    a, c = [0]*7, 0
    for i in s:
        a[ord(i)-65]+=1
    for i in range(7):
        if a[i]>=m:
            c+=0
        else:
            c+= m-a[i]
    print(c)
    t-=1