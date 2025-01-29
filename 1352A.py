t = int(input())
while t:
    n = input()
    c=n.count('0')
    print(len(n)-c)
    for i in range(len(n)):
        if n[i] != '0':
            print(n[i], '0'*(len(n)-i-1), sep = '', end = ' ')
    t-=1
