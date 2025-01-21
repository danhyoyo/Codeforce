def ss(s1,s2):
    if len(s1) != len(s2): return "NO"
    for i in range(len(s1)):
        if s1[i] != s2[len(s1)-i-1]: return("NO")
    return ("YES")
s1 = input()
s2 = input()
print(ss(s1,s2))