t = int(input())
while t:
    s = input()
    a = "abc"
    c = 0
    for i in range(3):
        if a[i]!=s[i]: c+=1
    if c==3:
        print("NO")
    else: print("YES")
    t-=1