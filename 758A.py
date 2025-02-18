n = int(input())
l = list(map(int, input().split()))
m, s = max(l), 0
for i in range(n):
   s += m-l[i] 
print(s)
