import math
t = int(input())
while t:
    a, b = map(int, input().split())
    print(math.ceil(abs(a-b)/10))
    t -= 1