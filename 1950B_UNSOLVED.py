t = int(input())
while t:
    n = int(input())
    c, b = 0, True
    for i in range(1,n+1):
        for j in range(0,n*2,2):
            if b:
                print("##", end = '')
                b = not b
            else:
                print("..", end = '')
                b = not b

        if n % 2 == 0:
            b = not b
        print()
        for j in range(0,n*2,2):
            if b:
                print("##", end = '')
                b = not b
            else:
                print("..", end = '')
                b = not b
        print()
        if i % 2 == 0:
            b = not b
    print()
    t -= 1