t = int(input())
while t:
    n, m = map(int, input().split())
    print((23-n)*60+60-m)
    t-=1