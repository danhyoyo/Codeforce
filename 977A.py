a, b = map(int, input().split())
while b:
    if a%10==0: a/=10
    else: a-=1
    b-=1
print(int(a))