t = int(input())
while t:
    a = ['0','a','b','c','d','e','f','g','h']
    s = input()
    for i in range(1,9):
        if s[0] != a[i]:
            print(a[i],s[1], sep = '')
    for i in range(1,9):
        if int(s[1]) != i:
            print(s[0],i, sep = '')
    t-=1