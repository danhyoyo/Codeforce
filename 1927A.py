t = int(input())
while t:
    n = int(input())
    s = input()
    s1 = s[::-1]
    if 'B' in s:
        print(len(s) - s1.find('B') - s.find('B'))
    t-=1