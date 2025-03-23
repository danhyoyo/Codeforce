c = []
n,q = map(int,input().split())
a = list(map(int,input().split()))
for i in range(q):
    l,r = map(int, input().split())
    c.append([l,r])
cd = [0]*(n+1)
cd[1] = a[0]
for i in range(2,n+1):
    cd[i] = cd[i-1] + a[i-1]
#print(cd)
for i in range(q):
    l, r = c[i][0], c[i][1]
    m = 10**12
    for j in range(l,r):
        #print(abs(cd[j]-cd[l-1] - (cd[r]-cd[j])), end = " ")
        m = min(m, abs(cd[j]-cd[l-1] - (cd[r]-cd[j])))
    print(m)