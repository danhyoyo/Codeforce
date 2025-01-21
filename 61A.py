a = input()
b = input()
c = ""
for i in range(len(a)):
    if a[i] != b[i] :
        c = c + '1'
    else: c = c + '0'
print(c)