t = int(input())
while t:
    s = input()
    for i in range(0,len(s)-2):
        print(s[i],end='')
    print('i')
    t -= 1