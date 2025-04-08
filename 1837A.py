t = int(input())
while t:
    x, k = map(int, input().split())
    if x % k != 0:
        print(1)
        print(x)
    else:
        print(2)
        print(x - 1, 1)
    t -= 1
