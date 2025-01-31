n, m = map(int, input().split())
c = 0
for i in range(n):
    if i%2 == 0:
        print("#"*m)
    else:
        if c%2==0:
            print("."*(m-1), "#", sep = '')
        else: print("#", "."*(m-1), sep = '')
        c+=1