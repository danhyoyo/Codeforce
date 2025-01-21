import math
from math import *
a ,b = map(int, input().split())
n = ceil(log(a/b,2/3))
if a*(3**n) == b*(2**n):
    print(n+1)
else: print(n)