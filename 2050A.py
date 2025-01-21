t = int(input())
def sol():
    n, m = map(int,input().split())
    count = 0
    sm = 0 
    for _ in range(0,n):
        s = input()
        sm += len(s)
        if (sm<=m): count += 1
    print(count)
for _ in range(t):
    sol()