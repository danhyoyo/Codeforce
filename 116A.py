n = int(input())
s = 0
m = -1
while n:
    a, b = map(int, input().split())
    s += b - a
    if(s > m): m = s 
    n-=1
print(m)