t = int(input())
while t:
    n, k = (map(int, input().split()))
    print(1 + ((n-k)//(k-1)) + ((n-k)%(k-1) != 0))
    t-=1