t = int(input())
s = "codeforces"
while t:
    c = input()
    d = 0
    for i in range(10):
        if s[i]!=c[i]: d+=1
    print(d)
    t-=1