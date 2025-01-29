n = int(input())
c = 0
while n:
    s = input()
    if s[0] == "T":
        c+=4
    elif s[0] == "C":
        c += 6 
    elif s[0] == "D":
        c += 12
    elif s[0] == "O":
        c += 8
    else: c += 20
    n-=1
print(c)