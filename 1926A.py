t = int(input())
while t:
    s = input()
    if s.count('A') > s.count('B'):
        print('A')
    else: print('B')
    t-=1