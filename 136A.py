n = int(input())
l = list(map(int, input().split()))
p = [0] * n 
for i in range(n):
    p[l[i]-1] = i+1
print(*p)