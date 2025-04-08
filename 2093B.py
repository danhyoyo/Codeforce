t = int(input())
while t:
    n = input()
    z = n.count('0')
    c = 0
    so = 0
    for i in range(len(n)-1,-1,-1):
        if n[i] != '0':
            c = i
            break
    for i in range(0,c):
        if n[i] != '0':
            so +=1
    print(so+(len(n)-c-1))
    t-=1