def solve(s1,s2,n):
    for i in range(n):
        if s1[i] != s2[i]:
            if (s1[i] == 'R' or s2[i] == 'R'):
                return "NO"
    return "YES"

t = int(input())
while t:
    n = int(input())
    s1 = input()
    s2 = input()
    print(solve(s1,s2,n))
    t-=1