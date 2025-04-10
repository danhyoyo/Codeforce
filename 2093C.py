from math import isqrt
a = [2,3,5,7,11,13]
def check(n):
    if n == 1:
        return False
    for i in a:
        if n == i:
            return True
        if n % i == 0:
            return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True
t = int(input())
while t:
    x, k = map(int, input().split())
    if (check(x) and k == 1) or (x==1 and k == 2):
        print("YES")
    else:
        print("NO")
    t-=1