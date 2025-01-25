n = int(input())
while n:
    a = int(input())
    if a%4!=0:
        print("NO")
    else:
        s = 0
        print("YES")
        for i in range(1, int(a/2+1)):
            print(2*i, end = ' ')
        for i in range(0, int(a/2-1)):
            print(2*i+1, end = ' ')
            s += 2*i+1
        print(int((2+a)*(a/4)-s))
    n-=1