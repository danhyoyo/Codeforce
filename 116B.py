r, c = map(int,input().split())
a = []
s = 0
for i in range(r):
    a.append(input())
for i in range(r):
    for j in range(c):
        if a[i][j] != 'W': continue
        for x,y in ((i, j+1), (i, j-1), (i-1, j), (i+1, j)):
            if 0<=x<r and 0<=y<c and a[x][y] == 'P': s+=1; break
print(s)
    
