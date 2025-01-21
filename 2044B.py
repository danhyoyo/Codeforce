t = int(input())
while t>0:
    s = input()
    for i in s[::-1]:
        if i == 'p':
            print('q', end = '')
        elif i =='q': print('p', end = '')
        else: print('w', end ='')
    print()
    t-=1