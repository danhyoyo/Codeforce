t = int(input())
s = input()
m = 0
char = ""
for i in range(len(s)-1):
    p = s[i:i+2]
    c = 0
    for j in range(i, len(s)-1):
        q = s[j:j+2]
        if(p == q): c+=1
    if c > m:
        m = c 
        char = p  
print(char)
