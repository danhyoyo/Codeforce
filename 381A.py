n = int(input())
l = list(map(int,input().split()))
i, j= 0,len(l)-1
s,d = 0,0
turn = True
while i<=j:
    if l[i]>l[j]:
        choice = l[i]
        i+=1
    else:
        choice = l[j]
        j-=1
    if turn:
        s += choice
    else: d += choice
    turn = not turn

print(s,d)