t = int(input())
while t:
    n = int(input())
    s = set(map(int,input().split()))
    if max(s)-min(s)>=len(s): print("NO")
    else: print("YES")
    t-=1

# t = int(input())
# while t:
#     b = True
#     n = int(input())
#     l = list(map(int,input().split()))
#     l.sort()
#     for i in range(1,len(l)):
#         if not(l[i]-l[i-1]<=1):
#             b = False
#     if b:
#         print("YES")
#     else: print("NO")
#     t-=1