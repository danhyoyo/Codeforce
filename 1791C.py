t = int(input())
while t:
    n = int(input())
    s = input()
    c = 0
    for i in range(0,n//2):
        if s[i] == s[n-i-1]:
            break
        else:
            c += 1
    print(n-(c*2))
    t -= 1