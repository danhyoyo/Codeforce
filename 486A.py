import math
n = int(input())
if n % 2 == 0:
    print(int(-(1+n-1)*(n//2)//2+(2+n)*(n//2)//2))
else: print(int(-(1+n)*math.ceil(n/2)//2+(2+n-1)*math.floor(n/2)//2))
