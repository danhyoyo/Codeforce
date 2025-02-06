import math
def isprime(n):
    if n<=2:
        return True
    else:
        for i in range(2, math.isqrt(n)+1):
            if n%i==0:
                return False
    return True
def check(n, m):
    if isprime(n) and isprime(m):
        for i in range(n+1,m):
            if isprime(i): return "NO"
        return "YES"
    else: return "NO"
n, m = map(int, input().split())
print(check(n, m))