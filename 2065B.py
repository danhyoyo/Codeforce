def giai(s):
    for i in range(0,len(s)-1):
        if(s[i]==s[i+1]): return 1
    return len(s)


t = int(input())
while t:
    s = input()
    print(giai(s))
    t -= 1