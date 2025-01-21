n, m = map(int,input().split())
l = list(map(int, input().split()))
pos, dis = 1, 0
for i in l:
    if i >= pos: dis+=i-pos; pos = i
    else: dis += n-pos+i; pos = i 
print(dis)
