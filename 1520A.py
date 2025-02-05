def solve(s):
    se = set(s[0])
    pos = s[0]
    for i in range(len(s)):
        if s[i]!=pos:
            if s[i] not in se:
                se.add(s[i])
                pos = s[i]
            else: return "NO"
    return "YES"
t = int(input())
while t:
    n = int(input())
    s = input()
    print(solve(s))
    t-=1