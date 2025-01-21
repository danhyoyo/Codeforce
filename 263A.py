r = 0
c = 0
for i in range (1,6):
    columnp = 0
    lit = list(map(int, input().split()))
    for j in lit:
        columnp += 1
        if j == 1:
            r = i
            c = columnp
            break
        else:
            continue
print(r, c)
        
print (abs(r-3)+ abs(c-3))