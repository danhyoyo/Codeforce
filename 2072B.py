import math
t = int(input())
while t:
    n = int(input())
    s = input()
    duoi, tren = s.count('_'), s.count('-')
    print(duoi * ((math.ceil(tren/2)) * math.floor(tren/2)))
    t-=1