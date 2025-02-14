n, k, l, c, d, p, nl, np = map(int, input().split())
ml = k*l
lime = c * d
print(min(ml//nl, lime, p//np)//n)