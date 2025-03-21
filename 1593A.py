t  = int(input())
while t:
	a = list(map(int,input().split()))
	b =[]
	m = max(a)
	for i in a:
		if a.count(i) == 1 and i == m:
			b.append(0)
		else:
			b.append(m-i+1)
	print(*b)
	t-=1