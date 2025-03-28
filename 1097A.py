s = input()
a = list(map(str, input().split()))
b = False
for i in range(5):
    if a[i][0] in s or a[i][1] in s:
        b = True
        break
if b:
    print("YES")
else:
    print("NO")