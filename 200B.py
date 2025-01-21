n = int(input())
s = 0 
l = list(map(int, input().split()))
for _ in l:
    s += _
print(s/n)