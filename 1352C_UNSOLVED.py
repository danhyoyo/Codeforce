import math
t = int(input())
while t:
    n , k = map(int, input().split())
    a = math.ceil(k/n) 
    b = math.ceil(a/n)
    print(k+a+b)
    t-=1
   // https://codeforces.com/contest/1352/status/C?order=BY_ARRIVED_DESC