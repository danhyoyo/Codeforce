def full(n,x):
    o = 0
    for i in range(0,n):
        o |= i
    if o == x:
        for i in range(0, n):
            print(i, end = ' ')
        print()
        return True
    return False

def thieu(n,x):
    a = []
    for i in range(0,n-1):
        if (i | x == x):
            a.append(i)
        else:
            break

    while len(a)!=n:
        a.append(x)
    for i in range(0, n):
        print(a[i], end=' ')
    print()

t = int(input())
while t:
    n, x = map(int, input().split())
    t-=1
    if not full(n,x):
        thieu(n,x)



# t = int(input())
# while t:
#     n, x = map(int, input().split())
#     c = 0
#     or_val = 0
#     for i in range(0, n-1):
#         if (i | x == x):
#             print(i, end = ' ')
#             c=i+1
#             or_val |= i
#         else:
#             break
#     b = c
#     if or_val|c == x:
#         while c != n:
#             print(b, end = ' ')
#             c+=1
#     else:
#         while c != n:
#             print(x, end = ' ')
#             c+=1
#     print()
#     t-=1