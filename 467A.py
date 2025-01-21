t = int(input())
c = 0
while t:
    a, b = map(int, input().split())
    if b-a>=2: c+=1
    t -= 1
print(c)