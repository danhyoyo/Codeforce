n, l = map(int, input().split())
a = list(map(int, input().split()))
a.sort() #tang dan
min_distance = max(l-a[n-1], a[0])
for i in range(1,n):
    if (a[i] - a[i-1]) / 2  > min_distance:
        min_distance = (a[i] - a[i-1])/2
print(min_distance)
