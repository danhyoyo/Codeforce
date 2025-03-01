t = int(input())
while t:
    n = input()
    
    if n >= n[0]*len(n):
        print(9*(len(n)-1)+int(n[0]))
    else: print(9*(len(n)-1)+int(n[0])-1)
    t-=1