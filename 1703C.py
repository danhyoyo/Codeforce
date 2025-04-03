t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        b, s = input().split()
        b = int(b)
        for j in range(b):
            if s[j] == 'D':
                a[i] += 1
                if a[i] == 10:
                    a[i] = 0
            else:
                a[i] -= 1
                if a[i] == -1:
                    a[i] = 9
    for i in a:
        print(i, end = ' ')
    print()
    t-=1