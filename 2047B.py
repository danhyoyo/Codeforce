t = int(input())
while t:
    n = int(input())
    s = input()
    freq = {}
    for i in s:
        freq[i] = freq.get(i, 0) + 1 
    l = list(freq.values())
    l.sort()
    print(l)
    t-=1