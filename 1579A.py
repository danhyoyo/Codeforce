t = int(input())
while t:
    a = input()
    if (a.count('B') == a.count('A') + a.count('C')):
        print("YES")
    else:
        print("NO")
    t-=1