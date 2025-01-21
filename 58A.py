s = input()
t = "hello"
j = 0
for c in s:
    if c == t[j]:
        j+=1
    if j == 5: break
if(j==5): print("YES")
else: print("NO")